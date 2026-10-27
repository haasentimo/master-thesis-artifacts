import io

import pytest
from ruamel.yaml import YAML

from llm_arch.abstraction.schema import ArchModel, Component, Relation
from llm_arch.ilograph import IlographValidationError, to_yaml, validate_ilograph

# Hand-written "correct" abstraction of the sample fixture's three layers.
SAMPLE = ArchModel(
    components=[
        Component(
            id="api",
            name="API Layer",
            kind="layer",
            role="api",
            contained_modules=["shop.api.routes"],
        ),
        Component(
            id="domain",
            name="Domain Layer",
            kind="layer",
            role="domain",
            contained_modules=["shop.domain.order"],
        ),
        Component(
            id="infra",
            name="Infrastructure Layer",
            kind="layer",
            role="infrastructure",
            contained_modules=["shop.infrastructure.repository"],
        ),
    ],
    relations=[
        Relation(from_="api", to="domain"),
        Relation(from_="api", to="infra"),
        Relation(from_="infra", to="domain"),
    ],
)


def _load(yaml_str: str) -> dict:
    return YAML().load(io.StringIO(yaml_str))


def test_roundtrip_serialize_and_validate():
    data = _load(to_yaml(SAMPLE))
    validate_ilograph(data)  # must not raise

    ids = {r["id"] for r in data["resources"]}
    assert ids == {"api", "domain", "infra"}
    # contained module surfaces as a child resource (anchor stays visible)
    api = next(r for r in data["resources"] if r["id"] == "api")
    assert api["children"][0]["id"] == "shop.api.routes"


def test_deterministic_output():
    assert to_yaml(SAMPLE) == to_yaml(SAMPLE)


def test_relation_to_unknown_resource_fails():
    bad = ArchModel(
        components=[Component(id="a", name="A")],
        relations=[Relation(from_="a", to="ghost")],
    )
    with pytest.raises(IlographValidationError):
        validate_ilograph(_load(to_yaml(bad)))


def test_duplicate_ids_fail():
    data = {
        "resources": [{"id": "x", "name": "X"}, {"id": "x", "name": "X2"}],
        "perspectives": [],
    }
    with pytest.raises(IlographValidationError):
        validate_ilograph(data)
