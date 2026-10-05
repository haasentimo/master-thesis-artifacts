#!/usr/bin/env python3
"""Prepare the BLINDED review sheet for the Z2 rule proposals (Z2 protocol §2, §6, §10).

WHAT THIS TOOL IS
-----------------
The Z2 protocol makes the single deduplicated rule proposal the unit of
evaluation (§2), judged by ONE assessor, BLINDED, in randomised order (§6,
"Bewertungsablauf -- EINZELBEWERTER, VERBLINDET"; threat T-Z2-7 in §10). This
tool builds that sheet: it pools the proposals of the six archived runs, merges
MECHANICALLY IDENTICAL ones, strips every condition and model marker, shuffles
with a registered seed, and writes the origin table into a SEPARATE key file
that the assessor must not open before finishing.

IT DOES NOT JUDGE
-----------------
Z2-P, Z2-G, Z2-Z and `kind` are left EMPTY -- they are human assessment (§6).
Nothing is proposed, hinted at or pre-filled. N1 is NOT counted. No verdict on
E1-E4. Z2-W and the granularity count are COPIED from the archived
`validation.json` of each run; both are machine results, not assessor work.

MECHANICAL IDENTITY IS ONLY A SUBSET OF Z2-R
--------------------------------------------
§6 Z2-R reads: "Zwei Vorschläge sind Duplikate, wenn Kategorie, Scope und
Kernaussage übereinstimmen (Umformulierungen zählen als ein Vorschlag)."
"Kernaussage" and "Umformulierungen" are a CONTENT judgement and belong to the
assessor. This tool therefore merges ONLY what is character-identical under the
definition in `IDENTITY_DEFINITION` below. Two proposals that say the same thing
in different words stay TWO entries; the sheet carries a dedup column for the
assessor to join them by hand.

THE WORDING IS NEVER RETYPED HERE
---------------------------------
The decision rules and value lists of the four dimensions are EXTRACTED FROM THE
FROZEN PROTOCOL at runtime, between the anchors in `SECTIONS`. The file is
pinned by SHA256 (`PROTO_SHA`); a mismatch aborts.

DETERMINISM
-----------
Standard library only, no clock, no environment, no network. Run twice, the
outputs are byte-identical. `--check` re-runs the generation into a temporary
directory and compares.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import random
import sys
import unicodedata
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

PROTO_PATH = REPO / "docs/protokolle/z2_protokoll_regelableitung.md"
PROTO_SHA = "862fdc3b7cfb264482db155575437edb25b1b436f92b5444b2137f1e332d9dde"

OUT_DIR = REPO / "data/z2/bewertung"
SHEET_NAME = "bewertungsblatt.md"
KEY_NAME = "zuordnungsschluessel.json"
SUMS_NAME = "SHA256SUMS"

# Fixed traversal order -- the pre-shuffle order of the entries depends on it,
# so it is part of the reproducibility claim.
CELLS = ("k2_b1", "k3_b1")
SLOTS = ("run0", "run1", "run2")

# Registered in the sheet, in the key and in the report. `random.Random(SEED)`.
SEED = 20260903

IDENTITY_DEFINITION = (
    "Zwei Vorschläge sind MECHANISCH IDENTISCH, wenn das Tupel "
    "(category, statement, severity, sorted(scope.components)) nach Unicode-NFC "
    "und Abschneiden führender und schliessender Leerzeichen ZEICHENGLEICH ist. "
    "`id` geht NICHT ein -- sie ist je Lauf frei gewählt. Keine weitere "
    "Normalisierung: keine Kleinschreibung, keine Interpunktions-, Zahlen- oder "
    "Synonymbehandlung, kein Zusammenziehen innerer Leerzeichen. "
    "MECHANISCHE IDENTITÄT IST NUR EINE TEILMENGE DESSEN, WAS Z2-R VERLANGT "
    "(§6: Kategorie, Scope und Kernaussage; Umformulierungen zählen als ein "
    "Vorschlag) -- die inhaltliche Zusammenführung steht aus und ist Sache des "
    "Bewerters."
)

# (label, start anchor, end anchor) -- both anchors verified unique at load time.
SECTIONS = (
    ("Z2-W", "**Z2-W Wohlgeformtheit**",
     "**`kind` (`structural` | `semantic`) — NEU als Dimension**"),
    ("kind", "**`kind` (`structural` | `semantic`) — NEU als Dimension**",
     "~~**Z2-P Prüfbarkeit** (K2)"),
    ("Z2-P", "**Z2-P Prüfbarkeit — NEUE FASSUNG**", "~~**K3 Normativer Gehalt**"),
    ("Z2-G", "**Z2-G Gehalt**", "> **Amendment (12.08.2026)"),
    ("Z2-Z", "**Z2-Z Zuordnung zum Abweichungstyp", "**Z2-R Redundanz/Dedup**"),
    ("Z2-R", "**Z2-R Redundanz/Dedup**", "**Bewertungsablauf — EINZELBEWERTER"),
    ("AnhangB", "## Anhang B — Grenzfall-Tabelle", None),
)

FENCE = "~~~~"  # tilde fence: the statements carry backticks, never tildes


def die(msg: str) -> None:
    print(f"ABBRUCH: {msg}", file=sys.stderr)
    raise SystemExit(1)


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_protocol() -> str:
    if not PROTO_PATH.exists():
        die(f"Protokoll fehlt: {PROTO_PATH}")
    actual = sha256_file(PROTO_PATH)
    if actual != PROTO_SHA:
        die(f"Protokoll-SHA256 {actual}, erwartet {PROTO_SHA}")
    return PROTO_PATH.read_text(encoding="utf-8")


def extract_sections(text: str) -> dict[str, str]:
    out: dict[str, str] = {}
    for label, start, end in SECTIONS:
        if text.count(start) != 1:
            die(f"Startanker fuer {label} nicht eindeutig: {start!r}")
        i = text.index(start)
        if end is None:
            j = len(text)
        else:
            if text.count(end) != 1:
                die(f"Endanker fuer {label} nicht eindeutig: {end!r}")
            j = text.index(end)
            if j <= i:
                die(f"Endanker vor Startanker fuer {label}")
        out[label] = text[i:j].rstrip() + "\n"
    return out


def norm(value: str) -> str:
    return unicodedata.normalize("NFC", value).strip()


def identity(rule: dict) -> tuple:
    """The tuple of `IDENTITY_DEFINITION`. `id` deliberately absent."""
    components = tuple(sorted(norm(c) for c in rule["scope"]["components"]))
    return (norm(rule["category"]), norm(rule["statement"]),
            norm(rule["severity"]), components)


def collect() -> list[dict]:
    """One record per raw proposal, in fixed traversal order."""
    records = []
    for cell in CELLS:
        for slot in SLOTS:
            raw_path = REPO / "data/z2" / cell / slot / "raw_response.json"
            val_path = REPO / "data/z2" / cell / slot / "validation.json"
            for path in (raw_path, val_path):
                if not path.exists():
                    die(f"Artefakt fehlt: {path}")
            raw = json.loads(raw_path.read_text(encoding="utf-8"))
            envelope = json.loads(raw["choices"][0]["message"]["content"])
            validation = json.loads(val_path.read_text(encoding="utf-8"))
            by_pos = {e["position"]: e for e in validation["z2w"]["je_vorschlag"]}
            for pos, rule in enumerate(envelope["rules"]):
                if pos not in by_pos:
                    die(f"validation.json ohne Position {pos} in {cell}/{slot}")
                records.append({
                    "cell": cell, "slot": slot, "position": pos,
                    "rule": rule, "z2w": by_pos[pos],
                })
    return records


def group(records: list[dict]) -> list[dict]:
    """Merge mechanically identical proposals, first-appearance order."""
    order: list[tuple] = []
    buckets: dict[tuple, list[dict]] = {}
    for rec in records:
        key = identity(rec["rule"])
        if key not in buckets:
            buckets[key] = []
            order.append(key)
        buckets[key].append(rec)

    entries = []
    for key in order:
        members = buckets[key]
        first = members[0]["rule"]
        # Z2-W and the granularity count are properties of the archived
        # validation; within a mechanically identical group they must agree,
        # because every check but `id_eindeutig` reads only the merged fields.
        z2w_flags = {json.dumps(m["z2w"]["pruefungen"], sort_keys=True) for m in members}
        z2w_verdicts = {m["z2w"]["wohlgeformt"] for m in members}
        gran = {json.dumps(m["z2w"]["granularitaet"], sort_keys=True) for m in members}
        if len(z2w_flags) > 1 or len(z2w_verdicts) > 1 or len(gran) > 1:
            die("Z2-W oder Granularitaet innerhalb einer mechanisch identischen "
                f"Gruppe uneinheitlich: {key[0]!r} -- melden, nicht angleichen")
        entries.append({
            "identity": key,
            "category": first["category"],
            "statement": first["statement"],
            "severity": first["severity"],
            "components": list(first["scope"]["components"]),
            "z2w_wohlgeformt": members[0]["z2w"]["wohlgeformt"],
            "z2w_pruefungen": members[0]["z2w"]["pruefungen"],
            "z2w_befunde": members[0]["z2w"]["befunde"],
            "granularitaet": members[0]["z2w"]["granularitaet"],
            "members": members,
        })
    return entries


def shuffle(entries: list[dict]) -> list[dict]:
    shuffled = list(entries)
    random.Random(SEED).shuffle(shuffled)
    for i, entry in enumerate(shuffled, 1):
        entry["label"] = f"P-{i:02d}"
    return shuffled


def fence(value: str) -> str:
    if FENCE in value:
        die(f"Wert enthaelt die Fence-Folge {FENCE!r}, zeichengleiche Wiedergabe "
            "waere nicht garantiert")
    return f"{FENCE}text\n{value}\n{FENCE}"


def render_sheet(entries: list[dict], sections: dict[str, str]) -> str:
    labels = [e["label"] for e in entries]
    parts: list[str] = []
    a = parts.append

    a("# Z2 — Bewertungsblatt (VERBLINDET)\n")
    a("**Auftrag S10 · Repo `masterarbeit` · Werkzeug `tools/prepare_z2_review.py`**\n")
    a(f"**Protokollstand:** `z2_protokoll_regelableitung.md`, SHA256 `{PROTO_SHA}`. "
      "Alle Entscheidungsregeln und Wertelisten unten sind **wörtlich aus §6 dieses "
      "Standes ausgeschnitten**, nicht nacherzählt.\n")
    a(f"**Seed der Reihenfolge:** `random.Random({SEED})` — im Schlüssel wiederholt.\n")
    a(f"**Einträge:** {len(entries)}, mechanisch verschieden nach der Definition unten.\n")

    a("\n---\n")
    a("\n## 0. Was dieses Blatt ist — und was der Bewerter zu tun hat\n")
    a("\nNach Protokoll **§2** ist die **Einheit der Auswertung der einzelne "
      "Regelvorschlag (nach Dedup, §6 Z2-R)**. Nach **§6** werden alle Vorschläge "
      "aller Läufe gepoolt, **anonymisiert (ohne Modell-/Bedingungs-Label)** und in "
      "**randomisierter Reihenfolge von EINEM Bewerter** bewertet; die Zuordnung "
      "wird **erst nach Abschluss der Bewertung aufgelöst**.\n")
    a("\n**AUFLAGE — der Zuordnungsschlüssel `zuordnungsschluessel.json` liegt im "
      "selben Verzeichnis und ist VOR ABSCHLUSS DER BEWERTUNG NICHT ZU ÖFFNEN.** Er "
      "trägt Bedingung, Slot, Position, ursprüngliche `id` und Vielfachheit je "
      "Eintrag. Wer ihn vorher öffnet, hebt die Verblindung auf, gegen die "
      "Erwartung **E2** gerichtet ist (§6, T-Z2-7).\n")
    a("\n**AUSZUFÜLLEN sind vier Dimensionen je Eintrag:** `kind`, **Z2-P**, "
      "**Z2-G**, **Z2-Z**. Sie sind hier **leer** und werden von Hand gesetzt.\n")
    a("\n**NICHT auszufüllen:** **Z2-W** und die **Granularitätszählung** stehen je "
      "Eintrag bereits da — sie sind **maschinell** aus der archivierten "
      "`validation.json` des jeweiligen Laufs **übernommen** und **keine "
      "Bewerterleistung**. Die Granularitätszählung ist ausdrücklich eine "
      "**BEOBACHTUNG, kein Kriterium**: sie steht in keiner Entscheidungsregel des "
      "§6 und geht in keine der vier Dimensionen ein.\n")
    a("\n**GRENZFÄLLE:** Jeder Grenzfall wird nach **§6 Punkt 1** und **§7 Punkt 7** "
      "in die **Grenzfall-Tabelle (Anhang B des Protokolls)** eingetragen — mit "
      "**Vorschlag-ID, Kriterium, Entscheidung und Begründung** — und im Befund "
      "**vollständig ausgewiesen, nicht nur gezählt**. Die Form der Tabelle steht "
      "unten in Abschnitt 6. Als Vorschlag-ID dient das Etikett `P-xx` dieses "
      "Blattes.\n")

    a("\n---\n")
    a("\n## 1. Die mechanische Zusammenführung, die diesem Blatt zugrunde liegt\n")
    a(f"\n{IDENTITY_DEFINITION}\n")
    a("\n**Folge für die Bewertung:** Zwei Einträge, die **dasselbe sagen**, aber "
      "**anders formuliert** sind, stehen hier als **ZWEI Einträge**. Die "
      "inhaltliche Zusammenführung nach **Z2-R** ist **Sache des Bewerters** und "
      "wird in der Spalte **„identisch mit P-xx“** je Eintrag festgehalten.\n")

    a("\n---\n")
    a("\n## 2. Z2-R — der Wortlaut, nach dem zusammenzuführen ist (§6, wörtlich)\n")
    a("\n" + sections["Z2-R"])

    a("\n---\n")
    a("\n## 3. Die vier auszufüllenden Dimensionen (§6, wörtlich)\n")
    a("\n### 3.1 `kind` — `structural` | `semantic`\n")
    a("\n" + sections["kind"])
    a("\n### 3.2 Z2-P — Prüfbarkeit\n")
    a("\n> Die **alte Fassung ist überholt** (02.09.2026, S1-A1c) und steht im "
      "Protokoll durchgestrichen; **gültig ist die folgende**.\n")
    a("\n" + sections["Z2-P"])
    a("\n### 3.3 Z2-G — Gehalt, DREIWERTIG plus „unklar“\n")
    a("\n> **Werteliste:** **Spiegelung** · **negierte Spiegelung** · **normativ** — "
      "plus **„unklar“** nach der Grenzfall-Regel am Ende dieses Abschnitts. "
      "**Alle drei Werte werden getrennt berichtet.** „unklar“ wird **nicht "
      "stillschweigend einer Seite zugeschlagen**.\n")
    a("\n" + sections["Z2-G"])
    a("\n### 3.4 Z2-Z — Zuordnung zum Abweichungstyp (Ebene 1)\n")
    a("\n> **Werteliste, sechs Kategorien plus zwei getrennte Auffangwerte:** "
      "`FORBIDDEN_RELATION` · `CYCLE` · `ABSENCE_REQUIRED` · "
      "`FORBIDDEN_SIGNATURE_TYPE` · `STRUCTURAL_PLACEMENT` · `API_CONTRACT` — dazu "
      "**„sonstige“** (Auffangkategorie **innerhalb** der Kodierung) und **„keiner "
      "der sechs“** (begründete Feststellung, dass die **Kodierung den Vorschlag "
      "nicht trägt**). Die beiden sind **getrennt auszuweisen**.\n")
    a("\n" + sections["Z2-Z"])

    a("\n---\n")
    a("\n## 4. Z2-W und Granularität — maschinell, nicht auszufüllen (§6, wörtlich)\n")
    a("\n" + sections["Z2-W"])
    a("\n> **Herkunft der Werte in diesem Blatt:** je Eintrag aus der archivierten "
      "`validation.json` des Laufs **übernommen**, in dem der Vorschlag steht "
      "(Prüfliste **§5.3 Punkt 2**). **Maschinell entstanden, keine "
      "Bewerterleistung.** Bei mechanisch identischen Vorschlägen stimmten die "
      "Werte aller Herkünfte überein; das Werkzeug bricht ab, wenn sie es nicht "
      "tun.\n")
    a("\n> **Granularitätszählung:** wie viele Einträge in `scope.components` sich "
      "gegen das Ist-Modell als **package**, **module** oder **artefact** auflösen "
      "und wie viele **unresolved** bleiben. **BEOBACHTUNG, KEIN KRITERIUM.**\n")

    a("\n---\n")
    a("\n## 5. Die Einträge\n")
    a("\n**Reihenfolge randomisiert** (Seed oben) — sie trägt **keine Information** "
      "über Bedingung, Modell oder Lauf. **Nicht enthalten sind** Bedingung, "
      "Modellname, Slot, die ursprüngliche `id`, die Zahl der Läufe je Eintrag, die "
      "Position im Array und Zeitstempel. Sie stehen **ausschliesslich im "
      "Zuordnungsschlüssel**.\n")

    for entry in entries:
        others = ", ".join(x for x in labels if x != entry["label"])
        gran = entry["granularitaet"]
        a(f"\n---\n\n### {entry['label']}\n")
        a("\n| Feld | Wert |\n|---|---|\n")
        a(f"| `category` | `{entry['category']}` |\n")
        a(f"| `severity` | `{entry['severity']}` |\n")
        a("| `scope.components` | "
          + " · ".join(f"`{c}`" for c in entry["components"]) + " |\n")
        a("\n**`statement`** — zeichengleich wie im Rohartefakt:\n\n")
        a(fence(entry["statement"]) + "\n")
        a("\n**Maschinell übernommen (nicht auszufüllen):**\n\n")
        a("| Maschinelle Angabe | Wert |\n|---|---|\n")
        a(f"| **Z2-W** wohlgeformt | **{'ja' if entry['z2w_wohlgeformt'] else 'nein'}** |\n")
        checks = ", ".join(
            f"{k}={'ja' if v else 'NEIN'}" for k, v in entry["z2w_pruefungen"].items())
        a(f"| Z2-W Einzelprüfungen (§5.3 Punkt 2) | {checks} |\n")
        befunde = "; ".join(entry["z2w_befunde"]) if entry["z2w_befunde"] else "—"
        a(f"| Z2-W Befunde | {befunde} |\n")
        a(f"| Granularität (BEOBACHTUNG, kein Kriterium) | package {gran['package']} · "
          f"module {gran['module']} · artefact {gran['artefact']} · "
          f"unresolved {gran['unresolved']} |\n")
        a("\n**Auszufüllen — vier Dimensionen aus §6:**\n\n")
        a("| Dimension | Werteliste | Eintrag |\n|---|---|---|\n")
        a("| `kind` | `structural` \\| `semantic` |  |\n")
        a("| **Z2-P** Prüfbarkeit | prüfbar \\| nicht prüfbar — bei Abhängigkeit von "
          "einem **externen** Import: nicht entscheidbar **MIT VERMERK DER URSACHE** "
          "(§6, Pflicht) |  |\n")
        a("| **Z2-G** Gehalt | Spiegelung \\| negierte Spiegelung \\| normativ \\| "
          "unklar |  |\n")
        a("| **Z2-Z** Zuordnung | `FORBIDDEN_RELATION` \\| `CYCLE` \\| "
          "`ABSENCE_REQUIRED` \\| `FORBIDDEN_SIGNATURE_TYPE` \\| "
          "`STRUCTURAL_PLACEMENT` \\| `API_CONTRACT` \\| sonstige \\| keiner der "
          "sechs |  |\n")
        a("\n**Dedup nach Z2-R (inhaltlich, vom Bewerter):**\n\n")
        a("| Feld | Eintrag |\n|---|---|\n")
        a(f"| identisch mit P-xx | *(leer, oder eines aus: {others})* |\n")
        a("| Grenzfall nach §6 Punkt 1? | *(ja/nein — bei ja in Abschnitt 6 "
          "eintragen)* |\n")
        a("| Bemerkung |  |\n")

    a("\n---\n")
    a("\n## 6. Grenzfall-Tabelle — Form nach Anhang B des Protokolls (wörtlich)\n")
    a("\n" + sections["AnhangB"])
    a("\n> **Für dieses Blatt:** als **Vorschlag-ID** dient das Etikett `P-xx`. Die "
      "ausgefüllte Tabelle gehört **vollständig in den Befund** (§7 Punkt 7), nicht "
      "in die Ablage.\n")

    a("\n---\n")
    a("\n## 7. Grenze der Verblindung — nach T-Z2-7 zu vermerken\n")
    a("\nDie Verblindung entfernt jede **Kennung** und jede **Kennzahl**, aus der die "
      "Bedingung ableitbar wäre — insbesondere die **Zahl der Läufe je Eintrag**: "
      "sie steht **nur im Zuordnungsschlüssel**, weil sie in einer der beiden "
      "Zellen mit der Bedingung zusammenfiele.\n")
    a("\n**Nicht heilbar, hier benannt:** **Stil und Länge der `statement`-Texte** "
      "können die **Modellklasse** dennoch erkennbar machen; ebenso die "
      "**Zuschnittsgewohnheit** der `scope.components`. Der Wortlaut der Vorschläge "
      "ist die **Messgrösse selbst** und darf nicht angetastet werden — die "
      "Verblindung ist deshalb **eine Verblindung gegen die Kennzeichnung, keine "
      "gegen den Text**. Das ist unter **T-Z2-7** zu führen: die vorab fixierten "
      "Entscheidungsregeln aus §6 und die vollständig ausgewiesene "
      "Grenzfall-Tabelle tragen die Kodierung, nicht die Undurchdringlichkeit der "
      "Darreichung.\n")

    a("\n---\n")
    a("\n## 8. Was dieses Blatt NICHT enthält\n")
    a("\n- **Keine Bewertung.** `kind`, Z2-P, Z2-G und Z2-Z sind **leer** — nicht "
      "vorgeschlagen, nicht angedeutet.\n")
    a("- **N₁ ist NICHT gezählt.** N₁ ist nach §7 Punkt 9 die **Pro-Lauf-Dedup des "
      "ersten Laufs** nach **Z2-R**; Z2-R ist inhaltlich und steht aus.\n")
    a("- **Kein Verdikt zu E1–E4**, keine Kennzahl, kein Anteil, kein Vergleich "
      "zwischen den Zellen.\n")
    a("- **Keine inhaltliche Zusammenführung** — nur die mechanische aus "
      "Abschnitt 1.\n")
    a("- **Keine Umformulierung**: `category`, `statement`, `severity` und "
      "`scope.components` stehen **zeichengleich** wie in `raw_response.json`.\n")
    return "".join(parts)


def render_key(entries: list[dict]) -> str:
    payload = {
        "zweck": (
            "Zuordnungsschlüssel zum verblindeten Bewertungsblatt "
            "`bewertungsblatt.md`. NACH §6 ERST NACH ABSCHLUSS DER BEWERTUNG ZU "
            "ÖFFNEN."
        ),
        "auftrag": "S10",
        "werkzeug": "tools/prepare_z2_review.py",
        "protokoll_sha256": PROTO_SHA,
        "seed": SEED,
        "seed_verwendung": f"random.Random({SEED}).shuffle(...) auf die Einträge "
                           "in Reihenfolge ihres ersten Auftretens "
                           "(Zellen k2_b1, k3_b1; Slots run0, run1, run2; "
                           "Position aufsteigend)",
        "identitaetsdefinition": IDENTITY_DEFINITION,
        "identitaetstupel": ["category", "statement", "severity",
                            "sorted(scope.components)"],
        "hinweis_vielfachheit": (
            "Die Vielfachheit ist eine Kennzahl, aus der die Bedingung ableitbar "
            "ist -- in einer der beiden Zellen sind die drei Generate "
            "zeichengleich. Sie steht deshalb NUR hier und nicht im Blatt."
        ),
        "eintraege": [
            {
                "etikett": e["label"],
                "vielfachheit": len(e["members"]),
                "herkunft": [
                    {
                        "bedingung": m["cell"],
                        "slot": m["slot"],
                        "position": m["position"],
                        "id": m["rule"]["id"],
                    }
                    for m in e["members"]
                ],
                "bedingungen": sorted({m["cell"] for m in e["members"]}),
                "slots": sorted({m["slot"] for m in e["members"]}),
                "positionen": sorted({m["position"] for m in e["members"]}),
                "ids": sorted({m["rule"]["id"] for m in e["members"]}),
            }
            for e in entries
        ],
    }
    return json.dumps(payload, ensure_ascii=False, indent=2) + "\n"


def render_sums(out_dir: Path) -> str:
    names = sorted(p.name for p in out_dir.iterdir()
                   if p.is_file() and p.name != SUMS_NAME)
    return "".join(f"{sha256_file(out_dir / n)}  {n}\n" for n in names)


def generate(out_dir: Path) -> list[dict]:
    sections = extract_sections(read_protocol())
    records = collect()
    entries = shuffle(group(records))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / SHEET_NAME).write_text(render_sheet(entries, sections), encoding="utf-8")
    (out_dir / KEY_NAME).write_text(render_key(entries), encoding="utf-8")
    (out_dir / SUMS_NAME).write_text(render_sums(out_dir), encoding="utf-8")
    return entries


def report(entries: list[dict], records_total: int) -> None:
    per_cell: dict[str, int] = {}
    for e in entries:
        for cell in {m["cell"] for m in e["members"]}:
            per_cell[cell] = per_cell.get(cell, 0) + 1
    print(f"roh: {records_total} Vorschläge")
    print(f"mechanisch verschieden: {len(entries)} Einträge")
    for cell in CELLS:
        print(f"  {cell}: {per_cell.get(cell, 0)}")
    print(f"seed: {SEED}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", default=str(OUT_DIR),
                        help="Zielverzeichnis (Vorgabe: data/z2/bewertung)")
    parser.add_argument("--check", action="store_true",
                        help="zweiter Lauf in ein Temporaerverzeichnis, "
                             "Bytevergleich gegen --out")
    args = parser.parse_args()

    out_dir = Path(args.out)
    entries = generate(out_dir)
    report(entries, sum(len(e["members"]) for e in entries))

    if args.check:
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            second = Path(tmp) / "bewertung"
            generate(second)
            diffs = []
            for name in (SHEET_NAME, KEY_NAME, SUMS_NAME):
                if (out_dir / name).read_bytes() != (second / name).read_bytes():
                    diffs.append(name)
            if diffs:
                die(f"NICHT deterministisch, abweichend: {', '.join(diffs)}")
            print("Determinismus: zwei Laeufe, drei Dateien bytegleich -- OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
