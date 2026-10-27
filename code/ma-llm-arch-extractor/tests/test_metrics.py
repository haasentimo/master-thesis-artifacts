"""Metrics tests with hand-computable values (no LLM)."""

from llm_arch.abstraction.schema import ArchModel, Component, Relation
from llm_arch.eval import (
    adjusted_rand_index,
    compression,
    count_import_edges,
    fact_fidelity,
    gold_similarity,
    induced_edges,
    reduce_arch,
)
from llm_arch.facts.models import ImportFact, ModuleFacts

# Tiny hand-built facts: a.x and a.y both import b.z; comps A={a.x,a.y}, B={b.z}.
# Real cross-component edge set T = {(A, B)}.
FACTS = [
    ModuleFacts(
        module_name="a.x",
        imports=[ImportFact(module="a.y"), ImportFact(module="b.z")],
    ),
    ModuleFacts(
        module_name="a.y",
        imports=[ImportFact(module="b.z")],
    ),
    ModuleFacts(module_name="b.z", imports=[]),
]
M = {"a.x", "a.y", "b.z"}

ARCH = ArchModel(
    components=[
        Component(id="A", name="A", contained_modules=["a.x", "a.y"]),
        Component(id="B", name="B", contained_modules=["b.z"]),
    ]
)


def test_induced_edges_directed_cross_component_only():
    assert induced_edges(FACTS, reduce_arch(ARCH).module_to_component) == {("A", "B")}


def test_precision_recall_perfect_claim():
    arch = ARCH.model_copy(update={"relations": [Relation(from_="A", to="B")]})
    ff = fact_fidelity(FACTS, reduce_arch(arch), M)
    assert ff.relation_precision == 1.0
    assert ff.relation_recall == 1.0
    assert ff.module_coverage == 1.0
    assert ff.phantom_modules == 0


def test_precision_half_on_hallucinated_edge():
    arch = ARCH.model_copy(
        update={"relations": [Relation(from_="A", to="B"), Relation(from_="B", to="A")]}
    )
    ff = fact_fidelity(FACTS, reduce_arch(arch), M)
    assert ff.relation_precision == 0.5  # (B,A) is hallucinated
    assert ff.relation_recall == 1.0


def test_recall_zero_when_no_relations_claimed():
    ff = fact_fidelity(FACTS, reduce_arch(ARCH), M)  # no relations
    assert ff.relation_recall == 0.0
    assert ff.relation_precision == 1.0  # vacuous: no false claims


def test_coverage_and_phantom():
    arch = ArchModel(
        components=[
            Component(id="A", name="A", contained_modules=["a.x", "made.up"]),
        ]
    )
    ff = fact_fidelity(FACTS, reduce_arch(arch), M)
    assert ff.module_coverage == 1 / 3  # only a.x of {a.x,a.y,b.z} placed
    assert ff.phantom_modules == 1  # made.up


def test_compression_hand_example():
    # M={a.x,a.y,b.z}; comps A={a.x,a.y}, B={b.z}; import edges a.x->a.y,
    # a.x->b.z, a.y->b.z = 3 raw edges.
    assert count_import_edges(FACTS, M) == 3

    no_rel = compression(FACTS, reduce_arch(ARCH), M)
    assert no_rel.module_count == 3
    assert no_rel.component_count == 2
    assert no_rel.module_compression == 1.5
    assert no_rel.import_edge_count == 3
    assert no_rel.component_relation_count == 0
    assert no_rel.relation_compression is None  # decision 5: no inf/NaN

    with_rel = ARCH.model_copy(update={"relations": [Relation(from_="A", to="B")]})
    c = compression(FACTS, reduce_arch(with_rel), M)
    assert c.relation_compression == 3.0  # 3 import edges folded into 1 relation


def test_ari_identical_is_one():
    p = {"1": "x", "2": "x", "3": "y"}
    assert adjusted_rand_index(p, p) == 1.0


def test_ari_is_label_invariant():
    a = {"1": "X", "2": "X", "3": "Y"}
    b = {"1": "foo", "2": "foo", "3": "bar"}  # same grouping, different labels
    assert adjusted_rand_index(a, b) == 1.0


def test_ari_zero_for_singletons_vs_one_cluster():
    a = {"1": "c", "2": "c"}
    b = {"1": "p", "2": "q"}
    assert adjusted_rand_index(a, b) == 0.0


def test_gold_similarity_uses_grouping_not_ids():
    # model uses generic ids, gold uses layer names; same partition -> 1.0
    arch = ArchModel(
        components=[
            Component(id="c1", name="C1", contained_modules=["a.x", "a.y"]),
            Component(id="c2", name="C2", contained_modules=["b.z"]),
        ]
    )
    gold = {"a.x": "left", "a.y": "left", "b.z": "right"}
    assert gold_similarity(reduce_arch(arch).module_to_component, gold) == 1.0
