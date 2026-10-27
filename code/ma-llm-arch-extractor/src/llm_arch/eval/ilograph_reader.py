"""Tool-agnostic Ilograph reader: any Ilograph YAML -> canonical ReducedModel.

Lets Triton's exported Ilograph go through the *same* metric path as our own
Approach-2 output. The only coupling between the approaches is this file format
-- no Triton code is imported.

Component level (methodological decision, provisional): a module is a LEAF in
the `children` tree; its component is its IMMEDIATE PARENT. For our output that
is the top-level component; for Triton's root->layer->module->artefact tree
that is the layer package (the top architectural grouping). Revisit this rule
for trees deeper than root->group->module once such an export appears.

Node-id normalization is provisional too: Triton ids are already canonical
dotted module names, so we only strip an artefact suffix and unify separators.
An optional alias map is the escape hatch for residual mismatches.
"""

from dataclasses import dataclass, field

from llm_arch.eval.metrics import ReducedModel


def normalize_node_id(raw_id: str, alias_map: dict[str, str] | None = None) -> str:
    """Map a raw Ilograph node id to a canonical module name (provisional)."""
    if alias_map and raw_id in alias_map:
        return alias_map[raw_id]
    nid = raw_id.split("::", 1)[0]  # drop artefact suffix, e.g. "::class:Foo"
    return nid.replace("/", ".")


@dataclass
class ReadResult:
    """A read Ilograph plus what could not be matched (never silently dropped)."""

    reduced: ReducedModel
    unmatched_modules: list[str] = field(default_factory=list)
    unresolved_relations: list[tuple[str, str]] = field(default_factory=list)


def _flatten(
    resources: list[dict],
    parent_id: str | None,
    alias_map: dict[str, str] | None,
    out: dict[str, str],
) -> None:
    """Walk the resource tree; map each leaf module to its immediate parent."""
    for node in resources:
        nid = normalize_node_id(node["id"], alias_map)
        children = node.get("children")
        if children:
            _flatten(children, nid, alias_map, out)
        else:
            # leaf == module; component == parent (or itself if a lone top node)
            out[nid] = parent_id if parent_id is not None else nid


def _resolve_endpoint(
    raw: str | None,
    module_to_component: dict[str, str],
    component_ids: set[str],
    alias_map: dict[str, str] | None,
) -> str | None:
    """Resolve a relation endpoint to a component id (module or component node)."""
    if raw is None:
        return None
    nid = normalize_node_id(raw, alias_map)
    if nid in module_to_component:
        return module_to_component[nid]
    if nid in component_ids:  # endpoint is already a component-level node
        return nid
    return None


def read_ilograph(
    data: dict,
    *,
    known_modules: set[str] | None = None,
    alias_map: dict[str, str] | None = None,
) -> ReadResult:
    """Reduce any parsed Ilograph document to a ReducedModel + unmatched report."""
    module_to_component: dict[str, str] = {}
    _flatten(data.get("resources", []), None, alias_map, module_to_component)
    component_ids = set(module_to_component.values())

    relations: set[tuple[str, str]] = set()
    unresolved: list[tuple[str, str]] = []
    for persp in data.get("perspectives", []):
        for rel in persp.get("relations", []):
            a = _resolve_endpoint(rel.get("from"), module_to_component, component_ids, alias_map)
            b = _resolve_endpoint(rel.get("to"), module_to_component, component_ids, alias_map)
            if a is None or b is None:
                unresolved.append((rel.get("from"), rel.get("to")))
            elif a != b:
                relations.add((a, b))

    unmatched_modules = (
        sorted(m for m in module_to_component if m not in known_modules)
        if known_modules is not None
        else []
    )

    return ReadResult(
        reduced=ReducedModel(module_to_component, relations),
        unmatched_modules=unmatched_modules,
        unresolved_relations=unresolved,
    )