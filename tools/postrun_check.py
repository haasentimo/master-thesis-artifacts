#!/usr/bin/env python3
"""C7 — post-run checker: the SOLE executor of the run acceptance rules.

Protocol §6 Nachtrag Rev. 24 makes this script, not the checker runner, responsible for
validity: `invalidReasons` (`reporter.ts:59-64`) knows only `invalid_final_response`,
`transport_failure`, `incomplete_runs` and `skipped_files` — `changed_files_count` is not
among them, which is why C3a run 1b ended at `changed_files_count: 0` with exit 0 and an
empty `invalid_reasons`.

The rules, WITH the repetition factor (§6 Nachtrag Rev. 26 — the factor-free versions would
have thrown away every one of the 32 injection runs at `--runs 3`):

    injection run   changed_files_count == 1  AND  calls_total == 1 * runs
    control run     calls_total == control_files_count * runs
    K4 (rev. 32)    kept + broken == 13 evaluated contracts
    K5 (rev. 32)    24 collected tests, collection finished without error

THE EXIT CODE IS NOT A VALIDITY CRITERION (§6 Nachtrag Rev. 26). Exit 0 at 0 findings and
exit 1 at >= 1 finding is measured normal behaviour; using it would mark every run that
actually found something as failed. Validity rests on `invalid_reasons`, `calls_invalid`,
`calls_transport_failed` and the counting rules above.

Two record counts are reported per run, NEVER as a sum (§4/§6 Nachtrag Rev. 25): `rule_id`
prefix `DERIVED:` is the deterministic path, every other `rule_id` is the LLM path. An
evaluation carrying only the total is invalid.

    tools/postrun_check.py --run-log L --json-out J --mode injection --runs 3
    tools/postrun_check.py --archive data/c3b-k2 --mode control --runs 3 \
                           --expect-files 1 --expect-files-total 52
    tools/postrun_check.py --selfcheck

THE TOKEN BUDGET IS READ PER CALL, never accumulated over the repetitions (C5 order (c)): an
`llm_call` record exists once per (module, run_index), and its `tokens_in_total`/
`tokens_out_total` sum the ATTEMPTS of that single call. `--archive data/c3b-k2` prints the
maximum over the stock and must reproduce the published 2356 (protocol §1 Nachtrag Rev. 27).

The window that budget is held against is a MEASURED environment parameter, not a constant:
`--context-length` takes the value measured for the session (`run_campaign.py` measures it via
`ollama show`/`ollama ps` and passes it). Without the switch the registered constant is used,
and the detail block names which of the two applied.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import campaign_spec as spec  # noqa: E402

DERIVED_PREFIX = "DERIVED:"


def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()
            if line.strip()]


# ── the checker configurations K1, K2, K3 ─────────────────────────────────────────────

def check_checker_run(run_log: Path, json_out: Path, mode: str, runs: int,
                      config: str | None, expect_files: int | None,
                      measured_context_length: int | None = None) -> dict:
    """`mode` is one of injection | control | fullpicture.

    `measured_context_length` is the window MEASURED for this campaign session (K2:
    `ollama ps`, see `run_campaign.measure_k2_context_window`). Passed, it replaces the
    registered constant as the token budget — the constant is the value C3b measured, not a
    promise about this session. Omitted, the registered constant of `campaign_spec` is used
    and the detail block says so, so an archive check stays reproducible without Ollama.

    For the descriptive FULL-PICTURE run the counting rules do NOT apply (protocol §6
    Amendment 12.08. and Nachtrag Rev. 29): it carries all 32 injections at once, goes into
    no metric and is not joined against the manifest. The exception is implemented here even
    though the commit does not exist yet — it is an open item of C4d.
    """
    reasons: list[str] = []
    detail: dict = {"mode": mode, "runs": runs}

    if not run_log.exists() or run_log.stat().st_size == 0:
        # No `run_header` means the run was NOT PERFORMED, not a run with zero findings: on
        # an unresolvable base git throws before the header is written (exit 2, log 0 bytes,
        # no artefact) — protocol §6 Amendment 11.08.
        return {"verdict": "INVALID", "reasons": ["no run_header — run NOT PERFORMED"],
                "detail": detail}

    records = load_jsonl(run_log)
    headers = [r for r in records if r.get("record_type") == "run_header"]
    footers = [r for r in records if r.get("record_type") == "run_footer"]
    calls = [r for r in records if r.get("record_type") == "llm_call"]
    if len(headers) != 1:
        reasons.append(f"run_header count = {len(headers)}, expected 1 — run NOT PERFORMED")
    if len(footers) != 1:
        reasons.append(f"run_footer count = {len(footers)}, expected 1 — run died hard")
    if not headers or not footers:
        return {"verdict": "INVALID", "reasons": reasons, "detail": detail}

    header, footer = headers[0], footers[0]
    detail.update({
        "run_id": header["run_id"],
        "status": footer["status"],
        "exit_code": footer["exit_code"],
        "exit_code_note": "not a validity criterion (protocol §6 Nachtrag Rev. 26)",
        "changed_files_count": header["changed_files_count"],
        "control_files_count": header["control_files_count"],
        "graph_files_count": header.get("graph_files_count"),
        "runs_requested": header["runs_requested"],
        "calls_total": footer["calls_total"],
        "rule_graph_mode": header.get("rule_graph_mode"),
    })

    # ── the counting rules, with the repetition factor ────────────────────────────────
    if mode == "fullpicture":
        detail["counting_rules"] = "NOT APPLICABLE (descriptive full-picture run)"
    elif mode == "injection":
        if header["changed_files_count"] != 1:
            reasons.append(f"changed_files_count = {header['changed_files_count']}, expected 1"
                           + (" — not a clean run but an unmeasured one"
                              if header["changed_files_count"] == 0 else ""))
        expected_calls = 1 * runs if config in ("K2", "K3") else 0
        if config in ("K2", "K3") and footer["calls_total"] != expected_calls:
            reasons.append(f"calls_total = {footer['calls_total']}, expected 1 * runs "
                           f"= {expected_calls}")
        if config == "K1" and footer["calls_total"] != 0:
            reasons.append(f"calls_total = {footer['calls_total']}, expected 0 on K1 "
                           f"(deterministic path, no model)")
        detail["counting_rules"] = (f"changed_files_count == 1 AND calls_total == 1 * runs "
                                    f"({expected_calls})")
    elif mode == "control":
        cfc = header["control_files_count"]
        if expect_files is not None and cfc != expect_files:
            reasons.append(f"control_files_count = {cfc}, expected {expect_files}")
        expected_calls = cfc * runs
        if footer["calls_total"] != expected_calls:
            reasons.append(f"calls_total = {footer['calls_total']}, expected "
                           f"control_files_count * runs = {expected_calls}")
        detail["counting_rules"] = f"calls_total == control_files_count * runs ({expected_calls})"

    # ── validity as the protocol defines it, exit code excluded ───────────────────────
    if footer["invalid_reasons"]:
        reasons.append(f"invalid_reasons = {footer['invalid_reasons']}")
    if footer.get("calls_invalid"):
        reasons.append(f"calls_invalid = {footer['calls_invalid']}")
    if footer.get("calls_transport_failed"):
        reasons.append(f"calls_transport_failed = {footer['calls_transport_failed']}")
    detail["invalid_reasons"] = footer["invalid_reasons"]
    detail["calls_invalid"] = footer.get("calls_invalid")
    detail["calls_transport_failed"] = footer.get("calls_transport_failed")
    detail["wall_clock_ms_inner"] = footer.get("wall_clock_ms")

    # ── token budget per call ─────────────────────────────────────────────────────────
    #
    # The window is a MEASURED environment parameter out of the protocol (§1 Nachtrag
    # Rev. 26 for K2, Rev. 30 for K3), not a log field — the checker sets no `num_ctx` and
    # logs no window. The counts come from the call records. No intervention in the
    # measurement path: an exceedance is REPORTED, it does not rewrite anything.
    if config in ("K2", "K3") and calls:
        window = dict(spec.CONTEXT_WINDOW[config])
        source = f"registered constant (campaign_spec.CONTEXT_WINDOW[{config!r}])"
        if measured_context_length is not None:
            window["context_length"] = measured_context_length
            source = "MEASURED this campaign session"
        worst = 0
        worst_call = None
        over = []
        # ONE record per call: `llm_call` is written per (module, run_index), and
        # `tokens_in_total`/`tokens_out_total` sum the ATTEMPTS of that one call (retries),
        # not the repetitions. Summing across repetitions would be wrong in both directions —
        # it would invent exceedances at `--runs 3` and hide none. Proof in the selfcheck
        # (`three calls of 1500 tokens must stay VALID at a 4096 window`) and against the
        # archive: `--archive data/c3b-k2` reproduces the published maximum of 2356.
        for c in calls:
            total = (c.get("tokens_in_total") or 0) + (c.get("tokens_out_total") or 0)
            if total > worst:
                worst, worst_call = total, c
            if window["context_length"] and total > window["context_length"]:
                over.append(f"{c.get('module')} r{c.get('run_index')}: {total} tokens")
            if window["max_output_tokens"] and (c.get("tokens_out_total") or 0) > window["max_output_tokens"]:
                over.append(f"{c.get('module')} r{c.get('run_index')}: "
                            f"{c.get('tokens_out_total')} out tokens")
        detail["token_budget"] = {
            "window": window,
            "window_source": source,
            "window_registered": spec.CONTEXT_WINDOW[config]["context_length"],
            "max_tokens_in_plus_out": worst,
            "max_call": None if worst_call is None else {
                "module": worst_call.get("module"),
                "run_index": worst_call.get("run_index"),
                "tokens_in_total": worst_call.get("tokens_in_total"),
                "tokens_out_total": worst_call.get("tokens_out_total"),
                "attempts_used": worst_call.get("attempts_used"),
            },
            "calls_read": len(calls),
            "note": "`usage` is null in the measured logs; the counts come from "
                    "`tokens_in_total` + `tokens_out_total` of the call record, read PER "
                    "CALL and never accumulated over the repetitions",
            "exceedances": over,
        }
        for o in over:
            reasons.append(f"token budget exceeded: {o}")

    # ── the two record counts, separated (rev. 25) ────────────────────────────────────
    if json_out.exists():
        result = json.loads(json_out.read_text(encoding="utf-8"))
        per_run = []
        for r in result.get("runs", []):
            findings = r.get("findings", [])
            derived = [f for f in findings if f["rule_id"].startswith(DERIVED_PREFIX)]
            llm = [f for f in findings if not f["rule_id"].startswith(DERIVED_PREFIX)]
            per_run.append({"run_index": r["run_index"],
                            "records_derived": len(derived),
                            "records_llm": len(llm)})
        detail["records_by_mechanism"] = per_run
        detail["records_note"] = ("reported separately, never as a sum — an evaluation "
                                  "carrying only the total is invalid (protocol Rev. 25)")
    else:
        reasons.append(f"json-out missing: {json_out}")

    return {"verdict": "INVALID" if reasons else "VALID", "reasons": reasons, "detail": detail}


# ── the static configurations K4 and K5 (protocol §6 Nachtrag Rev. 32 (3)) ────────────

def check_k4(stdout: str) -> dict:
    """`kept + broken` must equal the 13 registered contracts.

    Checked is that the tool READ ITS RULE SET, not how many violations it found. The hit
    count is the measurement and stays untouched: `broken` may be anything from 0 to 13.
    """
    reasons: list[str] = []
    m = re.search(r"Contracts:\s*(\d+)\s+kept,\s*(\d+)\s+broken", stdout)
    if not m:
        return {"verdict": "INVALID",
                "reasons": ["no `Contracts: N kept, M broken` line — import-linter did not "
                            "evaluate its contracts"],
                "detail": {"expected_contracts": spec.K4_EXPECTED_CONTRACTS}}
    kept, broken = int(m.group(1)), int(m.group(2))
    total = kept + broken
    if total != spec.K4_EXPECTED_CONTRACTS:
        reasons.append(f"evaluated contracts = {total} (kept {kept} + broken {broken}), "
                       f"expected {spec.K4_EXPECTED_CONTRACTS}")
    return {"verdict": "INVALID" if reasons else "VALID", "reasons": reasons,
            "detail": {"kept": kept, "broken": broken, "evaluated": total,
                       "expected_contracts": spec.K4_EXPECTED_CONTRACTS,
                       "note": "the hit count is the measurement; only completeness of the "
                               "rule set is checked"}}


def check_k5(stdout: str, stderr: str) -> dict:
    """24 collected tests, collection finished without error.

    Without `DEPOT_SRC` the frozen configuration raises at MODULE level, i.e. during
    collection: pytest aborts and 0 of 23 rules run, and neither exit code nor output tells
    that apart from a clean run (protocol §6 Nachtrag Rev. 32 (1)). This rule is what makes
    that case visible.
    """
    reasons: list[str] = []
    blob = stdout + "\n" + stderr
    if re.search(r"errors? during collection|INTERNALERROR|ERROR collecting", blob):
        reasons.append("collection did not finish without error")
    collected = None
    m = re.search(r"collected (\d+) items?", blob)
    if m:
        collected = int(m.group(1))
    else:
        # `-q` prints no `collected` line on success; the dot line and the summary carry the
        # count instead. Both forms are accepted, neither is invented.
        m = re.search(r"^(\d+) passed", blob, re.M) or re.search(r"(\d+) passed", blob)
        m2 = re.search(r"(\d+) failed", blob)
        if m:
            collected = int(m.group(1)) + (int(m2.group(1)) if m2 else 0)
    if collected is None:
        reasons.append("no collected/passed count in the output — pytest did not run the file")
    elif collected != spec.K5_EXPECTED_COLLECTED:
        reasons.append(f"collected tests = {collected}, expected "
                       f"{spec.K5_EXPECTED_COLLECTED}")
    return {"verdict": "INVALID" if reasons else "VALID", "reasons": reasons,
            "detail": {"collected": collected,
                       "expected_collected": spec.K5_EXPECTED_COLLECTED,
                       "note": "the failure count is the measurement; only completeness of "
                               "the rule set is checked"}}


def check_run(paths: dict, row: dict, measured_context_length: int | None = None) -> dict:
    """Entry point used by `run_campaign.py` right after an invocation.

    `measured_context_length` carries the window measured for this session; the runner passes
    it for K2 and leaves it `None` elsewhere.
    """
    cfg = row["config"]
    if cfg in ("K1", "K2", "K3"):
        return check_checker_run(Path(paths["run_log"]), Path(paths["json_out"]),
                                 "injection", row["runs"] or 1, cfg, None,
                                 measured_context_length)
    stdout = Path(paths["stdout"]).read_text(encoding="utf-8") if Path(paths["stdout"]).exists() else ""
    stderr = Path(paths["stderr"]).read_text(encoding="utf-8") if Path(paths["stderr"]).exists() else ""
    return check_k4(stdout) if cfg == "K4" else check_k5(stdout, stderr)


def report(name: str, verdict: dict) -> None:
    print(f"--- {name}")
    for k, v in verdict["detail"].items():
        print(f"      {k}: {v}")
    print(f"    RESULT: {verdict['verdict']}")
    for r in verdict["reasons"]:
        print(f"      - {r}")


def check_archive(root: Path, mode: str, runs: int, expect_files: int | None,
                  measured_context_length: int | None = None,
                  expect_files_total: int | None = None) -> int:
    """Runs the rules over an archived stock — `data/c3b-k2/`, `data/c3b-k3/`. READ ONLY.

    If the control rule comes out INVALID there, the script is wrong, not the archive.

    TWO LEVELS, because the C3b control runs were driven in SINGLE-FILE DECOMPOSITION: one
    invocation per control module, 52 of them, each with `control_files_count: 1` and
    `calls_total: 3` (`c3b_k2_bericht_kontrolllauf.md` §2). `--expect-files` is therefore the
    expectation PER INVOCATION (1 there), and `--expect-files-total` the expectation over the
    stock (52). Handing the stock total to `--expect-files` marks all 52 invocations invalid
    on a stock the protocol certifies as 52/52 valid — the caller is wrong there, not the
    archive.

    The token maximum over the whole stock is printed as well. That number is the PROOF that
    the budget is read per call: `data/c3b-k2` must reproduce the published maximum of 2356
    (`c3b_k2_bericht_kontrolllauf.md` §5, protocol §1 Nachtrag Rev. 27), `data/c3b-k3` the
    published 3136 (§1 Nachtrag Rev. 30). An accumulating read would land at a multiple.
    """
    logs = sorted((root / "runs").glob("*.jsonl"))
    if not logs:
        print(f"no run logs under {root}/runs", file=sys.stderr)
        return 2
    invalid = []
    worst = 0
    worst_where: dict | None = None
    calls_read = 0
    sum_files = 0
    sum_calls = 0
    for log in logs:
        j = log.with_suffix(".json")
        v = check_checker_run(log, j, mode, runs, "K2" if "k2" in root.name else "K3",
                              expect_files, measured_context_length)
        if v["verdict"] != "VALID":
            invalid.append((log.name, v))
        sum_files += v["detail"].get("control_files_count") or 0
        sum_calls += v["detail"].get("calls_total") or 0
        tb = v["detail"].get("token_budget")
        if tb:
            calls_read += tb["calls_read"]
            if tb["max_tokens_in_plus_out"] > worst:
                worst = tb["max_tokens_in_plus_out"]
                worst_where = {"invocation": log.name, **(tb["max_call"] or {})}
    print(f"archive   : {root}")
    print(f"invocations: {len(logs)}   mode {mode}   runs {runs}   expect-files {expect_files}"
          f"   expect-files-total {expect_files_total}")
    print(f"VALID     : {len(logs) - len(invalid)}")
    print(f"INVALID   : {len(invalid)}")
    for name, v in invalid:
        print(f"  {name}: {v['reasons']}")
    stock_failed = False
    if expect_files_total is not None:
        expected_calls = expect_files_total * runs
        ok_f = sum_files == expect_files_total
        ok_c = sum_calls == expected_calls
        stock_failed = not (ok_f and ok_c)
        print(f"stock sums: control_files_count {sum_files}/{expect_files_total} "
              f"{'OK' if ok_f else 'FAIL'}   calls_total {sum_calls}/{expected_calls} "
              f"{'OK' if ok_c else 'FAIL'}")
    if worst_where is not None:
        print(f"llm_call records read : {calls_read}  (read PER CALL, never accumulated "
              f"over the repetitions)")
        print(f"max tokens_in+out     : {worst}")
        print(f"  at                  : {worst_where['invocation']}  module "
              f"{worst_where.get('module')}  run_index {worst_where.get('run_index')}  "
              f"(in {worst_where.get('tokens_in_total')} + out "
              f"{worst_where.get('tokens_out_total')}, attempts_used "
              f"{worst_where.get('attempts_used')})")
    return 1 if (invalid or stock_failed) else 0


# ── self-check: the rule that decides validity carries its own proof ──────────────────

def selfcheck() -> int:
    import tempfile

    def call(idx: int, module: str, tin: int = 1000, tout: int = 200) -> dict:
        return {"record_type": "llm_call", "run_index": idx, "module": module,
                "tokens_in_total": tin, "tokens_out_total": tout, "attempts_used": 1}

    hdr = {"record_type": "run_header", "run_id": "x", "runs_requested": 3,
           "control_files_count": 0, "changed_files_count": 1, "graph_files_count": 1,
           "rule_graph_mode": "diff"}
    ftr = {"record_type": "run_footer", "run_id": "x", "status": "completed", "exit_code": 1,
           "invalid_reasons": [], "calls_total": 3, "calls_invalid": 0,
           "calls_transport_failed": 0, "wall_clock_ms": 100}

    def run(recs, findings, mode="injection", runs=3, config="K2", expect=None, ctx=None):
        with tempfile.TemporaryDirectory() as d:
            p, q = Path(d) / "l.jsonl", Path(d) / "l.json"
            p.write_text("".join(json.dumps(r) + "\n" for r in recs), encoding="utf-8")
            q.write_text(json.dumps({"runs": [{"run_index": i, "findings": f}
                                              for i, f in enumerate(findings)]}), encoding="utf-8")
            return check_checker_run(p, q, mode, runs, config, expect, ctx)

    good = [hdr, call(0, "a"), call(1, "a"), call(2, "a"), ftr]
    assert run(good, [[], [], []])["verdict"] == "VALID", "clean injection run must pass"

    # THE regression of rev. 26: with the factor-free rule this run was thrown away.
    assert run(good, [[], [], []])["detail"]["counting_rules"].endswith("(3)")

    # exit 1 at >= 1 finding is normal behaviour, never a validity criterion
    f = [{"rule_id": "R-LAYER-1"}]
    assert run(good, [f, f, f])["verdict"] == "VALID", "findings must not invalidate a run"

    # changed_files_count == 0 is not a clean run but an unmeasured one
    zero = [{**hdr, "changed_files_count": 0}, call(0, "a"), call(1, "a"), call(2, "a"), ftr]
    assert run(zero, [[], [], []])["verdict"] == "INVALID"

    # calls_total short of 1 * runs
    short = [hdr, call(0, "a"), call(1, "a"), {**ftr, "calls_total": 2}]
    assert run(short, [[], []])["verdict"] == "INVALID"

    # K1 must produce no call at all
    k1 = [hdr, call(0, "a"), {**ftr, "calls_total": 1}]
    assert run(k1, [[]], runs=1, config="K1")["verdict"] == "INVALID"

    # transport failure and invalid_reasons
    tf = [hdr, call(0, "a"), call(1, "a"), call(2, "a"),
          {**ftr, "calls_transport_failed": 1}]
    assert run(tf, [[], [], []])["verdict"] == "INVALID"
    ir = [hdr, call(0, "a"), call(1, "a"), call(2, "a"),
          {**ftr, "invalid_reasons": ["transport_failure"]}]
    assert run(ir, [[], [], []])["verdict"] == "INVALID"

    # token budget against the MEASURED K2 window of 4096
    fat = [hdr, call(0, "a", tin=4000, tout=500), call(1, "a"), call(2, "a"), ftr]
    assert run(fat, [[], [], []])["verdict"] == "INVALID"

    # PER CALL, NOT ACCUMULATED — the point of order (c) of the C5 assignment. Three
    # repetitions of the same module at 1500 tokens each sum to 4500 and would break a 4096
    # window if the counts were added up over the repetitions. They are not: `llm_call` is one
    # record per (module, run_index) and `tokens_*_total` sums that call's ATTEMPTS.
    triple = [hdr, call(0, "a", tin=1200, tout=300), call(1, "a", tin=1200, tout=300),
              call(2, "a", tin=1200, tout=300), ftr]
    v = run(triple, [[], [], []])
    assert v["verdict"] == "VALID", "per-call reading must not sum the repetitions"
    assert v["detail"]["token_budget"]["max_tokens_in_plus_out"] == 1500
    assert v["detail"]["token_budget"]["calls_read"] == 3
    assert v["detail"]["token_budget"]["max_call"]["run_index"] in (0, 1, 2)

    # the window is replaced by the MEASURED value when one is passed, and the registered
    # value stays visible next to it (protocol §1 Nachtrag Rev. 26, C5 order (b))
    ok4096 = [hdr, call(0, "a", tin=3000, tout=500), call(1, "a"), call(2, "a"), ftr]
    assert run(ok4096, [[], [], []])["verdict"] == "VALID"
    shrunk = run(ok4096, [[], [], []], ctx=2048)
    assert shrunk["verdict"] == "INVALID", "a shrunk MEASURED window must bite"
    assert shrunk["detail"]["token_budget"]["window_source"] == "MEASURED this campaign session"
    assert shrunk["detail"]["token_budget"]["window_registered"] == 4096
    assert run(ok4096, [[], [], []])["detail"]["token_budget"]["window_source"].startswith(
        "registered constant")

    # the full-picture run is exempt from the counting rules
    fp = [{**hdr, "changed_files_count": 32}, call(0, "a"), {**ftr, "calls_total": 1}]
    assert run(fp, [[]], mode="fullpicture", runs=1)["verdict"] == "VALID"

    # the two record counts stay separate
    d = run(good, [[{"rule_id": "DERIVED:cycle"}, {"rule_id": "R-LAYER-1"}], [], []])
    assert d["detail"]["records_by_mechanism"][0] == {"run_index": 0, "records_derived": 1,
                                                      "records_llm": 1}

    # control run with the repetition factor
    chdr = {**hdr, "changed_files_count": 0, "control_files_count": 52}
    cftr = {**ftr, "calls_total": 156}
    assert run([chdr] + [call(0, "a")] + [cftr], [[]], mode="control", runs=3,
               expect=52)["verdict"] == "VALID"
    assert run([chdr] + [call(0, "a")] + [{**cftr, "calls_total": 52}], [[]], mode="control",
               runs=3, expect=52)["verdict"] == "INVALID"

    # K4 and K5, the positive rule of rev. 32
    assert check_k4("Contracts: 13 kept, 0 broken.")["verdict"] == "VALID"
    assert check_k4("Contracts: 12 kept, 1 broken.")["verdict"] == "VALID", "broken is the measurement"
    assert check_k4("Contracts: 6 kept, 0 broken.")["verdict"] == "INVALID"
    assert check_k4("")["verdict"] == "INVALID"
    assert check_k5("24 passed in 0.18s", "")["verdict"] == "VALID"
    assert check_k5("23 passed, 1 failed in 0.2s", "")["verdict"] == "VALID", "failed is the measurement"
    assert check_k5("", "RuntimeError: DEPOT_SRC must point at the source root")["verdict"] == "INVALID"
    assert check_k5("ERROR collecting data/soll/test_architecture.py", "")["verdict"] == "INVALID"

    print("selfcheck OK")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--run-log", type=Path)
    ap.add_argument("--json-out", type=Path)
    ap.add_argument("--k4-stdout", type=Path)
    ap.add_argument("--k5-stdout", type=Path)
    ap.add_argument("--k5-stderr", type=Path)
    ap.add_argument("--archive", type=Path, help="an archived stock, e.g. data/c3b-k2")
    ap.add_argument("--mode", choices=("injection", "control", "fullpicture"),
                    default="injection")
    ap.add_argument("--config", choices=("K1", "K2", "K3"))
    ap.add_argument("--runs", type=int, default=3)
    ap.add_argument("--expect-files", type=int, default=None,
                    help="expected `control_files_count` PER INVOCATION (1 in the C3b "
                         "single-file decomposition)")
    ap.add_argument("--expect-files-total", type=int, default=None,
                    help="--archive only: expected sum of `control_files_count` over the "
                         "whole stock (52 for the C3b control runs)")
    ap.add_argument("--context-length", type=int, default=None,
                    help="the MEASURED context window for this session; without it the "
                         "registered constant of campaign_spec is used")
    ap.add_argument("--selfcheck", action="store_true")
    a = ap.parse_args()

    if a.selfcheck:
        return selfcheck()
    if a.archive:
        return check_archive(a.archive, a.mode, a.runs, a.expect_files, a.context_length,
                             a.expect_files_total)
    if a.k4_stdout:
        v = check_k4(a.k4_stdout.read_text(encoding="utf-8"))
        report(f"K4 {a.k4_stdout}", v)
        return 0 if v["verdict"] == "VALID" else 1
    if a.k5_stdout:
        v = check_k5(a.k5_stdout.read_text(encoding="utf-8"),
                     a.k5_stderr.read_text(encoding="utf-8") if a.k5_stderr else "")
        report(f"K5 {a.k5_stdout}", v)
        return 0 if v["verdict"] == "VALID" else 1
    if not a.run_log or not a.json_out:
        ap.error("--run-log and --json-out are required")
    v = check_checker_run(a.run_log, a.json_out, a.mode, a.runs, a.config, a.expect_files,
                          a.context_length)
    report(str(a.run_log), v)
    return 0 if v["verdict"] == "VALID" else 1


if __name__ == "__main__":
    sys.exit(main())
