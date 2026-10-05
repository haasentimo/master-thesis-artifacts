#!/usr/bin/env python3
"""Resolve the Z2 review key and tally the filled-in assessment sheet.

Reads, never writes, the sheet (`bewertungsblatt.md`) and the assignment key
(`zuordnungsschluessel.json`), resolves the blinding, and emits every mechanically
derivable figure of protocol §7 as JSON on stdout.

The script tallies. It does not interpret: no expectation is judged, no dimension
assigned by the reviewer is corrected, completed or second-guessed. Anything that
looks inconsistent is carried into the output as a remark, unchanged.

stdlib only; deterministic (two runs produce byte-identical output). The moment the
key was opened is a registered constant, not the current clock, so repeated runs stay
byte-identical.

Usage: tools/tally_z2_review.py [--repo PATH] > data/z2/bewertung/auswertung.json
"""

import argparse
import difflib
import json
import os
import re
import sys
import unicodedata

# --- registered constants -------------------------------------------------------

# Moment the assignment key was opened, task S11. A constant and not the clock, so
# the tool stays deterministic; the same value is registered in the S11 report and in
# data/z2/MANIFEST.md.
KEY_OPENED_AT = "2026-09-04T09:38:19+02:00"
KEY_OPENED_COMMIT = "9b6c76b1fe999724b7d108d45ba7e7958fba7fe8"

# The six level-1 deviation types of the main protocol, in the order §6 lists them.
LEVEL1_CATEGORIES = [
    "FORBIDDEN_RELATION",
    "CYCLE",
    "ABSENCE_REQUIRED",
    "FORBIDDEN_SIGNATURE_TYPE",
    "STRUCTURAL_PLACEMENT",
    "API_CONTRACT",
]
Z2Z_EXTRA = ["sonstige", "keiner der sechs"]
Z2G_VALUES = ["Spiegelung", "negierte Spiegelung", "normativ", "unklar"]
KIND_VALUES = ["structural", "semantic"]
GRAN_KEYS = ["package", "module", "artefact", "unresolved"]

# --- §7 point 8, loadability: result of the READ-ONLY probe -----------------------
#
# `parseArchitectureRules` is TypeScript and lives in the measurement worktree
# ~/ma/tritongraph-measure (detached on 348ca9d). It cannot be called from this
# stdlib-only script, and reimplementing the parser in Python is ruled out — it would
# measure something else. The probe was therefore run separately, read-only, and its
# result is registered here as a constant so this script stays deterministic and the
# figure stays reproducible from the repository alone.
#
# The probe imports rules.ts DIRECTLY, not through the package barrel index.ts (that
# one pulls in llmClient). It was run with Node's own type stripping, because the tsx
# in ~/ma/tritongraph/tools/ts-to-ilograph/node_modules/.bin is unusable on this
# machine (its esbuild is the darwin-arm64 build, the host is linux-x64) and `npm
# install` in tritongraph is out of the question. Nothing was written, built or
# installed in either repository; `git status` was empty in both before and after.
#
# Command, from a scratch directory outside all three repositories:
#   node ladbarkeit.ts ladbarkeit_input.json
# with node v22.23.2, and ladbarkeit.ts:
#
#   import { readFileSync } from 'node:fs'
#   import { parseArchitectureRules } from
#     '/home/haasentimo/ma/tritongraph-measure/packages/triton-conformance/src/rules.ts'
#   const input = JSON.parse(readFileSync(process.argv[2], 'utf-8'))
#   // each proposal alone, so a failure is attributable, and all of them in one array
#   for (const entry of input.rules) parseArchitectureRules({ rules: [entry.rule] })
#   parseArchitectureRules({ rules: input.rules.map((r) => r.rule) })
#
# The rewrite is exactly ONE field insertion — `kind`, as assigned by the reviewer —
# on top of the five fields of the sheet; `predicate` stays absent (permitted:
# types.ts:44, rules.ts:77).
LADBARKEIT = {
    "instrument": "parseArchitectureRules, "
                  "~/ma/tritongraph-measure/packages/triton-conformance/src/rules.ts",
    "worktree": "~/ma/tritongraph-measure, detached auf 348ca9d",
    "import": "DIREKT aus rules.ts, NICHT über die Paket-Barrel index.ts",
    "laufzeit": "node v22.23.2 mit eigenem Type-Stripping; der tsx in "
                "~/ma/tritongraph/tools/ts-to-ilograph/node_modules/.bin ist auf "
                "dieser Maschine unbrauchbar (esbuild als darwin-arm64 installiert, "
                "Host linux-x64), und ein npm install in tritongraph ist "
                "ausgeschlossen",
    "umschreibung": "genau EINE Feldeinfügung: das vom Bewerter zugewiesene `kind`; "
                    "id, category, scope, statement, severity unverändert, "
                    "`predicate` bleibt leer (zulässig: types.ts:44, rules.ts:77)",
    "nur_lesend": "kein Commit, kein Bau, kein npm install; `git status` in "
                  "~/ma/tritongraph-measure und ~/ma/tritongraph vorher und nachher "
                  "leer, HEAD unverändert 348ca9d",
    "etiketten_angenommen": 17,
    "etiketten_gesamt": 17,
    "alle_siebzehn_in_einem_array_angenommen": 17,
    "klassen_angenommen": 16,
    "klassen_gesamt": 16,
    "fehler": [],
    "groesse_nach_§7_punkt_8": "16 von 16 deduplizierten Vorschlägen angenommen",
    "vermerk": "Deskriptiv und KEIN Korrektheitsmaß (§7 Punkt 8). Die "
               "`kind`-Zuweisung ist eine Bewertung, keine maschinelle Angabe.",
}

# The reviewer looked at code and inputs of the test repository while assessing. A
# method detail for chapter 6, registered here and in data/z2/MANIFEST.md: it is
# compatible with the blinding, which is directed against condition and model
# labelling, not against the repository — and for Z2-G ("verbietet Realisiertes") the
# look at the as-is state is necessary. No threat.
METHODENDETAIL_EINSICHT = (
    "Der Bewerter hat während der Bewertung Code und Eingaben des Testrepos "
    "eingesehen. Das ist mit der Verblindung vereinbar — sie richtet sich gegen "
    "Bedingungs- und Modellkennzeichnung, nicht gegen das Repositorium; für Z2-G "
    "(„verbietet Realisiertes“) ist der Blick auf das Ist notwendig. Kein Threat, "
    "aber ein zu berichtendes Methodendetail."
)

# N1 threshold of the gate note §5c i. d. F. 02.09.2026 — one boundary, two outcomes.
N1_THRESHOLD = 50

# --- sheet parsing --------------------------------------------------------------


def split_row(line):
    """Split a markdown table row on pipes that are not backslash-escaped."""
    cells, cur, i = [], [], 0
    while i < len(line):
        c = line[i]
        if c == "\\" and i + 1 < len(line) and line[i + 1] == "|":
            cur.append("|")
            i += 2
            continue
        if c == "|":
            cells.append("".join(cur).strip())
            cur = []
            i += 1
            continue
        cur.append(c)
        i += 1
    cells.append("".join(cur).strip())
    if cells and cells[0] == "":
        cells = cells[1:]
    if cells and cells[-1] == "":
        cells = cells[:-1]
    return cells


def entry_blocks(text):
    """Return (label order, {label: body}) for the `### P-xx` sections of the sheet."""
    parts = re.split(r"^### (P-\d\d)\s*$", text, flags=re.M)
    order, bodies = [], {}
    for i in range(1, len(parts), 2):
        label, body = parts[i], parts[i + 1]
        cut = re.search(r"^## ", body, flags=re.M)
        if cut:
            body = body[: cut.start()]
        order.append(label)
        bodies[label] = body
    return order, bodies


def parse_entry(label, body):
    """Pull every field of one entry out of its markdown tables."""
    by_key = {}
    for line in body.split("\n"):
        s = line.strip()
        if not s.startswith("|"):
            continue
        cells = split_row(s)
        if len(cells) == 2:
            by_key[cells[0]] = cells[1]
        elif len(cells) == 3:
            by_key[cells[0]] = cells[2]  # Dimension | Werteliste | Eintrag
    m = re.search(r"^~~~~text\n(.*?)\n~~~~\s*$", body, flags=re.M | re.S)
    return {
        "etikett": label,
        "category": by_key.get("`category`"),
        "severity": by_key.get("`severity`"),
        "scope_components_roh": by_key.get("`scope.components`"),
        "statement": m.group(1) if m else None,
        "z2w_wohlgeformt": by_key.get("**Z2-W** wohlgeformt"),
        "z2w_einzelpruefungen": by_key.get("Z2-W Einzelprüfungen (§5.3 Punkt 2)"),
        "z2w_befunde": by_key.get("Z2-W Befunde"),
        "granularitaet_roh": by_key.get(
            "Granularität (BEOBACHTUNG, kein Kriterium)"
        ),
        "kind_roh": by_key.get("`kind`"),
        "z2p_roh": by_key.get("**Z2-P** Prüfbarkeit"),
        "z2g_roh": by_key.get("**Z2-G** Gehalt"),
        "z2z_roh": by_key.get("**Z2-Z** Zuordnung"),
        "identisch_mit": by_key.get("identisch mit P-xx"),
        "grenzfall": by_key.get("Grenzfall nach §6 Punkt 1?"),
        "bemerkung": by_key.get("Bemerkung"),
    }


def head_and_tail(value):
    """Split a filled-in cell into its verdict (before the em dash) and its reason."""
    parts = value.split("—", 1)
    return parts[0].strip(), (parts[1].strip() if len(parts) > 1 else "")


def normalise(entry, problems):
    """Map the reviewer's free-text cells onto the registered value lists of §6.

    Unknown values are recorded as problems and left as-is; nothing is guessed.
    """
    label = entry["etikett"]

    kind_head, kind_reason = head_and_tail(entry["kind_roh"])
    kind = kind_head.strip("`")
    if kind not in KIND_VALUES:
        problems.append(f"{label}: `kind` nicht aus der Werteliste: {kind_head!r}")
    entry["kind"] = kind
    entry["kind_begruendung"] = kind_reason

    p_head, p_reason = head_and_tail(entry["z2p_roh"])
    # §6 phrases the external-import case as "nicht entscheidbar MIT VERMERK DER
    # URSACHE"; it sits on the "nicht prüfbar" side of the dichotomy.
    if p_head == "prüfbar":
        z2p = "prüfbar"
    elif p_head in ("nicht prüfbar", "nicht entscheidbar"):
        z2p = "nicht prüfbar"
    else:
        z2p = None
        problems.append(f"{label}: Z2-P nicht aus der Werteliste: {p_head!r}")
    entry["z2p"] = z2p
    entry["z2p_wortlaut_verdikt"] = p_head
    entry["z2p_ursache"] = p_reason
    # Mechanical marker: §6 makes the cause note mandatory and names the external
    # import as the registered price of stage 0b. Detected on the uppercase marker,
    # and the full cause text travels along so the split stays auditable.
    entry["z2p_ursache_externer_import"] = bool(
        z2p == "nicht prüfbar" and re.search(r"EXTERNE?S?\b", p_reason)
    )

    g_head, g_reason = head_and_tail(entry["z2g_roh"])
    if g_head not in Z2G_VALUES:
        problems.append(f"{label}: Z2-G nicht aus der Werteliste: {g_head!r}")
    entry["z2g"] = g_head
    entry["z2g_begruendung"] = g_reason

    z_head, z_reason = head_and_tail(entry["z2z_roh"])
    z2z = z_head.strip("`")
    if z2z not in LEVEL1_CATEGORIES + Z2Z_EXTRA:
        problems.append(f"{label}: Z2-Z nicht aus der Werteliste: {z_head!r}")
    entry["z2z"] = z2z
    entry["z2z_begruendung"] = z_reason

    gf = entry["grenzfall"]
    if gf not in ("ja", "nein"):
        problems.append(f"{label}: Grenzfall weder ja noch nein: {gf!r}")
    entry["grenzfall_ja"] = gf == "ja"

    gran = {}
    for key in GRAN_KEYS:
        m = re.search(rf"{key}\s+(\d+)", entry["granularitaet_roh"] or "")
        gran[key] = int(m.group(1)) if m else None
        if gran[key] is None:
            problems.append(f"{label}: Granularität {key} nicht lesbar")
    entry["granularitaet"] = gran

    entry["scope_components"] = [
        c.strip().strip("`")
        for c in (entry["scope_components_roh"] or "").split("·")
        if c.strip()
    ]
    entry["category_klar"] = (entry["category"] or "").strip("`")
    entry["severity_klar"] = (entry["severity"] or "").strip("`")

    ident = (entry["identisch_mit"] or "").strip()
    entry["identisch_mit_etiketten"] = sorted(set(re.findall(r"P-\d\d", ident)))
    return entry


# --- Z2-R equivalence classes ---------------------------------------------------


def equivalence_classes(entries, problems):
    """Build the Z2-R classes from the reviewer's "identisch mit P-xx" column.

    The column may be filled in one direction only (§6 leaves the direction open);
    the relation is symmetrised and closed transitively. A pointer to a label that
    does not exist is a problem, not something to repair.
    """
    labels = [e["etikett"] for e in entries]
    known = set(labels)
    adj = {label: set() for label in labels}
    gerichtete_angaben = []
    for e in entries:
        for other in e["identisch_mit_etiketten"]:
            if other not in known:
                problems.append(
                    f"{e['etikett']}: verweist auf unbekanntes Etikett {other}"
                )
                continue
            gerichtete_angaben.append(
                {"von": e["etikett"], "auf": other, "gegenseitig": e["etikett"]
                 in {o for o in
                     next(x for x in entries if x["etikett"] == other)
                     ["identisch_mit_etiketten"]}}
            )
            adj[e["etikett"]].add(other)
            adj[other].add(e["etikett"])  # symmetrisiert

    classes, seen = [], set()
    for label in labels:  # labels are already in sheet order -> deterministic
        if label in seen:
            continue
        stack, comp = [label], set()
        while stack:
            cur = stack.pop()
            if cur in comp:
                continue
            comp.add(cur)
            stack.extend(sorted(adj[cur] - comp))
        seen |= comp
        classes.append(sorted(comp))
    return classes, sorted(
        gerichtete_angaben, key=lambda d: (d["von"], d["auf"])
    )


# --- tallying -------------------------------------------------------------------


def tally(values, domain):
    """Count `values` over the registered `domain`; every value of the domain shows."""
    out = {k: 0 for k in domain}
    for v in values:
        out[v] = out.get(v, 0) + 1
    return out


def class_value(cls, by_label, field):
    """Value of a class on a dimension, or a divergence marker if members differ."""
    vals = sorted({by_label[m][field] for m in cls}, key=repr)
    if len(vals) == 1:
        return vals[0]
    return "UNEINHEITLICH: " + " / ".join(f"{m}={by_label[m][field]}"
                                          for m in sorted(cls))


def make_verteilungen(cls_list, by_label, bezugsmenge):
    """Every distribution of §7 point 2 over one set of classes."""
    def cv(field):
        return [class_value(c, by_label, field) for c in cls_list]

    return {
        "bezugsmenge": bezugsmenge,
        "n": len(cls_list),
        "z2g": tally(cv("z2g"), Z2G_VALUES),
        "z2p": tally(cv("z2p"), ["prüfbar", "nicht prüfbar"]),
        "kind": tally(cv("kind"), KIND_VALUES),
        "z2z": tally(cv("z2z"), LEVEL1_CATEGORIES + Z2Z_EXTRA),
    }


def coverage(cls_list, by_label):
    """Coverage matrix of §7 point 3.

    The protocol wording is `welche Klassen tauchen überhaupt auf (>= 1 normativer,
    prüfbarer Vorschlag)` — so the registered criterion is normativ AND prüfbar. The
    plainer reading (any proposal at all) is carried alongside, marked as such,
    because it is the reading the S11 task text used.
    """
    streng, weit = {c: [] for c in LEVEL1_CATEGORIES}, {c: [] for c in LEVEL1_CATEGORIES}
    for cls in cls_list:
        cat = class_value(cls, by_label, "z2z")
        if cat not in LEVEL1_CATEGORIES:
            continue
        name = "+".join(cls)
        weit[cat].append(name)
        if (class_value(cls, by_label, "z2g") == "normativ"
                and class_value(cls, by_label, "z2p") == "prüfbar"):
            streng[cat].append(name)
    return {
        "kriterium_protokoll_§7_punkt_3": "≥ 1 normativer, prüfbarer Vorschlag",
        "belegt_streng": {c: sorted(v) for c, v in streng.items()},
        "belegt_streng_zahl": sum(1 for v in streng.values() if v),
        "unbelegt_streng": sorted(c for c, v in streng.items() if not v),
        "kriterium_weit": "≥ 1 Vorschlag beliebigen Gehalts und beliebiger Prüfbarkeit",
        "belegt_weit": {c: sorted(v) for c, v in weit.items()},
        "belegt_weit_zahl": sum(1 for v in weit.values() if v),
        "unbelegt_weit": sorted(c for c, v in weit.items() if not v),
        "vorschlaege_auf_die_sich_die_matrix_stuetzt": len(cls_list),
        "bei_dieser_vorschlagszahl_ueberhaupt_besetzbare_kategorien": min(
            len(cls_list), len(LEVEL1_CATEGORIES)
        ),
    }


# --- T-Z2-10: textual proximity to the Anhang A A3 example ----------------------


def anhang_a_beispiel(protokolltext):
    """Extract the example rule object from the frozen Anhang A A3, verbatim."""
    m = re.search(r"^### A3 Der Prompt$(.*?)^### A4 ", protokolltext, flags=re.M | re.S)
    if not m:
        raise SystemExit("Anhang A A3 im Protokoll nicht gefunden")
    a3 = m.group(1)
    fields = {}
    for key in ("id", "category", "statement", "severity"):
        f = re.search(rf'"{key}"\s*:\s*"((?:[^"\\]|\\.)*)"', a3)
        if not f:
            raise SystemExit(f"Beispielfeld {key} in A3 nicht gefunden")
        fields[key] = f.group(1)
    comp = re.search(r'"components"\s*:\s*\[([^\]]*)\]', a3)
    fields["scope.components"] = [
        c.strip().strip('"') for c in comp.group(1).split(",") if c.strip()
    ] if comp else []
    return fields


def norm_text(s):
    return unicodedata.normalize("NFC", s).lower()


def similarity(a, b):
    return difflib.SequenceMatcher(None, norm_text(a), norm_text(b)).ratio()


def word_diff(a, b):
    """Word-level diff of the two statements, as a list of ndiff lines."""
    return list(
        difflib.ndiff(norm_text(a).split(), norm_text(b).split())
    )


# --- main -----------------------------------------------------------------------


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))))
    args = ap.parse_args()
    R = args.repo

    sheet_path = os.path.join(R, "data/z2/bewertung/bewertungsblatt.md")
    key_path = os.path.join(R, "data/z2/bewertung/zuordnungsschluessel.json")
    proto_path = os.path.join(R, "docs/protokolle/z2_protokoll_regelableitung.md")

    sheet = open(sheet_path, encoding="utf-8").read()
    key = json.load(open(key_path, encoding="utf-8"))
    proto = open(proto_path, encoding="utf-8").read()

    problems = []          # anything noticed, reported, never repaired
    gegenproben = []       # every counter-check the task registered

    order, bodies = entry_blocks(sheet)
    entries = [normalise(parse_entry(l, bodies[l]), problems) for l in order]
    by_label = {e["etikett"]: e for e in entries}

    # --- step 2: resolve the assignment -----------------------------------------
    key_by_label = {k["etikett"]: k for k in key["eintraege"]}
    zuordnung = []
    for e in entries:
        k = key_by_label.get(e["etikett"])
        if k is None:
            problems.append(f"{e['etikett']}: kein Eintrag im Schlüssel")
            continue
        zuordnung.append({
            "etikett": e["etikett"],
            "bedingungen": k["bedingungen"],
            "slots": k["slots"],
            "positionen": k["positionen"],
            "ids": k["ids"],
            "vielfachheit": k["vielfachheit"],
            "herkunft": k["herkunft"],
        })
        e["bedingungen"] = k["bedingungen"]
        e["vielfachheit"] = k["vielfachheit"]
        e["herkunft"] = k["herkunft"]
        if len(k["bedingungen"]) != 1:
            problems.append(
                f"{e['etikett']}: Herkunft aus mehr als einer Bedingung "
                f"{k['bedingungen']}"
            )
        e["bedingung"] = k["bedingungen"][0]

    summe_vielfachheit = sum(z["vielfachheit"] for z in zuordnung)
    v3 = sorted(z["etikett"] for z in zuordnung if z["vielfachheit"] == 3)
    v1 = sorted(z["etikett"] for z in zuordnung if z["vielfachheit"] == 1)
    v3_zellen = sorted({by_label[l]["bedingung"] for l in v3})
    gegenproben += [
        {"probe": "17 Etiketten", "soll": 17, "ist": len(entries),
         "ok": len(entries) == 17},
        {"probe": "Summe der Vielfachheiten = 27", "soll": 27,
         "ist": summe_vielfachheit, "ok": summe_vielfachheit == 27},
        {"probe": "fünf Etiketten mit Vielfachheit 3", "soll": 5, "ist": len(v3),
         "ok": len(v3) == 5, "etiketten": v3},
        {"probe": "die fünf stammen alle aus EINER Zelle", "soll": 1,
         "ist": len(v3_zellen), "ok": len(v3_zellen) == 1, "zellen": v3_zellen},
        {"probe": "zwölf Etiketten mit Vielfachheit 1", "soll": 12, "ist": len(v1),
         "ok": len(v1) == 12, "etiketten": v1},
    ]

    # --- step 3: Z2-R equivalence classes ---------------------------------------
    classes, gerichtete = equivalence_classes(entries, problems)
    klassen = []
    for cls in classes:
        zellen = sorted({by_label[m]["bedingung"] for m in cls})
        klassen.append({
            "mitglieder": cls,
            "groesse": len(cls),
            "bedingungen": zellen,
            "zelluebergreifend": len(zellen) > 1,
            "laeufe": sorted({f"{h['bedingung']}/{h['slot']}"
                              for m in cls for h in by_label[m]["herkunft"]}),
            "dimensionen": {
                d: class_value(cls, by_label, d)
                for d in ("kind", "z2p", "z2g", "z2z", "grenzfall_ja")
            },
        })
    nichttriviale = [k for k in klassen if k["groesse"] > 1]
    gegenproben.append({
        "probe": "Z2-R-Relation symmetrisch und transitiv auflösbar",
        "soll": "auflösbar", "ist": "auflösbar (gerichtete Angaben symmetrisiert)",
        "ok": True, "gerichtete_angaben": gerichtete,
    })

    # --- step 4: N1 and per-run dedup -------------------------------------------
    def labels_of_run(cell, slot):
        return sorted(e["etikett"] for e in entries
                      if any(h["bedingung"] == cell and h["slot"] == slot
                             for h in e["herkunft"]))

    def classes_over(labels):
        s = set(labels)
        return [c for c in classes if set(c) & s]

    laeufe = []
    for cell in sorted({e["bedingung"] for e in entries}):
        for slot in ("run0", "run1", "run2"):
            labs = labels_of_run(cell, slot)
            cls = classes_over(labs)
            laeufe.append({
                "zelle": cell, "slot": slot,
                "etiketten": labs,
                "roh": len(labs),
                "klassen": [c for c in cls],
                "pro_lauf_dedup": len(cls),
            })

    n1_lauf = next(l for l in laeufe if l["zelle"] == "k2_b1" and l["slot"] == "run0")
    n1 = n1_lauf["pro_lauf_dedup"]

    # --- step 5: tallies ---------------------------------------------------------
    per_condition_classes = {}
    for cell in sorted({e["bedingung"] for e in entries}):
        per_condition_classes[cell] = [
            c for c in classes if all(by_label[m]["bedingung"] == cell for m in c)
        ]
    gemischt = [c for c in classes
                if len({by_label[m]["bedingung"] for m in c}) > 1]

    def roh_counts(labels, bezug):
        return {
            "bezugsmenge": bezug,
            "n": len(labels),
            "z2g": tally([by_label[l]["z2g"] for l in labels], Z2G_VALUES),
            "z2p": tally([by_label[l]["z2p"] for l in labels],
                         ["prüfbar", "nicht prüfbar"]),
            "kind": tally([by_label[l]["kind"] for l in labels], KIND_VALUES),
            "z2z": tally([by_label[l]["z2z"] for l in labels],
                         LEVEL1_CATEGORIES + Z2Z_EXTRA),
        }

    alle_labels = sorted(by_label)
    verteilungen = {
        "nach_inhaltlicher_dedup": {
            "gepoolt": make_verteilungen(
                classes, by_label,
                "alle 17 Etiketten nach Z2-R zusammengeführt (Äquivalenzklassen)"),
            **{cell: make_verteilungen(
                cls, by_label,
                f"Etiketten der Zelle {cell} nach Z2-R zusammengeführt")
               for cell, cls in per_condition_classes.items()},
        },
        "roh_je_etikett": {
            "gepoolt": roh_counts(alle_labels, "alle 17 Etiketten, ohne Z2-R-Dedup"),
            **{cell: roh_counts(
                sorted(e["etikett"] for e in entries if e["bedingung"] == cell),
                f"Etiketten der Zelle {cell}, ohne Z2-R-Dedup")
               for cell in per_condition_classes},
        },
        "roh_je_generat": {
            "bezugsmenge": "alle 27 Vorschlagsinstanzen der sechs Läufe "
                           "(Vielfachheit gewichtet, ohne jede Dedup)",
            "n": summe_vielfachheit,
            "je_zelle": {
                cell: sum(e["vielfachheit"] for e in entries
                          if e["bedingung"] == cell)
                for cell in per_condition_classes
            },
        },
    }

    # (b) Z2-P causes, verbatim, with the external-import split §6 demands
    nicht_pruefbar = [
        {"etikett": e["etikett"], "bedingung": e["bedingung"],
         "wortlaut_verdikt": e["z2p_wortlaut_verdikt"],
         "ursache_woertlich": e["z2p_ursache"],
         "ursache_externer_import": e["z2p_ursache_externer_import"]}
        for e in entries if e["z2p"] == "nicht prüfbar"
    ]
    z2p_ursachen = {
        "bezugsmenge": "alle 17 Etiketten; die Ursachen sind Bewertertext, wörtlich",
        "nicht_pruefbar_gesamt": len(nicht_pruefbar),
        "davon_ursache_externer_import": sum(
            1 for x in nicht_pruefbar if x["ursache_externer_import"]),
        "davon_andere_ursache": sum(
            1 for x in nicht_pruefbar if not x["ursache_externer_import"]),
        "eintraege": nicht_pruefbar,
    }

    # (e) coverage matrix
    abdeckung = {
        "gepoolt": coverage(classes, by_label),
        **{cell: coverage(cls, by_label) for cell, cls in per_condition_classes.items()},
    }

    # (f) borderline-case quota
    gf_tabelle_zeilen = re.findall(
        r"^\| (P-\d\d) \| ([^|]*) \| ([^|]*) \| ([^|]*) \|\s*$", sheet, flags=re.M)
    grenzfall = {
        "bezugsmenge_etiketten": len(entries),
        "etiketten_mit_grenzfall_ja": sorted(
            e["etikett"] for e in entries if e["grenzfall_ja"]),
        "je_zelle": {
            cell: {
                "grenzfaelle": sorted(e["etikett"] for e in entries
                                      if e["bedingung"] == cell and e["grenzfall_ja"]),
                "etiketten": sum(1 for e in entries if e["bedingung"] == cell),
            } for cell in per_condition_classes
        },
        "zeilen_der_grenzfall_tabelle": len(gf_tabelle_zeilen),
        "tabelle": [
            {"etikett": a, "kriterium": b.strip(), "entscheidung": c.strip(),
             "begruendung": d.strip()}
            for a, b, c, d in gf_tabelle_zeilen
        ],
        "entfallener_zweitbewerter_trigger": {
            "wert": "20 %",
            "fundstelle": "z2_protokoll_regelableitung.md §6, durchgestrichene "
                          "„Zweitbewerter-Regel (vorregistriert)“ — überholt am "
                          "31.08.2026 (Auftrag G1, Amendment §11); §6 Punkt 3 der "
                          "geltenden Fassung: „Kein Trigger, keine Pflicht.“",
            "status": "entfallen — zur Kenntnis, ohne Deutung",
        },
    }
    for cell, d in grenzfall["je_zelle"].items():
        d["anteil"] = round(len(d["grenzfaelle"]) / d["etiketten"], 4)
    grenzfall["anteil_gepoolt"] = round(
        len(grenzfall["etiketten_mit_grenzfall_ja"]) / len(entries), 4)
    # class basis as well: a class counts as borderline if any member does
    gf_klassen = [c for c in classes if any(by_label[m]["grenzfall_ja"] for m in c)]
    grenzfall["auf_klassenbasis"] = {
        "bezugsmenge": "Äquivalenzklassen nach Z2-R, gepoolt",
        "klassen": len(classes),
        "klassen_mit_grenzfall": len(gf_klassen),
        "anteil": round(len(gf_klassen) / len(classes), 4),
    }

    # (g) stability §7 point 4, per cell, never pooled across cells
    stabilitaet = {}
    for cell in per_condition_classes:
        cell_classes = [c for c in classes
                        if any(by_label[m]["bedingung"] == cell for m in c)]
        je_klasse = []
        for c in cell_classes:
            slots = sorted({h["slot"] for m in c for h in by_label[m]["herkunft"]
                            if h["bedingung"] == cell})
            je_klasse.append({"mitglieder": c, "laeufe": slots,
                              "wiederkehr": f"{len(slots)}/3",
                              "stabil_ge_2_von_3": len(slots) >= 2})
        stabil = sum(1 for x in je_klasse if x["stabil_ge_2_von_3"])
        stabilitaet[cell] = {
            "bezugsmenge": f"Äquivalenzklassen mit mindestens einem Etikett aus {cell}",
            "klassen": len(je_klasse),
            "klassen_mit_wiederkehr_ge_2_von_3": stabil,
            "anteil": round(stabil / len(je_klasse), 4) if je_klasse else None,
            "je_klasse": je_klasse,
        }
    stabilitaet["k2_b1"]["determinismusvermerk"] = (
        "In der Zelle K2 × B1 sind die drei Generate ZEICHENGLEICH — SHA256 "
        "`f71c9c743093e0c3…` über `choices[0].message.content`, 2 356 Zeichen, "
        "Fundstelle `data/z2/MANIFEST.md`, Abschnitt „Formbefund ohne Deutung: die "
        "drei Generate sind zeichengleich“. Die Wiederkehr ist dort daher KONSTRUKTIV "
        "3/3 für jeden Vorschlag. Die Größe misst in dieser Zelle Determinismus und "
        "nicht Wiederkehr über unabhängige Ziehungen."
    )
    stabilitaet["k3_b1"]["determinismusvermerk"] = (
        "In der Zelle K3 × B1 sind die drei Generate VERSCHIEDEN (SHA256 "
        "`f3514cf678fc7bec…` / `2ffde87ee71cd79c…` / `1fe29dd6972bd5f6…`, Fundstelle "
        "`data/z2/MANIFEST.md`). Die Wiederkehr ist hier über verschiedene Generate "
        "gebildet."
    )
    stabilitaet["_nicht_zusammenfassen"] = (
        "Die Zahlen der beiden Zellen werden NICHT zusammengefasst und NICHT "
        "gegeneinander gerechnet."
    )

    # (h) granularity, an observation and no criterion
    granularitaet = {"hinweis": "BEOBACHTUNG, kein Kriterium (§6)"}
    for cell in list(per_condition_classes) + ["gepoolt"]:
        labs = alle_labels if cell == "gepoolt" else [
            e["etikett"] for e in entries if e["bedingung"] == cell]
        summe = {k: sum(by_label[l]["granularitaet"][k] for l in labs)
                 for k in GRAN_KEYS}
        etiketten_mit = {k: sum(1 for l in labs
                                if by_label[l]["granularitaet"][k] > 0)
                         for k in GRAN_KEYS}
        granularitaet[cell] = {
            "bezugsmenge": f"Etiketten {cell} (ohne Z2-R-Dedup)",
            "etiketten": len(labs),
            "summe_der_scope_eintraege": summe,
            "etiketten_mit_mindestens_einem": etiketten_mit,
        }

    # borderline column of the entries against the rows of Anhang B
    gf_ja = sorted(e["etikett"] for e in entries if e["grenzfall_ja"])
    gf_tab_labels = sorted({a for a, _b, _c, _d in gf_tabelle_zeilen})
    gegenproben.append({
        "probe": "jedes Etikett mit „Grenzfall = ja“ hat mindestens eine Zeile in "
                 "der Grenzfall-Tabelle, und umgekehrt",
        "soll": gf_ja, "ist": gf_tab_labels, "ok": gf_ja == gf_tab_labels,
    })
    gegenproben.append({
        "probe": "jedes Etikett des Blattes steht im Schlüssel und umgekehrt",
        "soll": sorted(by_label), "ist": sorted(key_by_label),
        "ok": sorted(by_label) == sorted(key_by_label),
    })

    # Anything that stands out, reported and NOT changed, NOT counted differently.
    beobachtungen = []
    for k in klassen:
        for dim, val in k["dimensionen"].items():
            if isinstance(val, str) and val.startswith("UNEINHEITLICH"):
                beobachtungen.append(
                    f"Klasse {'+'.join(k['mitglieder'])}: die Mitglieder tragen auf "
                    f"„{dim}“ verschiedene Werte ({val}). Gemeldet, NICHT geändert; "
                    f"in die Zählung greift das nicht ein — die Klasse wird auf "
                    f"dieser Dimension als uneinheitlich geführt."
                )

    # --- step 7: T-Z2-10 ---------------------------------------------------------
    beispiel = anhang_a_beispiel(proto)
    aehnlich = sorted(
        ({"etikett": e["etikett"],
          "bedingung": e["bedingung"],
          "ratio": round(similarity(beispiel["statement"], e["statement"]), 6),
          "category": e["category_klar"],
          "severity": e["severity_klar"],
          "scope_components": e["scope_components"]}
         for e in entries),
        key=lambda d: (-d["ratio"], d["etikett"]),
    )
    top = aehnlich[0]
    tz210 = {
        "hinweis": "Erhoben wird die TEXTLICHE NÄHE. Es wird KEINE Aussage getroffen, "
                   "ob ein Vorschlag aus dem Beispiel stammt. T-Z2-10 ist der "
                   "registrierte Threat, unter dem der Autor sie einordnet.",
        "beispiel_aus_anhang_a_a3": beispiel,
        "mass": "difflib.SequenceMatcher.ratio über NFC-normalisierte, "
                "kleingeschriebene statement-Texte",
        "alle_werte": aehnlich,
        "drei_hoechste": aehnlich[:3],
        "hoechster": {
            **top,
            "wortdiff_beispiel_gegen_vorschlag": word_diff(
                beispiel["statement"], by_label[top["etikett"]]["statement"]),
            "statement_beispiel": beispiel["statement"],
            "statement_vorschlag": by_label[top["etikett"]]["statement"],
            "felderabgleich": {
                "category": {"beispiel": beispiel["category"],
                             "vorschlag": by_label[top["etikett"]]["category_klar"],
                             "gleich": beispiel["category"]
                             == by_label[top["etikett"]]["category_klar"]},
                "severity": {"beispiel": beispiel["severity"],
                             "vorschlag": by_label[top["etikett"]]["severity_klar"],
                             "gleich": beispiel["severity"]
                             == by_label[top["etikett"]]["severity_klar"]},
                "scope_components": {
                    "beispiel": beispiel["scope.components"],
                    "vorschlag": by_label[top["etikett"]]["scope_components"],
                    "gleich": beispiel["scope.components"]
                    == by_label[top["etikett"]]["scope_components"]},
            },
        },
    }

    # --- output ------------------------------------------------------------------
    out = {
        "dokument": "Auswertung der Z2-Bewertung — mechanische Auszählung",
        "auftrag": "S11",
        "werkzeug": "tools/tally_z2_review.py",
        "status": "MECHANISCHE AUSZÄHLUNG OHNE DEUTUNG",
        "keine_deutung": (
            "Dieses Dokument zählt aus. Es beurteilt keine vorregistrierte Erwartung, "
            "bezeichnet nichts als bestätigt oder widerlegt, korrigiert keine "
            "Zuweisung des Bewerters und formuliert kein Ergebnis. Die Verdikte und "
            "der Befund 09 stehen aus und sind Sache des Autors."
        ),
        "schluesseloeffnung": {
            "zeitpunkt": KEY_OPENED_AT,
            "commit_mit_ausgefuelltem_blatt": KEY_OPENED_COMMIT,
            "commit_botschaft": "docs: fill in bewertungsblatt.md",
            "bewertung_vor_der_oeffnung_abgeschlossen": True,
            "beleg": (
                "P3: alle 17 Etiketten tragen in `kind`, Z2-P, Z2-G, Z2-Z sowie in "
                "„identisch mit P-xx“ und „Grenzfall“ einen Eintrag, geprüft VOR dem "
                "Öffnen des Schlüssels. Commit-Reihenfolge: b17fc98 legt das leere "
                "Blatt an, 9b6c76b füllt es aus, S11 öffnet den Schlüssel danach; der "
                "Schlüssel ist seit b17fc98 bytegleich."
            ),
            "schluessel_sha256": (
                "0215a8b2ed377df1e4e074dd5f489c58a7341fc93e54362b61fcef8b78a320f2"),
            "blatt_sha256": (
                "72ebc3170f484a391a1d991c4fa155d57d04f6bfc5374c609ac8d601c109c029"),
            "protokoll_sha256": key["protokoll_sha256"],
            "seed": key["seed"],
        },
        "zuordnung": sorted(zuordnung, key=lambda z: z["etikett"]),
        "gegenproben": gegenproben,
        "z2r_klassen": {
            "regel": "§6 Z2-R — Duplikate bei Übereinstimmung in Kategorie, Scope und "
                     "Kernaussage; Umformulierungen zählen als ein Vorschlag. Die "
                     "Zusammenführung ist die des Bewerters, unverändert übernommen.",
            "klassen": klassen,
            "zahl_der_vorschlaege_nach_inhaltlicher_dedup": len(classes),
            "zahl_der_etiketten_vor_inhaltlicher_dedup": len(entries),
            "nichttriviale_klassen": nichttriviale,
            "zelluebergreifende_klassen": gemischt,
            "zelluebergreifend_vorhanden": bool(gemischt),
            "vermerk": "Ob eine Klasse zellübergreifend ist, ist eine Tatsache; ihre "
                       "Bedeutung bleibt offen.",
        },
        "n1": {
            "definition": "§7 Punkt 9 / Gate-Notiz §5b: N₁ ist die PRO-LAUF-Dedup des "
                          "ERSTEN Laufs der Zelle K2 × B1 nach Z2-R, NICHT die Dedup "
                          "über die drei Läufe.",
            "lauf": "k2_b1/run0",
            "beteiligte_etiketten": n1_lauf["etiketten"],
            "klassen": n1_lauf["klassen"],
            "n1": n1,
            "schwelle": N1_THRESHOLD,
            "zahlenvergleich": f"N₁ = {n1} ≤ {N1_THRESHOLD}" if n1 <= N1_THRESHOLD
                               else f"N₁ = {n1} > {N1_THRESHOLD}",
            "vermerk": "Zahlenvergleich, keine Entscheidung. Die Entscheidung I3 "
                       "fällt datiert am 13.09.2026 durch den Autor.",
        },
        "pro_lauf_dedup_alle_sechs_laeufe": laeufe,
        "verteilungen": verteilungen,
        "z2p_ursachen": z2p_ursachen,
        "abdeckungsmatrix": abdeckung,
        "grenzfaelle": grenzfall,
        "stabilitaet": stabilitaet,
        "granularitaet": granularitaet,
        "ladbarkeit_§7_punkt_8": LADBARKEIT,
        "methodendetail_einsicht_ins_testrepo": METHODENDETAIL_EINSICHT,
        "t_z2_10_textliche_naehe": tz210,
        "ausstehend": [
            "§7 Punkt 5 (Überlapp mit den sechzehn autorenformulierten Statements) — "
            "NICHT erhoben; „sinngemäß vorgeschlagen“ ist eine Bewerterleistung.",
            "Die Verdikte zu E1–E4 und Befund 09 — Sache des Autors.",
            "Die Entscheidung I3 — fällt datiert am 13.09.2026.",
        ],
        "gemeldet_nicht_geaendert": problems + beobachtungen,
        "eintraege": sorted(entries, key=lambda e: e["etikett"]),
    }
    json.dump(out, sys.stdout, ensure_ascii=False, indent=2, sort_keys=False)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
