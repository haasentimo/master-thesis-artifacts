"""Edge-review worksheets for MANUAL labelling of ambiguous component edges.

The tool only surfaces edges with context and an empty `label` field; a human
decides each label and the tool aggregates. It must NEVER classify an edge
itself (guardrail 2) -- that would contaminate the very finding.

Two worksheets:
- missing edges (T \\ R): a real cross-component dependency the model did not
  express. Carries the underlying module imports (weight). Labels:
  `abstracted` (deliberately rolled up) vs `lost` (genuine loss).
- unbacked edges (R \\ T): a claimed relation no import backs. Carries both
  components' member modules + docstrings (context). Labels:
  `semantic-inference` vs `hallucination`.
"""

import json
from collections import Counter
from pathlib import Path

from llm_arch.eval.metrics import ReducedModel, induced_edge_witnesses
from llm_arch.facts.models import ModuleFacts

MISSING_LABELS = ("abstracted", "lost")
UNBACKED_LABELS = ("semantic-inference", "hallucination")


def _members(reduced: ReducedModel) -> dict[str, list[str]]:
    """component id -> sorted list of its member modules."""
    out: dict[str, list[str]] = {}
    for module, comp in reduced.module_to_component.items():
        out.setdefault(comp, []).append(module)
    return {comp: sorted(modules) for comp, modules in out.items()}


def _docstrings(facts: list[ModuleFacts]) -> dict[str, str]:
    """module -> first line of its docstring (context for unbacked edges)."""
    out: dict[str, str] = {}
    for fact in facts:
        doc = (fact.module_docstring or "").strip().splitlines()
        out[fact.module_name] = doc[0] if doc else ""
    return out


def build_worksheets(
    facts: list[ModuleFacts], reduced: ReducedModel
) -> dict[str, list[dict]]:
    """Build the missing- and unbacked-edge worksheets (labels left empty)."""
    witnesses = induced_edge_witnesses(facts, reduced.module_to_component)
    induced = set(witnesses)
    claimed = reduced.component_relations
    members = _members(reduced)
    docs = _docstrings(facts)

    missing = [
        {
            "from": ca,
            "to": cb,
            "witness_imports": [list(w) for w in witnesses[(ca, cb)]],
            "witness_count": len(witnesses[(ca, cb)]),
            "label": "",  # human: abstracted | lost
        }
        for (ca, cb) in sorted(induced - claimed)
    ]

    def _ctx(comp: str) -> list[dict]:
        return [{"module": m, "docstring": docs.get(m, "")} for m in members.get(comp, [])]

    unbacked = [
        {
            "from": ca,
            "to": cb,
            "from_modules": _ctx(ca),
            "to_modules": _ctx(cb),
            "label": "",  # human: semantic-inference | hallucination
        }
        for (ca, cb) in sorted(claimed - induced)
    ]

    return {"missing": missing, "unbacked": unbacked}


def write_worksheets(
    facts: list[ModuleFacts], reduced: ReducedModel, out_dir: str | Path
) -> dict[str, Path]:
    """Write both worksheets as JSON into out_dir; return the file paths."""
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    sheets = build_worksheets(facts, reduced)
    paths = {}
    for name, rows in sheets.items():
        path = out / f"{name}_edges.json"
        path.write_text(json.dumps(rows, indent=2))
        paths[name] = path
    return paths


def _tally(rows: list[dict], valid_labels: tuple[str, ...]) -> dict[str, int]:
    counts = Counter(row.get("label", "") for row in rows)
    out = {label: counts.get(label, 0) for label in valid_labels}
    out["unlabeled"] = counts.get("", 0)
    unknown = sum(
        n for lab, n in counts.items() if lab and lab not in valid_labels
    )
    out["unknown"] = unknown
    out["total"] = len(rows)
    return out


def summarize(missing_rows: list[dict], unbacked_rows: list[dict]) -> dict:
    """Aggregate a filled worksheet into the defensible breakdown."""
    return {
        "missing": _tally(missing_rows, MISSING_LABELS),
        "unbacked": _tally(unbacked_rows, UNBACKED_LABELS),
    }


def read_worksheet(path: str | Path) -> list[dict]:
    """Read a (possibly labelled) worksheet JSON back in."""
    return json.loads(Path(path).read_text())
