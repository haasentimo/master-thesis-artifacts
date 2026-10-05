#!/usr/bin/env python3
"""Validate the target model ("Soll") against a working tree of the test repository.

Phase 04. Runs in C3 (clean-state audit) and as a precondition of the runner in C7, once per
injection commit — because none of the failures it looks for is visible at run time:

  * a module declared in the Soll but absent from the tree produces no warning, no report line,
    no log field and no exit code (`c1b_bericht_komponentenschnitt.md` point 7),
  * a component that appears in no relation is not a component at all for `resolveTopology`,
    and all of its modules resolve to unmapped (`topology.ts:18-49`),
  * a rule whose scope carries a typo is accepted and then never runs, and it shows up in no
    `checks_performed` line (`c1b_bericht_ruleengine_verifikation.md` §8.3),
  * a rule whose `category` carries a typo is accepted, runs, and produces a `match_key` that
    joins against nothing — visible only as recall 0 in that category, charged to the model
    (`c2a_bericht_regeldatei.md` §6d, probe B).

The import graph is read HERE, out of the code, with `ast` and top-level imports only. It is
deliberately not taken from `c1_modulliste.md`: that table is the template the Soll was
generated from, so checking one against the other would check the table against itself.

Usage:
    tools/validate_soll.py --soll data/soll/depot_soll.ilograph.yaml --testrepo DIR
        [--injection I25 | --phantoms mod,mod,...]   expected Soll-only difference
        [--expect-cycles N]                          0 on B, 1 on a CYCLE commit
        [--rules FILE]                               switches point (3a-3d) ON
"""

from __future__ import annotations

import argparse
import ast
import sys
from pathlib import Path

import yaml

# The four `INCORRECT_LOCATION` injections: clean location -> target location (protocol §2,
# addendum 13./14.08. (a)). On `B` all four targets are Soll-only; on the commit of injection X
# the target of X exists as a file and its clean location is Soll-only instead.
INCORRECT_LOCATION = {
    "I25": ("depot.orders.repository.legacy_order_index", "depot.orders.legacy_order_index"),
    "I26": ("depot.billing.repository.legacy_invoice_index", "depot.billing.legacy_invoice_index"),
    "I27": ("depot.identity.repository.legacy_token_index", "depot.identity.legacy_token_index"),
    "I28": ("depot.billing.models.legacy_tax_models", "depot.billing.legacy_tax_models"),
}

# Build rule I1 (`c1_komponentenschnitt.md` §4.6): `independence` evaluates transitively and has
# no off switch, so a chain orders -> shared -> billing would be reported in a commit whose
# injection has nothing to do with INDEPENDENCE.
I1_SOURCES = {"core", "core_adapters", "core_adapters_internal"}
I1_SOURCE_PREFIX = "identity_"
I1_TARGET_PREFIXES = ("orders_", "billing_")

# Z2' (i): the source of the clean edge must sort BEFORE the target in code-unit order, or the
# carrier of the CYCLE record is not predictable without simulating the traversal
# (`c1_komponentenschnitt.md` §4.5, `ruleEngine.ts:99-135`).
CYCLE_PAIRS = [
    ("identity_api", "identity_mappers"),
    ("orders_api", "orders_mappers"),
    ("billing_api", "billing_mappers"),
    ("orders_services", "orders_services_pricing"),
]

# The six level-1 violation types of protocol §3. `category` is the FIRST segment of the
# `match_key` (`matchKey.ts:26`), and neither `parseArchitectureRules` (`rules.ts:67`, any
# non-empty string) nor the scope check catches a typo in it: it surfaces only as a silent
# miss in the eval join, i.e. as recall 0 in the affected category, charged to the model.
# Hence point (3c) — see c2a report §6d, probe B.
LEVEL1_CATEGORIES = {
    "ABSENCE_REQUIRED",
    "API_CONTRACT",
    "CYCLE",
    "FORBIDDEN_RELATION",
    "FORBIDDEN_SIGNATURE_TYPE",
    "STRUCTURAL_PLACEMENT",
}

# Z2' (ii): each of these must have exactly one importing component.
SOLE_IMPORTER = [
    "identity_mappers",
    "orders_mappers",
    "billing_mappers",
    "orders_services_pricing",
    "core_adapters_internal",
]


class Report:
    def __init__(self) -> None:
        self.failed = False

    def point(self, number: int, title: str) -> None:
        print(f"\n[{number}] {title}")

    def line(self, text: str) -> None:
        print(f"      {text}")

    def result(self, ok: bool, actual: str) -> None:
        print(f"  {'OK  ' if ok else 'FAIL'} {actual}")
        if not ok:
            self.failed = True

    def skipped(self, why: str) -> None:
        print(f"  SKIP {why}")


# ── inputs ───────────────────────────────────────────────────────────────────────────────────

def load_soll(path: Path) -> tuple[dict[str, str], dict[str, list[str]], set[tuple[str, str]]]:
    """Return (module -> component, component -> modules, allowed component edges).

    Mirrors `resolveTopology`: components are the endpoints of the perspective relations, every
    resource nested under a component is one of its modules.
    """
    doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    relations = [r for p in doc.get("perspectives") or [] for r in p.get("relations") or []]
    edges = {(r["from"], r["to"]) for r in relations if r.get("from") and r.get("to")}
    components = {c for edge in edges for c in edge}

    module_to_component: dict[str, str] = {}
    declared: dict[str, list[str]] = {}
    for resource in doc.get("resources") or []:
        rid = resource.get("id") or resource.get("name")
        children = [c.get("id") or c.get("name") for c in resource.get("children") or []]
        declared[rid] = children
        for child in children:
            module_to_component[child] = rid
    return module_to_component, declared, edges


def module_of(rel_path: str) -> str:
    rel = rel_path[len("src/"):] if rel_path.startswith("src/") else rel_path
    if rel.endswith("/__init__.py"):
        rel = rel[: -len("/__init__.py")]
    elif rel.endswith(".py"):
        rel = rel[: -len(".py")]
    return rel.replace("/", ".")


def read_import_graph(testrepo: Path) -> tuple[set[str], set[tuple[str, str]]]:
    """Parse every .py under `src/` and return (modules, top-level module-level import edges)."""
    modules: set[str] = set()
    edges: set[tuple[str, str]] = set()
    for path in sorted((testrepo / "src").rglob("*.py")):
        rel = path.relative_to(testrepo).as_posix()
        module = module_of(rel)
        modules.add(module)
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=rel)
        for node in tree.body:  # top-level only (protocol §3, top-level import rule)
            if isinstance(node, ast.Import):
                for alias in node.names:
                    edges.add((module, alias.name))
            elif isinstance(node, ast.ImportFrom) and node.module and node.level == 0:
                for alias in node.names:
                    edges.add((module, f"{node.module}.{alias.name}"))
    return modules, edges


def component_edges(
    edges: set[tuple[str, str]], module_to_component: dict[str, str]
) -> set[tuple[str, str, str, str]]:
    """(from_component, to_component, from_module, to_module) for mapped, cross-component edges.

    Unmapped targets are external (`typing`, `sqlalchemy.orm`) and carry no component edge;
    `from == to` produces no record either (`ruleEngine.ts:47`).
    """
    out = set()
    for src_module, dst_module in edges:
        src = module_to_component.get(src_module)
        dst = module_to_component.get(dst_module)
        if src is None or dst is None or src == dst:
            continue
        out.add((src, dst, src_module, dst_module))
    return out


def strongly_connected(nodes: set[str], edges: set[tuple[str, str]]) -> list[list[str]]:
    """Tarjan; returns the components of size > 1. ponytail: 19 nodes, recursion is fine."""
    adjacency: dict[str, list[str]] = {n: [] for n in nodes}
    for src, dst in edges:
        adjacency[src].append(dst)
    index: dict[str, int] = {}
    low: dict[str, int] = {}
    stack: list[str] = []
    on_stack: set[str] = set()
    found: list[list[str]] = []
    counter = [0]

    def visit(node: str) -> None:
        index[node] = low[node] = counter[0]
        counter[0] += 1
        stack.append(node)
        on_stack.add(node)
        for nxt in sorted(adjacency[node]):
            if nxt not in index:
                visit(nxt)
                low[node] = min(low[node], low[nxt])
            elif nxt in on_stack:
                low[node] = min(low[node], index[nxt])
        if low[node] == index[node]:
            group = []
            while True:
                top = stack.pop()
                on_stack.discard(top)
                group.append(top)
                if top == node:
                    break
            if len(group) > 1:
                found.append(sorted(group))

    for node in sorted(nodes):
        if node not in index:
            visit(node)
    return sorted(found)


def order_evidence(smaller: str, larger: str) -> str:
    """Position and code point of the character that decides the code-unit comparison."""
    for i, (a, b) in enumerate(zip(smaller, larger)):
        if a != b:
            return f"Pos {i}: '{a}'(0x{ord(a):02X}) < '{b}'(0x{ord(b):02X})"
    if len(smaller) < len(larger):
        return f"prefix: '{smaller}' is a proper prefix, {len(larger) - len(smaller)} chars shorter"
    return "identical"


# ── the eight points ─────────────────────────────────────────────────────────────────────────

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--soll", type=Path, required=True)
    ap.add_argument("--testrepo", type=Path, required=True)
    group = ap.add_mutually_exclusive_group()
    group.add_argument("--injection", choices=sorted(INCORRECT_LOCATION),
                       help="the INCORRECT_LOCATION injection this commit carries; the expected "
                            "Soll-only difference follows from it")
    group.add_argument("--phantoms", help="comma-separated expected Soll-only modules "
                                          "(default: the four target locations, i.e. commit B)")
    ap.add_argument("--expect-cycles", type=int, default=0,
                    help="expected number of cycles in the component graph (0 on B, 1 on a CYCLE commit)")
    ap.add_argument("--rules", type=Path,
                    help="rule file; PRESENCE SWITCHES POINT (3) ON — scopes (3a/3b) and "
                         "categories (3c/3d)")
    args = ap.parse_args()

    module_to_component, declared, allowed = load_soll(args.soll)
    tree_modules, raw_edges = read_import_graph(args.testrepo)
    edges = component_edges(raw_edges, module_to_component)
    components = {c for edge in allowed for c in edge}

    if args.phantoms:
        expected_soll_only = {m.strip() for m in args.phantoms.split(",") if m.strip()}
    elif args.injection:
        clean, _ = INCORRECT_LOCATION[args.injection]
        others = {t for i, (_, t) in INCORRECT_LOCATION.items() if i != args.injection}
        expected_soll_only = others | {clean}
    else:
        expected_soll_only = {t for _, t in INCORRECT_LOCATION.values()}

    r = Report()
    print(f"soll     : {args.soll}")
    print(f"testrepo : {args.testrepo}")
    print(f"expected : Soll-only {sorted(expected_soll_only)}, cycles {args.expect_cycles}")

    # (1) module list of the Soll against the file tree, in BOTH directions
    r.point(1, "Soll module list against the file tree, both directions")
    soll_modules = set(module_to_component)
    soll_only = soll_modules - tree_modules
    tree_only = tree_modules - soll_modules
    r.line(f"Soll {len(soll_modules)}, tree {len(tree_modules)}")
    r.result(soll_only == expected_soll_only,
             f"only in the Soll = {len(soll_only)} {sorted(soll_only)}, expected {sorted(expected_soll_only)}")
    r.result(not tree_only, f"only in the tree = {len(tree_only)} {sorted(tree_only)} (expected 0)")

    # (2) every component occurs in at least one relation
    r.point(2, "Every component occurs in at least one relation")
    relationless = sorted(set(declared) - components)
    r.line(f"resources declaring modules {len(declared)}, relation endpoints {len(components)}")
    r.result(not relationless, f"components without a relation = {len(relationless)} {relationless}")

    # (3) the rule file against the topology and against the level-1 encoding
    r.point(3, "rules[]: scopes against the topology, categories against protocol §3")
    if args.rules is None:
        r.skipped("switched off — no --rules given")
    else:
        raw = yaml.safe_load(args.rules.read_text(encoding="utf-8")) or {}
        rules = raw.get("rules") or []
        r.line(f"rules {len(rules)}")

        # (3a) every scoped component exists in the topology — a typo here is accepted by
        # `parseArchitectureRules` (rules.ts:60-63 checks the shape only) and the rule then
        # never runs, because `contextBuilder.ts:19` compares exactly.
        scoped = {c for rule in rules for c in (rule.get("scope") or {}).get("components") or []}
        unknown = sorted(scoped - components)
        r.result(not unknown,
                 f"(3a) scoped components outside the topology = {len(unknown)} {unknown}")

        # (3b) every component is held by at least one rule — warning, not failure: an
        # unscoped component is a coverage gap, not a broken join.
        unscoped = sorted(components - scoped)
        print(f"  {'OK  ' if not unscoped else 'WARN'} (3b) components scoped by no rule = "
              f"{len(unscoped)} {unscoped}")

        # (3c) every `category` is one of the six level-1 strings, character for character.
        # FAILS the run: this is the one defect that is invisible everywhere else.
        used = [(rule.get("id"), rule.get("category")) for rule in rules]
        bad = sorted(f"{rid}={cat!r}" for rid, cat in used if cat not in LEVEL1_CATEGORIES)
        r.result(not bad, f"(3c) categories outside the level-1 encoding = {len(bad)} {bad}")

        # (3d) every level-1 category is carried by at least one rule — warning: a category
        # with no rule cannot be measured at all, but it breaks no join.
        missing = sorted(LEVEL1_CATEGORIES - {cat for _, cat in used})
        print(f"  {'OK  ' if not missing else 'WARN'} (3d) level-1 categories carried by no "
              f"rule = {len(missing)} {missing}")

    # (4) build rule I1
    r.point(4, "Build rule I1 — no edge from the shared components into orders_*/billing_*")
    violations = sorted(
        f"{src} -> {dst} ({sm} -> {dm})"
        for src, dst, sm, dm in edges
        if (src in I1_SOURCES or src.startswith(I1_SOURCE_PREFIX))
        and dst.startswith(I1_TARGET_PREFIXES)
    )
    r.result(not violations, f"I1 violations = {len(violations)} {violations}")

    # (5) Z2' (i) — order of the four cycle pairs in code-unit order
    r.point(5, "Z2' (i) — the four cycle pairs in code-unit order")
    for smaller, larger in CYCLE_PAIRS:
        r.result(smaller < larger, f"S={smaller:<17} T={larger:<25} S<T={smaller < larger}  "
                                   f"[{order_evidence(smaller, larger)}]")

    # (6) Z2' (ii) — sole importer
    r.point(6, "Z2' (ii) — sole importer per component")
    for target in SOLE_IMPORTER:
        importers = sorted({src for src, dst, _, _ in edges if dst == target})
        r.result(len(importers) == 1, f"{target:<24} importers = {len(importers)} {importers}")

    # (7) component graph of the actual state
    r.point(7, "Component graph of the actual state")
    cycles = strongly_connected(components, {(src, dst) for src, dst, _, _ in edges})
    r.result(len(cycles) == args.expect_cycles,
             f"cycles = {len(cycles)} (expected {args.expect_cycles}) {cycles}")

    # (8) no module edge outside the whitelist
    r.point(8, "No module edge outside the whitelist")
    outside = sorted(
        f"{src} -> {dst} ({sm} -> {dm})"
        for src, dst, sm, dm in edges
        if (src, dst) not in allowed
    )
    r.line(f"mapped cross-component module edges = {len(edges)}, whitelist relations = {len(allowed)}")
    r.result(not outside, f"edges outside the whitelist = {len(outside)} {outside}")

    print(f"\nRESULT: {'FAIL' if r.failed else 'OK'}")
    return 1 if r.failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
