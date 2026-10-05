#!/usr/bin/env python3
"""Campaign evaluation harness (C6b) — fills the chapter 7 table skeletons.

TWO OUTPUTS FROM ONE RUN
------------------------
(a) a machine-readable intermediate result (JSON) carrying every cell with its marker,
(b) a Markdown rendering that fills tables T1-T9 in EXACTLY the structure of
    docs/kapitel/kapitel7_tabellenskelette.md — same columns, same order, same footnotes,
    print order T1, T7, T2, T3, T4, T5, T6, T8, T9.

The skeleton's structure is never changed here. If a figure does not fit a cell, that is
reported, not fixed by rebuilding the table.

FOUR MARKERS, NOT INTERCHANGEABLE (skeleton §1, §1.1)
-----------------------------------------------------
    " — "   not expressible, from T1/T8, pre-registered — NEVER from missing data
    "n. b." not formable (K4/CYCLE localized, appendix row A-17) — pre-registered
    "n. e." not collected, derived from T7 (no valid run)
    value   computed

A cell may NEVER carry 0 where " — ", "n. b." or "n. e." holds. That is enforced by
`Cell.__post_init__` and by `assert_marker_discipline`, not by care.

A marker is ALWAYS printed in code markup, in every table — `marker_text()` is the only
place that renders one, and assertion R10 checks the finished text. Without the markup a
marker is not distinguishable from prose, and the three of them say three different
things. R10 also refuses any number in exponent notation: `plain()` renders `9190540`
where `%g` would have written `9.19054e+06` (C11c D1/D2).

T7 COMES OUT OF THE HASHED RUN MANIFESTS (C6c-a, protocol rev. 39)
------------------------------------------------------------------
One manifest per invocation under `data/campaign/manifests/`, every one of them
attested by a block `SHA256SUMS`. Read per invocation: verdict, `invalid_reasons`,
`calls_total`, `calls_invalid`, `calls_transport_failed`, `changed_files_count`,
`valid_final` (derived: measured minus invalid) and the external wall clock.

`journal.jsonl`, `campaign/MANIFEST.md` and the block manifests are the CROSS-CHECK,
never the source. They are prose and an append-only record; nothing hashes them.
A divergence is printed as ABWEICHUNG in T7 and reported on stderr — the harness
never adapts one side to the other (skeleton T7.3 building rule; protocol rev. 39).

BLINDNESS (precised C6c-a: the run manifests are EXPLICITLY allowed)
--------------------------------------------------------------------
Without --with-campaign the harness reads from data/campaign ONLY the metadata on the
allow-list in `CAMPAIGN_METADATA`: the run manifests, `journal.jsonl`, `MANIFEST.md`,
`README.md` and `SHA256SUMS`. The manifests carry verdicts, counters and provenance --
no findings. Every other path under the campaign root is a violation, `control/` and
the k1..k5 run artifacts included. That is the C6b mode: the harness is tested against
the published control values, never calibrated on the campaign figures.

tools/match_k4k5.py is imported as a module — the K4/K5 comparison rules are not
reimplemented here.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import statistics
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import match_k4k5  # noqa: E402  (same tools/ directory, imported not reimplemented)

REPO = Path(__file__).resolve().parent.parent

# --------------------------------------------------------------------------------------
# Markers
# --------------------------------------------------------------------------------------

DASH = " — "      # not expressible  (T1/T8, pre-registered)
NB = "n. b."      # not formable     (pre-registered)
NE = "n. e."      # not collected    (T7)
EMPTY = ""        # not inserted by this run — the skeleton's own "(leer)"

MARKERS = (DASH, NB, NE)

# A COMPUTED value, not a marker: the question does not arise. Used where a derived cell
# has a well-defined "does not apply" state that would otherwise be printed as an empty
# string -- kein-EN without a `strict` hit is the case this was introduced for (protocol
# rev. 40). Keeping it apart from the four markers is the whole point: an empty cell and
# a computed "does not apply" said the same thing in the first evaluation run, and the
# marker legend reads an empty cell as "not inserted by this run".
NOT_APPLICABLE = "entfällt"

CONFIGS = ["K1", "K2", "K3", "K4", "K5"]
LLM_CONFIGS = ["K2", "K3"]

# --------------------------------------------------------------------------------------
# Pre-registered tables. These are tool properties, not measurements: the harness READS
# them, it never writes them (skeleton T8 (ii)).
# --------------------------------------------------------------------------------------

# T1 Soll, verbatim from the skeleton (protocol §3). Values: ja | nein | teilweise.
T1_SOLL: dict[str, dict[str, str]] = {
    # scenario                     K1        K4           K5           K2/K3
    "LAYER_BACK_CALL":             {"K1": "ja",   "K4": "ja",         "K5": "ja",         "K2": "ja",   "K3": "ja"},
    "LAYER_SKIP_CALL":             {"K1": "ja",   "K4": "ja",         "K5": "ja",         "K2": "ja",   "K3": "ja"},
    "PROTECTED_MODULE":            {"K1": "ja",   "K4": "ja",         "K5": "ja",         "K2": "ja",   "K3": "ja"},
    "INDEPENDENCE":                {"K1": "ja",   "K4": "ja",         "K5": "ja",         "K2": "ja",   "K3": "ja"},
    "CYCLE_SIBLING":               {"K1": "ja",   "K4": "ja",         "K5": "teilweise",  "K2": "nein", "K3": "nein"},
    "CYCLE_PARENT_CHILD":          {"K1": "ja",   "K4": "nein",       "K5": "teilweise",  "K2": "nein", "K3": "nein"},
    "MISSING_PORT_REFERENCE":      {"K1": "nein", "K4": "nein",       "K5": "ja",         "K2": "ja",   "K3": "ja"},
    "FRAMEWORK_TYPE_IN_SIGNATURE": {"K1": "nein", "K4": "nein",       "K5": "nein",       "K2": "ja",   "K3": "ja"},
    "INCORRECT_LOCATION":          {"K1": "nein", "K4": "teilweise",  "K5": "nein",       "K2": "ja",   "K3": "ja"},
    "SIGNATURE_DEVIATION":         {"K1": "nein", "K4": "nein",       "K5": "nein",       "K2": "ja",   "K3": "ja"},
}

SCENARIO_N = {
    "LAYER_BACK_CALL": 3, "LAYER_SKIP_CALL": 3, "PROTECTED_MODULE": 3, "INDEPENDENCE": 3,
    "CYCLE_SIBLING": 3, "CYCLE_PARENT_CHILD": 1, "MISSING_PORT_REFERENCE": 4,
    "FRAMEWORK_TYPE_IN_SIGNATURE": 4, "INCORRECT_LOCATION": 4, "SIGNATURE_DEVIATION": 4,
}

SCENARIO_ORDER = list(SCENARIO_N)

SCENARIO_TO_L1 = {
    "LAYER_BACK_CALL": "FORBIDDEN_RELATION", "LAYER_SKIP_CALL": "FORBIDDEN_RELATION",
    "PROTECTED_MODULE": "FORBIDDEN_RELATION", "INDEPENDENCE": "FORBIDDEN_RELATION",
    "CYCLE_SIBLING": "CYCLE", "CYCLE_PARENT_CHILD": "CYCLE",
    "MISSING_PORT_REFERENCE": "ABSENCE_REQUIRED",
    "FRAMEWORK_TYPE_IN_SIGNATURE": "FORBIDDEN_SIGNATURE_TYPE",
    "INCORRECT_LOCATION": "STRUCTURAL_PLACEMENT", "SIGNATURE_DEVIATION": "API_CONTRACT",
}

L1_ORDER = ["FORBIDDEN_RELATION", "CYCLE", "ABSENCE_REQUIRED",
            "FORBIDDEN_SIGNATURE_TYPE", "STRUCTURAL_PLACEMENT", "API_CONTRACT"]
L1_N = {"FORBIDDEN_RELATION": 12, "CYCLE": 4, "ABSENCE_REQUIRED": 4,
        "FORBIDDEN_SIGNATURE_TYPE": 4, "STRUCTURAL_PLACEMENT": 4, "API_CONTRACT": 4}

# The " — " cells of T2, verbatim from the skeleton. A cell is " — " when the scenario is
# not expressible BY CONSTRUCTION for that configuration (T8 / T8.1) — never because a run
# is missing. "teilweise" cells are computed, not marked.
DASH_CELLS: set[tuple[str, str]] = {
    ("K1", "MISSING_PORT_REFERENCE"), ("K1", "FRAMEWORK_TYPE_IN_SIGNATURE"),
    ("K1", "INCORRECT_LOCATION"), ("K1", "SIGNATURE_DEVIATION"),
    ("K2", "CYCLE_SIBLING"), ("K2", "CYCLE_PARENT_CHILD"),
    ("K3", "CYCLE_SIBLING"), ("K3", "CYCLE_PARENT_CHILD"),
    ("K4", "CYCLE_PARENT_CHILD"),          # strict only; localized is n. b., see NB_CELLS
    ("K4", "MISSING_PORT_REFERENCE"), ("K4", "FRAMEWORK_TYPE_IN_SIGNATURE"),
    ("K4", "SIGNATURE_DEVIATION"),
    ("K5", "FRAMEWORK_TYPE_IN_SIGNATURE"), ("K5", "INCORRECT_LOCATION"),
    ("K5", "SIGNATURE_DEVIATION"),
}

# "n. b." cells: the metric is not formable from the tool's output form. Appendix row
# A-17, protocol §4 addendum rev 30: the acyclic_siblings block carries no module name.
NB_CELLS: set[tuple[str, str, str]] = {
    ("K4", "CYCLE_SIBLING", "localized"),
    ("K4", "CYCLE_PARENT_CHILD", "localized"),
}

# T5, second total row: denominators of the expressible range. They follow from T8, not
# from a measurement (skeleton T5 auflage (1)).
UF4_DENOMINATOR = {"K1": 16, "K2": 28, "K3": 28, "K4": 19, "K5": 20}

# The two pre-registered clean-control messages (§5 cases 4 and 5; protocol §5 addenda
# rev 16 and rev 18). DECIDED on 2026-08-28 (protocol rev 37, spec §7.2): they STAY IN the
# headline counter and are shown separately on top of it -- they are NOT subtracted. A
# predicted message on clean code is still a message; predictability is an addition, not a
# deduction. The subtracted reading is carried alongside but is not the headline.
PREREGISTERED_CONTROL = [
    ("depot.core.adapters", ("R-PROTECT-1",),
     "Adapterfassade `depot.core.adapters`, `R-PROTECT-1`", "Protokoll §5 Nachtrag Rev. 16"),
    ("depot.orders.services", ("R-PORT-2", "R-PORT-3"),
     "Nicht-Träger-Portregel auf `orders_services` (`R-PORT-2`/`R-PORT-3`)",
     "Protokoll §5 Nachtrag Rev. 18"),
]

# --------------------------------------------------------------------------------------
# Cell — value or marker, never both, never 0 behind a marker
# --------------------------------------------------------------------------------------


class MarkerViolation(AssertionError):
    """A cell would carry a number where a marker holds, or the reverse."""


def marker_text(marker: str) -> str:
    """A marker AS PRINTED — always in code markup, in every table (C11c D1).

    The markup is not decoration: without it a marker is not distinguishable from prose,
    and the three of them carry three different statements (skeleton 1.1). T5 printed the
    raw marker string while T1, T2 and T4 printed the marked-up one, so the SAME marker
    looked like two different things in one document (C11b 7 (1), 72 cells). One function
    now, so that a second rendering path cannot drift again. Enforced on the finished text
    by assertion R10.
    """
    return f"`{marker}`" if marker != DASH else "` — `"


@dataclass
class Cell:
    """One table cell. Exactly one of `value` and `marker` is set."""
    value: Any = None
    marker: str | None = None
    note: str = ""
    source: str = ""

    def __post_init__(self) -> None:
        if self.marker is not None:
            if self.marker not in MARKERS:
                raise MarkerViolation(f"unbekannter Marker {self.marker!r}")
            if self.value is not None:
                raise MarkerViolation(
                    f"Zelle trägt Marker {self.marker!r} UND Wert {self.value!r} — "
                    "eine Zelle darf niemals 0 tragen, wo ein Marker gilt")

    @property
    def text(self) -> str:
        if self.marker is not None:
            return marker_text(self.marker)
        if self.value is None:
            return EMPTY
        return str(self.value)

    def as_json(self) -> dict[str, Any]:
        return {"value": self.value, "marker": self.marker,
                "note": self.note, "source": self.source}


def marked(marker: str, note: str = "", source: str = "") -> Cell:
    return Cell(marker=marker, note=note, source=source)


def valued(value: Any, note: str = "", source: str = "") -> Cell:
    return Cell(value=value, note=note, source=source)


def blank(note: str = "") -> Cell:
    """Not inserted by this run — the skeleton's own '(leer)'. Distinct from every
    marker: it says nothing about the measurement, only that this run did not fill it."""
    return Cell(value=None, note=note)


# --------------------------------------------------------------------------------------
# Small helpers
# --------------------------------------------------------------------------------------


def plain(value: Any) -> str:
    """`%g` WITHOUT the exponent fallback — `9190540`, never `9.19054e+06` (C11c D2).

    `%g` switches to exponent notation above six significant digits, which printed two K3
    millisecond sums of T6 in a notation no other cell of the same row used (C11b 7 (2)).
    Only the NOTATION changes here, never the value: an int renders exactly, a float keeps
    its `%g` rendering and falls back to a plain decimal form only where `%g` would have
    produced an exponent. Enforced on the finished text by assertion R10.
    """
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, int):
        return str(value)
    text = f"{value:g}"
    if "e" not in text and "E" not in text:
        return text
    return f"{value:.0f}" if value == int(value) else f"{value:f}".rstrip("0").rstrip(".")


def num(value: Any) -> str:
    """Render a COMPUTED number. A computed zero is printed as `0`, never as an empty
    string — that is assertion R2, and it is enforced here rather than left to care.

    `len(hits) or ''` produced an empty cell for every computed zero in the first
    evaluation run (C11a question 2); an empty cell is the skeleton marker "not inserted
    by this run", so a measured 0 and an unevaluated cell became indistinguishable.
    """
    text = plain(value)
    if text == "":
        raise MarkerViolation(
            f"gerechnete Grösse {value!r} rendert zu einer Leerzeichenkette (R2)")
    return text


def run_list(values: list[int] | None) -> str:
    """The repetition counts printed SINGLY — `[0,0,1]` (spec §7.5 (5), rev. 40)."""
    if values is None:
        return NB
    return "[" + ",".join(num(v) for v in values) + "]"


def kein_en_cell(strict_cell: Cell, rest_exists: bool) -> Cell:
    """kein-EN on ONE aggregation stage — the EXISTENCE stage (protocol rev. 40).

    `strict` is an existence quantifier over the repetitions (spec §3) and is the SUBJECT
    of the rev. 31 wording ("ein `strict`-Treffer, der die Ruhezustandsrate nicht
    übersteigt"). The resting side is brought onto that same stage: it exists when at
    least one of the three C3b runs carried a finding of this module in this category.

    Three states, as before — only the stage of the comparison has moved:
      "ja"      strict hit that does NOT exceed the resting state -> no detection evidence
      "nein"    strict hit that DOES exceed it
      entfällt  no strict hit -- the question does not arise (COMPUTED, not a marker)

    A `strict` cell carrying a marker passes the marker on: kein-EN is derived from
    `strict`, so where `strict` is not expressible or not collected, neither is kein-EN.
    """
    if strict_cell.marker is not None:
        return marked(strict_cell.marker, "aus `strict` übernommen", strict_cell.source)
    if strict_cell.value != 1:
        return valued(NOT_APPLICABLE, "kein `strict`-Treffer — die Frage stellt sich nicht")
    return valued("ja" if rest_exists else "nein",
                  source="Protokoll Rev. 40 / Spez. §7.5 (3)")


def median(values: list[float]) -> float:
    """Median, never the mean (protocol §5 amendment 12.08., spec §7.1)."""
    return statistics.median(values)


def span(values: list[float]) -> tuple[float, float]:
    return (min(values), max(values))


def median_span_text(values: list[float]) -> str:
    """`Median (min–max)` — a bare median figure is inadmissible (spec §7.1)."""
    lo, hi = span(values)
    med = median(values)
    return f"{plain(med)} ({plain(lo)}–{plain(hi)})"


def segments(match_key: str) -> list[str]:
    """match_key = category|component|module|subjectKey (matchKey.ts:26, spec §3.1)."""
    return match_key.split("|")


def is_derived(finding: dict[str, Any]) -> bool:
    return str(finding.get("rule_id", "")).startswith("DERIVED:")


def split_by_mechanism(findings: Iterable[dict[str, Any]]) -> tuple[list, list]:
    """First join stage, BEFORE both metrics: filter by mechanism, not by invocation.

    K1 := records with rule_id prefix `DERIVED:`; K2/K3 := every other rule_id.
    Record counts are always kept apart, never summed (protocol §4 addendum rev 25;
    spec §2). Without this filter `localized` would be confounded, because the
    deterministic path runs along inside the K2/K3 invocations and writes into the same
    log.
    """
    derived, llm = [], []
    for f in findings:
        (derived if is_derived(f) else llm).append(f)
    return derived, llm


def expected_category(entry: dict[str, Any], path: str) -> str:
    """The expected category is path-dependent (spec §4, T2 footnote (f)).

    The rule engine knows only `layer-violation` and `cycle`; the four
    FORBIDDEN_RELATION scenarios all carry `layer-violation` there. In the LLM path the
    category comes from `rule.category` of the rule file, i.e. the level-1 category.
    """
    if path == "K1":
        return "cycle" if entry["category_l1"] == "CYCLE" else "layer-violation"
    return entry["category_l1"]


# --------------------------------------------------------------------------------------
# Loading
# --------------------------------------------------------------------------------------


# Every file this harness opens is recorded, so the blindness obligation can be AUDITED
# afterwards instead of merely asserted (see `blindness_violations`).
READS: list[Path] = []


def record_read(path: Path) -> Path:
    READS.append(Path(path).resolve())
    return path


def load_json(path: Path) -> Any:
    with record_read(path).open(encoding="utf-8") as handle:
        return json.load(handle)


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows = []
    with record_read(path).open(encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def read_text(path: Path) -> str:
    return record_read(path).read_text(encoding="utf-8")


# The blindness allow-list, EXPLICIT (C6c-a). Anything under the campaign root that is
# not matched here counts as a run artifact. Stated positively on purpose: a new artifact
# kind under `data/campaign/` is then a violation by default, not by oversight.
#
#   manifests/*.json   one run manifest per invocation -- verdicts, counters, provenance,
#                      NO findings; hashed in the block SHA256SUMS; source of T7
#   journal.jsonl      append-only record, one row per invocation -- cross-check
#   MANIFEST.md        campaign and block manifests, prose -- cross-check
#   README.md          storage description
#   SHA256SUMS         the attestation itself
CAMPAIGN_METADATA = ("journal.jsonl", "MANIFEST.md", "README.md", "SHA256SUMS")


def is_campaign_metadata(campaign: Path, path: Path) -> bool:
    """True for exactly the files the blindness obligation lets the harness open."""
    manifests = (campaign / "manifests").resolve()
    if path.parent == manifests and path.suffix == ".json":
        return True
    return path.name in CAMPAIGN_METADATA


def blindness_violations(campaign: Path) -> list[str]:
    """Which run artifacts under the campaign root were opened.

    Without --with-campaign this must be EMPTY: only the allow-listed metadata may be read
    from the campaign. The check runs over the recorded reads, not over intent, and it is
    a POSITIVE list -- everything under `data/campaign/` that is not on it counts as a run
    artifact, including `control/`, which the old block-wise test did not see at all.
    """
    root = campaign.resolve()
    hits = []
    for path in READS:
        if root in path.parents and not is_campaign_metadata(root, path):
            hits.append(str(path))
    return sorted(set(hits))


@dataclass
class ControlStock:
    """One clean-control stock (data/c3b-k2 or data/c3b-k3), read per run_index."""
    config: str
    denominator: int
    modules: list[str]
    per_run: dict[int, dict[str, list[dict]]] = field(default_factory=dict)
    derived_per_run: dict[int, int] = field(default_factory=dict)

    def findings(self, run_index: int, module: str) -> list[dict]:
        return self.per_run.get(run_index, {}).get(module, [])

    @property
    def run_indices(self) -> list[int]:
        return sorted(self.per_run)


def load_control(directory: Path, control_files: Path, config: str) -> ControlStock:
    """Load a clean-control stock. Module identity comes from the run log's `llm_call`
    record (`module`), the denominator from control_files.txt (spec §1.7, §7.2)."""
    denominator = sum(1 for line in read_text(control_files).splitlines()
                      if line.strip())
    per_run: dict[int, dict[str, list[dict]]] = {}
    derived_per_run: dict[int, int] = {}
    modules: list[str] = []
    for doc_path in sorted((directory / "runs").glob("*.json")):
        log_path = doc_path.with_suffix(".jsonl")
        module = None
        for record in load_jsonl(log_path):
            if record.get("record_type") == "llm_call":
                module = record.get("module")
                break
        if module is None:
            raise SystemExit(f"kein llm_call-Record in {log_path}")
        modules.append(module)
        doc = load_json(doc_path)
        for run in doc["runs"]:
            index = run["run_index"]
            derived, llm = split_by_mechanism(run["findings"])
            per_run.setdefault(index, {})[module] = llm
            derived_per_run[index] = derived_per_run.get(index, 0) + len(derived)
    return ControlStock(config=config, denominator=denominator, modules=modules,
                        per_run=per_run, derived_per_run=derived_per_run)


def is_preregistered(module: str, finding: dict[str, Any]) -> str | None:
    for mod, rules, label, _source in PREREGISTERED_CONTROL:
        if module == mod and finding.get("rule_id") in rules:
            return label
    return None


# --------------------------------------------------------------------------------------
# T3 — false-positive rates, two granularities
# --------------------------------------------------------------------------------------


def false_positive_rates(stock: ControlStock) -> dict[str, Any]:
    """Two granularities, kept in separate columns (skeleton T3).

    modulewise  : control modules with >= 1 finding / denominator — the reference for
                  `localized`, which dedups on module level (spec §7.2, §7.3).
    findingwise : findings in total, undeduplicated — the reference for `strict` and for
                  precision, because `strict` does not dedup and every further finding
                  counts as FP.

    HEADLINE = the modulewise series over ALL findings (spec §7.2 as decided in protocol
    rev 37, 2026-08-28). The two pre-registered messages stay in that counter and are
    shown separately in T3.1. The reading WITHOUT them is computed and carried alongside,
    so that it stays visible whether the two fall apart — on the real K2 stock they
    coincide (49), in the fixture they do not (4/6 against 3/6).
    """
    per_run_modules_all, per_run_modules_less, per_run_findings = [], [], []
    for index in stock.run_indices:
        table = stock.per_run[index]
        modules_all, modules_less, count = 0, 0, 0
        for module, findings in table.items():
            count += len(findings)
            if findings:
                modules_all += 1
            if [f for f in findings if not is_preregistered(module, f)]:
                modules_less += 1
        per_run_modules_all.append(modules_all)
        per_run_modules_less.append(modules_less)
        per_run_findings.append(count)
    return {
        "config": stock.config,
        "denominator": stock.denominator,
        "run_indices": stock.run_indices,
        "modulewise_all": per_run_modules_all,
        # the headline IS the all-findings series (spec §7.2, protocol rev 37)
        "modulewise_headline": per_run_modules_all,
        "modulewise_less_preregistered": per_run_modules_less,
        "findingwise": per_run_findings,
        "modulewise_all_median": median(per_run_modules_all),
        "modulewise_all_span": span(per_run_modules_all),
        "headline_median": median(per_run_modules_all),
        "headline_span": span(per_run_modules_all),
        "less_preregistered_median": median(per_run_modules_less),
        "less_preregistered_span": span(per_run_modules_less),
        "findingwise_median": median(per_run_findings),
        "findingwise_span": span(per_run_findings),
        "derived_per_run": [stock.derived_per_run.get(i, 0) for i in stock.run_indices],
    }


def preregistered_rows(stock: ControlStock) -> list[dict[str, Any]]:
    rows = []
    for mod, rules, label, source in PREREGISTERED_CONTROL:
        per_run = []
        for index in stock.run_indices:
            findings = stock.per_run[index].get(mod, [])
            per_run.append(len([f for f in findings if f.get("rule_id") in rules]))
        rows.append({"config": stock.config, "label": label, "source": source,
                     "per_run": per_run,
                     "runs_with": sum(1 for v in per_run if v > 0),
                     "runs_total": len(per_run)})
    return rows


# The reference classes of the control set. The archived analysis labels them K1..K4,
# which collides with the CONFIGURATION names K1..K5 — they are renamed here and are never
# printed as K1..K4 (protocol rev 27 addendum / rev 33 §9; c3b_k2_nachtrag_findingbezug.md
# part B3).
REFERENCE_CLASS_NAMES = {
    "K1": "Selbstbezug", "K2": "Fremdbezug", "K3": "Zielbezug", "K4": "nicht zuordenbar",
}
REFERENCE_CLASS_ORDER = ["Selbstbezug", "Fremdbezug", "Zielbezug", "nicht zuordenbar"]


def rule_id_distribution(stock: ControlStock) -> dict[str, int]:
    """Findings per rule_id over all runs, computed from the artifacts themselves —
    not copied from a report (appendix row A-10)."""
    counts: dict[str, int] = {}
    for index in stock.run_indices:
        for findings in stock.per_run[index].values():
            for f in findings:
                rid = f.get("rule_id", "?")
                counts[rid] = counts.get(rid, 0) + 1
    return dict(sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])))


def reference_classes(directory: Path, own_total: int) -> dict[str, Any] | None:
    """Descriptive cross-check of the control set (appendix rows A-09/A-10).

    Source is the archived `finding_reference_analysis.json`. Its class labels K1..K4 are
    renamed on read — the configurations are also called K1..K5, and printing both as
    "K1" in one chapter would be unreadable at best and wrong at worst.
    """
    path = directory / "finding_reference_analysis.json"
    if not path.is_file():
        return None
    data = load_json(path)
    block = data.get("b3_classification", {})
    counts = {REFERENCE_CLASS_NAMES.get(k, k): v for k, v in block.get("overall", {}).items()}
    pct = {REFERENCE_CLASS_NAMES.get(k, k): v for k, v in block.get("overall_pct", {}).items()}
    archived_total = data.get("n_total_llm_findings")
    return {"counts": counts, "pct": pct, "archived_total": archived_total,
            "own_total": own_total, "agrees": archived_total == own_total}


def control_preload(stock: ControlStock, entry: dict[str, Any]) -> list[int]:
    """Resting-state count per run: findings of the SAME module in the SAME category
    (spec §7.5 (3); protocol §5 addendum rev 31). Same repetition count on both sides."""
    module = entry["carrier_module"]
    category = entry["category_l1"]
    return [len([f for f in stock.findings(index, module) if f.get("category") == category])
            for index in stock.run_indices]


# --------------------------------------------------------------------------------------
# Campaign artifacts
# --------------------------------------------------------------------------------------


RUN_MANIFEST_NAME = re.compile(
    r"^(?P<cfg>k[1-5])(?:_(?P<mode>diff|full))?_(?P<sha>[0-9a-f]{40})(?:_(?P<rep>r\d+))?$")


@dataclass
class Invocation:
    """ONE invocation, read from ITS hashed run manifest -- the source of T7.

    Every field below stands in `data/campaign/manifests/<name>.json`, and that file is
    attested by the block `SHA256SUMS`. `valid_final` is not a manifest field; it is
    DERIVED here from the three call counters and named as derived wherever it is printed.
    """
    manifest: str
    config: str
    injection_id: str
    attempt: int
    repetition: str | None
    repo_sha: str | None
    verdict: str
    reasons: list[str]
    invalid_reasons: list[str]
    calls_total: int
    calls_invalid: int
    calls_transport_failed: int
    changed_files_count: int | None
    wall_clock_ms: int
    not_performed: bool
    detail: dict[str, Any]

    @property
    def calls_measured(self) -> int:
        """`outcome: measured` -- the transport failures stand BESIDE it, never inside
        it (skeleton T7.1)."""
        return self.calls_total - self.calls_transport_failed

    @property
    def valid_final(self) -> int:
        return self.calls_measured - self.calls_invalid

    @property
    def is_valid(self) -> bool:
        return self.verdict == "VALID"


@dataclass
class RunStock:
    """Every invocation of the campaign, per configuration. T7 is computed from THIS."""
    invocations: list[Invocation]

    def of(self, config: str) -> list[Invocation]:
        return [i for i in self.invocations if i.config == config]

    def seen(self, config: str) -> set[str]:
        return {i.injection_id for i in self.of(config)}

    def valid(self, config: str) -> set[str]:
        return {i.injection_id for i in self.of(config) if i.is_valid}

    def missing(self, config: str) -> list[str]:
        return sorted(self.seen(config) - self.valid(config))

    def totals(self, config: str) -> dict[str, Any]:
        rows = self.of(config)
        measured = sum(i.calls_measured for i in rows)
        invalid_reasons: dict[str, int] = {}
        for row in rows:
            for reason in row.invalid_reasons:
                invalid_reasons[reason] = invalid_reasons.get(reason, 0) + 1
        # `skipped_count` is no manifest field of its own: the checker reports skipped
        # files as the `invalid_reasons` value `skipped_files` (reporter.ts:59-64). Counted
        # from there, and named as derived from there wherever it is printed.
        skipped = sum(1 for row in rows
                      for reason in row.invalid_reasons if "skipped" in reason)
        return {
            "invocations": len(rows),
            "valid": sum(1 for i in rows if i.is_valid),
            "invalid": sum(1 for i in rows if not i.is_valid),
            "injections_seen": len(self.seen(config)),
            "injections_valid": len(self.valid(config)),
            "missing": self.missing(config),
            "calls_total": sum(i.calls_total for i in rows),
            "calls_invalid": sum(i.calls_invalid for i in rows),
            "calls_transport_failed": sum(i.calls_transport_failed for i in rows),
            "calls_measured": measured,
            "valid_final": sum(i.valid_final for i in rows),
            "valid_final_share": (sum(i.valid_final for i in rows) / measured
                                  if measured else None),
            "skipped_count": skipped,
            "invalid_reasons": dict(sorted(invalid_reasons.items())),
            "repetitions": sum(1 for i in rows if i.repetition),
            "wall_clock_ms": sum(i.wall_clock_ms for i in rows),
            "not_performed": sum(1 for i in rows if i.not_performed),
        }

    def outer_clock(self, config: str) -> list[int]:
        """`external_wall_clock_ms` per invocation — the OUTER clock, measured by the
        campaign runner around the subprocess. The only clock that is comparable across
        all five configurations (T6 footnote (a))."""
        return [i.wall_clock_ms for i in self.of(config)]

    def inner_clock(self, config: str) -> list[int]:
        """`run_footer.wall_clock_ms`, carried into the run manifest as
        `postrun.detail.wall_clock_ms_inner`. K4 and K5 have no `run_footer` at all —
        they are external tools without the checker log format; the list is empty and
        the cell carries `n. b.` (T6 footnote (a))."""
        return [i.detail["wall_clock_ms_inner"] for i in self.of(config)
                if i.detail.get("wall_clock_ms_inner") is not None]


def load_run_manifests(campaign: Path) -> RunStock:
    """Read every run manifest under `campaign/manifests/`. THE source of T7.

    The manifests are hashed (block `SHA256SUMS`); `journal.jsonl` and the prose manifests
    are not. A manifest whose file name does not parse is a finding, not something to skip
    quietly -- an unreadable name would silently shrink the invocation count.
    """
    directory = campaign / "manifests"
    invocations: list[Invocation] = []
    for path in sorted(directory.glob("*.json")):
        match = RUN_MANIFEST_NAME.match(path.stem)
        if match is None:
            raise SystemExit(f"Laufmanifest mit unlesbarem Namen: {path}")
        doc = load_json(path)
        if doc.get("is_smoke_test"):
            continue
        postrun = doc.get("postrun") or {}
        detail = postrun.get("detail") or {}
        invocations.append(Invocation(
            manifest=path.name,
            config=doc["run"]["config"],
            injection_id=doc["run"]["injection_id"],
            attempt=doc.get("attempt"),
            repetition=match.group("rep"),
            repo_sha=doc.get("target_repo_git_head") or (doc.get("run") or {}).get("sha"),
            verdict=postrun.get("verdict"),
            reasons=list(postrun.get("reasons") or []),
            invalid_reasons=[str(r) for r in (detail.get("invalid_reasons") or [])],
            calls_total=detail.get("calls_total") or 0,
            calls_invalid=detail.get("calls_invalid") or 0,
            calls_transport_failed=detail.get("calls_transport_failed") or 0,
            changed_files_count=detail.get("changed_files_count"),
            wall_clock_ms=doc.get("external_wall_clock_ms") or 0,
            not_performed=bool(doc.get("not_performed")),
            detail=detail,
        ))
    if not invocations:
        raise SystemExit(f"kein Laufmanifest unter {directory}")
    return RunStock(invocations=invocations)


@dataclass
class Journal:
    """`journal.jsonl` -- the CROSS-CHECK against the run manifests, not the source."""
    valid: dict[str, set[str]]
    seen: dict[str, set[str]]
    invalid_rows: list[dict[str, Any]]
    rows: list[dict[str, Any]]

    def missing(self, config: str) -> list[str]:
        return sorted(self.seen.get(config, set()) - self.valid.get(config, set()))


def journal_crosscheck(stock: RunStock, journal: Journal) -> dict[str, dict[str, Any]]:
    """T7.1 cross-check: does the append-only journal say what the manifests say?

    Compared per configuration: number of invocations, number of VALID ones and the list
    of injections without a valid run. A divergence means an attested artifact and a
    record contradict each other. It is REPORTED -- neither side is adapted to the other
    (order C6c-a; skeleton T7.3 building rule).
    """
    out: dict[str, dict[str, Any]] = {}
    for config in CONFIGS:
        totals = stock.totals(config)
        journal_valid = sorted(journal.valid.get(config, set()))
        journal_seen = journal.seen.get(config, set())
        rows = [r for r in journal.rows if r["config"] == config]
        divergences = []
        if len(rows) != totals["invocations"]:
            divergences.append(f"Invocationen Manifeste {totals['invocations']} "
                               f"gegen Journal {len(rows)}")
        if len(journal_valid) != totals["injections_valid"]:
            divergences.append(f"gültige Injektionen Manifeste "
                               f"{totals['injections_valid']} gegen Journal "
                               f"{len(journal_valid)}")
        if journal.missing(config) != totals["missing"]:
            divergences.append(f"n. e.-Liste Manifeste {totals['missing']} gegen Journal "
                               f"{journal.missing(config)}")
        if sorted(journal_seen) != sorted(stock.seen(config)):
            divergences.append("Injektionsmenge weicht ab")
        out[config] = {"journal_invocations": len(rows),
                       "journal_valid": len(journal_valid),
                       "journal_missing": journal.missing(config),
                       "divergences": divergences}
    return out


def acceptance_rules(stock: RunStock) -> list[dict[str, Any]]:
    """T7.2 — the POSITIVE run-acceptance rules, out of the run manifests.

    K4 and K5 write no run log; without a positive statement about the run, a
    misconfiguration that shortens the rule set is INVISIBLE -- it produces zero findings
    without an error message (protocol §9, T12 addendum rev. 32). These rows attest that
    the rule set was read in full breadth; about HIT COUNTS they say nothing.

    The `Erwartet` column carries the skeleton's pre-registered wording verbatim. Where
    the executed rule (`tools/postrun_check.py`, the sole executor per §6 addendum rev. 24)
    reads differently, that is printed as a divergence, not silently harmonised.
    """
    rows: list[dict[str, Any]] = []

    injection = [i for i in stock.invocations if i.config in ("K1", "K2", "K3")]
    with_cfc = [i for i in injection if i.changed_files_count is not None]
    ok_cfc = [i for i in with_cfc if i.changed_files_count == 1]
    rows.append({
        "scope": "K1/K2/K3, Injektionslauf",
        "rule": "`changed_files_count == 1`",
        "expected": "1 je Invocation",
        "measured": f"1 in {len(ok_cfc)} von {len(with_cfc)} Invocationen",
        "met": len(ok_cfc) == len(with_cfc) and len(with_cfc) == len(injection),
        "note": "",
    })

    # The executed rule: K2/K3 expect 1 * runs, K1 expects 0 -- the deterministic path
    # makes no model call at all (`postrun_check.py`, injection branch).
    per_config = {c: sorted({i.calls_total for i in stock.of(c)}) for c in ("K1", "K2", "K3")}
    measured = " · ".join(f"{c}: {', '.join(str(v) for v in per_config[c])}"
                          for c in ("K1", "K2", "K3"))
    executed_ok = (per_config["K1"] == [0] and per_config["K2"] == [3]
                   and per_config["K3"] == [3])
    rows.append({
        "scope": "K1/K2/K3, Injektionslauf",
        "rule": "`calls_total == 1 × runs`",
        "expected": "K1: 1 · K2/K3: 3",
        "measured": measured,
        "met": executed_ok,
        "note": ("**Abweichung zum Skelettwortlaut bei K1:** der ausgeführte Akzeptanztest "
                 "verlangt für K1 `calls_total == 0` (deterministischer Pfad, kein Modell) "
                 "— `tools/postrun_check.py`, §6 Nachtrag Rev. 24/26. Gemessen ist 0. "
                 "Beide Fassungen stehen hier nebeneinander; angeglichen wird keine."),
    })

    k4 = stock.of("K4")
    ok4 = [i for i in k4
           if (i.detail.get("kept") or 0) + (i.detail.get("broken") or 0)
           == i.detail.get("expected_contracts")]
    rows.append({
        "scope": "K4",
        "rule": "ausgewertete Contracts `kept + broken`",
        "expected": "13",
        "measured": f"{len(ok4)} von {len(k4)} Aufrufen mit `kept + broken` = "
                    + ", ".join(str(v) for v in sorted(
                        {(i.detail.get('kept') or 0) + (i.detail.get('broken') or 0)
                         for i in k4})),
        "met": None,      # the skeleton pre-registers `n. b.` in this cell
        "note": "`erfüllt` ist im Skelett als `n. b.` vorregistriert — die Trefferzahl "
                "ist die Messung, geprüft ist allein die Vollständigkeit der Regelmenge.",
    })

    k5 = stock.of("K5")
    ok5 = [i for i in k5 if i.detail.get("collected") == i.detail.get("expected_collected")]
    rows.append({
        "scope": "K5",
        "rule": "gesammelte Tests, Sammelphase fehlerfrei",
        "expected": "24",
        "measured": f"{len(ok5)} von {len(k5)} Aufrufen mit `collected` = "
                    + ", ".join(str(v) for v in sorted(
                        {i.detail.get("collected") for i in k5})),
        "met": len(ok5) == len(k5) and bool(k5),
        "note": "",
    })
    return rows


def load_journal(campaign: Path) -> Journal:
    valid: dict[str, set[str]] = {}
    seen: dict[str, set[str]] = {}
    invalid_rows = []
    rows = [r for r in load_jsonl(campaign / "journal.jsonl") if not r.get("is_smoke_test")]
    for row in rows:
        config = row["config"]
        seen.setdefault(config, set()).add(row["injection_id"])
        if row.get("verdict") == "VALID":
            valid.setdefault(config, set()).add(row["injection_id"])
        else:
            invalid_rows.append(row)
    return Journal(valid=valid, seen=seen, invalid_rows=invalid_rows, rows=rows)


def manifest_missing(campaign: Path) -> dict[str, list[str]]:
    """SECOND cross-check for T7.3: the same list read out of the PROSE manifests.

    Source of T7.3 is `load_run_manifests` (C6c-a, protocol rev. 39); this function and
    `journal_crosscheck` are the two counter-readings. The building rule names BOTH prose
    sources — `data/campaign/MANIFEST.md` AND the block manifest
    `data/campaign/k3/MANIFEST.md` (skeleton T7.3). Reading only the block manifests
    misses a campaign whose overall manifest carries the list; both are read and merged
    per configuration. If a prose manifest and the run manifests disagree, that is a
    finding and is reported, not silently resolved.
    """
    out: dict[str, list[str]] = {}

    def harvest(text: str, default_config: str | None) -> None:
        for line in text.splitlines():
            if "ohne" not in line or "gültigen Lauf" not in line:
                continue
            ids = sorted(set(re.findall(r"\bI\d{2}\b", line)))
            if not ids:
                continue
            named = sorted(set(re.findall(r"\bK[1-5]\b", line)))
            for config in (named or ([default_config] if default_config else [])):
                out.setdefault(config, [])
                out[config] = sorted(set(out[config]) | set(ids))

    overall = campaign / "MANIFEST.md"
    if overall.is_file():
        harvest(read_text(overall), None)
    for block in ("k1", "k2", "k3", "k4", "k5"):
        path = campaign / block / "MANIFEST.md"
        if path.is_file():
            harvest(read_text(path), block.upper())
            out.setdefault(block.upper(), [])
    return out


def call_costs(campaign: Path, config: str) -> dict[str, list[int]]:
    """Tokens and latency PER CHECK, read from the campaign run logs.

    One `llm_call` record is one check — one file prompt (protocol §5, Entscheidung I).
    The fields are `tokens_in_total`, `tokens_out_total` and `latency_ms_total`; `usage`
    is null throughout the measured logs, which is why the counts come from these three
    (run manifest note `token_budget.note`).

    Only ever called WITH `--with-campaign`: run logs carry findings and are barred by
    the blindness obligation otherwise.
    """
    tokens_in: list[int] = []
    tokens_out: list[int] = []
    latency: list[int] = []
    for path in sorted((campaign / config.lower()).glob("*.jsonl")):
        for record in load_jsonl(path):
            if record.get("record_type") != "llm_call":
                continue
            tokens_in.append(record.get("tokens_in_total") or 0)
            tokens_out.append(record.get("tokens_out_total") or 0)
            latency.append(record.get("latency_ms_total") or 0)
    return {"tokens_in": tokens_in, "tokens_out": tokens_out, "latency_ms": latency}


BLOCKS = ("k1", "k2", "k3", "k4", "k5")


def campaign_artifact(campaign: Path, config: str, entry: dict[str, Any],
                      suffix: str, stock: "RunStock") -> Path | None:
    """R11 — resolve the artifact of ONE pair (configuration, injection) FROM THE RUN
    MANIFEST (spec §1.9, protocol rev. 44).

    Read is the artifact whose HASHED run manifest carries `postrun.verdict == VALID`; of
    several valid attempts the EARLIEST (smallest `attempt`). Where none is valid, nothing
    is opened and the cell is `n. e.` out of T7.3 -- the same source `cell_for` already
    used for the marker, so marker and reading now stand on ONE decision.

    NOT the file name and NOT the number of records: both are silent about whether the run
    was valid. The rule this replaces was the glob `<cfg>_*<injection_sha256>.json`, which
    matches the file WITHOUT the `_r<n>` suffix -- the FIRST attempt. For eleven K3
    injections that artifact carries the verdict INVALID with reason `transport_failure`
    (C11d §A6b), and its findings went into the tables of the first three evaluation runs
    while T7 printed the invalidity correctly one table above. §7 of the protocol excludes
    exactly that: "stille Zählung invalider Läufe als '0 Findings' ist damit ausgeschlossen".

    The injection sha stays in play, but as a CHECK rather than as the selector: the
    manifest of the chosen attempt must name the same commit as the injection manifest.
    """
    block = campaign / config.lower()
    if not block.is_dir():
        return None
    valid = [i for i in stock.of(config)
             if i.injection_id == entry["id"] and i.is_valid]
    if not valid:
        return None
    chosen = min(valid, key=lambda i: (i.attempt if i.attempt is not None else 0,
                                       i.manifest))
    named = chosen.repo_sha
    if named and named != entry["injection_sha256"]:
        raise SystemExit(
            f"HARNESS-FEHLER: Laufmanifest {chosen.manifest} steht auf Commit {named}, "
            f"das Injektionsmanifest nennt für {entry['id']} {entry['injection_sha256']}")
    path = block / (Path(chosen.manifest).stem + suffix)
    if not path.is_file():
        raise SystemExit(
            f"HARNESS-FEHLER: {chosen.config}/{chosen.injection_id} hat einen gültigen "
            f"Lauf ({chosen.manifest}), das zugehörige Artefakt {path} fehlt")
    return path


def invalid_artifacts_read(campaign: Path, stock: RunStock) -> list[str]:
    """R12 — no finding may come out of a run whose manifest declares it invalid.

    Exit 2. The assertion is formulated INDEPENDENTLY of the selector: it asks the files
    that were actually OPENED, not a bookkeeping list the selector keeps. A return to a
    name-based rule would therefore show up here instead of working silently -- which is
    why this guard carries further than the repair it guards.

    Deliberately NOT covered, and named as such: the run logs `*.jsonl` of K2/K3. T6 reads
    them over ALL invocations, valid or not -- the run cost was incurred either way -- and
    they carry no cell of any hit computation.
    """
    verdicts = {Path(i.manifest).stem: i for i in stock.invocations}
    root = campaign.resolve()
    out = []
    for path in READS:
        if path.parent.parent != root or path.parent.name not in BLOCKS:
            continue
        name = path.name
        if name.endswith(".stdout.txt"):
            stem = name[:-len(".stdout.txt")]
        elif name.endswith(".json"):
            stem = name[:-len(".json")]
        else:
            continue                     # run log -- T6 reads it over all invocations
        invocation = verdicts.get(stem)
        if invocation is None:
            out.append(f"{path.parent.name}/{name} — kein Laufmanifest gleichen Namens")
        elif not invocation.is_valid:
            reasons = ", ".join(invocation.invalid_reasons) or "ohne genannten Grund"
            out.append(f"{path.parent.name}/{name} — Laufmanifest trägt Verdikt "
                       f"{invocation.verdict} ({reasons}), Paar {invocation.config}/"
                       f"{invocation.injection_id}, Versuch {invocation.attempt}")
    return sorted(set(out))


@dataclass
class InjectionResult:
    strict: Cell
    localized: Cell
    campaign_counts: list[int] | None
    strict_fp: int
    sv: bool | None
    co_findings: list[dict[str, Any]]
    special: list[dict[str, Any]]
    #: false positives of the `localized` metric: DEDUPLICATED triples that are neither
    #: the expected one nor a pre-registered special class (spec §4, §7.3).
    localized_fp: int = 0
    #: findings carrying a pre-registered T9 special class -- neither hit nor FP, caught
    #: BEFORE the general FP/FN rule (spec §5 closing paragraph, T5 auflage (4)).
    preregistered: list[dict[str, Any]] = field(default_factory=list)
    #: `localized` is a hit ON THE PLACE ONLY -- the pre-registered class "right place,
    #: wrong category". Carries the T1 verdict "teilweise" (footnote 7, protocol rev. 22).
    place_only: bool = False


def evaluate_llm_injection(doc: dict[str, Any], entry: dict[str, Any],
                           config: str) -> InjectionResult:
    """`strict` and `localized` for one injection on the LLM path (K2/K3) or on K1."""
    path = "K1" if config == "K1" else "K2_K3"
    expected_key = (entry.get("expected_match_key") or {}).get(path)
    want_category = expected_category(entry, "K1" if config == "K1" else "LLM")
    module, component = entry["carrier_module"], entry["carrier_component"]
    co_keys = {c.get("match_key") for c in (entry.get("expected_co_findings") or [])
               if c.get("match_key")}

    strict_hit = False
    strict_fp = 0
    localized_seen: set[tuple[str, str, str]] = set()
    localized_other: set[tuple[str, str, str]] = set()
    localized_hit = False
    place_only_seen = False
    counts: list[int] = []
    co_found: list[dict[str, Any]] = []
    special: list[dict[str, Any]] = []
    preregistered: list[dict[str, Any]] = []
    sv = False

    for run in doc["runs"]:
        derived, llm = split_by_mechanism(run["findings"])
        mine = derived if config == "K1" else llm
        # The counting quantity of spec §7.5 (3): findings of the SAME module in the SAME
        # category. The category is PATH-DEPENDENT (spec §4) -- the rule engine writes
        # `layer-violation`/`cycle`, never a level-1 name -- so the same `want_category`
        # the localized triple uses. Filtering on `category_l1` made every K1 count 0.
        counts.append(len([f for f in mine
                           if f.get("module") == module
                           and f.get("category") == want_category]))
        run_hit = False       # §3.2 is a PER-RUN rule: one TP per run, every further
                              # record of that run an FP. A correct hit repeated in the
                              # next run is reproducibility, not a false positive.
        for f in mine:
            key = f.get("match_key") or ""
            if key in co_keys:
                # pre-registered co-finding — neither hit nor FP (spec §5, T9 case 1)
                co_found.append({"injection": entry["id"], "config": config,
                                 "match_key": key, "run_index": run["run_index"]})
                continue
            triple = (f.get("component"), f.get("module"), f.get("category"))
            case6 = is_case_6(entry, config, f, module)
            if case6:
                # T9 case 6 — pre-registered special class. Caught BEFORE the general
                # FP/FN rule (spec §5 closing paragraph, T5 auflage (4)): neither hit
                # nor FP, and it must not be counted twice.
                preregistered.append({"injection": entry["id"], "config": config,
                                      "special_class": "T9-6", "category": f.get("category"),
                                      "run_index": run["run_index"], "match_key": key})
                place_only_seen = True
                continue
            if expected_key is not None and key == expected_key:
                if run_hit:
                    strict_fp += 1     # §3.2: one TP per run, every further record an FP
                run_hit = True
                strict_hit = True
            else:
                if expected_key is not None:
                    strict_fp += 1
                # mechanically formed writing-variant flag (§3.4 (1), §8 point 8)
                if expected_key and key:
                    a, b = segments(expected_key), segments(key)
                    if len(a) == 4 and len(b) == 4 and a[:3] == b[:3] and a[3] != b[3]:
                        sv = True
            if triple == (component, module, want_category):
                if triple not in localized_seen:      # dedup ONLY in localized (§7.3)
                    localized_seen.add(triple)
                localized_hit = True
            else:
                # every other triple is a `localized` false positive -- deduplicated on
                # (component, module, category), never counted per record (§7.3)
                localized_other.add(triple)
                if f.get("module") == module:
                    # right place, wrong category, NOT one of the pre-registered classes
                    # -> the general rule: FP *and* FN (protocol §4 main rule, spec §5)
                    special.append({"injection": entry["id"], "config": config,
                                    "category": f.get("category"),
                                    "run_index": run["run_index"], "match_key": key})

    return InjectionResult(
        strict=valued(1 if strict_hit else 0),
        localized=valued(1 if localized_hit else 0),
        campaign_counts=counts, strict_fp=strict_fp,
        sv=(sv and localized_hit and not strict_hit),
        co_findings=co_found, special=special,
        localized_fp=len(localized_other), preregistered=preregistered,
        place_only=place_only_seen and not localized_hit)


def is_case_6(entry: dict[str, Any], config: str, finding: dict[str, Any],
              module: str) -> bool:
    """T9 case 6, exactly as pre-registered and no wider.

    Spec §5 case 6: "`CYCLE`-Injektionen: K2/K3 melden `FORBIDDEN_RELATION` am richtigen
    Modul". All four conditions are named there and all four are required. A record at
    the carrier module carrying some OTHER category is NOT this class -- it falls under
    the general rule (FP *and* FN). Widening the class to "any wrong category" would
    remove false positives the pre-registration never removed, and that is precisely the
    ad-hoc rule in favour of the own tool that the skeleton's T9 note forbids.
    """
    return (config in LLM_CONFIGS
            and entry["category_l1"] == "CYCLE"
            and finding.get("module") == module
            and finding.get("category") == "FORBIDDEN_RELATION")


def evaluate_k4k5_injection(text: str, entry: dict[str, Any], config: str,
                            topology: dict[str, str]) -> InjectionResult:
    """K4/K5 have no match_key — the comparison rules live in tools/match_k4k5.py
    (spec §6.1 mengenregel for K4/CYCLE, §6.2 for K5). Imported, not reimplemented.

    The booking asks the parser's OWN vocabulary — `strict_eligible`, the named set
    `match_k4k5.LOCALIZED_HIT`, the named `special_class`. It never compares against a
    literal: C11a traced the loss of the four K5/CYCLE findings in the first evaluation
    run to exactly such a comparison (`localized == "treffer"` against the value
    `treffer (richtige Stelle, falsche Kategorie)`), and a literal patched at that one
    place would repeat itself at the next class the parser learns to tell apart.
    """
    result = match_k4k5.match(text, config, entry, topology)
    findings = result["findings"]

    # `strict_eligible is True` is the parser's own statement that this finding may
    # constitute a strict hit -- narrower than `classification == "treffer"`, because
    # K4/INCORRECT_LOCATION is a hit that is expressly NOT strict-eligible (footnote 5).
    strict_hit = any(f.get("strict_eligible") is True for f in findings)

    # `localized` books a hit ON THE PLACE. The pre-registered class "right place, wrong
    # category" is one -- footnote 7 / protocol rev. 22 word it as "In localized: Treffer
    # auf der Stelle", and it is that booking which moves the T1 cell from "nein" to
    # "teilweise". Whether the category was met as well is a SEPARATE statement, carried
    # in `place_only` and used by T1 and T5.
    full_hit = any(f.get("localized") == match_k4k5.LOC_TREFFER for f in findings)
    localized_hit = any(f.get("localized") in match_k4k5.LOCALIZED_HIT for f in findings)

    preregistered = [{"injection": entry["id"], "config": config,
                      "special_class": f["special_class"], "form": f["form"],
                      "reason": f["reason"]}
                     for f in findings if f.get("special_class")]
    co = [{"injection": entry["id"], "config": config, "form": f["form"],
           "reason": f["reason"]}
          for f in findings if f["classification"] == match_k4k5.BEGLEIT]
    # `sonstiger_fund` is the parser saying: a finding of the right OUTPUT FORM that does
    # not match this manifest entry. That is a false positive for both metrics. A tool
    # abort (`werkzeugabbruch`) and an unevaluated rule (`regel_nicht_ausgewertet`) are
    # NEITHER -- they carry no statement at all (T5 auflage (5), spec §6.2).
    special = [{"injection": entry["id"], "config": config, "form": f["form"],
                "reason": f["reason"]}
               for f in findings if f["classification"] == match_k4k5.SONSTIG]
    return InjectionResult(strict=valued(1 if strict_hit else 0),
                           localized=valued(1 if localized_hit else 0),
                           campaign_counts=k4k5_campaign_count(result, entry),
                           strict_fp=len(special), sv=None,
                           co_findings=co, special=special,
                           localized_fp=len(special), preregistered=preregistered,
                           place_only=is_place_only(result, localized_hit, full_hit))


def is_place_only(result: dict[str, Any], localized_hit: bool, full_hit: bool) -> bool:
    """Is this a PARTIAL detection — the tool reaches the place, never the category?

    Two ways it arises, both pre-registered, both read off the parser's own cell rule:

    * the finding itself carries the verdict "richtige Stelle, falsche Kategorie"
      (`LOC_STELLE`, T9 case 6/7);
    * the CELL is pre-registered as one that can never produce a strict hit
      (`strict: "nie"`) — footnote 5 for K4/`INCORRECT_LOCATION`, footnote 7 for the two
      K5/`CYCLE` cells. import-linter finds the moved module NAMENSBLIND, as an
      undeclared child, not as a misplacement: the place is reached, the kind is not.

    Those three cells are exactly the three `teilweise` cells of T1 — the parser's
    `strict: "nie"` and the matrix verdict `teilweise` are the same statement, so reading
    one off the other invents nothing.
    """
    rule = result.get("cell_rule") or {}
    never_strict = rule.get("strict") == "nie"
    return localized_hit and (not full_hit or never_strict)


def k4k5_campaign_count(result: dict[str, Any],
                        entry: dict[str, Any]) -> list[int] | None:
    """T4 campaign side for K4/K5 — the SAME counting quantity as on the LLM path:
    findings of the same module in the same category (spec §7.5 (3)/(4)). One run.

    Returns None where the quantity is NOT FORMABLE, i.e. where the cell rule itself
    says the output form carries no module (`n. b.`, A-17 / protocol §4 rev. 30). That
    is the case the marker was made for; a 0 there would claim a measurement that did
    not take place.
    """
    rule = result.get("cell_rule")
    if rule and rule.get("localized") == match_k4k5.LOC_NB:
        return None
    module, category = entry["carrier_module"], entry["category_l1"]
    count = 0
    for finding in result["findings"]:
        parts = finding.get("parts") or {}
        named = parts.get("source_module") or parts.get("module")
        if named == module and finding.get("category_l1") == category:
            count += 1
    return [count]


# --------------------------------------------------------------------------------------
# Cell assembly with marker discipline
# --------------------------------------------------------------------------------------


def cell_for(config: str, scenario: str, metric: str, injection_id: str,
             stock: RunStock, computed: Cell | None) -> Cell:
    """Decide ONE cell. The order of the tests is the marker discipline itself:

    1. " — "  pre-registered from T1/T8 — wins over everything, including over a run that
              produced zero findings. NEVER derived from missing data.
    2. "n. b." pre-registered: the metric is not formable from the output form (A-17).
    3. "n. e." derived from T7: no valid run for this injection, read from the HASHED run
              manifests (C6c-a) — not from the journal and not from a prose manifest.
    4. value   computed.
    """
    if (config, scenario, metric) in NB_CELLS:
        return marked(NB, "Ausgabeform trägt kein Modul", "Protokoll §4 Nachtrag Rev. 30 (A-17)")
    if (config, scenario) in DASH_CELLS:
        return marked(DASH, "Kategorie von dieser Konfiguration nicht ausdrückbar", "T1/T8")
    if injection_id not in stock.valid(config):
        return marked(NE, "kein gültiger Lauf", "T7.3")
    if computed is None:
        return blank("in diesem Lauf nicht ausgewertet")
    return computed


# --------------------------------------------------------------------------------------
# R1 — no marker-free empty cell, checked on the RENDERED output
# --------------------------------------------------------------------------------------

# The exemption list, EXPLICIT and short. An empty cell is allowed ONLY here, and only
# because the emptiness itself carries a meaning that is stated at the column. Everything
# else that is empty is a failure -- stated positively on purpose, so that a new empty
# cell is a violation by default rather than by oversight (same construction as the
# blindness allow-list).
EMPTY_CELL_ALLOWED: set[tuple[str, str]] = {
    # T1: "computed, no deviation" -- the note stands at the column
    ("T1", "Abweichung"),
    # T9 row 2 is a NULL EXPECTATION: there is no place of finding to name, and naming
    # one would assert a finding that must not exist.
    ("T9", "Betroffen"),
}


def table_empty_cells(markdown: str) -> list[str]:
    """Every data cell of every table that is EMPTY and carries no marker.

    Checked on the FINISHED text, not on the cell objects. That is the point: the first
    evaluation run lost computed values on the way into the table -- `len(hits) or ''`
    turns a computed 0 into an empty string without ever touching a Cell -- and a check
    at the cell object would not have seen it (C11a question 2, §4).

    An empty cell is indistinguishable from the skeleton marker *(leer)* "not inserted by
    this run". Where that marker legitimately applies -- a run WITHOUT `--with-campaign`
    -- this check does not run at all; the caller decides.
    """
    table, header, problems = None, None, []
    for number, line in enumerate(markdown.splitlines(), start=1):
        stripped = line.strip()
        if stripped.startswith("## T"):
            table = stripped[3:].split(" ")[0].strip()
            header = None
            continue
        if not stripped.startswith("|"):
            if stripped and not stripped.startswith(">"):
                header = None       # a paragraph ends the table
            continue
        cells = [c.strip() for c in stripped.strip("|").split("|")]
        if header is None:
            header = cells
            continue
        if all(set(c) <= set("-: ") for c in cells):
            continue                # the separator row
        for index, cell in enumerate(cells):
            if cell:
                continue
            column = header[index] if index < len(header) else f"Spalte {index + 1}"
            if (table, column) in EMPTY_CELL_ALLOWED:
                continue
            problems.append(
                f"{table or '?'} Zeile {number} ({cells[0] or '?'}), Spalte {column!r}: "
                "leere Zelle ohne Marker")
    return problems


# --------------------------------------------------------------------------------------
# R10 — no bare marker, no exponent notation, checked on the RENDERED output
# --------------------------------------------------------------------------------------

#: `%g` prints `9.19054e+06` above six significant digits. The pattern matches that form
#: and nothing else -- a SHA256 carries no decimal point, a version number no `e+`.
EXPONENT = re.compile(r"\d(?:\.\d+)?[eE][+-]\d+")

#: what may sit next to a marker in the SAME cell and still leave it a marker cell: the
#: footnote superscripts the skeleton sets (T5 footnote (a), T6 footnote (a)).
FOOTNOTE_MARKS = "ᵃᵇᶜᵈᵉ"


def table_render_defects(markdown: str) -> list[str]:
    """R10 — two rendering defects, checked on the FINISHED text like R1.

    **(a) No marker without code markup.** A cell that IS a marker must print it in
    backticks, in EVERY table. Without the markup a marker is not distinguishable from
    prose, and the three markers carry three different statements that chapter 8 reads
    differently (skeleton §1.1). `Score.cells()` returned the raw marker string while
    every other table went through `Cell.text`, so 72 T5 cells and the T3 findingwise
    headline printed the same marker in a second, unmarked form (C11b §7 (1), C11c D1/D3).

    Only a cell that is a marker AND NOTHING ELSE is asked: an em dash inside a sentence
    is punctuation, not a marker, and T9's booking rules are full of them.

    **(b) No number in exponent notation.** `9.19054e+06 ms` next to `252155 ms` in the
    same column is the same quantity in two notations (C11b §7 (2), C11c D2). Checked over
    the whole rendered text, not only inside tables.

    Neither check touches a computing rule, a filter, a denominator or an aggregation
    stage — both look at NOTATION, on text that is already final.
    """
    problems: list[str] = []

    for number, line in enumerate(markdown.splitlines(), start=1):
        for hit in EXPONENT.findall(line):
            problems.append(f"Zeile {number}: Zahl in Exponentialform {hit!r}")

    table, header = None, None
    for number, line in enumerate(markdown.splitlines(), start=1):
        stripped = line.strip()
        if stripped.startswith("## T"):
            table = stripped[3:].split(" ")[0].strip()
            header = None
            continue
        if not stripped.startswith("|"):
            if stripped and not stripped.startswith(">"):
                header = None
            continue
        cells = [c.strip() for c in stripped.strip("|").split("|")]
        if header is None:
            header = cells
            continue
        if all(set(c) <= set("-: ") for c in cells):
            continue
        for index, cell in enumerate(cells):
            bare = cell.strip("*").strip().rstrip(FOOTNOTE_MARKS).strip()
            if bare not in (DASH.strip(), NB, NE):
                continue                      # not a marker cell — nothing to ask
            if "`" in cell:
                continue                      # marked up, as it must be
            column = header[index] if index < len(header) else f"Spalte {index + 1}"
            problems.append(
                f"{table or '?'} Zeile {number} ({cells[0] or '?'}), Spalte {column!r}: "
                f"Marker {bare!r} ohne Code-Auszeichnung")
    return problems


def assert_marker_discipline(cells: Iterable[tuple[str, Cell]]) -> list[str]:
    """A cell may never carry 0 where a marker holds. Enforced, not left to care."""
    problems = []
    for label, cell in cells:
        if cell.marker is not None and cell.value is not None:
            problems.append(f"{label}: Marker {cell.marker!r} und Wert {cell.value!r}")
        if cell.marker == DASH and cell.value == 0:
            problems.append(f"{label}: ' — ' als 0 gebucht")
    return problems


# --------------------------------------------------------------------------------------
# Evaluation
# --------------------------------------------------------------------------------------


@dataclass
class Paths:
    soll: Path
    control_k2: Path
    control_k3: Path
    campaign: Path


def evaluate(paths: Paths, with_campaign: bool) -> dict[str, Any]:
    manifest_doc = load_json(paths.soll / "injection_manifest.json")
    entries = {e["id"]: e for e in manifest_doc["injections"]}
    completeness = manifest_doc.get("completeness_check", {})

    control = {
        "K2": load_control(paths.control_k2, paths.soll / "control_files.txt", "K2"),
        "K3": load_control(paths.control_k3, paths.soll / "control_files.txt", "K3"),
    }
    fp = {cfg: false_positive_rates(stock) for cfg, stock in control.items()}
    prereg = {cfg: preregistered_rows(stock) for cfg, stock in control.items()}
    rules = {cfg: rule_id_distribution(stock) for cfg, stock in control.items()}
    reference = {
        "K2": reference_classes(paths.control_k2, sum(fp["K2"]["findingwise"])),
        "K3": reference_classes(paths.control_k3, sum(fp["K3"]["findingwise"])),
    }

    # SOURCE of T7: the hashed run manifests. Journal and prose manifests follow only as
    # cross-checks (C6c-a, protocol rev. 39).
    stock = load_run_manifests(paths.campaign)
    journal = load_journal(paths.campaign)
    manifest_ne = manifest_missing(paths.campaign)
    crosscheck = journal_crosscheck(stock, journal)

    topology = match_k4k5.load_topology()

    injections: dict[str, dict[str, Any]] = {}
    co_findings: list[dict[str, Any]] = []
    specials: list[dict[str, Any]] = []
    preregistered: list[dict[str, Any]] = []

    for iid, entry in entries.items():
        scenario = entry["scenario_l2"]
        row: dict[str, Any] = {"id": iid, "scenario_l2": scenario,
                               "category_l1": entry["category_l1"],
                               "carrier_module": entry["carrier_module"],
                               "configs": {}}
        for config in CONFIGS:
            computed_strict = computed_loc = None
            counts = None
            strict_fp = loc_fp = 0
            sv = None
            place_only = False
            prereg_here: list[dict[str, Any]] = []
            if with_campaign:
                if config in ("K1", "K2", "K3"):
                    doc_path = campaign_artifact(paths.campaign, config, entry, ".json",
                                                 stock)
                    if doc_path is not None:
                        result = evaluate_llm_injection(load_json(doc_path), entry, config)
                    else:
                        result = None
                else:
                    text_path = campaign_artifact(paths.campaign, config, entry,
                                                  ".stdout.txt", stock)
                    if text_path is not None:
                        result = evaluate_k4k5_injection(
                            read_text(text_path), entry, config, topology)
                    else:
                        result = None
                if result is not None:
                    computed_strict, computed_loc = result.strict, result.localized
                    counts, strict_fp, sv = (result.campaign_counts, result.strict_fp,
                                             result.sv)
                    loc_fp, place_only = result.localized_fp, result.place_only
                    prereg_here = result.preregistered
                    co_findings.extend(result.co_findings)
                    specials.extend(result.special)
                    preregistered.extend(result.preregistered)

            strict_cell = cell_for(config, scenario, "strict", iid, stock, computed_strict)
            loc_cell = cell_for(config, scenario, "localized", iid, stock, computed_loc)

            entry_cfg: dict[str, Any] = {"strict": strict_cell, "localized": loc_cell,
                                         "strict_fp": strict_fp, "localized_fp": loc_fp,
                                         "place_only": place_only,
                                         "preregistered": [p["special_class"]
                                                           for p in prereg_here]}

            # --- T4: resting side, campaign side, difference -------------------------
            # For K2/K3 the resting side is C3b, per run. For K1/K4/K5 it is the
            # clean-state audit constant, carried as a REPORT value and marked as such
            # (appendix A-14) -- that does not change here.
            if config in LLM_CONFIGS:
                rest = control_preload(control[config], entry)
                rest_source = "C3b"
            else:
                rest = None
                rest_source = "C3a (A-14)"

            if with_campaign and iid not in stock.valid(config):
                for key in ("rest", "campaign", "delta", "runs", "sv", "kein_en"):
                    entry_cfg[key] = marked(NE, source="T7.3")
            else:
                if rest is None:
                    entry_cfg["rest"] = valued("0 ᴬ¹⁴", source=rest_source)
                    rest_med = 0.0
                    rest_exists = False
                else:
                    rest_med = median(rest)
                    entry_cfg["rest"] = valued(plain(rest_med), source=rest_source)
                    rest_exists = any(value > 0 for value in rest)

                if counts is None:
                    # not formable: the output form carries no module (A-17). NEVER 0.
                    reason = ("Ausgabeform trägt kein Modul"
                              if with_campaign else "in diesem Lauf nicht ausgewertet")
                    nb = marked(NB, reason, "A-17") if with_campaign else blank(reason)
                    entry_cfg["campaign"] = nb
                    entry_cfg["delta"] = nb
                    entry_cfg["runs"] = nb
                else:
                    camp_med = median(counts)
                    entry_cfg["campaign"] = valued(plain(camp_med))
                    # BINDING: the difference is reported also when it is zero or
                    # negative (protocol §5 rev 31; spec §7.5 (4)). Nothing is
                    # suppressed, rounded away or replaced by the aggregate.
                    entry_cfg["delta"] = valued(plain(camp_med - rest_med))
                    # spec §7.5 (5), protocol rev. 40: the three repetition counts
                    # PRINTED SINGLY, resting side and campaign side. Purely descriptive.
                    entry_cfg["runs"] = valued(
                        f"{run_list(rest)} · {run_list(counts)}")

                if config in LLM_CONFIGS:
                    entry_cfg["sv"] = valued(
                        "ja" if sv else ("nein" if sv is not None else NOT_APPLICABLE))
                    entry_cfg["kein_en"] = kein_en_cell(strict_cell, rest_exists)
            if rest is not None:
                entry_cfg["rest_per_run"] = rest
            entry_cfg["campaign_per_run"] = counts
            row["configs"][config] = entry_cfg
        injections[iid] = row

    # T6 — run cost. The invocation counters and both clocks come from the HASHED run
    # manifests and are therefore available blind; tokens and latency come from the run
    # logs and only with --with-campaign.
    cost: dict[str, dict[str, Any]] = {}
    for config in CONFIGS:
        cost[config] = {
            "outer_ms": stock.outer_clock(config),
            "inner_ms": stock.inner_clock(config),
            "calls": None,
        }
        if with_campaign and config in LLM_CONFIGS:
            cost[config]["calls"] = call_costs(paths.campaign, config)

    return {
        "manifest_completeness": completeness,
        "control_denominator": control["K2"].denominator,
        "false_positives": fp,
        "preregistered_control": prereg,
        "rule_id_distribution": rules,
        "reference_classes": reference,
        "t7": {
            "totals": {c: stock.totals(c) for c in CONFIGS},
            "valid": {c: sorted(stock.valid(c)) for c in CONFIGS},
            "missing": {c: stock.missing(c) for c in CONFIGS},
            "invalid_invocations": [
                {"config": i.config, "injection_id": i.injection_id, "attempt": i.attempt,
                 "manifest": i.manifest, "repetition": i.repetition,
                 "invalid_reasons": i.invalid_reasons, "reasons": i.reasons,
                 "calls_total": i.calls_total, "calls_invalid": i.calls_invalid,
                 "calls_transport_failed": i.calls_transport_failed}
                for i in stock.invocations if not i.is_valid],
            "acceptance": acceptance_rules(stock),
            "crosscheck_journal": crosscheck,
        },
        "journal": {"valid": {k: sorted(v) for k, v in journal.valid.items()},
                    "missing": {c: journal.missing(c) for c in CONFIGS},
                    "invalid_rows": journal.invalid_rows},
        "manifest_missing": manifest_ne,
        "injections": injections,
        "co_findings": co_findings,
        "specials": specials,
        "preregistered": preregistered,
        "cost": cost,
        "t10": overlap(injections),
        "with_campaign": with_campaign,
        # R12 — checked on the files that were OPENED, not on the selector's bookkeeping.
        "invalid_artifacts_read": invalid_artifacts_read(paths.campaign, stock),
    }


# --------------------------------------------------------------------------------------
# Rendering — the skeleton's structure, unchanged
# --------------------------------------------------------------------------------------


# --------------------------------------------------------------------------------------
# T5 — precision, recall, F1
# --------------------------------------------------------------------------------------


#: the pre-registered classes that take an injection OUT of precision/recall/F1 --
#: exactly the two the T5 auflage (4) names. T9 cases 1 and 3 are co-findings: neither
#: hit nor false positive, but their injection stays in the computation.
T9_EXCLUDES = frozenset({"T9-6", "T9-7"})


@dataclass
class Score:
    """TP/FP/FN of one T5 row, with everything that was taken OUT of it named."""
    tp: int = 0
    fp: int = 0
    fn: int = 0
    dash: int = 0          # not expressible — counts as 0 in UF3, out of the denominator in UF4
    not_formable: int = 0  # `n. b.` — no measurement took place
    not_collected: int = 0 # `n. e.` — no valid run
    preregistered: int = 0 # T9 case 6/7 — neither hit nor FP, caught BEFORE this rule
    marker: str | None = None

    @property
    def denominator(self) -> int:
        return self.tp + self.fn

    def precision(self) -> float | None:
        return self.tp / (self.tp + self.fp) if (self.tp + self.fp) else None

    def recall(self) -> float | None:
        return self.tp / self.denominator if self.denominator else None

    def f1(self) -> float | None:
        p, r = self.precision(), self.recall()
        if p is None or r is None or (p + r) == 0:
            return None if (p is None or r is None) else 0.0
        return 2 * p * r / (p + r)

    def cells(self) -> list[str]:
        """P, R, F1 as printed. The reduced denominator is SHOWN, not silently used
        (T5 auflage (2)); an undefined value prints `0/0` — a computed statement about an
        empty set, never one of the four markers."""
        if self.marker is not None:
            # AS PRINTED, like every other table -- not the raw string (C11c D1).
            return [marker_text(self.marker)] * 3
        p, r, f = self.precision(), self.recall(), self.f1()
        p_text = (f"{num(self.tp)}/{num(self.tp + self.fp)} = {p:.3f}".replace(".", ",")
                  if p is not None else "0/0")
        r_text = (f"{num(self.tp)}/{num(self.denominator)} = {r:.3f}".replace(".", ",")
                  if r is not None else "0/0")
        f_text = f"{f:.3f}".replace(".", ",") if f is not None else "0/0"
        return [p_text, r_text, f_text]


def score_rows(result: dict[str, Any], config: str, metric: str,
               ids: list[str], *, drop_dash: bool) -> Score:
    """TP/FP/FN over a set of injections, with the four exclusions in their binding order.

    1. `n. b.` / `n. e.`  — no measurement. Out of the denominator, in BOTH total rows;
       the reduced denominator is shown (T5 auflage (2)).
    2. pre-registered special class (T9 case 6/7) — neither hit nor FP nor FN, caught
       BEFORE the general FP/FN rule (T5 auflage (4), spec §5 closing paragraph). The
       injection leaves the computation entirely; its frequency stands in T9.
    3. ` — ` — not excluded but DIRECTION-DEPENDENT: it enters the UF3 row as a 0
       (coverage is exactly the question) and is taken out of the UF4 denominator
       (`drop_dash`). False positives from a ` — ` injection do go into T5 (skeleton §1,
       Kontrollregel 2) — into UF3; they leave UF4 together with their injection.
    4. `ERROR` / tool abort — never an FN (T5 auflage (5), spec §6.2). It never reaches
       here: `evaluate_k4k5_injection` books it into no bucket at all.
    """
    score = Score()
    for iid in ids:
        cfg = result["injections"][iid]["configs"][config]
        cell = cfg[metric]
        # Markers come FIRST. A ` — ` cell is a statement about the TOOL — this category
        # is not expressible — and a pre-registered special class, which is a statement
        # about a FINDING, cannot overrule it: K2/`CYCLE` stays a not-expressible row
        # even though every finding on it is T9 case 6.
        if cell.marker == NB:
            score.not_formable += 1
            continue
        if cell.marker == NE:
            score.not_collected += 1
            continue
        if not cell.marker and set(cfg.get("preregistered") or ()) & T9_EXCLUDES:
            # ONLY cases 6 and 7 leave the computation (T5 auflage (4) names exactly
            # those two). T9 cases 1 and 3 are pre-registered CO-FINDINGS: neither hit
            # nor FP, but they do not remove their injection from P/R/F1.
            score.preregistered += 1
            continue
        if cell.marker == DASH:
            score.dash += 1
            if drop_dash:
                continue
            score.fn += 1
            score.fp += cfg["strict_fp"] if metric == "strict" else cfg["localized_fp"]
            continue
        if cell.value is None:
            continue                      # blind run — nothing computed
        score.tp += 1 if cell.value == 1 else 0
        score.fn += 0 if cell.value == 1 else 1
        score.fp += cfg["strict_fp"] if metric == "strict" else cfg["localized_fp"]
    return score


# --------------------------------------------------------------------------------------
# T10 — overlap of the baseline set against K2 resp. K3 (protocol rev. 44, spec §8.10)
# --------------------------------------------------------------------------------------


#: the four states ONE side can be in. `SIDE_OPEN` is the "no measurement" state -- it
#: collects `n. b.`, `n. e.` and the pre-registered special classes T9 case 6/7, which are
#: neither a hit nor a miss (T10 auflage (4)).
SIDE_HIT = "Treffer"
SIDE_MISS = "Verfehlung"
SIDE_DASH = "nicht ausdrückbar"
SIDE_OPEN = "nicht beurteilbar"

#: the baseline side IS a union, and it is named as one wherever it is printed.
BASELINE_CONFIGS = ["K1", "K4", "K5"]
BASELINE_LABEL = "Vereinigung K1 ∪ K4 ∪ K5"

#: the four assessable states of ONE injection -- and only these four form the
#: denominator of the aggregate row (T10 auflage (5)).
T10_BOTH = "beide"
T10_ONLY_BASE = "nur Baseline"
T10_NEITHER = "keiner"


def t10_cell_state(cfg: dict[str, Any], metric: str) -> tuple[str, str]:
    """The state of ONE cell, in the order T5 auflage (2) binds — and it is that order,
    not a second one invented here (T10 auflage (2)).

    The order decides exactly ONE constellation, and the fixture and the campaign both
    carry it: a ` — ` cell that ALSO carries a pre-registered special class — K2/`CYCLE`
    and K3/`CYCLE`, where every finding is T9 case 6. It stays NOT EXPRESSIBLE. ` — ` is a
    statement about the TOOL, the special class one about a FINDING; the second does not
    overwrite the first. `score_rows` books the same way, so the same cell means the same
    thing in T5 and in T10.
    """
    cell = cfg[metric]
    if cell.marker == NB:
        return SIDE_OPEN, "`n. b.`"
    if cell.marker == NE:
        return SIDE_OPEN, "`n. e.`"
    if cell.marker == DASH:
        return SIDE_DASH, "T8"
    if set(cfg.get("preregistered") or ()) & T9_EXCLUDES:
        return SIDE_OPEN, "Sonderklasse T9"
    if cell.value is None:
        return SIDE_OPEN, "nicht ausgewertet"
    return (SIDE_HIT, "") if cell.value == 1 else (SIDE_MISS, "")


def t10_side(row: dict[str, Any], configs: list[str], metric: str) -> tuple[str, str]:
    """The state of ONE side over its configurations, plus the cell text that names WHO
    carries it — a union must not hide what it is made of (T10, head of the table)."""
    states = [(config, t10_cell_state(row["configs"][config], metric)[0])
              for config in configs]
    for state in (SIDE_HIT, SIDE_MISS):
        carriers = [c for c, s in states if s == state]
        if carriers:
            return state, f"{state} ({', '.join(carriers)})"
    dash = [c for c, s in states if s == SIDE_DASH]
    if dash and len(dash) == len(states):
        return SIDE_DASH, f"{SIDE_DASH} ({', '.join(dash)})"
    reasons = sorted({t10_cell_state(row["configs"][c], metric)[1]
                      for c, s in states if s == SIDE_OPEN} - {""})
    return SIDE_OPEN, f"{SIDE_OPEN} ({', '.join(reasons) or 'ohne Messung'})"


def t10_class(base: str, llm: str, config: str) -> str:
    """(baseline state, LLM state) -> class. NOT EXPRESSIBLE beats everything — it is the
    statement about the tool; NOT ASSESSABLE beats hit and miss — it is the statement "no
    measurement"; the four states sit underneath.

    The line that carries this table: a pair with a not-expressible side NEVER becomes
    "only the other side". Turning it into one would book EXPRESSIVENESS as PERFORMANCE,
    and that is what the G2 reframing (B17, skeleton §1.1) rules out.
    """
    if base == SIDE_DASH and llm == SIDE_DASH:
        return "beide Seiten nicht ausdrückbar"
    if base == SIDE_DASH:
        return "Baseline nicht ausdrückbar"
    if llm == SIDE_DASH:
        return f"{config} nicht ausdrückbar"
    if SIDE_OPEN in (base, llm):
        return SIDE_OPEN
    if base == SIDE_HIT and llm == SIDE_HIT:
        return T10_BOTH
    if base == SIDE_HIT:
        return T10_ONLY_BASE
    if llm == SIDE_HIT:
        return f"nur {config}"
    return T10_NEITHER


def overlap_table(injections: dict[str, dict[str, Any]], config: str,
                  metric: str) -> dict[str, Any]:
    """ONE row group of T10: the baseline union against ONE LLM configuration.

    Nothing is computed a second time here. Every state comes out of a cell T2 and T4
    already carry, and out of the pre-registered expressiveness of T8 (T10 auflage (6)):
    if T10 disagrees with T2, T10 is wrong.
    """
    rows = []
    counts: dict[str, int] = {}
    for iid, row in injections.items():
        base_state, base_text = t10_side(row, BASELINE_CONFIGS, metric)
        llm_state, llm_text = t10_side(row, [config], metric)
        verdict = t10_class(base_state, llm_state, config)
        counts[verdict] = counts.get(verdict, 0) + 1
        rows.append({"injection": iid, "scenario_l2": row["scenario_l2"],
                     "baseline": base_text, "llm": llm_text, "class": verdict})
    assessable = [T10_BOTH, T10_ONLY_BASE, f"nur {config}", T10_NEITHER]
    excluded = ["Baseline nicht ausdrückbar", f"{config} nicht ausdrückbar",
                "beide Seiten nicht ausdrückbar", SIDE_OPEN]
    return {"config": config, "metric": metric, "rows": rows,
            "counts": {name: counts.get(name, 0) for name in assessable + excluded},
            "denominator": sum(counts.get(name, 0) for name in assessable),
            "excluded": {name: counts.get(name, 0) for name in excluded},
            "total": len(rows)}


def overlap(injections: dict[str, dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    """T10a (`localized`) and T10b (`strict`), each with ONE row group per LLM
    configuration. K2 and K3 are NEVER united into "the LLM path" — the same auflage that
    stands over T2 and T5."""
    return {metric: [overlap_table(injections, config, metric)
                     for config in LLM_CONFIGS]
            for metric in ("localized", "strict")}


def t5_row(result: dict[str, Any], config: str, ids: list[str],
           *, drop_dash: bool) -> tuple[Score, Score]:
    """One T5 row for both metrics. A row whose injections ALL carry the same marker
    carries that marker itself — never a 0."""
    out = []
    for metric in ("strict", "localized"):
        score = score_rows(result, config, metric, ids, drop_dash=drop_dash)
        if ids and score.dash == len(ids):
            score.marker = DASH
        elif ids and score.not_formable == len(ids):
            score.marker = NB
        elif ids and score.not_collected == len(ids):
            score.marker = NE
        out.append(score)
    return out[0], out[1]


def ist_verdict(result: dict[str, Any], scenario: str, config: str) -> tuple[str, str]:
    """The Ist finding of ONE T1 cell, in the matrix vocabulary `ja / teilweise / nein`.

    T1 (ii): "je Zelle die Ist-Feststellung „erkannt / teilweise / nicht erkannt" aus T2".
    `Soll` holds for `localized` (protocol §3, amendment 11.08.), so `localized` is read.

    Three values, and `teilweise` is not a rounding: an injection whose `localized` hit
    comes ONLY from a pre-registered "right place, wrong category" class is a PARTIAL
    detection — the tool reaches the place, not the category. That is exactly the
    distinction footnote 7 draws, and it is the reason protocol rev. 22 moved the two
    K5/CYCLE cells from `nein` to `teilweise`.

    Returns (verdict, marker) — the marker is non-empty where no verdict is formable.
    """
    rows = [r for r in result["injections"].values() if r["scenario_l2"] == scenario]
    cells = [(r["configs"][config]["localized"], r["configs"][config]) for r in rows]
    if not cells:
        return "", "kein Szenarioeintrag"
    if all(c.marker == DASH for c, _ in cells):
        # not expressible — the pre-registered Soll for such a cell is `nein`, and the
        # skeleton says so: "jede Soll-Zelle nein, die auf Ausdrucksmächtigkeit beruht,
        # erscheint in T2 als ` — `"
        return "nein", ""
    if all(c.marker == NB for c, _ in cells):
        return "", NB
    usable = [(c, cfg) for c, cfg in cells if c.marker is None]
    if not usable:
        return "", NE
    if any(c.value is None for c, _ in usable):
        return "", "nicht ausgewertet"
    full = sum(1 for c, cfg in usable if c.value == 1 and not cfg.get("place_only"))
    place = sum(1 for c, cfg in usable if c.value == 1 and cfg.get("place_only"))
    if full == len(usable):
        return "ja", ""
    if full == 0 and place == 0:
        return "nein", ""
    return "teilweise", ""


def t1_divergence(result: dict[str, Any], scenario: str) -> str:
    """T1 `Abweichung` — Soll against Ist, per row, COMPUTED.

    An empty cell means "computed, no deviation" and that is stated at the column. A
    deviation is REPORTED, never resolved: the Soll columns reproduce protocol §3 and are
    not re-decided here (T1 auflage (iii), protocol §7).
    """
    soll = T1_SOLL[scenario]
    out = []
    for config in ("K1", "K4", "K5", "K2", "K3"):
        verdict, marker = ist_verdict(result, scenario, config)
        want = soll["K2"] if config in LLM_CONFIGS else soll[config]
        if marker:
            out.append(f"{config} `{marker}` (kein Vergleich bildbar)")
        elif verdict != want:
            out.append(f"**{config}: Soll {want} / Ist {verdict}**")
    return " · ".join(out)


def t7_divergences(result: dict[str, Any]) -> list[str]:
    """Every place where a T7 cross-check contradicts the hashed run manifests."""
    out = []
    for config in CONFIGS:
        for divergence in result["t7"]["crosscheck_journal"][config]["divergences"]:
            out.append(f"`journal.jsonl` / {config}: {divergence}")
        from_manifest = sorted(result["manifest_missing"].get(config, []))
        if from_manifest != sorted(result["t7"]["missing"][config]):
            out.append(f"Prosa-Manifest / {config}: {from_manifest or '(keine)'} gegen "
                       f"Laufmanifeste {result['t7']['missing'][config] or '(keine)'}")
    return out


def scenario_cells(result: dict[str, Any], scenario: str, config: str,
                   metric: str) -> tuple[Cell, int, int]:
    """Aggregate one T2 cell over the injections of a scenario. Returns the cell plus the
    reduced numerator/denominator; a rate over fewer injections is a different rate and
    the reduced denominator is shown, not silently used (T7.3 auflage)."""
    rows = [r for r in result["injections"].values() if r["scenario_l2"] == scenario]
    if not rows:
        # No injection carries this scenario. That is a COMPUTED empty set, not a missing
        # cell: `0/0` says the denominator is empty, an empty cell would say "not
        # inserted by this run". Reachable only on a reduced stock (fixtures) -- the
        # pre-registered manifest occupies all ten scenarios.
        return valued("0/0", "leerer Nenner — keine Injektion trägt dieses Szenario"), 0, 0
    cells = [r["configs"][config][metric] for r in rows]
    if all(c.marker == DASH for c in cells):
        return marked(DASH, source="T1/T8"), 0, 0
    if all(c.marker == NB for c in cells):
        return marked(NB, source="A-17"), 0, 0
    usable = [c for c in cells if c.marker is None]
    if not usable:
        return marked(NE, source="T7.3"), 0, 0
    if any(c.value is None for c in usable):
        return blank(), 0, len(usable)
    return valued(f"{sum(int(c.value) for c in usable)}/{len(usable)}"), \
        sum(int(c.value) for c in usable), len(usable)


def render(result: dict[str, Any], paths: Paths) -> str:
    out: list[str] = []
    w = out.append
    fp = result["false_positives"]
    den = result["control_denominator"]

    def headline(config: str) -> str:
        data = fp.get(config)
        if not data:
            return "`n. b.`"
        return f"{plain(median(data['modulewise_headline']))}/{data['denominator']}"

    w("# Kapitel 7 — Ergebnistabellen (Ausgabe der Auswertungsharness)")
    w("")
    w("**Erzeugt von `tools/evaluate_campaign.py`.** Struktur, Spalten, Reihenfolge und")
    w("Fussnoten folgen `docs/kapitel/kapitel7_tabellenskelette.md` unverändert;")
    w("Druckreihenfolge **T1, T7, T2, T3, T4, T5, T6, T8, T9**.")
    w("")
    if not result["with_campaign"]:
        w("> **Kampagnenauswertung NICHT ausgeführt** (`--with-campaign` nicht gesetzt).")
        w("> Aus `data/campaign/` sind ausschliesslich **Metadaten** gelesen — die")
        w("> **gehashten Laufmanifeste** für **T7** sowie `journal.jsonl` und die")
        w("> Prosa-Manifeste als Gegenprobe. Die Laufmanifeste tragen Verdikte, Zähler und")
        w("> Provenienz, **keine Funde** (Blindheitsauflage, präzisiert C6c-a). Kein")
        w("> Laufartefakt unter `k1/`…`k5/` wurde geöffnet. Die kampagnenabhängigen Zellen")
        w("> von T2, T4, T5, T6,")
        w("> T9 bleiben **leer** — das ist der Skelettmarker *(leer)* „wird eingesetzt“ und")
        w("> ausdrücklich **weder** `n. e.` **noch** 0: für K1, K2, K4 und K5 liegen nach T7")
        w("> gültige Läufe vor, sie sind hier nur nicht ausgewertet.")
        w("")
    divergences = t7_divergences(result)
    if divergences:
        w("> **BEFUND — die T7-Gegenproben widersprechen den gehashten Laufmanifesten.**")
        w("> Ein bezeugtes Artefakt und eine Aufzeichnung sagen Verschiedenes. **Diese")
        w("> Ausgabe ist nicht zu verwenden, bevor geklärt ist, welche Seite falsch ist**;")
        w("> die Harness passt keine Seite an die andere an (Protokoll Rev. 39).")
        w(">")
        for line in divergences:
            w(f"> - {line}")
        w("")
    w("**Marker:** ` — ` nicht ausdrückbar (T1/T8, vorregistriert) · `n. b.` nicht bildbar")
    w("(vorregistriert) · `n. e.` nicht erhoben (aus T7) · *(leer)* von diesem Lauf nicht")
    w("eingesetzt. **Keine Zelle trägt 0, wo ein Marker gilt.**")
    w("")
    w("---")
    w("")

    # ---------------------------------------------------------------- T1 --------------
    w("## T1 — Erwartungsmatrix, Kategorie × Konfiguration (Soll gegen Ist)")
    w("")
    w("**Soll gilt für `localized`. Für `strict` besteht keine Vorhersage** (Protokoll §3,")
    w("Amendment 11.08.2026). Die Soll-Spalten reproduzieren Protokoll §3 und werden")
    w("**nicht neu entschieden**; jede Abweichung ist ein **Befund**.")
    w("")
    w("| Szenario (Ebene 2) | n | Soll K1 | Soll K4 | Soll K5 | Soll K2/K3 | Ist K1 | Ist K4 | Ist K5 | Ist K2 | Ist K3 | Abweichung |")
    w("|---|---|---|---|---|---|---|---|---|---|---|---|")
    for scenario in SCENARIO_ORDER:
        soll = T1_SOLL[scenario]
        ist = []
        for config in ["K1", "K4", "K5", "K2", "K3"]:
            cell, _hits, _denom = scenario_cells(result, scenario, config, "localized")
            ist.append(cell.text if cell.text else "")
        w(f"| `{scenario}` | {SCENARIO_N[scenario]} | {soll['K1']} | {soll['K4']} | "
          f"{soll['K5']} | {soll['K2']} | " + " | ".join(ist) + " | "
          + t1_divergence(result, scenario) + " |")
    w("")
    w("**Die Spalte `Abweichung` ist gerechnet.** Verglichen wird die vorregistrierte")
    w("Soll-Zelle mit der Ist-Feststellung derselben Zeile, im Matrixvokabular")
    w("**`ja` / `teilweise` / `nein`** und über `localized` (für `strict` besteht keine")
    w("Vorhersage). **`ja`** = jede auswertbare Injektion des Szenarios ist erkannt ·")
    w("**`nein`** = keine · **`teilweise`** = ein Teil, **oder** die Erkennung liegt")
    w("allein auf der **Stelle** (vorregistrierte Klasse „richtige Stelle, falsche")
    w("Kategorie“, T9 Fall 6/7) — genau die Unterscheidung, aus der Fussnote 7 die")
    w("Zelle `teilweise` bildet. Eine ` — `-Zeile wird als **`nein`** gelesen, weil das")
    w("Soll dort auf Ausdrucksmächtigkeit beruht (Skelett, Lesehilfe zu T2).")
    w("")
    w("> **EINE LEERE ZELLE IN DIESER SPALTE BEDEUTET: GERECHNET, KEINE ABWEICHUNG.** Sie")
    w("> ist **nicht** „nicht eingesetzt“. Das ist die einzige Spalte dieser Ausgabe, in")
    w("> der eine leere Zelle etwas aussagt, und sie steht deshalb namentlich in der")
    w("> Ausnahmeliste der Zusicherung R1. **Abweichungen werden AUSGEWIESEN, nicht")
    w("> aufgelöst** — die Soll-Spalten reproduzieren Protokoll §3 und werden hier nicht")
    w("> neu entschieden (Protokoll §7).")
    w("")
    w("---")
    w("")

    # ---------------------------------------------------------------- T7 --------------
    w("## T7 — Gültigkeit und Vollständigkeit des Messbestands")
    w("")
    w("> **Diese Tabelle steht VOR T2, T4 und T5.** Sie rechtfertigt **jedes** `n. e.`")
    w("> dort. Ein `n. e.`, das hier keine Entsprechung hat, ist ein Harness-Fehler.")
    w("")
    w("**Quelle: die gehashten Laufmanifeste** unter `data/campaign/manifests/`, ein")
    w("Manifest je Invocation, jedes von einem Block-`SHA256SUMS` bezeugt (Protokoll")
    w("Rev. 39). `journal.jsonl` und die Prosa-Manifeste sind **Gegenprobe, nicht Quelle**.")
    w("")
    t7 = result["t7"]
    w("### T7.1 — Gültigkeit je Konfiguration")
    w("")
    w("| Konfiguration | Invocationen | VALID | INVALID | Model-Calls | `calls_invalid` | "
      "`calls_transport_failed` | `valid_final`-Anteil | `skipped_count` | "
      "`invalid_reasons` (Werte) | Wiederholungen (`_r<n>`) |")
    w("|---|---|---|---|---|---|---|---|---|---|---|")
    for config in CONFIGS:
        t = t7["totals"][config]
        share = t["valid_final_share"]
        share_text = (f"{t['valid_final']} / {t['calls_measured']} = "
                      f"{share:.3f}".replace(".", ",") if share is not None
                      else "*(keine Model-Calls)*")
        reasons = ", ".join(f"`{k}` ×{v}" for k, v in t["invalid_reasons"].items()) \
            or "*(keine)*"
        w(f"| {config} | {t['invocations']} | {t['valid']} | {t['invalid']} | "
          f"{t['calls_total']} | {t['calls_invalid']} | {t['calls_transport_failed']} | "
          f"{share_text} | {t['skipped_count']} | {reasons} | {t['repetitions']} |")
    w("")
    w("`valid_final` ist **kein Manifestfeld**, sondern hier abgeleitet: gemessene Calls")
    w("(`calls_total` − `calls_transport_failed`) minus `calls_invalid`. Der Anteil steht")
    w("über den **gemessenen** Calls (`outcome: measured`); die Transportausfälle stehen")
    w("**daneben, nie darin** (Skelett T7.1). `skipped_count` ist aus den Werten von")
    w("`invalid_reasons` gezählt — der Checker führt übersprungene Dateien dort als")
    w("`skipped_files`, ein eigenes Feld gibt es nicht. Die Vielfachheit hinter den")
    w("`invalid_reasons`-Werten zählt **Invocationen**, nicht Calls.")
    w("")
    gate = [c for c in CONFIGS
            if (t7["totals"][c]["valid_final_share"] or 1.0) < 0.9]
    if gate:
        w(f"> **Validitäts-Gate §7 unterschritten** (Anteil < 0,9): {', '.join(gate)}. Nach")
        w("> Protokoll §7 ist das als **Befund zu dokumentieren** und die Konfiguration mit")
        w("> den vorhandenen gültigen Läufen auszuwerten — **nicht nachzubessern**.")
    else:
        w("**Validitäts-Gate §7:** kein `valid_final`-Anteil unter 0,9.")
    w("")
    w("**Gegenprobe `journal.jsonl` (append-only, keine gehashte Quelle):**")
    w("")
    w("| Konfiguration | Invocationen Journal | gültige Injektionen Journal | Ergebnis |")
    w("|---|---|---|---|")
    for config in CONFIGS:
        cross = t7["crosscheck_journal"][config]
        verdict = "**deckungsgleich**" if not cross["divergences"] else \
            "**ABWEICHUNG** — " + " · ".join(cross["divergences"])
        w(f"| {config} | {cross['journal_invocations']} | {cross['journal_valid']} | "
          f"{verdict} |")
    w("")
    w("### T7.2 — Zählregeln und positive Lauf-Akzeptanz")
    w("")
    w("| Konfiguration | Regel | Erwartet | Gemessen | erfüllt |")
    w("|---|---|---|---|---|")
    notes = []
    for row in t7["acceptance"]:
        met = "`n. b.`" if row["met"] is None else ("**ja**" if row["met"] else "**NEIN**")
        mark = ""
        if row["note"]:
            notes.append(row["note"])
            mark = f" ({len(notes)})"
        w(f"| {row['scope']} | {row['rule']} | {row['expected']} | {row['measured']} | "
          f"{met}{mark} |")
    w("")
    for index, note in enumerate(notes, start=1):
        w(f"({index}) {note}")
        w("")
    w("**Warum diese Zeilen keine Formalie sind.** K4 und K5 schreiben **kein**")
    w("Laufprotokoll; ohne eine **positive** Aussage über den Lauf ist eine")
    w("Fehlkonfiguration, die die Regelmenge verkürzt, **unsichtbar** — sie erzeugt null")
    w("Findings ohne Fehlermeldung (Protokoll §9, T12-Ergänzung Rev. 32). Die Bezeugung")
    w("des K4-Rohtexts gilt für die **archivierte Zeilenaufteilung** (80 Spalten), nicht")
    w("für eine beliebig nacherzeugte (Skelett T7.2, C6b-2b).")
    w("")
    w("### T7.3 — Nicht erhobene Injektionen (Quelle jedes `n. e.`)")
    w("")
    w("| Konfiguration | Injektionen ohne gültigen Lauf | Anzahl | Gegenprobe Journal | "
      "Gegenprobe Prosa-Manifest |")
    w("|---|---|---|---|---|")
    for config in CONFIGS:
        missing = t7["missing"][config]
        cross = t7["crosscheck_journal"][config]
        from_journal = cross["journal_missing"]
        from_manifest = result["manifest_missing"].get(config, [])
        agree_j = "**deckungsgleich**" if sorted(from_journal) == sorted(missing) else \
            f"**ABWEICHUNG** — Journal: {', '.join(from_journal) or '(keine)'}"
        agree_m = "**deckungsgleich**" if sorted(from_manifest) == sorted(missing) else \
            f"**ABWEICHUNG** — Manifest: {', '.join(from_manifest) or '(keine)'}"
        w(f"| {config} | {', '.join(missing) if missing else '*(keine)*'} | "
          f"{len(missing)} | {agree_j} | {agree_m} |")
    w("")
    w("**Weicht eine Gegenprobe ab, wird das berichtet, nicht aufgelöst** — die Harness")
    w("passt keine Seite an die andere an (Skelett T7.3 Bildungsvorschrift; Protokoll")
    w("Rev. 39). Die Abweichung erscheint zusätzlich auf `stderr`.")
    w("")
    w("### T7.4 — Ungültige Läufe im Einzelnen")
    w("")
    w("| Konfiguration | Injektion | `attempt` | Laufmanifest | Grund (`invalid_reasons`) | "
      "`calls_total` / `calls_invalid` / `calls_transport_failed` | Verdikt danach |")
    w("|---|---|---|---|---|---|---|")
    invalid = t7["invalid_invocations"]
    if not invalid:
        w("| *(keine)* | | | | | | |")
    for row in invalid:
        later = "**VALID** in einem späteren Versuch" \
            if row["injection_id"] not in t7["missing"][row["config"]] else "**ohne gültigen Lauf**"
        reasons = ", ".join(f"`{r}`" for r in row["invalid_reasons"]) or "*(keine)*"
        w(f"| {row['config']} | {row['injection_id']} | {row['attempt']} | "
          f"`{row['manifest']}` | {reasons} | {row['calls_total']} / "
          f"{row['calls_invalid']} / {row['calls_transport_failed']} | {later} |")
    w("")
    w("**Eine unbekannte `rule_id` invalidiert den ganzen Versuch**, nicht nur das")
    w("betroffene Finding (Auswertungsspezifikation §7.4). Der Exit-Code ist **kein**")
    w("Gültigkeitskriterium (Protokoll §6 Nachtrag Rev. 26).")
    w("")
    w("---")
    w("")

    # ---------------------------------------------------------------- T2 --------------
    w("## T2 — Haupttabelle Erkennung")
    w("")
    w("**Erste Stufe vor beiden Metriken: Filter nach Mechanismus** — K1 := Records mit")
    w("`rule_id`-Präfix `DERIVED:`, K2/K3 := jeder andere `rule_id` (Protokoll §4 Nachtrag")
    w("Rev. 25). **K2 und K3 werden nirgends addiert.**")
    w("")
    w("| Szenario (n) | K1 loc | K1 str | K2 loc | K2 str | K2 FP-M | K3 loc | K3 str | K3 FP-M | K4 loc | K4 str | K5 loc | K5 str |")
    w("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for scenario in SCENARIO_ORDER:
        cells = []
        for config in ["K1"]:
            for metric in ("localized", "strict"):
                cells.append(scenario_cells(result, scenario, config, metric)[0].text)
        for config in ("K2", "K3"):
            for metric in ("localized", "strict"):
                cells.append(scenario_cells(result, scenario, config, metric)[0].text)
            cells.append(f"**{headline(config)}**")
        for config in ("K4", "K5"):
            for metric in ("localized", "strict"):
                cells.append(scenario_cells(result, scenario, config, metric)[0].text)
        # column order of the skeleton: K1 loc/str, K2 loc/str/FP, K3 loc/str/FP, K4, K5
        w(f"| `{scenario}` ({SCENARIO_N[scenario]}) | " + " | ".join(cells) + " |")
    w("")
    w("**Die Spalten `K2 FP-M` / `K3 FP-M` sind Pflicht** und tragen die modulweise")
    w("Falsch-Positiv-Rate derselben Konfiguration aus T3 in **jeder** Zeile: `localized`")
    w("darf für K2/K3 nie ohne sie erscheinen (Protokoll §5 Amendment 11.08.;")
    w("Auswertungsspezifikation §4.2, §8 Punkt 1).")
    w("")
    w("**Fussnoten (Pflicht, Wortlaut im Skelett):** (a) `localized` bei K4/`CYCLE` ist")
    w("`n. b.`, nicht 0 · (b) die K2/K3-Nullzeilen bei `CYCLE` sind konstruktionsbedingt ·")
    w("**(c) `FORBIDDEN_SIGNATURE_TYPE` — vorregistrierter `strict`-Ausfallmodus** (Segmente")
    w("1–3 gleich, Segment 4 gekürzt; Kennzeichnung als eigene Spalte **SV** in T4, nicht")
    w("als Fussnote am Tabellenende) · **(d) `STRUCTURAL_PLACEMENT` — `strict` ist dort")
    w("nicht unabhängig von `localized`** (Segment 4 == Segment 3) · (e) `localized` misst")
    w("auf dem LLM-Pfad die **Meldequote** · (f) die erwartete Kategorie ist pfadabhängig ·")
    w("(g) die Subjektform ist im Regelstatement vorgegeben.")
    w("")
    w("---")
    w("")

    # ---------------------------------------------------------------- T3 --------------
    w("## T3 — Falsch-Positiv-Raten je LLM-Konfiguration, zwei Granularitäten")
    w("")
    w("> **AUFLAGE IM KOPF DER TABELLE (Protokoll §5, Amendment 11.08.2026):** `localized`")
    w("> ist **nur zusammen mit dieser Messreihe interpretierbar**. **`localized` wird nie")
    w("> ohne diese Tabelle berichtet.** **K2 und K3 werden nirgends addiert.**")
    w("")
    w(f"**Quelle:** `{paths.control_k2}` und `{paths.control_k3}` — **nicht** die Kampagne.")
    w(f"**Nenner {den}** (inhaltstragende Kontrollmodule).")
    w("")
    w("| Konfiguration | Granularität | Bezugsmetrik | run 0 | run 1 | run 2 | Median | Spannweite | Headline |")
    w("|---|---|---|---|---|---|---|---|---|")
    for config in LLM_CONFIGS:
        data = fp[config]
        runs = data["modulewise_headline"]
        lo, hi = data["headline_span"]
        w(f"| {config} | **modulweise** (Module mit ≥ 1 Finding / {den}) | Bezug für "
          f"`localized` | " + " | ".join(str(v) for v in runs) +
          f" | **{plain(median(runs))}** | {plain(lo)}–{plain(hi)} | "
          f"**{plain(median(runs))}/{den}** |")
        fw = data["findingwise"]
        flo, fhi = data["findingwise_span"]
        w(f"| {config} | **findingweise** (Findings gesamt, undedupliziert) | Bezug für "
          f"`strict` und Precision | " + " | ".join(str(v) for v in fw) +
          f" | **{plain(median(fw))}** | {plain(flo)}–{plain(fhi)} | {marker_text(DASH)} |")
    w("")
    w("**Die Headline zählt ALLE Findings — die beiden vorregistrierten Meldungen bleiben")
    w("darin und stehen zusätzlich getrennt in T3.1** (§7.2 in der Fassung der")
    w("Protokoll-Rev. 37, 28.08.2026: nicht herausgerechnet, weil die Herausrechnung die")
    w("gemessene Rate verbesserte, gewählt und nicht erzwungen wäre und der Auflage")
    w("widerspräche, `localized` nie ohne die vollständige FP-Rate zu berichten).")
    w("")
    w("**Zweite Lesart, mitgeführt und ausdrücklich NICHT die Headline:** dieselbe")
    w("modulweise Zahl **ohne** die vorregistrierten Meldungen — sie steht hier, damit")
    w("sichtbar bleibt, ob die beiden Lesarten auseinanderfallen:")
    w("")
    w("| Konfiguration | run 0 | run 1 | run 2 | Median | fällt auseinander? |")
    w("|---|---|---|---|---|---|")
    for config in LLM_CONFIGS:
        data = fp[config]
        less = data["modulewise_less_preregistered"]
        same = data["modulewise_all"] == less
        w(f"| {config} | " + " | ".join(str(v) for v in less) +
          f" | **{plain(median(less))}** | "
          f"{'nein — beide Lesarten gleich' if same else '**ja**'} |")
    w("")
    w("### T3.1 — Die vorregistrierten Meldungen, getrennt ausgewiesen")
    w("")
    w("**Sie sind im Headline-Zähler oben ENTHALTEN** (§7.2, Protokoll Rev. 37) und stehen")
    w("hier zusätzlich, damit sichtbar bleibt, welcher Teil der Rate vorhergesagt war.")
    w("")
    w("| Konfiguration | Fall | Zähler je Lauf (0/1/2) | Häufigkeit | vorregistriert in |")
    w("|---|---|---|---|---|")
    for config in LLM_CONFIGS:
        for row in result["preregistered_control"][config]:
            w(f"| {config} | {row['label']} | " + "/".join(str(v) for v in row["per_run"]) +
              f" | **{row['runs_with']} von {row['runs_total']} Läufen** | {row['source']} |")
    w("")
    w("**Getrennte Recordzählung (Protokoll §4 Rev. 25), nie als Summe:**")
    w("")
    w("| Konfiguration | `DERIVED:`-Records je Lauf | LLM-Records je Lauf |")
    w("|---|---|---|")
    for config in LLM_CONFIGS:
        data = fp[config]
        w(f"| {config} | " + "/".join(str(v) for v in data["derived_per_run"]) + " | " +
          "/".join(str(v) for v in data["findingwise"]) + " |")
    w("")
    w("**Findings je `rule_id`** (aus den Artefakten gezählt, nicht aus einem Bericht")
    w("übernommen — Anhang A, Zeile A-10):")
    w("")
    w("| Konfiguration | " + " | ".join(f"`{r}`" for r in
                                        sorted({r for cfg in LLM_CONFIGS
                                                for r in result["rule_id_distribution"][cfg]})) + " |")
    all_rules = sorted({r for cfg in LLM_CONFIGS for r in result["rule_id_distribution"][cfg]})
    w("|---" * (len(all_rules) + 1) + "|")
    for config in LLM_CONFIGS:
        dist = result["rule_id_distribution"][config]
        w(f"| {config} | " + " | ".join(str(dist.get(r, 0)) for r in all_rules) + " |")
    w("")
    for config in LLM_CONFIGS:
        ref = result["reference_classes"].get(config)
        if not ref:
            continue
        w(f"**Bezug der {config}-Findings zum geprüften Modul** (deskriptive Gegenprobe,")
        w("Anhang A Zeile A-09/A-10). **Die Klassen heissen Selbstbezug, Fremdbezug,")
        w("Zielbezug und nicht zuordenbar** — nicht K1–K4: jene Bezeichner kollidieren mit")
        w("den Konfigurationsnamen dieser Arbeit:")
        w("")
        w("| Klasse | Anzahl | Anteil |")
        w("|---|---|---|")
        for name in REFERENCE_CLASS_ORDER:
            if name in ref["counts"]:
                w(f"| {name} | {ref['counts'][name]} | {ref['pct'].get(name, '')} % |")
        agree = ("**deckungsgleich**" if ref["agrees"]
                 else f"**ABWEICHUNG** — archiviert {ref['archived_total']}")
        w(f"| **gesamt** | **{ref['own_total']}** | Gegenprobe gegen das archivierte "
          f"`finding_reference_analysis.json`: {agree} |")
        w("")
    w("---")
    w("")

    # ---------------------------------------------------------------- T4 --------------
    w("## T4 — Vorbelastung, Kampagnenwert und paarweise Differenz je Injektion")
    w("")
    w("> **BINDEND: Die Differenz wird auch berichtet, wenn sie null oder negativ ist.**")
    w("> Sie fällt nicht heraus, wird nicht gerundet und wird nicht kommentarlos durch die")
    w("> Aggregatzahl ersetzt (Protokoll §5 Rev. 31). **Es wird nichts subtrahiert** —")
    w("> die Differenz tritt **neben** Precision/Recall/F1, nie an ihre Stelle.")
    w("")
    w("**Ruhezustandsseite:** `data/c3b-k2/` bzw. `data/c3b-k3/`, konfigurationsgleich,")
    w("gleiche Repetitionszahl auf beiden Seiten. **Berichtsform Grössenordnungen**, ohne")
    w("Nachkommastellen-Interpretation.")
    w("")
    w("| ID | Szenario | Trägermodul | K2 Ruhe | K2 Kampagne | K2 Δ | K2 Läufe (Ruhe · Kampagne) | K2 `strict` | K2 `loc` | K2 SV | K2 kein-EN | K3 Ruhe | K3 Kampagne | K3 Δ | K3 Läufe (Ruhe · Kampagne) | K3 `strict` | K3 `loc` | K3 SV | K3 kein-EN |")
    w("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for iid in sorted(result["injections"]):
        row = result["injections"][iid]
        cells = [iid, f"`{row['scenario_l2']}`", f"`{row['carrier_module']}`"]
        for config in LLM_CONFIGS:
            cfg = row["configs"][config]
            for key in ("rest", "campaign", "delta", "runs",
                        "strict", "localized", "sv", "kein_en"):
                cells.append(cfg[key].text if key in cfg else "")
        w("| " + " | ".join(cells) + " |")
    w("")
    w("**Spaltenbedeutung.** **Ruhe** = Ruhezustandszahl desselben Moduls in derselben")
    w("Kategorie aus C3b (Median über drei Läufe) · **Kampagne** = dieselbe Zählgrösse auf")
    w("dem Injektionscommit (Median) · **Δ** = Kampagne − Ruhe · **Läufe (Ruhe ·")
    w("Kampagne)** = dieselbe Zählgrösse für **jede der drei Repetitionen einzeln**, in")
    w("`run_index`-Reihenfolge, **rein deskriptiv** (Spez. §7.5 (5), Protokoll Rev. 40) ·")
    w("**SV** = Schreibweisenverfehlung, mechanisch gebildet (`localized` Treffer **und**")
    w("`strict` 0 **und** Abweichung allein in Segment 4) · **kein-EN** = ein")
    w("`strict`-Treffer, der die Ruhezustandsrate **nicht übersteigt**, wird nicht als")
    w("Erkennungsnachweis geführt.")
    w("")
    w("> **kein-EN steht auf EINER Aggregationsstufe — der Existenzstufe** (Protokoll")
    w("> Rev. 40, gesetzt **nach** dem ersten Auswertungslauf und dort ungeschminkt")
    w("> registriert). Verglichen wird `strict` (Existenz über die drei Repetitionen,")
    w("> unverändert nach §4) mit der **Existenz** der Ruhezustandszählgrösse — mindestens")
    w("> einer der drei C3b-Läufe > 0. **`ja`** = beides vorhanden (übersteigt nicht) ·")
    w("> **`nein`** = `strict`-Treffer bei leerem Ruhezustand (übersteigt) ·")
    w(f"> **`{NOT_APPLICABLE}`** = kein `strict`-Treffer, die Frage stellt sich nicht — ein")
    w("> **gerechneter** Wert, **kein Marker**. Trägt `strict` einen Marker, trägt kein-EN")
    w("> denselben. **Die Spalten `Ruhe`, `Kampagne` und `Δ` bleiben auf dem Median** und")
    w("> werden von kein-EN **nicht gelesen** — sie sind die eigenständige paarweise")
    w("> Auslesart nach §7.5 (4). **Der Filterunterschied bleibt und ist benannt:**")
    w("> `strict` filtert über den `match_key`, die Ruhezustandszahl über Trägermodul und")
    w("> Kategorie; Rev. 40 legt die **Stufe** fest, nicht den Filter.")
    w("")
    w("### T4 Symmetrieteil — K1, K4, K5")
    w("")
    w("| ID | K1 Ruhe | K1 Kampagne | K1 Δ | K4 Ruhe | K4 Kampagne | K4 Δ | K5 Ruhe | K5 Kampagne | K5 Δ |")
    w("|---|---|---|---|---|---|---|---|---|---|")
    for iid in sorted(result["injections"]):
        row = result["injections"][iid]
        cells = [iid]
        for config in ("K1", "K4", "K5"):
            cfg = row["configs"][config]
            # A-14: no archived resting-state artifact for K1/K4/K5 — C3b covers only the
            # LLM paths. Carried as a constant 0 WITH a report reference, marked as such.
            # The CAMPAIGN side is computed here (C11b R5): the same counting quantity as
            # on the LLM path, read path-correctly, one run.
            for key in ("rest", "campaign", "delta"):
                cells.append(cfg[key].text if key in cfg else "")
        w("| " + " | ".join(cells) + " |")
    w("")
    w("**Kampagnenseite für K1/K4/K5 (nachgetragen C11b).** Dieselbe Zählgrösse wie im")
    w("Hauptteil — **Findings desselben Moduls in derselben Kategorie** —, mit der")
    w("**pfadabhängigen** Kategorie (Spez. §4): auf dem K1-Pfad `layer-violation` bzw.")
    w("`cycle`, nie ein Ebene-1-Name. Für K4/K5 stammt der gemeldete Modulname aus")
    w("`tools/match_k4k5.py`; wo die Ausgabeform **strukturell kein Modul** trägt")
    w("(`acyclic_siblings`-Block), ist die Zählgrösse **nicht bildbar** und die Zelle")
    w("trägt `n. b.` — **nicht 0** (A-17, Protokoll §4 Rev. 30). Alle drei")
    w("Konfigurationen tragen **einen** Lauf; die Differenz ist mangels Streuung trivial")
    w("und wird aus Symmetrie der Tabelle **dennoch ausgewiesen** (Spez. §7.5 (4)).")
    w("")
    w("**ᴬ¹⁴ Herkunft der Ruhezustandsseite für K1/K4/K5:** der Clean-State-Audit (C3a,")
    w("**0 Findings**), **nicht** C3b — C3b umfasst nur die LLM-Pfade. Ein")
    w("maschinenlesbares C3a-Artefakt ist **nicht archiviert**; die 0 ist aus")
    w("`c3a_bericht_clean_state_audit.md` übernommen und hier als **Berichtswert**")
    w("gekennzeichnet, nicht als gemessenes Artefakt (Anhang A, Zeile **A-14**).")
    w("")
    w("---")
    w("")

    # ---------------------------------------------------------------- T5 --------------
    w("## T5 — Precision / Recall / F1")
    w("")
    w("> **AUFLAGE IM KOPF DER TABELLE:** **K2 und K3 stehen in getrennten Zeilen und")
    w("> werden NIRGENDS zu „dem LLM-Pfad“ addiert oder gemittelt.**")
    w("")
    w("Kennzahlen **ohne Nachkommastellen-Interpretation**; die Arbeit macht Existenz-,")
    w("Non-Inferiority- und Nicht-Abdeckungsaussagen, keine Präzisionsschätzungen.")
    w("")
    w("| Konfiguration | Kategorie (Ebene 1) | n | `strict` P | `strict` R | `strict` F1 | `loc` P | `loc` R | `loc` F1 | FP-Bezug (T3) |")
    w("|---|---|---|---|---|---|---|---|---|---|")
    by_l1: dict[str, list[str]] = {l1: [] for l1 in L1_ORDER}
    for iid, row in sorted(result["injections"].items()):
        by_l1.setdefault(row["category_l1"], []).append(iid)
    every = sorted(result["injections"])

    def emit(config: str, label: str, n: Any, ids: list[str], drop_dash: bool,
             fp_ref: str, note: str = "") -> None:
        strict_score, loc_score = t5_row(result, config, ids, drop_dash=drop_dash)
        cells = strict_score.cells() + loc_score.cells()
        if config == "K4" and label.startswith("`CYCLE`"):
            cells[3] = cells[4] = cells[5] = "`n. b.`ᵃ"
        w(f"| {config} | {label}{note} | {n} | " + " | ".join(cells) + f" | {fp_ref} |")

    for config in CONFIGS:
        fp_ref = f"**{headline(config)}**" if config in LLM_CONFIGS else "`n. b.`"
        for l1 in L1_ORDER:
            emit(config, f"`{l1}`", L1_N[l1], by_l1.get(l1, []), False, fp_ref)
        # The label names WHICH denominator it means. The cells compute with the
        # COMPUTED one, which drops on `n. b.`, `n. e.` and the pre-registered special
        # classes -- for K4 and K5 the UF3 row lands on 28. The old label said "Nenner 32"
        # and contradicted the reading rule printed under the table (C11c phase 1;
        # skeleton correction of 28.08.2026 under T5). Label only -- no denominator, no
        # filter and no aggregation stage is touched here.
        emit(config, "**Gesamt — UF3, Abdeckung des Kategoriespektrums, "
                     "vorregistrierter Nenner 32, gerechneter Nenner je Zelle "
                     "ausgewiesen**", 32, every, False, fp_ref)
        emit(config, f"**Gesamt — UF4, Leistung im ausdrückbaren Bereich, "
                     f"vorregistrierter Nenner {UF4_DENOMINATOR[config]}, gerechneter "
                     f"Nenner je Zelle ausgewiesen**", UF4_DENOMINATOR[config], every,
             True, fp_ref)
    w("")
    w("**Wie die Zellen zu lesen sind.** `TP/Nenner = Wert`. **Der Nenner ist der")
    w("gerechnete, ausgewiesene Nenner** — er sinkt bei `n. e.` und `n. b.` und bei den")
    w("vorregistrierten Sonderklassen, und eine Rate über weniger Injektionen ist eine")
    w("andere Rate (Auflage (2)). Die Spalte `n` bleibt daneben der **vorregistrierte**")
    w("Wert aus dem Skelett und wird nicht nachgeführt. **`0/0`** heisst: der Nenner ist")
    w("**leer** — bei Precision, dass die Konfiguration in dieser Zeile **nichts** gemeldet")
    w("hat, bei Recall, dass **keine** Injektion der Zeile in die Rechnung eingeht. Das ist")
    w("eine **gerechnete Angabe, kein Marker**, und ausdrücklich **nicht** dasselbe wie 0.")
    w("")
    w("**Die vier Ausschlüsse, in dieser Reihenfolge.** **(1)** `n. b.` und `n. e.` — keine")
    w("Messung, aus dem Nenner **beider** Gesamtzeilen genommen · **(2)** die")
    w("vorregistrierten Sonderklassen **T9 Fall 6 und Fall 7** — **weder** Treffer **noch**")
    w("FP **noch** FN, **vor** der allgemeinen FP/FN-Rechnung abgefangen (Auflage (4));")
    w("ihre Häufigkeit steht in **T9** · **(3)** ` — ` — **nicht** ausgeschlossen, sondern")
    w("richtungsabhängig: in **UF3** geht es als **0** ein (Abdeckung ist genau die Frage),")
    w("in **UF4** ist es aus dem Nenner **genommen**; die Falsch-Positiven einer")
    w("` — `-Injektion gehen nach Skelett §1 Kontrollregel 2 dennoch in T5 ein — in UF3, und")
    w("mit ihrer Injektion zusammen fallen sie aus UF4 · **(4)** `ERROR` und")
    w("Werkzeugabbruch sind **kein** FN (Auflage (5)) — sie erreichen die Rechnung nicht.")
    w("")
    w("**FP-Bildung.** `strict` dedupliziert **nicht**: je **Lauf** zählt der passende")
    w("Record als **ein** TP, jeder weitere Record desselben Laufs als FP, über die Läufe")
    w("summiert (§3.2). Ein in der nächsten Repetition **wiederholter richtiger** Treffer")
    w("ist Reproduzierbarkeit, kein Falsch-Positiv. `localized` **dedupliziert** auf")
    w("`(component, module, category)`; jedes andere Tripel ist **ein** FP, unabhängig")
    w("davon, wie oft es auftritt (§7.3).")
    w("")
    # R14 (C14, protocol rev. 44): this note said "LÜCKE, benannt und nicht gefüllt"
    # while skeleton, specification and protocol have carried the requirement as
    # WITHOUT OBJECT and thereby SETTLED since rev. 42 (C11c §2). The text is pulled onto
    # that reasoning; no cell moves.
    w("> **ERLEDIGT, GEGENSTANDSLOS — die Anforderung entfällt, sie wird nicht")
    w("> abgewiesen** (Protokoll Rev. 42, Skelett T5 (ii), Spezifikation §8 Punkt 1).")
    w("> Skelett T5 (ii) verlangte für K2/K3 zusätzlich **Median und Spannweite über drei")
    w("> Läufe**. Beide setzen eine **laufweise** Grösse voraus, über die gestreut werden")
    w("> kann; `strict` ist nach Spezifikation §3 ein **Existenzquantor über die")
    w("> Repetitionen** und hat konstruktiv **keine Verteilung über Läufe**. Eine")
    w("> laufweise Fassung wäre keine zweite Auslesart derselben Metrik, sondern eine")
    w("> **neue Metrikdefinition** — gesperrt nach Protokoll §0.1 Punkt 2. **Die")
    w("> Laufstreuung ist ausgewiesen, an der dafür vorregistrierten Stelle:** seit")
    w("> Rev. 40 trägt **T4** die Spalte **Läufe (Ruhe · Kampagne)** mit **jeder der drei")
    w("> Repetitionen einzeln** — feinkörniger als ein Median, nicht gröber. **T3 führt")
    w("> Median und Spannweite über drei Läufe unverändert weiter**; die Erledigung")
    w("> betrifft allein diese Tabelle.")
    w("")
    w("**Beide Gesamtzeilen werden immer gemeinsam gedruckt.** In der UF3-Zeile gehen die")
    w("nicht ausdrückbaren Kategorien **als 0** ein — das ist gewollt und steht **an der")
    w("Zeile**: Abdeckung ist genau die Frage. In der UF4-Zeile sind sie aus dem Nenner")
    w("**genommen**, nicht als 0 gezählt; die Nenner folgen aus **T8**, nicht aus einer")
    w("Messung. **(3)** `localized` für K2/K3 nie ohne FP-Bezug; für K1/K4/K5 trägt die")
    w("Spalte `n. b.` **(4)** die vorregistrierten Sonderklassen (T9 Fälle 6 und 7) gehen")
    w("**nicht** in P/R/F1 ein und werden **vor** der allgemeinen FP/FN-Rechnung")
    w("abgefangen **(5)** `ERROR` ist **kein** FN — eigene Klasse „Regel nicht")
    w("ausgewertet“.")
    w("")
    w("---")
    w("")

    # ---------------------------------------------------------------- T6 --------------
    w("## T6 — Laufkosten je Konfiguration")
    w("")
    w("| Konfiguration | Invocationen | Model-Calls | Wanduhr aussen, Summe | Wanduhr aussen je Invocation (Median / Spannweite) | Wanduhr innen (`wall_clock_ms`) | Tokens in gesamt | Tokens out gesamt | Tokens je Check (Median) | Latenz je Call (Median / Spannweite) |")
    w("|---|---|---|---|---|---|---|---|---|---|")
    for config in CONFIGS:
        totals = result["t7"]["totals"][config]
        cost = result["cost"][config]
        outer = cost["outer_ms"]
        inner = cost["inner_ms"]
        # K4/K5 have no `run_footer` — the inner value is NOT FORMABLE there, not zero.
        inner_cell = "`n. b.`ᵃ" if not inner else f"{num(sum(inner))} ms"
        tok = "` — `" if config in ("K1", "K4", "K5") else ""
        calls = cost["calls"]
        if calls is not None:
            per_check = [a + b for a, b in zip(calls["tokens_in"], calls["tokens_out"])]
            tokens_in = f"{num(sum(calls['tokens_in']))}"
            tokens_out = f"{num(sum(calls['tokens_out']))}"
            per_check_cell = median_span_text(per_check) if per_check else "0/0"
            latency_cell = (median_span_text(calls["latency_ms"]) + " ms"
                            if calls["latency_ms"] else "0/0")
        else:
            tokens_in = tokens_out = per_check_cell = latency_cell = tok
        w(f"| {config} | {num(totals['invocations'])} | {num(totals['calls_total'])} | "
          f"{num(sum(outer))} ms | "
          f"{median_span_text(outer) if outer else '0/0'} ms | {inner_cell} | "
          f"{tokens_in} | {tokens_out} | {per_check_cell} | {latency_cell} |")
    w("")
    w("**Herkunft jeder Spalte.** *Invocationen*, *Model-Calls* und beide Wanduhren")
    w("stammen aus den **gehashten Laufmanifesten** (`external_wall_clock_ms` für aussen,")
    w("`postrun.detail.wall_clock_ms_inner` für innen) und sind deshalb auch ohne")
    w("`--with-campaign` verfügbar. *Tokens* und *Latenz* stammen aus den `llm_call`-")
    w("Records der Kampagnen-Laufprotokolle (`tokens_in_total`, `tokens_out_total`,")
    w("`latency_ms_total`) — **ein `llm_call` ist ein Check**, also ein Dateiprompt")
    w("(Protokoll §5, Entscheidung I). Sie werden **nur** mit `--with-campaign` gelesen;")
    w("die Laufprotokolle tragen Funde und sind sonst durch die Blindheitsauflage")
    w("gesperrt. **`0/0`** heisst auch hier: leere Menge, kein gemessener Nullwert.")
    w("")
    w("**Fussnoten (Pflicht).** **(a)** Die berichtete Wanduhrzeit ist für alle fünf")
    w("Konfigurationen **extern** gemessen; für K4/K5 existiert **kein** `run_footer`, der")
    w("Innenwert ist dort `n. b.` Feldname der externen Zeit im Laufmanifest:")
    w("**`external_wall_clock_ms`** (Anhang A, Zeile **A-28**, hiermit geschlossen) ·")
    w("**(b)** K4 baut den Graphen bei jedem Lauf neu (`--no-cache` ist Ablaufregel) —")
    w("die gemessene Zeit **enthält den vollen Graphaufbau** · **(c)** K5 bricht beim")
    w("ersten fehlgeschlagenen Assert ab; die Laufzeit hängt am **Trefferzeitpunkt** ·")
    w("**(d)** Berichtsform **Grössenordnungen**, ohne Interpretation von")
    w("Nachkommastellen; Token-Zahlen tragen den **Tokenizer-Vorbehalt** (§9 T5) ·")
    w("**(e) Der K4-Rohtext ist an der Terminalbreite geformt:** `rich` fällt bei Ausgabe")
    w("in eine Pipe auf **80 Spalten** zurück, gemessen `console.width = 80`,")
    w("`is_terminal = False`; **ein Reproduktionsversuch mit anderer Terminalbreite steht")
    w("vor ANDEREM ROHTEXT** — die Befundmenge ist dieselbe, ihre Zeilenaufteilung nicht.")
    w("")
    w("**Weitere Umgebungsparameter, durchgezogen (Spezifikation §1.4):** Graphmodus —")
    w("**K1** `full` bei `CYCLE`, sonst `diff`; **K2/K3** immer `diff`; **K4/K5** kennen")
    w("den Schalter nicht (`n/a`).")
    w("")
    w("---")
    w("")

    # ---------------------------------------------------------------- T8 --------------
    w("## T8 — Ausdrucksmächtigkeit der Baselines")
    w("")
    w("**Benötigte Harness-Ausgabe: keine.** Die Tabelle steht vor der Messung fertig da;")
    w("die Harness **liest** sie, sie schreibt sie nicht. Sie ist die **Begründung jedes")
    w("` — `** in T2, T4 und T5 und enthält **Werkzeugeigenschaften, keine Messergebnisse**.")
    w("")
    w("| Szenario | K1 | K4 | K5 | K2/K3 | Beleg |")
    w("|---|---|---|---|---|---|")
    for scenario in SCENARIO_ORDER:
        soll = T1_SOLL[scenario]
        def mark(cfg: str) -> str:
            if (cfg, scenario) in DASH_CELLS:
                return "**nicht ausdrückbar**"
            return {"ja": "ausdrückbar", "teilweise": "**teilweise**",
                    "nein": "**nicht ausdrückbar**"}[soll[cfg]]
        beleg = ("**abgeleitet, nicht gemessen**" if scenario == "SIGNATURE_DEVIATION"
                 else "gemessen")
        w(f"| `{scenario}` | {mark('K1')} | {mark('K4')} | {mark('K5')} | {mark('K2')} | {beleg} |")
    w("")
    w("**`SIGNATURE_DEVIATION` ist die einzige nicht gemessene Zeile der Erwartungsmatrix.**")
    w("")
    w("---")
    w("")

    # ---------------------------------------------------------------- T9 --------------
    w("## T9 — Begleitmeldungen und vorhergesagte Falschmeldungen")
    w("")
    w("Alle Fälle: **getrennt geführt**, **kein False Positive**, **gesondert")
    w("ausgewiesen** — und **vor** der allgemeinen FP/FN-Berechnung abgefangen, sonst")
    w("würden sie doppelt gezählt (Auswertungsspezifikation §5, Schlussabsatz).")
    w("")
    # The skeleton's shape is the specification: SEVEN rows with SEVEN different numbers
    # and SEVEN columns, the last one `vorregistriert in`. Cases 4, 5 and 6 carry the
    # path `K2/K3` in ONE row -- the first evaluation run rendered one row per (case,
    # configuration) and thereby printed the numbers 4, 5 and 6 twice (C11a §5).
    w("| # | Fall | Pfad | Betroffen | Häufigkeit | Buchungsregel | vorregistriert in |")
    w("|---|---|---|---|---|---|---|")
    co = result["co_findings"]
    blind = not result["with_campaign"]

    def co_count(config: str, ids: set[str]) -> str:
        if blind:
            return EMPTY
        hits = [c for c in co if c["config"] == config and c["injection"] in ids]
        runs = len({(c["injection"], c.get("run_index")) for c in hits})
        # A computed zero is printed as 0 (R2), never as an empty cell.
        return f"{num(len(hits))} Records / {num(runs)} Läufe"

    cyc = {i for i, r in result["injections"].items() if r["category_l1"] == "CYCLE"}
    lbc = {i for i, r in result["injections"].items() if r["scenario_l2"] == "LAYER_BACK_CALL"}
    fbr = {i for i, r in result["injections"].items()
           if r["category_l1"] == "FORBIDDEN_RELATION"}
    prereg = result["preregistered"]

    def class_count(config: str, name: str) -> int:
        return len([p for p in prereg
                    if p["config"] == config and p.get("special_class") == name])

    w(f"| 1 | `CYCLE`-Injektion (Modus `full`) erzeugt zusätzlich `layer-violation` auf "
      f"derselben Kante | K1 | {', '.join(sorted(cyc))} | {co_count('K1', cyc)} | "
      "`expected_co_findings` im Manifest; **kein FP** | Protokoll §4 Am. 13.08. (a) |")
    w(f"| 2 | `FORBIDDEN_RELATION`-Injektion (Modus `diff`) erzeugt **keinen** "
      f"`cycle`-Record | K1 | {', '.join(sorted(fbr))} | **Nullerwartung** | ein "
      "`cycle`-Record wäre ein **Befund** | DDR M.2 Festlegung 2; §3 Nachtrag Rev. 29 |")
    w(f"| 3 | `LAYER_BACK_CALL` wird von K4 **zweifach** gemeldet (`layers` **und** "
      f"`acyclic_siblings`) | K4 | {', '.join(sorted(lbc))} | {co_count('K4', lbc)} | "
      "vorregistrierte Doppelmeldung, **nicht wegkonfigurierbar**, **kein FP** | "
      "Protokoll §4 Am. 13.08. (a)/(c) |")

    control_rows = {}
    for config in LLM_CONFIGS:
        for row in result["preregistered_control"][config]:
            number = 4 if "Adapterfassade" in row["label"] else 5
            control_rows.setdefault(number, {"label": row["label"], "per": {}})
            control_rows[number]["per"][config] = (
                EMPTY if blind else f"{num(row['runs_with'])}/{num(row['runs_total'])}")
    for number, source in ((4, "Protokoll §5 Nachtrag Rev. 16"),
                           (5, "Protokoll §5 Nachtrag Rev. 18")):
        entry = control_rows.get(number)
        label = entry["label"] if entry else ("Adapterfassade `depot.core.adapters` "
                                              "(`R-PROTECT-1`)" if number == 4 else
                                              "Nicht-Träger-Portregel auf `orders_services`")
        per = entry["per"] if entry else {}
        freq = EMPTY if blind else " · ".join(
            f"{cfg} {per.get(cfg, num(0) + '/' + num(0))} Läufe" for cfg in LLM_CONFIGS)
        w(f"| {number} | {label} | K2/K3 | Kontrollset | {freq} | vorhergesagt, **kein** "
          f"unerwarteter FP | {source} |")

    # Case 6 is counted from the NAMED pre-registered class, not from the mixed bucket of
    # every wrong-category record: the pre-registration names `FORBIDDEN_RELATION`, and
    # widening it would remove false positives it never removed (see `is_case_6`).
    freq6 = EMPTY if blind else " · ".join(
        f"{cfg} {num(class_count(cfg, 'T9-6'))}" for cfg in LLM_CONFIGS)
    other6 = [s for s in result["specials"]
              if s["config"] in LLM_CONFIGS and s["injection"] in cyc]
    note6 = ""
    if other6 and not blind:
        kinds = sorted({f"{s['config']}/{s['category']}" for s in other6})
        note6 = (f" · **daneben {num(len(other6))} Records** am selben Modul mit anderer "
                 f"Kategorie ({', '.join(kinds)}) — **nicht** Fall 6, sie fallen unter die "
                 "Allgemeinregel **FP *und* FN**")
    w(f"| 6 | `CYCLE`: K2/K3 melden `FORBIDDEN_RELATION` am **richtigen Modul** | K2/K3 | "
      f"{', '.join(sorted(cyc))} | {freq6} | **kein** Treffer für `CYCLE` (Zelle bleibt "
      f"`nein`), **kein** FP; in `localized` als „richtige Stelle, falsche Kategorie“"
      f"{note6} | Protokoll §4 Am. 13.08. (f) |")

    freq7 = EMPTY if blind else num(class_count("K5", "T9-7"))
    w(f"| 7 | `CYCLE_*`: K5 meldet die Rückkante als **nicht gelistete Kante**, nicht als "
      f"Zyklus | K5 | {', '.join(sorted(cyc))} | {freq7} | `strict`: kein Treffer "
      "(Kategoriesegment weicht ab) · `localized`: Treffer auf der **Stelle**, Klasse "
      "„richtige Stelle, falsche Kategorie“ — **ohne neue Regel** gebucht | "
      "Protokoll §3 Fussnote 7 (B39) |")
    w("")
    w("**Die Häufigkeiten der Fälle 6 und 7 werden aus einer BENANNTEN Sonderklasse")
    w("gezählt** (`special_class`), nicht aus einem Klassifikationseimer, den sie sich mit")
    w("anderen Funden teilen. Im ersten Auswertungslauf zählte Fall 7 aus `specials`,")
    w("während die Funde in `co_findings` lagen; die Zelle blieb leer und war von einer")
    w("nicht eingesetzten Zelle nicht zu unterscheiden (C11a §2.4). **Eine gerechnete 0")
    w("wird als `0` gedruckt.**")
    w("")
    w("**Allgemeine Regel, von der die Fälle 6 und 7 die einzigen Ausnahmen sind:**")
    w("„falsche Regel/Kategorie, richtige Stelle“ → der `match_key` matcht nicht → zählt")
    w("als **FP *und* FN**.")
    w("")
    w("---")
    w("")

    # ---------------------------------------------------------------- T10 -------------
    w("## T10 — Overlap-Analyse: die Baselines gegen K2 bzw. gegen K3")
    w("")
    w("> **AUFLAGE IM KOPF DER TABELLE.** **K2 und K3 werden NICHT zu „dem LLM-Pfad“")
    w("> vereinigt** — je Konfiguration eine eigene Zeilengruppe, dieselbe Auflage wie in")
    w("> T2 und T5. **Die Baselineseite IST eine Vereinigung** — K1 ∪ K4 ∪ K5 — und heisst")
    w("> hier so; jede Zelle nennt, **welche** Konfigurationen den Zustand tragen.")
    w("> **Eine Injektion, die eine Seite nach T8 nicht AUSDRÜCKEN kann, ist dort NICHT")
    w("> verfehlt** und wird **nie** als „nur die andere Seite“ gebucht (Auflage (3),")
    w("> G2-Reframing/B17). `n. b.`, `n. e.` und die vorregistrierten Sonderklassen **T9")
    w("> Fall 6/7** sind **weder Treffer noch Verfehlung** (Auflage (4)).")
    w("")
    w("**Quelle: die bereits gerechneten Trefferzellen aus T2/T4 und die vorregistrierte")
    w("Ausdrucksmächtigkeit aus T8. Keine neue Metrik, keine neue Schwelle, kein neuer")
    w("Nenner** (Protokoll §8 UF3, Rev. 44; Auswertungsspezifikation §8 Punkt 10).")
    w("**Weicht T10 von T2 ab, ist T10 falsch — nicht T2.**")
    w("")
    for metric, label, name in (("localized", "`localized`", "T10a"),
                                ("strict", "`strict`", "T10b")):
        w(f"### {name} — Metrik {label}")
        w("")
        w(f"| Gruppe | Injektion | Szenario (Ebene 2) | Baselineseite ({BASELINE_LABEL}) "
          "| LLM-Seite | Zustand |")
        w("|---|---|---|---|---|---|")
        for group in result["t10"][metric]:
            config = group["config"]
            for row in group["rows"]:
                w(f"| {config} gegen die Baselines | {row['injection']} | "
                  f"`{row['scenario_l2']}` | {row['baseline']} | {row['llm']} | "
                  f"**{row['class']}** |")
            counts, excluded = group["counts"], group["excluded"]
            spread = " · ".join(
                f"{name_} {num(counts[name_])}"
                for name_ in (T10_ONLY_BASE, f"nur {config}", T10_BOTH, T10_NEITHER))
            out_text = " · ".join(f"{name_} {num(value)}"
                                  for name_, value in excluded.items())
            w(f"| {config} gegen die Baselines | **Aggregat** | "
              f"alle {num(group['total'])} | *ausserhalb des Nenners:* {out_text} | "
              f"*Nenner = die vier Zustände* | **{spread} — Nenner "
              f"{num(group['denominator'])}** |")
        w("")
    w("**Wie die Aggregatzeile zu lesen ist.** Der **Nenner** ist die Zahl der")
    w("Injektionen in den **vier** Zuständen — `nur Baseline`, `nur K2` bzw. `nur K3`,")
    w("`beide`, `keiner`. Die Klassen daneben stehen **ausserhalb** des Nenners und")
    w("werden einzeln beziffert; eine Rate über weniger Injektionen ist eine andere Rate")
    w("(dieselbe Auflage wie T5 (2)). **Probe:** Nenner plus die vier ausgewiesenen")
    w("Klassen ergibt die Injektionszahl der Zeilengruppe.")
    w("")
    w("**Zustand je Seite, in der Reihenfolge von T5 Auflage (2):** `n. b.` und `n. e.`")
    w("(keine Messung) · ` — ` (nicht ausdrückbar, T8/T8.1) · vorregistrierte Sonderklasse")
    w("T9 Fall 6/7 · Wert 1 (Treffer) · Wert 0 (Verfehlung). Eine ` — `-Zelle, die")
    w("**zugleich** eine Sonderklasse trägt — K2/`CYCLE` und K3/`CYCLE` —, bleibt **nicht")
    w("ausdrückbar**: ` — ` ist eine Aussage über das **Werkzeug**, die Sonderklasse eine")
    w("über einen **Fund**. Eine Seite ist **Treffer**, sobald **eine** ihrer Zellen")
    w("trifft; sonst **Verfehlung**, sobald **eine** verfehlt; sonst **nicht ausdrückbar**,")
    w("wenn **alle** es sind; sonst **nicht beurteilbar**.")
    w("")
    w("> **Was T10 NICHT ist.** Kein Non-Inferiority-Test, keine Rangfolge, keine Aussage")
    w("> darüber, welche Seite die bessere ist. Sie zählt aus, **wo sich die Trefferseiten")
    w("> schneiden und wo nicht**; die Deutung gehört nach Kapitel 8.")
    w("")
    return "\n".join(out) + "\n"


# --------------------------------------------------------------------------------------
# JSON serialisation
# --------------------------------------------------------------------------------------


def to_jsonable(obj: Any) -> Any:
    if isinstance(obj, Cell):
        return obj.as_json()
    if isinstance(obj, dict):
        return {k: to_jsonable(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [to_jsonable(v) for v in obj]
    return obj


# --------------------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------------------


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--root", type=Path,
                        help="fixture root holding soll/, control-k2/, control-k3/, campaign/")
    parser.add_argument("--soll", type=Path, default=REPO / "data/soll")
    parser.add_argument("--control-k2", type=Path, default=REPO / "data/c3b-k2")
    parser.add_argument("--control-k3", type=Path, default=REPO / "data/c3b-k3")
    parser.add_argument("--campaign", type=Path, default=REPO / "data/campaign")
    parser.add_argument("--with-campaign", action="store_true",
                        help="evaluate the campaign run artifacts; without it only "
                             "journal/manifest metadata is read from the campaign (T7)")
    parser.add_argument("--json-out", type=Path)
    parser.add_argument("--markdown-out", type=Path)
    args = parser.parse_args(argv)

    if args.root:
        paths = Paths(soll=args.root / "soll", control_k2=args.root / "control-k2",
                      control_k3=args.root / "control-k3", campaign=args.root / "campaign")
    else:
        paths = Paths(soll=args.soll, control_k2=args.control_k2,
                      control_k3=args.control_k3, campaign=args.campaign)

    result = evaluate(paths, with_campaign=args.with_campaign)

    checks = []
    for iid, row in result["injections"].items():
        for config, cfg in row["configs"].items():
            for metric in ("strict", "localized"):
                checks.append((f"{iid}/{config}/{metric}", cfg[metric]))
    problems = assert_marker_discipline(checks)
    if problems:
        for problem in problems:
            print(f"MARKERVERLETZUNG: {problem}", file=sys.stderr)
        return 2

    # Control rule: every `n. e.` in T2/T4/T5 must have a counterpart in T7.3 — and T7.3
    # is now read from the hashed run manifests (C6c-a), not from the journal.
    for iid, row in result["injections"].items():
        for config, cfg in row["configs"].items():
            if cfg["strict"].marker == NE and iid not in result["t7"]["missing"][config]:
                print(f"HARNESS-FEHLER: {iid}/{config} trägt n. e. ohne T7-Beleg",
                      file=sys.stderr)
                return 2

    # R12 — no finding out of an invalid run. THE bolt against a repetition of the
    # defect C13 carried: it asks the files that were opened, not the selector.
    for problem in result["invalid_artifacts_read"]:
        print(f"UNGUELTIGES ARTEFAKT GELESEN: {problem}", file=sys.stderr)
    if result["invalid_artifacts_read"]:
        print(f"UNGUELTIGES ARTEFAKT GELESEN: "
              f"{len(result['invalid_artifacts_read'])} Artefakte ohne gültiges "
              "Laufmanifest — die Ausgabe ist nicht zu verwenden (Zusicherung R12)",
              file=sys.stderr)
        return 2

    # A cross-check that disagrees with the hashed source is a FINDING about the stock,
    # not a harness defect: it is reported here and in T7, and neither side is adapted to
    # the other. The run does NOT end -- clarifying which side is wrong is handwork
    # (order C6c-a; skeleton T7.3 building rule; protocol rev. 39).
    for divergence in t7_divergences(result):
        print(f"HARNESS-BEFUND: T7-Gegenprobe weicht ab — {divergence}", file=sys.stderr)

    violations = blindness_violations(paths.campaign)
    if not args.with_campaign and violations:
        for path in violations:
            print(f"BLINDHEITSVERLETZUNG: {path}", file=sys.stderr)
        return 3
    result["reads"] = {"total": len(READS),
                       "campaign_run_artifacts": violations}

    markdown = render(result, paths)

    # The pre-registered UF4 denominators follow from T8, not from a measurement (T5
    # auflage (1)). That makes them a checkable invariant of the computed structure: the
    # injections whose cell is NOT ` — ` must be exactly as many. Checked only on the
    # full stock -- a reduced fixture legitimately carries fewer.
    if len(result["injections"]) == 32:
        for config in CONFIGS:
            expressible = sum(
                1 for row in result["injections"].values()
                if row["configs"][config]["strict"].marker != DASH)
            if expressible != UF4_DENOMINATOR[config]:
                print(f"HARNESS-FEHLER: UF4-Nenner {config}: {expressible} ausdrückbare "
                      f"Injektionen gegen vorregistrierte {UF4_DENOMINATOR[config]} (T8)",
                      file=sys.stderr)
                return 2

    # T10: the four states plus the four excluded classes must account for EVERY
    # injection of the group. A class that swallows an injection would shrink the
    # denominator unnoticed -- the same failure mode T5 auflage (2) guards against.
    for metric, groups in result["t10"].items():
        for group in groups:
            booked = sum(group["counts"].values())
            if booked != group["total"]:
                print(f"HARNESS-FEHLER: T10/{metric}/{group['config']}: {booked} "
                      f"gebuchte Injektionen gegen {group['total']} der Zeilengruppe",
                      file=sys.stderr)
                return 2

    # R1: no marker-free empty cell, over ALL tables. Only with --with-campaign: without
    # it an empty cell IS the skeleton marker *(leer)* and is correct.
    if args.with_campaign:
        empties = table_empty_cells(markdown)
        if empties:
            for problem in empties:
                print(f"LEERZELLE: {problem}", file=sys.stderr)
            print(f"LEERZELLE: {len(empties)} markerfreie Leerzellen — die Ausgabe ist "
                  "nicht zu verwenden (Zusicherung R1)", file=sys.stderr)
            return 2

    # R10: no bare marker, no exponent notation. Unlike R1 this runs on EVERY run --
    # a marker and a number render the same way with and without `--with-campaign`, so
    # there is no reason to exempt the blind run. R10 is the third assertion, after R1
    # (empty cell) and R2 (computed zero); R3-R9 are the C11a/C11b REPAIR numbers and are
    # deliberately not reused here.
    defects = table_render_defects(markdown)
    if defects:
        for problem in defects:
            print(f"DARSTELLUNG: {problem}", file=sys.stderr)
        print(f"DARSTELLUNG: {len(defects)} Darstellungsverletzungen — die Ausgabe ist "
              "nicht zu verwenden (Zusicherung R10)", file=sys.stderr)
        return 2

    if args.markdown_out:
        args.markdown_out.write_text(markdown, encoding="utf-8")
    else:
        sys.stdout.write(markdown)
    if args.json_out:
        args.json_out.write_text(
            json.dumps(to_jsonable(result), indent=1, ensure_ascii=False) + "\n",
            encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
