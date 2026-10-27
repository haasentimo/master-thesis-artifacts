"""Pydantic data models for raw AST facts.

These models are pure structure: names, signatures, inheritance and
docstrings. No interpretation happens here (guardrail 1: facts only).
"""

from pydantic import BaseModel


class ImportedName(BaseModel):
    """A single name pulled in by a `from ... import` statement."""

    name: str
    alias: str | None = None


class ImportFact(BaseModel):
    """One import statement.

    `module` is the dotted source (empty for `from . import x`).
    `relative_level` is the number of leading dots (0 for absolute imports).
    `names` is empty for plain `import x` statements.
    """

    module: str
    relative_level: int = 0
    names: list[ImportedName] = []
    alias: str | None = None  # for `import x as y`


class FunctionFact(BaseModel):
    """A module-level function or a method, including its rendered signature."""

    name: str
    signature: str  # e.g. "(self, item: LineItem) -> None"
    decorators: list[str] = []
    docstring: str | None = None


class ClassFact(BaseModel):
    """A class with its base classes, decorators, methods and docstring."""

    name: str
    bases: list[str] = []
    decorators: list[str] = []
    docstring: str | None = None
    methods: list[FunctionFact] = []


class ModuleFacts(BaseModel):
    """All facts extracted from one Python module.

    `module_name` is the dotted path relative to the repo root and serves
    as the stable node anchor for the later UF1 diff (guardrail 4).
    """

    module_name: str
    module_docstring: str | None = None
    imports: list[ImportFact] = []
    classes: list[ClassFact] = []
    functions: list[FunctionFact] = []
