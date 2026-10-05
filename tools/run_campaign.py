#!/usr/bin/env python3
"""C7 — campaign runner for the five configurations K1…K5 over the 32 injection commits.

Executes the invocation lines pre-registered in `eval_protokoll_phase04.md` §6 (rev. 24, as
corrected by rev. 32), pulled from `campaign_spec.py`. The runner CHOOSES nothing about the
measurement: graph mode is derived from the manifest category, `--base` is always the
baseline SHA, repetition counts and timeouts come from the protocol.

    tools/run_campaign.py --plan                 full run matrix, executes NOTHING
    tools/run_campaign.py --run [filters]        executes, with per-run preconditions
    tools/run_campaign.py --run --smoke-test     marks the artefacts as a smoke test

Measured is the FREEZE WORKTREE `~/ma/tritongraph-measure` at tag `phase04-freeze`, never the
working tree of the checker; every run manifest carries `phase04-freeze = <SHA>` (C5).

Two obligations shape the design, both of them protocol text:

  * `--json-out` is REPLACED, not appended (`jsonOut.ts`). A target path collision is
    therefore silent data loss, and the plan mode refuses to run before it happens.
  * K4 and K5 write no `run_header`. Their only evidence is stdout/stderr, which §6 Nachtrag
    Rev. 30 (2) requires verbatim and complete — not `stdout_tail`, not pre-parsed.

Nothing here evaluates a measurement. Validity is decided by `postrun_check.py` alone
(protocol §6 Nachtrag Rev. 24), which this runner calls after each run and whose verdict it
records in the journal.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import campaign_spec as spec  # noqa: E402
import validate_soll as soll_model  # noqa: E402

MA = Path(__file__).resolve().parent.parent

# THE MEASUREMENT PATH IS THE FREEZE WORKTREE, not the working tree of the checker (C5).
# `git worktree add ../tritongraph-measure phase04-freeze` puts the tagged state on disk
# detached, so the campaign cannot be moved by a `pull`, `checkout`, `merge` or editor commit
# in `~/ma/tritongraph` while it runs. The gate that admits this path is the build hash:
# built in the worktree, `dist/cli.js` came out at the registered
# `c0bbdfeb…d35d95` (C5 §2), byte-identical to the working tree.
CHECKER_REPO = MA.parent / "tritongraph-measure"
FREEZE_TAG = "phase04-freeze"
CHECKER_PKG = CHECKER_REPO / "packages" / "triton-conformance"
CLI_JS = CHECKER_PKG / "dist" / "cli.js"
TESTREPO = MA.parent / "ma-conformance-testrepo"
VENV_BIN = MA.parent / "venv" / "bin"
SOLL = MA / "data" / "soll"

# THE ARCHIVE ROOT IS VERSIONED, not scratch (C5c). §6 point 4 obliges the campaign to keep the
# raw logs; a scratch directory is volatile and does not carry them — C4c lost its raw output that
# way. `data/campaign/` sits in the repo next to `data/c3b-k2/`, one subdirectory per configuration.
# Overridable via `--out`, so a smoke test can be kept out of the archive.
CAMPAIGN_OUT = MA / "data" / "campaign"

CONFIGS = ("K1", "K2", "K3", "K4", "K5")


class Abort(RuntimeError):
    """A precondition failed. The protocol asks for an abort, not a warning."""


def now() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git(repo: Path, *args: str) -> str:
    r = subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True)
    if r.returncode != 0:
        raise Abort(f"git {' '.join(args)} in {repo} failed: {r.stderr.strip()}")
    return r.stdout.strip()


# ── the run matrix ────────────────────────────────────────────────────────────────────

def load_matrix(manifest_path: Path) -> list[dict]:
    """One entry per (injection, configuration) — 32 × 5 = 160 invocations.

    Graph mode is derived here and nowhere else (protocol §6 Nachtrag Rev. 31).
    """
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    rows: list[dict] = []
    for inj in manifest["injections"]:
        mode = spec.graph_mode(inj["category_l1"])
        # (a) of C5, extended by rev. 35 — the THREE per-commit expectations of the Soll
        # validator, carried on the row so the plan can print them and `run_soll_validator`
        # judges against the same values. All three are DERIVED from registered documents,
        # never chosen here: (7) and (8) out of the manifest, (6) out of the manifest and the
        # Soll whitelist.
        exp_cycles = spec.expected_cycles(inj["id"])
        exp_edge = spec.expected_whitelist_edge(inj)
        exp_importers = sole_importer_expectations(inj)
        for config in CONFIGS:
            rows.append({
                "config": config,
                "injection_id": inj["id"],
                "tag": inj["injection_ref"],
                "sha": inj["injection_sha256"],
                "category_l1": inj["category_l1"],
                "scenario_l2": inj["scenario_l2"],
                "carrier_module": inj["carrier_module"],
                "manifest_entry": inj,
                "expected_cycles": exp_cycles,
                "expected_whitelist_edge": exp_edge,
                "expected_sole_importers": exp_importers,
                "expected_edge_boundary_raw": inj.get("expected_edge_boundary"),
                "rule_graph_mode": mode if config == "K1" else
                                   ("diff" if config in ("K2", "K3") else None),
                "runs": spec.RUNS[config],
            })
    return rows


def artefact_paths(row: dict, out: Path, attempt: int) -> dict:
    """Target paths of one run. The K1/K2/K3 names are the ones registered in §6 Rev. 24.

    K4 and K5 have no registered output paths — the protocol notes explicitly that neither
    tool offers a structured output option (§6 Rev. 24, "Bewusste Lücken"), so the harness
    has to archive stdout and exit code itself. These names are the runner's, and they are
    reported as such.

    `attempt` > 1 lands on a NEW unique path. An invalid run is repeated, never overwritten
    (protocol §6 Nachtrag Rev. 24).
    """
    suffix = "" if attempt == 1 else f"_r{attempt}"
    cfg, sha = row["config"], row["sha"]
    d = out / cfg.lower()
    if cfg == "K1":
        stem = f"k1_{row['rule_graph_mode']}_{sha}{suffix}"
    else:
        stem = f"{cfg.lower()}_{sha}{suffix}"
    p = {"dir": d, "stem": stem, "manifest": out / "manifests" / f"{stem}.json"}
    if cfg in ("K1", "K2", "K3"):
        p["run_log"] = d / f"{stem}.jsonl"
        p["json_out"] = d / f"{stem}.json"
    else:
        p["stdout"] = d / f"{stem}.stdout.txt"
        p["stderr"] = d / f"{stem}.stderr.txt"
    return p


def build_argv(row: dict, paths: dict) -> tuple[list[str], dict]:
    """Returns (argv, extra environment). Every line comes out of `campaign_spec`."""
    cfg = row["config"]
    if cfg in ("K1", "K2", "K3"):
        argv = spec.checker_argv(
            cli_js=str(CLI_JS),
            topology=str(SOLL / "depot_soll.ilograph.yaml"),
            rules=str(SOLL / "architecture-rules.yaml"),
            mode=row["rule_graph_mode"],
            base_sha=spec.EXPECTED_BASELINE_SHA,
            runs=row["runs"],
            timeout_ms=spec.TIMEOUT_MS[cfg],
            run_log=str(paths["run_log"]),
            json_out=str(paths["json_out"]),
        )
        env: dict[str, str] = {}
        if cfg == "K2":
            env = dict(spec.K2_ENV)
        elif cfg == "K3":
            # Key first, as in the registered line (protocol §6 Nachtrag Rev. 32).
            env = {"CONFORMANCE_API_KEY": read_do_key(), **spec.K3_ENV}
        return argv, env
    if cfg == "K4":
        return spec.k4_argv(str(VENV_BIN), str(SOLL / "importlinter.ini")), {"PYTHONPATH": "src"}
    return (spec.k5_argv(str(VENV_BIN), str(SOLL / "test_architecture.py")),
            {"DEPOT_SRC": str(TESTREPO / "src")})


def read_do_key() -> str:
    """The K3 key out of `~/ma/.secrets/do.env` (`k3_machbarkeitslauf_direktzugang_bericht.md` §3)."""
    f = MA.parent / spec.K3_KEY_FILE
    if not f.exists():
        raise Abort(f"K3 key file missing: {f}")
    for line in f.read_text(encoding="utf-8").splitlines():
        line = line.strip().removeprefix("export ").strip()
        if line.startswith(f"{spec.K3_KEY_VAR}="):
            return line.split("=", 1)[1].strip().strip("'\"")
    raise Abort(f"{spec.K3_KEY_VAR} not found in {f}")


def render_line(row: dict, paths: dict) -> str:
    """The invocation as it will be executed, for the plan output and the run manifest.

    The K3 key is NEVER rendered — the placeholder of the protocol line stands in its place.
    """
    argv, env = build_argv(row, paths)
    shown = dict(env)
    if "CONFORMANCE_API_KEY" in shown and row["config"] == "K3":
        shown["CONFORMANCE_API_KEY"] = "<DO_MODEL_ACCESS_KEY aus ~/ma/.secrets/do.env>"
    prefix = " ".join(f"{k}={v}" for k, v in shown.items())
    return (prefix + " " if prefix else "") + " ".join(argv)


# ── plan mode ─────────────────────────────────────────────────────────────────────────

def check_star_shape() -> list[str]:
    """All 32 tags resolvable, each with exactly one parent = the baseline.

    Protocol §6 Amendment 12.08.: star history, `B` as the sole parent, NO merge — a linear
    chain would be cumulative and K4, K5 and K1-full would report every earlier injection
    along with the current one.
    """
    lines = []
    baseline = git(TESTREPO, "rev-parse", "baseline")
    if baseline != spec.EXPECTED_BASELINE_SHA:
        raise Abort(f"baseline {baseline} != registered {spec.EXPECTED_BASELINE_SHA}")
    lines.append(f"baseline {baseline}  OK")
    for n in range(1, 33):
        tag = f"inj/{n:02d}"
        sha = git(TESTREPO, "rev-parse", f"{tag}^{{commit}}")
        parents = git(TESTREPO, "rev-list", "--parents", "-n1", sha).split()[1:]
        if len(parents) != 1:
            raise Abort(f"{tag}: {len(parents)} parents — a merge breaks `git diff <parent>`")
        if parents[0] != baseline:
            raise Abort(f"{tag}: parent {parents[0]} != baseline")
        lines.append(f"{tag} {sha}  parent=baseline  OK")
    return lines


def plan(rows: list[dict], out: Path) -> int:
    print("=" * 100)
    print("C7 — RUN MATRIX (plan mode, nothing is executed)")
    print(f"generated : {now()}")
    print(f"out root  : {out}")
    print(f"testrepo  : {TESTREPO}")
    print(f"checker   : {CLI_JS}")
    print(f"freeze    : {FREEZE_TAG} = {git(CHECKER_REPO, 'rev-parse', FREEZE_TAG + '^{commit}')}"
          f"   (measurement path {CHECKER_REPO})")
    print("=" * 100)

    print("\n--- star shape of the 32 injection commits (protocol §6 Amendment 12.08.) ---")
    for line in check_star_shape():
        print(f"  {line}")

    # (a) of C5, rev. 35 — the abort criterion of the Soll validator, outside the code.
    # Points (1)-(5) are commit-invariant SOLL properties and every FAIL aborts; points (6),
    # (7) and (8) describe the CODE GRAPH of the actual state and deviate on an injection
    # commit BY THE INJECTION. All three expected values are printed here per injection, so
    # the criterion `run_soll_validator` applies can be checked against the protocol without
    # reading the runner.
    print("\n--- Soll validator expectations per injection (points (6), (7) and (8)) ---")
    print("    (7) cycle count of the actual state   — protocol §3 Nachtrag Rev. 29, "
          "`c4b_bericht_injektionen.md` §8.5")
    print("    (8) component edge outside the whitelist — `expected_edge_boundary` of the "
          "manifest entry")
    print("    (6) importer set of the guarded components — the whitelisted importer out of "
          "the Soll,")
    print("        plus the source of the registered edge on the component it targets "
          "(rev. 35)")
    print(f"    {'injection':<10} {'category_l1':<25} {'(7) cycles':<11} (8) expected edge")
    seen_inj: set[str] = set()
    for row in rows:
        if row["injection_id"] in seen_inj:
            continue
        seen_inj.add(row["injection_id"])
        edge = row["expected_whitelist_edge"] or "none"
        note = ("" if row["expected_whitelist_edge"] is not None
                else f"   [manifest: {row['expected_edge_boundary_raw']}]")
        print(f"    {row['injection_id']:<10} {row['category_l1']:<25} "
              f"{row['expected_cycles']:<11} {edge}{note}")
    print("\n    (6) expected importer sets, deviations from the resting state marked +")
    print(f"    {'injection':<10} guarded component and expected importers")
    seen6: set[str] = set()
    resting = sole_importer_expectations({})
    for row in rows:
        if row["injection_id"] in seen6:
            continue
        seen6.add(row["injection_id"])
        deltas = [(c, v) for c, v in sorted(row["expected_sole_importers"].items())
                  if v != resting[c]]
        if deltas:
            for component, importers in deltas:
                added = sorted(set(importers) - set(resting[component]))
                print(f"    {row['injection_id']:<10} + {component:<24} {importers}   "
                      f"(added: {', '.join(added)})")
        else:
            print(f"    {row['injection_id']:<10}   resting state, all five components "
                  f"at their whitelisted importer")
    touched = sorted({r["injection_id"] for r in rows
                      if r["expected_sole_importers"] != resting})
    print(f"    → resting state: " + ", ".join(f"{c}={v}" for c, v in sorted(resting.items())))
    print(f"    → {len(touched)} injections expect an added importer: {', '.join(touched)}")
    print("    → any other importer SET is a validator FAIL and ABORTS before a call comes "
          "into being")

    with_cycle = sorted({r["injection_id"] for r in rows if r["expected_cycles"]})
    with_edge = sorted({r["injection_id"] for r in rows if r["expected_whitelist_edge"]})
    print(f"    → {len(with_cycle)} injections expect a cycle: {', '.join(with_cycle)}")
    print(f"    → {len(with_edge)} injections expect an edge outside the whitelist: "
          f"{', '.join(with_edge)}")
    print("    → every other value is a validator FAIL and ABORTS before a call comes "
          "into being")

    print("\n--- target path uniqueness (`--json-out` is replaced, not appended) ---")
    seen: dict[Path, str] = {}
    collisions = []
    for row in rows:
        paths = artefact_paths(row, out, 1)
        for key in ("run_log", "json_out", "stdout", "stderr", "manifest"):
            p = paths.get(key)
            if p is None:
                continue
            owner = f"{row['config']}/{row['injection_id']}"
            if p in seen:
                collisions.append(f"{p} claimed by {seen[p]} and {owner}")
            seen[p] = owner
    if collisions:
        for c in collisions:
            print(f"  COLLISION {c}")
        raise Abort(f"{len(collisions)} target path collisions — silent data loss, aborting")
    print(f"  {len(seen)} target paths, all distinct  OK")

    print("\n--- the matrix ---")
    calls = 0
    for row in rows:
        paths = artefact_paths(row, out, 1)
        runs = row["runs"]
        n_calls = runs if row["config"] in ("K2", "K3") else 0
        calls += n_calls
        print()
        print(f"[{row['config']}] {row['injection_id']}  {row['scenario_l2']} / {row['category_l1']}")
        print(f"     tag            {row['tag']}   sha {row['sha']}")
        print(f"     carrier        {row['carrier_module']}")
        print(f"     graph mode     {row['rule_graph_mode'] or 'n/a'}"
              f"   (derived from category_l1, protocol §6 Rev. 31)")
        print(f"     runs           {runs if runs is not None else 'n/a (no repetition option)'}"
              f"   calls {n_calls}")
        print(f"     validator (7)  {row['expected_cycles']} cycles expected")
        print(f"     validator (8)  {row['expected_whitelist_edge'] or 'no edge outside the whitelist'}")
        print(f"     command        {render_line(row, paths)}")
        for key in ("run_log", "json_out", "stdout", "stderr"):
            if key in paths:
                print(f"     {key:<14} {paths[key]}")
        print(f"     manifest       {paths['manifest']}")

    invocations = len(rows)
    print()
    print("=" * 100)
    per_cfg = {c: sum(1 for r in rows if r["config"] == c) for c in CONFIGS}
    print(f"invocations : {invocations}   ({', '.join(f'{c} {n}' for c, n in per_cfg.items())})")
    print(f"model calls : {calls}   (K2 {sum(r['runs'] for r in rows if r['config'] == 'K2')}, "
          f"K3 {sum(r['runs'] for r in rows if r['config'] == 'K3')}; K1/K4/K5 are call-free)")
    print("=" * 100)
    return 0


# ── per-run preconditions (protocol §6, step 2 of the C7 order) ───────────────────────

def machine_identification() -> dict:
    """(3) of protocol §6 Nachtrag Rev. 30 — recorded per run, compared against D2 M5(d)."""
    def out(*cmd: str) -> str:
        try:
            return subprocess.run(cmd, capture_output=True, text=True).stdout.strip()
        except OSError:
            return "<unavailable>"
    return {"uname": out("uname", "-a"),
            "python3": out("python3", "--version"),
            "node": out("node", "--version")}


def ensure_clean_testrepo() -> None:
    """(a) Any output aborts BEFORE a call comes into being.

    B33: the diff compares `<base>` against the WORKING TREE, not `<base>..HEAD`. With a
    dirty tree the diff mixes committed and uncommitted change, and NO log field tells the
    two apart — such a run cannot be separated from a clean one afterwards.
    """
    porcelain = subprocess.run(["git", "-C", str(TESTREPO), "status", "--porcelain"],
                               capture_output=True, text=True).stdout
    if porcelain.strip():
        raise Abort(f"test repo working tree is dirty:\n{porcelain}")


def ensure_checker_build() -> dict:
    """(b) Hash of `dist/cli.js` per run; rebuild only on deviation, but log every time.

    A deviation from the registered hash is an abort reason (protocol §1 Nachtrag Rev. 24).
    """
    if not CLI_JS.exists():
        build_checker()
    digest = sha256(CLI_JS)
    if digest != spec.EXPECTED_CLI_SHA256:
        build_checker()
        digest = sha256(CLI_JS)
    if digest != spec.EXPECTED_CLI_SHA256:
        raise Abort(f"dist/cli.js sha256 {digest} != registered {spec.EXPECTED_CLI_SHA256}")
    porcelain = subprocess.run(["git", "-C", str(CHECKER_REPO), "status", "--porcelain"],
                               capture_output=True, text=True).stdout
    head = git(CHECKER_REPO, "rev-parse", "HEAD")
    if head != spec.EXPECTED_CHECKER_HEAD:
        raise Abort(f"checker HEAD {head} != registered {spec.EXPECTED_CHECKER_HEAD}")
    # The freeze tag, resolved per run: `phase04-freeze = <SHA>` in every run manifest, so the
    # measured state is named in the artefact and not only in a report (C5 §2).
    freeze_sha = git(CHECKER_REPO, "rev-parse", f"{FREEZE_TAG}^{{commit}}")
    if freeze_sha != spec.EXPECTED_CHECKER_HEAD:
        raise Abort(f"{FREEZE_TAG} resolves to {freeze_sha}, "
                    f"registered is {spec.EXPECTED_CHECKER_HEAD}")
    return {
        "measurement_path": str(CHECKER_REPO),
        "phase04_freeze": f"{FREEZE_TAG} = {freeze_sha}",
        "checker_git_head": head,
        "checker_git_status_porcelain": porcelain,
        "dist_cli_js_sha256": digest,
        "dist_cli_js_mtime": datetime.fromtimestamp(CLI_JS.stat().st_mtime,
                                                    timezone.utc).astimezone().isoformat(timespec="seconds"),
    }


def build_checker() -> None:
    """`npm run build` in the checker package. Building is not writing to the repo — `dist/`
    is gitignored (C4c §B1); the caller re-checks `git status --porcelain` afterwards."""
    r = subprocess.run(["npm", "run", "build"], cwd=str(CHECKER_PKG),
                       capture_output=True, text=True)
    if r.returncode != 0:
        raise Abort(f"npm run build failed:\n{r.stdout}\n{r.stderr}")


# ── point (6), COMMIT-SHARP since rev. 35 ─────────────────────────────────────────────
#
# Validator point (6), Z2' (ii) "sole importer per component", is a property of the CODE
# GRAPH, not of the Soll model. Treating it as commit-invariant — as the runner did until
# rev. 34 — aborts every injection that legitimately adds an importer to one of the guarded
# components: C10 stopped at I07, and the same wall stands at I08 and I09, all three of them
# `FORBIDDEN_RELATION` onto `core_adapters_internal`. The abort was the criterion being
# wrong, not the injection.
#
# The expectation is CALCULATED, never chosen, and never copied out of a report:
#
#   * the resting-state importer of a guarded component is the ONE whitelisted relation
#     into it, read out of `depot_soll.ilograph.yaml` by the validator's own `load_soll`;
#   * the injection's registered edge comes out of `expected_edge_boundary` of the manifest
#     entry — the same value points (7)/(8) are judged against.
#
# The test that results is SHARPER than the one it replaces, not looser: rev. 34 compared a
# COUNT (`len(importers) == 1`) and never looked at which component was importing. Rev. 35
# compares the SET. A second importer is admitted only when it is exactly the source
# component of the registered edge; another component, a second extra importer, or any
# deviation at a component the injection does not touch aborts as before.


def sole_importer_expectations(manifest_entry: dict) -> dict[str, list[str]]:
    """Expected importer set per guarded component for THIS commit.

    `{component: sorted importers}` over `validate_soll.SOLE_IMPORTER` — the resting-state
    importer out of the Soll whitelist, plus the source component of the registered edge on
    the one component the injection targets.
    """
    _, _, allowed = soll_model.load_soll(SOLL / "depot_soll.ilograph.yaml")
    expected = {t: sorted({src for src, dst in allowed if dst == t})
                for t in soll_model.SOLE_IMPORTER}
    edge = spec.expected_whitelist_edge(manifest_entry)
    if edge and "->" in edge:
        src, _, dst = (part.strip() for part in edge.partition("->"))
        if dst in expected:
            expected[dst] = sorted(set(expected[dst]) | {src})
    return expected


IMPORTERS_RE = __import__("re").compile(r"^(\S+)\s+importers = \d+\s+(\[.*\])$")


def check_point_6(lines: list[tuple[str, str]], expected: dict[str, list[str]]) -> list[str]:
    """Point (6) against the calculated set. Returns the failures, empty when it holds.

    The validator's own OK/FAIL verdict is DELIBERATELY ignored here: it still carries the
    rev.-34 count rule, which calls the injected importer a failure. What is read off the
    line is the measured set; the verdict on it is formed here.
    """
    failures: list[str] = []
    seen: set[str] = set()
    for _, text in lines:
        m = IMPORTERS_RE.match(text)
        if not m:
            failures.append(f"validator point (6): unparsable line {text!r}")
            continue
        component = m.group(1)
        try:
            measured = sorted(__import__("ast").literal_eval(m.group(2)))
        except (ValueError, SyntaxError):
            failures.append(f"validator point (6): unreadable importer list in {text!r}")
            continue
        seen.add(component)
        want = expected.get(component)
        if want is None:
            failures.append(f"validator point (6): unregistered component {component!r}")
        elif measured != want:
            failures.append(f"validator point (6), {component}: expected importers {want}, "
                            f"measured {measured}")
    for component in sorted(set(expected) - seen):
        failures.append(f"validator point (6): {component} not reported by the validator")
    return failures


POINT_RE = __import__("re").compile(r"^\[(\d)\]")
VERDICT_RE = __import__("re").compile(r"^\s+(OK|FAIL)\s+(.*)$")


def parse_validator(stdout: str) -> dict[int, list[tuple[str, str]]]:
    """`OK`/`FAIL` lines grouped by the validator's numbered points."""
    points: dict[int, list[tuple[str, str]]] = {}
    current = 0
    for line in stdout.splitlines():
        m = POINT_RE.match(line)
        if m:
            current = int(m.group(1))
            points.setdefault(current, [])
            continue
        v = VERDICT_RE.match(line)
        if v and current:
            points[current].append((v.group(1), v.group(2).strip()))
    return points


def run_soll_validator(row: dict, manifest_entry: dict) -> dict:
    """(c) and (d) — the Soll validator per injection commit, with the phantom set expected
    for THIS commit, and the I1 check that comes with it (validator point 4).

    Protocol §2 Rev. 11 makes the validator a per-commit precondition: none of the failures
    it looks for is visible at run time. A deviation aborts BEFORE a call comes into being.

    On an `INCORRECT_LOCATION` commit the carrier has moved, so the expected Soll-only set
    changes — `--injection I25…I28` expresses exactly that. On every other commit the four
    target locations are Soll-only, which is the validator's default.

    POINTS (6), (7) AND (8) ARE JUDGED AGAINST THE REGISTRATION, NOT AGAINST THE BASELINE.
    The validator was written for the clean baseline: point (6) counts importers of the
    guarded components, point (7) counts cycles of the actual state and point (8) counts
    module edges outside the whitelist. All three are CODE GRAPH properties, and on an
    injection commit they deviate BY THE INJECTION — that is the injection working, not a
    defect, and aborting on it would abort the structural runs. The expected values are
    derived, not chosen here: the edge comes from `expected_edge_boundary` of the manifest
    entry, the cycle count from `c4b_bericht_injektionen.md` §8.5 / protocol §3 Nachtrag
    Rev. 29 (I01-I03 carry a construction-bound cycle, I13-I16 the injected one, every other
    commit zero), and the importer sets from the Soll whitelist plus that same edge
    (rev. 35 — the amendment C10a wrote after C10 aborted at I07). A deviation BEYOND the
    registered one aborts, exactly as before.
    """
    # The SAME values `--plan` printed, off the row — plan and run cannot drift apart (C5 (a)).
    expect_cycles = row.get("expected_cycles", spec.expected_cycles(row["injection_id"]))
    argv = [str(VENV_BIN / "python"), str(MA / "tools" / "validate_soll.py"),
            "--soll", str(SOLL / "depot_soll.ilograph.yaml"),
            "--testrepo", str(TESTREPO),
            "--rules", str(SOLL / "architecture-rules.yaml"),
            "--expect-cycles", str(expect_cycles)]
    if row["injection_id"] in ("I25", "I26", "I27", "I28"):
        argv += ["--injection", row["injection_id"]]
    r = subprocess.run(argv, capture_output=True, text=True)
    points = parse_validator(r.stdout)

    failures: list[str] = []
    # points (1)-(5): commit-invariant Soll properties, every FAIL aborts
    for n in range(1, 6):
        for verdict, text in points.get(n, []):
            if verdict == "FAIL":
                failures.append(f"validator point ({n}): {text}")
    # point (6): commit-SHARP since rev. 35 — the measured importer set against the set
    # calculated from the Soll whitelist and the registered edge, never against a count
    expected_importers = row.get("expected_sole_importers",
                                 sole_importer_expectations(manifest_entry))
    failures += check_point_6(points.get(6, []), expected_importers)
    # point (7): the validator itself compares against `--expect-cycles`
    for verdict, text in points.get(7, []):
        if verdict == "FAIL":
            failures.append(f"validator point (7), expected {expect_cycles} cycles: {text}")
    # point (8): the injected edge is expected, anything else is not
    expected_edge = row.get("expected_whitelist_edge",
                            spec.expected_whitelist_edge(manifest_entry))
    outside = points.get(8, [])
    for verdict, text in outside:
        if verdict == "OK":
            continue
        if expected_edge and text.count("->") and expected_edge in text and "= 1 " in text:
            continue
        failures.append(f"validator point (8), expected edge {expected_edge!r}: {text}")

    # I1 occurrences are RECORDED, never suppressed (protocol §3 Rev. 12: import-linter 2.13
    # has no switch against transitive `independence`, so a chain orders->core->billing or
    # orders->identity->billing would be reported as an `independence` violation in a commit
    # whose injection has nothing to do with INDEPENDENCE).
    i1 = [f"{v} {t}" for v, t in points.get(4, [])]
    i1_violations = [line for v, t in points.get(4, []) if v == "FAIL" for line in [t]]

    if failures:
        raise Abort(f"Soll validator failed for {row['injection_id']}:\n  "
                    + "\n  ".join(failures) + f"\n--- full output ---\n{r.stdout}")
    return {"validator_exit_code": r.returncode,
            "expected_cycles": expect_cycles,
            "expected_whitelist_edge": expected_edge,
            "expected_sole_importers": expected_importers,
            "points_1_to_5": "all OK",
            "point_6": "measured importer sets equal the calculated expectation",
            "i1_point_4": i1,
            "i1_violations_recorded": i1_violations,
            "stdout": r.stdout,
            "stderr": r.stderr}


# ── the K2 context window, MEASURED once per campaign session ─────────────────────────
#
# Protocol §1 Nachtrag Rev. 26 registers the window as a MEASURED ENVIRONMENT PARAMETER, not
# as a model property: the checker sets no `num_ctx` (`llmClient.ts:114-124`), so Ollama falls
# back on its own default — measured `CONTEXT 4096`, while the model carries 32768. On an
# exceedance Ollama truncates AT THE FRONT, without error and without a log line, so nothing
# in the artefacts would show it. A changed Ollama default would move a registered parameter
# and is an abort reason, not a note (C5 order (b)).
#
# THE TWO COMMANDS MEASURE DIFFERENT THINGS AND ONLY ONE OF THEM ANSWERS THE QUESTION:
#   `ollama show`  reports the MODEL limit (32768). Recorded, compared, never the budget.
#   `ollama ps`    reports the LOADED window in its `CONTEXT` column — the value that binds.
#
# And `ollama ps` can only report a RESIDENT instance. `k2_machbarkeitslauf_bericht.md` §1d
# records exactly that: "ollama ps (vor dem ersten Lauf) → leer (kein Modell geladen)". The
# window is therefore measured in two stages, and the raw output of both goes into the run
# manifest verbatim:
#
#   before_first_call  the gate the order asks for. If a K2 instance is already resident —
#                      from an earlier session, or under `keep_alive` — the measurement stands
#                      here and a deviation aborts BEFORE a call comes into being.
#   after_first_call   the fallback, taken only when the model was not resident. Ollama loads
#                      it with the first call, so the window becomes readable there. A
#                      deviation aborts the campaign right after that first invocation, and
#                      that invocation is journalled INVALID: it was measured under an
#                      unregistered environment parameter.
#
# Reading the window earlier is not possible without loading the model, and loading it is a
# call — the two-stage form is the honest one, not a convenience.

OLLAMA_PS_CONTEXT_COLUMN = "CONTEXT"
_K2_WINDOW: dict | None = None


def ollama_raw(*args: str) -> dict:
    """`ollama <args>` verbatim. A status query: it loads no model and issues no call."""
    try:
        r = subprocess.run(["ollama", *args], capture_output=True, text=True, timeout=60)
    except (OSError, subprocess.SubprocessError) as e:
        return {"argv": ["ollama", *args], "exit_code": None, "stdout": "", "stderr": "",
                "error": f"{type(e).__name__}: {e}"}
    return {"argv": ["ollama", *args], "exit_code": r.returncode,
            "stdout": r.stdout, "stderr": r.stderr}


def parse_ps_context(stdout: str, model: str) -> tuple[int | None, str]:
    """The `CONTEXT` column of the resident instance, with the reason when there is none.

    Sliced by the header positions, not by `split()`: `PROCESSOR` holds "100% GPU" and `UNTIL`
    holds "4 minutes from now", both with blanks, so a whitespace split shifts the columns.
    Verified against the archived raw output of C3b-K2 (`data/c3b-k2/temperature_log.json`).
    """
    lines = [l for l in stdout.splitlines() if l.strip()]
    if not lines:
        return None, "`ollama ps` empty — no model resident"
    header = lines[0]
    if OLLAMA_PS_CONTEXT_COLUMN not in header:
        return None, (f"`ollama ps` has no {OLLAMA_PS_CONTEXT_COLUMN} column "
                      f"(header: {header.strip()!r}) — this Ollama does not report the "
                      f"loaded window")
    start = header.index(OLLAMA_PS_CONTEXT_COLUMN)
    rest = header[start + len(OLLAMA_PS_CONTEXT_COLUMN):]
    # everything up to the next header word belongs to the CONTEXT column
    nxt = header.find(rest.split()[0], start) if rest.split() else -1
    end = nxt if nxt > start else len(header)
    for line in lines[1:]:
        if line.split() and line.split()[0] == model:
            raw = line[start:end].strip()
            if raw.isdigit():
                return int(raw), "read from the CONTEXT column of the resident instance"
            return None, f"CONTEXT column of {model} is not a number: {raw!r}"
    return None, f"{model} not resident in `ollama ps`"


def parse_show_context(stdout: str) -> int | None:
    """`context length` out of `ollama show` — the MODEL limit, never the budget."""
    m = __import__("re").search(r"context length\s+(\d+)", stdout)
    return int(m.group(1)) if m else None


def measure_k2_context_window(stage: str) -> dict:
    """Measure once per campaign session; the raw output goes into every run manifest.

    Returns the record. `measured_context_length` is `None` while the model is not resident —
    the caller decides what that means at its stage.
    """
    global _K2_WINDOW
    if _K2_WINDOW is not None and _K2_WINDOW.get("measured_context_length") is not None:
        return _K2_WINDOW
    model = spec.K2_MODEL
    show = ollama_raw("show", model)
    ps = ollama_raw("ps")
    measured, how = parse_ps_context(ps["stdout"], model)
    model_limit = parse_show_context(show["stdout"])
    rec = {
        "stage": stage,
        "measured_at": now(),
        "model": model,
        "measured_context_length": measured,
        "measurement_source": how,
        "registered_context_length": spec.K2_REGISTERED_CONTEXT_LENGTH,
        "model_context_length_from_show": model_limit,
        "model_context_length_registered": spec.K2_MODEL_CONTEXT_LENGTH,
        "note": "`ollama show` reports the model limit, `ollama ps` the loaded window; only "
                "the loaded window is the token budget (protocol §1 Nachtrag Rev. 26)",
        "raw_ollama_show": show,
        "raw_ollama_ps": ps,
    }
    _K2_WINDOW = rec
    return rec


def k2_window_deviation(rec: dict) -> str | None:
    """The abort reason, or `None`. A changed window is a changed registered parameter."""
    measured = rec["measured_context_length"]
    if measured is None:
        return None
    if measured != spec.K2_REGISTERED_CONTEXT_LENGTH:
        return (f"K2 context window MEASURED {measured}, registered "
                f"{spec.K2_REGISTERED_CONTEXT_LENGTH} (protocol §1 Nachtrag Rev. 26) — a "
                f"changed registered environment parameter. The campaign does not start "
                f"against it and it is not adjusted here.\n"
                f"--- ollama ps ---\n{rec['raw_ollama_ps']['stdout']}"
                f"--- ollama show ---\n{rec['raw_ollama_show']['stdout']}")
    return None


def grimp_cache_state(stage: str) -> dict:
    """(5) — `.grimp_cache/` presence is recorded, and the directory is removed before a K4
    run. `--no-cache` is the protocol rule (B9+ (b)); the record shows it took effect."""
    cache = TESTREPO / ".grimp_cache"
    present = cache.exists()
    if present and stage == "before":
        shutil.rmtree(cache)
    return {"stage": stage, "present": present, "removed": present and stage == "before"}


# ── execution ─────────────────────────────────────────────────────────────────────────

def execute(row: dict, out: Path, attempt: int, smoke: bool, journal: Path) -> dict:
    paths = artefact_paths(row, out, attempt)
    paths["dir"].mkdir(parents=True, exist_ok=True)
    paths["manifest"].parent.mkdir(parents=True, exist_ok=True)

    ensure_clean_testrepo()                                     # (a)
    build_info = ensure_checker_build()                         # (b)
    subprocess.run(["git", "-C", str(TESTREPO), "checkout", "--detach", row["sha"]],
                   capture_output=True, text=True, check=True)
    ensure_clean_testrepo()                                     # (a), again after checkout
    validator = run_soll_validator(row, row["manifest_entry"])  # (c), (d)

    cache_before = grimp_cache_state("before") if row["config"] == "K4" else None

    # (b) of C5 — the K2 window, measured once per session, checked BEFORE the call whenever
    # an instance is already resident. A deviation aborts here, before a call comes into being.
    ctx_window = None
    if row["config"] == "K2":
        ctx_window = measure_k2_context_window("before_first_call")
        deviation = k2_window_deviation(ctx_window)
        if deviation:
            raise Abort(deviation)

    argv, extra_env = build_argv(row, paths)
    env = {**os.environ, **extra_env}

    # (1) of protocol §6 Nachtrag Rev. 30 — external wall clock, MONOTONIC, per invocation,
    # for all five configurations. `run_footer.wall_clock_ms` stays untouched as the inner
    # value; for K4 and K5 there is no other source at all.
    t0 = time.monotonic()
    proc = subprocess.run(argv, cwd=str(TESTREPO), env=env, capture_output=True, text=True)
    wall_ms = round((time.monotonic() - t0) * 1000)
    cache_after = grimp_cache_state("after") if row["config"] == "K4" else None

    # The fallback stage: the model was not resident before the call, so the window was not
    # readable then. It is now. The abort is raised at the END of this function, after manifest
    # and journal are written — the deviation is a finding and has to survive in the artefacts.
    ctx_deviation = None
    if row["config"] == "K2" and ctx_window is not None and \
            ctx_window["measured_context_length"] is None:
        ctx_window = measure_k2_context_window("after_first_call")
        ctx_deviation = k2_window_deviation(ctx_window)
        if ctx_window["measured_context_length"] is None:
            ctx_deviation = (
                "K2 context window NOT MEASURABLE: the model is not resident in `ollama ps` "
                "even after the first call — "
                f"{ctx_window['measurement_source']}. The registered parameter of protocol §1 "
                "Nachtrag Rev. 26 cannot be confirmed for this session, and it is not assumed."
                f"\n--- ollama ps ---\n{ctx_window['raw_ollama_ps']['stdout']}")

    # (2) — stdout AND stderr of every K4/K5 invocation, verbatim and complete, unparsed.
    if row["config"] in ("K4", "K5"):
        paths["stdout"].write_text(proc.stdout, encoding="utf-8")
        paths["stderr"].write_text(proc.stderr, encoding="utf-8")

    # (f) — exit 2 means git threw before the header was written: no `run_header`, no
    # artefact, log file 0 bytes. Such a run counts as NOT PERFORMED, not as a run with zero
    # findings (protocol §6 Amendment 11.08.).
    not_performed = False
    if row["config"] in ("K1", "K2", "K3"):
        log = paths["run_log"]
        has_header = log.exists() and log.stat().st_size > 0 and "run_header" in log.read_text(
            encoding="utf-8", errors="replace")
        if proc.returncode == 2 or not has_header:
            not_performed = True

    manifest = {
        "run": {k: row[k] for k in ("config", "injection_id", "tag", "sha", "category_l1",
                                    "scenario_l2", "carrier_module", "runs")},
        # (4) — the DERIVED graph mode, written per run so the assignment is checkable
        # afterwards instead of having to be believed of the runner code.
        "rule_graph_mode": row["rule_graph_mode"],
        "rule_graph_mode_source": "derived from category_l1 (protocol §6 Nachtrag Rev. 31)",
        "attempt": attempt,
        "is_smoke_test": smoke,
        "started": now(),
        "command": render_line(row, paths),
        "argv": argv,
        "env_overrides": {k: ("<redacted>" if "API_KEY" in k else v)
                          for k, v in extra_env.items()},
        # (3) — absolute test repo path, cwd of the invocation, machine identification.
        "abs_repo_path": str(TESTREPO),
        "cwd": str(TESTREPO),
        "machine": machine_identification(),
        "machine_reference_d2_m5d": spec.REFERENCE_MACHINE,
        "target_repo_git_head": git(TESTREPO, "rev-parse", "HEAD"),
        "base_ref": spec.EXPECTED_BASELINE_SHA,
        **build_info,
        "exit_code": proc.returncode,
        "external_wall_clock_ms": wall_ms,
        "not_performed": not_performed,
        "soll_validator": validator,
        # (b) — the MEASURED window with the raw output of both commands, per run manifest.
        "k2_context_window": ctx_window,
        "grimp_cache": [c for c in (cache_before, cache_after) if c is not None],
        "artefacts": {k: str(v) for k, v in paths.items() if k not in ("dir", "stem")},
    }
    if row["config"] in ("K4", "K5"):
        manifest["stdout_bytes"] = len(proc.stdout.encode("utf-8"))
        manifest["stderr_bytes"] = len(proc.stderr.encode("utf-8"))
    paths["manifest"].write_text(json.dumps(manifest, indent=1), encoding="utf-8")

    # The token budget is held against the MEASURED window, not against the constant (C5 (b)).
    measured_ctx = ctx_window["measured_context_length"] if ctx_window else None
    verdict = postrun(paths, row, out, measured_ctx)
    if ctx_deviation:
        # The run was measured under an environment parameter that is not the registered one.
        # It is not a valid measurement, whatever the counting rules say about it.
        verdict = {"verdict": "INVALID",
                   "reasons": [ctx_deviation] + verdict["reasons"],
                   "detail": verdict["detail"]}
    manifest["postrun"] = verdict
    paths["manifest"].write_text(json.dumps(manifest, indent=1), encoding="utf-8")

    with journal.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps({"timestamp": now(), "config": row["config"],
                             "injection_id": row["injection_id"], "attempt": attempt,
                             "verdict": verdict["verdict"], "reasons": verdict["reasons"],
                             "is_smoke_test": smoke,
                             "paths": {k: str(v) for k, v in paths.items()
                                       if k not in ("dir", "stem")}}) + "\n")
    if ctx_deviation:
        raise Abort(ctx_deviation)
    return manifest


def postrun(paths: dict, row: dict, out: Path,
            measured_context_length: int | None = None) -> dict:
    """Calls `postrun_check.py`. The runner never decides validity itself."""
    import postrun_check
    return postrun_check.check_run(paths, row, measured_context_length)


# ── resumption ────────────────────────────────────────────────────────────────────────

def journal_state(journal: Path) -> dict[tuple[str, str], dict]:
    """Last verdict per (config, injection) out of the append-only journal."""
    state: dict[tuple[str, str], dict] = {}
    if journal.exists():
        for line in journal.read_text(encoding="utf-8").splitlines():
            if line.strip():
                e = json.loads(line)
                state[(e["config"], e["injection_id"])] = e
    return state


def next_attempt(journal: Path, config: str, injection: str) -> int:
    n = 0
    if journal.exists():
        for line in journal.read_text(encoding="utf-8").splitlines():
            if line.strip():
                e = json.loads(line)
                if e["config"] == config and e["injection_id"] == injection:
                    n = max(n, e["attempt"])
    return n + 1


def run(rows: list[dict], out: Path, smoke: bool) -> int:
    out.mkdir(parents=True, exist_ok=True)
    journal = out / "journal.jsonl"
    state = journal_state(journal)
    failures = 0
    try:
        for row in rows:
            key = (row["config"], row["injection_id"])
            prev = state.get(key)
            if prev and prev["verdict"] == "VALID":
                print(f"SKIP  {row['config']} {row['injection_id']} — already VALID "
                      f"(attempt {prev['attempt']}, {prev['timestamp']})")
                continue
            attempt = next_attempt(journal, *key)
            if prev:
                print(f"REDO  {row['config']} {row['injection_id']} — previous attempt "
                      f"{prev['attempt']} was {prev['verdict']}; new paths, nothing overwritten")
            m = execute(row, out, attempt, smoke, journal)
            v = m["postrun"]
            print(f"{v['verdict']:<7} {row['config']} {row['injection_id']} "
                  f"attempt {attempt}  exit {m['exit_code']}  {m['external_wall_clock_ms']} ms")
            for r in v["reasons"]:
                print(f"        - {r}")
            if v["verdict"] != "VALID":
                failures += 1
    finally:
        subprocess.run(["git", "-C", str(TESTREPO), "checkout", "main"],
                       capture_output=True, text=True)
    return 1 if failures else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--plan", action="store_true", help="print the matrix, execute nothing")
    mode.add_argument("--run", action="store_true")
    ap.add_argument("--out", type=Path, default=CAMPAIGN_OUT,
                    help=f"archive root, one subdirectory per configuration (default {CAMPAIGN_OUT})")
    ap.add_argument("--manifest", type=Path, default=SOLL / "injection_manifest.json")
    ap.add_argument("--configs", help="comma-separated subset, e.g. K1,K4")
    ap.add_argument("--injections", help="comma-separated subset, e.g. I01,I13")
    ap.add_argument("--smoke-test", action="store_true",
                    help="mark artefacts as a smoke test — NOT a measurement")
    a = ap.parse_args()

    rows = load_matrix(a.manifest)
    if a.configs:
        keep = {c.strip().upper() for c in a.configs.split(",")}
        rows = [r for r in rows if r["config"] in keep]
    if a.injections:
        keep = {i.strip().upper() for i in a.injections.split(",")}
        rows = [r for r in rows if r["injection_id"] in keep]
    if not rows:
        raise Abort("the filters select no run")

    try:
        return plan(rows, a.out) if a.plan else run(rows, a.out, a.smoke_test)
    except Abort as e:
        print(f"\nABORT: {e}", file=sys.stderr)
        return 3


if __name__ == "__main__":
    sys.exit(main())
