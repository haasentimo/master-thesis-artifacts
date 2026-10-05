#!/usr/bin/env python3
"""C3b — deskriptive Auswertung eines Kontrolllaufs. ZAEHLT UND KLASSIFIZIERT, bewertet nicht.

Die Frage, ob ein Finding „berechtigt" ist, gehoert nach Kapitel 7. Dieses Skript
beantwortet ausschliesslich die Zaehlfragen des Auftrags C3b §4:

  4a  je Run-Index: Module mit mindestens einem Finding, Gesamtzahl der Findings,
      Verteilung ueber die sechs Kategorien und die 19 Komponenten
  4b  die beiden VORREGISTRIERTEN Meldungen (Protokoll §5 Rev. 16 / Rev. 18),
      getrennt gefuehrt, mit `rule_id` und `subject` woertlich
  4c  Median ueber die drei Laeufe als Headline-Zahl (§5), Einzellaeufe daneben,
      Spannweite ungeglaettet
  4d  alle uebrigen Findings tabellarisch
  4e  halluzinierte `rule_id` — Zahl der Laeufe mit unbekanntem Regelbezug und ob
      der Lauf dadurch invalidiert wurde (B1 D1: llmChecker.ts:273-276 verwirft den
      GANZEN Versuch, die Findings erscheinen deshalb nicht in `findings`, sondern
      nur im `raw_response` des ungueltigen Versuchs)

Der Filter aus Protokoll §4/§6 Nachtrag Rev. 25 greift VOR jeder Zahl:
`rule_id`-Praefix `DERIVED:` ist der deterministische Pfad (K1), jedes andere
`rule_id` ist der LLM-Pfad (K2/K3). Eine Gesamtzahl allein ist ungueltig.
"""

from __future__ import annotations

import argparse
import json
import re
import statistics
import sys
from collections import Counter, defaultdict
from pathlib import Path

import yaml

DERIVED_PREFIX = "DERIVED:"

# Protokoll §5 Nachtrag Rev. 16 und Rev. 18 — die beiden vorregistrierten Meldungen.
PREREG_FACADE_MODULE = "depot.core.adapters"
PREREG_FACADE_RULE = "R-PROTECT-1"
PREREG_PORT_RULES = {"R-PORT-2": "depot.orders.services.catalog_service",
                     "R-PORT-3": "depot.orders.services.refund_service"}


def load_soll(path: Path) -> tuple[dict[str, str], list[str]]:
    """module -> component, plus die Komponentenliste in Soll-Reihenfolge."""
    soll = yaml.safe_load(path.read_text(encoding="utf-8"))
    mod2comp: dict[str, str] = {}
    comps: list[str] = []

    def rec(resources: list[dict]) -> None:
        for r in resources:
            children = r.get("children")
            if children and any("children" not in c for c in children):
                cid = r["id"]
                comps.append(cid)
                for c in children:
                    if "children" not in c:
                        mod2comp[c["id"]] = cid
            if children:
                rec(children)

    rec(soll["resources"])
    return mod2comp, comps


def load_rules(path: Path) -> tuple[set[str], dict[str, str], list[str]]:
    d = yaml.safe_load(path.read_text(encoding="utf-8"))
    ids = {r["id"] for r in d["rules"]}
    cat = {r["id"]: r["category"] for r in d["rules"]}
    cats = sorted({r["category"] for r in d["rules"]})
    return ids, cat, cats


def hallucinated_in_raw(raw: str, known: set[str]) -> list[str]:
    """`rule_id`-Werte einer verworfenen Antwort. Erst als JSON, dann per Regex."""
    found: list[str] = []
    try:
        obj = json.loads(raw)
        for v in obj.get("violations", []) or []:
            rid = v.get("rule_id")
            if rid is not None:
                found.append(str(rid))
    except (json.JSONDecodeError, AttributeError, TypeError):
        found = re.findall(r'"rule_id"\s*:\s*"([^"]*)"', raw or "")
    return [r for r in found if r not in known]


def subject_str(subject: dict | None) -> str:
    if not subject:
        return ""
    if subject.get("offending_type") is not None:
        return f"offending_type={subject['offending_type']}"
    return f"from={subject.get('from')} to={subject.get('to')}"


def evaluate(label: str, jsonl: Path, jsonout: Path, soll: Path, rules: Path, control: Path) -> None:
    mod2comp, components = load_soll(soll)
    known_rules, rule_cat, categories = load_rules(rules)
    control_modules = [
        p.removeprefix("src/").removesuffix(".py").removesuffix("/__init__").replace("/", ".")
        for p in control.read_text(encoding="utf-8").split()
    ]
    result = json.loads(jsonout.read_text(encoding="utf-8"))
    calls = [json.loads(l) for l in jsonl.read_text(encoding="utf-8").splitlines() if l.strip()]
    calls = [c for c in calls if c.get("record_type") == "llm_call"]

    print("=" * 78)
    print(f"C3b — Auswertung {label}")
    print("=" * 78)
    print(f"Kontrollmodule    : {len(control_modules)}")
    print(f"Komponenten (Soll): {len(components)}")
    print(f"Kategorien (Soll) : {len(categories)}  {categories}")
    print(f"bekannte rule_id  : {len(known_rules)}  {sorted(known_rules)}")
    print()

    # ---- 4a ---------------------------------------------------------------
    print("-" * 78)
    print("[4a] Je Run-Index: Module mit Finding, Gesamtzahl, Kategorien, Komponenten")
    print("-" * 78)
    per_run_llm: dict[int, list[dict]] = {}
    per_run_derived: dict[int, list[dict]] = {}
    for run in result["runs"]:
        idx = run["run_index"]
        fs = run["findings"]
        per_run_derived[idx] = [f for f in fs if f["rule_id"].startswith(DERIVED_PREFIX)]
        per_run_llm[idx] = [f for f in fs if not f["rule_id"].startswith(DERIVED_PREFIX)]

    for idx in sorted(per_run_llm):
        llm, der = per_run_llm[idx], per_run_derived[idx]
        mods = {f["module"] for f in llm}
        print(f"\nrun_index {idx}")
        print(f"  Records getrennt (Rev. 25) : DERIVED: {len(der)}   LLM {len(llm)}")
        print(f"  Module mit >=1 Finding     : {len(mods)} von {len(control_modules)}")
        print(f"  Findings insgesamt (LLM)   : {len(llm)}")
        cc = Counter(f["category"] for f in llm)
        print("  Verteilung ueber die sechs Kategorien:")
        for c in categories:
            print(f"      {c:28s} {cc.get(c, 0)}")
        unknown_cats = {c for c in cc if c not in categories}
        if unknown_cats:
            print(f"      AUSSERHALB der sechs: {sorted(unknown_cats)}")
        pc = Counter(f["component"] for f in llm)
        print("  Verteilung ueber die 19 Komponenten (nur besetzte):")
        for c in components:
            if pc.get(c):
                print(f"      {c:28s} {pc[c]}")
        print(f"      -- unbesetzt: {sum(1 for c in components if not pc.get(c))} von {len(components)}")

    # ---- 4b ---------------------------------------------------------------
    print()
    print("-" * 78)
    print("[4b] Die beiden VORREGISTRIERTEN Meldungen — getrennt gefuehrt")
    print("-" * 78)

    def hits_facade(f: dict) -> bool:
        return f["module"] == PREREG_FACADE_MODULE and f["rule_id"] == PREREG_FACADE_RULE

    def hits_port(f: dict) -> bool:
        carrier = PREREG_PORT_RULES.get(f["rule_id"])
        return carrier is not None and f["module"] != carrier

    for name, pred, ref in (
        (f"Adapterfassade {PREREG_FACADE_MODULE} / {PREREG_FACADE_RULE}", hits_facade, "§5 Nachtrag Rev. 16"),
        ("Nicht-Traeger-Portregel auf orders_services (R-PORT-2 / R-PORT-3)", hits_port, "§5 Nachtrag Rev. 18"),
    ):
        runs_hit = [idx for idx in sorted(per_run_llm) if any(pred(f) for f in per_run_llm[idx])]
        print(f"\n{name}   [{ref}]")
        print(f"  aufgetreten in {len(runs_hit)} von {len(per_run_llm)} Laeufen: {runs_hit or '—'}")
        for idx in sorted(per_run_llm):
            for f in per_run_llm[idx]:
                if pred(f):
                    print(f"    run {idx}  rule_id={f['rule_id']}  module={f['module']}"
                          f"  component={f['component']}  category={f['category']}")
                    print(f"             subject (woertlich): {json.dumps(f['subject'], ensure_ascii=False)}")

    # ---- 4c ---------------------------------------------------------------
    print()
    print("-" * 78)
    print("[4c] Median ueber die Laeufe als Headline-Zahl, Einzellaeufe und Spannweite")
    print("-" * 78)
    for what, vals in (
        ("Findings (LLM) je Lauf", [len(per_run_llm[i]) for i in sorted(per_run_llm)]),
        ("Module mit >=1 Finding", [len({f['module'] for f in per_run_llm[i]}) for i in sorted(per_run_llm)]),
    ):
        med = statistics.median(vals)
        print(f"  {what:24s} Einzellaeufe {vals}   MEDIAN {med:g}"
              f"   Spannweite {min(vals)}–{max(vals)} (= {max(vals) - min(vals)})")
    mods_med = statistics.median([len({f["module"] for f in per_run_llm[i]}) for i in sorted(per_run_llm)])
    print(f"\n  Falsch-Positiv-Rate auf Modulebene (Median / {len(control_modules)} Kontrollmodule): "
          f"{mods_med:g}/{len(control_modules)} = {mods_med / len(control_modules):.3f}")
    print("  Keine Interpretation — das ist Kapitel 7.")

    # ---- 4d ---------------------------------------------------------------
    print()
    print("-" * 78)
    print("[4d] Alle UEBRIGEN Findings tabellarisch (ohne die vorregistrierten), ohne Bewertung")
    print("-" * 78)
    print(f"{'run':>3} | {'Modul':46s} | {'Komponente':24s} | {'rule_id':14s} | {'Kategorie':26s} | subject")
    print("-" * 78)
    rest = 0
    for idx in sorted(per_run_llm):
        for f in per_run_llm[idx]:
            if hits_facade(f) or hits_port(f):
                continue
            rest += 1
            print(f"{idx:>3} | {f['module']:46s} | {str(f['component']):24s} | {f['rule_id']:14s} | "
                  f"{f['category']:26s} | {subject_str(f.get('subject'))}")
    if not rest:
        print("  (keine)")
    print(f"\n  uebrige Findings insgesamt ueber alle Laeufe: {rest}")

    # ---- 4e ---------------------------------------------------------------
    print()
    print("-" * 78)
    print("[4e] Halluzinierte rule_id (B1 D1 — ein unbekanntes rule_id verwirft den GANZEN Versuch)")
    print("-" * 78)
    per_run_halluc: dict[int, Counter] = defaultdict(Counter)
    per_run_final_invalid: dict[int, list[str]] = defaultdict(list)
    for c in calls:
        idx = c["run_index"]
        for a in c["attempts"]:
            if a.get("valid"):
                continue
            for rid in hallucinated_in_raw(a.get("raw_response") or "", known_rules):
                per_run_halluc[idx][rid] += 1
        if not c["valid_final"]:
            per_run_final_invalid[idx].append(c["module"])
    # Der andere Weg: ein unbekanntes rule_id, das dennoch in findings steht.
    in_findings: dict[int, Counter] = defaultdict(Counter)
    for idx, fs in per_run_llm.items():
        for f in fs:
            if f["rule_id"] not in known_rules:
                in_findings[idx][f["rule_id"]] += 1

    runs_with = sorted(set(per_run_halluc) | set(in_findings))
    print(f"  Laeufe mit mindestens einer unbekannten rule_id: {len(runs_with)} von {len(per_run_llm)}"
          f"  {runs_with or '—'}")
    for idx in sorted(per_run_llm):
        h, inf = per_run_halluc.get(idx, Counter()), in_findings.get(idx, Counter())
        fin = per_run_final_invalid.get(idx, [])
        print(f"\n  run_index {idx}")
        print(f"    in verworfenen Versuchen : {dict(h) or '—'}")
        print(f"    in gezaehlten Findings   : {dict(inf) or '—'}")
        print(f"    valid_final == false     : {len(fin)} Calls {fin[:6]}{' …' if len(fin) > 6 else ''}")
        if fin:
            verdikt = "JA — invalid_final_response, der Lauf ist ungueltig"
        elif inf:
            # Nach B1 D1 verwirft llmChecker.ts:273-276 den ganzen Versuch. Ein unbekanntes
            # rule_id IN den gezaehlten Findings widerspricht dem und ist selbst ein Befund.
            verdikt = ("NEIN — aber ANOMALIE: unbekanntes rule_id in den gezaehlten Findings, "
                       "obwohl llmChecker.ts:273-276 den Versuch verwerfen muesste")
        elif h:
            verdikt = "NEIN — Versuch verworfen, nach Retry gueltig"
        else:
            verdikt = "nicht zutreffend (keine unbekannte rule_id)"
        print(f"    Lauf dadurch invalidiert : {verdikt}")
    print(f"\n  Lauf-Verdikt aus invalid_reasons: {result['validity']['invalid_reasons'] or '[] (leer)'}")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--label", required=True)
    ap.add_argument("--run-log", required=True)
    ap.add_argument("--json-out", required=True)
    ap.add_argument("--soll", default="data/soll/depot_soll.ilograph.yaml")
    ap.add_argument("--rules", default="data/soll/architecture-rules.yaml")
    ap.add_argument("--control-files", default="data/soll/control_files.txt")
    a = ap.parse_args()
    evaluate(a.label, Path(a.run_log), Path(a.json_out), Path(a.soll), Path(a.rules), Path(a.control_files))
    return 0


if __name__ == "__main__":
    sys.exit(main())
