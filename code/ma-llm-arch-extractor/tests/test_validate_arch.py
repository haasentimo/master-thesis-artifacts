from llm_arch.abstraction.schema import ArchModel, Component, Relation
from llm_arch.ilograph import validate_arch

# substantive module set (M) and the full known set for a tiny repo
M = {"a.x", "a.y", "b.z"}
KNOWN = M | {"a", "b"}  # empty __init__ packages are known but not required


def _arch(components, relations=None):
    return ArchModel(components=components, relations=relations or [])


def test_valid_disjoint_complete_model():
    arch = _arch(
        [
            Component(id="a", name="A", contained_modules=["a.x", "a.y"]),
            Component(id="b", name="B", contained_modules=["b.z"]),
        ],
        [Relation(from_="b", to="a")],
    )
    res = validate_arch(arch, required_modules=M, known_modules=KNOWN)
    assert res.valid
    assert res.errors == []


def test_double_mapping_is_disjointness_error():
    # the finding: book_repository-style module placed in two components
    arch = _arch(
        [
            Component(id="a", name="A", contained_modules=["a.x", "a.y"]),
            Component(id="db", name="DB", contained_modules=["a.y", "b.z"]),
        ]
    )
    res = validate_arch(arch, required_modules=M, known_modules=KNOWN)
    assert not res.valid
    assert any(e.startswith("disjointness:") and "'a.y'" in e for e in res.errors)


def test_missing_module_is_completeness_error():
    arch = _arch([Component(id="a", name="A", contained_modules=["a.x", "a.y"])])
    res = validate_arch(arch, required_modules=M, known_modules=KNOWN)
    assert any(e.startswith("completeness:") and "'b.z'" in e for e in res.errors)


def test_phantom_module_error():
    arch = _arch(
        [
            Component(id="a", name="A", contained_modules=["a.x", "a.y"]),
            Component(id="b", name="B", contained_modules=["b.z", "made.up"]),
        ]
    )
    res = validate_arch(arch, required_modules=M, known_modules=KNOWN)
    assert any(e.startswith("phantom_module:") and "made.up" in e for e in res.errors)


def test_unresolvable_relation_error():
    arch = _arch(
        [Component(id="a", name="A", contained_modules=["a.x", "a.y", "b.z"])],
        [Relation(from_="a", to="ghost")],
    )
    res = validate_arch(arch, required_modules=M, known_modules=KNOWN)
    assert any(e.startswith("relation:") and "ghost" in e for e in res.errors)


def test_placing_known_nonrequired_init_is_allowed():
    arch = _arch(
        [
            Component(id="a", name="A", contained_modules=["a", "a.x", "a.y"]),
            Component(id="b", name="B", contained_modules=["b.z"]),
        ]
    )
    res = validate_arch(arch, required_modules=M, known_modules=KNOWN)
    assert res.valid  # placing the empty package "a" is fine, not a phantom
