# Examiner package

This directory holds **no bundle**. It describes material that is handed to the
examiners separately, on the submission medium, and that is not part of this repository.

| # | Item | Why it is separate |
|---|---|---|
| 1 | Full `git bundle --all` of the private thesis repository (`masterarbeit`) | Keeps the commit history in which the protocol freezes were made (`34d6738`, `793e573`/`35aff9b`, `3e17f44`), so `git show <commit>:<path>` can be repeated independently. |
| 2 | Bundle of the Triton/checker state used (`tritongraph`, commit `348ca9daa456af4954f11f7152fc45201035297e`) — **only if legally allowed** | Third-party code; publication rights not yet settled. See [`data/checker/README.md`](../data/checker/README.md). |
| 3 | Further artifacts that cannot be published | Case by case. |

Local copies of these files may be placed in `examiner-package/local-only/`. That path is
listed in `.gitignore` so that the bundles do not end up on GitHub by accident. They are
not covered by the top-level `SHA256SUMS`.

## Checking the thesis repository bundle

```bash
git bundle verify masterarbeit.bundle
git clone masterarbeit.bundle masterarbeit && cd masterarbeit
git show 3e17f44:docs/protokolle/eval_protokoll_phase04.md | sha256sum
# expected: 2cb0385f08e88333863d83d0819943e352d3f1b857d4870801211b4817ac181e
```
