# `docs/repo-kontext/` — selected reports

Added for the artifact package. The reports here are copied **unchanged** from the private
thesis repository (state `f5dca31`). They are in German and were written while the work was
carried out. They are kept because they document a measurement, a freeze or an evaluation
step that the archived data alone does not explain. SHA256 values are in
[`MANIFEST.md`](../../MANIFEST.md).

## Included

| Report | Study | Why it is here |
|---|---|---|
| [`z1_p_bericht_freeze.md`](z1_p_bericht_freeze.md) | Z1 | Freeze witness of the Z1 protocol |
| [`z1_p_arch_model_schema.json`](z1_p_arch_model_schema.json) | Z1 | Archived `ArchModel` schema, a measurement input |
| [`z1_t_bericht_kontextfenster.md`](z1_t_bericht_kontextfenster.md) | Z1 | Context window as a measurement input: why `k2_trunkiert` is a delivery failure and under which condition the block `k2` was run |
| [`s3_bericht_anhang_a_freeze.md`](s3_bericht_anhang_a_freeze.md) | Z2 | Freeze witness of the Z2 protocol (Anhang A) |
| [`c4b_bericht_injektionen.md`](c4b_bericht_injektionen.md) | Z3 | Construction and structural checks of the 32 injection commits |
| [`c3b_k2_bericht_kontrolllauf.md`](c3b_k2_bericht_kontrolllauf.md) | Z3 | Control run K2 over the 52 control modules (false-positive base rate), data in `data/c3b-k2/` |
| [`c3b_k3_bericht_kontrolllauf.md`](c3b_k3_bericht_kontrolllauf.md) | Z3 | Control run K3, data in `data/c3b-k3/` |
| [`c5b_bericht_protokoll_freeze.md`](c5b_bericht_protokoll_freeze.md) | Z3 | Freeze witness of the Z3 protocol, with all protocol hashes per revision |
| [`c10_bericht_kampagne.md`](c10_bericht_kampagne.md) | Z3 | Procedure of the campaign K1–K5: measurement state, order, repetitions, incidents |
| [`c11_bericht_auswertungslauf.md`](c11_bericht_auswertungslauf.md) | Z3 | Evaluation run 1 |
| [`c11a_bericht_diagnose.md`](c11a_bericht_diagnose.md) | Z3 | Diagnosis of run 1 (nine instrument defects) |
| [`c11b_bericht_zweiter_lauf.md`](c11b_bericht_zweiter_lauf.md) | Z3 | Evaluation run 2 |
| [`c11c_bericht_dritter_lauf.md`](c11c_bericht_dritter_lauf.md) | Z3 | Evaluation run 3 |
| [`c11d_bericht_befund08_grundlagen.md`](c11d_bericht_befund08_grundlagen.md) | Z3 | Mechanical recount that led to run 4 |
| [`c14_bericht_vierter_lauf.md`](c14_bericht_vierter_lauf.md) | Z3 | Canonical evaluation run 4 (C14) |

## Referenced but not included

Some included documents link to files of the thesis repository that are not part of this
package. These links stay **dangling on purpose**; the documents are originals and are not
edited. Every target below exists in the thesis repository at `f5dca31`, so none of them is a
wrong path. They were left out because the published results do not depend on them.

| Target | Linked from | Kind | Why not included |
|---|---|---|---|
| `docs/repo-kontext/k2_machbarkeitslauf_bericht.md`, `k3_machbarkeitslauf_direktzugang_bericht.md` | `data/c3b-k2/MANIFEST.md`, `data/c3b-k3/MANIFEST.md`, both C3b reports | historical working report | Feasibility runs on five files before the control runs; the control runs themselves are documented |
| `docs/repo-kontext/4b4_bericht_baseline_billing.md` | `data/testrepo/MANIFEST.md` | historical working report | Construction step of the baseline; the baseline itself is archived as a bundle |
| `docs/repo-kontext/4c_bericht_soll_und_validator.md`, `c2a_bericht_regeldatei.md`, `c2b_bericht_k4_konfiguration.md`, `c2c_bericht_k5_konfiguration.md`, `c3a_bericht_clean_state_audit.md` | `data/soll/MANIFEST.md` | historical working report | How the target model was built; the seven inputs and their index `data/soll/MANIFEST.md` are included |
| `docs/repo-kontext/c4c_bericht_vorabpruefung.md` | `data/soll/injection_manifest.md`, `c5b_bericht_protokoll_freeze.md` | historical working report | Pre-check of the expected match keys against the deterministic engine, made before the campaign; the evaluation does not depend on it |
| `docs/repo-kontext/c5_bericht_freeze.md` | `c5b_bericht_protokoll_freeze.md` | historical working report | Earlier freeze report; `c5b_bericht_protokoll_freeze.md` is the witness |
| `docs/repo-kontext/c6b1_bericht_nachtraege.md` | `data/campaign/control/MANIFEST.md` | historical working report | Addenda before the evaluation harness; the clean-state runs it added are in `data/campaign/control/` |
| `docs/repo-kontext/c10a_bericht_validator_punkt6.md` | `data/campaign/MANIFEST.md`, `data/campaign/k2/MANIFEST.md` | historical working report | A validator fix during the campaign; summarised in `c10_bericht_kampagne.md` |
| `docs/kapitel/kapitel7_tabellenskelette.md` | `data/campaign/control/MANIFEST.md` | thesis chapter draft | Table skeletons of chapter 7; the filled tables are in `data/campaign/eval/c14_eval_full.md` |
| `data/checker/MANIFEST.md` | `data/testrepo/MANIFEST.md` | deliberately excluded | Describes the third-party checker bundles; see `data/checker/README.md` |
| `tools/describe_campaign.py` | `c11d_bericht_befund08_grundlagen.md` | deliberately excluded | Documentation helper, not a measurement or evaluation tool |
