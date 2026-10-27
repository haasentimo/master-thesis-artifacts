from pathlib import Path

from llm_arch.facts import extract_repo

FIXTURE = Path(__file__).parent.parent / "fixtures" / "sample_repo"


def _by_name(modules):
    return {m.module_name: m for m in modules}


def test_extracts_all_modules():
    mods = _by_name(extract_repo(FIXTURE))
    assert set(mods) == {
        "shop",
        "shop.api",
        "shop.api.routes",
        "shop.domain",
        "shop.domain.order",
        "shop.infrastructure",
        "shop.infrastructure.repository",
    }


def test_api_layer_imports_other_layers():
    routes = _by_name(extract_repo(FIXTURE))["shop.api.routes"]
    sources = {imp.module for imp in routes.imports}
    assert "shop.domain.order" in sources
    assert "shop.infrastructure.repository" in sources


def test_captures_signatures_inheritance_and_docstrings():
    order = _by_name(extract_repo(FIXTURE))["shop.domain.order"]
    classes = {c.name: c for c in order.classes}

    # docstring captured (semantic signal, guardrail 3)
    assert order.module_docstring.startswith("Core domain entities")

    line_item = classes["LineItem"]
    subtotal = next(m for m in line_item.methods if m.name == "subtotal_cents")
    assert subtotal.signature == "(self) -> int"

    # inheritance captured
    err = classes["OrderValidationError"]
    assert err.bases == ["Exception"]

    # dataclass decorator captured
    assert "dataclass" in line_item.decorators


def test_relative_and_aliased_imports(tmp_path):
    pkg = tmp_path / "pkg"
    pkg.mkdir()
    (pkg / "__init__.py").write_text("")
    (pkg / "mod.py").write_text(
        "import os.path as osp\n"
        "from . import sibling\n"
        "from ..other import thing as t\n"
    )
    mod = _by_name(extract_repo(tmp_path))["pkg.mod"]
    aliased = next(i for i in mod.imports if i.module == "os.path")
    assert aliased.alias == "osp"

    rel = next(i for i in mod.imports if i.relative_level == 1)
    assert rel.names[0].name == "sibling"

    parent = next(i for i in mod.imports if i.relative_level == 2)
    assert parent.module == "other"
    assert parent.names[0].alias == "t"
