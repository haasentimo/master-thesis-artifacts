#!/usr/bin/env python3
"""Read the SERVER-REPORTED prompt token count of a chat request (Z2 protocol §3b (a)).

WHAT THIS IS AND WHAT IT IS NOT
-------------------------------
§3b (a) replaced `tools/z1_tokenizer.py` as the measuring instrument of the size
rule: the primary quantity is the count the SERVER reports (`usage.prompt_tokens`
/ `prompt_eval_count`) on a cold call with `max_tokens: 1` against the local
endpoint -- the same way Z1-T measured and `tools/check_z1_delivery.py` counts.

This tool DOES NOT COUNT. It sends one request and reads back what the server
says. It is therefore NOT `tools/z2_tokenizer.py` (§3b (d)) and does not replace
it: that future tool has to produce an expected count WITHOUT a model call, for
the delivery assurance in S4.

A call made with this tool is an INSTRUMENT MEASUREMENT, not a Z2 run (§3b (a)):
it counts against no Z2 budget, it is not archived as a run, and the model's
output is neither read nor judged. `choices[*].message.content` is discarded
unread -- the tool never returns it, never prints it and never stores it.

The context window is READ, never set: `--context-file` points at the systemd
drop-in that configures the running service. Changing the window is a manual,
privileged act outside this tool.

INVOCATION
----------
    python3 tools/measure_prompt_tokens.py \
        --id M1 --purpose "Basismessung" \
        --message user:text:x

    python3 tools/measure_prompt_tokens.py \
        --id M3 --purpose "Messgegenstand" \
        --message user:file:data/z2/eingaben/ist_modell.yaml \
        --out /tmp/m3.json

Each `--message` is `ROLE:file:PATH` or `ROLE:text:LITERAL`; the order of the
options is the order of the messages sent.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import time
import urllib.error
import urllib.request
from pathlib import Path

MODEL = "qwen2.5-coder:7b"
ENDPOINT = "http://localhost:11434/v1/chat/completions"
CONTEXT_FILE = "/etc/systemd/system/ollama.service.d/context.conf"
CONTEXT_KEY = "OLLAMA_CONTEXT_LENGTH"


class Fail(RuntimeError):
    """A stop condition. Never a warning, never a fallback."""


def sha256_bytes(blob: bytes) -> str:
    return hashlib.sha256(blob).hexdigest()


def parse_message(spec: str) -> dict[str, object]:
    """Turn `ROLE:file:PATH` / `ROLE:text:LITERAL` into a message plus its witness.

    The witness carries the SHA256 and the byte size of exactly what is sent, so
    the measured text is identifiable afterwards (§3b (a): "SHA256 des gemessenen
    Textes").
    """
    role, _, rest = spec.partition(":")
    kind, _, value = rest.partition(":")
    if role not in {"system", "user", "assistant"} or kind not in {"file", "text"}:
        raise Fail(f"Nachrichtenangabe unlesbar: {spec!r} "
                   f"(erwartet ROLE:file:PATH oder ROLE:text:LITERAL)")
    if kind == "file":
        path = Path(value)
        if not path.exists():
            raise Fail(f"Nutzlastdatei fehlt: {path}")
        blob = path.read_bytes()
        content = blob.decode("utf-8")
        source: dict[str, object] = {"art": "datei", "pfad": str(path)}
    else:
        content = value
        blob = content.encode("utf-8")
        source = {"art": "literal", "literal": content}
    source.update(bytes=len(blob), sha256=sha256_bytes(blob))
    return {"message": {"role": role, "content": content},
            "witness": {"rolle": role, **source}}


def read_context_window(path: str) -> dict[str, object]:
    """Read the configured window from the systemd drop-in. Never sets it."""
    conf = Path(path)
    if not conf.exists():
        return {"quelle": str(conf), "wert": None,
                "hinweis": "Drop-in nicht vorhanden -- Fenster nicht ablesbar"}
    for line in conf.read_text(encoding="utf-8").splitlines():
        if CONTEXT_KEY in line:
            raw = line.split(CONTEXT_KEY, 1)[1].lstrip("=").strip().strip('"')
            if raw.isdigit():
                return {"quelle": str(conf), "wert": int(raw)}
    return {"quelle": str(conf), "wert": None,
            "hinweis": f"{CONTEXT_KEY} im Drop-in nicht gefunden"}


def measure(messages: list[dict[str, str]], *, model: str, endpoint: str,
            timeout: int) -> dict[str, int]:
    """One call, `max_tokens: 1`, no `response_format`. Reads `usage` only."""
    body = json.dumps({"model": model, "messages": messages,
                       "temperature": 0, "max_tokens": 1}).encode()
    req = urllib.request.Request(endpoint, data=body, method="POST",
                                 headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            payload = json.loads(resp.read())
    except urllib.error.URLError as exc:
        raise Fail(f"Aufruf scheiterte am Endpunkt {endpoint}: {exc}") from exc
    usage = payload.get("usage")
    if not isinstance(usage, dict):
        raise Fail("Antwort trägt kein `usage` -- keine serverseitige Tokenzahl. "
                   "Die Messung gilt als nicht erfolgt.")
    prompt_tokens = usage.get("prompt_tokens")
    if not isinstance(prompt_tokens, int) or prompt_tokens == 0:
        raise Fail(f"`usage.prompt_tokens` ist {prompt_tokens!r} -- "
                   "keine brauchbare Zahl. Die Messung gilt als nicht erfolgt.")
    completion = usage.get("completion_tokens")
    # `choices[*].message.content` is deliberately NOT touched: the output of an
    # instrument measurement is not read and not judged (§3b (a)).
    return {"prompt_tokens": prompt_tokens,
            "completion_tokens": completion if isinstance(completion, int) else None}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--message", action="append", required=True, metavar="SPEC",
                        help="ROLE:file:PATH oder ROLE:text:LITERAL, in Sendereihenfolge")
    parser.add_argument("--id", required=True, help="Kennung der Messung, z. B. M1")
    parser.add_argument("--purpose", default="", help="Zweck der Messung, ein Satz")
    parser.add_argument("--model", default=MODEL)
    parser.add_argument("--endpoint", default=ENDPOINT)
    parser.add_argument("--context-file", default=CONTEXT_FILE,
                        help="systemd-Drop-in, aus dem das Fenster GELESEN wird")
    parser.add_argument("--timeout", type=int, default=900)
    parser.add_argument("--out", help="Datensatz zusätzlich als JSON hierhin schreiben")
    args = parser.parse_args()

    try:
        parsed = [parse_message(spec) for spec in args.message]
        window = read_context_window(args.context_file)
        started = time.strftime("%Y-%m-%dT%H:%M:%S%z", time.localtime())
        clock = time.monotonic()
        usage = measure([p["message"] for p in parsed], model=args.model,
                        endpoint=args.endpoint, timeout=args.timeout)
    except Fail as exc:
        print(f"ABBRUCH ({args.id}): {exc}", flush=True)
        return 1

    record = {
        "kennung": args.id,
        "zweck": args.purpose,
        "nachrichtenstruktur": [p["witness"] for p in parsed],
        "gemeldete_prompt_tokens": usage["prompt_tokens"],
        "completion_tokens": usage["completion_tokens"],
        "gesetztes_fenster": window,
        "modell": args.model,
        "endpunkt": args.endpoint,
        "zeitstempel": started,
        "dauer_s": round(time.monotonic() - clock, 3),
        "ausgabe": "ungelesen verworfen (§3b (a): Instrumentenmessung, kein Z2-Lauf)",
    }
    text = json.dumps(record, indent=2, ensure_ascii=False)
    print(text, flush=True)
    if args.out:
        Path(args.out).write_text(text + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
