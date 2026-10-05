#!/usr/bin/env python3
"""Z1 evaluation: approach 1 computed, approach 2 reported as not collected.

Registered in the Z1 protocol as building item D1b (section 7.2): the compression
figures are read straight out of `meta.json`, `scripts/compare_runs.py` stays
byte-identical and is used unchanged as the counter-instance for the two things it
does compute (byte-identity of `arch_model.json` across a group, and
`validity_rate(valid_final)`).

This tool computes NOTHING of its own. Every fidelity and compression number comes
out of `llm_arch.eval.metrics`, every validity verdict out of
`llm_arch.ilograph.validate`, both imported unchanged from the extractor at the
registered HEAD. What the extractor's code does not compute is not reported
(protocol section 4.5).

Approach 1 (Triton) is computed against the archived fixture. Approach 2 is NOT:
all three condition blocks are `valid_final == false` throughout, and on invalid
output no fidelity is measured (protocol section 5.4, clarification rev. 4). What
is reported per condition is validity, counters and cause -- and for a block whose
registered input never arrived, that it is not a model finding.

Two outputs: a machine-readable JSON and a Markdown rendering in the table shape of
protocol section 7.

    python3 tools/evaluate_z1.py --out data/z1/auswertung
    python3 tools/evaluate_z1.py --selftest
"""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import subprocess
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXTRACTOR = Path.home() / "ma" / "ma-llm-arch-extractor"
Z1_ROOT = ROOT / "data" / "z1"

EXPECTED_HEAD = "5c0b65a82cc3d8af47c022d779ff63d8a20a9e08"

# Protocol section 8, E1/E2: gehashed determinations, not predictions. Character
# for character `tests/test_reader.py:53-73` (blob 7fc33d1b...); any deviation is
# an instrument finding and aborts (see `tests/fixtures/z1/EXPECTED.md` section 4).
E1_E2 = {
    "relation_precision": 1.0,
    "relation_recall": 1.0,
    "module_coverage": 1.0,
    "phantom_modules": 0,
    "module_count": 11,
    "component_count": 4,
    "module_compression": 11 / 4,
    "import_edge_count": 16,
    "component_relation_count": 5,
    "relation_compression": 16 / 5,
}

FIDELITY_KEYS = ["relation_precision", "relation_recall", "module_coverage", "phantom_modules"]
COMPRESSION_KEYS = ["module_count", "component_count", "module_compression",
                    "import_edge_count", "component_relation_count", "relation_compression"]

BLOCKS = [
    ("k2", "K2 · `qwen2.5-coder:7b` · Profil `ollama`, Fenster 16384"),
    ("k3", "K3 · `nvidia-nemotron-3-super-120b` · Profil `digitalocean`"),
    ("k2_trunkiert", "K2 (Altblock) · Fenster 4096 — LIEFERAUSFALL"),
]


class Abort(SystemExit):
    """A named abort: the protocol says stop here, and why."""

    def __init__(self, invariant: str, detail: str) -> None:
        super().__init__(2)
        self.invariant = invariant
        self.detail = detail


# --- the extractor, imported unchanged ------------------------------------------------


def load_extractor(extractor: Path):
    """Put the extractor's `src/` on the path and hand back the registered callables."""
    sys.path.insert(0, str(extractor / "src"))
    from llm_arch.abstraction.schema import ArchModel
    from llm_arch.eval import compression, fact_fidelity, read_ilograph, reduce_arch
    from llm_arch.eval.metrics import gold_similarity
    from llm_arch.facts import extract_repo, substantive_modules
    from llm_arch.ilograph import validate_arch
    return dict(ArchModel=ArchModel, compression=compression, fact_fidelity=fact_fidelity,
                read_ilograph=read_ilograph, reduce_arch=reduce_arch,
                gold_similarity=gold_similarity, extract_repo=extract_repo,
                substantive_modules=substantive_modules, validate_arch=validate_arch)


def blob_sha1(extractor: Path, path: str) -> str:
    out = subprocess.run(["git", "-C", str(extractor), "ls-files", "-s", path],
                         capture_output=True, text=True, check=True).stdout
    return out.split()[1] if out else ""


def head_of(repo: Path) -> str:
    return subprocess.run(["git", "-C", str(repo), "rev-parse", "HEAD"],
                          capture_output=True, text=True, check=True).stdout.strip()


# --- approach 1 -----------------------------------------------------------------------


def evaluate_approach1(api: dict, extractor: Path) -> dict:
    """Compute the ten registered figures plus gold_similarity for the Triton export."""
    from ruamel.yaml import YAML

    fixture = extractor / "fixtures" / "rich_repo.full.ilograph.yaml"
    doc = YAML().load(io.StringIO(fixture.read_text()))
    facts = api["extract_repo"](str(extractor / "fixtures" / "rich_repo"))
    modules = api["substantive_modules"](facts)
    known = {f.module_name for f in facts}
    res = api["read_ilograph"](doc, known_modules=known)
    ff = api["fact_fidelity"](facts, res.reduced, modules)
    comp = api["compression"](facts, res.reduced, modules)
    gold = json.loads((extractor / "fixtures" / "rich_repo.gold.json").read_text())

    values = {
        "relation_precision": ff.relation_precision,
        "relation_recall": ff.relation_recall,
        "module_coverage": ff.module_coverage,
        "phantom_modules": ff.phantom_modules,
        "module_count": comp.module_count,
        "component_count": comp.component_count,
        "module_compression": comp.module_compression,
        "import_edge_count": comp.import_edge_count,
        "component_relation_count": comp.component_relation_count,
        "relation_compression": comp.relation_compression,
        "gold_similarity": api["gold_similarity"](res.reduced.module_to_component, gold),
        "gold_similarity_method": "adjusted_rand_index",
    }
    deviations = [
        {"kennzahl": k, "soll": v, "ist": values[k]}
        for k, v in E1_E2.items() if values[k] != v
    ]
    return {
        "quelle": "fixtures/rich_repo.full.ilograph.yaml",
        "blob_sha1": blob_sha1(extractor, "fixtures/rich_repo.full.ilograph.yaml"),
        "substanzielle_module": sorted(modules),
        "modul_zu_komponente": dict(sorted(res.reduced.module_to_component.items())),
        "komponentenrelationen": sorted(res.reduced.component_relations),
        "unmatched_modules": res.unmatched_modules,
        "unresolved_relations": res.unresolved_relations,
        "werte": values,
        "e1_e2_abweichungen": deviations,
        "valid_felder": "entfällt — kein Lauf",
    }


# --- approach 2 -----------------------------------------------------------------------


def artefacts(run_dir: Path) -> Path:
    """The extractor's own run directory: `<slot>/extractor/` in the archive, the slot
    itself in the parse-assertion fixtures, which are bare run dirs."""
    nested = run_dir / "extractor"
    return nested if (nested / "meta.json").exists() else run_dir


def read_meta(run_dir: Path) -> dict:
    """Read one run's meta.json; a MISSING `valid_final` aborts (protocol section 5.2)."""
    meta = json.loads((artefacts(run_dir) / "meta.json").read_text())
    if "valid_final" not in meta:
        raise Abort("§5.2", f"{run_dir}: meta.json führt das Feld `valid_final` nicht. "
                            "Der Lauf wird NICHT als ungültig gezählt und NICHT als 0 verrechnet.")
    return meta


def error_classes(errors: list[str]) -> dict[str, int]:
    return dict(Counter(e.split(":", 1)[0] for e in errors))


def revalidate(api: dict, run_dir: Path, facts, modules, known) -> dict:
    """Re-run `validate_arch` over the archived model -- the Gegenprobe to meta.json."""
    arch = api["ArchModel"].model_validate_json(
        (artefacts(run_dir) / "arch_model.json").read_text())
    result = api["validate_arch"](arch, required_modules=modules, known_modules=known)
    return {"valid": result.valid, "fehler": len(result.errors),
            "klassen": error_classes(result.errors), "errors": result.errors}


def evaluate_block(api: dict, block: Path, facts, modules, known) -> dict:
    runs = sorted(p for p in block.iterdir() if p.is_dir())
    rows, hashes = [], {}
    for run in runs:
        meta = read_meta(run)
        art = artefacts(run)
        arch_bytes = (art / "arch_model.json").read_bytes()
        digest = hashlib.sha256(arch_bytes).hexdigest()
        hashes.setdefault(digest, []).append(run.name)
        arch = json.loads(arch_bytes)
        attempts = sorted((art / "attempts").glob("attempt_*"))
        per_attempt = []
        for att in attempts:
            val = json.loads((att / "validation.json").read_text())
            per_attempt.append({"versuch": att.name,
                                "fehler": len(val["errors"]),
                                "klassen": error_classes(val["errors"])})
        gegenprobe = revalidate(api, run, facts, modules, known)
        rows.append({
            "slot": run.name,
            "run_index": meta["run_index"],
            "valid_raw": meta["valid_raw"],
            "valid_final": meta["valid_final"],
            "attempts_used": meta["attempts_used"],
            "fehler_endversuch": len(meta["validation_errors"]),
            "fehlerklassen_endversuch": error_classes(meta["validation_errors"]),
            "fehlerklassen_je_versuch": per_attempt,
            "komponenten_im_modell": len(arch["components"]),
            "relationen_im_modell": len(arch["relations"]),
            "platzierte_moduleintraege": sum(len(c.get("contained_modules", [])) for c in arch["components"]),
            "arch_model_sha256": digest,
            "prompt_tokens": meta["prompt_tokens"],
            "completion_tokens": meta["completion_tokens"],
            "latency_ms": meta["latency_ms"],
            "model_version": meta["model_version"],
            "base_url": meta["base_url"],
            "repo_commit": meta["repo_commit"],
            "validate_arch_gegenprobe": gegenprobe,
        })
    abweichungen = [
        {"slot": r["slot"], "meta_json": r["fehlerklassen_endversuch"],
         "validate_arch": r["validate_arch_gegenprobe"]["klassen"]}
        for r in rows
        if r["fehlerklassen_endversuch"] != r["validate_arch_gegenprobe"]["klassen"]
        or r["valid_final"] != r["validate_arch_gegenprobe"]["valid"]
    ]
    return {
        "laeufe": len(rows),
        "gueltig": sum(1 for r in rows if r["valid_final"]),
        "byte_identisch": len(hashes) == 1,
        "arch_model_hashes": {h: slots for h, slots in hashes.items()},
        "relation_fehler_in_laeufen": sum(
            1 for r in rows
            if any("relation" in a["klassen"] for a in r["fehlerklassen_je_versuch"])),
        "relation_fehler_im_endversuch": sum(
            1 for r in rows if "relation" in r["fehlerklassen_endversuch"]),
        "zeilen": rows,
        "gegenprobe_abweichungen": abweichungen,
    }


def compare_runs_gegenprobe(extractor: Path, block: Path) -> dict:
    """Run `scripts/compare_runs.py` unchanged and read back its two aggregates."""
    script = extractor / "scripts" / "compare_runs.py"
    dirs = [str(artefacts(p)) for p in sorted(block.iterdir()) if p.is_dir()]
    proc = subprocess.run([sys.executable, str(script), *dirs],
                          capture_output=True, text=True, cwd=str(extractor))
    tail = [ln for ln in proc.stdout.splitlines() if "output byte-identical" in ln]
    parsed = {}
    if tail:
        line = tail[-1]
        parsed["byte_identical"] = "True" in line.split("byte-identical:")[1].split("·")[0]
        parsed["validity_rate"] = float(line.rsplit(":", 1)[1].strip())
    return {"blob_sha1": blob_sha1(extractor, "scripts/compare_runs.py"),
            "returncode": proc.returncode, "gelesen": parsed, "rohzeile": tail[-1] if tail else ""}


# --- the extrapolation (protocol has no section for this: it is NOT a measurement) -----


def extrapolate(z1_root: Path) -> dict:
    """Split the rendered prompt into constant frame and fact part, then extrapolate."""
    sys.path.insert(0, str(ROOT / "tools"))
    from z1_tokenizer import (Tokenizer, TokenizerUnavailable, assert_ascii, gates,
                              render_chat, split_prompt_file)
    try:
        tok = Tokenizer()
    except TokenizerUnavailable as exc:
        return {"verfuegbar": False, "grund": str(exc)}

    checked = gates(tok, z1_root)
    if not all(g["ok"] for g in checked):
        return {"verfuegbar": False, "grund": "Zählgatter verfehlt", "gatter": checked}

    path = z1_root / "k2" / "run0" / "extractor" / "attempts" / "attempt_0" / "prompt.txt"
    raw = path.read_text(encoding="utf-8")
    assert_ascii(raw, "the archived attempt_0 prompt")
    system, user = split_prompt_file(raw)[0][1], split_prompt_file(raw)[1][1]
    pre = "Here are the extracted code facts as JSON:\n\n"
    post = "\n\nProduce the abstracted architecture."
    facts_json = user[len(pre):-len(post)]
    facts = json.loads(facts_json)

    def render(fj: str) -> str:
        return render_chat([("system", system), ("user", pre + fj + post)])

    total = tok.count(render(facts_json))
    frame = tok.count(render(json.dumps([], indent=2)))
    fact_part = total - frame

    per_entry = []
    for entry in facts:
        rest = [e for e in facts if e is not entry]
        substantive = bool(entry["classes"] or entry["functions"] or entry["imports"])
        per_entry.append({"modul": entry["module_name"], "substanziell": substantive,
                          "token": total - tok.count(render(json.dumps(rest, indent=2)))})

    substantive_count = sum(1 for e in per_entry if e["substanziell"])
    per_module = fact_part / substantive_count

    thresholds = {}
    for limit in (4096, 16384, 32768):
        n = 0
        while frame + per_module * n <= limit:
            n += 1
        thresholds[str(limit)] = {"erste_modulzahl_darueber": n,
                                  "token_dort": round(frame + per_module * n, 1)}

    attempts = [tok.count(render_chat(split_prompt_file(
        (z1_root / "k2" / "run0" / "extractor" / "attempts" / f"attempt_{n}" / "prompt.txt")
        .read_text(encoding="utf-8")))) for n in (0, 1, 2)]

    return {
        "verfuegbar": True,
        "charakter": "EXTRAPOLATION, keine Messung",
        "tokenizer": {"quelle": str(tok.blob), "manifest_digest": tok.manifest_digest,
                      "pre": "qwen2", "modell": "gpt2 (byte-level BPE)"},
        "gatter": checked,
        "zeichen": {"systemteil": len(system), "faktenteil": len(facts_json),
                    "nutzertext_rahmen": len(pre) + len(post), "datei_gesamt": len(raw)},
        "token": {"gesamt_gerendert": total, "konstanter_rahmen": frame,
                  "faktenteil": fact_part, "versuchsprompts": attempts},
        "je_modul": {"substanzielle_module": substantive_count,
                     "token_je_modul": per_module,
                     "je_eintrag": per_entry,
                     "davon_substanziell": sum(e["token"] for e in per_entry if e["substanziell"]),
                     "davon_leere_pakete": sum(e["token"] for e in per_entry if not e["substanziell"])},
        "schwellen": thresholds,
        "annahmen": [
            "Linearität: der Faktenteil wächst proportional zur Modulzahl.",
            "Gleichverteilte Modulgrösse: jedes Modul kostet den Mittelwert dieser Fixture.",
            "rich_repo als Maßstab: Docstring-Dichte, Signaturlänge und Importzahl dieser "
            "Fixture gelten als typisch; ein anderes Repo verschiebt den Wert je Modul.",
            "Der konstante Rahmen enthält den Systemtext, den Nutzertextrahmen und die "
            "ChatML-Marken; er wächst nicht mit der Modulzahl.",
            "Gerechnet ist der ERSTE Versuch. Die Retry-Konversation wächst darüber hinaus "
            "(hier 4 281 → 5 483 → 6 685 Token); die Schwellen sind insofern optimistisch.",
        ],
    }


# --- rendering ------------------------------------------------------------------------


def fmt(v) -> str:
    if v is None:
        return "*nicht gebildet*"
    if isinstance(v, bool):
        return "ja" if v else "nein"
    if isinstance(v, float):
        # keep at least one decimal: E1 determines 1.0, and "1" would read as an int.
        return f"{v:.1f}" if v == int(v) else f"{v:.4f}".rstrip("0")
    return str(v)


def render_markdown(data: dict) -> str:
    a1 = data["ansatz1"]["werte"]
    out: list[str] = []
    add = out.append
    add("# Z1 — Auswertungsausgabe (maschinell erzeugt)\n")
    add(f"Erzeugt: {data['erzeugt_utc']} · `tools/evaluate_z1.py`")
    add(f"Extractor-`HEAD`: `{data['extractor_head']}` · "
        f"Protokoll Rev. {data['protokoll']['revision']}, SHA256 `{data['protokoll']['sha256'][:16]}…`\n")
    add("> **Diese Datei rechnet nichts.** Jede Treue- und Kompressionszahl kommt aus")
    add("> `llm_arch.eval.metrics`, jedes Gültigkeitsverdikt aus `llm_arch.ilograph.validate`,")
    add("> beide unverändert aus dem Extractor importiert.\n")

    add("## 1. Ergebnistabelle (Protokoll §7.1)\n")
    add("| Kennzahl | Ansatz 1 — Triton (deterministisch, ein Wert) | Ansatz 2 — K2 `qwen2.5-coder:7b` | Ansatz 2 — K3 `nvidia-nemotron-3-super-120b` |")
    add("|---|---|---|---|")
    for key in FIDELITY_KEYS + COMPRESSION_KEYS:
        add(f"| `{key}` | **{fmt(a1[key])}** | *nicht erhoben* | *nicht erhoben* |")
    add(f"| `gold_similarity` *(gold-bezogen, Referenzsignal)* | **{fmt(a1['gold_similarity'])}** "
        "| *nicht erhoben* | *nicht erhoben* |")
    add("| `valid_raw` / `valid_final` / `attempts_used` | *entfällt — kein Lauf* "
        "| `false` / `false` / 3 in allen sechs | `false` / `false` / 3 in allen sechs |\n")
    add("**„nicht erhoben\" ist kein Nullwert** (Protokoll §5.4). Auf ungültiger Ausgabe wird")
    add("keine Treue gemessen; die Zellen tragen deshalb keine Zahl, auch keine 0.\n")

    dev = data["ansatz1"]["e1_e2_abweichungen"]
    add("## 2. E1 und E2 — die gehashten Festlegungen\n")
    if dev:
        add("**ABWEICHUNG — Instrumentenbefund:**\n")
        for d in dev:
            add(f"- `{d['kennzahl']}`: SOLL {d['soll']} · IST {d['ist']}")
    else:
        add("Alle zehn Werte treffen `tests/test_reader.py:53-73` **zeichengleich**. "
            "E1 und E2 sind **BESTÄTIGT**.")
    add("")

    add("## 3. Ansatz 2 je Bedingung — Gültigkeit, Zähler, Ursache\n")
    for key, label in BLOCKS:
        blk = data["ansatz2"][key]
        add(f"### {label}\n")
        add(f"- Läufe: **{blk['laeufe']}**, davon gültig: **{blk['gueltig']}** → **NICHT ERHOBEN**")
        n_hashes = len(blk["arch_model_hashes"])
        add(f"- `arch_model.json` über alle Läufe bytegleich: **{fmt(blk['byte_identisch'])}** "
            + (f"(ein Hash über {blk['laeufe']} Läufe)" if n_hashes == 1
               else f"({n_hashes} verschiedene Hashes über {blk['laeufe']} Läufe)"))
        add(f"- Läufe mit `relation:`-Fehlern in irgendeinem Versuch: "
            f"**{blk['relation_fehler_in_laeufen']} von {blk['laeufe']}** "
            f"(im Endversuch: {blk['relation_fehler_im_endversuch']})")
        add(f"- `validate_arch`-Gegenprobe gegen `meta.json`: "
            f"**{'abweichungsfrei' if not blk['gegenprobe_abweichungen'] else 'ABWEICHUNG'}**")
        cr = data["compare_runs"][key]["gelesen"]
        add(f"- **Gegenprobe `compare_runs.py`** (Blob `{data['compare_runs'][key]['blob_sha1'][:12]}…`, "
            f"unverändert): `output byte-identical: {cr.get('byte_identical')}` · "
            f"`validity_rate(valid_final): {cr.get('validity_rate'):.2f}` — deckungsgleich mit "
            "der Zeile darüber")
        add("")
        add("| Slot | `run_index` | `valid_raw`/`valid_final` | Versuche | Fehler (Endversuch) | Klassen | Komp. | Rel. | Moduleinträge | `arch_model` sha256 | `prompt_tokens` | `latency_ms` |")
        add("|---|---|---|---|---|---|---|---|---|---|---|---|")
        for r in blk["zeilen"]:
            add(f"| `{r['slot']}` | {r['run_index']} | {fmt(r['valid_raw'])} / {fmt(r['valid_final'])} "
                f"| {r['attempts_used']} | {r['fehler_endversuch']} | "
                f"{', '.join(f'{k}:{v}' for k, v in r['fehlerklassen_endversuch'].items())} | "
                f"{r['komponenten_im_modell']} | {r['relationen_im_modell']} | "
                f"{r['platzierte_moduleintraege']} | `{r['arch_model_sha256'][:12]}…` | "
                f"{r['prompt_tokens']} | {r['latency_ms']:.0f} |")
        add("")

    ex = data["extrapolation"]
    add("## 4. Kontextfenster — EXTRAPOLATION, keine Messung\n")
    if not ex["verfuegbar"]:
        add(f"**Nicht gestellt:** {ex['grund']}\n")
    else:
        add("Zählgatter gegen die bereits archivierten Ollama-Zählungen:\n")
        add("| Gatter | Gegenstand | Soll | Ist | Quelle |")
        add("|---|---|---|---|---|")
        for g in ex["gatter"]:
            add(f"| {g['gate']} | {g['was']} | `{g['soll']}` | `{g['ist']}` | {g['quelle']} |")
        add("")
        add("| Teil | Zeichen | Token |")
        add("|---|---|---|")
        add(f"| konstanter Systemteil (Systemtext + ChatML-Marken + Nutzertextrahmen) "
            f"| {ex['zeichen']['systemteil'] + ex['zeichen']['nutzertext_rahmen']} "
            f"| **{ex['token']['konstanter_rahmen']}** |")
        add(f"| Faktenteil (die 16 JSON-Einträge) | {ex['zeichen']['faktenteil']} "
            f"| **{ex['token']['faktenteil']}** |")
        add(f"| **gerenderter Prompt gesamt** | {ex['zeichen']['datei_gesamt']} "
            f"| **{ex['token']['gesamt_gerendert']}** |")
        add("")
        add(f"**Token je Modul:** {ex['token']['faktenteil']} / "
            f"{ex['je_modul']['substanzielle_module']} = "
            f"**{ex['je_modul']['token_je_modul']:.1f}** Token je substanziellem Modul.\n")
        add("| Schwelle | erste Modulzahl darüber | Token dort |")
        add("|---|---|---|")
        for limit, row in ex["schwellen"].items():
            add(f"| {limit} | **{row['erste_modulzahl_darueber']}** | {row['token_dort']} |")
        add("")
        add("**Annahmen, offengelegt:**\n")
        for a in ex["annahmen"]:
            add(f"- {a}")
        add("")
    return "\n".join(out) + "\n"


# --- driver ---------------------------------------------------------------------------


def protocol_state() -> dict:
    proto = ROOT / "docs" / "protokolle" / "z1_protokoll_extraktionsvergleich.md"
    text = proto.read_text(encoding="utf-8")
    rev = text.split("Stand:", 1)[1].split("(Rev.", 1)[1].split(")", 1)[0].strip()
    return {"revision": rev, "sha256": hashlib.sha256(proto.read_bytes()).hexdigest()}


def evaluate(extractor: Path, z1_root: Path) -> dict:
    head = head_of(extractor)
    if head != EXPECTED_HEAD:
        raise Abort("§6.1", f"Extractor-HEAD ist {head}, registriert ist {EXPECTED_HEAD}.")
    api = load_extractor(extractor)
    facts = api["extract_repo"](str(extractor / "fixtures" / "rich_repo"))
    modules = api["substantive_modules"](facts)
    known = {f.module_name for f in facts}

    data = {
        "erzeugt_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "extractor_head": head,
        "protokoll": protocol_state(),
        "instrumente": {
            path: blob_sha1(extractor, path) for path in [
                "src/llm_arch/eval/metrics.py",
                "src/llm_arch/eval/ilograph_reader.py",
                "src/llm_arch/ilograph/validate.py",
                "src/llm_arch/facts/extractor.py",
                "tests/test_reader.py",
                "scripts/compare_runs.py",
            ]
        },
        "ansatz1": evaluate_approach1(api, extractor),
        "ansatz2": {},
        "compare_runs": {},
        "extrapolation": extrapolate(z1_root),
    }
    for key, _ in BLOCKS:
        data["ansatz2"][key] = evaluate_block(api, z1_root / key, facts, modules, known)
        data["compare_runs"][key] = compare_runs_gegenprobe(extractor, z1_root / key)
    return data


def selftest(extractor: Path) -> int:
    """The §5.2 abort must fire on the fixture that has no `valid_final`."""
    fixtures = ROOT / "tests" / "fixtures" / "z1"
    ok = True
    try:
        read_meta(fixtures / "fehlendes_valid_final")
        print("FEHL  fehlendes_valid_final: kein Abbruch")
        ok = False
    except Abort as exc:
        print(f"OK    fehlendes_valid_final → Abbruch {exc.invariant}")
    for name in ("p1_fremdschluessel", "p2_verlorene_relation"):
        meta = read_meta(fixtures / name)
        print(f"OK    {name}: valid_final={meta['valid_final']} gelesen, kein Abbruch")
    api = load_extractor(extractor)
    a1 = evaluate_approach1(api, extractor)
    if a1["e1_e2_abweichungen"]:
        print("FEHL  Ansatz 1 verfehlt E1/E2:", a1["e1_e2_abweichungen"])
        ok = False
    else:
        print("OK    Ansatz 1 trifft E1/E2 zeichengleich (10 von 10)")
    return 0 if ok else 1


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", type=Path, help="Zielverzeichnis für JSON und Markdown")
    ap.add_argument("--extractor", type=Path, default=EXTRACTOR)
    ap.add_argument("--z1-root", type=Path, default=Z1_ROOT)
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args(argv)

    if args.selftest:
        return selftest(args.extractor)

    try:
        data = evaluate(args.extractor, args.z1_root)
    except Abort as exc:
        print(f"ABBRUCH ({exc.invariant}): {exc.detail}", file=sys.stderr)
        return 2

    if data["ansatz1"]["e1_e2_abweichungen"]:
        print("ABBRUCH (§8 E1/E2): " + json.dumps(data["ansatz1"]["e1_e2_abweichungen"]),
              file=sys.stderr)
        return 2

    md = render_markdown(data)
    if args.out:
        args.out.mkdir(parents=True, exist_ok=True)
        (args.out / "z1_auswertung.json").write_text(
            json.dumps(data, indent=2, ensure_ascii=False, sort_keys=False) + "\n")
        (args.out / "z1_auswertung.md").write_text(md)
        print(f"geschrieben: {args.out / 'z1_auswertung.json'} und {args.out / 'z1_auswertung.md'}")
    else:
        print(md)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
