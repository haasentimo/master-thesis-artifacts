#!/usr/bin/env python3
"""Drive the Z2 runs of cell K2 x B1 and K3 x B1 (Z2 protocol, Anhang A, §3b, §5.3).

WHAT THIS TOOL IS
-----------------
It renders the ONE frozen prompt, calls the two model conditions, secures the
delivery, parses the answer against the registered envelope schema and the
well-formedness list Z2-W, and archives the run. It is the tool §5.3 point 2
announces ("Implementiert in `tools/run_z2.py` (S4)") and the one §3b (b)'s
supplement demands ("der Waechter von `tools/run_z2.py` prueft NICHT nur
Gleichstand mit dem Fenster, sondern (b2) und (b3) mit").

THE WORDING IS NEVER DUPLICATED HERE
------------------------------------
The `system` message, the block headings, the composition formula of the `user`
message and the sent JSON schema are EXTRACTED FROM THE FROZEN PROTOCOL at
runtime -- Anhang A, sections A3, A2 and A4 of
`docs/protokolle/z2_protokoll_regelableitung.md`. Nothing of it is retyped in
this file. Two byte gates (`--gates`, run before every call) prove that the
extraction yields exactly the text that was measured in S3.

WHAT IT DOES NOT DO
-------------------
It judges NEITHER Z2-P (testability) NOR Z2-G (content) NOR Z2-Z (deviation
type) -- those are human assessment (§6) -- and it does NOT deduplicate (Z2-R);
N1 is counted by the assessor. Schema conformity is protocol-only, never a
measurand (§5.3 point 1).

NO DEPENDENCIES
---------------
Standard library only. The extractor's client is not used: it hard-wires
`"name": "arch_model"` (`openai_compatible.py:56`) where the frozen schema in A4
carries its own name, and it sends no request options at all.

SUBCOMMANDS
-----------
    render    build both messages, print hashes, send nothing
    selftest  offline positive/negative probes; writes to /tmp only
    probe     the two reachability probes with a trivial payload
    run       one Z2 run of one condition into one slot

INVOCATION
----------
    python3 tools/run_z2.py render
    python3 tools/run_z2.py selftest
    python3 tools/run_z2.py probe --condition k2_b1
    python3 tools/run_z2.py run --condition k2_b1 --slot run0
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
import subprocess
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

REPO = Path(__file__).resolve().parent.parent

PROTOCOL = REPO / "docs/protokolle/z2_protokoll_regelableitung.md"
MEASUREMENTS = REPO / "data/z2/messungen/tokenmessung_2026-09-02.json"
IST_MODELL = REPO / "data/z2/eingaben/ist_modell.yaml"
INPUT_FACTS = REPO / "data/z2/eingaben/input_facts.json"
ARCHIVE_ROOT = REPO / "data/z2"

CONTEXT_FILE = "/etc/systemd/system/ollama.service.d/context.conf"
CONTEXT_KEY = "OLLAMA_CONTEXT_LENGTH"

# The key file itself; only the VALUE of this variable is read, in-process, and
# it never leaves the Authorization header. The variable name is the one the
# extractor's profile `digitalocean` declares (`openai_compatible.py:23`).
SECRETS_FILE = Path.home() / "ma/.secrets/do.env"
SECRET_ENV_KEY = "DO_MODEL_ACCESS_KEY"
# RFC 6750 token type, kept as its own constant so that no line of this file
# joins the scheme word to a value -- the key search of the order has to come
# back empty over this file.
AUTH_SCHEME = "Bearer"

# Tolerance of the delivery assurance against the registered target count,
# +/-0.5 %, TWO-SIDED (§3b (a): the server-reported number is the measurand).
SOLL_TOLERANCE = 0.005
# Both truncation criteria that work off a distance carry the same tolerance,
# registered in §3b (b) and (b3).
DETECTOR_TOLERANCE = 64

CONDITIONS: dict[str, dict[str, Any]] = {
    # K2 -- local, hard delivery assurance: the target count is computable
    # (M11, same bytes, same tokenizer, same server) and the window is ours.
    "k2_b1": {
        "bedingung": "K2",
        "modell": "qwen2.5-coder:7b",
        "base_url": "http://localhost:11434/v1",
        "endpunkt": "http://localhost:11434/v1/chat/completions",
        "provider": "ollama",
        "delivery_assurance": "hard",
        "delivery_assurance_begruendung": (
            "Lokaler Endpunkt: der Sollwert der Prompt-Tokenzahl ist aus M11 "
            "registriert, der Tokenisierer ist derselbe, und das Fenster ist "
            "ueber den systemd-Drop-in gesetzt und ueber `ollama ps` bezeugt. "
            "Alle drei Detektorkriterien aus §3b (b)/(b2)/(b3) binden."
        ),
        "api_key_env": None,
    },
    # K3 -- DigitalOcean, recording instead of assurance: a foreign tokenizer
    # yields no computable target count and the window is not controllable.
    # §3b (e): the threshold binds on K2; K3's count is reported, not binding.
    "k3_b1": {
        "bedingung": "K3",
        "modell": "nvidia-nemotron-3-super-120b",
        "base_url": "https://inference.do-ai.run/v1",
        "endpunkt": "https://inference.do-ai.run/v1/chat/completions",
        "provider": "digitalocean",
        "delivery_assurance": "record_only",
        "delivery_assurance_begruendung": (
            "Fremder Tokenisierer: es gibt keinen berechenbaren Sollwert, und "
            "das Kontextfenster des Anbieters ist weder gesetzt noch ablesbar. "
            "(b) und (b3) sind Ollama-Eigenschaften und binden hier NICHT; "
            "geprueft wird ausschliesslich (b2) gegen fruehere Messungen "
            "DERSELBEN Bedingung. §3b (e): die Schwelle bindet auf K2, K3s "
            "Tokenzahl wird berichtet und ist nicht schwellenbildend."
        ),
        "api_key_env": SECRET_ENV_KEY,
    },
}

SLOTS = ("run0", "run1", "run2")


class Fail(RuntimeError):
    """A stop condition. Never a warning, never a fallback."""


class DeliveryFailure(Fail):
    """The delivery was short or unprovable. NOT a model finding (Z1: `k2_trunkiert`)."""


# --------------------------------------------------------------------------
# hashing and small helpers
# --------------------------------------------------------------------------

def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def nbytes(text: str) -> int:
    return len(text.encode("utf-8"))


def witness(path: Path) -> dict[str, Any]:
    return {"pfad": str(path.relative_to(REPO)), "bytes": path.stat().st_size,
            "sha256": sha256_file(path)}


def git(*args: str) -> str | None:
    try:
        out = subprocess.run(["git", "-C", str(REPO), *args], capture_output=True,
                             text=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None
    return out.stdout.strip()


# --------------------------------------------------------------------------
# extraction from the frozen protocol -- Anhang A
# --------------------------------------------------------------------------

def _lines(text: str) -> list[str]:
    return text.split("\n")


def section_body(text: str, heading: str) -> list[str]:
    """Lines of one `### ` section. Fence-aware: A2 carries `### BLOCK ...` INSIDE a fence."""
    lines = _lines(text)
    try:
        start = lines.index(heading)
    except ValueError as exc:
        raise Fail(f"Abschnitt {heading!r} steht nicht in {PROTOCOL.name}") from exc
    end, in_fence = start + 1, False
    while end < len(lines):
        line = lines[end]
        if line.startswith("```"):
            in_fence = not in_fence
        elif not in_fence and line.startswith("### "):
            break
        end += 1
    return lines[start + 1:end]


def fenced_blocks(body: list[str]) -> list[str]:
    """The fenced code blocks of a section, each with its trailing newline."""
    blocks: list[str] = []
    current: list[str] | None = None
    for line in body:
        if line.startswith("```"):
            if current is None:
                current = []
            else:
                blocks.append("\n".join(current) + "\n")
                current = None
        elif current is not None:
            current.append(line)
    if current is not None:
        raise Fail("unbalancierter Codezaun im Anhang A -- Extraktion abgebrochen")
    return blocks


def one_block(text: str, heading: str, index: int, what: str) -> str:
    blocks = fenced_blocks(section_body(text, heading))
    if len(blocks) <= index:
        raise Fail(f"{what}: {heading} traegt {len(blocks)} Codebloecke, "
                   f"Block {index} wird gebraucht")
    return blocks[index]


def extract_system_message(text: str) -> str:
    """The `system` message, verbatim: the code block of Anhang A, A3."""
    return one_block(text, "### A3 Der Prompt", 0, "system-Nachricht")


def extract_block_headings(text: str) -> dict[str, str]:
    """The two block headings of the `user` message: Anhang A, A2, first block."""
    block = one_block(text, "### A2 Nachrichtenstruktur", 0, "Blockueberschriften")
    headings: dict[str, str] = {}
    for line in block.split("\n"):
        if not line.strip():
            continue
        match = re.match(r"###\s+BLOCK\s+(\d+)\b", line)
        if not match:
            raise Fail(f"Blockueberschrift unlesbar: {line!r}")
        headings[f"BLOCK{match.group(1)}"] = line
    if len(headings) != 2:
        raise Fail(f"A2 traegt {len(headings)} Blockueberschriften, erwartet sind zwei")
    return headings


def extract_composition_formula(text: str) -> str:
    """The composition formula of the `user` message: Anhang A, A2, second block."""
    return one_block(text, "### A2 Nachrichtenstruktur", 1, "Zusammensetzungsformel")


def extract_response_schema(text: str) -> dict[str, Any]:
    """The sent JSON schema, verbatim: the code block of Anhang A, A4."""
    block = one_block(text, "### A4 Das gesendete JSON-Schema", 0, "response_format-Schema")
    try:
        schema = json.loads(block)
    except json.JSONDecodeError as exc:
        raise Fail(f"Das Schema aus A4 ist kein gueltiges JSON: {exc}") from exc
    for key in ("name", "strict", "schema"):
        if key not in schema:
            raise Fail(f"Das Schema aus A4 traegt kein Feld {key!r}")
    return schema


_ESCAPES = {"\\n": "\n", "\\t": "\t", "\\r": "\r", '\\"': '"', "\\\\": "\\"}
_PLACEHOLDER = re.compile(r"\{([A-Za-z_][A-Za-z0-9_]*)(\.rstrip\(\))?\}")


def _unescape(chunk: str) -> str:
    out: list[str] = []
    i = 0
    while i < len(chunk):
        if chunk[i] == "\\":
            pair = chunk[i:i + 2]
            if pair not in _ESCAPES:
                raise Fail(f"unbekannte Escape-Sequenz {pair!r} in der Zusammensetzungsformel")
            out.append(_ESCAPES[pair])
            i += 2
        else:
            out.append(chunk[i])
            i += 1
    return "".join(out)


def apply_composition_formula(formula: str, values: dict[str, str]) -> str:
    """Interpret the registered f-string, rather than reimplementing it.

    Only two placeholder forms occur and only two are accepted: `{NAME}` and
    `{NAME.rstrip()}`. Anything else stops the tool -- a formula this code
    cannot read exactly must not be approximated.
    """
    body = formula.strip()
    if not (body.startswith('f"') and body.endswith('"')):
        raise Fail(f"Zusammensetzungsformel nicht in der erwarteten f-String-Form: {body!r}")
    template = body[2:-1]
    out: list[str] = []
    pos = 0
    for match in _PLACEHOLDER.finditer(template):
        out.append(_unescape(template[pos:match.start()]))
        name, call = match.group(1), match.group(2)
        if name not in values:
            raise Fail(f"Die Formel nennt {name!r}; dafuer gibt es keinen Wert")
        out.append(values[name].rstrip() if call else values[name])
        pos = match.end()
    tail = template[pos:]
    if "{" in tail or "}" in tail:
        raise Fail(f"unlesbarer Platzhalter am Formelende: {tail!r}")
    out.append(_unescape(tail))
    return "".join(out)


# --------------------------------------------------------------------------
# the registered measurements -- read, never hard-coded
# --------------------------------------------------------------------------

def measurement(kennung: str) -> dict[str, Any]:
    records = json.loads(MEASUREMENTS.read_text(encoding="utf-8")).get("messungen", [])
    for record in records:
        if record.get("kennung") == kennung:
            return record
    raise Fail(f"Messung {kennung!r} steht nicht in {MEASUREMENTS.name}")


def measured_message(kennung: str, role: str) -> dict[str, Any]:
    for entry in measurement(kennung).get("nachrichtenstruktur", []):
        if isinstance(entry, dict) and entry.get("rolle") == role:
            return entry
    raise Fail(f"Messung {kennung!r} traegt keine Nachricht der Rolle {role!r}")


def registered_targets() -> dict[str, Any]:
    """Everything the gates and the delivery assurance compare against.

    M11 is the full prompt under R3 (the two message hashes and the target token
    count), M11a the single measurement of the largest component -- the reference
    of the monotonicity criterion (b2) -- and M1 the base count B.
    """
    m11, m11a, m1 = measurement("M11"), measurement("M11a"), measurement("M1")
    system, user = measured_message("M11", "system"), measured_message("M11", "user")
    return {
        "quelle": str(MEASUREMENTS.relative_to(REPO)),
        "quelle_sha256": sha256_file(MEASUREMENTS),
        "G1_system": {"sha256": system["sha256"], "bytes": system["bytes"],
                      "herkunft": "M11, Nachricht der Rolle `system`"},
        "G2_user": {"sha256": user["sha256"], "bytes": user["bytes"],
                    "herkunft": "M11, Nachricht der Rolle `user`"},
        "soll_prompt_tokens": {"wert": m11["gemeldete_prompt_tokens"], "herkunft": "M11"},
        "monotonie_bezug": {"wert": m11a["gemeldete_prompt_tokens"],
                            "herkunft": "M11a, Faktenbasis in der gezogenen Fassung"},
        "basiszahl_B": {"wert": m1["gemeldete_prompt_tokens"], "herkunft": "M1"},
    }


# --------------------------------------------------------------------------
# rendering and the two byte gates
# --------------------------------------------------------------------------

def render_messages() -> dict[str, Any]:
    """Build both messages from the frozen document and the two hashed inputs."""
    text = PROTOCOL.read_text(encoding="utf-8")
    system = extract_system_message(text)
    headings = extract_block_headings(text)
    formula = extract_composition_formula(text)
    schema = extract_response_schema(text)
    user = apply_composition_formula(formula, {
        **headings,
        "ist_modell": IST_MODELL.read_text(encoding="utf-8"),
        "faktenbasis": INPUT_FACTS.read_text(encoding="utf-8"),
    })
    return {
        "messages": [{"role": "system", "content": system},
                     {"role": "user", "content": user}],
        "schema": schema,
        "formel": formula.strip(),
        "blockueberschriften": headings,
        "protokoll": {
            "pfad": str(PROTOCOL.relative_to(REPO)),
            "sha256": sha256_file(PROTOCOL),
            "commit": git("log", "-1", "--format=%H", "--", str(PROTOCOL)),
        },
        "eingaben": {"ist_modell": witness(IST_MODELL),
                     "input_facts": witness(INPUT_FACTS)},
    }


def gate_report(rendered: dict[str, Any]) -> dict[str, Any]:
    """G1 and G2: the extraction must be byte-identical with what S3 measured."""
    targets = registered_targets()
    system, user = rendered["messages"][0]["content"], rendered["messages"][1]["content"]
    gates = []
    for name, content, target in (("G1", system, targets["G1_system"]),
                                  ("G2", user, targets["G2_user"])):
        got_sha, got_bytes = sha256_text(content), nbytes(content)
        gates.append({
            "gatter": name,
            "gegenstand": "system-Nachricht (Anhang A, A3)" if name == "G1"
                          else "user-Nachricht (Anhang A, A2, Zusammensetzungsformel)",
            "soll_sha256": target["sha256"], "ist_sha256": got_sha,
            "soll_bytes": target["bytes"], "ist_bytes": got_bytes,
            "herkunft_soll": target["herkunft"],
            "urteil": "GEHALTEN" if (got_sha == target["sha256"]
                                     and got_bytes == target["bytes"]) else "GERISSEN",
        })
    return {"gatter": gates, "urteil": "GEHALTEN"
            if all(g["urteil"] == "GEHALTEN" for g in gates) else "GERISSEN",
            "registrierte_sollwerte": targets}


def require_gates(rendered: dict[str, Any]) -> dict[str, Any]:
    report = gate_report(rendered)
    if report["urteil"] != "GEHALTEN":
        broken = [g for g in report["gatter"] if g["urteil"] == "GERISSEN"]
        detail = "; ".join(
            f"{g['gatter']}: soll {g['soll_sha256']} ({g['soll_bytes']} B), "
            f"ist {g['ist_sha256']} ({g['ist_bytes']} B)" for g in broken)
        raise Fail("BYTEGATTER GERISSEN -- kein Aufruf. " + detail)
    return report


# --------------------------------------------------------------------------
# the window, read and witnessed -- never set by this tool
# --------------------------------------------------------------------------

def configured_window(path: str = CONTEXT_FILE) -> dict[str, Any]:
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


def ollama_ps() -> dict[str, Any]:
    """Raw `ollama ps` plus the parsed CONTEXT column -- the window witness."""
    try:
        out = subprocess.run(["ollama", "ps"], capture_output=True, text=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError) as exc:
        return {"roh": None, "fehler": str(exc), "zeilen": []}
    lines = [ln for ln in out.stdout.splitlines() if ln.strip()]
    record: dict[str, Any] = {"roh": out.stdout, "zeilen": lines, "eintraege": []}
    if not lines:
        return record
    header = re.split(r"\s{2,}", lines[0].strip())
    for line in lines[1:]:
        columns = re.split(r"\s{2,}", line.strip())
        entry = dict(zip(header, columns))
        if str(entry.get("CONTEXT", "")).isdigit():
            entry["CONTEXT"] = int(entry["CONTEXT"])
        record["eintraege"].append(entry)
    return record


def ollama_stop(model: str) -> dict[str, Any]:
    try:
        out = subprocess.run(["ollama", "stop", model], capture_output=True, text=True)
    except FileNotFoundError as exc:
        return {"aufruf": f"ollama stop {model}", "fehler": str(exc)}
    return {"aufruf": f"ollama stop {model}", "returncode": out.returncode,
            "stderr": out.stderr.strip()}


def ollama_digest(model: str) -> dict[str, Any]:
    """Manifest digest from the local model store -- no model call (Z1 §3.3 (7))."""
    tag = model.split(":", 1)
    name, version = (tag[0], tag[1]) if len(tag) == 2 else (tag[0], "latest")
    manifest = (Path.home() / ".ollama/models/manifests/registry.ollama.ai/library"
                / name / version)
    if not manifest.exists():
        return {"pfad": str(manifest), "digest": None,
                "hinweis": "Manifest nicht gefunden -- Digest nicht erhoben"}
    digest = sha256_file(manifest)
    return {"pfad": str(manifest), "digest": digest, "kurzform": digest[:12]}


# --------------------------------------------------------------------------
# delivery assurance -- §3b (b), (b2), (b3), asymmetric between K2 and K3
# --------------------------------------------------------------------------

def delivery_check(*, reported: int | None, window: int | None, monotony_ref: int | None,
                   soll: int | None, assurance: str) -> dict[str, Any]:
    """Judge one reported prompt-token count. Every violation is a DELIVERY FAILURE.

    `hard` (K2) binds four criteria: the two-sided tolerance band around the
    target count, and the three truncation criteria. `record_only` (K3) binds
    (b2) alone -- (b) and (b3) are properties of the Ollama server, and there is
    no computable target count for a foreign tokenizer (§3b (e)).
    """
    hard = assurance == "hard"
    checks: list[dict[str, Any]] = []

    def add(kriterium: str, regel: str, gilt: bool, verletzt: bool,
            rechnung: str, grund_wenn_aus: str = "") -> None:
        checks.append({
            "kriterium": kriterium, "regel": regel, "rechnung": rechnung,
            "gilt": gilt,
            "urteil": ("VERLETZT" if verletzt else "spricht nicht an") if gilt
                      else "gilt nicht",
            "grund_wenn_aus": grund_wenn_aus,
        })

    if reported is None:
        raise DeliveryFailure(
            "Die Antwort traegt keine serverseitige Prompt-Tokenzahl "
            "(`usage.prompt_tokens`). Die Lieferung ist unbezeugt: LIEFERAUSFALL.")

    # Target count and its TWO-SIDED tolerance band, K2 only. The form follows
    # `tools/check_z1_delivery.py:62-63`: a reference count, a band of +/-0.5 %
    # around it, both sides, and NO separate shortfall rule. S4 had ordered the
    # band AND an abort on every shortfall of the target count at once; together
    # the lower bound of the band is inoperative, and the tool ran the stricter
    # reading. S4b takes that reading back: a hard shortfall rule would score a
    # legitimate fluctuation of the token count as a delivery failure and burn a
    # run that was in fact delivered. The three detector criteria of §3b (b),
    # (b2) and (b3) are UNTOUCHED by this and bite independently of the band --
    # every violation of them is still a delivery failure.
    if soll is not None and hard:
        lower_band = math.ceil(soll * (1 - SOLL_TOLERANCE))
        upper_band = math.floor(soll * (1 + SOLL_TOLERANCE))
        if reported < lower_band:
            rechnung = f"{reported} unter dem Band [{lower_band}, {upper_band}]"
        elif reported > upper_band:
            rechnung = f"{reported} ueber dem Band [{lower_band}, {upper_band}]"
        else:
            rechnung = f"{reported} im Band [{lower_band}, {upper_band}]"
        add("soll_toleranz",
            f"gemeldete Zahl im Band {lower_band}-{upper_band} (Sollwert {soll}, "
            f"Toleranz +/-{SOLL_TOLERANCE:.1%}, beidseitig; keine Unterschreitungsregel)",
            True, not (lower_band <= reported <= upper_band), rechnung)
    else:
        add("soll_toleranz", "Sollwert und Toleranzband", False, False,
            "kein berechenbarer Sollwert",
            "record_only: fremder Tokenisierer, kein berechenbarer Sollwert (§3b (e))")

    # (b) window equality, K2 only.
    if hard and window:
        suspect_from = window - DETECTOR_TOLERANCE + 1
        add("b_fenstergleichstand",
            f"ungueltig bei Gleichstand mit dem Fenster {window} oder weniger als "
            f"{DETECTOR_TOLERANCE} Token Abstand darunter (Verdachtsbereich ab {suspect_from})",
            True, reported >= suspect_from,
            f"{window} - {reported} = {window - reported}")
    else:
        add("b_fenstergleichstand", "Gleichstand mit dem gesetzten Fenster", False, False,
            "Fenster nicht kontrollierbar",
            "record_only: das Fenster des Anbieters ist weder gesetzt noch ablesbar; "
            "das Kriterium ist eine Ollama-Eigenschaft")

    # (b2) monotonicity -- binds under BOTH assurances.
    if monotony_ref is not None:
        add("b2_monotonie",
            "die gemeldete Zahl des vollen Prompts muss mindestens so gross sein wie "
            f"die Einzelmessung seiner groessten Komponente ({monotony_ref})",
            True, reported < monotony_ref, f"{reported} gegen {monotony_ref}")
    else:
        add("b2_monotonie", "Monotonie gegen die groesste Komponente", False, False,
            "kein Bezugswert",
            "record_only ohne frueheren Lauf DERSELBEN Bedingung: es gibt noch keine "
            "Vergleichsmessung; das Kriterium ist gegenstandslos, nicht bestanden")

    # (b3) half-window signature, K2 only.
    if hard and window:
        signature = window // 2 + 2
        distance = signature - reported
        add("b3_halbfenster",
            f"ungueltig bei Gleichstand mit Fenster/2 + 2 = {signature} oder weniger "
            f"als {DETECTOR_TOLERANCE} Token darunter",
            True, 0 <= distance < DETECTOR_TOLERANCE,
            f"{signature} - {reported} = {distance}")
    else:
        add("b3_halbfenster", "Halbfenster-Signatur Fenster/2 + 2", False, False,
            "Signatur ist eine Ollama-Eigenschaft",
            "record_only: die Halbfenster-Signatur ist an zwei Ollama-Messpunkten "
            "abgeleitet (§3b (b3), Evidenzeinordnung) und auf einen fremden Server "
            "nicht uebertragbar")

    violated = [c for c in checks if c["urteil"] == "VERLETZT"]
    return {
        "delivery_assurance": assurance,
        "gemeldete_prompt_tokens": reported,
        "gesetztes_fenster": window,
        "sollwert": soll,
        "monotonie_bezug": monotony_ref,
        "kriterien": checks,
        "verletzt": [c["kriterium"] for c in violated],
        "urteil": "LIEFERAUSFALL" if violated else "LIEFERUNG ZUGESICHERT"
                  if assurance == "hard" else "LIEFERUNG AUFGEZEICHNET",
    }


def require_delivery(report: dict[str, Any]) -> dict[str, Any]:
    if report["verletzt"]:
        detail = "; ".join(f"{c['kriterium']}: {c['rechnung']}"
                           for c in report["kriterien"] if c["urteil"] == "VERLETZT")
        raise DeliveryFailure(
            f"LIEFERAUSFALL ({report['delivery_assurance']}) -- der Lauf wird NICHT als "
            f"Lauf gezaehlt und ist KEIN Modellbefund. Verletzt: {detail}")
    return report


# --------------------------------------------------------------------------
# parsing, stage (i): schema conformity -- protocol only, never a measurand
# --------------------------------------------------------------------------

def validate_schema(instance: Any, schema: dict[str, Any], path: str = "$") -> list[str]:
    """A strict validator for exactly the constructs the frozen A4 schema uses."""
    errors: list[str] = []
    expected = schema.get("type")
    if expected == "object":
        if not isinstance(instance, dict):
            return [f"{path}: erwartet object, ist {type(instance).__name__}"]
        properties = schema.get("properties", {})
        for name in schema.get("required", []):
            if name not in instance:
                errors.append(f"{path}: Pflichtfeld {name!r} fehlt")
        if schema.get("additionalProperties") is False:
            for name in instance:
                if name not in properties:
                    errors.append(f"{path}: zusaetzliches Feld {name!r} "
                                  f"(additionalProperties: false)")
        for name, value in instance.items():
            if name in properties:
                errors += validate_schema(value, properties[name], f"{path}.{name}")
    elif expected == "array":
        if not isinstance(instance, list):
            return [f"{path}: erwartet array, ist {type(instance).__name__}"]
        minimum = schema.get("minItems")
        if isinstance(minimum, int) and len(instance) < minimum:
            errors.append(f"{path}: {len(instance)} Elemente, minItems: {minimum}")
        item_schema = schema.get("items")
        if isinstance(item_schema, dict):
            for index, item in enumerate(instance):
                errors += validate_schema(item, item_schema, f"{path}[{index}]")
    elif expected == "string":
        if not isinstance(instance, str):
            errors.append(f"{path}: erwartet string, ist {type(instance).__name__}")
        elif "enum" in schema and instance not in schema["enum"]:
            errors.append(f"{path}: {instance!r} steht nicht im Enum {schema['enum']}")
    elif expected is not None:
        errors.append(f"{path}: unbekannter Typ {expected!r} im Schema")
    return errors


# --------------------------------------------------------------------------
# parsing, stage (ii): the registered binary list Z2-W (§5.3 point 2)
# --------------------------------------------------------------------------

def resource_levels(path: Path = IST_MODELL) -> dict[str, str]:
    """Every `- id:` of the Ilograph export, with the LEVEL the id sits on.

    Read line-wise on purpose: the tool is standard library only, and the export
    is machine-written with one id per line (175 of them, no other `id:` key).

    Three levels, straight out of the export: an id carrying the `::` separator
    comes from an `x-triton-inner-artefacts` block and is an `artefact`; a plain
    id is a `package` or a `module` according to the marker its node carries one
    indent level in (`x-triton-node-type: package`, `x-triton-project-kind:
    module`). The counts of the frozen input are 23 + 50 + 102 = 175.

    The level is an OBSERVATION only -- see `scope_granularity`. The resolution
    stock of `scope.components` stays every one of the 175 ids, as §5.3 has it.
    """
    levels: dict[str, str] = {}
    current, current_indent = None, 0
    for line in path.read_text(encoding="utf-8").splitlines():
        match = re.match(r"^(\s*)-\s+id:\s*(\S+)\s*$", line)
        if match:
            indent, resource = len(match.group(1)), match.group(2)
            if "::" in resource:
                levels[resource], current = "artefact", None
            else:
                levels[resource] = "unbestimmt"
                current, current_indent = resource, indent
            continue
        if current is None:
            continue
        marker = re.match(r"^(\s*)x-triton-(node-type|project-kind):\s*(\S+)\s*$", line)
        if marker and len(marker.group(1)) == current_indent + 2:
            if marker.group(2) == "node-type" and marker.group(3) == "package":
                levels[current] = "package"
            elif marker.group(2) == "project-kind" and marker.group(3) == "module":
                levels[current] = "module"
    if not levels:
        raise Fail(f"{path.name} traegt keine Ressourcen-Ids -- Z2-W nicht pruefbar")
    return levels


def resource_ids(path: Path = IST_MODELL) -> set[str]:
    """Every `- id:` of the export -- the names BLOCK 1 offers verbatim.

    ALL of them, on every level: the resolution stock of `scope.components` is
    the full set of 175 ids (§5.3). The level a component sits on is counted,
    never judged.
    """
    return set(resource_levels(path))


def _normalise(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().casefold()


# --------------------------------------------------------------------------
# OBSERVATION, NOT A CRITERION: on which level the named components sit
# --------------------------------------------------------------------------

GRANULARITY_NOTE = (
    "BEOBACHTUNG, KEIN Z2-W-KRITERIUM UND KEIN BEWERTUNGSKRITERIUM. Z2-W bleibt "
    "die in §5.3 registrierte binaere Liste; ein Vorschlag auf Artefaktebene ist "
    "WOHLGEFORMT. Diese Zaehlung wird berichtet, nicht gewertet, und geht in "
    "keine Kennzahl ein. Anlass: Granularitaet war in Z1 der Ausfallgrund "
    "(Befund 07 -- beide Modelle schrieben die Relationsendpunkte auf der "
    "falschen Granularitaet)."
)


def scope_granularity(components: Any, levels: dict[str, str]) -> dict[str, int]:
    """Count, per proposal, the level of each named component. Nothing is judged.

    `unresolved` is the count of ids that do not resolve against `ist_modell.yaml`
    -- the SAME ids that make the Z2-W criterion `components_aufloesbar` fail.
    The count merely mirrors that criterion here; it does not add one.
    """
    tally = {"package": 0, "module": 0, "artefact": 0, "unresolved": 0}
    if not isinstance(components, list):
        return tally
    for component in components:
        level = levels.get(component) if isinstance(component, str) else None
        tally[level if level in tally else "unresolved"] += 1
    return tally


def check_z2w(rules: list[Any], ids: set[str],
              levels: dict[str, str] | None = None) -> dict[str, Any]:
    """The four registered conditions of §5.3, binary, per proposal and aggregated.

    `levels` feeds the granularity OBSERVATION only and never a condition.
    """
    levels = levels if levels is not None else {}
    seen: dict[str, int] = {}
    for rule in rules:
        if isinstance(rule, dict) and isinstance(rule.get("id"), str):
            seen[rule["id"]] = seen.get(rule["id"], 0) + 1

    per_rule: list[dict[str, Any]] = []
    for index, rule in enumerate(rules):
        if not isinstance(rule, dict):
            per_rule.append({"position": index, "id": None, "wohlgeformt": False,
                             "befunde": ["Vorschlag ist kein Objekt"]})
            continue
        rule_id = rule.get("id")
        category = rule.get("category")
        statement = rule.get("statement")
        components = (rule.get("scope") or {}).get("components") \
            if isinstance(rule.get("scope"), dict) else None
        findings: list[str] = []
        checks: dict[str, bool] = {}

        unresolved = [c for c in components if c not in ids] \
            if isinstance(components, list) else None
        if unresolved is None:
            checks["components_aufloesbar"] = False
            findings.append("scope.components fehlt oder ist keine Liste")
        else:
            checks["components_aufloesbar"] = not unresolved
            if unresolved:
                findings.append("scope.components nicht gegen ist_modell.yaml "
                                f"aufloesbar: {sorted(unresolved)}")

        checks["statement_nicht_leer"] = isinstance(statement, str) and bool(statement.strip())
        if not checks["statement_nicht_leer"]:
            findings.append("statement ist leer")

        repetition = (isinstance(statement, str)
                      and _normalise(statement) in {
                          _normalise(rule_id) if isinstance(rule_id, str) else "\0",
                          _normalise(category) if isinstance(category, str) else "\0"})
        checks["statement_keine_wiederholung"] = not repetition
        if repetition:
            findings.append("statement wiederholt id oder category")

        checks["id_eindeutig"] = isinstance(rule_id, str) and seen.get(rule_id, 0) == 1
        if not checks["id_eindeutig"]:
            findings.append("id fehlt oder ist im Lauf nicht eindeutig")

        checks["category_nicht_leer"] = isinstance(category, str) and bool(category.strip())
        if not checks["category_nicht_leer"]:
            findings.append("category ist leer")

        per_rule.append({"position": index, "id": rule_id,
                         "pruefungen": checks, "befunde": findings,
                         "wohlgeformt": all(checks.values()),
                         # observation, deliberately OUTSIDE `pruefungen`, so
                         # that it can never reach `wohlgeformt`
                         "granularitaet": scope_granularity(components, levels)})

    wellformed = sum(1 for r in per_rule if r["wohlgeformt"])
    with_artefact = sum(1 for r in per_rule
                        if r.get("granularitaet", {}).get("artefact", 0) > 0)
    return {
        "regel": "§5.3 Punkt 2 -- binaere, maschinelle Liste; vier Bedingungen je Vorschlag",
        "je_vorschlag": per_rule,
        "aggregat": {"vorschlaege": len(rules), "wohlgeformt": wellformed,
                     "nicht_wohlgeformt": len(rules) - wellformed},
        "granularitaet": {
            "vorschlaege_mit_mindestens_einer_artefakt_id": with_artefact,
            "ebenen_je_vorschlag": [
                {"position": r["position"], "id": r["id"],
                 **r.get("granularitaet", {})} for r in per_rule],
            "einordnung": GRANULARITY_NOTE,
        },
    }


NOT_IMPLEMENTED_NOTE = {
    "Z2-P": "Pruefbarkeit -- menschliche Bewertung (§6); dieses Werkzeug bewertet nichts "
            "davon und schreibt dafuer kein Feld.",
    "Z2-G": "Gehalt -- menschliche Bewertung (§6).",
    "Z2-Z": "Zuordnung zum Abweichungstyp -- menschliche Bewertung (§6).",
    "Z2-R": "Redundanz/Dedup -- NICHT automatisiert; N1 zaehlt der Bewerter.",
}


def build_validation(raw_text: str, schema: dict[str, Any], ids: set[str],
                     levels: dict[str, str] | None = None) -> dict[str, Any]:
    """Both stages, kept apart: (i) is protocol only, (ii) is the measurand.

    `levels` carries the granularity observation through; it is no third stage.
    """
    parse_error = None
    payload: Any = None
    try:
        payload = json.loads(raw_text)
    except json.JSONDecodeError as exc:
        parse_error = str(exc)

    schema_errors = ["Antwort ist kein JSON: " + parse_error] if parse_error \
        else validate_schema(payload, schema["schema"])
    rules = payload.get("rules") if isinstance(payload, dict) else None
    z2w = check_z2w(rules, ids, levels) if isinstance(rules, list) else {
        "regel": "§5.3 Punkt 2", "je_vorschlag": [],
        "aggregat": {"vorschlaege": 0, "wohlgeformt": 0, "nicht_wohlgeformt": 0},
        "granularitaet": {"vorschlaege_mit_mindestens_einer_artefakt_id": 0,
                          "ebenen_je_vorschlag": [], "einordnung": GRANULARITY_NOTE},
        "hinweis": "Die Antwort traegt keine Liste `rules`; Z2-W ist nicht anwendbar.",
    }
    return {
        "schema_konformitaet": {
            "schemaname": schema["name"],
            "strict": schema["strict"],
            "verstoesse": schema_errors,
            "urteil": "konform" if not schema_errors else "nicht konform",
            "einordnung": "§5.3 Punkt 1: unter `strict: true` providerseitig erzwungen "
                          "und AUSDRUECKLICH KEINE Messgroesse -- hier nur protokolliert.",
        },
        "z2w": z2w,
        "nicht_implementiert": NOT_IMPLEMENTED_NOTE,
    }


# --------------------------------------------------------------------------
# the key, and the one call
# --------------------------------------------------------------------------

def load_api_key(env_key: str) -> str:
    """Read the key in-process. It never reaches a record, an output or a log."""
    if SECRETS_FILE.exists():
        for line in SECRETS_FILE.read_text(encoding="utf-8").splitlines():
            name, sep, value = line.strip().partition("=")
            if sep and name.strip().lstrip("export ").strip() == env_key:
                key = value.strip().strip('"').strip("'")
                if key:
                    return key
    fallback = os.environ.get(env_key)
    if fallback:
        return fallback
    raise Fail(f"Kein Schluessel: {env_key} steht weder in {SECRETS_FILE} noch in der "
               f"Umgebung. (Der Inhalt der Datei wird nicht ausgegeben.)")


def scrub(text: str, secret: str | None) -> str:
    """Never let a key reach an error message, however the server phrases it."""
    return text.replace(secret, "<redaktiert>") if secret else text


def post_json(endpoint: str, payload: dict[str, Any], *, api_key: str | None,
              timeout: int) -> dict[str, Any]:
    body = json.dumps(payload).encode("utf-8")
    headers = {"Content-Type": "application/json"}
    if api_key:
        headers["Authorization"] = f"{AUTH_SCHEME} {api_key}"
    request = urllib.request.Request(endpoint, data=body, method="POST", headers=headers)
    clock = time.monotonic()
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            raw = response.read().decode("utf-8")
            status = response.status
    except urllib.error.HTTPError as exc:
        detail = scrub(exc.read().decode("utf-8", "replace")[:600], api_key)
        raise Fail(f"HTTP {exc.code} von {endpoint}: {detail}") from None
    except urllib.error.URLError as exc:
        raise Fail(f"Aufruf scheiterte am Endpunkt {endpoint}: "
                   f"{scrub(str(exc.reason), api_key)}") from None
    latency_ms = (time.monotonic() - clock) * 1000
    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise Fail(f"Antwort von {endpoint} ist kein JSON: {exc}") from None
    return {"http_status": status, "latenz_ms": round(latency_ms, 3), "payload": parsed}


def usage_of(payload: dict[str, Any]) -> dict[str, Any]:
    """`usage.prompt_tokens` -- the same count Z1-T and `check_z1_delivery.py` read."""
    usage = payload.get("usage")
    usage = usage if isinstance(usage, dict) else {}
    return {
        "prompt_tokens": usage.get("prompt_tokens"),
        "completion_tokens": usage.get("completion_tokens"),
        "total_tokens": usage.get("total_tokens"),
    }


# --------------------------------------------------------------------------
# archiving -- §3.4 (hash duty) and the shape of data/z1/
# --------------------------------------------------------------------------

def render_prompt_file(messages: list[dict[str, str]]) -> str:
    """The render form of `run_logger.py:39-40`, so Z1 and Z2 archives read alike."""
    return "\n\n".join(f"### {m['role']}\n{m['content']}" for m in messages)


def slot_dir(condition: str, slot: str, root: Path = ARCHIVE_ROOT) -> Path:
    return root / condition / slot


def require_free_slot(condition: str, slot: str, root: Path = ARCHIVE_ROOT) -> Path:
    """Nothing is written into an occupied slot -- no overwrite, no append.

    `root` exists so the self-test can exercise THIS guard against a temporary
    directory instead of a re-implementation of it.
    """
    target = slot_dir(condition, slot, root)
    if target.exists():
        raise Fail(f"Zielslot {target} existiert bereits -- ABBRUCH. "
                   f"Es wird nicht ueberschrieben und nicht angehaengt.")
    return target


def write_block_sums(condition: str) -> Path | None:
    """Refresh `SHA256SUMS` of one condition block. MANIFEST.md stays untouched."""
    block = ARCHIVE_ROOT / condition
    if not block.exists():
        return None
    lines = []
    for path in sorted(block.rglob("*")):
        if path.is_file() and path.name not in {"SHA256SUMS", "MANIFEST.md"}:
            lines.append(f"{sha256_file(path)}  {path.relative_to(block)}")
    sums = block / "SHA256SUMS"
    sums.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return sums


def earlier_reported_counts(condition: str) -> list[int]:
    """Reported prompt-token counts of earlier archived runs of the SAME condition."""
    block = ARCHIVE_ROOT / condition
    counts: list[int] = []
    if not block.exists():
        return counts
    for manifest in sorted(block.glob("*/run_manifest.json")):
        try:
            record = json.loads(manifest.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        value = (record.get("lieferzusicherung") or {}).get("gemeldete_prompt_tokens")
        if isinstance(value, int):
            counts.append(value)
    return counts


# --------------------------------------------------------------------------
# subcommand: render -- build both messages, print hashes, send nothing
# --------------------------------------------------------------------------

def cmd_render(args: argparse.Namespace) -> int:
    rendered = render_messages()
    report = gate_report(rendered)
    system, user = rendered["messages"][0]["content"], rendered["messages"][1]["content"]
    record = {
        "unterbefehl": "render",
        "gesendet": False,
        "protokoll": rendered["protokoll"],
        "eingaben": rendered["eingaben"],
        "blockueberschriften": rendered["blockueberschriften"],
        "zusammensetzungsformel": rendered["formel"],
        "schemaname": rendered["schema"]["name"],
        "nachrichten": [
            {"rolle": "system", "bytes": nbytes(system), "sha256": sha256_text(system),
             "herkunft": "Anhang A, A3 (Codeblock), programmatisch extrahiert"},
            {"rolle": "user", "bytes": nbytes(user), "sha256": sha256_text(user),
             "herkunft": "Anhang A, A2: Blockueberschriften und Zusammensetzungsformel"},
        ],
        "bytegatter": report,
    }
    print(json.dumps(record, indent=2, ensure_ascii=False))
    if args.write_prompt:
        Path(args.write_prompt).write_text(render_prompt_file(rendered["messages"]),
                                           encoding="utf-8")
    return 0 if report["urteil"] == "GEHALTEN" else 1


# --------------------------------------------------------------------------
# subcommand: probe -- reachability, trivial payload, INSTRUMENT MEASUREMENT
# --------------------------------------------------------------------------

def cmd_probe(args: argparse.Namespace) -> int:
    """§3b (a): counts against no budget, is not archived as a run, output unread.

    The Z2 prompt is NOT sent -- that would be a run. The payload is the literal
    `x`, exactly the one M1 measured, so K2's answer is comparable with B = 30.
    """
    config = CONDITIONS[args.condition]
    rendered = render_messages()
    gates = require_gates(rendered)          # gate before every call, also before a probe
    targets = registered_targets()
    api_key = load_api_key(config["api_key_env"]) if config["api_key_env"] else None

    preflight: dict[str, Any] = {}
    if config["provider"] == "ollama":
        preflight = {"ollama_stop": ollama_stop(config["modell"]),
                     "ollama_ps_vor": ollama_ps()}

    started = time.strftime("%Y-%m-%dT%H:%M:%S%z", time.localtime())
    response = post_json(config["endpunkt"], {
        "model": config["modell"],
        "messages": [{"role": "user", "content": "x"}],
        "temperature": 0,
        "max_tokens": 1,
    }, api_key=api_key, timeout=args.timeout)
    payload = response["payload"]

    record: dict[str, Any] = {
        "sonde": "S-K2" if config["provider"] == "ollama" else "S-K3",
        "einordnung": "INSTRUMENTENMESSUNG nach §3b (a) -- kein Z2-Lauf, kein Budget, "
                      "keine Archivierung als Lauf, Ausgabe ungelesen verworfen.",
        "bedingung": config["bedingung"],
        "nutzlast": {"art": "literal", "literal": "x", "bytes": 1,
                     "sha256": sha256_text("x")},
        "modell_angefordert": config["modell"],
        "modell_echo": payload.get("model"),
        "endpunkt": config["endpunkt"],
        "http_status": response["http_status"],
        "usage": usage_of(payload),
        "system_fingerprint": payload.get("system_fingerprint"),
        "latenz_ms": response["latenz_ms"],
        "zeitstempel": started,
        "bytegatter": gates["urteil"],
        "ausgabe": "ungelesen verworfen (§3b (a))",
    }
    if preflight:
        record["kaltsonde"] = preflight
        record["ollama_ps_nach"] = ollama_ps()
        record["gesetztes_fenster"] = configured_window(args.context_file)
        base = targets["basiszahl_B"]["wert"]
        got = record["usage"]["prompt_tokens"]
        record["gegen_basiszahl_B"] = {
            "erwartet": base, "herkunft": targets["basiszahl_B"]["herkunft"],
            "gemeldet": got,
            "urteil": "trifft" if got == base else f"WEICHT AB um {got - base}"
            if isinstance(got, int) else "keine Zahl gemeldet",
        }
    else:
        record["t_z1_5"] = ("DO-Direktzugang: `system_fingerprint` ist `null`, es gibt "
                            "keinen Digest, und die Identitaet der Gewichte ist nicht "
                            "verifizierbar (Z1-Protokoll §3.3 (7), T-Z1-5).")
    print(json.dumps(record, indent=2, ensure_ascii=False))
    if args.out:
        Path(args.out).write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n",
                                  encoding="utf-8")
    return 0


# --------------------------------------------------------------------------
# subcommand: run -- one Z2 run of one condition into one slot
# --------------------------------------------------------------------------

def cmd_run(args: argparse.Namespace) -> int:
    config = CONDITIONS[args.condition]
    target = require_free_slot(args.condition, args.slot)     # slot protection FIRST
    rendered = render_messages()
    gates = require_gates(rendered)                           # both byte gates, offline
    targets = registered_targets()
    window = configured_window(args.context_file)
    api_key = load_api_key(config["api_key_env"]) if config["api_key_env"] else None
    hard = config["delivery_assurance"] == "hard"

    preflight: dict[str, Any] = {}
    if config["provider"] == "ollama":
        preflight = {"ollama_stop": ollama_stop(config["modell"]),
                     "ollama_ps_vor": ollama_ps()}

    request = {
        "model": config["modell"],
        "messages": rendered["messages"],
        "temperature": 0,
        "seed": 0,
        "response_format": {"type": "json_schema", "json_schema": rendered["schema"]},
    }
    started = time.strftime("%Y-%m-%dT%H:%M:%S%z", time.localtime())
    response = post_json(config["endpunkt"], request, api_key=api_key, timeout=args.timeout)
    finished = time.strftime("%Y-%m-%dT%H:%M:%S%z", time.localtime())
    payload = response["payload"]
    usage = usage_of(payload)

    if config["provider"] == "ollama":
        preflight["ollama_ps_nach"] = ollama_ps()

    # Monotonicity reference: for K2 the registered single measurement M11a, for
    # K3 the largest reported count of EARLIER runs of the same condition.
    if hard:
        monotony_ref = targets["monotonie_bezug"]["wert"]
        monotony_source = targets["monotonie_bezug"]["herkunft"]
    else:
        earlier = earlier_reported_counts(args.condition)
        monotony_ref = max(earlier) if earlier else None
        monotony_source = (f"groesste gemeldete Zahl frueherer Laeufe der Bedingung "
                           f"{args.condition}: {earlier}" if earlier
                           else "kein frueherer Lauf derselben Bedingung")

    delivery = delivery_check(
        reported=usage["prompt_tokens"],
        window=window["wert"] if hard else None,
        monotony_ref=monotony_ref,
        soll=targets["soll_prompt_tokens"]["wert"] if hard else None,
        assurance=config["delivery_assurance"])
    delivery["delivery_assurance_begruendung"] = config["delivery_assurance_begruendung"]
    delivery["monotonie_bezug_herkunft"] = monotony_source
    delivery["sollwert_herkunft"] = targets["soll_prompt_tokens"]["herkunft"] if hard else None

    if hard and window["wert"]:
        loaded = [e.get("CONTEXT") for e in preflight.get("ollama_ps_nach", {})
                  .get("eintraege", []) if e.get("NAME") == config["modell"]]
        delivery["wirksames_fenster"] = {"gemessen": loaded, "gesetzt": window["wert"],
                                         "quelle": "`ollama ps`, Spalte CONTEXT"}
        if loaded and loaded[0] != window["wert"]:
            delivery["verletzt"].append("wirksames_fenster")
            delivery["urteil"] = "LIEFERAUSFALL"

    try:
        require_delivery(delivery)
    except DeliveryFailure as exc:
        print(json.dumps({"bedingung": args.condition, "slot": args.slot,
                          "urteil": "LIEFERAUSFALL",
                          "einordnung": "Der Lauf wird NICHT als Lauf gezaehlt und ist "
                                        "KEIN Modellbefund (Z1-Praezedenz "
                                        "`k2_trunkiert`).",
                          "lieferzusicherung": delivery},
                         indent=2, ensure_ascii=False), flush=True)
        raise

    choice = (payload.get("choices") or [{}])[0]
    content = (choice.get("message") or {}).get("content") or ""
    levels = resource_levels()
    validation = build_validation(content, rendered["schema"], set(levels), levels)

    manifest = {
        "schema": "z2-run-manifest/1",
        "bedingung": config["bedingung"],
        "zelle": args.condition,
        "slot": args.slot,
        "protokoll": {**rendered["protokoll"],
                      "stand": "eingefroren; Kopf-Freeze-Vermerk im Dokument"},
        "nachrichten": {
            "system_sha256": sha256_text(rendered["messages"][0]["content"]),
            "system_bytes": nbytes(rendered["messages"][0]["content"]),
            "user_sha256": sha256_text(rendered["messages"][1]["content"]),
            "user_bytes": nbytes(rendered["messages"][1]["content"]),
            "struktur": "zwei Nachrichten nach A2/R3",
        },
        "eingaben": rendered["eingaben"],
        "modell": config["modell"],
        "modell_echo": payload.get("model"),
        "provider": config["provider"],
        "base_url": config["base_url"],
        "endpunkt": config["endpunkt"],
        "schemaname": rendered["schema"]["name"],
        "fenster": {"gesetzt": window,
                    "wirksam": preflight.get("ollama_ps_nach", {}).get("eintraege")
                    if config["provider"] == "ollama" else
                    "nicht kontrollierbar und nicht ablesbar (fremder Anbieter)"},
        "ollama": {**preflight, "digest": ollama_digest(config["modell"])}
        if config["provider"] == "ollama" else None,
        "delivery_assurance": config["delivery_assurance"],
        "delivery_assurance_begruendung": config["delivery_assurance_begruendung"],
        "lieferzusicherung": delivery,
        "bytegatter": gates,
        "zeitstempel": {"start": started, "ende": finished},
        "werkzeug": {"pfad": str(Path(__file__).resolve().relative_to(REPO)),
                     "sha256": sha256_file(Path(__file__).resolve())},
        "git_head": git("rev-parse", "HEAD"),
        "aufruf": {"temperature": 0, "seed": 0,
                   "seed_hinweis": "gesendet, aber nicht als wirksam angenommen "
                                   "(Z1-Protokoll §3.3 (1), T-Z1-5)",
                   "max_tokens": "nicht gesetzt -- ein abgeschnittenes Generat saehe wie "
                                 "Modellversagen aus (§3b, Generat-Reserve)",
                   "options": "nicht gesendet -- das Fenster ist eine Eigenschaft des "
                              "Servers (systemd-Drop-in), nicht des Calls"},
    }
    meta = {
        "modell": config["modell"], "modell_echo": payload.get("model"),
        "base_url": config["base_url"], "endpunkt": config["endpunkt"],
        "http_status": response["http_status"], "latenz_ms": response["latenz_ms"],
        "usage": usage, "system_fingerprint": payload.get("system_fingerprint"),
        "finish_reason": choice.get("finish_reason"),
        "temperature": 0, "seed": 0, "schemaname": rendered["schema"]["name"],
        "delivery_assurance": config["delivery_assurance"],
        "zeitstempel": {"start": started, "ende": finished},
    }

    target.mkdir(parents=True, exist_ok=False)
    (target / "prompt.txt").write_text(render_prompt_file(rendered["messages"]),
                                       encoding="utf-8")
    (target / "raw_response.json").write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (target / "validation.json").write_text(
        json.dumps(validation, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (target / "meta.json").write_text(
        json.dumps(meta, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (target / "run_manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    sums = write_block_sums(args.condition)

    print(json.dumps({
        "bedingung": args.condition, "slot": args.slot,
        "abgelegt": str(target.relative_to(REPO)),
        "sha256sums": str(sums.relative_to(REPO)) if sums else None,
        "lieferzusicherung": delivery["urteil"],
        "schema_konformitaet": validation["schema_konformitaet"]["urteil"],
        "z2w": validation["z2w"]["aggregat"],
        "nachzupflegen_von_hand": "data/z2/MANIFEST.md -- lebendes Dokument, ungehasht",
    }, indent=2, ensure_ascii=False))
    return 0


# --------------------------------------------------------------------------
# subcommand: selftest -- offline, writes to /tmp only, never to data/
# --------------------------------------------------------------------------

FIXTURES = Path(__file__).resolve().parent / "fixtures/z2"

# Each probe carries its EXPECTED finding. A probe that passes is a defect of
# the tool, not a success -- the expectation is what is asserted, not the run.
PARSE_PROBES: list[dict[str, str]] = [
    {"nr": "P", "datei": "antwort_positiv.json", "stufe": "positiv",
     "erwartet": "schemakonform, beide Vorschlaege wohlgeformt, validation.json geschrieben"},
    {"nr": "1", "datei": "antwort_negativ_01_leere_regelliste.json", "stufe": "schema",
     "erwartet": "Schemaverstoss: minItems auf `rules`", "muster": "minItems: 1"},
    {"nr": "2", "datei": "antwort_negativ_02_leere_components.json", "stufe": "schema",
     "erwartet": "Schemaverstoss: minItems auf `scope.components`", "muster": "minItems: 1"},
    {"nr": "3", "datei": "antwort_negativ_03_fehlendes_pflichtfeld.json", "stufe": "schema",
     "erwartet": "Schemaverstoss: Pflichtfeld `severity` fehlt", "muster": "'severity' fehlt"},
    {"nr": "4", "datei": "antwort_negativ_04_zusaetzliches_feld.json", "stufe": "schema",
     "erwartet": "Schemaverstoss: zusaetzliches Feld `kind`",
     "muster": "zusaetzliches Feld 'kind'"},
    {"nr": "5", "datei": "antwort_negativ_05_severity_enum.json", "stufe": "schema",
     "erwartet": "Schemaverstoss: `severity` ausserhalb des Enums", "muster": "steht nicht im Enum"},
    {"nr": "6", "datei": "antwort_negativ_06_component_unaufloesbar.json", "stufe": "z2w",
     "erwartet": "Z2-W: scope.components nicht aufloesbar", "muster": "nicht gegen ist_modell.yaml"},
    {"nr": "7", "datei": "antwort_negativ_07_id_doppelt.json", "stufe": "z2w",
     "erwartet": "Z2-W: id im Lauf nicht eindeutig", "muster": "nicht eindeutig"},
    {"nr": "8", "datei": "antwort_negativ_08_statement_wiederholt_category.json", "stufe": "z2w",
     "erwartet": "Z2-W: statement wiederholt die category", "muster": "wiederholt id oder category"},
    {"nr": "9", "datei": "antwort_negativ_09_statement_leer.json", "stufe": "z2w",
     "erwartet": "Z2-W: statement leer", "muster": "statement ist leer"},
    # S4b: the observation, not a criterion -- an artefact id in the scope is
    # WELL-FORMED, and it is counted on its level.
    {"nr": "G", "datei": "antwort_positiv_artefakt_scope.json", "stufe": "granularitaet",
     "erwartet": "wohlgeformt; gezaehlt package 1, module 1, artefact 1, unresolved 0",
     "granularitaet": {"package": 1, "module": 1, "artefact": 1, "unresolved": 0}},
]

# The delivery probes, with fed-in `usage` values -- no network, no model.
DELIVERY_PROBES: list[dict[str, Any]] = [
    {"nr": "10", "reported": 16386, "assurance": "hard",
     "erwartet": "(b3) greift, ABBRUCH als LIEFERAUSFALL", "greift": ["b3_halbfenster"]},
    {"nr": "11", "reported": 12000, "assurance": "hard",
     "erwartet": "(b2) greift (unter M11a)", "greift": ["b2_monotonie"]},
    {"nr": "12", "reported": 32750, "assurance": "hard",
     "erwartet": "(b) greift", "greift": ["b_fenstergleichstand"]},
    {"nr": "13", "reported": 23405, "assurance": "hard",
     "erwartet": "alle drei schweigen, Lauf zulaessig", "greift": []},
    {"nr": "14", "reported": 16386, "assurance": "record_only",
     "erwartet": "(b) und (b3) greifen NICHT", "greift": []},
    {"nr": "14", "reported": 12000, "assurance": "record_only",
     "erwartet": "(b2) greift, Grund im Record vermerkt", "greift": ["b2_monotonie"]},
    {"nr": "14", "reported": 32750, "assurance": "record_only",
     "erwartet": "(b) greift NICHT", "greift": []},
    {"nr": "14", "reported": 23405, "assurance": "record_only",
     "erwartet": "kein Kriterium greift", "greift": []},
    # S4b: the band is two-sided, and it is the ONLY rule on the target count.
    # `band_verletzt` asserts the band itself; `greift` stays the assertion on
    # the three detector criteria, which the band never touches.
    {"nr": "S4b-1", "reported": 23250, "assurance": "hard",
     "erwartet": "LIEFERAUSFALL, Grund: unter dem Band", "greift": [],
     "band_verletzt": True, "muster": "unter dem Band"},
    {"nr": "S4b-2", "reported": 23400, "assurance": "hard",
     "erwartet": "zulaessig, alle Kriterien schweigen", "greift": [],
     "band_verletzt": False, "muster": "im Band"},
    # the regression probe of S4b: BELOW the target count, INSIDE the band.
    # Under the withdrawn shortfall rule this was a delivery failure.
    {"nr": "S4b-3", "reported": 23300, "assurance": "hard",
     "erwartet": "zulaessig (unter dem Sollwert, im Band) -- belegt die Ruecknahme",
     "greift": [], "band_verletzt": False, "muster": "im Band"},
]


def cmd_selftest(args: argparse.Namespace) -> int:
    workdir = Path(args.workdir)
    workdir.mkdir(parents=True, exist_ok=True)
    if ARCHIVE_ROOT in workdir.resolve().parents or workdir.resolve() == ARCHIVE_ROOT:
        raise Fail(f"Der Selbsttest schreibt nie nach {ARCHIVE_ROOT}; {workdir} liegt darin.")

    text = PROTOCOL.read_text(encoding="utf-8")
    schema = extract_response_schema(text)
    levels = resource_levels()
    ids = set(levels)
    results: list[dict[str, Any]] = []

    # (0) the two byte gates, offline -- the precondition of every call
    rendered = render_messages()
    gates = gate_report(rendered)
    results.append({"probe": "G1/G2", "erwartet": "beide Gatter GEHALTEN",
                    "erhalten": gates["urteil"],
                    "bestanden": gates["urteil"] == "GEHALTEN",
                    "detail": [{k: g[k] for k in
                                ("gatter", "soll_sha256", "ist_sha256", "soll_bytes",
                                 "ist_bytes", "urteil")} for g in gates["gatter"]]})

    # (1)-(9) plus the positive probe
    for probe in PARSE_PROBES:
        raw = (FIXTURES / probe["datei"]).read_text(encoding="utf-8")
        validation = build_validation(raw, schema, ids, levels)
        schema_errors = validation["schema_konformitaet"]["verstoesse"]
        aggregate = validation["z2w"]["aggregat"]
        findings = [f for rule in validation["z2w"]["je_vorschlag"] for f in rule["befunde"]]
        if probe["stufe"] == "positiv":
            got = (f"schema: {validation['schema_konformitaet']['urteil']}, "
                   f"z2w: {aggregate['wohlgeformt']}/{aggregate['vorschlaege']} wohlgeformt")
            written = workdir / "validation_positivprobe.json"
            written.write_text(json.dumps(validation, indent=2, ensure_ascii=False) + "\n",
                               encoding="utf-8")
            passed = (not schema_errors and aggregate["vorschlaege"] == 2
                      and aggregate["wohlgeformt"] == 2 and written.exists())
            results.append({"probe": probe["nr"], "datei": probe["datei"],
                            "erwartet": probe["erwartet"], "erhalten": got,
                            "geschrieben": str(written), "bestanden": passed})
            continue
        if probe["stufe"] == "granularitaet":
            counted = [r["granularitaet"] for r in validation["z2w"]["je_vorschlag"]]
            got = {"wohlgeformt": f"{aggregate['wohlgeformt']}/{aggregate['vorschlaege']}",
                   "granularitaet_je_vorschlag": counted,
                   "vorschlaege_mit_artefakt_id":
                       validation["z2w"]["granularitaet"]
                       ["vorschlaege_mit_mindestens_einer_artefakt_id"]}
            hit = (not schema_errors and aggregate["vorschlaege"] == 1
                   and aggregate["wohlgeformt"] == 1
                   and counted == [probe["granularitaet"]]
                   and got["vorschlaege_mit_artefakt_id"] == 1)
            results.append({"probe": probe["nr"], "datei": probe["datei"],
                            "erwartet": probe["erwartet"], "erhalten": got,
                            "bestanden": hit,
                            "einordnung": GRANULARITY_NOTE})
            continue
        if probe["stufe"] == "schema":
            hit = any(probe["muster"] in error for error in schema_errors)
            got = schema_errors or ["keine"]
        else:
            hit = any(probe["muster"] in finding for finding in findings) and not schema_errors
            got = {"schemaverstoesse": schema_errors, "z2w_befunde": findings}
        results.append({"probe": probe["nr"], "datei": probe["datei"],
                        "erwartet": probe["erwartet"], "erhalten": got, "bestanden": hit})

    # (10)-(14) the delivery probes
    targets = registered_targets()
    window = configured_window(args.context_file)["wert"] or 32768
    for probe in DELIVERY_PROBES:
        hard = probe["assurance"] == "hard"
        report = delivery_check(
            reported=probe["reported"],
            window=window if hard else None,
            monotony_ref=targets["monotonie_bezug"]["wert"],
            soll=targets["soll_prompt_tokens"]["wert"] if hard else None,
            assurance=probe["assurance"])
        detector_hits = [c for c in report["verletzt"]
                         if c in {"b_fenstergleichstand", "b2_monotonie", "b3_halbfenster"}]
        reasons = {c["kriterium"]: c["grund_wenn_aus"] for c in report["kriterien"]
                   if not c["gilt"]}
        band = next(c for c in report["kriterien"] if c["kriterium"] == "soll_toleranz")
        # The band assertion is OPTIONAL, so that the probes registered before
        # S4b keep asserting exactly what they asserted then: the detectors.
        band_ok = True
        if "band_verletzt" in probe:
            band_ok = (("soll_toleranz" in report["verletzt"]) == probe["band_verletzt"]
                       and probe["muster"] in band["rechnung"])
        results.append({
            "probe": probe["nr"],
            "eingespeist": {"prompt_tokens": probe["reported"],
                            "delivery_assurance": probe["assurance"], "fenster": window},
            "erwartet": probe["erwartet"],
            "erhalten": {"urteil": report["urteil"], "verletzt": report["verletzt"],
                         "band": band["rechnung"],
                         "abgeschaltete_kriterien_mit_grund": reasons},
            "bestanden": detector_hits == probe["greift"] and band_ok,
        })

    # (15) slot protection
    (workdir / "k2_b1" / "run0").mkdir(parents=True, exist_ok=True)
    guard_message, aborted = None, False
    try:
        require_free_slot("k2_b1", "run0", root=workdir)     # the real guard, not a copy
    except Fail as exc:
        aborted, guard_message = True, str(exc)
    free_slot = require_free_slot("k2_b1", "run2", root=workdir)
    results.append({
        "probe": "15", "erwartet": "ABBRUCH, kein Ueberschreiben",
        "erhalten": guard_message, "bestanden": aborted,
        "gegenprobe_freier_slot": f"{free_slot} ist frei und wird durchgelassen, wie es soll",
    })

    passed = sum(1 for r in results if r["bestanden"])
    summary = {"unterbefehl": "selftest", "netz": "nein", "modell": "nein",
               "arbeitsverzeichnis": str(workdir),
               "proben": len(results), "bestanden": passed,
               "durchgefallen": [r["probe"] for r in results if not r["bestanden"]],
               "ergebnisse": results}
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    return 0 if passed == len(results) else 1


# --------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="befehl", required=True)

    render = sub.add_parser("render", help="Prompt bauen, Hashes ausgeben, NICHTS senden")
    render.add_argument("--write-prompt", help="gerenderte prompt.txt zusaetzlich hierhin")
    render.set_defaults(func=cmd_render)

    selftest = sub.add_parser("selftest", help="offline, ohne Netz und ohne Modell")
    selftest.add_argument("--workdir", default="/tmp/run_z2_selftest")
    selftest.add_argument("--context-file", default=CONTEXT_FILE)
    selftest.set_defaults(func=cmd_selftest)

    probe = sub.add_parser("probe", help="Erreichbarkeitssonde, triviale Nutzlast")
    probe.add_argument("--condition", required=True, choices=sorted(CONDITIONS))
    probe.add_argument("--context-file", default=CONTEXT_FILE)
    probe.add_argument("--timeout", type=int, default=900)
    probe.add_argument("--out", help="Datensatz zusaetzlich als JSON hierhin")
    probe.set_defaults(func=cmd_probe)

    run = sub.add_parser("run", help="EIN Z2-Lauf einer Bedingung in einen Slot")
    run.add_argument("--condition", required=True, choices=sorted(CONDITIONS))
    run.add_argument("--slot", required=True, choices=SLOTS)
    run.add_argument("--context-file", default=CONTEXT_FILE)
    run.add_argument("--timeout", type=int, default=3600)
    run.set_defaults(func=cmd_run)

    args = parser.parse_args()
    try:
        return args.func(args)
    except Fail as exc:
        print(f"ABBRUCH ({args.befehl}): {exc}", flush=True)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
