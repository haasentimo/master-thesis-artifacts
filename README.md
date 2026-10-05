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
  reported results. The Z3 evaluation can be rerun from the included campaign artifacts,
  while parts of Z1 depend on the separately versioned `llm_arch` extractor.
- A byte-identical regeneration of all model responses is **not** claimed.
- K3 depended on a hosted provider (DigitalOcean endpoint, not pinned). Its valid runs came
  from several points in time under server-side conditions that were neither controlled nor
  measured (see `data/campaign/k3/MANIFEST.md`).
- Where `system_fingerprint` was not available (recorded as `null` in the artifacts), the
  full serving identity of the model is **not** known. A seed was sent but is not assumed to
  have been effective.
- The tools depend on code outside this package (the extractor package `llm_arch` for Z1/Z2
  and the Triton conformance checker for Z3), which is not included.

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
| `data/testrepo/` | Git bundles of the synthetic test repository |
| `data/checker/` | Reference to the checker state (no code, see its README) |
| `tools/` | Runner and evaluation tools as used, unchanged |
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
   `data/z2/`, `data/soll/` and `data/testrepo/` use paths relative to their own directory;
   those under `data/campaign/` use paths relative to the repository root, so they are
   checked from there;
3. the three frozen protocols in `freezes/` against the SHA256 recorded at freeze time.

It exits non-zero on the first mismatch and changes no file.

## Public-release note

This repository is in a private, pre-release state. Before any public release, check in
particular the publication rights for the Triton/checker artifacts and any references to
the employer. No license has been added yet.
