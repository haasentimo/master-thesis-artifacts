"""Edge-review worksheet tests with constructed T/R sets (no LLM)."""

from llm_arch.eval import build_worksheets, read_worksheet, summarize, write_worksheets
from llm_arch.eval.metrics import ReducedModel
from llm_arch.facts.models import ImportFact, ModuleFacts

# a.x imports b.z and c.w. Components A={a.x,a.y}, B={b.z}, C={c.w}.
# Induced T = {(A,B), (A,C)}.
FACTS = [
    ModuleFacts(
        module_name="a.x",
        imports=[ImportFact(module="b.z"), ImportFact(module="c.w")],
    ),
    ModuleFacts(module_name="a.y", imports=[]),
    ModuleFacts(module_name="b.z", module_docstring="The B store.", imports=[]),
    ModuleFacts(module_name="c.w", module_docstring="The C widget.", imports=[]),
]
# Claimed R = {(A,B), (B,C)}: (A,C) is missing, (B,C) is unbacked.
REDUCED = ReducedModel(
    module_to_component={"a.x": "A", "a.y": "A", "b.z": "B", "c.w": "C"},
    component_relations={("A", "B"), ("B", "C")},
)


def test_missing_edge_carries_witness_imports():
    sheets = build_worksheets(FACTS, REDUCED)
    assert len(sheets["missing"]) == 1
    row = sheets["missing"][0]
    assert (row["from"], row["to"]) == ("A", "C")
    assert row["witness_imports"] == [["a.x", "c.w"]]
    assert row["witness_count"] == 1
    assert row["label"] == ""  # never auto-classified


def test_unbacked_edge_carries_member_context():
    sheets = build_worksheets(FACTS, REDUCED)
    assert len(sheets["unbacked"]) == 1
    row = sheets["unbacked"][0]
    assert (row["from"], row["to"]) == ("B", "C")
    assert row["from_modules"] == [{"module": "b.z", "docstring": "The B store."}]
    assert row["to_modules"] == [{"module": "c.w", "docstring": "The C widget."}]
    assert row["label"] == ""


def test_summarize_filled_worksheet():
    missing = [
        {"from": "A", "to": "C", "label": "abstracted"},
        {"from": "A", "to": "D", "label": "lost"},
        {"from": "A", "to": "E", "label": ""},  # not yet labelled
    ]
    unbacked = [{"from": "B", "to": "C", "label": "hallucination"}]
    summary = summarize(missing, unbacked)
    assert summary["missing"] == {
        "abstracted": 1, "lost": 1, "unlabeled": 1, "unknown": 0, "total": 3,
    }
    assert summary["unbacked"] == {
        "semantic-inference": 0, "hallucination": 1,
        "unlabeled": 0, "unknown": 0, "total": 1,
    }


def test_write_and_reingest_roundtrip(tmp_path):
    paths = write_worksheets(FACTS, REDUCED, tmp_path)
    missing = read_worksheet(paths["missing"])
    unbacked = read_worksheet(paths["unbacked"])
    # simulate a human labelling the single missing edge
    missing[0]["label"] = "lost"
    summary = summarize(missing, unbacked)
    assert summary["missing"]["lost"] == 1
    assert summary["unbacked"]["unlabeled"] == 1  # left blank
