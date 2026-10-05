#!/usr/bin/env python3
"""Byte-level BPE tokenizer for the Z1 K2 model, built from its GGUF metadata block.

Why this exists
---------------
The context-window extrapolation in the Z1-A report needs a token count for the
rendered prompt at module counts the experiment never ran. Z1-T counted tokens by
asking the Ollama server itself (`prompt_eval_count` at `num_predict: 1`) -- the
most faithful source there is, but a model call. Z1-A must not call a model, so
the counting is reconstructed from the *same* model file: vocabulary, merges and
the pre-tokenizer id come out of the GGUF metadata block that Ollama loaded.

Nothing is downloaded, no model runs, and the model store is only ever read.

The reconstruction is worth nothing unless it reproduces measurements that are
already on record. `gates()` checks it against four archived numbers (Z1 protocol
section 3.3 (6), `z1_t_bericht_kontextfenster.md` section 1.1, `data/z1/MANIFEST.md`);
`evaluate_z1.py` refuses to state the extrapolation when a gate fails.

Two provisos, stated rather than hidden:

* `\\p{L}` / `\\p{N}` in the qwen2 pre-tokenizer pattern are rendered as `[A-Za-z]`
  / `[0-9]`. That is exact for the prompt at hand (pure ASCII, verified by
  `assert_ascii`) and would be wrong for other text.
* The chat template is applied in the shape Ollama's own template layer produces
  for one system plus one user message; `render_chat` carries that shape and the
  gates check it.
"""

from __future__ import annotations

import functools
import json
import re
import struct
from pathlib import Path

DEFAULT_STORE = Path("/usr/share/ollama/.ollama/models")
DEFAULT_MODEL = "registry.ollama.ai/library/qwen2.5-coder/7b"
MODEL_LAYER = "application/vnd.ollama.image.model"

# GGUF value types (gguf spec v3).
T_U8, T_I8, T_U16, T_I16, T_U32, T_I32, T_F32, T_BOOL, T_STR, T_ARR, T_U64, T_I64, T_F64 = range(13)
_FMT = {T_U8: "<B", T_I8: "<b", T_U16: "<H", T_I16: "<h", T_U32: "<I", T_I32: "<i",
        T_F32: "<f", T_BOOL: "<?", T_U64: "<Q", T_I64: "<q", T_F64: "<d"}

# llama.cpp LLAMA_VOCAB_PRE_TYPE_QWEN2, with the two Unicode classes spelled ASCII.
QWEN2_SPLIT = (
    r"(?:'[sS]|'[tT]|'[rR][eE]|'[vV][eE]|'[mM]|'[lL][lL]|'[dD])"
    r"|[^\r\nA-Za-z0-9]?[A-Za-z]+"
    r"|[0-9]"
    r"| ?[^\sA-Za-z0-9]+[\r\n]*"
    r"|\s*[\r\n]+"
    r"|\s+(?!\S)"
    r"|\s+"
)


class TokenizerUnavailable(RuntimeError):
    """The model store is not readable, so no extrapolation can be stated."""


class _Reader:
    def __init__(self, handle) -> None:
        self.handle = handle

    def raw(self, n: int) -> bytes:
        buf = self.handle.read(n)
        if len(buf) != n:
            raise TokenizerUnavailable("truncated GGUF header")
        return buf

    def scalar(self, kind: int):
        fmt = _FMT[kind]
        return struct.unpack(fmt, self.raw(struct.calcsize(fmt)))[0]

    def string(self) -> str:
        return self.raw(self.scalar(T_U64)).decode("utf-8", "replace")

    def value(self, kind: int):
        if kind == T_STR:
            return self.string()
        if kind == T_ARR:
            elem = self.scalar(T_U32)
            count = self.scalar(T_U64)
            if elem == T_STR:
                return [self.string() for _ in range(count)]
            fmt = _FMT[elem]
            buf = self.raw(struct.calcsize(fmt) * count)
            return list(struct.unpack("<" + fmt[1] * count, buf))
        return self.scalar(kind)


def read_gguf_metadata(path: Path) -> dict:
    """Read a GGUF file's metadata key/value block; tensor data is never touched."""
    with path.open("rb") as handle:
        reader = _Reader(handle)
        if reader.raw(4) != b"GGUF":
            raise TokenizerUnavailable(f"not a GGUF file: {path}")
        reader.scalar(T_U32)  # format version
        reader.scalar(T_U64)  # tensor count
        count = reader.scalar(T_U64)
        return {(_k := reader.string()): reader.value(reader.scalar(T_U32)) for _ in range(count)}


def resolve_model_blob(store: Path = DEFAULT_STORE, model: str = DEFAULT_MODEL) -> tuple[Path, str]:
    """Return (GGUF blob path, manifest digest) for one Ollama model tag."""
    manifest_path = store / "manifests" / model
    if not manifest_path.exists():
        raise TokenizerUnavailable(f"no Ollama manifest at {manifest_path}")
    import hashlib

    manifest_digest = hashlib.sha256(manifest_path.read_bytes()).hexdigest()
    manifest = json.loads(manifest_path.read_text())
    for layer in manifest["layers"]:
        if layer["mediaType"] == MODEL_LAYER:
            blob = store / "blobs" / layer["digest"].replace(":", "-")
            if not blob.exists():
                raise TokenizerUnavailable(f"model blob missing: {blob}")
            return blob, manifest_digest
    raise TokenizerUnavailable("manifest carries no model layer")


def bytes_to_unicode() -> dict[int, str]:
    """GPT-2's reversible byte<->printable-codepoint map (byte-level BPE)."""
    printable = list(range(ord("!"), ord("~") + 1)) + list(range(0xA1, 0xAD)) + list(range(0xAE, 0x100))
    mapped = printable[:]
    spill = 0
    for byte in range(256):
        if byte not in printable:
            printable.append(byte)
            mapped.append(256 + spill)
            spill += 1
    return dict(zip(printable, (chr(c) for c in mapped)))


class Tokenizer:
    """Counts tokens exactly as the loaded model's own tokenizer does."""

    def __init__(self, store: Path = DEFAULT_STORE, model: str = DEFAULT_MODEL) -> None:
        self.blob, self.manifest_digest = resolve_model_blob(store, model)
        meta = read_gguf_metadata(self.blob)
        if meta.get("tokenizer.ggml.model") != "gpt2" or meta.get("tokenizer.ggml.pre") != "qwen2":
            raise TokenizerUnavailable(
                "unexpected tokenizer flavour: "
                f"{meta.get('tokenizer.ggml.model')!r}/{meta.get('tokenizer.ggml.pre')!r}"
            )
        self.meta = {k: v for k, v in meta.items() if not isinstance(v, list)}
        self.tokens: list[str] = meta["tokenizer.ggml.tokens"]
        self.ids = {tok: i for i, tok in enumerate(self.tokens)}
        self.rank = {tuple(m.split(" ")): i for i, m in enumerate(meta["tokenizer.ggml.merges"])}
        self.byte_map = bytes_to_unicode()
        self.pattern = re.compile(QWEN2_SPLIT)
        # token_type 3 = CONTROL, 4 = USER_DEFINED; both are matched whole.
        special = [t for t, ty in zip(self.tokens, meta["tokenizer.ggml.token_type"]) if ty in (3, 4)]
        self.special = set(special)
        self.special_re = re.compile("(" + "|".join(re.escape(s) for s in sorted(special, key=len, reverse=True)) + ")")

    @functools.lru_cache(maxsize=None)
    def _merge(self, word: str) -> tuple[str, ...]:
        parts = list(word)
        while len(parts) > 1:
            best_rank, best_at = None, None
            for i in range(len(parts) - 1):
                rank = self.rank.get((parts[i], parts[i + 1]))
                if rank is not None and (best_rank is None or rank < best_rank):
                    best_rank, best_at = rank, i
            if best_at is None:
                break
            parts[best_at:best_at + 2] = [parts[best_at] + parts[best_at + 1]]
        return tuple(parts)

    def _encode_plain(self, text: str) -> list[int]:
        out: list[int] = []
        for chunk in self.pattern.findall(text):
            mapped = "".join(self.byte_map[b] for b in chunk.encode("utf-8"))
            out.extend(self.ids[piece] for piece in self._merge(mapped))
        return out

    def encode(self, text: str, *, parse_special: bool = True) -> list[int]:
        if not parse_special:
            return self._encode_plain(text)
        out: list[int] = []
        for part in self.special_re.split(text):
            if not part:
                continue
            if part in self.special:
                out.append(self.ids[part])
            else:
                out.extend(self._encode_plain(part))
        return out

    def count(self, text: str, *, parse_special: bool = True) -> int:
        return len(self.encode(text, parse_special=parse_special))


def assert_ascii(text: str, what: str) -> None:
    """The ASCII proviso of QWEN2_SPLIT, checked rather than assumed."""
    if not text.isascii():
        raise TokenizerUnavailable(f"{what} is not pure ASCII; the ASCII split pattern would be wrong")


def split_prompt_file(text: str) -> list[tuple[str, str]]:
    """Undo `run_logger._render_prompt`: '### <role>\\n<content>' joined by '\\n\\n'."""
    messages: list[tuple[str, str]] = []
    for i, block in enumerate(text.split("\n\n### ")):
        head = block[len("### "):] if i == 0 else block
        role, _, content = head.partition("\n")
        messages.append((role, content))
    return messages


def render_chat(messages: list[tuple[str, str]]) -> str:
    """Apply the ChatML shape of Ollama's own template layer for this model."""
    out = "".join(f"<|im_start|>system\n{c}<|im_end|>\n" for r, c in messages if r == "system")
    out += "".join(f"<|im_start|>{r}\n{c}<|im_end|>\n" for r, c in messages if r != "system")
    return out + "<|im_start|>assistant\n"


def gates(tok: Tokenizer, z1_root: Path) -> list[dict]:
    """Check the reconstruction against four already-archived Ollama counts."""
    first = z1_root / "k2" / "run0" / "extractor" / "attempts" / "attempt_0" / "prompt.txt"
    old2 = z1_root / "k2_trunkiert" / "run0" / "extractor" / "attempts" / "attempt_2" / "prompt.txt"
    raw_first = first.read_text(encoding="utf-8")
    assert_ascii(raw_first, "the archived attempt_0 prompt")
    results = [
        {"gate": "G1", "was": "attempt_0/prompt.txt mit Chat-Template",
         "soll": 4281, "ist": tok.count(render_chat(split_prompt_file(raw_first))),
         "quelle": "Z1-Protokoll §3.3 (6)"},
        {"gate": "G2", "was": "dieselbe Datei ohne Template",
         "soll": 4274, "ist": tok.count(raw_first),
         "quelle": "z1_t_bericht_kontextfenster.md §1.1"},
        {"gate": "G3", "was": "k2_trunkiert attempt_2 ohne Template",
         "soll": 6010, "ist": tok.count(old2.read_text(encoding="utf-8")),
         "quelle": "Z1-Protokoll §3.3 (6), Tabelle"},
    ]
    triple = [
        tok.count(render_chat(split_prompt_file(
            (z1_root / "k2" / "run0" / "extractor" / "attempts" / f"attempt_{n}" / "prompt.txt")
            .read_text(encoding="utf-8"))))
        for n in (0, 1, 2)
    ]
    results.append({"gate": "G4", "was": "die drei Versuchsprompts des Blocks k2/, mit Template",
                    "soll": [4281, 5483, 6685], "ist": triple,
                    "quelle": "data/z1/MANIFEST.md (= usage.prompt_tokens der Artefakte)"})
    for row in results:
        row["ok"] = row["ist"] == row["soll"]
    return results
