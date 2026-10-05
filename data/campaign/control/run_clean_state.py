#!/usr/bin/env python3
"""C6b-1 — clean-state runs of the deterministic configurations (A-14).

ARCHIVES a resting state that C3a already measured but wrote only into a scratch path. It
re-executes K1 (both registered graph modes), K4 and K5 against the clean baseline with the
invocation lines of protocol §6 rev. 24/32, the same runner code (`run_campaign.py` at
`4caf083`, imported here — not reimplemented), the same per-run preconditions and the same
recording. It DECIDES nothing about the measurement.

The acceptance criterion is NOT the campaign counting rule. On the clean baseline
`changed_files_count == 0` by construction (base == HEAD), so the injection rule cannot hold;
C3a itself recorded exactly that (`postrun_check.py` docstring: "C3a run 1b ended at
changed_files_count: 0 with exit 0"). The criterion here is the value C3a PUBLISHED:
K1 0 findings, K4 `13 kept, 0 broken`, K5 `24 passed`. The campaign-rule verdict is recorded
alongside, with the reason it does not apply — it is not hidden.
"""
from __future__ import annotations
import json, subprocess, sys, time
from pathlib import Path

sys.path.insert(0, "/home/haasentimo/ma/masterarbeit/tools")
import run_campaign as rc
import campaign_spec as spec
import postrun_check

OUT = rc.MA / "data" / "campaign" / "control"
JOURNAL = OUT / "journal.jsonl"
BASE = spec.EXPECTED_BASELINE_SHA

ROWS = [
    dict(config="K1", rule_graph_mode="full", runs=1),
    dict(config="K1", rule_graph_mode="diff", runs=1),
    dict(config="K4", rule_graph_mode=None, runs=None),
    dict(config="K5", rule_graph_mode=None, runs=None),
]


def make_row(base: dict) -> dict:
    row = dict(base)
    row.update(
        injection_id="B", tag="baseline", sha=BASE,
        category_l1=None, scenario_l2=None, carrier_module=None,
        manifest_entry={},
        # Clean baseline: no injection, therefore no cycle, no edge outside the whitelist,
        # and the importer sets are the ones the Soll whitelist alone prescribes.
        expected_cycles=0,
        expected_whitelist_edge=None,
        expected_sole_importers=rc.sole_importer_expectations({}),
    )
    return row


def k1_expectation(paths: dict) -> dict:
    """C3a §3a: 0 findings, exit 0, `graph_files_count: 73` in the full run."""
    doc = json.loads(Path(paths["json_out"]).read_text(encoding="utf-8"))
    findings = sum(len(r["findings"]) for r in doc["runs"])
    records = [json.loads(l) for l in Path(paths["run_log"]).read_text(
        encoding="utf-8").splitlines() if l.strip()]
    header = next(r for r in records if r["record_type"] == "run_header")
    footer = next(r for r in records if r["record_type"] == "run_footer")
    checks = {
        "findings_total": findings,
        "expected_findings": 0,
        "run_header_present": True,
        "run_footer_status": footer["status"],
        "invalid_reasons": footer["invalid_reasons"],
        "calls_total": footer["calls_total"],
        "changed_files_count": header["changed_files_count"],
        "graph_files_count": header.get("graph_files_count"),
        "rule_graph_mode": header.get("rule_graph_mode"),
        "records_derived": sum(1 for r in doc["runs"] for f in r["findings"]
                               if f["rule_id"].startswith("DERIVED:")),
        "records_other": sum(1 for r in doc["runs"] for f in r["findings"]
                             if not f["rule_id"].startswith("DERIVED:")),
    }
    fail = []
    if findings != 0:
        fail.append(f"findings = {findings}, C3a published 0")
    if footer["status"] != "completed":
        fail.append(f"run_footer status = {footer['status']}")
    if footer["invalid_reasons"]:
        fail.append(f"invalid_reasons = {footer['invalid_reasons']}")
    if footer["calls_total"] != 0:
        fail.append(f"calls_total = {footer['calls_total']}, expected 0 (no model)")
    if header.get("rule_graph_mode") == "full" and header.get("graph_files_count") != 73:
        fail.append(f"graph_files_count = {header.get('graph_files_count')}, "
                    "C3a published 73")
    return {"checks": checks, "failures": fail}


def execute_control(row: dict) -> dict:
    paths = rc.artefact_paths(row, OUT, 1)
    paths["dir"].mkdir(parents=True, exist_ok=True)
    paths["manifest"].parent.mkdir(parents=True, exist_ok=True)

    rc.ensure_clean_testrepo()                                     # (a)
    build_info = rc.ensure_checker_build()                         # (b)
    subprocess.run(["git", "-C", str(rc.TESTREPO), "checkout", "--detach", row["sha"]],
                   capture_output=True, text=True, check=True)
    rc.ensure_clean_testrepo()
    validator = rc.run_soll_validator(row, row["manifest_entry"])  # (c), (d)

    cache_before = rc.grimp_cache_state("before") if row["config"] == "K4" else None
    argv, extra_env = rc.build_argv(row, paths)
    import os
    env = {**os.environ, **extra_env}

    t0 = time.monotonic()
    proc = subprocess.run(argv, cwd=str(rc.TESTREPO), env=env, capture_output=True, text=True)
    wall_ms = round((time.monotonic() - t0) * 1000)
    cache_after = rc.grimp_cache_state("after") if row["config"] == "K4" else None

    if row["config"] in ("K4", "K5"):
        paths["stdout"].write_text(proc.stdout, encoding="utf-8")
        paths["stderr"].write_text(proc.stderr, encoding="utf-8")

    manifest = {
        "run": {"config": row["config"], "state": "clean baseline B",
                "tag": row["tag"], "sha": row["sha"], "runs": row["runs"]},
        "purpose": ("A-14 — archives the resting state of the deterministic configurations; "
                    "C3a measured it on 23.08.2026 but wrote the artefacts into a scratch "
                    "path. No new registration, no extended measurement."),
        "rule_graph_mode": row["rule_graph_mode"],
        "rule_graph_mode_source": ("both registered K1 lines executed (protocol §6 Nachtrag "
                                   "Rev. 24); the derivation from category_l1 has no subject "
                                   "here — the clean baseline carries no injection"),
        "attempt": 1,
        "is_smoke_test": False,
        "started": rc.now(),
        "command": rc.render_line(row, paths),
        "argv": argv,
        "env_overrides": dict(extra_env),
        "abs_repo_path": str(rc.TESTREPO),
        "cwd": str(rc.TESTREPO),
        "machine": rc.machine_identification(),
        "machine_reference_d2_m5d": spec.REFERENCE_MACHINE,
        "target_repo_git_head": rc.git(rc.TESTREPO, "rev-parse", "HEAD"),
        "base_ref": BASE,
        **build_info,
        "exit_code": proc.returncode,
        "external_wall_clock_ms": wall_ms,
        "soll_validator": validator,
        "grimp_cache": [c for c in (cache_before, cache_after) if c is not None],
        "artefacts": {k: str(v) for k, v in paths.items() if k not in ("dir", "stem")},
    }
    if row["config"] in ("K4", "K5"):
        manifest["stdout_bytes"] = len(proc.stdout.encode("utf-8"))
        manifest["stderr_bytes"] = len(proc.stderr.encode("utf-8"))

    if row["config"] == "K1":
        exp = k1_expectation(paths)
        manifest["c3a_expectation"] = exp["checks"]
        manifest["c3a_expectation_source"] = ("c3a_bericht_clean_state_audit.md §3a; "
                                              "protokoll §6 Nachtrag Rev. 23 (C3a — AUDIT)")
        failures = exp["failures"]
        campaign_rule = postrun_check.check_checker_run(
            Path(paths["run_log"]), Path(paths["json_out"]), "injection", row["runs"],
            "K1", None)
        manifest["campaign_rule_verdict"] = campaign_rule
        manifest["campaign_rule_note"] = (
            "The injection counting rule (§6 Nachtrag Rev. 26) CANNOT hold on the clean "
            "baseline: base == HEAD, so changed_files_count is 0 by construction. C3a "
            "recorded the same. The criterion for this archival run is the value C3a "
            "published, above; the campaign verdict is recorded, not applied.")
    else:
        verdict = (postrun_check.check_k4(proc.stdout) if row["config"] == "K4"
                   else postrun_check.check_k5(proc.stdout, proc.stderr))
        manifest["postrun"] = verdict
        manifest["postrun_note"] = ("positive run acceptance rule of §6 Nachtrag Rev. 32 (3) "
                                    "— applies unchanged on the clean baseline")
        failures = [] if verdict["verdict"] == "VALID" else list(verdict["reasons"])
        pub = ("Contracts: 13 kept, 0 broken." if row["config"] == "K4" else "24 passed")
        manifest["c3a_expectation"] = {"published": pub,
                                       "found_in_stdout": pub in proc.stdout}
        manifest["c3a_expectation_source"] = (
            "c3a_bericht_clean_state_audit.md " + ("§3a" if row["config"] == "K4" else "§3b")
            + "; d2_bericht_vormessungen.md M5")
        if pub not in proc.stdout:
            failures.append(f"published C3a value {pub!r} not present in stdout")

    manifest["expectation_failures"] = failures
    paths["manifest"].write_text(json.dumps(manifest, indent=1), encoding="utf-8")

    with JOURNAL.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps({"timestamp": rc.now(), "config": row["config"],
                             "state": "B", "rule_graph_mode": row["rule_graph_mode"],
                             "attempt": 1,
                             "verdict": "MATCHES_C3A" if not failures else "DEVIATION",
                             "reasons": failures,
                             "paths": {k: str(v) for k, v in paths.items()
                                       if k not in ("dir", "stem")}}) + "\n")
    return manifest


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    rc.ensure_clean_testrepo()
    deviations = []
    for base in ROWS:
        row = make_row(base)
        label = row["config"] + (f"/{row['rule_graph_mode']}" if row["rule_graph_mode"] else "")
        print(f"--- {label}", flush=True)
        m = execute_control(row)
        print(f"    exit {m['exit_code']}  wall {m['external_wall_clock_ms']} ms")
        print(f"    expectation: {m['c3a_expectation']}")
        if m["expectation_failures"]:
            deviations.append((label, m["expectation_failures"]))
            print(f"    !! DEVIATION: {m['expectation_failures']}")
    if deviations:
        print("\nABORT — deviation from the published C3a values:")
        for label, f in deviations:
            print(f"  {label}: {f}")
        return 1
    print("\nAll four runs reproduce the published C3a values.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
