# `data/checker/` — Conformance checker (Triton) measurement state

The Z3 campaign measured with the conformance checker of the `tritongraph` monorepo.

| Item | Value |
|---|---|
| Measurement state | `phase04-freeze` |
| Commit | `348ca9daa456af4954f11f7152fc45201035297e` (`feat: run the llm path over unchanged control files`) |
| Branch | `feat/conformance-checker` of `tritongraph` (owned by the first supervisor, not by the author) |
| Logged in every campaign record as | `checker_git_head = 348ca9d` |

## Not included in this repository

The thesis repository keeps two full `git bundle --all` backups of the `tritongraph` monorepo
under `data/checker/`. They contain third-party source code. Their publication rights have
not been settled yet, so they are **deliberately not part of this curated repository**.
The original `data/checker/MANIFEST.md` and `data/checker/SHA256SUMS` are left out too, since
they only describe these two bundles.

The hashes recorded in the thesis repository identify the bundles:

```
68561a86005474ebfceabd8d6fce2a7809297c3578b05d89e8ec35c4605faf85  tritongraph-348ca9d.bundle   (measured state)
b480e2c6199c3c50cd25835ae8079ff821452efa33fc2f6d29ef531a4dfc2671  tritongraph-fe66357.bundle   (earlier backup, verification run B4)
```
