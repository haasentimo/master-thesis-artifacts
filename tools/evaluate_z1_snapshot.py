#!/usr/bin/env python3
"""Replay mode: run `tools/evaluate_z1.py` against the public extractor snapshot.

Added to the artifact package; NOT part of the thesis repository and NOT used for the
archived evaluation. `evaluate_z1.py` itself stays byte-identical.

`evaluate_z1.py` reads its provenance out of git: `git rev-parse HEAD` of the extractor
checkout must equal the registered commit `5c0b65a…` (protocol section 6.1), and the
instrument blobs are reported via `git ls-files -s`. The package ships the extractor as a
plain file snapshot (`code/ma-llm-arch-extractor/`), without the private history, so
there is no `.git` to ask.

This wrapper replaces exactly those two git look-ups and nothing else:

* `head_of(extractor)` — verifies the snapshot against `SNAPSHOT.json` (every file
  present, its git blob SHA1 recomputed from its bytes and equal to the listed one, no
  unlisted file) and returns the commit named there, which must be `EXPECTED_HEAD`.
* `blob_sha1(extractor, path)` — returns the git blob SHA1 recomputed from the file
  bytes (`sha1(b"blob <len>\\0" + bytes)`, identical to `git hash-object`), after the
  same verification.

Every figure, validity verdict and metric still comes from `evaluate_z1.py` and the
unchanged extractor code; run selection, `meta.json` reading and the `validate_arch`
cross-check are untouched.

    python3 tools/evaluate_z1_snapshot.py --selftest
    python3 tools/evaluate_z1_snapshot.py --out <dir>
    python3 tools/evaluate_z1_snapshot.py --verify-snapshot   # stdlib only
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import evaluate_z1 as z1  # noqa: E402

SNAPSHOT = z1.ROOT / "code" / "ma-llm-arch-extractor"
_verified: dict[Path, str] = {}


def git_blob_sha1(data: bytes) -> str:
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def verify_snapshot(extractor: Path) -> str:
    """Check the snapshot against SNAPSHOT.json; return the source commit."""
    extractor = extractor.resolve()
    if extractor in _verified:
        return _verified[extractor]
    doc = json.loads((extractor / "SNAPSHOT.json").read_text(encoding="utf-8"))
    listed = doc["files"]
    present = {p.relative_to(extractor).as_posix()
               for p in extractor.rglob("*")
               if p.is_file() and p.name != "SNAPSHOT.json" and "__pycache__" not in p.parts}
    problems = [f"fehlt: {p}" for p in sorted(set(listed) - present)]
    problems += [f"nicht gelistet: {p}" for p in sorted(present - set(listed))]
    for path in sorted(set(listed) & present):
        actual = git_blob_sha1((extractor / path).read_bytes())
        if actual != listed[path]["git_blob_sha1"]:
            problems.append(f"Blob weicht ab: {path} ({actual})")
    if problems:
        raise z1.Abort("§6.1", "Snapshot entspricht nicht SNAPSHOT.json: " + "; ".join(problems))
    if doc["commit"] != z1.EXPECTED_HEAD:
        raise z1.Abort("§6.1", f"Snapshot stammt von {doc['commit']}, "
                               f"registriert ist {z1.EXPECTED_HEAD}.")
    _verified[extractor] = doc["commit"]
    return doc["commit"]


def head_of(repo: Path) -> str:
    return verify_snapshot(repo)


def blob_sha1(extractor: Path, path: str) -> str:
    verify_snapshot(extractor)
    return git_blob_sha1((extractor / path).read_bytes())


def main(argv: list[str]) -> int:
    if argv == ["--verify-snapshot"]:
        try:
            commit = verify_snapshot(SNAPSHOT)
        except z1.Abort as exc:
            print(f"ABBRUCH ({exc.invariant}): {exc.detail}", file=sys.stderr)
            return 2
        print(f"OK    {SNAPSHOT.relative_to(z1.ROOT)} = {commit}")
        return 0
    z1.head_of, z1.blob_sha1, z1.EXTRACTOR = head_of, blob_sha1, SNAPSHOT
    return z1.main(argv)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
