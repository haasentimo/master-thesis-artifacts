#!/usr/bin/env python3
"""Tally the author-decided overlap matrix for Z2 protocol section 7 item 5.

The matrix `data/z2/bewertung/ueberlappmatrix.md` carries, per authored rule
statement, a machine-produced pre-finding (S12) and the three decision fields
the author filled in.  This tool READS both, checks the sheet for completeness
and consistency, counts `n of 16` mechanically, breaks the count down, and
tallies the author's decisions against the pre-finding.

It never re-decides a row: an author decision is copied, never corrected, and
anything that looks odd is reported, not changed.  The tool is stdlib-only and
deterministic -- two runs produce byte-identical output.

Vocabulary is fixed by the task: the number is carried exclusively as
"n von 16 autorenformulierten Statements haben eine Entsprechung unter den
Vorschlaegen".  It is neither a correctness nor a recall measure.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
MATRIX = REPO / "data" / "z2" / "bewertung" / "ueberlappmatrix.md"
AUSWERTUNG = REPO / "data" / "z2" / "bewertung" / "auswertung.json"
SCHLUESSEL = REPO / "data" / "z2" / "bewertung" / "zuordnungsschluessel.json"
RULES = REPO / "data" / "soll" / "architecture-rules.yaml"

AUFTRAG = "S13"
STAND = "2026-09-06"

LABEL_RE = re.compile(r"P-\d{2}")
# Split a markdown row on pipes that are not backslash-escaped: the sheet's own
# field name `ENTSCHEIDUNG (ja \| nein)` carries an escaped pipe.
CELL_SPLIT_RE = re.compile(r"(?<!\\)\|")


class Abbruch(Exception):
    """A precondition or consistency check failed; nothing is tallied."""


def norm(text: str) -> str:
    """NFC-normalise and strip -- the sheet's own identity convention."""
    return unicodedata.normalize("NFC", text).strip()


def read_rule_categories(path: Path) -> list[tuple[str, str]]:
    """Pair each rule id with its category by position in the frozen YAML.

    stdlib-only, so the file is read line-wise rather than parsed: every `- id:`
    is followed directly by its `category:` (verified for all sixteen entries).
    """
    pairs: list[tuple[str, str]] = []
    pending: str | None = None
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\s*-\s+id:\s*(\S+)\s*$", line)
        if m:
            pending = m.group(1)
            continue
        m = re.match(r"^\s*category:\s*(\S+)\s*$", line)
        if m and pending is not None:
            pairs.append((pending, m.group(1)))
            pending = None
    return pairs


def split_sections(text: str, level: str) -> list[tuple[str, str]]:
    """Split markdown into (heading, body) pairs at the given heading level."""
    out: list[tuple[str, str]] = []
    head: str | None = None
    buf: list[str] = []
    for line in text.splitlines():
        if line.startswith(level + " "):
            if head is not None:
                out.append((head, "\n".join(buf)))
            head = line[len(level) + 1 :].strip()
            buf = []
        elif head is not None:
            buf.append(line)
    if head is not None:
        out.append((head, "\n".join(buf)))
    return out


def table_cells(block: str) -> dict[str, str]:
    """Collect every two-column markdown table row of a block as key -> value."""
    cells: dict[str, str] = {}
    for line in block.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|") or not stripped.endswith("|"):
            continue
        parts = CELL_SPLIT_RE.split(stripped)[1:-1]
        if len(parts) != 2:
            continue
        key, val = norm(parts[0]), norm(parts[1])
        if not key or set(key) <= {"-", ":"}:
            continue
        key = key.replace("**", "").replace("\\|", "|").strip()
        cells.setdefault(key, val.replace("**", "").replace("\\|", "|").strip())
    return cells


def labels_in(field: str) -> list[str]:
    """Extract the P-xx labels of a field, in order of appearance, deduplicated."""
    seen: list[str] = []
    for lab in LABEL_RE.findall(field):
        if lab not in seen:
            seen.append(lab)
    return seen


def parse_matrix(text: str) -> list[dict]:
    """Read part 3 of the sheet: one record per authored rule statement."""
    body = text.split("## 3. Die Matrix", 1)
    if len(body) != 2:
        raise Abbruch("Teil 3 der Matrix nicht gefunden")
    part3 = body[1].split("## 4. Summenfeld", 1)[0]

    rows: list[dict] = []
    for head, block in split_sections(part3, "###"):
        soll_id = head.strip()
        if not soll_id.startswith("R-"):
            continue
        vor_block, _, ent_block = block.partition("#### ENTSCHEIDUNG DES AUTORS")
        if not ent_block:
            raise Abbruch(f"{soll_id}: Entscheidungsblock fehlt")
        pre_block = vor_block.split("#### VORBEFUND", 1)
        stmt_cells = table_cells(pre_block[0])
        vor_cells = table_cells(pre_block[1]) if len(pre_block) > 1 else {}
        ent_cells = table_cells(ent_block)

        rows.append(
            {
                "soll_id": soll_id,
                "category": stmt_cells.get("`category`", ""),
                "vorbefund": vor_cells.get("(a) VORBEFUND (maschinell)", ""),
                "kandidaten_feld": vor_cells.get("(b) Kandidat(en)", ""),
                "vorbefund_begruendung": vor_cells.get(
                    "(c) Begründung des Vorbefunds", ""
                ),
                "entscheidung_feld": ent_cells.get("ENTSCHEIDUNG (ja | nein)", ""),
                "etiketten_feld": ent_cells.get("durch welche(s) P-xx", ""),
                "begruendung": ent_cells.get("Begründung des Autors", ""),
            }
        )
    return rows


def read_summenfeld(text: str) -> str:
    """Return the author's entry in the sheet's sum field, or the empty marker."""
    tail = text.split("## 4. Summenfeld", 1)
    if len(tail) != 2:
        return ""
    return table_cells(tail[1]).get("n von 16", "")


def klassen_von(auswertung: dict) -> list[dict]:
    """The sixteen Z2-R equivalence classes, as the reviewer merged them (S11)."""
    return list(auswertung["z2r_klassen"]["klassen"])


def klassenname(klasse: dict) -> str:
    return " + ".join(klasse["mitglieder"])


def build(matrix_text: str, auswertung: dict, rules: list[tuple[str, str]]) -> dict:
    rows = parse_matrix(matrix_text)
    meldungen: list[str] = []

    # --- P5 completeness -------------------------------------------------
    if len(rows) != 16:
        raise Abbruch(f"P5: {len(rows)} Abschnitte statt 16")
    for r in rows:
        e = r["entscheidung_feld"]
        if e not in ("ja", "nein"):
            raise Abbruch(
                f"P5: {r['soll_id']} Feld ENTSCHEIDUNG ist {e!r}, nicht 'ja'/'nein'"
            )
        if not r["begruendung"]:
            raise Abbruch(f"P5: {r['soll_id']} Feld 'Begründung des Autors' leer")
        if e == "ja" and not labels_in(r["etiketten_feld"]):
            raise Abbruch(f"P5: {r['soll_id']} Entscheidung 'ja' ohne P-xx")

    # --- consistency (a)-(d) --------------------------------------------
    klassen = klassen_von(auswertung)
    if len(klassen) != 16:
        raise Abbruch(f"{len(klassen)} Äquivalenzklassen statt 16")
    label_to_class = {m: klassenname(k) for k in klassen for m in k["mitglieder"]}
    class_bedingungen = {klassenname(k): sorted(k["bedingungen"]) for k in klassen}

    for r in rows:
        r["etiketten"] = labels_in(r["etiketten_feld"])
        r["kandidaten"] = labels_in(r["kandidaten_feld"])
        # (a) every named label must be a member of one of the sixteen classes
        for lab in r["etiketten"]:
            if lab not in label_to_class:
                raise Abbruch(
                    f"(a) {r['soll_id']}: Etikett {lab} ist in keiner der 16 "
                    f"Äquivalenzklassen aus auswertung.json"
                )
        r["klassen"] = sorted({label_to_class[l] for l in r["etiketten"]})
        r["kandidat_klassen"] = sorted(
            {label_to_class[l] for l in r["kandidaten"] if l in label_to_class}
        )
        # (b) a 'nein' row must name no label
        r["b_verstoss"] = r["entscheidung_feld"] == "nein" and bool(r["etiketten"])
        if r["b_verstoss"]:
            meldungen.append(
                f"(b) {r['soll_id']}: Entscheidung 'nein', dennoch Etikett(en) "
                f"{', '.join(r['etiketten'])} genannt — nicht geändert, in der "
                f"Zählung als 'nein' geführt"
            )
        # (c) confirm: a 'ja' row names at least one label
        r["c_ok"] = r["entscheidung_feld"] != "ja" or bool(r["etiketten"])
        # (d) the author's reasoning must not be character-identical to the pre-finding's
        r["d_zeichengleich"] = (
            norm(r["begruendung"]) == norm(r["vorbefund_begruendung"])
            and bool(norm(r["begruendung"]))
        )
        if r["d_zeichengleich"]:
            meldungen.append(
                f"(d) {r['soll_id']}: Begründung des Autors zeichengleich mit der "
                f"Begründung des Vorbefunds — HINWEIS, nicht gewertet"
            )
        r["vorbefund_kandidat"] = r["vorbefund"].startswith("Kandidat vorhanden")

    # --- n / 16 -----------------------------------------------------------
    ja_rows = [r for r in rows if r["entscheidung_feld"] == "ja"]
    n = len(ja_rows)

    # --- 3a: per soll category -------------------------------------------
    cat_of = dict(rules)
    if sorted(cat_of) != sorted(r["soll_id"] for r in rows):
        raise Abbruch("Soll-IDs der Matrix decken sich nicht mit architecture-rules.yaml")
    nenner = Counter(c for _, c in rules)
    zaehler = Counter(cat_of[r["soll_id"]] for r in ja_rows)
    je_kategorie = {
        cat: {"mit_entsprechung": zaehler.get(cat, 0), "bezugsmenge": nenner[cat]}
        for cat in sorted(nenner)
    }

    # --- 3b: per condition (blinding lifted with S11) ---------------------
    je_bedingung: dict[str, list[str]] = {}
    for r in ja_rows:
        beds = sorted({b for k in r["klassen"] for b in class_bedingungen[k]})
        herkunft = (
            "beide" if len(beds) > 1 else (beds[0] if beds else "unbestimmt")
        )
        r["herkunft"] = herkunft
        je_bedingung.setdefault(herkunft, []).append(r["soll_id"])
    je_bedingung = {k: sorted(v) for k, v in sorted(je_bedingung.items())}

    # --- 3c: multiple mentions in both directions ------------------------
    klasse_zu_statements: dict[str, list[str]] = {}
    for r in ja_rows:
        for k in r["klassen"]:
            klasse_zu_statements.setdefault(k, []).append(r["soll_id"])
    mehrfach_klassen = {
        k: sorted(v) for k, v in sorted(klasse_zu_statements.items()) if len(v) > 1
    }
    mehrfach_statements = {
        r["soll_id"]: list(r["klassen"]) for r in ja_rows if len(r["klassen"]) > 1
    }

    # --- 3d: classes named in no row -------------------------------------
    alle_klassen = [klassenname(k) for k in klassen]
    ungenannt = [k for k in alle_klassen if k not in klasse_zu_statements]

    # --- 4: author against the pre-finding -------------------------------
    felder = {
        "kandidat_und_ja_bestaetigt": [],
        "kandidat_und_nein_ueberstimmt_verworfen": [],
        "kein_kandidat_und_ja_ueberstimmt_ergaenzt": [],
        "kein_kandidat_und_nein_bestaetigt": [],
    }
    for r in rows:
        ja = r["entscheidung_feld"] == "ja"
        if r["vorbefund_kandidat"] and ja:
            felder["kandidat_und_ja_bestaetigt"].append(r["soll_id"])
        elif r["vorbefund_kandidat"] and not ja:
            felder["kandidat_und_nein_ueberstimmt_verworfen"].append(r["soll_id"])
        elif not r["vorbefund_kandidat"] and ja:
            felder["kein_kandidat_und_ja_ueberstimmt_ergaenzt"].append(r["soll_id"])
        else:
            felder["kein_kandidat_und_nein_bestaetigt"].append(r["soll_id"])

    etikettvergleich = []
    for r in ja_rows:
        if not r["vorbefund_kandidat"]:
            continue
        gen, kand = set(r["klassen"]), set(r["kandidat_klassen"])
        if gen == kand:
            urteil = "deckungsgleich"
        elif gen < kand:
            urteil = "echte Teilmenge der Kandidaten"
        elif gen > kand:
            urteil = "echte Obermenge der Kandidaten"
        else:
            urteil = "abweichend"
        etikettvergleich.append(
            {
                "soll_id": r["soll_id"],
                "genannt": list(r["klassen"]),
                "kandidaten": list(r["kandidat_klassen"]),
                "urteil": urteil,
                "nicht_uebernommen": sorted(kand - gen),
                "zusaetzlich_genannt": sorted(gen - kand),
            }
        )

    return {
        "rows": rows,
        "n": n,
        "meldungen": meldungen,
        "je_kategorie": je_kategorie,
        "je_bedingung": je_bedingung,
        "mehrfach_klassen": mehrfach_klassen,
        "mehrfach_statements": mehrfach_statements,
        "ungenannte_klassen": ungenannt,
        "alle_klassen": alle_klassen,
        "ueberstimmung": felder,
        "etikettvergleich": etikettvergleich,
        "class_bedingungen": class_bedingungen,
    }


def abschnitt(res: dict, summenfeld: str) -> dict:
    """The `ueberlapp_p5` section that is merged into auswertung.json."""
    rows = res["rows"]
    return {
        "dokument": "Überlapp §7 Punkt 5 — mechanische Auszählung der Autorenentscheidungen",
        "auftrag": AUFTRAG,
        "stand": STAND,
        "werkzeug": "tools/tally_z2_overlap.py",
        "status": "MECHANISCHE AUSZÄHLUNG OHNE DEUTUNG UND OHNE NACHBEWERTUNG",
        "keine_nachbewertung": (
            "Dieses Werkzeug zählt aus, was der Autor in `ueberlappmatrix.md` "
            "entschieden hat. Keine Entscheidung wurde korrigiert, ergänzt, "
            "plausibilisiert oder aus der Zählung genommen. Auffälligkeiten stehen "
            "unter `meldungen`; sie sind gemeldet, nicht gewertet."
        ),
        "sprachregelung": (
            "Die Größe wird ausschliesslich geführt als „n von 16 autorenformulierten "
            "Statements haben eine Entsprechung unter den Vorschlägen“. Sie wird als "
            "Bruch n / 16 angegeben, ohne Prozentangabe — bei 16 Fällen wäre eine "
            "Prozentzahl Scheingenauigkeit."
        ),
        "einhegung": {
            "charakter": "sekundär und deskriptiv (§7 Punkt 5)",
            "kein_korrektheitsmass": True,
            "kein_recallmass": True,
            "autor_beider_seiten": (
                "Der Autor hat die sechzehn Soll-Statements und das Messobjekt "
                "formuliert, auf das sie passen (§7 Punkt 5, gleiche Logik wie die "
                "Gold-Degradierung in Befund 01)."
            ),
            "t_z2_8": (
                "Die Affordanzen der sechs Kategorien stecken strukturell im "
                "Testrepo; eine hohe Überschneidung wäre insoweit Eigenschaft des "
                "Messobjekts, nicht Leistung des Modells."
            ),
        },
        "abgrenzung_zu_§7_punkt_3": (
            "Die Abdeckungsmatrix (§7 Punkt 3, dort 1 von 6) fragt, welche der sechs "
            "KATEGORIEN durch mindestens einen normativen, prüfbaren Vorschlag belegt "
            "sind; §7 Punkt 5 fragt nach Entsprechungen zu den sechzehn EINZELNEN "
            "Statements. Verschiedene Größen, verschiedene Nenner — nicht zu "
            "verwechseln, nicht gegeneinander zu rechnen."
        ),
        "zweistufiges_verfahren": (
            "Stufe 1 war die maschinelle Nachschlagearbeit aus S12 (Vorbefund, "
            "Kandidaten, Begründung, Prüfspur); Stufe 2 ist die Entscheidung des "
            "Autors je Zeile. Ausgezählt wird ausschliesslich Stufe 2."
        ),
        "verblindung": (
            "Die Verblindung ist mit S11 aufgehoben. Die Aufschlüsselung je Bedingung "
            "entsteht danach und wird als solche berichtet; §7 Punkt 5 ist sekundär und "
            "deskriptiv, nicht bedingungsvergleichend — sie wird ohne Vergleichsaussage "
            "geführt."
        ),
        "ergebnis": {
            "n": res["n"],
            "nenner": 16,
            "als_bruch": f"{res['n']} / 16",
            "lesart": (
                f"{res['n']} von 16 autorenformulierten Statements haben eine "
                f"Entsprechung unter den Vorschlägen."
            ),
            "herleitung": "Zahl der Abschnitte in Teil 3 mit Entscheidungsfeld „ja“.",
            "ja": [r["soll_id"] for r in rows if r["entscheidung_feld"] == "ja"],
            "nein": [r["soll_id"] for r in rows if r["entscheidung_feld"] == "nein"],
            "summenfeld_des_blattes": summenfeld,
            "summenfeld_vergleich": (
                "Das Summenfeld in Teil 4 ist unausgefüllt geblieben "
                f"(Eintrag {summenfeld!r}); ein Gegenhalten war daher nicht möglich. "
                "Maßgeblich ist die mechanische Zählung."
                if summenfeld in ("", "___")
                else (
                    f"Summenfeld des Blattes {summenfeld!r} gegen mechanische Zählung "
                    f"{res['n']}. Maßgeblich ist die mechanische Zählung; das Blatt "
                    "wurde nicht geändert."
                )
            ),
        },
        "je_zeile": [
            {
                "soll_id": r["soll_id"],
                "soll_kategorie": r["category"],
                "entscheidung": r["entscheidung_feld"],
                "genannte_etiketten": r["etiketten"],
                "genannte_klassen": r["klassen"],
                "vorbefund": "Kandidat vorhanden" if r["vorbefund_kandidat"] else "kein Kandidat",
                "kandidaten_des_vorbefunds": r["kandidat_klassen"],
                "herkunft_der_genannten_klassen": r.get("herkunft", ""),
            }
            for r in rows
        ],
        "aufschluesselung_je_soll_kategorie": {
            "bezugsmenge": (
                "die 16 Statements, je Kategorie deren Zahl aus "
                "data/soll/architecture-rules.yaml gezählt"
            ),
            "werte": res["je_kategorie"],
        },
        "aufschluesselung_je_bedingung": {
            "bezugsmenge": (
                f"die {res['n']} Statements mit Entscheidung „ja“, aufgeschlüsselt nach "
                "der Herkunft der genannten Vorschlagsklassen"
            ),
            "vermerk": (
                "Entsteht nach Aufhebung der Verblindung (S11). Keine "
                "Vergleichsaussage zwischen den Bedingungen."
            ),
            "werte": res["je_bedingung"],
        },
        "mehrfachnennungen": {
            "bezugsmenge": f"die {res['n']} Statements mit Entscheidung „ja“",
            "klasse_fuer_mehrere_statements": res["mehrfach_klassen"],
            "statement_nennt_mehrere_klassen": res["mehrfach_statements"],
        },
        "in_keiner_zeile_genannte_klassen": {
            "bezugsmenge": "die 16 Z2-R-Äquivalenzklassen der bewerteten Vorschläge",
            "zahl": len(res["ungenannte_klassen"]),
            "klassen": res["ungenannte_klassen"],
        },
        "ueberstimmungsquote": {
            "bezugsmenge": "alle 16 Zeilen",
            "erlaeuterung": (
                "Maschineller Vorbefund aus S12 gegen die Entscheidung des Autors. "
                "Die Zahlen belegen, in welchem Umfang der Vorbefund übernommen und in "
                "welchem er überstimmt wurde. Keine Deutung dazu."
            ),
            "felder": {k: {"zahl": len(v), "soll_ids": v} for k, v in res["ueberstimmung"].items()},
            "etikettvergleich_bei_ja_mit_kandidat": res["etikettvergleich"],
        },
        "meldungen_nicht_geaendert": res["meldungen"],
        "ausstehend": [
            "Die Verdikte zu E1–E4 stehen aus.",
            "Befund 09 steht aus.",
            "Die Entscheidung I3 fällt datiert am 13.09.2026.",
        ],
    }


def render(sec: dict, res: dict) -> str:
    """Human-readable report on stdout; deterministic, no timestamps."""
    out: list[str] = []
    w = out.append
    w(f"tally_z2_overlap — Auftrag {AUFTRAG}, Stand {STAND}")
    w("")
    w(f"ERGEBNIS  {sec['ergebnis']['als_bruch']}")
    w(f"          {sec['ergebnis']['lesart']}")
    w(f"          Herleitung: {sec['ergebnis']['herleitung']}")
    w(f"          {sec['ergebnis']['summenfeld_vergleich']}")
    w("")
    w("JE ZEILE")
    w("  Soll-ID         | Entsch. | genannt                | Vorbefund")
    for z in sec["je_zeile"]:
        w(
            "  %-15s | %-7s | %-22s | %s"
            % (
                z["soll_id"],
                z["entscheidung"],
                ", ".join(z["genannte_klassen"]) or "—",
                z["vorbefund"],
            )
        )
    w("")
    w("JE SOLL-KATEGORIE  (Bezugsmenge: %s)" % sec["aufschluesselung_je_soll_kategorie"]["bezugsmenge"])
    for cat, v in sec["aufschluesselung_je_soll_kategorie"]["werte"].items():
        w("  %-26s %d von %d" % (cat, v["mit_entsprechung"], v["bezugsmenge"]))
    w("")
    w("JE BEDINGUNG  (Bezugsmenge: %s)" % sec["aufschluesselung_je_bedingung"]["bezugsmenge"])
    w("  Vermerk: %s" % sec["aufschluesselung_je_bedingung"]["vermerk"])
    for k, v in sec["aufschluesselung_je_bedingung"]["werte"].items():
        w("  %-12s %d  (%s)" % (k, len(v), ", ".join(v)))
    w("")
    w("MEHRFACHNENNUNGEN")
    mk = sec["mehrfachnennungen"]["klasse_fuer_mehrere_statements"]
    w("  Klasse für mehrere Statements: " + (
        "; ".join(f"{k} -> {', '.join(v)}" for k, v in mk.items()) if mk else "keine"))
    ms = sec["mehrfachnennungen"]["statement_nennt_mehrere_klassen"]
    w("  Statement nennt mehrere Klassen: " + (
        "; ".join(f"{k} -> {', '.join(v)}" for k, v in ms.items()) if ms else "keines"))
    w("")
    ung = sec["in_keiner_zeile_genannte_klassen"]
    w("IN KEINER ZEILE GENANNT  (Bezugsmenge: %s)" % ung["bezugsmenge"])
    w("  %d von 16: %s" % (ung["zahl"], ", ".join(ung["klassen"]) or "—"))
    w("")
    w("ÜBERSTIMMUNGSQUOTE  (Bezugsmenge: %s)" % sec["ueberstimmungsquote"]["bezugsmenge"])
    for k, v in sec["ueberstimmungsquote"]["felder"].items():
        w("  %-42s %2d  (%s)" % (k, v["zahl"], ", ".join(v["soll_ids"]) or "—"))
    w("  Etikettvergleich bei „ja“ mit Kandidat:")
    for e in sec["ueberstimmungsquote"]["etikettvergleich_bei_ja_mit_kandidat"]:
        w("    %-15s %s" % (e["soll_id"], e["urteil"]))
        if e["nicht_uebernommen"]:
            w("      nicht übernommen: " + ", ".join(e["nicht_uebernommen"]))
        if e["zusaetzlich_genannt"]:
            w("      zusätzlich genannt: " + ", ".join(e["zusaetzlich_genannt"]))
    w("")
    w("MELDUNGEN (nicht geändert)")
    for m in sec["meldungen_nicht_geaendert"] or ["keine"]:
        w("  " + m)
    w("")
    w("ABGRENZUNG  " + sec["abgrenzung_zu_§7_punkt_3"])
    w("EINHEGUNG   " + sec["sprachregelung"])
    return "\n".join(out) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--write",
        action="store_true",
        help="merge the ueberlapp_p5 section into auswertung.json",
    )
    args = ap.parse_args()

    matrix_text = MATRIX.read_text(encoding="utf-8")
    auswertung = json.loads(AUSWERTUNG.read_text(encoding="utf-8"))
    rules = read_rule_categories(RULES)

    try:
        res = build(matrix_text, auswertung, rules)
    except Abbruch as exc:
        print(f"ABBRUCH: {exc}", file=sys.stderr)
        return 1

    sec = abschnitt(res, read_summenfeld(matrix_text))
    sys.stdout.write(render(sec, res))

    if args.write:
        auswertung["ueberlapp_p5"] = sec
        AUSWERTUNG.write_text(
            json.dumps(auswertung, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        print(f"\ngeschrieben: {AUSWERTUNG.relative_to(REPO)} (Abschnitt ueberlapp_p5)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
