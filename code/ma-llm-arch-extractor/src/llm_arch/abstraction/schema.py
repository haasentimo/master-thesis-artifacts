"""The abstracted architecture model the LLM must produce.

This is deliberately at an architectural altitude (layers/components and
their relations), not a 1:1 mirror of the module list (guardrail 2).
pydantic generates the JSON schema used to constrain the LLM output.
"""

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

# Closed vocabularies (rendered as JSON-schema enums to constrain the LLM).
ComponentKind = Literal["layer", "component", "service"]
ComponentRole = Literal[
    "domain",
    "application",
    "infrastructure",
    "api",
    "presentation",
    "shared",
]
RelationKind = Literal["depends_on", "uses"]


class Component(BaseModel):
    """A layer, component or service grouping one or more real modules."""

    id: str
    name: str
    kind: ComponentKind = "component"
    description: str | None = None
    role: ComponentRole | None = None
    contained_modules: list[str] = Field(
        default_factory=list,
        description="Real dotted module names from the facts (node anchors).",
    )


class Relation(BaseModel):
    """A dependency between two components, by their ids."""

    model_config = ConfigDict(populate_by_name=True)

    from_: str = Field(alias="from")
    to: str
    kind: RelationKind = "depends_on"


class ArchModel(BaseModel):
    """The full abstracted architecture: components and their relations."""

    components: list[Component]
    relations: list[Relation] = Field(default_factory=list)
