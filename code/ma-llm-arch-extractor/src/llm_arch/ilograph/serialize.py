"""Deterministic ArchModel -> Ilograph YAML serialization (no LLM).

Each component becomes a top-level Ilograph resource; its contained modules
become child resources (the real module-name anchors stay visible in the
diagram). Relations become a single perspective's relation list.

Output is stably sorted so that diffs between runs are clean.
"""

import io

from ruamel.yaml import YAML

from llm_arch.abstraction.schema import ArchModel

PERSPECTIVE_NAME = "Dependencies"


def to_ilograph_dict(arch: ArchModel) -> dict:
    """Build the Ilograph document as plain ordered dicts/lists."""
    resources = []
    for comp in sorted(arch.components, key=lambda c: c.id):
        resource: dict = {"id": comp.id, "name": comp.name}
        if comp.description:
            resource["subtitle"] = comp.description
        children = [
            {"id": module, "name": module}
            for module in sorted(comp.contained_modules)
        ]
        if children:
            resource["children"] = children
        resources.append(resource)

    relations = [
        {"from": rel.from_, "to": rel.to, "label": rel.kind}
        for rel in sorted(arch.relations, key=lambda r: (r.from_, r.to, r.kind))
    ]

    return {
        "resources": resources,
        "perspectives": [{"name": PERSPECTIVE_NAME, "relations": relations}],
    }


def to_yaml(arch: ArchModel) -> str:
    """Render an ArchModel to an Ilograph YAML string."""
    yaml = YAML()
    yaml.default_flow_style = False
    buf = io.StringIO()
    yaml.dump(to_ilograph_dict(arch), buf)
    return buf.getvalue()
