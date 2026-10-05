#!/usr/bin/env python3
"""Generic K4/K5 output match rules — one rule per occupied cell of table T8.

WHAT THIS MODULE IS
-------------------
Input  : the archived raw text of one K4 (`lint-imports`) or K5 (`pytest`/PyTestArch)
         invocation, exactly as the campaign runner wrote it to `*.stdout.txt`.
Output : a structured finding list — tool, cell, extracted parts, classification
         (`treffer` / `begleitmeldung` / `sonstiger_fund` / `regel_nicht_ausgewertet`).

WHAT THIS MODULE IS NOT
-----------------------
No metric, no aggregation, no comparison across runs, no precision/recall, no median.
Those belong to the harness (C6b). This module answers one question per finding:
"which pre-registered output form is this, what does it name, and does that agree with
the manifest entry of the injection this run carries?"

BLINDNESS
---------
Every pattern and every comparison rule in this file is derived from output forms that
were measured and written down BEFORE the campaign ran:

    docs/repo-kontext/c2b_bericht_k4_konfiguration.md   §B3, §B4, §B5 (g)/(h)/(i), §B6
    docs/repo-kontext/c2c_bericht_k5_konfiguration.md   §B1-§B5, §B6, §B7
    docs/repo-kontext/c2a_bericht_contract_semantik.md  §1, §2, §3, §4, §5.1
    docs/protokolle/eval_protokoll_phase04.md           §3 (footnotes 1-7), §4, §5
    docs/protokolle/c6_auswertungsspezifikation.md      §1.4, §1.5, §5, §6.1, §6.2
    data/soll/importlinter.ini, data/soll/test_architecture.py,
    data/soll/depot_soll.ilograph.yaml, data/soll/injection_manifest.json
    data/campaign/control/                              (resting state, the null form)

No file under data/campaign/k1|k2|k3|k4|k5 was read while this file was written.
See docs/repo-kontext/c6b2_bericht_matchregel.md for the per-cell derivation.

GRANULARITY
-----------
One rule per occupied cell of T8, i.e. per (tool, level-2 scenario) — not one expectation
per injection. Thirteen cells are occupied: six for K4, seven for K5. Unoccupied cells get
no rule at all; they carry ` — ` from T1/T8 and can therefore never produce a `treffer`.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass, field, asdict
from typing import Any, Iterable

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOLL_DIR = os.path.join(REPO_ROOT, "data", "soll")

# ══════════════════════════════════════════════════════════════════════════════════════
# 0 — the topology: module → component
# ══════════════════════════════════════════════════════════════════════════════════════
#
# The K4 and K5 output forms name MODULES (and, for the acyclic block, PACKAGES relative
# to an ancestor). The manifest states the expectation as a COMPONENT pair
# (`expected_edge_boundary`) plus a carrier module. The mapping between the two levels is
# the frozen target model `data/soll/depot_soll.ilograph.yaml`, whose `resources` block
# lists every module under its component — the same source from which the K5 allow lists
# were generated mechanically (c2c §B2).

_RESOURCE_ID = re.compile(r"^  - id: (?P<component>\S+)\s*$")
_CHILD_ID = re.compile(r"^      - \{ id: (?P<module>\S+) \}\s*$")


def load_topology(path: str | None = None) -> dict[str, str]:
    """Return {module: component} from the frozen Soll topology."""
    path = path or os.path.join(SOLL_DIR, "depot_soll.ilograph.yaml")
    module_to_component: dict[str, str] = {}
    component: str | None = None
    with open(path, encoding="utf-8") as handle:
        for line in handle:
            resource = _RESOURCE_ID.match(line)
            if resource:
                component = resource.group("component")
                continue
            child = _CHILD_ID.match(line)
            if child and component is not None:
                module_to_component[child.group("module")] = component
    return module_to_component


def component_of(module: str, topology: dict[str, str]) -> str | None:
    """Resolve a module name reported by K4 or K5 to its Soll component.

    Three steps, in this order, all mechanical:
      1. exact lookup — covers every module and every package module of the Soll;
      2. strip a trailing `.__init__` — PyTestArch carries an `__init__.py` as
         `<package>.__init__`, the Soll as `<package>` (c2c §B2, step 1);
      3. walk up one segment at a time — covers a module the Soll does not list at all
         (a phantom target before its injection, an external node).
    """
    if module in topology:
        return topology[module]
    if module.endswith(".__init__"):
        trimmed = module[: -len(".__init__")]
        if trimmed in topology:
            return topology[trimmed]
        module = trimmed
    parts = module.split(".")
    while len(parts) > 1:
        parts.pop()
        candidate = ".".join(parts)
        if candidate in topology:
            return topology[candidate]
    return None


# ══════════════════════════════════════════════════════════════════════════════════════
# 1 — line grammar
# ══════════════════════════════════════════════════════════════════════════════════════
#
# Every non-empty line of an archived stdout is claimed by exactly one pattern. A pattern
# is either `frame` (framing that carries no finding: banner, rules, section titles,
# summaries) or `signal` (it carries a component of a finding). A line claimed by nothing
# is counted — that count, and nothing else, is what the blind coverage check reports.

FRAME = "frame"
SIGNAL = "signal"

# ── K4 — import-linter 2.13 ───────────────────────────────────────────────────────────
#
# The thirteen contract names are read from the frozen configuration, not hard-coded, so
# that a renamed contract shows up as an uncovered line rather than as a silent miss.

_CONTRACT_NAME = re.compile(r"^name = (?P<name>.+?)\s*$")


def load_contract_names(path: str | None = None) -> list[str]:
    path = path or os.path.join(SOLL_DIR, "importlinter.ini")
    names: list[str] = []
    with open(path, encoding="utf-8") as handle:
        for line in handle:
            match = _CONTRACT_NAME.match(line)
            if match:
                names.append(match.group("name"))
    return names


# The banner import-linter prints before the report. Measured verbatim in the archived
# resting state (`data/campaign/control/k4/k4_<baseline>.stdout.txt`) and identical to
# `importlinter/application/rendering.py:TEXT_LOGO`; box-drawing glyphs only, so a real
# report line can never be swallowed by it.
_BANNER_GLYPHS = " -─│┐└┘═║╔╗╚╝╠╣╦╩╬▲▶◀"

# ── K4 line wrapping ──────────────────────────────────────────────────────────────────
#
# import-linter renders through `rich` (`importlinter/application/output.py`:
# `console = Console(highlight=False)`). A `rich` Console whose file is NOT a terminal
# falls back to a width of 80 columns, and the campaign runner captures stdout through a
# pipe (`tools/run_campaign.py:783`, `subprocess.run(..., capture_output=True)`), with no
# `COLUMNS` in the environment. Every rendered line longer than 80 columns is therefore
# WORD-WRAPPED into several physical lines. Measured on 27.08.2026 against a throwaway
# input (C6b-2a; `console.width == 80`, `is_terminal == False` under a pipe):
#
#   soft break at a word boundary — the chunk KEEPS the break space, the continuation
#   starts at column 0:
#       '- zz.ctx.repository.a_repository_module_with_a_deliberately_long_name -> '
#       'zz.ctx.services.a_service_module_with_a_deliberately_long_name (l.1)'
#
#   hard break inside a token longer than the width — the chunk is EXACTLY the width and
#   carries no trailing space, because the token itself was cut:
#       'zz.ctx.deep.aaaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggg'
#       'gghhhhhhhhhh (l.1)'
#
#   EXACT-FIT break at a word boundary — the chunk is EXACTLY the width and also carries
#   no trailing space, because the text ends flush and the break space is DROPPED:
#       '- zz.ctx.repository.exact_fit_source_module -> zz.shared.adapters.internal.xxxxx'
#       '(l.1)'
#
# The last two forms look identical from the outside: width columns, no trailing space.
# They must be reassembled DIFFERENTLY — the hard break by plain concatenation, the
# exact-fit break with the dropped space put back. The discriminator is structural and
# needs no knowledge of the content: `rich` splits a token across lines ONLY when the
# token alone does not fit the width. So if the chunk's trailing token and the
# continuation's leading token, put together, would exceed the width, the token was cut
# and the halves belong together; otherwise they are two tokens and a space was dropped.
#
# The wrap is FRAME, not content: the logical line is reassembled before matching, so a
# wrapped detail line produces exactly the finding its unwrapped form produces — never
# two, never none.

K4_CONSOLE_WIDTH = 80


def _leading_token(text: str) -> str:
    return text.split(" ", 1)[0]


def _trailing_token(text: str) -> str:
    return text.rsplit(" ", 1)[-1]


def _k4_join(chunk: str, following: str, width: int) -> str | None:
    """How does `following` continue `chunk` — or does it not?

    Returns the separator to reassemble with ("" for a cut token, " " for a dropped break
    space), or None if `following` starts a new logical line.
    """
    if not following or not following.strip():
        return None
    if following[0].isspace():
        # `rich` never indents a continuation; a leading blank means a new logical line.
        return None
    if chunk.endswith(" "):
        # Soft break with the break space retained: it fits only if the next token does
        # not. Plain concatenation restores the logical line.
        return "" if len(chunk) + len(_leading_token(following)) > width else None
    if len(chunk) != width:
        return None
    # Flush at the width and no trailing space: either a cut token or an exact fit.
    if len(_trailing_token(chunk)) + len(_leading_token(following)) > width:
        return ""   # the token itself was cut
    return " "      # the break space was dropped


def unwrap_k4(lines: list[str], width: int = K4_CONSOLE_WIDTH) -> list[tuple[str, list[int]]]:
    """Reassemble `rich`'s word-wrapped physical lines into logical lines.

    Returns (logical line, physical line numbers). A logical line that was never wrapped
    carries exactly one number, so line-number provenance survives unwrapping. The
    continuation test runs on the LAST physical fragment, not on the accumulation — a
    break is a property of the fragment, not of the reassembled line.
    """
    out: list[tuple[str, list[int]]] = []
    index = 0
    count = len(lines)
    while index < count:
        chunk = lines[index]
        logical = chunk
        numbers = [index + 1]
        while index + 1 < count:
            separator = _k4_join(chunk, lines[index + 1], width)
            if separator is None:
                break
            index += 1
            chunk = lines[index]
            logical += separator + chunk
            numbers.append(index + 1)
        out.append((logical, numbers))
        index += 1
    return out

MODULE = r"[A-Za-z_][A-Za-z0-9_.]*"

K4_PATTERNS: list[tuple[str, str, re.Pattern[str]]] = [
    # framing
    ("k4_banner", FRAME, re.compile(rf"^[{re.escape(_BANNER_GLYPHS)}]+$")),
    ("k4_rule", FRAME, re.compile(r"^-{3,}$")),
    ("k4_section_contracts", FRAME, re.compile(r"^Contracts$")),
    ("k4_section_broken", FRAME, re.compile(r"^Broken contracts$")),
    (
        "k4_analyzed",
        FRAME,
        re.compile(r"^Analyzed (?P<files>\d+) files?, (?P<deps>\d+) dependenc(?:y|ies)\.$"),
    ),
    (
        "k4_summary",
        FRAME,
        re.compile(r"^Contracts: (?P<kept>\d+) kept, (?P<broken>\d+) broken\.$"),
    ),
    (
        "k4_contract_verdict",
        SIGNAL,
        # `_build_warning_text` (rendering.py) may append " (N warning[s])".
        re.compile(r"^(?P<name>.+?) (?P<verdict>KEPT|BROKEN)"
                   r"(?: \((?P<warnings>\d+) warnings?\))?$"),
    ),
    ("k4_section_warnings", FRAME, re.compile(r"^Warnings$")),
    # detail block openers — one per contract type, measured in c2b §B4
    (
        "k4_forbidden_header",
        SIGNAL,
        re.compile(rf"^(?P<src>{MODULE}) is not allowed to import (?P<dst>{MODULE}):$"),
    ),
    (
        "k4_protected_header",
        SIGNAL,
        re.compile(rf"^Illegal imports of protected package (?P<pkg>{MODULE}):$"),
    ),
    (
        "k4_cycle_header",
        SIGNAL,
        re.compile(rf"^No cycles are allowed in (?P<pkg>{MODULE})\.$"),
    ),
    (
        "k4_cycle_intro",
        FRAME,
        re.compile(r"^It could be made acyclic by removing (?P<n>\d+) dependenc(?:y|ies):$"),
    ),
    (
        "k4_exhaustive_header",
        SIGNAL,
        re.compile(r"^The following modules are not listed as layers:$"),
    ),
    (
        "k4_exhaustive_note",
        FRAME,
        # One logical line; `rich` wraps it, and `unwrap_k4` puts it back together. Both
        # the reassembled form and the two halves are accepted, so the pattern also holds
        # for a text captured at a different console width.
        re.compile(
            r"^\(Since this contract is marked as 'exhaustive', every child of every container"
            r"(?: must be declared as a layer\.\))?$"
            r"|^must be declared as a layer\.\)$"
        ),
    ),
    # detail lines
    (
        "k4_cycle_edge",
        SIGNAL,
        re.compile(
            rf"^-\s+\.(?P<src>{MODULE}) -> \.(?P<dst>{MODULE}) \((?P<imports>\d+) imports?\)$"
        ),
    ),
    (
        "k4_edge",
        SIGNAL,
        re.compile(rf"^-\s+(?P<src>{MODULE}) -> (?P<dst>{MODULE}) \(l\.(?P<line>\d+)\)$"),
    ),
    (
        "k4_edge_chain",
        SIGNAL,
        re.compile(rf"^\s+(?P<src>{MODULE}) -> (?P<dst>{MODULE}) \(l\.(?P<line>\d+)\)$"),
    ),
    ("k4_exhaustive_module", SIGNAL, re.compile(rf"^-\s+(?P<module>{MODULE})$")),
    # configuration abort — no contract is evaluated at all (c6 spec §1.4)
    (
        "k4_config_abort",
        SIGNAL,
        re.compile(
            r"^The top level configuration must have include_external_packages=True.*$"
            r"|^Contract \".*\" is not configured correctly.*$"
            r"|^.*(?:NoSuchContractType|is not a valid|are not valid).*$"
        ),
    ),
]

# ── K5 — PyTestArch 4.0.1 under pytest 9.0.1, called with `-q` ────────────────────────
#
# Two of the forms below are documented verbatim in a pre-campaign source: the progress
# line and the count line (c2c §B4, archived resting state) and the `FAILED …` line with
# its `AssertionError` (c2c §B5, protocol §3 footnote 7). The remaining forms — the
# `FAILURES` banner, the traceback frame and the short-summary section — are pytest's own
# report grammar; NO pre-campaign source prints a complete failing K5 run verbatim. They
# are therefore derived from the tool's output grammar, not from a measured sample, and
# that is exactly what the blind coverage check of C6b-2 step 6 puts to the test.

NODEID = r"[^\s]+"

# pytest does NOT wrap: a 126-column traceback locator is written out in full (measured).
# The only length-dependent behaviour is the short summary, which drops the ` - <message>`
# half when the line would grow too long — the node id itself is never cut (measured).
#
# The traceback of a K5 failure is CHAINED, because `assert_applies` raises inside
# PyTestArch rather than in the test body. That produces three frame forms that a naive
# model misses, all measured on 27.08.2026:
#     'tw_arch_one.py:28: '                                   entry frame, no exception
#     '_ _ _ _ _ _ _ … _ '                                    frame separator
#     '/…/query_language/rule.py:212: in assert_applies'       chained frame header
# and, where an exception has a cause (`NetworkXError` from `KeyError`):
#     'The above exception was the direct cause of the following exception:'

K5_PATTERNS: list[tuple[str, str, re.Pattern[str]]] = [
    ("k5_progress", FRAME, re.compile(r"^[.FEsxXu]+\s*\[\s*\d+%\]$")),
    (
        "k5_counts",
        FRAME,
        re.compile(
            r"^(?:\d+ (?:passed|failed|error|errors|skipped|xfailed|xpassed|warning|warnings|deselected)"
            r"(?:, )?)+ in [\d.]+s.*$"
        ),
    ),
    ("k5_no_tests", FRAME, re.compile(r"^no tests ran in [\d.]+s.*$")),
    ("k5_banner", FRAME, re.compile(r"^=+ .+ =+$")),
    # The frame separator is single underscores joined by blanks; it must be claimed
    # BEFORE the test header, whose underscore runs are unbroken.
    ("k5_frame_separator", FRAME, re.compile(r"^_(?: _)+$")),
    ("k5_test_header", SIGNAL, re.compile(r"^_{2,} (?P<test>.+?) _{2,}$")),
    (
        "k5_exception_chain",
        FRAME,
        re.compile(r"^(?:During handling of the above exception, another exception occurred:"
                   r"|The above exception was the direct cause of the following exception:)$"),
    ),
    (
        "k5_assert",
        SIGNAL,
        re.compile(r"^E\s+(?P<exc>[A-Za-z_][\w.]*(?:Error|Exception|Warning)): (?P<msg>.*)$"),
    ),
    ("k5_assert_cont", SIGNAL, re.compile(r'^E\s+(?P<msg>".*)$')),
    ("k5_e_other", FRAME, re.compile(r"^E(?:\s.*)?$")),
    (
        "k5_failed_summary",
        SIGNAL,
        re.compile(r"^FAILED (?P<nodeid>" + NODEID + r")(?: - (?P<msg>.*))?$"),
    ),
    (
        "k5_error_summary",
        SIGNAL,
        re.compile(r"^ERROR (?P<nodeid>" + NODEID + r")(?: - (?P<msg>.*))?$"),
    ),
    (
        "k5_chained_frame",
        FRAME,
        re.compile(r"^(?P<file>\S+):(?P<line>\d+): in (?P<function>.+)$"),
    ),
    (
        "k5_location",
        FRAME,
        re.compile(r"^(?P<file>\S+):(?P<line>\d+): (?P<exc>[A-Za-z_][\w.]*)$"),
    ),
    ("k5_entry_frame", FRAME, re.compile(r"^(?P<file>\S+):(?P<line>\d+):$")),
    ("k5_docs_link", FRAME, re.compile(r"^-- Docs: \S+$")),
    ("k5_param", FRAME, re.compile(r"^\w+ = .*$")),
    ("k5_source", FRAME, re.compile(r"^(?:>|\s{2,}).*$")),
    ("k5_rule_line", FRAME, re.compile(r"^-{3,}.*$")),
    ("k5_warning_header", FRAME, re.compile(r"^\s*[\w./\\-]+:\d+: \w*Warning:.*$")),
]


@dataclass
class ScannedLine:
    number: int
    text: str
    pattern: str | None
    kind: str | None
    groups: dict[str, str] = field(default_factory=dict)
    # Physical source lines of this logical line. More than one only where `rich` wrapped
    # a K4 line; the first entry is always `number`.
    numbers: list[int] = field(default_factory=list)


def scan(text: str, tool: str) -> tuple[list[ScannedLine], list[int]]:
    """Claim every non-empty line with exactly one pattern.

    Returns (scanned lines, line numbers of non-empty lines claimed by no pattern).
    The second element is the ONLY thing the blind coverage check looks at.
    """
    patterns = K4_PATTERNS if tool == "K4" else K5_PATTERNS
    contract_names: set[str] = set()
    if tool == "K4":
        # The detail block of a broken contract opens with a bare repetition of the
        # contract name. Two sources for that name, both structural, neither invented:
        # the frozen configuration, and the verdict list of this very run.
        contract_names = set(load_contract_names())
        for _raw in text.splitlines():
            _line = _raw.rstrip()
            _match = re.match(r"^(?P<name>.+?) (?:KEPT|BROKEN)$", _line)
            if _match:
                contract_names.add(_match.group("name"))
    physical = [raw.rstrip("\n") for raw in text.splitlines()]
    if tool == "K4":
        logical = unwrap_k4(physical)
    else:
        # pytest does not wrap (measured); its physical lines ARE its logical lines.
        logical = [(raw, [index]) for index, raw in enumerate(physical, start=1)]

    scanned: list[ScannedLine] = []
    uncovered: list[int] = []
    for raw, numbers in logical:
        number = numbers[0]
        line = raw.rstrip()
        if not line.strip():
            scanned.append(ScannedLine(number, line, None, None, {}, numbers))
            continue
        # A bare contract title opens a detail block (c2a §2a, verbatim layout). It is
        # matched against the frozen configuration first, so that it is never mistaken
        # for a free-text message.
        if tool == "K4" and line in contract_names:
            scanned.append(
                ScannedLine(number, line, "k4_contract_title", SIGNAL, {"name": line}, numbers)
            )
            continue
        for name, kind, regex in patterns:
            match = regex.match(line)
            if match:
                groups = {k: v for k, v in match.groupdict().items() if v is not None}
                scanned.append(ScannedLine(number, line, name, kind, groups, numbers))
                break
        else:
            scanned.append(ScannedLine(number, line, None, None, {}, numbers))
            # A wrapped logical line that matches nothing counts once per PHYSICAL line,
            # so the coverage counter stays a count of lines in the archived file.
            uncovered.extend(numbers)
    return scanned, uncovered


# ══════════════════════════════════════════════════════════════════════════════════════
# 2 — raw findings: the output forms, per tool
# ══════════════════════════════════════════════════════════════════════════════════════


@dataclass
class RawFinding:
    tool: str
    form: str
    lines: list[int]
    parts: dict[str, Any]


@dataclass
class RunSummary:
    tool: str
    fields: dict[str, Any]


def parse_k4(scanned: list[ScannedLine]) -> tuple[list[RawFinding], RunSummary]:
    """Reassemble the K4 detail blocks.

    Layout, measured verbatim in c2a §2a and c2b §B4:

        Analyzed N files, M dependencies.
        ---------------------------------
        <contract name> KEPT|BROKEN            (one per contract)
        Contracts: N kept, M broken.
        ----------------
        Broken contracts
        ----------------
        <contract name>                        (title of the detail block)
        ---------------
        <detail lines of that contract>

    A broken contract may carry SEVERAL `No cycles are allowed in …` blocks, one per
    level (c2a §2.2c; c6 spec §1.4) — the blocks are collected as a list, never folded
    into one.
    """
    findings: list[RawFinding] = []
    summary: dict[str, Any] = {"verdicts": {}, "kept": None, "broken": None, "config_abort": False}
    contract: str | None = None
    pending_header: dict[str, Any] | None = None
    cycle_block: dict[str, Any] | None = None
    exhaustive_open = False
    in_detail = False

    def close_cycle_block() -> None:
        nonlocal cycle_block
        if cycle_block is not None:
            findings.append(
                RawFinding("K4", "acyclic_block", cycle_block["lines"], {
                    "contract": cycle_block["contract"],
                    "ancestor_path": cycle_block["ancestor_path"],
                    "removal_set": cycle_block["edges"],
                })
            )
            cycle_block = None

    for item in scanned:
        pattern = item.pattern
        if pattern is None:
            continue
        if pattern == "k4_analyzed":
            summary["files"] = int(item.groups["files"])
            summary["dependencies"] = int(item.groups["deps"])
        elif pattern == "k4_contract_verdict":
            summary["verdicts"][item.groups["name"]] = item.groups["verdict"]
        elif pattern == "k4_summary":
            summary["kept"] = int(item.groups["kept"])
            summary["broken"] = int(item.groups["broken"])
        elif pattern == "k4_section_broken":
            in_detail = True
        elif pattern == "k4_contract_title":
            close_cycle_block()
            contract = item.groups["name"]
            pending_header = None
            exhaustive_open = False
            in_detail = True
        elif pattern == "k4_forbidden_header":
            close_cycle_block()
            pending_header = {
                "kind": "forbidden_or_layers",
                "src_scope": item.groups["src"],
                "dst_scope": item.groups["dst"],
                "line": item.number,
            }
            exhaustive_open = False
        elif pattern == "k4_protected_header":
            close_cycle_block()
            pending_header = {
                "kind": "protected",
                "protected_package": item.groups["pkg"],
                "line": item.number,
            }
            exhaustive_open = False
        elif pattern == "k4_cycle_header":
            close_cycle_block()
            pending_header = None
            exhaustive_open = False
            cycle_block = {
                "contract": contract,
                "ancestor_path": item.groups["pkg"],
                "edges": [],
                "lines": [item.number],
            }
        elif pattern == "k4_exhaustive_header":
            close_cycle_block()
            pending_header = None
            exhaustive_open = True
        elif pattern == "k4_cycle_edge":
            if cycle_block is None:  # an edge without its header is a structural anomaly
                findings.append(RawFinding("K4", "orphan_cycle_edge", [item.number], dict(item.groups)))
                continue
            cycle_block["edges"].append({
                "source_package": f"{cycle_block['ancestor_path']}.{item.groups['src']}",
                "target_package": f"{cycle_block['ancestor_path']}.{item.groups['dst']}",
                "relative": f".{item.groups['src']} -> .{item.groups['dst']}",
                "imports": int(item.groups["imports"]),
                "line": item.number,
            })
            cycle_block["lines"].append(item.number)
        elif pattern == "k4_exhaustive_module":
            if not exhaustive_open:
                findings.append(RawFinding("K4", "orphan_module_line", [item.number], dict(item.groups)))
                continue
            findings.append(RawFinding("K4", "exhaustive_undeclared_child", [item.number], {
                "contract": contract,
                "module": item.groups["module"],
            }))
        elif pattern in ("k4_edge", "k4_edge_chain"):
            form = "protected_import" if (pending_header or {}).get("kind") == "protected" else "layer_or_forbidden_import"
            findings.append(RawFinding("K4", form, [item.number], {
                "contract": contract,
                "header": pending_header,
                "source_module": item.groups["src"],
                "target_module": item.groups["dst"],
                "code_line": int(item.groups["line"]),
                "indirect_step": pattern == "k4_edge_chain",
            }))
        elif pattern == "k4_config_abort":
            summary["config_abort"] = True
            findings.append(RawFinding("K4", "configuration_abort", [item.number], {"message": item.text}))
    close_cycle_block()
    summary["in_detail_section_seen"] = in_detail
    return findings, RunSummary("K4", summary)


_K5_IMPORTS = re.compile(r'^"(?P<src>[^"]+)" imports "(?P<dst>[^"]+)"\.$')
_K5_NOT_IMPORTS = re.compile(r'^"(?P<src>[^"]+)" does not import "(?P<dst>[^"]+)"\.$')
_K5_TESTID = re.compile(r"^(?:.*::)?(?P<func>test_\w+)(?:\[(?P<param>[^\]]+)\])?$")


def _split_testid(raw: str) -> tuple[str | None, str | None]:
    match = _K5_TESTID.match(raw.strip())
    if not match:
        return None, None
    return match.group("func"), match.group("param")


def parse_k5(scanned: list[ScannedLine]) -> tuple[list[RawFinding], RunSummary]:
    """Reassemble the K5 failures.

    One finding per violation LINE, not per failing test: the forbidding half of an
    allow-list rule evaluates per import and per module and names the guilty module in
    every line (c2b §1c/§1d, c2c §B5/§B6 — eight lines in one AssertionError).

    ONE finding block per failing test. The traceback of a K5 failure is chained, so a
    test can print SEVERAL `E   <Exc>: …` blocks — the earlier ones are the CAUSE
    (`KeyError` under `NetworkXError`, measured), the last one is the exception that
    actually failed the test. Only the last block is emitted; the causes are frame.

    `ERROR`/`NetworkXError` is kept apart from `FAILED`: for that rule NO measurement
    took place, which is not the same as a non-hit (c6 spec §1.5, §6.2).
    """
    findings: list[RawFinding] = []
    summary: dict[str, Any] = {"failed_ids": [], "error_ids": [], "collected": None}
    current_test: str | None = None
    open_block: list[tuple[str, int, str]] = []
    last_block: list[tuple[str, int, str]] = []
    block_test: str | None = None

    E_PATTERNS = {"k5_assert", "k5_assert_cont", "k5_e_other"}

    def emit(message: str, line: int, exc: str, test: str | None) -> None:
        func, param = _split_testid(test or "")
        imports = _K5_IMPORTS.match(message)
        not_imports = _K5_NOT_IMPORTS.match(message)
        if exc == "AssertionError" and imports:
            findings.append(RawFinding("K5", "allowlist_violation", [line], {
                "test_function": func,
                "test_parameter": param,
                "source_module": imports.group("src"),
                "target_module": imports.group("dst"),
                "message": message,
            }))
        elif exc == "AssertionError" and not_imports:
            findings.append(RawFinding("K5", "required_import_missing", [line], {
                "test_function": func,
                "test_parameter": param,
                "source_module": not_imports.group("src"),
                "required_module": not_imports.group("dst"),
                "message": message,
            }))
        elif exc == "AssertionError":
            findings.append(RawFinding("K5", "assertion_other", [line], {
                "test_function": func,
                "test_parameter": param,
                "message": message,
            }))
        else:
            findings.append(RawFinding("K5", "rule_not_evaluated", [line], {
                "test_function": func,
                "test_parameter": param,
                "exception": exc,
                "message": message,
            }))

    def flush() -> None:
        nonlocal last_block
        for message, line, exc in last_block:
            emit(message, line, exc, block_test)
        last_block = []

    for item in scanned:
        pattern = item.pattern
        if pattern in E_PATTERNS:
            if pattern == "k5_assert":
                open_block.append((item.groups["msg"], item.number, item.groups["exc"]))
            elif pattern == "k5_assert_cont":
                exc = open_block[-1][2] if open_block else "AssertionError"
                open_block.append((item.groups["msg"], item.number, exc))
            continue
        if open_block:
            # A block just closed; it supersedes any earlier block of the same test.
            last_block = open_block
            block_test = current_test
            open_block = []
        if pattern == "k5_test_header":
            flush()
            current_test = item.groups["test"]
        elif pattern == "k5_failed_summary":
            flush()
            summary["failed_ids"].append(item.groups["nodeid"])
            # In a full run the short summary comes last and carries its message on the
            # same line; the finding has then already been read from the FAILURES section.
            # In the excerpt form of c2c §B5 the `FAILED …` line stands directly above its
            # `E   AssertionError: …` line and is the only carrier of the test id, so it
            # opens a test context here as well.
            current_test = item.groups["nodeid"]
        elif pattern == "k5_error_summary":
            flush()
            summary["error_ids"].append(item.groups["nodeid"])
            current_test = item.groups["nodeid"]
    if open_block:
        last_block = open_block
        block_test = current_test
    flush()

    # Cross-check: the failures reassembled from the FAILURES section must cover exactly
    # the node ids of the short summary. A divergence is a structural anomaly, reported,
    # never silently resolved. Node ids that the short summary lists but the FAILURES
    # section does not name are counted, not resolved.
    from_section = {(f.parts.get("test_function"), f.parts.get("test_parameter")) for f in findings}
    from_summary = {_split_testid(nid) for nid in summary["failed_ids"] + summary["error_ids"]}
    from_summary.discard((None, None))
    summary["section_summary_agree"] = (not from_summary) or from_summary <= from_section
    return findings, RunSummary("K5", summary)


# ══════════════════════════════════════════════════════════════════════════════════════
# 3 — the thirteen cell rules
# ══════════════════════════════════════════════════════════════════════════════════════
#
# `localized` values:
#   "bildbar"  the output form names a module, the (component, module) comparison of
#              Decision Record O can be formed;
#   "n. b."    the output form structurally carries no module — protocol §4 Nachtrag
#              Rev. 30, decided, not re-opened here.
#
# `strict` values:
#   "mengenregel"  protocol §4 Rev. 7 for K4/CYCLE: hit if the named removal set contains
#                  the injected edge;
#   "vergleich"    direct comparison of the named modules against the manifest entry;
#   "nie"          the cell can never produce a strict hit: the tool finds the right
#                  place but the wrong kind/category — footnote 5 (K4) resp. footnote 7
#                  (K5). Both bookings are quoted verbatim in the report.

TREFFER = "treffer"
BEGLEIT = "begleitmeldung"
SONSTIG = "sonstiger_fund"
NICHT_AUSGEWERTET = "regel_nicht_ausgewertet"
ABBRUCH = "werkzeugabbruch"

# The `localized` verdict vocabulary, NAMED. The join in evaluate_campaign.py asks these
# names; it never compares against a literal. C11a found the first evaluation run losing
# the four K5/CYCLE findings at exactly such a literal comparison (`localized == "treffer"`
# against the value `treffer (richtige Stelle, falsche Kategorie)`) -- a defect that would
# have repeated itself at the next class the parser learns to tell apart.
LOC_TREFFER = "treffer"                                     # place AND category
LOC_STELLE = "treffer (richtige Stelle, falsche Kategorie)"  # place only, T9 case 6/7
LOC_KEIN = "kein treffer"
LOC_NB = "n. b."                                            # form carries no module (A-17)

#: every verdict that is a hit ON THE PLACE -- what `localized` books (footnote 7,
#: protocol rev. 22: "In localized: Treffer auf der Stelle").
LOCALIZED_HIT = frozenset({LOC_TREFFER, LOC_STELLE})

# The pre-registered special classes of T9, by NAME. A finding that carries one of these
# is neither a hit nor a false positive and is caught BEFORE the general FP/FN rule
# (spec §5 closing paragraph, T5 auflage (4)); its frequency belongs in T9 and nowhere
# else. Naming the class is what lets the harness book it out of the right bucket instead
# of guessing from a classification that it shares with other findings.
T9_CASE_3 = "T9-3"   # K4 reports LAYER_BACK_CALL twice (layers + acyclic_siblings)
T9_CASE_7 = "T9-7"   # K5 reports the injected back edge as a NON-LISTED EDGE, not a cycle


@dataclass
class CellRule:
    tool: str
    scenario: str
    category_l1: str
    forms: tuple[str, ...]
    strict: str
    localized: str
    contract_types: tuple[str, ...] = ()
    note: str = ""


CELL_RULES: dict[tuple[str, str], CellRule] = {
    # ── K4, six occupied cells ────────────────────────────────────────────────────────
    ("K4", "LAYER_BACK_CALL"): CellRule(
        "K4", "LAYER_BACK_CALL", "FORBIDDEN_RELATION",
        ("layer_or_forbidden_import",), "vergleich", "bildbar", ("layers",),
        note="spine contract; the acyclic block of the same run is the pre-registered "
             "double report (T9 case 3), never a hit and never a false positive",
    ),
    ("K4", "LAYER_SKIP_CALL"): CellRule(
        "K4", "LAYER_SKIP_CALL", "FORBIDDEN_RELATION",
        ("layer_or_forbidden_import",), "vergleich", "bildbar", ("forbidden",),
    ),
    ("K4", "PROTECTED_MODULE"): CellRule(
        "K4", "PROTECTED_MODULE", "FORBIDDEN_RELATION",
        ("protected_import",), "vergleich", "bildbar", ("protected",),
    ),
    ("K4", "INDEPENDENCE"): CellRule(
        "K4", "INDEPENDENCE", "FORBIDDEN_RELATION",
        ("layer_or_forbidden_import",), "vergleich", "bildbar", ("independence",),
    ),
    ("K4", "CYCLE_SIBLING"): CellRule(
        "K4", "CYCLE_SIBLING", "CYCLE",
        ("acyclic_block",), "mengenregel", LOC_NB, ("acyclic_siblings",),
        note="protocol §4 Nachtrag Rev. 30: localized is not computable for this cell",
    ),
    ("K4", "INCORRECT_LOCATION"): CellRule(
        "K4", "INCORRECT_LOCATION", "STRUCTURAL_PLACEMENT",
        ("exhaustive_undeclared_child",), "nie", "bildbar", ("layers/exhaustive",),
        note="footnote 5 — right place, wrong kind; counts in localized, never in strict",
    ),
    # ── K5, seven occupied cells ──────────────────────────────────────────────────────
    ("K5", "LAYER_BACK_CALL"): CellRule(
        "K5", "LAYER_BACK_CALL", "FORBIDDEN_RELATION",
        ("allowlist_violation",), "vergleich", "bildbar",
    ),
    ("K5", "LAYER_SKIP_CALL"): CellRule(
        "K5", "LAYER_SKIP_CALL", "FORBIDDEN_RELATION",
        ("allowlist_violation",), "vergleich", "bildbar",
    ),
    ("K5", "PROTECTED_MODULE"): CellRule(
        "K5", "PROTECTED_MODULE", "FORBIDDEN_RELATION",
        ("allowlist_violation",), "vergleich", "bildbar",
    ),
    ("K5", "INDEPENDENCE"): CellRule(
        "K5", "INDEPENDENCE", "FORBIDDEN_RELATION",
        ("allowlist_violation",), "vergleich", "bildbar",
    ),
    ("K5", "CYCLE_SIBLING"): CellRule(
        "K5", "CYCLE_SIBLING", "CYCLE",
        ("allowlist_violation",), "nie", "bildbar",
        note="footnote 7 — the back edge is reported as a non-listed edge, not as a "
             "cycle; strict no hit, localized hit on the place (T9 case 7)",
    ),
    ("K5", "CYCLE_PARENT_CHILD"): CellRule(
        "K5", "CYCLE_PARENT_CHILD", "CYCLE",
        ("allowlist_violation",), "nie", "bildbar",
        note="footnote 7, as CYCLE_SIBLING",
    ),
    ("K5", "MISSING_PORT_REFERENCE"): CellRule(
        "K5", "MISSING_PORT_REFERENCE", "ABSENCE_REQUIRED",
        ("required_import_missing",), "vergleich", "bildbar",
    ),
}

# Cells of T8 that carry ` — ` for this tool: not expressible, no rule, and therefore
# never a hit. Listed explicitly so that an unexpected finding on such a scenario is
# reported as `sonstiger_fund` rather than falling through unnoticed.
UNOCCUPIED: dict[str, tuple[str, ...]] = {
    "K4": ("CYCLE_PARENT_CHILD", "MISSING_PORT_REFERENCE", "FRAMEWORK_TYPE_IN_SIGNATURE",
           "SIGNATURE_DEVIATION"),
    "K5": ("FRAMEWORK_TYPE_IN_SIGNATURE", "INCORRECT_LOCATION", "SIGNATURE_DEVIATION"),
}


@dataclass
class ClassifiedFinding:
    tool: str
    form: str
    cell: str | None
    category_l1: str | None
    lines: list[int]
    parts: dict[str, Any]
    classification: str
    strict_eligible: bool | None
    localized: str | None
    reason: str
    #: name of the pre-registered T9 special class, or None. Set ONLY where the
    #: pre-registration names the case; it is what the harness books from.
    special_class: str | None = None


def _edge_components(boundary: str) -> tuple[str, str] | None:
    """`expected_edge_boundary` is written `<source component> -> <target component>`,
    optionally followed by a parenthesised note (the CYCLE rows carry one)."""
    head = boundary.split("(")[0].strip()
    if "->" not in head:
        return None
    source, target = (part.strip() for part in head.split("->", 1))
    return source, target


def classify(
    raw: Iterable[RawFinding],
    injection: dict[str, Any] | None,
    topology: dict[str, str],
) -> list[ClassifiedFinding]:
    """Apply the cell rule of the injection's scenario to every raw finding."""
    scenario = (injection or {}).get("scenario_l2")
    out: list[ClassifiedFinding] = []
    for finding in raw:
        rule = CELL_RULES.get((finding.tool, scenario)) if scenario else None
        out.append(_classify_one(finding, rule, injection, topology, scenario))
    return out


def _classify_one(
    finding: RawFinding,
    rule: CellRule | None,
    injection: dict[str, Any] | None,
    topology: dict[str, str],
    scenario: str | None,
) -> ClassifiedFinding:
    parts = dict(finding.parts)
    tool = finding.tool

    def result(classification: str, reason: str, strict: bool | None = False,
               localized: str | None = None,
               special_class: str | None = None) -> ClassifiedFinding:
        return ClassifiedFinding(
            tool, finding.form, rule.scenario if rule else None,
            rule.category_l1 if rule else None, finding.lines, parts,
            classification, strict, localized, reason, special_class,
        )

    # ── forms that are neither hit nor accompanying message, in any cell ──────────────
    if finding.form == "configuration_abort":
        return result(ABBRUCH, "K4 configuration abort before any contract was evaluated "
                               "(c6 spec §1.4) — no measurement for this run", None, None)
    if finding.form == "rule_not_evaluated":
        return result(NICHT_AUSGEWERTET, "K5 ERROR, not FAILED: the rule names a module that is "
                                         "not in the graph — tool abort, no statement for this "
                                         "rule (c6 spec §1.5, §6.2); never counts as FN", None, None)
    if finding.form in ("orphan_cycle_edge", "orphan_module_line", "assertion_other"):
        return result(SONSTIG, "output form recognised but not attributable to a block — "
                               "structural anomaly, reported, not resolved", None, None)

    # ── the pre-registered K4 double report on LAYER_BACK_CALL (T9 case 3) ────────────
    if tool == "K4" and finding.form == "acyclic_block" and scenario == "LAYER_BACK_CALL":
        return result(BEGLEIT, "pre-registered K4 double report: the injected back edge closes a "
                               "sibling cycle services ↔ repository and is reported by the "
                               "acyclic_siblings contract in addition to the layers contract "
                               "(protocol §4 Am. 13.08. (a)/(c); T9 case 3) — neither hit nor "
                               "false positive", None, LOC_NB, T9_CASE_3)

    if rule is None:
        return result(SONSTIG, f"no cell rule: scenario {scenario!r} is not an occupied cell of "
                               f"T8 for {tool}", None, None)
    if finding.form not in rule.forms:
        if tool == "K4" and finding.form == "acyclic_block":
            return result(SONSTIG, "acyclic_siblings block outside the cells that pre-register it "
                                   "(CYCLE_SIBLING as hit, LAYER_BACK_CALL as accompanying "
                                   "message) — reported as a separate finding", None, LOC_NB)
        return result(SONSTIG, f"output form {finding.form!r} is not the form that constitutes a "
                               f"finding in cell {tool}/{rule.scenario} "
                               f"({', '.join(rule.forms)})", None, None)

    injection = injection or {}
    carrier_module = injection.get("carrier_module")
    carrier_component = injection.get("carrier_component")
    boundary = _edge_components(injection.get("expected_edge_boundary") or "")

    # ── K4/CYCLE_SIBLING — the set rule (protocol §4 Rev. 7, c6 spec §6.1) ────────────
    if rule.strict == "mengenregel":
        edges = parts.get("removal_set") or []
        pairs = []
        for edge in edges:
            source = component_of(edge["source_package"], topology)
            target = component_of(edge["target_package"], topology)
            edge["source_component"] = source
            edge["target_component"] = target
            pairs.append((source, target))
        parts["ancestor_of_contract"] = "depot"  # `acyclic`, from data/soll/importlinter.ini
        if boundary and boundary in pairs:
            return result(TREFFER, "set rule: the removal set named in this block contains the "
                                   "injected edge, resolved against the block head "
                                   f"{parts.get('ancestor_path')!r} → component pair "
                                   f"{boundary[0]} -> {boundary[1]} (protocol §4 Rev. 7)",
                          True, LOC_NB)
        return result(SONSTIG, "set rule not satisfied: the removal set of this block does not "
                               f"contain the injected edge {boundary} — the block is reported as "
                               "a separate finding, never folded into the contract",
                      False, LOC_NB)

    # ── the direct comparisons ───────────────────────────────────────────────────────
    source_module = parts.get("source_module")
    target_module = parts.get("target_module")

    if finding.form == "exhaustive_undeclared_child":
        module = parts.get("module")
        parts["module_component"] = component_of(module or "", topology)
        if module == carrier_module:
            return result(TREFFER,
                          "the exhaustive contract names the moved module with its full dotted "
                          f"path and it equals carrier_module {carrier_module!r}. Footnote 5: "
                          "import-linter finds it namensblind, as an undeclared child, not as a "
                          "name violation — right place, wrong kind, 'zaehlt in localized anders "
                          "als in strict'. Manifest k4_match_rule (I25) states the direction: "
                          "'zaehlt in localized, nie in strict'",
                          False, LOC_TREFFER)
        return result(SONSTIG, f"undeclared child {module!r} is not the carrier module of this "
                               f"injection ({carrier_module!r})", False, LOC_KEIN)

    if finding.form == "required_import_missing":
        rule_id = parts.get("test_parameter")
        parts["expected_rule_id"] = injection.get("rule_id")
        # `data/soll/test_architecture.py` parametrises the port test over the RULE ID
        # (`test_carrier_references_the_core_ports[R-PORT-1]`), not over the module name.
        # Where the archived text carries no test id the module-sharp comparison alone
        # decides — the four port rules are bound to one carrier each (c6 spec §6.2).
        parts["rule_id_absent"] = rule_id is None
        module_ok = source_module == carrier_module
        rule_ok = rule_id is None or rule_id == injection.get("rule_id")
        if module_ok and rule_ok:
            return result(TREFFER, "K5 rule name: the parametrised test id carries the rule id of "
                                   f"the dedicated port rule ({rule_id}) and the AssertionError "
                                   f"names the carrier module {carrier_module!r} (c6 spec §6.2; "
                                   "the four port rules are bound module-sharply)", True, LOC_TREFFER)
        return result(SONSTIG, f"port rule finding on {source_module!r} / {rule_id!r} does not "
                               f"match the manifest entry ({carrier_module!r} / "
                               f"{injection.get('rule_id')!r})", False, LOC_KEIN)

    # allow-list violation (K5) and layers/forbidden/protected import (K4)
    parts["source_component"] = component_of(source_module or "", topology)
    parts["target_component"] = component_of(target_module or "", topology)
    if tool == "K5":
        parts["rule_component"] = parts.get("test_parameter")
    source_ok = source_module == carrier_module
    target_ok = bool(boundary) and parts["target_component"] == boundary[1]
    component_ok = (not carrier_component) or parts["source_component"] == carrier_component
    if tool == "K5" and parts.get("rule_component") is not None:
        component_ok = component_ok and parts["rule_component"] == carrier_component

    if source_ok and target_ok and component_ok:
        if rule.strict == "nie":
            return result(BEGLEIT,
                          "footnote 7: K5 reports the injected back edge as a NON-LISTED EDGE, "
                          "not as a cycle — 'In strict: kein Treffer (Kategoriesegment weicht "
                          "ab). In localized: Treffer auf der Stelle, Kategorie \"nicht "
                          "gelistete Kante\" statt CYCLE' (T9 case 7). Neither hit nor false "
                          "positive; booked without a new class",
                          False, LOC_STELLE, T9_CASE_7)
        return result(TREFFER,
                      "direct comparison: the detail line names the carrier module "
                      f"{carrier_module!r} and a target in component {boundary[1] if boundary else None!r} "
                      "of expected_edge_boundary (c6 spec §6.1 for K4, §6.2 for K5)",
                      True, LOC_TREFFER)
    return result(SONSTIG,
                  "the named edge does not match the manifest entry — source "
                  f"{source_module!r} vs. carrier {carrier_module!r}, target component "
                  f"{parts['target_component']!r} vs. expected "
                  f"{boundary[1] if boundary else None!r}",
                  False, LOC_KEIN)


# ══════════════════════════════════════════════════════════════════════════════════════
# 4 — public entry point
# ══════════════════════════════════════════════════════════════════════════════════════


def load_manifest(path: str | None = None) -> dict[str, dict[str, Any]]:
    path = path or os.path.join(SOLL_DIR, "injection_manifest.json")
    with open(path, encoding="utf-8") as handle:
        document = json.load(handle)
    return {entry["id"]: entry for entry in document["injections"]}


def match(text: str, tool: str, injection: dict[str, Any] | None = None,
          topology: dict[str, str] | None = None) -> dict[str, Any]:
    """Parse one archived raw text and return the structured finding list."""
    tool = tool.upper()
    if tool not in ("K4", "K5"):
        raise ValueError(f"tool must be K4 or K5, not {tool!r}")
    topology = topology if topology is not None else load_topology()
    scanned, uncovered = scan(text, tool)
    raw, summary = (parse_k4 if tool == "K4" else parse_k5)(scanned)
    classified = classify(raw, injection, topology)
    return {
        "tool": tool,
        "injection_id": (injection or {}).get("id"),
        "scenario_l2": (injection or {}).get("scenario_l2"),
        "cell_rule": asdict(CELL_RULES[(tool, (injection or {}).get("scenario_l2"))])
        if (tool, (injection or {}).get("scenario_l2")) in CELL_RULES else None,
        "run_summary": summary.fields,
        "findings": [asdict(item) for item in classified],
        "uncovered_nonempty_lines": len(uncovered),
    }


def coverage(text: str, tool: str) -> int:
    """Blind coverage check: the number of non-empty lines claimed by NO pattern.

    Returns a count and nothing else — no content, no line text, no finding list.
    """
    _, uncovered = scan(text, tool.upper())
    return len(uncovered)


# ══════════════════════════════════════════════════════════════════════════════════════
# 5 — self-test against the fixtures
# ══════════════════════════════════════════════════════════════════════════════════════
#
# Every fixture under tests/fixtures/k4k5/ is a COPY of an output documented before the
# campaign, with its provenance in the header. The header ends at the sentinel below and
# is not part of the raw text.

FIXTURE_DIR = os.path.join(REPO_ROOT, "tests", "fixtures", "k4k5")
FIXTURE_SENTINEL = "# --- RAW OUTPUT BELOW ---"


def load_fixture(name: str) -> str:
    with open(os.path.join(FIXTURE_DIR, name), encoding="utf-8") as handle:
        text = handle.read()
    marker = text.index(FIXTURE_SENTINEL) + len(FIXTURE_SENTINEL)
    return text[marker:].lstrip("\n")


# fixture, tool, injection id, expected {classification: count}, expected uncovered lines
SELFTEST_CASES: list[tuple[str, str, str | None, dict[str, int], int]] = [
    # ── K4 ────────────────────────────────────────────────────────────────────────────
    ("k4_null_control.txt", "K4", None, {}, 0),
    ("k4_neg_clean_c2b_b3.txt", "K4", None, {}, 0),
    ("k4_pos_layer_back_call.txt", "K4", "I02", {TREFFER: 1, BEGLEIT: 1}, 0),
    # C6c: the same pairing from an own run against a throwaway tree — complete
    # frame including the `Contracts: 11 kept, 2 broken.` footer and a wrapped
    # detail line, where k4_pos_layer_back_call.txt is a report excerpt.
    ("k4_pos_layer_back_call_i02_selfmade.txt", "K4", "I02", {TREFFER: 1, BEGLEIT: 1}, 0),
    ("k4_pos_layer_skip_call.txt", "K4", "I05", {TREFFER: 1}, 0),
    ("k4_pos_protected_module.txt", "K4", "I08", {TREFFER: 1}, 0),
    # Luecke L1: the c2b probe carries `order_service`, no INDEPENDENCE injection does.
    # The form is proven, the positive branch of the comparison is not — it runs
    # through the same code path as LAYER_BACK_CALL and LAYER_SKIP_CALL, which each
    # carry a documented positive case.
    ("k4_pos_independence.txt", "K4", "I10", {SONSTIG: 1}, 0),
    ("k4_pos_cycle_sibling.txt", "K4", "I14", {TREFFER: 1}, 0),
    ("k4_pos_incorrect_location.txt", "K4", "I25", {TREFFER: 1}, 0),
    ("k4_neg_cycle_parent_child.txt", "K4", "I16", {}, 0),
    ("k4_pos_cycle_sibling_full.txt", "K4", "I14", {TREFFER: 1}, 0),
    ("k4_neg_cycle_sibling.txt", "K4", "I14", {}, 0),
    ("k4_frame_indirect_chain.txt", "K4", "I02", {SONSTIG: 2}, 0),
    ("k4_frame_exhaustive_on_clean.txt", "K4", "I25", {SONSTIG: 3}, 0),
    # ── K5 ────────────────────────────────────────────────────────────────────────────
    ("k5_null_control.txt", "K5", None, {}, 0),
    ("k5_neg_clean_c2c_b4.txt", "K5", None, {}, 0),
    ("k5_pos_layer_back_call.txt", "K5", "I01", {TREFFER: 1}, 0),
    # C6c: the K5 positive pairing the harness fixture lacked — raw text and
    # manifest entry belong together, and it carries the test-id line that the
    # report excerpts above do not print (gap L2 on the positive path).
    ("k5_pos_layer_back_call_i02_selfmade.txt", "K5", "I02", {TREFFER: 1}, 0),
    ("k5_pos_layer_skip_call.txt", "K5", "I05", {TREFFER: 1}, 0),
    ("k5_pos_protected_module.txt", "K5", "I09", {TREFFER: 1}, 0),
    ("k5_pos_independence.txt", "K5", "I10", {TREFFER: 1}, 0),
    ("k5_pos_cycle_sibling.txt", "K5", "I14", {BEGLEIT: 1}, 0),
    ("k5_pos_cycle_parent_child.txt", "K5", "I16", {BEGLEIT: 1}, 0),
    ("k5_pos_missing_port_reference.txt", "K5", "I17", {TREFFER: 1}, 0),
    ("k5_probe_framework_multiline.txt", "K5", "I21", {SONSTIG: 8}, 0),
    ("k5_error_networkxerror.txt", "K5", "I25", {NICHT_AUSGEWERTET: 1}, 0),
    # ── Rahmen, selbst gemessen (C6b-2a) ──────────────────────────────────────────────
    # Wegwerfeingaben ohne Manifestbezug: es gibt keine Injektion, also greift keine
    # Zellenregel und jeder Fund ist `sonstiger_fund`. Geprueft wird hier der RAHMEN —
    # dass er vollstaendig erfasst wird und dass er weder Funde erzeugt noch unterdrueckt.
    ("k4_frame_one_broken_wrapped.txt", "K4", None, {SONSTIG: 1}, 0),
    ("k4_frame_two_broken.txt", "K4", None, {SONSTIG: 2}, 0),
    ("k4_frame_six_broken.txt", "K4", None, {SONSTIG: 6}, 0),
    ("k4_frame_hard_break.txt", "K4", None, {SONSTIG: 1}, 0),
    # C6b-2b: exact fit at the width, break space dropped — two findings, one of
    # them reassembled from two physical lines.
    ("k4_frame_exact_fit_break.txt", "K4", None, {SONSTIG: 2}, 0),
    ("k5_frame_failing_run.txt", "K5", None, {SONSTIG: 2}, 0),
    ("k5_frame_chained_error.txt", "K5", None, {SONSTIG: 4, NICHT_AUSGEWERTET: 1}, 0),
    ("k5_frame_long_nodeid.txt", "K5", None, {SONSTIG: 2}, 0),
]


def selftest(stream: Any = sys.stdout) -> int:
    """Run every fixture through the matcher. Returns the number of failed cases."""
    manifest = load_manifest()
    topology = load_topology()
    failures = 0
    width = max(len(case[0]) for case in SELFTEST_CASES)
    print(f"{'fixture':<{width}}  tool  inj   uncov  classification counts", file=stream)
    print("-" * (width + 46), file=stream)
    for name, tool, injection_id, expected, expected_uncovered in SELFTEST_CASES:
        text = load_fixture(name)
        injection = manifest[injection_id] if injection_id else None
        report = match(text, tool, injection, topology)
        counts: dict[str, int] = {}
        for finding in report["findings"]:
            counts[finding["classification"]] = counts.get(finding["classification"], 0) + 1
        uncovered = report["uncovered_nonempty_lines"]
        ok = counts == expected and uncovered == expected_uncovered
        failures += 0 if ok else 1
        rendered = ", ".join(f"{k}={v}" for k, v in sorted(counts.items())) or "(keine)"
        print(f"{name:<{width}}  {tool}    {injection_id or '  - ':<4}  {uncovered:>5}  "
              f"{rendered}   {'OK' if ok else 'ABWEICHUNG'}", file=stream)
        if not ok:
            print(f"{'':<{width}}        erwartet: "
                  f"{', '.join(f'{k}={v}' for k, v in sorted(expected.items())) or '(keine)'}, "
                  f"uncov={expected_uncovered}", file=stream)
    print("-" * (width + 46), file=stream)
    print(f"{len(SELFTEST_CASES)} Fixtures, {len(SELFTEST_CASES) - failures} OK, "
          f"{failures} Abweichungen", file=stream)
    return failures


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("path", nargs="?", help="archived raw text of one invocation")
    parser.add_argument("--tool", choices=["K4", "K5", "k4", "k5"])
    parser.add_argument("--injection", help="injection id, e.g. I14")
    parser.add_argument("--coverage-only", action="store_true",
                        help="print only the number of uncovered non-empty lines")
    parser.add_argument("--selftest", action="store_true",
                        help="run every fixture under tests/fixtures/k4k5/")
    args = parser.parse_args(argv)
    if args.selftest:
        return 1 if selftest() else 0
    if not args.path or not args.tool:
        parser.error("path and --tool are required unless --selftest is given")
    with open(args.path, encoding="utf-8") as handle:
        text = handle.read()
    if args.coverage_only:
        print(coverage(text, args.tool))
        return 0
    injection = load_manifest()[args.injection] if args.injection else None
    json.dump(match(text, args.tool, injection), sys.stdout, indent=1, ensure_ascii=False)
    print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
