# `code/` — extractor snapshot

`ma-llm-arch-extractor/` is a file snapshot of the extractor package `llm_arch` at the commit
registered for Z1 (protocol section 6.1, `EXPECTED_HEAD` in `tools/evaluate_z1.py`):

- **Source:** repository `ma-llm-arch-extractor` (private), commit
  `5c0b65a82cc3d8af47c022d779ff63d8a20a9e08` (31.08.2026, "docs: correct the stale
  expected.json references").
- **Extraction:** `git archive 5c0b65a… -- <paths>`, i.e. versioned files only, byte-identical
  to the commit's blobs. No file was edited. The development history is **not** included.
- **Integrity:** `ma-llm-arch-extractor/SNAPSHOT.json` lists the git blob SHA1, SHA256 and size
  of each of the 59 files. The blob SHA1 can be checked against the original commit
  (`git ls-tree -r 5c0b65a`) by anyone with access to it. Without access, the cross-check is
  the 28 blobs registered in `tools/run_z1.py` (`REGISTERED_BLOBS`, protocol sections 3.1/3.2)
  and the six instrument blobs recorded in `data/z1/auswertung/z1_auswertung.json`. All of
  them match. `scripts/verify.sh` and `tools/evaluate_z1_snapshot.py` check the snapshot
  against `SNAPSHOT.json`.
- **License:** MIT, see `ma-llm-arch-extractor/LICENSE`. It applies to the snapshot.

## Used for

| Study | Use |
|---|---|
| Z1 | Fact extraction, `ArchModel` schema, prompt, validation (`validate_arch`), metrics (`fact_fidelity`, `compression`, `gold_similarity`), Ilograph reader, `scripts/compare_runs.py`; fixture `rich_repo` with Triton export, gold reference and `PROVENANCE.md` |
| Z2 | `extract_repo` for the B1 fact base `data/z2/eingaben/input_facts_raw.json` |

## Included

| Path | Why |
|---|---|
| `src/llm_arch/` (complete package) | Imported by `tools/evaluate_z1.py` and `tools/run_z1.py`; the package `__init__` modules import their siblings, so it is kept whole |
| `fixtures/rich_repo/`, `fixtures/rich_repo.full.ilograph.yaml`, `fixtures/rich_repo.gold.json`, `fixtures/PROVENANCE.md` | Measurement input of Z1 (approach 1, fact base) and its provenance |
| `fixtures/sample_repo/` | Synthetic test fixture of the extractor's own tests (9 small files) |
| `scripts/compare_runs.py` | Called unchanged by `evaluate_z1.py` as a cross-check |
| `tests/` | `test_reader.py` holds the registered E1/E2 values; the other tests cover schema, validator, metrics and logger. 41 tests pass. `test_provider_smoke.py` calls a local Ollama server and is skipped if none runs |
| `pyproject.toml`, `LICENSE` | Declared dependencies (lower bounds only) and license |

## Excluded

| Path in the commit | Reason |
|---|---|
| `README.md`, `DEFERRED.md`, `docs/befunde_log.md`, `docs/runs-archive-manifest.md` | Development notes and logs, not needed for any measurement |
| `scale-probe/` | Formative diagnostic (token-fit probe), not part of Z1 or Z2 |
| `fixtures/sample_repo.ilograph.yaml` | Not used by any test or tool |
| `.gitignore` | Repository housekeeping |
| `runs/`, `.env` (untracked in the original working tree) | Formative June runs and local credentials; never versioned, never copied |

## Dependencies

The package declares only lower bounds (`pydantic>=2.0`, `ruamel.yaml>=0.18`, `openai>=1.0`,
`typer>=0.12`). No lockfile exists in the original repository. The pinned environment
`tools/z2_extractor_requirements.txt` (Python 3.12.3) is a documented reconstruction. With it
the snapshot reproduces the archived Z1 evaluation and the Z1/Z2 fact bases byte for byte
(see the main [`README.md`](../README.md)).
