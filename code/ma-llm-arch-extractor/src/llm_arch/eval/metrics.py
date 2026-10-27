"""Gold-free correctness metrics over (AST facts, reduced architecture).

Both approaches are projected to the same canonical reduced form -- a
module->component map plus a set of directed component relations -- so the
identical metric functions score Approach 2 (via reduce_arch) and Triton
(via the Ilograph reader). Fact-fidelity is the strongest correctness signal;
gold similarity (ARI) is a reference signal only, never correctness.
"""

from collections import Counter
from dataclasses import dataclass, field

from llm_arch.abstraction.schema import ArchModel
from llm_arch.facts.models import ImportFact, ModuleFacts


@dataclass
class ReducedModel:
    """Canonical, tool-agnostic projection of an architecture.

    `module_to_component` maps each placed module to its component id.
    `component_relations` is the set of directed (from, to) component edges.
    """

    module_to_component: dict[str, str]
    component_relations: set[tuple[str, str]] = field(default_factory=set)


def reduce_arch(arch: ArchModel) -> ReducedModel:
    """Project an Approach-2 ArchModel onto the canonical reduced form."""
    module_to_component = {
        m: c.id for c in arch.components for m in c.contained_modules
    }
    relations = {(r.from_, r.to) for r in arch.relations}
    return ReducedModel(module_to_component, relations)


def _resolve_targets(imp: ImportFact, importer: str, known: set[str]) -> set[str]:
    """Resolve one import to the repo modules it refers to (best-effort).

    Handles absolute imports fully; relative imports are resolved against the
    importer's package on a best-effort basis (fixtures use absolute imports).
    """
    if imp.relative_level == 0:
        base = imp.module
    else:
        parent = importer.rsplit(".", imp.relative_level)[0] if "." in importer else ""
        base = f"{parent}.{imp.module}" if imp.module else parent

    targets: set[str] = set()
    if base in known:
        targets.add(base)
    for name in imp.names:
        cand = f"{base}.{name.name}" if base else name.name
        if cand in known:
            targets.add(cand)
    return targets


def induced_edge_witnesses(
    facts: list[ModuleFacts], module_to_component: dict[str, str]
) -> dict[tuple[str, str], list[tuple[str, str]]]:
    """Component edges induced by imports, each with its module-level witnesses.

    Maps every cross-component edge (ca, cb) to the sorted list of underlying
    module import edges (module_a, module_b) that caused it -- the evidence the
    edge-review worksheet needs to weigh a missing edge.
    """
    known = {f.module_name for f in facts}
    witnesses: dict[tuple[str, str], set[tuple[str, str]]] = {}
    for fact in facts:
        ca = module_to_component.get(fact.module_name)
        if ca is None:
            continue
        for imp in fact.imports:
            for target in _resolve_targets(imp, fact.module_name, known):
                cb = module_to_component.get(target)
                if cb is not None and cb != ca:
                    witnesses.setdefault((ca, cb), set()).add(
                        (fact.module_name, target)
                    )
    return {edge: sorted(wits) for edge, wits in witnesses.items()}


def induced_edges(
    facts: list[ModuleFacts], module_to_component: dict[str, str]
) -> set[tuple[str, str]]:
    """Component edges induced by real cross-component imports (directed)."""
    return set(induced_edge_witnesses(facts, module_to_component))


@dataclass
class FactFidelity:
    """How well the model's claims match the facts (all gold-free)."""

    relation_precision: float  # claimed edges backed by >=1 real import
    relation_recall: float  # real cross-component deps the model captured
    module_coverage: float  # placed substantive modules / |M|
    phantom_modules: int  # placed modules not present in the facts


def fact_fidelity(
    facts: list[ModuleFacts],
    reduced: ReducedModel,
    required_modules: set[str],
) -> FactFidelity:
    """Compute fact-fidelity metrics for one reduced model against the facts."""
    induced = induced_edges(facts, reduced.module_to_component)
    claimed = reduced.component_relations
    hit = claimed & induced

    # ponytail: with no claimed relations precision is vacuous (no false claims).
    precision = len(hit) / len(claimed) if claimed else 1.0
    recall = len(hit) / len(induced) if induced else 1.0

    placed = set(reduced.module_to_component)
    coverage = (
        len(placed & required_modules) / len(required_modules)
        if required_modules
        else 1.0
    )
    known = {f.module_name for f in facts}
    phantom = sum(1 for m in placed if m not in known)

    return FactFidelity(precision, recall, coverage, phantom)


def count_import_edges(facts: list[ModuleFacts], modules: set[str]) -> int:
    """Distinct directed import edges between substantive modules (the raw graph)."""
    known = {f.module_name for f in facts}
    edges: set[tuple[str, str]] = set()
    for fact in facts:
        if fact.module_name not in modules:
            continue
        for imp in fact.imports:
            for target in _resolve_targets(imp, fact.module_name, known):
                if target in modules and target != fact.module_name:
                    edges.add((fact.module_name, target))
    return len(edges)


@dataclass
class Compression:
    """Descriptive only -- how much was folded, NOT how well (guardrail 3)."""

    module_count: int  # substantive modules placed
    component_count: int
    module_compression: float | None  # modules per component
    import_edge_count: int  # raw module-level import edges
    component_relation_count: int
    relation_compression: float | None  # import edges per component relation


def compression(
    facts: list[ModuleFacts], reduced: ReducedModel, modules: set[str]
) -> Compression:
    """Compute descriptive compression ratios for one reduced model."""
    placed = {m: c for m, c in reduced.module_to_component.items() if m in modules}
    module_count = len(placed)
    component_count = len(set(placed.values()))
    import_edge_count = count_import_edges(facts, modules)
    relation_count = len(reduced.component_relations)

    return Compression(
        module_count=module_count,
        component_count=component_count,
        module_compression=(
            module_count / component_count if component_count else None
        ),
        import_edge_count=import_edge_count,
        component_relation_count=relation_count,
        # decision 5: None (not inf/NaN) when there are no component relations.
        relation_compression=(
            import_edge_count / relation_count if relation_count else None
        ),
    )


def _comb2(n: int) -> int:
    return n * (n - 1) // 2


def adjusted_rand_index(a: dict[str, str], b: dict[str, str]) -> float:
    """Adjusted Rand Index between two label maps, over their common keys.

    Label-invariant: only the grouping matters, not the label strings.
    Returns 1.0 for the degenerate case (no comparable items / single item).
    """
    common = sorted(set(a) & set(b))
    if len(common) < 2:
        return 1.0
    la = [a[m] for m in common]
    lb = [b[m] for m in common]
    pair = Counter(zip(la, lb))
    rows = Counter(la)
    cols = Counter(lb)

    index = sum(_comb2(v) for v in pair.values())
    sum_rows = sum(_comb2(v) for v in rows.values())
    sum_cols = sum(_comb2(v) for v in cols.values())
    expected = sum_rows * sum_cols / _comb2(len(common))
    max_index = (sum_rows + sum_cols) / 2
    denom = max_index - expected
    if denom == 0:
        return 1.0
    return (index - expected) / denom


def gold_similarity(
    module_to_component: dict[str, str], gold: dict[str, str]
) -> float:
    """ARI between a module->component map and a gold module->label map.

    This is a SIMILARITY signal to a chosen reference partition, NOT correctness.
    """
    return adjusted_rand_index(module_to_component, gold)
