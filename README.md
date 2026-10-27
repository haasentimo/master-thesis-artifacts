# Master Thesis Artifacts

Curated artifact and evidence package for the master thesis of Timo Haas (HTWG Konstanz).

## Purpose

This repository collects the material an external reader or examiner needs to check the
empirical part of the thesis:

- the study protocols, frozen before the measurements;
- the measurement inputs and the raw artifacts, including the original model responses;
- the deterministic evaluation tools;
- the canonical results.

Everything reported can be recomputed from the archived raw artifacts **without calling a
language model again** (see [Checking the results](#checking-the-results-without-llm-calls)).

The package is a **curated selection** from the private thesis repository (`masterarbeit`,
state `f5dca31b41720f9b9204afebf285d162c36ee874`). It is **not** a complete export of that
repository and **not** a full replication package. Files keep their original relative paths,
so path references inside the documents resolve here too. Links to reports that were not
selected stay dangling on purpose; [`docs/repo-kontext/README.md`](docs/repo-kontext/README.md)
lists them.

[`MANIFEST.md`](MANIFEST.md) is the technical index: study, role, path, origin, freeze, commit
and SHA256 of every key artifact. This README is for orientation.

## Context

- **The thesis** examines LLM-assisted derivation of architecture models and rules from code, and
  LLM-assisted detection of architecture violations. Each study compares the LLM path with
  deterministic tools or with references written by the author.
- **Triton** (`tritongraph`) is the architecture tool under study. It belongs to the first
  supervisor, not to the author. Its Ilograph export is input to Z1 and Z2, and its conformance
  checker is the instrument of Z3 (configurations K1–K3), at commit
  `348ca9daa456af4954f11f7152fc45201035297e`. Triton code is not part of this package, see
  [`data/checker/README.md`](data/checker/README.md).
- **The synthetic test repository** `ma-conformance-testrepo` was built for Z3: a clean baseline
  and 32 injected violations. Its measured refs are archived here as git bundles in
  [`data/testrepo/`](data/testrepo/). It is also kept as a separate GitHub repository
  (`haasentimo/ma-conformance-testrepo`) with its own README.

## Studies

| Study | Question | Conditions | Raw material |
|---|---|---|---|
| **Z1** — architecture model derivation | Can an LLM abstract a valid architecture model from extracted code facts? Compared with Triton's deterministic export (approach 1). | K2 `qwen2.5-coder:7b` (Ollama), K3 `nvidia-nemotron-3-super-120b` (DigitalOcean); 6 runs each, plus 6 earlier K2 runs whose input was truncated | 18 runs, each with prompts, raw responses and validation logs per attempt |
| **Z2** — architecture rule derivation | Which architecture rules does an LLM propose from the actual model and the fact base, and how do they relate to the authored rules? | K2 and K3 × input B1; 3 runs each | 6 runs; blinded single-assessor rating; overlap with the 16 authored statements |
| **Z3** — architecture violation detection | Which of 32 injected violations do five checker configurations detect, at what false-positive rate? | K1 Triton deterministic, K2/K3 Triton with LLM, K4 import-linter, K5 PyTestArch | 32 injections × 5 configurations, clean-control runs, evaluation C14 |

**Z4 is not included.** It is based on a non-public company repository.

## Where to start

### Z1 — architecture model derivation

| What | Where |
|---|---|
| Canonical evaluation | [`data/z1/auswertung/z1_auswertung.md`](data/z1/auswertung/z1_auswertung.md) (`.json` alongside) |
| Raw responses and validation data | [`data/z1/`](data/z1/MANIFEST.md): blocks `k2/`, `k3/`, `k2_trunkiert/`, per run `extractor/attempts/attempt_<n>/` with `prompt.txt`, `raw_response.json` and `validation.json` |
| Frozen protocol | [`freezes/z1/`](freezes/z1/) (Rev. 1). Current version with amendments: [`docs/protokolle/z1_protokoll_extraktionsvergleich.md`](docs/protokolle/z1_protokoll_extraktionsvergleich.md). Freeze witness: [`z1_p_bericht_freeze.md`](docs/repo-kontext/z1_p_bericht_freeze.md) |
| Context window as measurement input (why `k2_trunkiert` is a delivery failure) | [`docs/repo-kontext/z1_t_bericht_kontextfenster.md`](docs/repo-kontext/z1_t_bericht_kontextfenster.md) |
| Extractor code snapshot | [`code/README.md`](code/README.md), [`code/ma-llm-arch-extractor/`](code/ma-llm-arch-extractor/) |
| Re-evaluation | [REPRODUCING.md — Z1](REPRODUCING.md#rerunning-the-z1-evaluation) |

### Z2 — architecture rule derivation

| What | Where |
|---|---|
| Walkthrough of the whole Z2 chain | [`data/z2/README.md`](data/z2/README.md) |
| Input data | [`data/z2/eingaben/`](data/z2/eingaben/): `ist_modell.yaml` (Triton export), `input_facts_raw.json`, `input_facts.json`; token measurement in [`data/z2/messungen/`](data/z2/messungen/) |
| Six model runs | `data/z2/k2_b1/run0…2`, `data/z2/k3_b1/run0…2`, each with `prompt.txt`, `raw_response.json`, `validation.json`, `meta.json`, `run_manifest.json` |
| Rule proposals and rating sheets | [`bewertungsblatt.md`](data/z2/bewertung/bewertungsblatt.md) (completed blinded sheet), [`zuordnungsschluessel.json`](data/z2/bewertung/zuordnungsschluessel.json) (blinding key) |
| Evaluation and overlap analysis | [`auswertung.json`](data/z2/bewertung/auswertung.json), [`ueberlappmatrix.md`](data/z2/bewertung/ueberlappmatrix.md) |
| Protocol | [`freezes/z2/`](freezes/z2/), current version [`docs/protokolle/z2_protokoll_regelableitung.md`](docs/protokolle/z2_protokoll_regelableitung.md) |
| Scripts | `tools/run_z2.py`, `reduce_facts.py`, `measure_prompt_tokens.py`, `prepare_z2_review.py`, `tally_z2_review.py`, `prepare_z2_overlap.py`, `tally_z2_overlap.py` (roles in [`data/z2/README.md`](data/z2/README.md)) |

### Z3 — architecture violation detection

| What | Where |
|---|---|
| Target model and injection manifest | [`data/soll/`](data/soll/MANIFEST.md): seven hashed measurement inputs, including [`injection_manifest.md`](data/soll/injection_manifest.md) / `.json` |
| Synthetic test repository | Git bundles in [`data/testrepo/`](data/testrepo/MANIFEST.md); construction of the 32 injections: [`c4b_bericht_injektionen.md`](docs/repo-kontext/c4b_bericht_injektionen.md) |
| Results of the five configurations | [`data/campaign/`](data/campaign/MANIFEST.md): `k1/` … `k5/`, run manifests, `journal.jsonl`; procedure of the campaign: [`c10_bericht_kampagne.md`](docs/repo-kontext/c10_bericht_kampagne.md) |
| Control runs K2 and K3 (false-positive base rate) | [`data/c3b-k2/`](data/c3b-k2/MANIFEST.md), [`data/c3b-k3/`](data/c3b-k3/MANIFEST.md); reports [`c3b_k2_bericht_kontrolllauf.md`](docs/repo-kontext/c3b_k2_bericht_kontrolllauf.md), [`c3b_k3_bericht_kontrolllauf.md`](docs/repo-kontext/c3b_k3_bericht_kontrolllauf.md). Clean-state runs K1/K4/K5: [`data/campaign/control/`](data/campaign/control/MANIFEST.md) |
| Canonical evaluation C14 and repair chain | [`data/campaign/eval/c14_eval_full.md`](data/campaign/eval/c14_eval_full.md); why C11 → C12 → C13 → C14: [`data/campaign/eval/README.md`](data/campaign/eval/README.md) and the reports C11–C14 in `docs/repo-kontext/` |
| Protocol and evaluation specification | [`freezes/z3/`](freezes/z3/) (Rev. 33), current [`eval_protokoll_phase04.md`](docs/protokolle/eval_protokoll_phase04.md), [`c6_auswertungsspezifikation.md`](docs/protokolle/c6_auswertungsspezifikation.md) |
| Re-evaluation | [REPRODUCING.md — C14](REPRODUCING.md#rerunning-the-c14-evaluation) |

## Checking the results without LLM calls

| Check | Command | Needs |
|---|---|---|
| Integrity of the whole package | `scripts/verify.sh` | `bash`, `sha256sum`, Python 3 |
| Z1 evaluation | `tools/evaluate_z1_snapshot.py --out <dir>` | Python 3.12 with `tools/z2_extractor_requirements.txt` |
| Z1/Z2 fact bases | `extract_repo` from the snapshot + `tools/reduce_facts.py` | same |
| Z2 evaluation | `tools/tally_z2_review.py`, `tools/tally_z2_overlap.py --write` | Python 3, standard library |
| Z3 evaluation C14 | `tools/evaluate_campaign.py --with-campaign …` | Python 3, standard library |

The exact commands, the expected hashes and the one documented normalization are in
[`REPRODUCING.md`](REPRODUCING.md) and [`data/z2/README.md`](data/z2/README.md). All of them
were run against this package with the stated results.

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
This package documents the frozen protocol states, their commit references and their SHA256
values, and `scripts/verify.sh` checks the frozen files against these values. The original
commit times are recorded in the private thesis repository, which is not published. Without
access to that history, it cannot be fully verified independently that the protocols were
frozen at the stated times, before the measurements.
Later changes to the protocols are recorded as dated revisions with amendments inside the
protocols themselves; the current versions are in `docs/protokolle/`.

## Reproducibility limits

- Some LLM endpoints and provider states used in the measurements cannot be reproduced
  identically today. A byte-identical regeneration of the model responses is **not** claimed;
  the package recomputes the evaluations from the archived responses.
- K3 depended on a hosted provider (DigitalOcean endpoint, not pinned). Its valid runs came
  from several points in time under server-side conditions that were neither controlled nor
  measured (see `data/campaign/k3/MANIFEST.md`).
- Where `system_fingerprint` was not available (recorded as `null` in the artifacts), the
  full serving identity of the model is **not** known. A seed was sent but is not assumed to
  have been effective.
- The Z1 Python environment is a documented reconstruction (`tools/z2_extractor_requirements.txt`);
  the token extrapolation section of Z1 needs a local Ollama model store (see REPRODUCING.md).
- The extractor package `llm_arch` (Z1/Z2) is included as a file snapshot of the registered
  commit, without its development history (`code/`). The Triton conformance checker for Z3
  is not included; repeating the Z3 measurements (not the evaluation) needs it.

## Repository structure

| Path | Content |
|---|---|
| `README.md`, `MANIFEST.md`, `REPRODUCING.md` | Orientation, technical index, recomputation procedures |
| `docs/protokolle/` | Current versions of the four protocols / specifications |
| `docs/repo-kontext/` | Selected witness and procedure reports, plus the Z1 architecture model schema; index in its [`README.md`](docs/repo-kontext/README.md) |
| `freezes/z1/`, `freezes/z2/`, `freezes/z3/` | Protocol states at freeze time, extracted from git history |
| `data/z1/` | Z1 runs (K2, truncated K2, K3) and evaluation |
| `data/z2/` | Z2 inputs, instrument measurements, runs (K2/K3, B1) and rating; walkthrough in its [`README.md`](data/z2/README.md) |
| `data/soll/` | Z3 target model: the seven registered measurement inputs |
| `data/campaign/` | Z3 campaign: raw artifacts K1–K5, run manifests, clean-state runs, evaluation runs C11–C14 |
| `data/c3b-k2/`, `data/c3b-k3/` | Z3 clean-control stocks (C3b) for K2 and K3: the 52 control modules on the baseline, input of the C14 evaluation |
| `data/testrepo/` | Git bundles of the synthetic test repository |
| `data/checker/` | Reference to the checker state (no code, see its README) |
| `code/ma-llm-arch-extractor/` | Snapshot of the extractor `llm_arch` at the registered commit `5c0b65a` (Z1, Z2 fact bases), see [`code/README.md`](code/README.md) |
| `tests/fixtures/z1/` | Parse-assertion fixtures of the Z1 tools (used by `--selftest`) |
| `tools/` | Runner and evaluation tools as used, unchanged; plus `evaluate_z1_snapshot.py`, added for this package |
| `scripts/verify.sh` | Verification of this package |
## Synthetic test repository

`data/testrepo/` holds the git bundles of `ma-conformance-testrepo`: the clean baseline
`0d651041ed87dd03f2f78359713633fac01c0a66` (tag `baseline`) and 32 injection tags `inj/01`
to `inj/32`.

- The test repository was built for this study.
- It was not publicly accessible during the evaluation period.
- A later publication does not change this statement for the measurement made at that time.
- For future studies with models trained later, non-publication can no longer be assumed
  once the repository has been published.

## Public-release note

This repository is in a private, pre-release state. Before any public release, check in
particular the publication rights for the Triton/checker artifacts and any references to
the employer. No license has been added to this repository yet (the extractor snapshot
carries its own MIT license).
