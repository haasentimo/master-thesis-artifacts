#!/usr/bin/env python3
"""Build the clean-control file list of the campaign (protocol §5, addendum Rev. 17).

Phase 04, C3a. The control set is the DENOMINATOR of the false-positive rate measured in C3b:
every one of its files is sent through the LLM path although nothing changed in it, so anything
reported on it is a false positive by construction.

Criterion, taken from the protocol and not invented here (§5, addendum 14.08.2026, Rev. 17):

    every `.py` file of the tree EXCEPT the EMPTY `__init__.py`
    empty = no import, no `def`, no `class`, no `__all__`

Emptiness is decided with `ast`, never by file size: a package module carrying nothing but a
docstring is empty in the sense of the criterion, and one carrying a re-export facade is not,
although both are small. The two content-bearing package modules of the baseline —
`depot/core/adapters/__init__.py` (re-export facade) and `depot/orders/services/__init__.py`
(parent edge of the CYCLE_PARENT_CHILD pair plus two functions) — are therefore IN, and that is
the whole point of the Rev. 17 wording: without them the false positive preregistered on the
adapter facade (§5, addendum Rev. 16) would not be measurable.

The output is sorted and repo-relative, one path per line, so the file is a stable, hashable
measurement input like the Soll and the rule file. It is passed to the checker as
`--control-files`, and the run acceptance rule of a control run reads
`control_files_count == calls_total` (protocol §6, addendum Rev. 22).

Usage:
    tools/build_control_set.py --testrepo DIR [--out data/soll/control_files.txt]
    tools/build_control_set.py --selfcheck
"""

from __future__ import annotations

import argparse
import ast
import sys
from pathlib import Path


def is_empty_init(path: Path) -> bool:
    """Empty in the sense of protocol §5 Rev. 17: no import, no def, no class, no __all__."""
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            return False
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            return False
        if isinstance(node, ast.Name) and node.id == "__all__":
            return False
    return True


def control_files(testrepo: Path) -> list[str]:
    paths = []
    for path in testrepo.rglob("*.py"):
        if ".git" in path.parts:
            continue
        if path.name == "__init__.py" and is_empty_init(path):
            continue
        paths.append(path.relative_to(testrepo).as_posix())
    return sorted(paths)


def selfcheck() -> None:
    """The emptiness rule, on source strings — it decides 21 exclusions and has to be right."""
    import tempfile

    cases = {
        "": True,
        '"""Just a docstring."""\n': True,
        "# only a comment\n": True,
        "from depot.core import ports\n": False,
        "import os\n": False,
        "def f() -> None:\n    pass\n": False,
        "class C:\n    pass\n": False,
        '__all__ = ["a"]\n': False,
        # the two real content-bearing package modules of the baseline, in miniature
        'from . import storage\n\n__all__ = ["storage"]\n\n\ndef __getattr__(name: str) -> object:\n    raise AttributeError(name)\n': False,
    }
    with tempfile.TemporaryDirectory() as tmp:
        for source, expected in cases.items():
            path = Path(tmp) / "__init__.py"
            path.write_text(source, encoding="utf-8")
            got = is_empty_init(path)
            assert got == expected, f"is_empty_init({source!r}) = {got}, expected {expected}"
    print("selfcheck OK", file=sys.stderr)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--testrepo", type=Path)
    ap.add_argument("--selfcheck", action="store_true", help="run the emptiness-rule assertions and exit")
    ap.add_argument("--out", type=Path, default=Path("data/soll/control_files.txt"))
    args = ap.parse_args()
    if args.selfcheck:
        selfcheck()
        return 0
    if not args.testrepo:
        ap.error("--testrepo is required")

    paths = control_files(args.testrepo)
    args.out.write_text("".join(f"{p}\n" for p in paths), encoding="utf-8")
    print(f"{args.out}: {len(paths)} files", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
