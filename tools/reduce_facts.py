#!/usr/bin/env python3
"""Apply the registered reduction ladder (Z2 protocol §3b) to a facts base.

WHAT THIS IS
------------
The size rule of §3b lists the stages by which the rendered Z2 prompt is
brought under the threshold of 24 000 tokens. Two of those stages act on the
facts base `input_facts.json` (§3a-2):

    Stage 0   `--drop-docstrings` + `--drop-empty-init`
              Remove `module_docstring`, and `docstring` on functions, classes
              and methods; drop the records of empty `__init__.py` modules.
    Stage 0b  `--drop-imports`
              Remove the `imports` block, because the import edges already
              stand module-sharp in the current-state model
              (`containerImportRelations`, `codeModelToIlograph.ts:575-589`).

The fields are REMOVED, not emptied: a `"docstring": null` still costs tokens,
which is what the ladder is trying to save.

An "empty `__init__.py`" is a record that carries no `imports`, no `classes`,
no `functions` and no `module_docstring` -- the emptiness criterion of
`substantive_modules` (`extractor.py:113-123`) plus the docstring. Those
records map onto package names in the current-state model, so the model still
sees them; only the empty record disappears.

ORDER WITHIN STAGE 0, and it matters: the docstrings are removed FIRST, the
emptiness test runs on the ALREADY STRIPPED record. In the Z2 facts base all
23 package records carry a `module_docstring`, so testing emptiness on the raw
record would drop NONE of them and the second half of stage 0 would be a no-op;
testing it after the strip drops the 21 that carry nothing else. Passing
`--drop-empty-init` WITHOUT `--drop-docstrings` therefore judges emptiness with
the docstring still in place -- deliberately, so each flag stays meaningful on
its own.

DETERMINISM
-----------
Key order and nesting are preserved as read; nothing is sorted, nothing is
renamed. Output is `json.dumps(..., indent=2)` and written WITHOUT a trailing
newline -- byte-identical in form to what `run_logger.py:62-64` produces for
the original. Applying the tool twice to the same input yields byte-identical
output.

This tool NEVER edits in place and never touches its input file.

INVOCATION
----------
    python3 tools/reduce_facts.py --drop-docstrings --drop-empty-init \
        data/z2/eingaben/input_facts_raw.json /tmp/facts_s0.json
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

DOCSTRING_KEY = "docstring"
MODULE_DOCSTRING_KEY = "module_docstring"
IMPORTS_KEY = "imports"
SUBSTANCE_KEYS = ("imports", "classes", "functions")


def is_empty_init(record: dict) -> bool:
    """True for a module record carrying no substance at all.

    Empty means: no imports, no classes, no functions and no module docstring.
    Such a record comes from an empty `__init__.py`; `_module_name`
    (`extractor.py:23-29`) shortens it to the package name.
    """
    if record.get(MODULE_DOCSTRING_KEY):
        return False
    return not any(record.get(key) for key in SUBSTANCE_KEYS)


def strip_docstrings(node: object) -> object:
    """Remove every `docstring` / `module_docstring` key, at any depth."""
    if isinstance(node, dict):
        return {
            key: strip_docstrings(value)
            for key, value in node.items()
            if key not in (DOCSTRING_KEY, MODULE_DOCSTRING_KEY)
        }
    if isinstance(node, list):
        return [strip_docstrings(item) for item in node]
    return node


def reduce_facts(records: list[dict], *, drop_docstrings: bool,
                 drop_empty_init: bool, drop_imports: bool) -> list[dict]:
    """Apply the requested stages, in the order the ladder registers them."""
    out = records
    if drop_docstrings:
        out = [strip_docstrings(r) for r in out]
    if drop_empty_init:
        # Tested on the already stripped record -- see ORDER WITHIN STAGE 0 above.
        out = [r for r in out if not is_empty_init(r)]
    if drop_imports:
        out = [{k: v for k, v in r.items() if k != IMPORTS_KEY} for r in out]
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("input", help="Eingabepfad, wird NICHT verändert")
    parser.add_argument("output", help="Ausgabepfad")
    parser.add_argument("--drop-docstrings", action="store_true",
                        help="Stufe 0: alle docstring-/module_docstring-Felder entfernen")
    parser.add_argument("--drop-empty-init", action="store_true",
                        help="Stufe 0: Records leerer __init__.py auslassen")
    parser.add_argument("--drop-imports", action="store_true",
                        help="Stufe 0b: das Feld imports entfernen")
    args = parser.parse_args()

    records = json.loads(Path(args.input).read_text(encoding="utf-8"))
    reduced = reduce_facts(records,
                           drop_docstrings=args.drop_docstrings,
                           drop_empty_init=args.drop_empty_init,
                           drop_imports=args.drop_imports)
    Path(args.output).write_text(json.dumps(reduced, indent=2), encoding="utf-8")
    print(f"{args.input}: {len(records)} Records -> "
          f"{args.output}: {len(reduced)} Records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
