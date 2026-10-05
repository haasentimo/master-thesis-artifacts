#!/usr/bin/env python3
"""P3 -- the delivery assurance for Z1 condition K2 (protocol section 5.3, Rev. 3).

WHAT THIS IS AND WHAT IT IS NOT
-------------------------------
P1 and P2 (in `tools/run_z1.py`) secure the ANSWER: they put the raw response
against the parsed model. Neither can see whether the model ever received the
whole QUESTION. On 2026-08-31 exactly that happened: of the 4281 tokens of the
rendered prompt, 2050 arrived -- the Ollama server truncated the rest away
without an error, without a log line and with HTTP 200. P3 secures the DELIVERY.

This checker is READ-ONLY over the archive and repairs nothing. It calls the
model exactly once, for the cold probe, with `max_tokens: 1` -- that is a
measurement of the delivery, not a run: no extractor, no schema, no retry loop,
and nothing it produces enters `data/z1/`.

`tools/run_z1.py` is NOT touched. P3 sits at the artifact boundary, like P1/P2.

THE THREE PARTS (protocol section 5.3, amendment Rev. 3)
--------------------------------------------------------
    P3a  COLD PROBE, before the invocation. The model instance is unloaded
         (`ollama stop`), then the registered rendered prompt goes over the SAME
         endpoint the measurement uses (`/v1/chat/completions`, `max_tokens: 1`);
         `usage.prompt_tokens` must land in the registered band.
         Cold, because Ollama reports `prompt_eval_count` -- NEWLY evaluated
         tokens. A warm KV-cache prefix lowers the number legitimately (measured:
         attempt_1 reports 1065 after attempt_0's 2050, on a LONGER conversation).
         On a cold instance that ambiguity does not exist.
    P3b  WINDOW WITNESS. `ollama ps`, column CONTEXT, raw output, before and
         after the invocation. Must read the registered window.
    P3c  BYTE WITNESS. SHA256 of `attempts/attempt_0/prompt.txt` of every
         archived run against the registered rendering.

Every deviation is a STOP, never a warning: before the invocation the run is not
started, after it the run is treated per protocol section 5.4.

INVOCATION
----------
    python3 tools/check_z1_delivery.py --pre           # P3b + P3a, before the runs
    python3 tools/check_z1_delivery.py --post data/z1/k2   # P3b + P3c, after them
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]

# --- what protocol sections 3.3 (6) and 5.3 registered ----------------------------------

MODEL = "qwen2.5-coder:7b"
ENDPOINT = "http://localhost:11434/v1/chat/completions"

REGISTERED_CONTEXT = 16384          # section 3.3 (6), OLLAMA_CONTEXT_LENGTH
TOKENS_REFERENCE = 4281             # section 5.3 P3a, measured 2026-08-31
TOKENS_MIN, TOKENS_MAX = 4260, 4302 # reference +- 0.5 %, two-sided

# The rendered prompt of the registered condition: prompt blob 6c8e4639... over
# fixtures/rich_repo. Byte-identical in the June runs and in those of 2026-08-31.
PROMPT_SHA256 = "cb2fcefddbbb1f2e81c62bc4b4231b458d12bfcc0948d3764dad7f287db0ee2d"
PROMPT_SOURCE = REPO / "data/z1/k2_trunkiert/run0/extractor/attempts/attempt_0/prompt.txt"

SYSTEM_MARK, USER_MARK = "### system\n", "\n### user\n"


class Fail(RuntimeError):
    """A registered stop condition. Never a warning, never a fallback."""


def say(*parts: object) -> None:
    print(*parts, flush=True)


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def registered_messages() -> list[dict[str, str]]:
    """Split the archived rendering back into the two messages that were sent.

    The archived file is the extractor's own rendering: `### system`, the system
    text, `### user`, the user text. Its hash is checked BEFORE it is used --
    a probe against an unverified prompt would prove nothing.
    """
    if not PROMPT_SOURCE.exists():
        raise Fail(f"Referenzprompt fehlt: {PROMPT_SOURCE.relative_to(REPO)}")
    got = sha256_file(PROMPT_SOURCE)
    if got != PROMPT_SHA256:
        raise Fail(f"Referenzprompt trägt nicht den registrierten SHA256.\n"
                   f"  ist  {got}\n  soll {PROMPT_SHA256}")
    raw = PROMPT_SOURCE.read_text(encoding="utf-8")
    if not raw.startswith(SYSTEM_MARK) or USER_MARK not in raw:
        raise Fail("Referenzprompt trägt nicht die erwarteten Marken `### system`/`### user`.")
    body = raw[len(SYSTEM_MARK):]
    cut = body.index(USER_MARK)
    return [{"role": "system", "content": body[:cut]},
            {"role": "user", "content": body[cut + len(USER_MARK):]}]


# --- P3b: the window witness ------------------------------------------------------------


def ollama_ps() -> str:
    out = subprocess.run(["ollama", "ps"], capture_output=True, text=True)
    if out.returncode != 0:
        raise Fail(f"`ollama ps` scheiterte: {out.stderr.strip()}")
    return out.stdout.rstrip("\n")


def context_of(ps_output: str) -> int | None:
    """The CONTEXT column of the resident instance, or None if none is loaded.

    The column carries a resident instance only -- that is a property of the
    tool, not a defect: with no instance loaded there is nothing to witness.
    """
    lines = [ln for ln in ps_output.splitlines() if ln.strip()]
    for line in lines[1:]:
        if not line.startswith(MODEL):
            continue
        for field in line.split():
            if field.isdigit() and int(field) >= 512:
                return int(field)
    return None


def p3b(label: str, *, required: bool) -> dict[str, object]:
    ps = ollama_ps()
    say(f"  (P3b) Fensterzeuge {label} -- `ollama ps`, Rohausgabe:")
    for line in ps.splitlines():
        say(f"        {line}")
    ctx = context_of(ps)
    if ctx is None:
        if required:
            raise Fail("Keine residente Instanz -- das geladene Fenster ist nicht bezeugt. "
                       "Nach dem ersten Call erneut messen (Methode C5 Schritt 3b).")
        say("        keine residente Instanz -- Messung nach dem ersten Call zu wiederholen")
        return {"context": None, "roh": ps}
    say(f"        CONTEXT = {ctx} · registriert {REGISTERED_CONTEXT}")
    if ctx != REGISTERED_CONTEXT:
        raise Fail(f"Geladenes Fenster {ctx} weicht vom registrierten Wert "
                   f"{REGISTERED_CONTEXT} ab (§3.3 (6)). ABBRUCH.")
    return {"context": ctx, "roh": ps}


# --- P3a: the cold delivery probe -------------------------------------------------------


def unload() -> None:
    out = subprocess.run(["ollama", "stop", MODEL], capture_output=True, text=True)
    if out.returncode != 0:
        raise Fail(f"`ollama stop {MODEL}` scheiterte: {out.stderr.strip()}")


def p3a() -> dict[str, object]:
    messages = registered_messages()
    say(f"  (P3a) Liefersonde · Referenzprompt {PROMPT_SHA256[:12]}… "
        f"({PROMPT_SOURCE.relative_to(REPO)})")
    unload()
    say("        Instanz entladen (`ollama stop`) -- die Sonde läuft kalt, damit kein "
        "Cache-Präfix die Zahl senkt")
    body = json.dumps({"model": MODEL, "messages": messages,
                       "temperature": 0, "seed": 0, "max_tokens": 1}).encode()
    req = urllib.request.Request(ENDPOINT, data=body, method="POST", headers={
        "Content-Type": "application/json", "Authorization": "Bearer ollama"})
    try:
        with urllib.request.urlopen(req, timeout=900) as resp:
            payload = json.loads(resp.read())
    except urllib.error.URLError as exc:
        raise Fail(f"Liefersonde scheiterte am Endpunkt: {exc}") from exc
    tokens = int(payload.get("usage", {}).get("prompt_tokens", -1))
    say(f"        usage.prompt_tokens = {tokens} · Referenz {TOKENS_REFERENCE} · "
        f"zulässig {TOKENS_MIN}–{TOKENS_MAX}")
    if not TOKENS_MIN <= tokens <= TOKENS_MAX:
        verb = "unterschreitet" if tokens < TOKENS_MIN else "überschreitet"
        raise Fail(f"Gemeldete Prompt-Tokenzahl {tokens} {verb} das zulässige Band "
                   f"{TOKENS_MIN}–{TOKENS_MAX} (§5.3 P3a). "
                   + ("Der Prompt kommt nicht vollständig an -- der Lauf wird NICHT "
                      "gestartet." if tokens < TOKENS_MIN else
                      "Gesendet wurde nicht der registrierte Prompt -- der Lauf wird "
                      "NICHT gestartet."))
    return {"prompt_tokens": tokens, "referenz": TOKENS_REFERENCE,
            "band": [TOKENS_MIN, TOKENS_MAX], "prompt_sha256": PROMPT_SHA256}


# --- P3c: the byte witness over an archived block ----------------------------------------


def p3c(block: Path) -> dict[str, object]:
    if not block.exists():
        raise Fail(f"Block fehlt: {block}")
    slots = sorted(p for p in block.iterdir() if p.is_dir())
    if not slots:
        raise Fail(f"Block {block.relative_to(REPO)} enthält keinen Lauf.")
    say(f"  (P3c) Bytezeuge über {len(slots)} Läufe in {block.relative_to(REPO)}:")
    out: dict[str, object] = {}
    bad: list[str] = []
    for slot in slots:
        first = slot / "extractor/attempts/attempt_0/prompt.txt"
        if not first.exists():
            bad.append(f"{slot.name}: attempt_0/prompt.txt fehlt")
            continue
        got = sha256_file(first)
        out[slot.name] = got
        mark = "OK " if got == PROMPT_SHA256 else "FEHL"
        say(f"        {mark} {slot.name}  {got[:16]}…")
        if got != PROMPT_SHA256:
            bad.append(f"{slot.name}: {got}")
    if bad:
        raise Fail("Erstprompt weicht vom registrierten Rendering ab (§5.3 P3c):\n  "
                   + "\n  ".join(bad))
    return out


# --- entry point -------------------------------------------------------------------------


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--pre", action="store_true",
                        help="P3b und P3a vor der Invocation")
    parser.add_argument("--post", metavar="BLOCK",
                        help="P3b und P3c über einen archivierten Block")
    args = parser.parse_args()
    record: dict[str, object] = {}
    try:
        if args.pre:
            say("=== P3 vor der Invocation (Protokoll §5.3, Rev. 3)")
            record["p3a"] = p3a()
            record["p3b_nach_sonde"] = p3b("nach der Sonde", required=True)
        elif args.post:
            say("=== P3 nach der Invocation (Protokoll §5.3, Rev. 3)")
            record["p3b"] = p3b("nach dem Lauf", required=True)
            record["p3c"] = p3c(Path(args.post).resolve())
        else:
            parser.print_help()
            return 0
    except Fail as exc:
        say("")
        say("ABBRUCH (P3):")
        for line in str(exc).splitlines():
            say(f"  {line}")
        return 1
    say("")
    say("P3 ERFÜLLT")
    say(json.dumps(record, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
