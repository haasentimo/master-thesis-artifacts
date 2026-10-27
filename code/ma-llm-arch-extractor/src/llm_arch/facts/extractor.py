"""AST-based fact extraction for a Python repository.

Walks every `.py` file, parses it with the stdlib `ast` module and emits
one `ModuleFacts` per module. Only top-level classes and functions are
captured; nested definitions are intentionally ignored (this is a thin
fact layer, not a full code model).
"""

import ast
from pathlib import Path

from llm_arch.facts.models import (
    ClassFact,
    FunctionFact,
    ImportedName,
    ImportFact,
    ModuleFacts,
)

FunctionDef = ast.FunctionDef | ast.AsyncFunctionDef


def _module_name(path: Path, repo_root: Path) -> str:
    """Dotted module name relative to the repo root (`__init__` -> package)."""
    rel = path.relative_to(repo_root).with_suffix("")
    parts = list(rel.parts)
    if parts and parts[-1] == "__init__":
        parts.pop()
    return ".".join(parts)


def _signature(node: FunctionDef) -> str:
    """Render a function's argument list and return annotation as text."""
    args = ast.unparse(node.args)
    returns = f" -> {ast.unparse(node.returns)}" if node.returns else ""
    return f"({args}){returns}"


def _function_fact(node: FunctionDef) -> FunctionFact:
    return FunctionFact(
        name=node.name,
        signature=_signature(node),
        decorators=[ast.unparse(d) for d in node.decorator_list],
        docstring=ast.get_docstring(node),
    )


def _class_fact(node: ast.ClassDef) -> ClassFact:
    methods = [
        _function_fact(child)
        for child in node.body
        if isinstance(child, FunctionDef)
    ]
    return ClassFact(
        name=node.name,
        bases=[ast.unparse(b) for b in node.bases],
        decorators=[ast.unparse(d) for d in node.decorator_list],
        docstring=ast.get_docstring(node),
        methods=methods,
    )


def _import_facts(node: ast.Import | ast.ImportFrom) -> list[ImportFact]:
    if isinstance(node, ast.Import):
        # `import a.b as c` -> one fact per aliased name.
        return [
            ImportFact(module=alias.name, alias=alias.asname)
            for alias in node.names
        ]
    # ast.ImportFrom: `from .mod import x, y as z`
    names = [ImportedName(name=a.name, alias=a.asname) for a in node.names]
    return [
        ImportFact(
            module=node.module or "",
            relative_level=node.level,
            names=names,
        )
    ]


def extract_module(path: Path, repo_root: Path) -> ModuleFacts:
    """Parse a single `.py` file into `ModuleFacts`."""
    tree = ast.parse(path.read_text(encoding="utf-8"))
    imports: list[ImportFact] = []
    classes: list[ClassFact] = []
    functions: list[FunctionFact] = []
    for node in tree.body:
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            imports.extend(_import_facts(node))
        elif isinstance(node, ast.ClassDef):
            classes.append(_class_fact(node))
        elif isinstance(node, FunctionDef):
            functions.append(_function_fact(node))
    return ModuleFacts(
        module_name=_module_name(path, repo_root),
        module_docstring=ast.get_docstring(tree),
        imports=imports,
        classes=classes,
        functions=functions,
    )


def extract_repo(repo_path: str | Path) -> list[ModuleFacts]:
    """Extract facts for every `.py` module under `repo_path`, sorted by name."""
    repo_root = Path(repo_path).resolve()
    modules = [
        extract_module(py, repo_root) for py in repo_root.rglob("*.py")
    ]
    modules.sort(key=lambda m: m.module_name)
    return modules


def substantive_modules(facts: list[ModuleFacts]) -> set[str]:
    """Module names carrying architecture signal (classes, functions or imports).

    Empty/namespace `__init__` packages are excluded: they must not be required
    in a component (completeness) nor counted in coverage.
    """
    return {
        m.module_name
        for m in facts
        if m.classes or m.functions or m.imports
    }
