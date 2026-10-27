#!/usr/bin/env python3
"""Side-by-side run comparison + variance check, from existing meta.json fields.

Usage:
    python scripts/compare_runs.py <runA-dir> <runA-dir> ... -- <runB-dir> ...

Groups are separated by a literal `--`. Each group is summarised (one row per
run) and checked for output byte-identity (sha256 of arch_model.json) so the
"is this deterministic / what's the validity_rate" question is measured, not
assumed. Reads only fields the pipeline already logs; invents no metric.
"""

import hashlib
import json
import sys
from pathlib import Path

COLS = [
    "model", "run_index", "module_coverage", "relation_precision",
    "relation_recall", "phantom_modules", "valid_raw", "valid_final",
    "attempts_used", "prompt_tokens", "completion_tokens", "latency_ms",
]


def _split_groups(args: list[str]) -> list[list[str]]:
    groups, cur = [], []
    for a in args:
        if a == "--":
            groups.append(cur)
            cur = []
        else:
            cur.append(a)
    groups.append(cur)
    return [g for g in groups if g]


def _fmt(v: object) -> str:
    return f"{v:.3f}" if isinstance(v, float) else str(v)


def _arch_hash(run_dir: Path) -> str | None:
    f = run_dir / "arch_model.json"
    return hashlib.sha256(f.read_bytes()).hexdigest()[:12] if f.exists() else None


def main(argv: list[str]) -> int:
    if not argv:
        print(__doc__)
        return 1
    groups = _split_groups(argv)
    print("| " + " | ".join(COLS) + " |")
    print("|" + "|".join("---" for _ in COLS) + "|")
    for gi, group in enumerate(groups):
        metas = [json.loads((Path(d) / "meta.json").read_text()) for d in group]
        for m in metas:
            print("| " + " | ".join(_fmt(m.get(c, "")) for c in COLS) + " |")
        hashes = {_arch_hash(Path(d)) for d in group}
        identical = len(hashes) == 1 and None not in hashes
        valid_rate = sum(bool(m.get("valid_final")) for m in metas) / len(metas)
        model = metas[0].get("model", f"group{gi}")
        print(
            f"\n_{model}_: {len(metas)} runs · "
            f"output byte-identical: {identical} · "
            f"validity_rate(valid_final): {valid_rate:.2f}\n"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))