# Master Thesis Artifacts

Curated artifact and evidence package for the master thesis of Timo Haas (HTWG Konstanz).

## Purpose

This repository collects the material an external examiner needs to check the empirical
part of the thesis: the study protocols frozen before the measurements, the measurement
inputs and raw artifacts, the deterministic evaluation tools, and the canonical result
artifacts. It is a **curated selection** taken from the private thesis repository
(`masterarbeit`, state `f5dca31b41720f9b9204afebf285d162c36ee874`). It is **not** a complete
export of that repository and **not** a full replication package.

Files keep their original relative paths, so path references inside the documents
(e.g. `data/campaign/eval/c14_eval_full.md`) resolve in this repository too. Some documents
link to reports under `docs/repo-kontext/` that were not selected; those links stay dangling
on purpose. The complete history is part of the examiner package.

[`MANIFEST.md`](MANIFEST.md) is the central index: study, role, path, freeze, commit and SHA256
of every key artifact.

## Included studies

- **Z1: architecture model derivation** — extraction comparison, protocol
  `docs/protokolle/z1_protokoll_extraktionsvergleich.md`, data under `data/z1/`.
- **Z2: architecture rule derivation** — protocol `docs/protokolle/z2_protokoll_regelableitung.md`,
  data under `data/z2/`.
- **Z3: architecture violation detection** — evaluation protocol
  `docs/protokolle/eval_protokoll_phase04.md`, evaluation specification
  `docs/protokolle/c6_auswertungsspezifikation.md`, target model under `data/soll/`, campaign
  under `data/campaign/`, synthetic test repository under `data/testrepo/`.

**Z4 is not included.** It is based on a non-public company repository.

## Evidence and preregistration

The study protocols were frozen, dated by commit, before the respective measurements. The
frozen states, their commit references and their SHA256 values are documented in this
package (`freezes/`, `MANIFEST.md`, and the witness reports in `docs/repo-kontext/`). Each
frozen file was extracted with `git show <commit>:<path>` from the history of the thesis
repository and checked against the SHA256 recorded at freeze time.

| Study | Frozen state | Commit | SHA256 |
|---|---|---|---|
| Z1 | Rev. 1, 31.08.2026 | `34d6738c1c295665d1dcf5036e58799df312ef8a` | `60cd6b3a255e148611cb5425e24c410db9d2e81235df75fc31e8cdf1fdba85c4` |
| Z2 | content state of 02.09.2026, freeze note in `35aff9bd777a204977a77ab7fc25df09e9983da6` | `793e5734cc1157a7cae2e4a0aa3a0b8fb893efae` | `04690cd5a08b8c7bf61bc8d98253a344b64b05cf6ce9e85a68f4fea1e411d525` |
| Z3 | Rev. 33, 27.08.2026 | `3e17f44e0cee551d11e29f19a932db1cdff10648` | `2cb0385f08e88333863d83d0819943e352d3f1b857d4870801211b4817ac181e` |

No external preregistration platform and no external cryptographic timestamp was used.
The evidence is the commit history of the private thesis repository, which is handed to
the examiners as a bundle (see [`examiner-package/README.md`](examiner-package/README.md)).
Later changes to the protocols are recorded as dated revisions with amendments inside the
protocols themselves; the current versions are in `docs/protokolle/`.

## Reproducibility limits

- Some LLM endpoints and provider states used in the measurements cannot be reproduced
  identically today.
- The package is meant for checking the frozen inputs, the raw artifacts and the
  deterministic evaluation. The archived artifacts permit independent inspection of the
  reported results. The Z3 evaluation can be rerun from the included campaign artifacts
  and clean-control stocks (see [Rerunning the C14 evaluation](#rerunning-the-c14-evaluation)).
  The Z1 evaluation and the Z2 fact bases can be rerun from the included extractor snapshot
  (see [Rerunning the Z1 evaluation](#rerunning-the-z1-evaluation)).
- A byte-identical regeneration of all model responses is **not** claimed.
- K3 depended on a hosted provider (DigitalOcean endpoint, not pinned). Its valid runs came
  from several points in time under server-side conditions that were neither controlled nor
  measured (see `data/campaign/k3/MANIFEST.md`).
- Where `system_fingerprint` was not available (recorded as `null` in the artifacts), the
  full serving identity of the model is **not** known. A seed was sent but is not assumed to
  have been effective.
- The extractor package `llm_arch` (Z1/Z2) is included as a file snapshot of the registered
  commit, without its development history (`code/`). The Triton conformance checker for Z3
  is not included.

## Repository structure

| Path | Content |
|---|---|
| `docs/protokolle/` | Current versions of the four protocols / specifications |
| `docs/repo-kontext/` | Positive list of witness reports (freeze reports, Z3 evaluation repair chain C11–C14), plus the Z1 architecture model schema |
| `freezes/z1/`, `freezes/z2/`, `freezes/z3/` | Protocol states at freeze time, extracted from git history |
| `data/z1/` | Z1 runs (K2, truncated K2, K3) and evaluation |
| `data/z2/` | Z2 inputs, instrument measurements, runs (K2/K3, B1) and rating |
| `data/soll/` | Z3 target model: the seven registered measurement inputs |
| `data/campaign/` | Z3 campaign: raw artifacts K1–K5, run manifests, control runs, evaluation runs C11–C14 |
| `data/c3b-k2/`, `data/c3b-k3/` | Z3 clean-control stocks (C3b) for K2 and K3: the 52 control modules on the baseline, input of the C14 evaluation |
| `data/testrepo/` | Git bundles of the synthetic test repository |
| `data/checker/` | Reference to the checker state (no code, see its README) |
| `code/ma-llm-arch-extractor/` | Snapshot of the extractor `llm_arch` at the registered commit `5c0b65a` (Z1, Z2 fact bases), see [`code/README.md`](code/README.md) |
| `tests/fixtures/z1/` | Parse-assertion fixtures of the Z1 tools (used by `--selftest`) |
| `tools/` | Runner and evaluation tools as used, unchanged; plus `evaluate_z1_snapshot.py`, added for this package |
| `scripts/verify.sh` | Verification of this package |
| `examiner-package/` | Description of the material handed to the examiners separately |

## Synthetic test repository

`data/testrepo/` holds the git bundles of `ma-conformance-testrepo`: the clean baseline
`0d651041ed87dd03f2f78359713633fac01c0a66` (tag `baseline`) and 32 injection tags `inj/01`
to `inj/32`.

- The test repository was built for this study.
- It was not publicly accessible during the evaluation period.
- A later publication does not change this statement for the measurement made at that time.
- For future studies with models trained later, non-publication can no longer be assumed
  once the repository has been published.

## Verification

```bash
scripts/verify.sh
```

The script checks, from the repository root:

1. the top-level `SHA256SUMS` (`sha256sum -c SHA256SUMS`), which covers every file of this
   repository except `.git/`, itself and ignored local-only files;
2. every nested `SHA256SUMS` from the original thesis repository. Those under `data/z1/`,
   `data/z2/`, `data/soll/`, `data/testrepo/`, `data/c3b-k2/` and `data/c3b-k3/` use paths
   relative to their own directory;
   those under `data/campaign/` use paths relative to the repository root, so they are
   checked from there;
3. the three frozen protocols in `freezes/` against the SHA256 recorded at freeze time;
4. the extractor snapshot `code/ma-llm-arch-extractor/` against its `SNAPSHOT.json` (git
   blob SHA1 of every file, no unlisted file, source commit `5c0b65a`; Python standard
   library only).

It exits non-zero on the first mismatch and changes no file.

## Rerunning the Z1 evaluation

`tools/evaluate_z1.py` computes the Z1 result (`data/z1/auswertung/z1_auswertung.json` /
`.md`) with the unchanged extractor code. The extractor is included as a snapshot of the
registered commit `5c0b65a82cc3d8af47c022d779ff63d8a20a9e08` in
`code/ma-llm-arch-extractor/` (origin, content and exclusions: [`code/README.md`](code/README.md)).

**Environment.** Python 3.12.3 with the pins of `tools/z2_extractor_requirements.txt`
(pydantic 2.13.5, openai 3.6.0, ruamel.yaml 0.19.1, …). That file documents itself as a
reconstruction: the environment of the Z1 runs on 31.08.2026 is not attested, only its
Python, pydantic and openai versions (`run_manifest.json`). `pytest` is needed only for the
extractor's own tests.

```bash
python3.12 -m venv .venv
.venv/bin/pip install -r tools/z2_extractor_requirements.txt
.venv/bin/python tools/evaluate_z1_snapshot.py --selftest
out=$(mktemp -d)
.venv/bin/python tools/evaluate_z1_snapshot.py --out "$out"
```

**Why a wrapper.** `evaluate_z1.py` checks its provenance through git: the extractor's
`git rev-parse HEAD` must equal the registered commit, and the instrument blobs are read
with `git ls-files -s`. The snapshot has no `.git`. `tools/evaluate_z1_snapshot.py`
(added for this package, not part of the thesis repository) replaces exactly these two
look-ups. It verifies the snapshot against `SNAPSHOT.json` (every file's git blob SHA1,
recomputed from its bytes, equal to the one in the commit tree; no file missing; no
unlisted file) and takes the commit from there. Blob hashes are recomputed from the file
bytes as `git hash-object` would. Run selection, `meta.json` reading, the `validate_arch`
cross-check, metrics and rendering stay those of the unchanged `evaluate_z1.py`. A
modified or additional file in the snapshot aborts with `ABBRUCH (§6.1)`.

**Expected result.** The output equals the archived evaluation except for two fields:

- `erzeugt_utc` (generation time);
- `protokoll` (revision and SHA256 of `docs/protokolle/z1_protokoll_extraktionsvergleich.md`).
  The archived run read Rev. 5 (`a6a42f3a…`, thesis commit `062e604`); this package
  carries Rev. 6 (`618ebde0…`). With the Rev. 5 file in place the output differs only in
  `erzeugt_utc`.

What is compared: approach 1 (ten figures plus `gold_similarity`, E1/E2 10 of 10) and,
per block `k2`, `k3`, `k2_trunkiert`, six runs each (`run0`, `run0_w1`…`run0_w3`, `run1`,
`run2`): 0 of 6 valid in every block, no deviation between `meta.json` and the
`validate_arch` cross-check, the `compare_runs.py` aggregates, and the token extrapolation.

**Limit: the tokenizer.** The extrapolation section (`tools/z1_tokenizer.py`) builds its
tokenizer from the GGUF metadata of the Ollama model `qwen2.5-coder:7b` in the local
Ollama store. Model weights are not part of this package. Without that store the section
reports `verfuegbar: false` and differs from the archive; all measured figures are
unaffected.

## Reproducing the Z2 fact bases

The B1 input `data/z2/eingaben/input_facts_raw.json` was produced with the same extractor
commit, by its `extract_repo` on the test repository's `src/` and the serialization of
`run_logger.py:62-64` (no trailing newline). `input_facts.json` follows from
`tools/reduce_facts.py` (stages 0 and 0b). From the repository root, with the environment
above:

```bash
work=$(mktemp -d)
git clone -q data/testrepo/ma-conformance-testrepo-baseline.bundle "$work/testrepo"
git -C "$work/testrepo" checkout -q 0d651041ed87dd03f2f78359713633fac01c0a66
PYTHONPATH=code/ma-llm-arch-extractor/src .venv/bin/python -c "
import json, sys
from llm_arch.facts import extract_repo
facts = extract_repo(sys.argv[1])
open(sys.argv[2], 'w').write(json.dumps([f.model_dump() for f in facts], indent=2))
" "$work/testrepo/src" "$work/input_facts_raw.json"
python3 tools/reduce_facts.py --drop-docstrings --drop-empty-init --drop-imports \
  "$work/input_facts_raw.json" "$work/input_facts.json"
sha256sum "$work"/input_facts*.json
```

Expected: `85b7a2c1834b4f954a630f3ff3ccf01ebc139a9f51039365b7759f7fbcc28951`
(`input_facts_raw.json`, 73 records) and
`f670593a7add275c364ebff5a5529cb95a787a10de5e0c80f97cd46574eb282a` (`input_facts.json`, 52
records), the hashes in `data/z2/eingaben/SHA256SUMS`. The same call on
`code/ma-llm-arch-extractor/fixtures/rich_repo` gives the Z1 fact base
`data/z1/k2/run0/extractor/input_facts.json` (`f8976558…`). The second B1 input,
`ist_modell.yaml`, is a Triton export (provenance in `data/z2/MANIFEST.md`).

## Rerunning the C14 evaluation

`tools/evaluate_campaign.py` regenerates the canonical Z3 result C14
(`data/campaign/eval/c14_eval_full.json` / `.md`) from data in this repository only. It
needs Python 3 with the standard library (it imports `tools/match_k4k5.py`, nothing else)
and reads, at its default paths:

| Input | Path | Role |
|---|---|---|
| Target model | `data/soll/` | `injection_manifest.json`, `control_files.txt` (denominator 52) |
| Clean-control stocks | `data/c3b-k2/`, `data/c3b-k3/` | False-positive base rate and the clean-state side of every K2/K3 cell |
| Campaign | `data/campaign/` | Run manifests (source of T7), `journal.jsonl`, `MANIFEST.md` files, raw artifacts K1–K5 |

From the repository root, writing to a scratch directory so the archived files stay
untouched:

```bash
out=$(mktemp -d)
python3 tools/evaluate_campaign.py --with-campaign \
  --json-out "$out/c14.json" --markdown-out "$out/c14.md"
for f in json md; do
  sed "s|$(pwd -P)|/home/haasentimo/ma/masterarbeit|g" "$out/c14.$f" | sha256sum
done
```

Expected, as registered in the archived run head (`c14_run_head.rohausgabe_sha256`):

```
c7c6d003946129f64b4ae7b180d1a251cf4e5c243ed9bf022918a22cd359280a  (json)
759c72c89f2cf30ed60539ba02ac5fb0028d71ac5c81d407348e1b66dba8aa24  (md)
```

**The one normalization.** The tool records the absolute paths of the files it reads
(JSON keys `reads` and `journal`, and one `**Quelle:**` line in the Markdown). The original
run was made in `/home/haasentimo/ma/masterarbeit`, the working directory recorded in the
run head. The `sed` above replaces the resolved repository root of the rerun with that
original root, as a literal string, and changes nothing else. No value, count, marker or
ordering is touched.

**Why the archived files themselves have different hashes.** The archived
`c14_eval_full.json` / `.md` are the raw output plus a run head prepended afterwards: a
top-level JSON key `c14_run_head` and 60 lines of Markdown above the first harness line.
The raw output hashes above are the ones the run head registers. Equivalently, the
archived JSON without `c14_run_head` equals the normalized rerun JSON, and the archived
Markdown ends with the normalized rerun Markdown.

Without `data/c3b-k2/` and `data/c3b-k3/`, the tool aborts with
`StatisticsError: no median for empty data`.

## Public-release note

This repository is in a private, pre-release state. Before any public release, check in
particular the publication rights for the Triton/checker artifacts and any references to
the employer. No license has been added yet.
