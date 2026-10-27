# MANIFEST — Master Thesis Artifacts

Central index of the evidence package. Every entry can be cited in the thesis instead of an
external reference (e.g. "SSoT §2"): path in this repository, original path in the thesis
repository `masterarbeit`, freeze date, commit and full SHA256.

- **Source repository:** `masterarbeit`, state `f5dca31b41720f9b9204afebf285d162c36ee874`
  (05.10.2026), working tree clean. Only git-tracked files were copied.
- **Copy rule:** byte-identical, original relative path kept (`Path` = `Original path`
  unless stated otherwise). Freeze files were extracted with `git show <commit>:<path>`.
- **SHA256** of every file is in `SHA256SUMS`; the values below are the ones that matter
  for citation. Where a nested `SHA256SUMS` exists, it is the original from the thesis
  repository.

## Z1 — architecture model derivation

| Study | Role | Path | Original path | Date/Freeze | Commit | SHA256 | Notes |
|---|---|---|---|---|---|---|---|
| Z1 | Frozen protocol | `freezes/z1/z1_protokoll_extraktionsvergleich@34d6738.md` | `docs/protokolle/z1_protokoll_extraktionsvergleich.md` | Rev. 1, 31.08.2026 | `34d6738c1c295665d1dcf5036e58799df312ef8a` | `60cd6b3a255e148611cb5425e24c410db9d2e81235df75fc31e8cdf1fdba85c4` | Preregistration anchor |
| Z1 | Current protocol | `docs/protokolle/z1_protokoll_extraktionsvergleich.md` | same | Rev. 6, 01.09.2026 | `f5dca31` (source state) | `618ebde09d66201034013a0b7ed92c97df6b8234ab5c92c7588d2c574eca7679` | Amendments recorded in the protocol |
| Z1 | Freeze witness report | `docs/repo-kontext/z1_p_bericht_freeze.md` | same | 31.08.2026 | — | `244ee3065c62c8e08e3eca819ee6e5e31cf9aea537de9e6b9334b6dfca703a28` | |
| Z1 | Architecture model schema | `docs/repo-kontext/z1_p_arch_model_schema.json` | same | — | — | `a83a84af306d647f2d4d9618a39f9b0059431015d3e5234bce931df642012ec0` | Measurement input |
| Z1 | Archive root | `data/z1/MANIFEST.md` | same | living document | — | `09e2c605620cb4fdef531238301da93acd71073bc77b8526501bec1d69374368` | Not hashed in the original by design |
| Z1 | Runs K2 | `data/z1/k2/` | same | — | — | see `data/z1/k2/SHA256SUMS` (85 entries) | qwen2.5-coder:7b, Ollama |
| Z1 | Runs K2, truncated | `data/z1/k2_trunkiert/` | same | 31.08.2026 | — | see `data/z1/k2_trunkiert/SHA256SUMS` (85 entries) | Evidence of the delivery failure (2 050 of 4 281 prompt tokens), kept on purpose |
| Z1 | Runs K3 | `data/z1/k3/` | same | — | — | see `data/z1/k3/SHA256SUMS` (85 entries) | nvidia-nemotron-3-super-120b, DigitalOcean |
| Z1 | Evaluation (JSON) | `data/z1/auswertung/z1_auswertung.json` | same | 01.09.2026 | — | `6e6e005f7e634ecb08ceb21bd89c51d6083a2e37cdef7e56e4ff8a07353264f0` | Output of `tools/evaluate_z1.py` |
| Z1 | Evaluation (Markdown) | `data/z1/auswertung/z1_auswertung.md` | same | 01.09.2026 | — | `18180bb4e64098977a56e1f89848f981592edc25181cf675bc73e464481d32b0` | |

## Z2 — architecture rule derivation

| Study | Role | Path | Original path | Date/Freeze | Commit | SHA256 | Notes |
|---|---|---|---|---|---|---|---|
| Z2 | Frozen protocol (content state) | `freezes/z2/z2_protokoll_regelableitung@793e573.md` | `docs/protokolle/z2_protokoll_regelableitung.md` | 02.09.2026 | `793e5734cc1157a7cae2e4a0aa3a0b8fb893efae` | `04690cd5a08b8c7bf61bc8d98253a344b64b05cf6ce9e85a68f4fea1e411d525` | Preregistration anchor; no Z2 run existed at this point |
| Z2 | Freeze note | `docs/protokolle/z2_protokoll_regelableitung.md` (contains the note) | same | 02.09.2026 | `35aff9bd777a204977a77ab7fc25df09e9983da6` | `862fdc3b7cfb264482db155575437edb25b1b436f92b5444b2137f1e332d9dde` | The note names commit and SHA256 of the frozen state |
| Z2 | Current protocol | `docs/protokolle/z2_protokoll_regelableitung.md` | same | — | `f5dca31` (source state) | `862fdc3b7cfb264482db155575437edb25b1b436f92b5444b2137f1e332d9dde` | Byte-identical to the state at `35aff9b` |
| Z2 | Freeze witness report (Anhang A) | `docs/repo-kontext/s3_bericht_anhang_a_freeze.md` | same | 02.09.2026 | — | `9da4a27d3e2bd88065574ab43ec84f8fc539ceadf5362abad946ae15ecb97739` | |
| Z2 | Archive root | `data/z2/MANIFEST.md` | same | living document | — | `8d90dfc2687758d5016871b9f1b7261d9af7b4a33460b611dd3d45be9b8b8081` | |
| Z2 | Input: actual model | `data/z2/eingaben/ist_modell.yaml` | same | 02.09.2026 | — | `146dbb055e059b9dd948b27e185f33a2cb56557a534c55e0daf983c892336673` | Exported by Triton's editor (data, not code) |
| Z2 | Input: fact base | `data/z2/eingaben/input_facts.json` | same | 02.09.2026 | — | `f670593a7add275c364ebff5a5529cb95a787a10de5e0c80f97cd46574eb282a` | 52 records, after stage 0 + 0b |
| Z2 | Input: raw fact base | `data/z2/eingaben/input_facts_raw.json` | same | 02.09.2026 | — | `85b7a2c1834b4f954a630f3ff3ccf01ebc139a9f51039365b7759f7fbcc28951` | 73 records, provenance |
| Z2 | Instrument measurement | `data/z2/messungen/tokenmessung_2026-09-02.json` | same | 02.09.2026 | — | `a9625d88ec0746b90b9e21955c69fad9bc078431e24a3b58a8b10ebc0461b280` | |
| Z2 | Runs K2, B1 | `data/z2/k2_b1/` | same | — | — | see `data/z2/k2_b1/SHA256SUMS` (15 entries) | |
| Z2 | Runs K3, B1 | `data/z2/k3_b1/` | same | — | — | see `data/z2/k3_b1/SHA256SUMS` (15 entries) | |
| Z2 | Evaluation | `data/z2/bewertung/auswertung.json` | same | — | — | `ed75e49d797dfda69931f390fef86818c0f4e6e63d42458da4cc41258e71043e` | |
| Z2 | Completed rating sheet | `data/z2/bewertung/bewertungsblatt.md` | same | — | — | `72ebc3170f484a391a1d991c4fa155d57d04f6bfc5374c609ac8d601c109c029` | |
| Z2 | Overlap matrix | `data/z2/bewertung/ueberlappmatrix.md` | same | — | — | `57031cb7515519d91184d4111588c60025175f6d815a66549ccaa03acf7abe23` | |
| Z2 | Assignment key | `data/z2/bewertung/zuordnungsschluessel.json` | same | — | — | `0215a8b2ed377df1e4e074dd5f489c58a7341fc93e54362b61fcef8b78a320f2` | |

## Z3 — architecture violation detection

| Study | Role | Path | Original path | Date/Freeze | Commit | SHA256 | Notes |
|---|---|---|---|---|---|---|---|
| Z3 | Frozen protocol | `freezes/z3/eval_protokoll_phase04@3e17f44.md` | `docs/protokolle/eval_protokoll_phase04.md` | Rev. 33, 27.08.2026 | `3e17f44e0cee551d11e29f19a932db1cdff10648` | `2cb0385f08e88333863d83d0819943e352d3f1b857d4870801211b4817ac181e` | Preregistration anchor; commit and hash from `c5b_bericht_protokoll_freeze.md` §3; the only commit in history with this hash |
| Z3 | Current protocol | `docs/protokolle/eval_protokoll_phase04.md` | same | Rev. 48, 01.09.2026 | `f5dca31` (source state) | `fd0a6b4e6638022e70da6d8ff5f0cd66930a6264d63fa4db0e02bc222ca899b0` | Amendments Rev. 34–48 recorded in protocol §10 |
| Z3 | Evaluation specification | `docs/protokolle/c6_auswertungsspezifikation.md` | same | — | `f5dca31` (source state) | `39822edc0d9c109d7f1c1cfc285af9dd1363ec48b1a96a69334c173cd2cd71c7` | |
| Z3 | Freeze witness report | `docs/repo-kontext/c5b_bericht_protokoll_freeze.md` | same | 27.08.2026 | — | `b68bb20b58952bf35e603b828504b7f4e8263936a3acb1151246485976ad76b4` | Table of all protocol hashes per revision |
| Z3 | Target model (Soll) index | `data/soll/MANIFEST.md` | same | — | — | `7bb1332e481e42ad672f6d3e38d935e262e14648e262e818b0f747117192077f` | |
| Z3 | Soll: architecture rules | `data/soll/architecture-rules.yaml` | same | — | — | `72fa851ffd9eae3865827f959e962f564216fe48948e792944537d64a8d87b95` | Measurement input 1/7 |
| Z3 | Soll: Ilograph model | `data/soll/depot_soll.ilograph.yaml` | same | — | — | `e97013685ff217d85095b637459a2eb02d2f4effb9f9ad44d1f45798144ec25d` | Measurement input 2/7 |
| Z3 | Soll: import-linter | `data/soll/importlinter.ini` | same | — | — | `0c9a1e0e0430ff01e8383407ec6212c58ddcbec6e529db7b044a30132b528751` | Measurement input 3/7 |
| Z3 | Soll: architecture test | `data/soll/test_architecture.py` | same | — | — | `7504e30ce993803f4f3dab3023ed60742fcbd2382b9deb481d1860a67186a289` | Measurement input 4/7 |
| Z3 | Soll: control files | `data/soll/control_files.txt` | same | — | — | `7356e6d332e5165acdfdcfac1a66bd9803a7fa36cb4b3e7d5480bcb3526fee62` | Measurement input 5/7 |
| Z3 | Soll: injection manifest (md) | `data/soll/injection_manifest.md` | same | — | — | `63425d5501c8f5c13459e78782e370981db8e4aa68072aae46137550b98629e1` | Measurement input 6/7 |
| Z3 | Soll: injection manifest (json) | `data/soll/injection_manifest.json` | same | — | — | `2744116e513c9e79e3174e6e3681abdcdc7c18f36d00b6d334875e4e918cfb1f` | Measurement input 7/7 |
| Z3 | Campaign index | `data/campaign/MANIFEST.md`, `data/campaign/README.md` | same | — | — | `36d6e80561a3d1f259a85db6ccf76e91224b5477cbcbd0784c0236ca3578415e`, `5db059bcbc9d163275fe084ece610ccce45e7c74d070974f08d191c508f7a0c9` | |
| Z3 | Campaign journal | `data/campaign/journal.jsonl` | same | — | — | `e594e77dbe94197616ac6963fa253f6d083f66bb56899fba861962f0297d3335` | |
| Z3 | Raw artifacts K1–K5 | `data/campaign/k1/` … `data/campaign/k5/` | same | 27.–28.08.2026 | — | see `SHA256SUMS` in each directory | Nested sums use repository-root paths |
| Z3 | Run manifests | `data/campaign/manifests/` | same | — | — | top-level `SHA256SUMS` | No nested sum in the original |
| Z3 | Control runs | `data/campaign/control/` | same | — | — | see `data/campaign/control/SHA256SUMS` (14 entries) | |
| Z3 | Clean-control stock K2 (C3b-K2) | `data/c3b-k2/` | same | 24.08.2026 | last change `82f69d4b0f7045cec197935fbc87ccf0bc7a6532` | `SHA256SUMS` `03470aa6c2e8f2aa986de3ad64314bae34cc9b0cd29cf7a4f91e555ab76205d9` (109 entries) | 52 control modules, Ollama; input of `evaluate_campaign.py` (`--control-k2`); copied from source state `f5dca31`, 111 files |
| Z3 | Clean-control stock K3 (C3b-K3) | `data/c3b-k3/` | same | 25.08.2026 | last change `74e2b10ce5133da4f35777fcbcb2f458c84a9afc` | `SHA256SUMS` `e7c3a8bfd6d3737010f69708ec9f158d9f46843ed037b550e1d8e08e79afe5fb` (105 entries) | 52 control modules, DigitalOcean; input of `evaluate_campaign.py` (`--control-k3`); copied from source state `f5dca31`, 107 files |
| Z3 | Evaluation run C11 (run 1) | `data/campaign/eval/c11_eval_full.json` / `.md` | same | 28.08.2026, protocol Rev. 39 | — | `ad8f0483ffd2c261d8e33a21c425c5f6a492dedae0cc99c4e135dc56b371ea30` / `3d4874842a5baf92d455c1140b4874d396550fe87c50714d537a15a0a0e595af` | Superseded, validly archived; report `c11_bericht_auswertungslauf.md`, diagnosis `c11a_bericht_diagnose.md` |
| Z3 | Evaluation run C12 (run 2, order C11b) | `data/campaign/eval/c12_eval_full.json` / `.md` | same | 28.08.2026, Rev. 41 | — | `12751c3e506e3f28d4d32c7c4a104e97c826dad4e71c83f00dc49d200b09f0c7` / `afe28bc2d3d81da4b565d0b2f735745f09422f39523de2f44b27e2c80c921918` | Superseded, validly archived; report `c11b_bericht_zweiter_lauf.md` |
| Z3 | Evaluation run C13 (run 3, order C11c) | `data/campaign/eval/c13_eval_full.json` / `.md` | same | 28.08.2026, Rev. 43 | — | `873893e771f3dd8a1a195b283f874858990dcd27a75a1c348fa85a1c1914977c` / `f8cd9c074353cefcfe52d55e0df06a76b41c3f4ff75164c3ee1e5777f414c8a2` | Superseded, validly archived; reports `c11c_bericht_dritter_lauf.md`, `c11d_bericht_befund08_grundlagen.md` |
| Z3 | **Evaluation run C14 (canonical)** | `data/campaign/eval/c14_eval_full.json` / `.md` | same | 28.08.2026, Rev. 45 | — | `46ba024d266398cea278103592daf12c2a04193f9b45caa4812ce20333cc0a71` / `ed59aa95f01b2a73e773110e5aa56b45b6d687c49f812dcca1bad8ed65e2329b` | **Canonical result**; report `c14_bericht_vierter_lauf.md` |
| Z3 | Evaluation index | `data/campaign/eval/README.md` | same | 28.08.2026 | — | `6ae1d15b6d1e8764451885f5035f017f6bfdcca5be0b2323688d3eb034aa24b4` | Explains the repair chain C11 → C12 → C13 → C14 |
| Z3 | Checker state | `data/checker/README.md` (reference only) | `data/checker/` | tag `phase04-freeze` | `348ca9daa456af4954f11f7152fc45201035297e` | bundle: `68561a86005474ebfceabd8d6fce2a7809297c3578b05d89e8ec35c4605faf85` | Bundle **not included** (third-party code, rights open) |
| Z3 | Test repository, baseline bundle | `data/testrepo/ma-conformance-testrepo-baseline.bundle` | same | 14.08.2026 | baseline `0d651041ed87dd03f2f78359713633fac01c0a66` | `597fa466c5ff4e05ab5c1f3550fb88e0407c3968fae8fafd420166324d4a7b18` | 4 refs, complete history |
| Z3 | Test repository, injections bundle | `data/testrepo/ma-conformance-testrepo-injections.bundle` | same | — | baseline `0d651041ed87dd03f2f78359713633fac01c0a66` | `1b9f8b58f271332e2d66ead83a3858271a04f3aebce95b7927977d9fa1be508b` | 37 refs, tags `inj/01`–`inj/32` |

## C11–C14 repair chain — reports

| Order | Report | SHA256 |
|---|---|---|
| C11 | `docs/repo-kontext/c11_bericht_auswertungslauf.md` | `72d3e2c157abf0c602128e200df5cd8051ed7af899dd20c7d7ca3045baa15c55` |
| C11a | `docs/repo-kontext/c11a_bericht_diagnose.md` | `b12702c376ee102ae8ceb83c758706a3f705fc9e88d6fa472f3aa0123591d929` |
| C11b | `docs/repo-kontext/c11b_bericht_zweiter_lauf.md` | `3dd09387977897d14e966139b28e87cd2c03542c0172d23b55237c10bf6dbc77` |
| C11c | `docs/repo-kontext/c11c_bericht_dritter_lauf.md` | `3456ea852e32d3b1c6828c8de3c34f0edf587170ef0ae256c925c5fbfa5d9bc2` |
| C11d | `docs/repo-kontext/c11d_bericht_befund08_grundlagen.md` | `6c5813fea6a6e3de93742d2a0a1105f7b4ffd251f83e7c3e33b8eb5a265ba2cb` |
| C14 | `docs/repo-kontext/c14_bericht_vierter_lauf.md` | `58b0c2b40763d22bd24103050dcb941be65468e322b5bccabbbd5a396c03425d` |

## Tools

Copied unchanged from `tools/` at the source state. They are the **current** versions, not
necessarily the versions of every individual run. The run reports name the tool hash used.

| Tool | Status | Note |
|---|---|---|
| `run_z1.py`, `evaluate_z1.py`, `check_z1_delivery.py`, `z1_tokenizer.py` | included | Z1 |
| `run_z2.py`, `reduce_facts.py`, `measure_prompt_tokens.py`, `prepare_z2_review.py`, `tally_z2_review.py`, `prepare_z2_overlap.py`, `tally_z2_overlap.py`, `z2_extractor_requirements.txt`, `fixtures/z2/` | included | Z2; named in `data/z2/MANIFEST.md`; fixtures are used by `run_z2.py` |
| `run_campaign.py`, `campaign_spec.py`, `postrun_check.py`, `validate_soll.py`, `build_control_set.py`, `generate_soll.py`, `evaluate_control_run.py` | included | Z3 runs and Soll |
| `evaluate_campaign.py` | included | `b66be750f9b7cf524b9afa8edbab0138d17c409de4637465eb82d0f079a93428` = the version of the canonical run C14 |
| `match_k4k5.py` | included | `c16e7c4380034163f3034916193bd96cfc6bb957768fe610cb7018d7799f4ca6` = the version of runs 2–4 |
| `check_doc_invariants.py` | included | Current state, see the table below |

### `check_doc_invariants.py` — current state and the state registered for C14

| Study | Role | Path | Original path | Date/Freeze | Commit | SHA256 | Notes |
|---|---|---|---|---|---|---|---|
| Z3 | Invariant checker, state of C11–C14 | `freezes/z3/tools/check_doc_invariants@02d8fc8.py` | `tools/check_doc_invariants.py` | 28.08.2026, 11:01 | `02d8fc8d3eed1a8bd5925a25a48ee9aec4b5c51d` | `6cc16ef9c041b8721500fc521a437ea090fcacd209cf275561f673a1e52b7018` | Extracted with `git show`. `02d8fc8` is the only commit that produced this byte state; it was valid until `f328761` (31.08.2026), so it covers C14 (28.08.2026, 23:49). Hash registered in `data/campaign/eval/README.md` for all four runs |
| Z1/Z3 | Invariant checker, current | `tools/check_doc_invariants.py` | same | 31.08.2026, 15:27 | `f328761` | `c351a137e3f32e00b67e8f73d7cce0777f607c872fda4a7719c1b142b8707fdf` | Later state, not the one used by C14 |

The later state (`f328761`, "feat: check the Z1 protocol hash in the document invariants")
only adds the Z1 invariant (F): it checks the SHA256 of the frozen Z1 protocol against
`z1_p_bericht_freeze.md` §3. To reuse the existing lookup, the helper
`expected_protocol_hash()` now takes the report and protocol name as parameters. Invariant (A)
calls it with the previous fixed values, so its behaviour is unchanged. Invariants (A)–(E)
are not otherwise touched (`git diff 02d8fc8 f328761 -- tools/check_doc_invariants.py`,
42 insertions, 6 deletions).
| `z2_tokenizer.py` | **not present** in the source repository | Not recreated |
| `analyze_control_findings.py`, `describe_campaign.py`, `postcheck_run.py`, `bundle-docs.sh` | not included | Not referenced by any measurement document, or document tooling only |
| `z4_generate_soll.py` | not included | Z4 |

External dependencies not included: the extractor package `llm_arch` (Z1/Z2) and the Triton
conformance checker (Z3).

## Deliberately not included

- `docs/repo-kontext/` beyond the positive list above (138 files in the source repository).
- `data/checker/*.bundle`, `data/checker/MANIFEST.md`, `data/checker/SHA256SUMS` — see `data/checker/README.md`.
- `data/z4/` and everything else Z4-related.
- Other `data/` directories of the source repository (`befund06`, `befunde01-05`, `c3b`,
  `manifest`, `z1_s_diagnose`): preparatory or diagnostic material outside the three measurements.
  `data/c3b/` holds the four aborted C3b attempts. The clean-control stocks `data/c3b-k2/`
  and `data/c3b-k3/` **are included** (see Z3 above), because the C14 evaluation reads them.
- Untracked `__pycache__/` directories.
