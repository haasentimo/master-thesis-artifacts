#!/usr/bin/env python3
"""Check the document invariants of the thesis repo. Read-only, exit 0 or 1.

Five invariants, each reported separately with actual and expected value:

  (A) The SHA256 of the frozen evaluation protocol equals the value carried as current
      in section 3 of the freeze report. This is the movement check: the protocol SHA is
      the anchor that makes an unregistered byte change visible. Protocol section 0.1
      rule 5 (rev 36) says every change to the protocol is a revision, a plain hash
      pull-through included -- so a mismatch here is always a finding, never noise.

  (B) The revision number in the protocol head equals the highest row of the section 10
      revision table equals the newest entry of the head's revision history. Protocol
      section 0.1 rule 1 requires an amendment to be carried in both places, never only
      one; this checks that the head agrees with both.

  (C) The SHA256 of the evaluation specification equals the value registered in protocol
      section 1 (addendum rev 30) AND the value in section 0.1 (frozen measurement
      state). Both places are checked separately, because the failure mode this guards
      against is exactly that the two drift apart.

  (D) Two parts, because a hashed inventory can fail in two directions.
      (D1) `sha256sum -c` passes in data/soll and in every directory under data/campaign
      that carries a SHA256SUMS -- this catches CHANGED and MISSING files.
      (D2) Every file in those directories is listed. `sha256sum -c` reads only the
      entries it is given, so an ADDED file is invisible to it; C10c showed the checker
      passing before the checksums were regenerated. The listing is therefore compared in
      BOTH directions, and unlisted files are named.

The checker never writes and never repairs. It reads no run artifact content: for (D) it
reports only the OK/failed counts that sha256sum returns and the NAMES of unlisted files.

  (E) The SHA256 of the three evaluation instruments -- tools/evaluate_campaign.py,
      tools/match_k4k5.py and this checker itself -- equals the value registered in
      protocol section 0.1. From the first evaluation run over data/campaign/k* onward
      these three PRODUCE the chapter-7 numbers: a silent edit to a calculation rule or a
      marker would move every table without moving any input.

Background: C6b-2b (commit 0c1cc34) pulled the specification's SHA through into the
protocol -- correctly -- but without head revision, history entry or section 10 row. The
resulting byte state was attested in no document. C6b-0a registered it as rev 36 and
added this checker as the latch.
"""

from __future__ import annotations

import hashlib
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

PROTOCOL = ROOT / "docs" / "protokolle" / "eval_protokoll_phase04.md"
SPEC = ROOT / "docs" / "protokolle" / "c6_auswertungsspezifikation.md"
FREEZE_REPORT = ROOT / "docs" / "repo-kontext" / "c5b_bericht_protokoll_freeze.md"

HEX64 = re.compile(r"\b([0-9a-f]{64})\b")
BOLD_HEX64 = re.compile(r"\*\*`([0-9a-f]{64})`\*\*")


class InvariantError(Exception):
    """A parse failure: the anchor a check needs is absent or ambiguous."""


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read(path: Path) -> str:
    if not path.is_file():
        raise InvariantError(f"Datei fehlt: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def current_hash_in_cell(row: str) -> str:
    """The current hash of a table row: struck predecessors precede it, so take the last.

    Prefer a bold-and-backticked hash (the form the reports use for the current value);
    fall back to the last plain 64-hex in the row.
    """
    bold = BOLD_HEX64.findall(row)
    if bold:
        return bold[-1]
    plain = HEX64.findall(row)
    if not plain:
        raise InvariantError(f"kein SHA256 in der Zeile: {row[:80]}...")
    return plain[-1]


# --- (A) protocol SHA against the freeze report ---------------------------------------


def expected_protocol_hash() -> tuple[int, str]:
    """The value carried as current in section 3 of the freeze report.

    The table lists every attested state. Struck rows are superseded; a row whose
    revision cell reads *(keine)* is an attested byte state that was never a revision
    (the C6b-2b intermediate state). Current is the unstruck row with the highest
    revision number.
    """
    text = read(FREEZE_REPORT)
    lines = text.splitlines()
    try:
        head = next(
            i for i, line in enumerate(lines)
            if line.startswith("| Datei | Rev. | Commit | SHA256 |")
        )
    except StopIteration:
        raise InvariantError(
            "Tabellenkopf '| Datei | Rev. | Commit | SHA256 |' in §3 nicht gefunden"
        )

    candidates: list[tuple[int, str]] = []
    for line in lines[head + 2:]:
        if not line.startswith("|"):
            break
        if "eval_protokoll_phase04.md" not in line:
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 4:
            continue
        if cells[0].startswith("~~"):          # superseded state
            continue
        rev_match = re.search(r"(\d+)", cells[1].replace("~~", ""))
        if not rev_match:                       # *(keine)* -- never a revision
            continue
        candidates.append((int(rev_match.group(1)), current_hash_in_cell(cells[3])))

    if not candidates:
        raise InvariantError("keine aktuelle (ungestrichene) Protokollzeile in §3")
    return max(candidates, key=lambda pair: pair[0])


def check_a() -> tuple[bool, list[str]]:
    actual = sha256_file(PROTOCOL)
    rev, expected = expected_protocol_hash()
    if actual == expected:
        return True, [
            f"SHA256 {actual}",
            f"bezeugt in c5b_bericht_protokoll_freeze.md §3 als Rev. {rev}",
        ]
    return False, [
        f"IST  (Datei)              {actual}",
        f"SOLL (c5b §3, Rev. {rev})   {expected}",
        "Der Bytestand des Protokolls ist nicht bezeugt. Entweder ist das Protokoll",
        "geändert und die Änderung nicht als Revision registriert (§0.1 Punkt 5), oder",
        "der Nachzug in §3 des Freeze-Berichts fehlt.",
    ]


# --- (B) revision number in three places -----------------------------------------------


def head_region(text: str) -> str:
    """The head: everything before the first '## ' heading."""
    match = re.search(r"^## ", text, re.MULTILINE)
    return text[: match.start()] if match else text


def check_b() -> tuple[bool, list[str]]:
    text = read(PROTOCOL)
    head = head_region(text)

    stand = [
        line for line in head.splitlines()
        if line.startswith("Stand: ") and not line.startswith("~~")
    ]
    if not stand:
        raise InvariantError("keine ungestrichene 'Stand:'-Zeile im Kopf")
    head_rev = re.search(r"\(Rev\. (\d+)\)", stand[0])
    if not head_rev:
        raise InvariantError(f"keine Revisionsnummer in: {stand[0][:80]}")
    head_rev_no = int(head_rev.group(1))

    history = [int(m) for m in re.findall(r"^Rev\. (\d+):", head, re.MULTILINE)]
    if not history:
        raise InvariantError("keine Revisionshistorie im Kopf gefunden")
    newest_history = max(history)

    rows = [
        int(m)
        for m in re.findall(r"^\| (\d+) \| \d{2}\.\d{2}\.\d{4} \|", text, re.MULTILINE)
    ]
    if not rows:
        raise InvariantError("keine Revisionszeilen in der §10-Tabelle gefunden")
    highest_row = max(rows)

    if head_rev_no == newest_history == highest_row:
        return True, [
            f"Kopf Rev. {head_rev_no} = Revisionshistorie Rev. {newest_history} "
            f"= §10-Zeile {highest_row}"
        ]
    return False, [
        f"Kopfzeile            Rev. {head_rev_no}",
        f"Revisionshistorie    Rev. {newest_history}  (neuester Eintrag im Kopf)",
        f"§10-Tabelle          Rev. {highest_row}  (höchste Zeile)",
        "Die drei Stellen müssen dieselbe Nummer tragen (§0.1 Punkt 1: geführt in",
        "Revisionshistorie UND Amendments-Tabelle, nie nur an einer der beiden Stellen).",
    ]


# --- (C) specification SHA in protocol section 1 and section 0.1 -----------------------


def check_c() -> tuple[bool, list[str]]:
    actual = sha256_file(SPEC)
    text = read(PROTOCOL)

    places = {
        "§0.1 (Messstand)": [
            line for line in text.splitlines()
            if line.startswith("| **Auswertungsspezifikation** |")
        ],
        "§1 (Nachtrag Rev. 30)": [
            line for line in text.splitlines()
            if line.startswith("> | `docs/protokolle/c6_auswertungsspezifikation.md` |")
        ],
    }

    ok = True
    detail: list[str] = []
    for where, rows in places.items():
        if len(rows) != 1:
            raise InvariantError(
                f"Zeile für die Auswertungsspezifikation in {where} nicht eindeutig "
                f"({len(rows)} Treffer)"
            )
        registered = current_hash_in_cell(rows[0])
        if registered == actual:
            detail.append(f"{where}: {registered}")
        else:
            ok = False
            detail.append(f"{where}: IST (Datei) {actual}")
            detail.append(f"{' ' * len(where)}  SOLL (registriert) {registered}")

    if ok:
        detail.insert(0, f"SHA256 {actual}, an beiden Stellen zeichengleich")
        return True, detail
    detail.append(
        "Der registrierte Auswertungseingang und die Datei fallen auseinander (§0.1)."
    )
    return False, detail


# --- (D) sha256sum -c over the hashed inventories --------------------------------------


def sums_files() -> list[Path]:
    found = []
    soll = ROOT / "data" / "soll" / "SHA256SUMS"
    if soll.is_file():
        found.append(soll)
    campaign = ROOT / "data" / "campaign"
    if campaign.is_dir():
        found.extend(sorted(campaign.rglob("SHA256SUMS")))
    if not found:
        raise InvariantError("keine SHA256SUMS unter data/soll oder data/campaign")
    return found


def verify_sums(sums: Path) -> tuple[bool, str]:
    """Run sha256sum -c. Paths inside a SHA256SUMS are relative either to its own
    directory (data/soll) or to the repo root (data/campaign/*); pick the cwd that
    resolves the first entry."""
    first = next(
        (line for line in sums.read_text(encoding="utf-8").splitlines() if line.strip()),
        None,
    )
    if first is None:
        return False, "SHA256SUMS ist leer"
    name = first.split(None, 1)[1].lstrip("*") if len(first.split(None, 1)) > 1 else ""
    if (sums.parent / name).exists():
        cwd = sums.parent
    elif (ROOT / name).exists():
        cwd = ROOT
    else:
        return False, f"erster Eintrag nicht auflösbar: {name}"

    proc = subprocess.run(
        ["sha256sum", "-c", str(sums)],
        cwd=cwd,
        capture_output=True,
        text=True,
    )
    out = proc.stdout.splitlines()
    ok = sum(1 for line in out if line.endswith(": OK"))
    bad = [line for line in out if not line.endswith(": OK") and line.strip()]
    if proc.returncode == 0 and not bad:
        return True, f"{ok} von {ok} OK"
    detail = "; ".join(bad[:5]) or proc.stderr.strip().splitlines()[:1]
    return False, f"{ok} OK, {len(bad)} nicht OK (Exit {proc.returncode}): {detail}"


# --- (D2) the listing compared in both directions --------------------------------------
#
# `sha256sum -c` reads only the entries it is given. A file ADDED to a hashed inventory is
# therefore invisible to it -- which is how the checker came up green in C10c before the
# checksums were regenerated. The second half of (D) walks the directories instead of the
# list and asks the opposite question: is every file here attested?

HASHED_ROOTS = (Path("data") / "soll", Path("data") / "campaign")

# A SHA256SUMS cannot list itself -- the hash would change on writing it. Same argument as
# for the protocol hash in (A), which is why that one lives in the freeze report.
SELF_EXEMPT = "SHA256SUMS"

# LIVING DOCUMENTS -- decided exceptions, protocol rev. 39 (C6c-a, 28.08.2026).
#
# These seven files are unlisted, and they STAY unlisted. A hash is the wrong instrument
# for them: `journal.jsonl` is append-only and grows as planned, the `MANIFEST.md` are
# documents to be continued. A checksum over them would tear on every LEGITIMATE
# continuation and would train the reader to regenerate it -- which destroys the detector.
# Integrity for them comes from the commit history; the snapshot hash inside the manifest
# stays where it is.
#
# None of them is a run artifact, and after C6c-a none of them is the SOURCE of a T-value
# any more: T7 is computed from the hashed run manifests under `data/campaign/manifests/`
# (protocol rev. 39). `journal.jsonl` and the prose manifests are the CROSS-CHECK; the
# harness reports a divergence and adapts neither side.
#
# The list is EXPLICIT on purpose. Each entry is reported by name on every run as a known,
# decided exception -- never as a failure. A file that is neither listed in a SHA256SUMS
# nor on this list is a FAILURE: that is the latch, and it is what makes an EIGHTH
# unlisted file visible instead of absorbed.
DECISION = "entschieden C6c-a 28.08.2026, Protokoll Rev. 39"

KNOWN_UNLISTED: dict[str, str] = {
    "data/soll/MANIFEST.md":
        "lebendes Dokument: Herleitungsdoku der sieben Messeingaenge, selbst kein "
        f"Messeingang (0.1 fuehrt sieben von sieben) — {DECISION}",
    "data/campaign/MANIFEST.md":
        "lebendes Dokument: fortzuschreibendes Kampagnenmanifest, seit C6c-a "
        f"Gegenprobe zu T7, nicht dessen Quelle — {DECISION}",
    "data/campaign/README.md":
        f"lebendes Dokument: Ablagebeschreibung, traegt keinen Messwert — {DECISION}",
    "data/campaign/journal.jsonl":
        "append-only und planmaessig wachsend: ein Hash risse bei jeder legitimen "
        f"Fortschreibung; seit C6c-a Gegenprobe zu T7, nicht dessen Quelle — {DECISION}",
    "data/campaign/control/journal.jsonl":
        "append-only und planmaessig wachsend: Journal des Kontrollbestands, dessen "
        f"Laufmanifeste und Rohartefakte sehr wohl gehasht sind — {DECISION}",
    "data/campaign/k2/MANIFEST.md":
        f"lebendes Dokument: fortzuschreibendes Blockmanifest — {DECISION}",
    "data/campaign/k3/MANIFEST.md":
        f"lebendes Dokument: fortzuschreibendes Blockmanifest — {DECISION}",
}


def listed_paths() -> set[Path]:
    """Every path any SHA256SUMS attests, resolved.

    The entries are relative either to the SHA256SUMS' own directory (data/soll) or to the
    repo root (data/campaign/*) -- the same ambiguity `verify_sums` resolves, resolved the
    same way, per entry.
    """
    listed: set[Path] = set()
    for sums in sums_files():
        for line in sums.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            parts = line.split(None, 1)
            if len(parts) < 2:
                continue
            name = parts[1].lstrip("*")
            for base in (sums.parent, ROOT):
                candidate = base / name
                if candidate.exists():
                    listed.add(candidate.resolve())
                    break
    return listed


def hashed_directories() -> list[Path]:
    """Every directory under the hashed roots, `__pycache__` excluded.

    Walking the roots rather than the inventories is deliberate: a directory that NO
    SHA256SUMS reaches would otherwise never be looked at, and `data/campaign/` itself is
    exactly such a directory.
    """
    found: list[Path] = []
    for rel in HASHED_ROOTS:
        root = ROOT / rel
        if not root.is_dir():
            continue
        found.append(root)
        found.extend(
            d for d in sorted(root.rglob("*"))
            if d.is_dir() and "__pycache__" not in d.parts
        )
    return found


def check_unlisted() -> tuple[bool, list[str]]:
    listed = listed_paths()
    directories = hashed_directories()
    unexpected: list[str] = []
    reported: list[str] = []
    scanned = 0
    for directory in directories:
        for entry in sorted(directory.iterdir()):
            if not entry.is_file():
                continue
            scanned += 1
            if entry.resolve() in listed or entry.name == SELF_EXEMPT:
                continue
            rel = str(entry.relative_to(ROOT))
            if rel in KNOWN_UNLISTED:
                reported.append(f"{rel} — {KNOWN_UNLISTED[rel]}")
                continue
            else:
                unexpected.append(rel)

    detail = [f"{scanned} Dateien in {len(directories)} Verzeichnissen geprüft, "
              f"{len(listed)} Pfade gelistet"]
    if reported:
        detail.append(f"AUSNAHME lebende Dokumente, {len(reported)} von "
                      f"{len(KNOWN_UNLISTED)} entschiedenen — Protokoll Rev. 39; ein "
                      f"achter ungelisteter Pfad ist ein FEHLSCHLAG, keine Ausnahme")
    detail.extend(f"MELDUNG  {line}" for line in reported)
    stale = [rel for rel in KNOWN_UNLISTED
             if not (ROOT / rel).is_file() or (ROOT / rel).resolve() in listed]
    detail.extend(
        f"HINWEIS  {rel} — inzwischen gelistet oder fort; Eintrag kann entfallen"
        for rel in sorted(stale)
    )
    if unexpected:
        detail.append("")
        detail.extend(f"UNGELISTET  {rel}" for rel in unexpected)
        detail.append(
            "Diese Dateien liegen in einem gehashten Bestand, ohne dass ein SHA256SUMS"
        )
        detail.append(
            "sie bezeugt. `sha256sum -c` sieht sie nicht — es prüft nur die gelisteten"
        )
        detail.append("Einträge (belegt in C10c).")
        return False, detail
    return True, detail


def check_d() -> tuple[bool, list[str]]:
    ok = True
    detail = []
    for sums in sums_files():
        passed, message = verify_sums(sums)
        ok = ok and passed
        mark = "OK  " if passed else "FEHL"
        detail.append(f"{mark} {sums.parent.relative_to(ROOT)}: {message}")
    if not ok:
        detail.append(
            "Ein gehashter Bestand stimmt nicht mehr mit seinem SHA256SUMS überein."
        )

    listing_ok, listing_detail = check_unlisted()
    detail.append("")
    detail.append(f"{'OK  ' if listing_ok else 'FEHL'} Listing gegen SHA256SUMS, "
                  f"beide Richtungen:")
    detail.extend(f"     {line}" if line else "" for line in listing_detail)
    return ok and listing_ok, detail


# --- (E) the three evaluation instruments against protocol section 0.1 -----------------
#
# From the first evaluation run over data/campaign/k* onward the three tools that PRODUCE
# the chapter-7 numbers are part of the measurement state: a silent edit to a calculation
# rule or a marker would change every table without changing any input. Their SHA256 is
# therefore registered in protocol section 0.1 and checked here, the same way the
# specification is checked in (C).

INSTRUMENTS = (
    "tools/evaluate_campaign.py",
    "tools/match_k4k5.py",
    "tools/check_doc_invariants.py",
)


def registered_instrument_hash(text: str, name: str) -> str:
    """The hash registered for one instrument in protocol section 0.1.

    The row form is the one the seven measurement inputs use: `<path>` = `<hash>`, struck
    predecessors before the current value.
    """
    needle = f"`{name}` = "
    rows = [line for line in text.splitlines() if needle in line]
    if len(rows) != 1:
        raise InvariantError(
            f"Zeile für {name} in §0.1 nicht eindeutig ({len(rows)} Treffer)"
        )
    return current_hash_in_cell(rows[0])


def check_e() -> tuple[bool, list[str]]:
    text = read(PROTOCOL)
    ok = True
    detail: list[str] = []
    for name in INSTRUMENTS:
        path = ROOT / name
        if not path.is_file():
            ok = False
            detail.append(f"FEHLT  {name}")
            continue
        actual = sha256_file(path)
        registered = registered_instrument_hash(text, name)
        if actual == registered:
            detail.append(f"OK   {name}  {actual}")
        else:
            ok = False
            detail.append(f"FEHL {name}")
            detail.append(f"       IST  (Datei)      {actual}")
            detail.append(f"       SOLL (§0.1)       {registered}")
    if not ok:
        detail.append(
            "Ein Auswertungsinstrument weicht von dem in §0.1 registrierten Stand ab."
        )
        detail.append(
            "Ab dem ersten Auswertungslauf über data/campaign/k* ist jede Änderung an"
        )
        detail.append(
            "diesen drei Dateien eine datierte Revision mit Begründung (§0.1 Punkt 6)."
        )
    return ok, detail


CHECKS = [
    ("A", "Protokoll-SHA gegen c5b_bericht_protokoll_freeze.md §3", check_a),
    ("B", "Kopf-Revision = §10-Höchstzeile = neuester Historieneintrag", check_b),
    ("C", "Spezifikations-SHA gegen Protokoll §1 UND §0.1", check_c),
    ("D", "sha256sum -c UND Listing beidseitig, data/soll und data/campaign", check_d),
    ("E", "SHA256 der drei Auswertungsinstrumente gegen Protokoll §0.1", check_e),
]


def main() -> int:
    print(f"check_doc_invariants — Repo {ROOT}")
    print()
    failed = []
    for key, title, check in CHECKS:
        try:
            passed, detail = check()
        except InvariantError as error:
            passed, detail = False, [f"PARSE-FEHLER: {error}"]
        print(f"[{'OK ' if passed else 'FEHL'}] ({key}) {title}")
        for line in detail:
            print(f"        {line}")
        print()
        if not passed:
            failed.append(key)

    if failed:
        print(f"ERGEBNIS: FEHLGESCHLAGEN — Invariante(n) {', '.join(failed)}")
        return 1
    print(f"ERGEBNIS: alle {len(CHECKS)} Invarianten erfüllt")
    return 0


if __name__ == "__main__":
    sys.exit(main())
