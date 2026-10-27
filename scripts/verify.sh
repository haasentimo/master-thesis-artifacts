#!/usr/bin/env bash
# Verifies the artifact package. Changes no file; exits non-zero on the first mismatch.
set -euo pipefail
cd "$(dirname "$0")/.."

echo "== top-level SHA256SUMS"
sha256sum -c --quiet SHA256SUMS

echo "== nested SHA256SUMS"
while IFS= read -r sums; do
  dir=$(dirname "$sums")
  # The campaign sums carry repository-root paths, all others are relative to their directory.
  if head -n1 "$sums" | grep -q '  data/'; then
    sha256sum -c --quiet "$sums"
  else
    (cd "$dir" && sha256sum -c --quiet SHA256SUMS)
  fi
  echo "ok  $sums"
done < <(find . -mindepth 2 -path ./.git -prune -o -name SHA256SUMS -print | sed 's#^\./##' | LC_ALL=C sort)

echo "== frozen protocols"
sha256sum -c - <<'EOF'
60cd6b3a255e148611cb5425e24c410db9d2e81235df75fc31e8cdf1fdba85c4  freezes/z1/z1_protokoll_extraktionsvergleich@34d6738.md
04690cd5a08b8c7bf61bc8d98253a344b64b05cf6ce9e85a68f4fea1e411d525  freezes/z2/z2_protokoll_regelableitung@793e573.md
2cb0385f08e88333863d83d0819943e352d3f1b857d4870801211b4817ac181e  freezes/z3/eval_protokoll_phase04@3e17f44.md
EOF

echo "== tool state registered for C14"
sha256sum -c - <<'EOF'
6cc16ef9c041b8721500fc521a437ea090fcacd209cf275561f673a1e52b7018  freezes/z3/tools/check_doc_invariants@02d8fc8.py
EOF

echo "== extractor snapshot (git blob SHA1 against SNAPSHOT.json, commit 5c0b65a)"
PYTHONDONTWRITEBYTECODE=1 python3 tools/evaluate_z1_snapshot.py --verify-snapshot

echo "all checks passed"
