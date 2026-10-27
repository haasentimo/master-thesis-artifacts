"""Validation of the architecture model and the serialized Ilograph document.

`validate_arch` checks the semantic contract on the ArchModel against the AST
facts (disjoint containment, completeness over substantive modules, no phantom
modules, resolvable relations) and returns named errors usable as retry
feedback. `validate_ilograph` is the structural backstop on the serialized YAML.
"""

from dataclasses import dataclass, field

from llm_arch.abstraction.schema import ArchModel


@dataclass
class ValidationResult:
    """Outcome of validating an ArchModel: a flag plus typed error messages."""

    valid: bool
    errors: list[str] = field(default_factory=list)


def validate_arch(
    arch: ArchModel,
    *,
    required_modules: set[str],
    known_modules: set[str],
) -> ValidationResult:
    """Validate module placement and relations against the AST facts.

    `required_modules` (M) is the substantive set every output must place once.
    `known_modules` is every module name in the facts (to detect phantoms).
    """
    placement: dict[str, list[str]] = {}
    for comp in arch.components:
        for module in comp.contained_modules:
            placement.setdefault(module, []).append(comp.id)

    errors: list[str] = []

    for module, comps in placement.items():
        if len(comps) > 1:
            errors.append(
                f"disjointness: module {module!r} placed in multiple "
                f"components {sorted(comps)}; model shared infrastructure as a "
                f"separate sibling component referenced via a relation instead"
            )

    for module in placement:
        if module not in known_modules:
            errors.append(f"phantom_module: {module!r} is not a real module")

    for module in sorted(required_modules - set(placement)):
        errors.append(
            f"completeness: module {module!r} is not placed in any component"
        )

    comp_ids = {comp.id for comp in arch.components}
    for rel in arch.relations:
        for end, ref in (("from", rel.from_), ("to", rel.to)):
            if ref not in comp_ids:
                errors.append(
                    f"relation: {end} {ref!r} references unknown component"
                )

    return ValidationResult(valid=not errors, errors=errors)


class IlographValidationError(Exception):
    """Raised when an Ilograph document violates the expected structure."""


def _collect_ids(resources: list[dict], seen: dict[str, int]) -> None:
    """Recursively gather resource ids (or names as fallback), counting dupes."""
    for res in resources:
        ident = res.get("id") or res.get("name")
        if not ident:
            raise IlographValidationError("resource without id or name")
        seen[ident] = seen.get(ident, 0) + 1
        children = res.get("children")
        if children:
            _collect_ids(children, seen)


def validate_ilograph(data: dict) -> None:
    """Validate a parsed Ilograph document, raising on any violation."""
    resources = data.get("resources")
    if not isinstance(resources, list) or not resources:
        raise IlographValidationError("missing non-empty top-level 'resources'")
    if "perspectives" not in data or not isinstance(data["perspectives"], list):
        raise IlographValidationError("missing 'perspectives' list")

    ids: dict[str, int] = {}
    _collect_ids(resources, ids)
    dupes = [k for k, n in ids.items() if n > 1]
    if dupes:
        raise IlographValidationError(f"duplicate resource ids: {sorted(dupes)}")

    for persp in data["perspectives"]:
        for rel in persp.get("relations", []):
            for end in ("from", "to"):
                ref = rel.get(end)
                if ref not in ids:
                    raise IlographValidationError(
                        f"relation '{end}' references unknown resource {ref!r}"
                    )
