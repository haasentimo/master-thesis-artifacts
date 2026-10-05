#!/usr/bin/env python3
"""C7 — the invocation specification of the campaign, pulled from the pre-registered documents.

EVERY literal in this module is quoted from a document, with its source in the comment above
it. Nothing here is reconstructed, inferred or estimated. Where two documents disagreed, the
disagreement was reported and decided in the protocol first (rev. 32, auftrag D3c) — it was
NOT resolved here.

Binding sources:
  * `docs/protokolle/eval_protokoll_phase04.md` §1 and §6 (invocation lines, repetition
    counts, graph mode, run acceptance rules)
  * `docs/repo-kontext/c2b_bericht_k4_konfiguration.md` (K4)
  * `docs/repo-kontext/c2c_bericht_k5_konfiguration.md` (K5)

Read by `run_campaign.py` and `postrun_check.py`; carries no state and runs nothing.
"""

from __future__ import annotations

# ── the frozen measurement state ──────────────────────────────────────────────────────
#
# Protokoll §1 Nachtrag Rev. 24 (build provenance) and §6 Nachtrag Rev. 30 (3), reference
# values from `d2_bericht_vormessungen.md` M5(d).

EXPECTED_CLI_SHA256 = "c0bbdfebbdce5899cc7d24d271b8fc43c9fc53aec5e8b0f3e3e91c3d43d35d95"
EXPECTED_CHECKER_HEAD = "348ca9daa456af4954f11f7152fc45201035297e"
EXPECTED_BASELINE_SHA = "0d651041ed87dd03f2f78359713633fac01c0a66"

# `d2_bericht_vormessungen.md` M5(d) — the reference machine identification. Recorded per run
# and compared; a deviation is REPORTED, not fatal (protocol §9 T13: the gate is the build
# hash, not the node version).
REFERENCE_MACHINE = {
    "uname": "Linux DESKTOP-PJA89CF 5.15.153.1-microsoft-standard-WSL2 #1 SMP "
             "Fri Mar 29 23:14:13 UTC 2024 x86_64 x86_64 x86_64 GNU/Linux",
    "python3": "Python 3.12.3",
    "node": "v22.23.2",
}

# ── the context windows ───────────────────────────────────────────────────────────────
#
# MEASURED environment parameters, not model limits. K2: protocol §1 Nachtrag Rev. 26 — no
# `num_ctx` is set (`llmClient.ts:114-124`), Ollama loads `CONTEXT 4096` instead of the model
# limit 32768. K3: protocol §1 Nachtrag Rev. 30, verbatim from the DigitalOcean catalogue
# (`d2_bericht_vormessungen.md` M1).
CONTEXT_WINDOW = {
    "K2": {"context_length": 4096, "max_output_tokens": None},
    "K3": {"context_length": 1_000_000, "max_output_tokens": 32_768},
}

# The K2 entry above is the value MEASURED IN C3B, not a limit to trust going forward. §1
# Nachtrag Rev. 26 registers it as an environment parameter, and an environment parameter is
# re-measured per campaign session — a changed Ollama default would silently shrink the window
# and Ollama truncates AT THE FRONT, without error and without a log line. `run_campaign.py`
# measures it (`ollama show` + `ollama ps`, raw output into the run manifest) and checks the
# token budget against the MEASURED value; this constant is only the registered comparison
# value the measurement is held against.
K2_REGISTERED_CONTEXT_LENGTH = 4096

# The model whose loaded window is measured — the same string the invocation line carries.
K2_MODEL = "qwen2.5-coder:7b"

# `ollama show` reports the MODEL limit, not the loaded window (`k2_machbarkeitslauf_bericht.md`
# §1b: "context length 32768 ist die vom Modell unterstützte Obergrenze, nicht das tatsächlich
# beim Laden verwendete Kontextfenster"). Recorded and compared, never used as the budget.
K2_MODEL_CONTEXT_LENGTH = 32768

# ── the graph mode, DERIVED — protocol §6 Rev. 7 and Nachtrag Rev. 31 ─────────────────
#
# Rev. 31 makes this an obligation, not a style question: the mode is derived from
# `category_l1` of the manifest entry and NEVER set per invocation line. A hand-set mode is
# a line that CAN deviate from the category; a derived one is a line that CANNOT.

def graph_mode(category_l1: str) -> str:
    """`full` for CYCLE, `diff` otherwise (protocol §6 Nachtrag Rev. 31)."""
    return "full" if category_l1 == "CYCLE" else "diff"


# ── repetition counts, per configuration — protocol §6 Nachtrag Rev. 24 ───────────────
#
# K1 `--runs 1`, K2 `--runs 3`, K3 `--runs 3`. K4 and K5 have no repetition option at all
# (§6 Rev. 24, "Bewusste Lücken/Nichtanwendbarkeit"): one invocation is one run.
RUNS = {"K1": 1, "K2": 3, "K3": 3, "K4": None, "K5": None}

# Timeouts, same source.
TIMEOUT_MS = {"K1": 120000, "K2": 240000, "K3": 600000}

# ── the environment blocks of the LLM configurations ──────────────────────────────────
#
# K2 — protocol §6 Nachtrag Rev. 24, section "K2, Ollama (je Injektion)".
K2_ENV = {
    "CONFORMANCE_API_KEY": "ollama",           # <ollama-dummy-key>
    "CONFORMANCE_BASE_URL": "http://localhost:11434/v1",
    "CONFORMANCE_MODEL": "qwen2.5-coder:7b",
}

# K3 — protocol §6 Nachtrag Rev. 32, section "K3, DigitalOcean-Direktzugang (je Injektion) —
# KORRIGIERTE FASSUNG". The rev. 24 block (OpenRouter endpoint, OpenRouter slug,
# `CONFORMANCE_PROVIDER_PIN=digitalocean`) stands struck through in the protocol and is NOT
# used. `CONFORMANCE_PROVIDER_PIN` is deliberately absent: without a router there is nothing
# to pin (B32), and `cli.ts:50` reads it as `undefined`.
K3_ENV = {
    "CONFORMANCE_BASE_URL": "https://inference.do-ai.run/v1",
    "CONFORMANCE_MODEL": "nvidia-nemotron-3-super-120b",
}
K3_KEY_FILE = ".secrets/do.env"   # `k3_machbarkeitslauf_direktzugang_bericht.md` §3
K3_KEY_VAR = "DO_MODEL_ACCESS_KEY"


def checker_argv(cli_js: str, topology: str, rules: str, mode: str, base_sha: str,
                 runs: int, timeout_ms: int, run_log: str, json_out: str,
                 control_files: str | None = None) -> list[str]:
    """The checker invocation of protocol §6 Nachtrag Rev. 24, verbatim.

    Identical for K1, K2 and K3 — the three differ only in the environment block, in `--runs`
    and in `--timeout-ms`. `--base` is ALWAYS the baseline SHA out of the manifest, never a
    relative reference (protocol §6 Amendment 11.08.: `base_ref` is logged verbatim and not
    resolved, so a relative reference is only interpretable together with the repo history).
    `--src-root src` is fixed before C4 because it determines the third segment of every
    `match_key` (`b1_bericht_matchkey.md` D1).

    `--control-files` stands only in the K2/K3 control run and in no injection run (§6
    Rev. 24, "Bewusste Lücken"): it feeds unchanged files into the LLM path, not into the
    static baselines.
    """
    argv = [
        "node", cli_js,
        "--topology", topology,
        "--rules", rules,
        "--src-root", "src",
        "--rule-graph", mode,
        "--base", base_sha,
        "--runs", str(runs),
        "--timeout-ms", str(timeout_ms),
    ]
    if control_files is not None:
        argv += ["--control-files", control_files]
    argv += ["--run-log", run_log, "--json-out", json_out]
    return argv


def k4_argv(venv_bin: str, config_ini: str) -> list[str]:
    """K4 — protocol §6 Nachtrag Rev. 24 plus Nachtrag Rev. 32 (Schreibform).

    `PYTHONPATH=src` with an ABSOLUTE `--config`, `cwd = <testrepo>`, `--no-cache`. Rev. 32
    fixes this writing form so the runner does not have to choose between it and the
    equivalent form of `c2b_bericht_k4_konfiguration.md` §B3 (`PYTHONPATH=<baseline>/src`,
    relative `--config`, `cwd = <ma>`); both resolve to the same absolute paths under the
    working directory laid down in §6.

    `--no-cache` on EVERY import-linter invocation: protocol §1 Amendment 11.08. (B9+ (b)).
    """
    return [f"{venv_bin}/lint-imports", "--config", config_ini, "--no-cache"]


def k5_argv(venv_bin: str, test_file: str) -> list[str]:
    """K5 — protocol §6 Nachtrag Rev. 32, "KORRIGIERTE FASSUNG".

    The rev. 24 line lacked `DEPOT_SRC` and was therefore NOT EXECUTABLE: the frozen K5
    configuration derives `root_path` and `module` from that variable at module level
    (`data/soll/test_architecture.py`), so pytest aborts during COLLECTION and 0 of 23 rules
    run — indistinguishable from a clean run by exit code or output. `DEPOT_SRC` is set by
    the caller in the environment block.

    `-q` stays (rev. 32): the sharpness proof in `c2c_bericht_k5_konfiguration.md` §B5 — the
    empirical basis of the K4/K5 match rule — was measured with it, and its output forms are
    the reference for the raw-text obligation of §6 Nachtrag Rev. 30 (2).

    `-p no:cacheprovider` on every pytest invocation (`c2c` §0).
    """
    return [f"{venv_bin}/python", "-m", "pytest", "-p", "no:cacheprovider", "-q", test_file]


# ── the run acceptance rules ──────────────────────────────────────────────────────────
#
# Protocol §6 Nachtrag Rev. 26 (repetition factor) and Nachtrag Rev. 32 (3) (positive rule
# for K4/K5). Enforced by `postrun_check.py`, which is their sole executor (§6 Rev. 24).

# K5: 19 allow-list rules + 4 port rules + 1 guard test = 24 collected tests. Derived from
# `data/soll/test_architecture.py`, cross-checked against C3a §3b, D2 M5(c)
# (`collected 24 items`) and C2c §B4.
K5_EXPECTED_COLLECTED = 24

# K4: 13 `[importlinter:contract:*]` sections in `data/soll/importlinter.ini`, cross-checked
# against C3a §3a (`Contracts: 13 kept, 0 broken`).
K4_EXPECTED_CONTRACTS = 13

# ── the expected state of the Soll validator per injection commit ─────────────────────
#
# The validator is written for the CLEAN baseline. Its points (1)-(6) are commit-invariant
# and are the precondition of protocol §2 Rev. 11; its points (7) "component graph of the
# actual state" and (8) "no module edge outside the whitelist" describe the ACTUAL STATE and
# therefore deviate on an injection commit BY THE INJECTION ITSELF. Both deviations are
# pre-registered, so they are checked against the registration instead of aborting.
#
# Cycles per injection commit, measured and registered in `c4b_bericht_injektionen.md` §8.5
# and carried into the protocol as §3 Nachtrag Rev. 29: I13-I16 one cycle each (the CYCLE
# injections), I01-I03 one cycle each — CONSTRUCTION-BOUND, because `LAYER_BACK_CALL`
# injects the counter-edge to the spine edge `<k>_services -> <k>_repository` — and every
# other injection zero.
EXPECTED_CYCLES = {f"I{n:02d}": 1 for n in (1, 2, 3, 13, 14, 15, 16)}


def expected_cycles(injection_id: str) -> int:
    return EXPECTED_CYCLES.get(injection_id, 0)


def expected_whitelist_edge(manifest_entry: dict) -> str | None:
    """The one component edge the injection adds outside the whitelist, or None.

    Taken from `expected_edge_boundary` of the manifest entry. The sixteen semantic
    injections carry "keine Kante" there: `ABSENCE_REQUIRED` removes an import,
    `FORBIDDEN_SIGNATURE_TYPE` leaves the import set unchanged (protocol §3 Am. (h)),
    `STRUCTURAL_PLACEMENT` moves an import-free module, `API_CONTRACT` touches a signature.
    """
    raw = manifest_entry.get("expected_edge_boundary") or ""
    if raw.startswith("keine Kante"):
        return None
    return raw.split(" (")[0].strip()


# The pre-registered control set (protocol §5 Nachtrag Rev. 17, `data/soll/control_files.txt`).
CONTROL_FILES_COUNT = 52
