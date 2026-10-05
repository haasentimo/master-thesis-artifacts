#!/usr/bin/env python3
"""Generate the target model ("Soll") of the conformance campaign as an Ilograph document.

Phase 04, step 4c. The file this writes is a frozen measurement input: its SHA256 goes into
every log line as `topology_sha256` (protocol §1), so the run must be byte-reproducible.

Two sources, deliberately separate:

  * the FILE TREE of the test repository at tag `baseline` decides WHICH modules exist,
  * `docs/planung/c1_modulliste.md` §1 decides WHICH COMPONENT each module belongs to.

The component is not derivable from the path (`c1_modulliste.md` §D.11): the five empty
package modules `depot`, `depot.core`, `depot.identity`, `depot.orders` and `depot.billing`
belong to the component `core` although three of them sit outside `src/depot/core/**`.

On top of the file tree come the FOUR PHANTOM ENTRIES — the target locations of the
`INCORRECT_LOCATION` injections I25-I28. They are listed here explicitly rather than derived,
because the Soll has to cover the whole measurement space, not one state (protocol §2,
amendment 12.08., point (1)); each inherits the component of its clean location (protocol §2,
addendum 13./14.08. (a)).

Output format is not invented here — it is the shape `resolveTopology` compiles and the shape
of the shipped fixture `packages/triton-conformance/examples/bookshop/soll.ilograph.yaml`:
components are the resources that appear as endpoints of `perspectives[].relations`, every
resource nested under a component is one of its modules, and the relations are the allowed-edge
whitelist. Written by hand rather than through a YAML dumper so the byte layout is ours.

Usage:
    tools/generate_soll.py [--testrepo DIR] [--rev baseline] [--out FILE]
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_TESTREPO = Path.home() / "Schreibtisch" / "ma-conformance-testrepo"
DEFAULT_OUT = REPO_ROOT / "data" / "soll" / "depot_soll.ilograph.yaml"
MODULLISTE = REPO_ROOT / "docs" / "planung" / "c1_modulliste.md"

# The four phantom entries, EXPLICIT (protocol §2, addendum 13./14.08. (a)). Component inherited
# from the clean location; the target is a direct child of the context package (§3 am. (g)).
PHANTOMS: list[tuple[str, str, str]] = [
    # (injection, phantom module, inherited component)
    ("I25", "depot.orders.legacy_order_index", "orders_repository"),
    ("I26", "depot.billing.legacy_invoice_index", "billing_repository"),
    ("I27", "depot.identity.legacy_token_index", "identity_repository"),
    ("I28", "depot.billing.legacy_tax_models", "billing_models"),
]

CONTEXTS = ("identity", "orders", "billing")

# Whitelist of the Soll, `c1_komponentenschnitt.md` §4 (rev. 2). Only listed edges are allowed.
# Templates over `<k>` are expanded per context; the count is asserted below.
RELATION_TEMPLATES = [
    ("{k}_api", "{k}_services"),            # §4.1 spine
    ("{k}_services", "{k}_repository"),     # §4.1 spine
    ("{k}_repository", "{k}_models"),       # §4.1 spine
    ("{k}_mappers", "{k}_models"),          # §4.1 model of the original system
    ("{k}_api", "{k}_mappers"),             # §4.1 S->T of the cycle pair
    ("{k}_api", "core"),                    # §4.1 added rev. 2
    ("{k}_services", "core"),               # §4.2 ports and errors
    ("{k}_repository", "core"),             # §4.2 ports
    ("{k}_models", "core"),                 # §4.2 base types
    ("{k}_mappers", "core"),                # §4.2 errors
    ("{k}_services", "core_adapters"),      # §4.2 access through the facade
]
RELATIONS_FIXED = [
    ("core_adapters", "core"),                          # §4.2
    ("core_adapters", "core_adapters_internal"),        # §4.2 the only edge into the internals
    ("orders_services", "identity_services"),           # §4.3
    ("billing_services", "identity_services"),          # §4.3
    ("orders_services", "orders_services_pricing"),     # §4.4 S->T of the parent/child pair
    ("orders_services_pricing", "core"),                # §4.4
]
EXPECTED_RELATIONS = 39
EXPECTED_COMPONENTS = 19


def whitelist() -> list[tuple[str, str]]:
    edges = [
        (src.format(k=k), dst.format(k=k)) for k in CONTEXTS for src, dst in RELATION_TEMPLATES
    ]
    edges += RELATIONS_FIXED
    if len(edges) != EXPECTED_RELATIONS:
        sys.exit(f"whitelist: expected {EXPECTED_RELATIONS} relations, built {len(edges)}")
    return sorted(set(edges))


def module_of(path: str) -> str:
    """Map a repo-relative .py path to its dotted module name (`pythonCodeModel.ts:70-80`)."""
    rel = path[len("src/"):] if path.startswith("src/") else path
    if rel.endswith("/__init__.py"):
        rel = rel[: -len("/__init__.py")]  # a package maps to the PACKAGE name (protocol §2 (6))
    elif rel.endswith(".py"):
        rel = rel[: -len(".py")]
    return rel.replace("/", ".")


def tree_modules(testrepo: Path, rev: str) -> list[str]:
    out = subprocess.run(
        ["git", "-C", str(testrepo), "ls-tree", "-r", "--name-only", rev],
        capture_output=True, text=True, check=True,
    ).stdout.splitlines()
    return sorted(module_of(p) for p in out if p.endswith(".py"))


def modulliste() -> tuple[dict[str, str], dict[str, str]]:
    """Read module -> component out of `c1_modulliste.md` §1. Returns (files, phantom rows)."""
    text = MODULLISTE.read_text(encoding="utf-8")
    start = text.index("## 1. Modulliste")
    section = text[start: text.index("\n## ", start + 1)]
    files: dict[str, str] = {}
    phantoms: dict[str, str] = {}
    for line in section.splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip().strip("`") for c in line.split("|")[1:-1]]
        if len(cells) < 3 or cells[0] in ("Dateipfad (ab `src/`)", "Dateipfad (ab src/)"):
            continue
        if set(cells[0]) <= set("-: "):
            continue
        path, module, component = cells[0], cells[1], cells[2]
        (phantoms if path == "—" else files)[module] = component
    if not files:
        sys.exit("modulliste: parsed no rows from §1 — table shape changed?")
    return files, phantoms


def render(components: dict[str, list[str]], edges: list[tuple[str, str]], rev: str) -> str:
    lines = [
        "# Target architecture (\"Soll\") of the conformance test repository `ma-conformance-testrepo`.",
        "#",
        "# GENERATED by tools/generate_soll.py — do not edit by hand. Regenerating from the same",
        f"# inputs reproduces this file byte for byte. Source: file tree at `{rev}` plus the",
        "# module-to-component assignment of docs/planung/c1_modulliste.md §1, plus the four",
        "# explicit phantom entries (target locations of I25-I28, protocol §2).",
        "#",
        "# Components are the resources referenced by the perspective relations; every nested",
        "# module belongs to its component. The relations are the allowed-edge whitelist",
        "# (c1_komponentenschnitt.md §4) — anything not listed is forbidden.",
        "resources:",
    ]
    for component in sorted(components):
        lines.append(f"  - id: {component}")
        lines.append(f"    name: {component.replace('_', ' ').title()}")
        lines.append("    children:")
        for module in sorted(components[component]):
            lines.append(f"      - {{ id: {module} }}")
    lines.append("")
    lines.append("perspectives:")
    lines.append("  - name: dependencies")
    lines.append("    relations:")
    for src, dst in edges:
        lines.append(f"      - {{ from: {src}, to: {dst} }}")
    return "\n".join(lines) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--testrepo", type=Path, default=DEFAULT_TESTREPO)
    ap.add_argument("--rev", default="baseline")
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = ap.parse_args()

    files, table_phantoms = modulliste()
    modules = tree_modules(args.testrepo, args.rev)

    # The file tree decides what exists, the table decides where it belongs — so both have to
    # agree. A silent mismatch here would put a wrong component into every match_key of that
    # module, or leave the module unmapped (no LLM call, no warning, no exit code).
    missing = [m for m in modules if m not in files]
    extra = [m for m in files if m not in modules]
    if missing or extra:
        sys.exit(f"tree vs. c1_modulliste §1: only in tree {missing}, only in table {extra}")

    explicit = {module: component for _, module, component in PHANTOMS}
    if explicit != table_phantoms:
        sys.exit(f"phantom list vs. c1_modulliste §1: {explicit} != {table_phantoms}")

    components: dict[str, list[str]] = {}
    for module in modules:
        components.setdefault(files[module], []).append(module)
    for _, module, component in PHANTOMS:
        components.setdefault(component, []).append(module)

    edges = whitelist()
    endpoints = {c for edge in edges for c in edge}
    if endpoints != set(components):
        sys.exit(f"components without relation: {sorted(set(components) - endpoints)}; "
                 f"relation endpoints without modules: {sorted(endpoints - set(components))}")
    if len(components) != EXPECTED_COMPONENTS:
        sys.exit(f"expected {EXPECTED_COMPONENTS} components, got {len(components)}")

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(render(components, edges, args.rev), encoding="utf-8")

    total = sum(len(v) for v in components.values())
    print(f"wrote {args.out}")
    print(f"  components : {len(components)}")
    print(f"  modules    : {total} ({len(modules)} from the file tree + {len(PHANTOMS)} phantoms)")
    print(f"  relations  : {len(edges)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
