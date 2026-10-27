"""Ilograph reader tests against the real Triton export and our own output."""

import io
from pathlib import Path

from ruamel.yaml import YAML

from llm_arch.abstraction.schema import ArchModel, Component, Relation
from llm_arch.eval import compression, fact_fidelity, read_ilograph, reduce_arch
from llm_arch.facts import extract_repo, substantive_modules
from llm_arch.ilograph import to_yaml

TRITON = Path(__file__).parent.parent / "fixtures" / "rich_repo.full.ilograph.yaml"
LAYERS = {
    "bookshop.api",
    "bookshop.application",
    "bookshop.domain",
    "bookshop.infrastructure",
}


def _load(path_or_str) -> dict:
    text = path_or_str.read_text() if isinstance(path_or_str, Path) else path_or_str
    return YAML().load(io.StringIO(text))


def test_triton_reads_modules_to_layer_components():
    res = read_ilograph(_load(TRITON))
    m2c = res.reduced.module_to_component
    assert len(m2c) == 11  # leaf modules only, artefacts ignored
    assert set(m2c.values()) == LAYERS  # decision 3: component = layer package
    assert m2c["bookshop.api.catalog_routes"] == "bookshop.api"


def test_triton_lifts_relations_to_component_edges():
    res = read_ilograph(_load(TRITON))
    assert res.reduced.component_relations == {
        ("bookshop.api", "bookshop.application"),
        ("bookshop.api", "bookshop.domain"),
        ("bookshop.application", "bookshop.domain"),
        ("bookshop.application", "bookshop.infrastructure"),
        ("bookshop.infrastructure", "bookshop.domain"),
    }
    assert res.unresolved_relations == []


def test_triton_no_unmatched_against_facts():
    facts = extract_repo("fixtures/rich_repo")
    res = read_ilograph(_load(TRITON), known_modules={f.module_name for f in facts})
    assert res.unmatched_modules == []  # Triton ids already canonical


def test_triton_is_faithful_baseline():
    # Triton transcribes imports deterministically -> perfect fact-fidelity.
    facts = extract_repo("fixtures/rich_repo")
    res = read_ilograph(_load(TRITON))
    ff = fact_fidelity(facts, res.reduced, substantive_modules(facts))
    assert ff.relation_precision == 1.0
    assert ff.relation_recall == 1.0
    assert ff.module_coverage == 1.0
    assert ff.phantom_modules == 0


def test_triton_compression():
    facts = extract_repo("fixtures/rich_repo")
    res = read_ilograph(_load(TRITON))
    c = compression(facts, res.reduced, substantive_modules(facts))
    assert c.module_count == 11
    assert c.component_count == 4
    assert c.module_compression == 11 / 4  # 2.75, structural folding
    assert c.import_edge_count == 16
    assert c.component_relation_count == 5
    assert c.relation_compression == 16 / 5  # 3.2


def test_unmatched_node_is_reported_not_dropped():
    doc = {
        "resources": [
            {"id": "comp", "name": "C", "children": [
                {"id": "real.module", "name": "real"},
                {"id": "ghost.module", "name": "ghost"},
            ]}
        ],
        "perspectives": [],
    }
    res = read_ilograph(doc, known_modules={"real.module"})
    assert res.unmatched_modules == ["ghost.module"]


def test_roundtrip_our_own_output():
    # Our Approach-2 Ilograph must read back to the same reduced model.
    arch = ArchModel(
        components=[
            Component(id="a", name="A", contained_modules=["x.one", "x.two"]),
            Component(id="b", name="B", contained_modules=["y.one"]),
        ],
        relations=[Relation(from_="a", to="b")],
    )
    res = read_ilograph(_load(to_yaml(arch)))
    assert res.reduced.module_to_component == reduce_arch(arch).module_to_component
    assert res.reduced.component_relations == reduce_arch(arch).component_relations