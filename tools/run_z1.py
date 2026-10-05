#!/usr/bin/env python3
"""Z1 run driver -- preconditions, invocation, parse assertions, archive.

WHAT THIS IS AND WHAT IT IS NOT
-------------------------------
This driver CALLS the extractor (`llm_arch.cli:app`, the entry point the console
script `llm-arch` exposes). It does NOT reimplement a single line of it: no fact
extraction, no prompting, no metric. Every number it reports is read back out of
artifacts the extractor wrote itself.

It computes NO metric of its own. Z1 evaluation (medians, ranges, the section 8
verdicts, ARI) is a separate task (Z1-A). This driver reports validity, counters
and provenance -- nothing else.

THE THREE STOP CLASSES, NEVER WARNINGS (protocol section 6, section 5)
----------------------------------------------------------------------
(1) PRECONDITION  -- checked BEFORE any call can be issued. A dirty extractor
    worktree, a wrong HEAD, a moved input blob, a moved schema hash, a target
    path that already exists: the driver exits, no model is contacted.
(2) INSTRUMENT    -- `valid_final` missing from a meta.json. Protocol section 5.2:
    `bool(None)` is False, so a missing field would run as a silent `false`.
    This is a HARD STOP, not a repeat: the field is written unconditionally by
    run_logger.py, so its absence means the artifact is not what section 3
    registered. The run is NOT counted as invalid and NOT scored as 0.
(3) RUN FINDING   -- `valid_final == false`, or a parse assertion (P1/P2) that
    fires. That is a finding ABOUT THE RUN, not a bug in this driver: the raw
    response is archived, the run is journalled as invalid, and the condition is
    repeated (at most three repetitions, protocol section 5.4).

THE PARSE ASSERTIONS (protocol section 5.3) -- THE CORE
------------------------------------------------------
Measured cause, not a feared one. In the test call of 2026-08-31 the answer
carried TWO edges and the parsed model NONE
(`z1_p_bericht_endpunktfrage.md` section 3.3, check C: "components: 3 |
relations: 0 - Relationen des Modells gehen verloren: 2 Kanten im Dokument -> 0
im ArchModel"). The edges fell out SILENTLY: the document carried them under
`dependencies` instead of `relations`, the schema permits foreign keys (there is
no `additionalProperties: false` anywhere in it), pydantic drops unknown fields,
and `relations` has a default. `ArchModel.model_validate_json()` accepted the
answer WITHOUT error and returned a model that was substantively amputated.

    P1  key set of the raw answer against the field set of `ArchModel`,
        recursively into `Component` and `Relation`. Any foreign key aborts.
    P2  number of components and relations RAW against PARSED. Any difference
        aborts.

The schema is NOT adjusted -- it is the instrument, exactly as the 17 archived
June runs used it; `additionalProperties: false` would move the measured object
in the middle of the comparison chain. The assertion sits AT THE PARSE BOUNDARY.

The field sets are DERIVED from the pydantic models at run time, never
transcribed: a transcribed field list would be a second source of truth that can
drift away from the schema it is supposed to guard.

Decisive is the LAST attempt -- it produces `arch_model.json` and therefore every
reported figure. Both comparisons are additionally computed for every earlier
attempt and reported, but do not abort: an early attempt may be form-alien, that
is what the retry loop is for.

SECRETS
-------
`DO_MODEL_ACCESS_KEY` is read in-process from ~/ma/.secrets/do.env and handed to
the child through the environment -- never into a file, an argv, or an output.
Every captured stream is passed through `redact()` before it is stored or shown.

INVOCATION
----------
    python tools/run_z1.py --plan
    python tools/run_z1.py --selftest
    python tools/run_z1.py --condition k2
    python tools/run_z1.py --condition k3
    python tools/run_z1.py --finalize k2

Needs an interpreter that can import `llm_arch` (PYTHONPATH=<extractor>/src) with
pydantic and openai installed -- the same environment the runs execute in, so the
schema hash this driver checks is the schema hash the calls actually send.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import queue
import shutil
import subprocess
import sys
import threading
import time
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
EXTRACTOR = Path.home() / "ma" / "ma-llm-arch-extractor"
ARCHIVE_ROOT = REPO / "data" / "z1"
SECRETS_FILE = Path.home() / "ma" / ".secrets" / "do.env"

# --- what section 3 of the protocol registered ------------------------------------------

EXTRACTOR_COMMIT = "5c0b65a82cc3d8af47c022d779ff63d8a20a9e08"
PROMPT_FILE = "src/llm_arch/abstraction/prompt.py"
PROMPT_VERSION_EXPECTED = "v3"

# The archived form of `ArchModel.model_json_schema()`, protocol section 3.2:
# json.dumps(schema, indent=2, ensure_ascii=False) + "\n". The wire form
# (separators=(",",":")) is registered too; the archived one is the anchor
# because it is bound to a versioned file.
SCHEMA_SHA256_ARCHIVED = "a83a84af306d647f2d4d9618a39f9b0059431015d3e5234bce931df642012ec0"
SCHEMA_SHA256_WIRE = "1a4cf09cbe22e08dba4ff2d4a4c09234e37131e8d4fab78be654ff7248f70b23"

# path -> (git blob SHA1, SHA256 of the blob bytes), protocol sections 3.1 and 3.2.
# The BLOB is the reference, not the worktree file (protocol section 3): otherwise
# the measured state would hang on line endings and editor states. Both are checked
# anyway -- blob against registration, and worktree against blob.
REGISTERED_BLOBS: dict[str, tuple[str, str]] = {
    "fixtures/PROVENANCE.md": (
        "a3221fa9419f1405989bb199ab2891a5694fac9f",
        "c5dda4dcedcacd35330ada9833a97dfc304c3ddced281daa065003ca011ca3b6"),
    "fixtures/rich_repo.full.ilograph.yaml": (
        "ef8e0d0181eccddf5b2e88f3315c418cc1270208",
        "34d6f2f4c7731c5a1a8640e6d1583218d0b73d2875a623f311208f20345d915f"),
    "fixtures/rich_repo.gold.json": (
        "f34f74849ab6e74cf16e0212cf090045041387be",
        "481c3aad5c5d6c4a19d446c0519ea9209820a4cb57d954e41a044a5b71a278a3"),
    "fixtures/rich_repo/bookshop/__init__.py": (
        "d7a77ac4854dbe1c9134adae23ebbd6d1f9fb3e5",
        "3375f2d18b7a39c306831decb09b23b4d5d734bda42d7f16b10ca1ca310f654f"),
    "fixtures/rich_repo/bookshop/api/__init__.py": (
        "e69de29bb2d1d6434b8b29ae775ad8c2e48c5391",
        "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"),
    "fixtures/rich_repo/bookshop/api/catalog_routes.py": (
        "6772d542150e1e71f298182f9d5d97b74746c1ef",
        "56787ef8075a0cdf338d7f7964a6febf4396bb12dbd370ac0ed3a950dae1df55"),
    "fixtures/rich_repo/bookshop/api/checkout_routes.py": (
        "6aff2cbd01edaf989d8292e09d39ebeacdf7d5cb",
        "b8cb66670cd614010bf9466fcd3d962e944e2edd402562df7c86db0ef4386a2e"),
    "fixtures/rich_repo/bookshop/application/__init__.py": (
        "e69de29bb2d1d6434b8b29ae775ad8c2e48c5391",
        "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"),
    "fixtures/rich_repo/bookshop/application/checkout.py": (
        "5bad7691614fef54793e17a3247f098c0c1d980d",
        "d70971541fe42658927c5163370800f05d298efe3f259417d257a82f0f611119"),
    "fixtures/rich_repo/bookshop/application/inventory.py": (
        "fe27bcbfb642c71dcad1488b0bdb4eaa594b2ff9",
        "046398eff2645522379f2b8b96f6ff6f313e93f001921faac93d0ce6f011614a"),
    "fixtures/rich_repo/bookshop/domain/__init__.py": (
        "e69de29bb2d1d6434b8b29ae775ad8c2e48c5391",
        "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"),
    "fixtures/rich_repo/bookshop/domain/book.py": (
        "06405dc040f30f87203c6a4387d364830e0fa2c7",
        "eda3a2da15155a3f8698ba017dbe78f0db019bc9b9856b34beeacb92c0771100"),
    "fixtures/rich_repo/bookshop/domain/catalog.py": (
        "a23a28aefa60483b7c4173b75f416a98694eddd8",
        "628ecefda4324d75d2ec092c88912e598003cc110e9bc64789a59ed1c0b1074c"),
    "fixtures/rich_repo/bookshop/domain/order.py": (
        "f3ee4afec980f026d12165a2c296da4711fd3918",
        "76f2a392c67b8bf05a3280f724b219e1edf83aee37b6402a6e81037f504ad323"),
    "fixtures/rich_repo/bookshop/domain/pricing.py": (
        "ee9e35df44db588cd46a38237637a5c943f245d5",
        "6fa1fd05e27119acf50398fdc8aed54ff5df0ffa524294bd4d1d8875975f0e8a"),
    "fixtures/rich_repo/bookshop/infrastructure/__init__.py": (
        "e69de29bb2d1d6434b8b29ae775ad8c2e48c5391",
        "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"),
    "fixtures/rich_repo/bookshop/infrastructure/book_repository.py": (
        "ee479d6a0b8bd693b267cfbf13f5ce61ec362ca4",
        "57e851ff56ed5357cb823cbb070f61096e7ba99ff4120c3edf15a353bff9c9ae"),
    "fixtures/rich_repo/bookshop/infrastructure/order_repository.py": (
        "859c30e3993bb9cb6c34dac97b88d44bde65cb3d",
        "8fe4ebdd394f5de1fd7ffff253ecf5637f8a72afb8b0c964c87f9491d826548c"),
    "fixtures/rich_repo/bookshop/infrastructure/payment_gateway.py": (
        "1e8e1fbaff286959689cda0eb4ad18c0adf78cdd",
        "e8049b0af15df9144d1753351941427c1212a83756213a3f7d7aa0086381d893"),
    "scripts/compare_runs.py": (
        "c6db316b3904338d034ac65297aa8557f1fee028",
        "5728c1438187bd7b3208402f229ae05876aaac444a45fc57735eec018c9efa16"),
    "src/llm_arch/abstraction/abstractor.py": (
        "84ae1a024aac1973be99993dff149edfe3402ac0",
        "ef7a8c15410a884f5dbd945257fe43af493d756145a9c01fd86d7864881ac09d"),
    "src/llm_arch/abstraction/prompt.py": (
        "6c8e4639441df6081c6d5bf9bc29b40c04033f61",
        "ed9e1ebd51c6328968ecd7645bd073c4512f99b2512ad75f35f486272f946d46"),
    "src/llm_arch/abstraction/schema.py": (
        "5846232d9328685294f8d49f84a1546b2c843ec5",
        "03379c14f304ba37b1cccd797f42b61ec3a28350ee95fcec617c93271a8e4636"),
    "src/llm_arch/cli.py": (
        "f1fe37dd56ca8ef4b430edfc8dcabf176356ca5a",
        "407b04e56ba5a49180982e25caedb8aac65696ed6077a7c47b9d2977db0a8c9d"),
    "src/llm_arch/eval/metrics.py": (
        "54a8021c51f1a05447b5ec64005853d5a8c9760b",
        "668d6d47e68923b78cb339b38ea7b39b64a5f4ce7bd3c9c99a8004825934cdb6"),
    "src/llm_arch/logging/run_logger.py": (
        "cc6d3cc4d71446b1ace9cc64a0ad94eea1410257",
        "6e6d2b3d1da65639faba31c46a086ce40f214dffe16fd55cd8cad29ba35dbe5d"),
    "src/llm_arch/providers/openai_compatible.py": (
        "9cbfc91e7bfda91ebc41d11ecd50a63f32a8a1d8",
        "6a48a882be339d713add7f8a2460c1ac80d008af9c133771954f8578017ce07f"),
    "tests/test_reader.py": (
        "7fc33d1b795debca65488afb863c35dc2517622d",
        "3c58a2d0480f7baca70946bbafe1836e3e78b3a47da274ab32011146833bd1b7"),
}

# --- the six runs (protocol section 2.2, section 6.2) -----------------------------------

FIXTURE = "fixtures/rich_repo"
RUNS_PER_CONDITION = 3
MAX_REPEATS = 3
MAX_CONSECUTIVE_TRANSPORT_FAILURES = 3   # K3 stop rule
STALL_SECONDS = 600                      # K3 stop rule: ten minutes without progress

CONDITIONS: dict[str, dict[str, str | None]] = {
    "k2": {
        "model": "qwen2.5-coder:7b",
        "provider": "ollama",
        "base_url": "http://localhost:11434/v1",
        "api_key_env": None,
        "note": "lokal, kostenlos, kein Kontingent",
    },
    "k3": {
        "model": "nvidia-nemotron-3-super-120b",
        "provider": "digitalocean",
        "base_url": "https://inference.do-ai.run/v1",
        "api_key_env": "DO_MODEL_ACCESS_KEY",
        "note": "DigitalOcean-Direktzugang, derselbe Zugangsweg wie K3 in Z3",
    },
}


class Abort(RuntimeError):
    """A pre-registered stop condition. Never a warning, never a fallback."""


class InstrumentAbort(Abort):
    """The artifact is not what the protocol registered -- a repeat cannot help."""


# --- secrets ----------------------------------------------------------------------------

_SECRETS: dict[str, str] = {}


def load_secrets() -> dict[str, str]:
    """Read ~/ma/.secrets/do.env in-process. The value never leaves this dict."""
    if _SECRETS:
        return _SECRETS
    if not SECRETS_FILE.exists():
        raise Abort(f"Schlüsseldatei fehlt: {SECRETS_FILE}")
    for line in SECRETS_FILE.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        line = line.removeprefix("export ").strip()
        if "=" in line:
            name, _, value = line.partition("=")
            _SECRETS[name.strip()] = value.strip().strip('"').strip("'")
    return _SECRETS


def redact(text: str) -> str:
    """Replace every loaded secret value by a placeholder. Key incident 24.08."""
    for value in _SECRETS.values():
        if value and len(value) >= 8:
            text = text.replace(value, "***REDACTED***")
    return text


# --- small helpers ----------------------------------------------------------------------


def utcnow() -> str:
    return datetime.now(timezone.utc).isoformat()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def git(root: Path, *args: str) -> str:
    """Run git in `root` and return stdout, or raise Abort with the stderr."""
    proc = subprocess.run(
        ["git", "-C", str(root), *args], capture_output=True, text=True
    )
    if proc.returncode != 0:
        raise Abort(f"git {' '.join(args)} in {root}: {redact(proc.stderr.strip())}")
    return proc.stdout


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(REPO))
    except ValueError:
        return str(path)


def say(*parts: object) -> None:
    print(*parts, flush=True)


# --- preconditions (protocol section 6.1, order 2a) -------------------------------------


def check_worktree_clean(root: Path, label: str) -> None:
    """Abort on ANY porcelain output -- BEFORE a call can come into existence.

    In the WSL clone ~/ma/ma-llm-arch-extractor this is genuinely empty; the
    "60 CRLF lines" of the old clone under /mnt/c are not an exception that is
    tolerated here (z1_1 section 0.3, E-X section 0).
    """
    out = git(root, "status", "--porcelain")
    if out.strip():
        lines = out.strip().splitlines()
        raise Abort(
            f"Arbeitsbaum {label} ({root}) ist NICHT leer -- "
            f"{len(lines)} Zeile(n), erste: {lines[0]!r}. "
            "Kein Call wird abgesetzt (Protokoll §6.1)."
        )


def check_head(root: Path, expected: str) -> str:
    head = git(root, "rev-parse", "HEAD").strip()
    if head != expected:
        raise Abort(f"Extractor-HEAD ist {head}, Soll {expected} (Protokoll §3).")
    return head


def check_input_blobs(root: Path, expected: dict[str, tuple[str, str]]) -> dict[str, str]:
    """Every registered input, blob against registration AND worktree against blob.

    `expected` is a parameter, not a global read, so the self-test can drive a
    deliberately falsified expectation table against the untouched extractor.
    """
    index = {}
    for line in git(root, "ls-files", "-s").splitlines():
        meta, _, path = line.partition("\t")
        parts = meta.split()
        if len(parts) >= 2:
            index[path] = parts[1]

    problems: list[str] = []
    for path, (blob_sha1, blob_sha256) in sorted(expected.items()):
        actual_sha1 = index.get(path)
        if actual_sha1 is None:
            problems.append(f"{path}: nicht im Index von {root}")
            continue
        if actual_sha1 != blob_sha1:
            problems.append(
                f"{path}: Blob IST {actual_sha1}, SOLL {blob_sha1}")
            continue
        raw = subprocess.run(
            ["git", "-C", str(root), "cat-file", "blob", blob_sha1],
            capture_output=True, check=True).stdout
        actual_sha256 = sha256_bytes(raw)
        if actual_sha256 != blob_sha256:
            problems.append(
                f"{path}: SHA256 der Blob-Bytes IST {actual_sha256}, SOLL {blob_sha256}")
            continue
        # The worktree must be byte-identical with the blob (protocol section 3:
        # "12 von 12 gleich, der Arbeitsbaum ist byteidentisch mit dem Index").
        worktree = root / path
        if not worktree.exists():
            problems.append(f"{path}: im Arbeitsbaum nicht vorhanden")
            continue
        wt_sha1 = subprocess.run(
            ["git", "hash-object", str(worktree)],
            capture_output=True, text=True, check=True).stdout.strip()
        if wt_sha1 != blob_sha1:
            problems.append(
                f"{path}: Arbeitsbaum {wt_sha1} weicht vom Blob {blob_sha1} ab")

    if problems:
        raise Abort(
            "Gehashte Messeingänge weichen ab (Protokoll §3) -- "
            f"{len(problems)} von {len(expected)}:\n  " + "\n  ".join(problems))
    return {"geprueft": f"{len(expected)} von {len(expected)} gleich"}


def check_prompt(root: Path) -> dict[str, str]:
    """Prompt file, blob hash and PROMPT_VERSION -- meta.json carries only the version."""
    blob_sha1, blob_sha256 = REGISTERED_BLOBS[PROMPT_FILE]
    text = (root / PROMPT_FILE).read_text(encoding="utf-8")
    version = None
    for line in text.splitlines():
        if line.startswith("PROMPT_VERSION"):
            version = line.split("=", 1)[1].strip().strip('"').strip("'")
            break
    if version != PROMPT_VERSION_EXPECTED:
        raise Abort(
            f"PROMPT_VERSION ist {version!r}, Soll {PROMPT_VERSION_EXPECTED!r} "
            "(Protokoll §2.2).")
    return {
        "file": PROMPT_FILE,
        "blob_sha1": blob_sha1,
        "blob_sha256": blob_sha256,
        "PROMPT_VERSION": version,
    }


def environment() -> dict[str, str]:
    """The three runtime versions -- nowhere in the run record (protocol §3.3 (4))."""
    import openai
    import pydantic

    return {
        "python": ".".join(str(n) for n in sys.version_info[:3]),
        "pydantic": pydantic.VERSION,
        "openai": openai.__version__,
        "registriert_in_protokoll": "python 3.12.3 · pydantic 2.13.5 · openai 3.6.0",
    }


def check_schema_hash() -> dict[str, str]:
    """Recompute `ArchModel.model_json_schema()` IN THIS ENVIRONMENT (protocol §3.3 (4)).

    A deviating version is reported; a deviating schema hash forbids the run.
    """
    from llm_arch.abstraction.schema import ArchModel

    schema = ArchModel.model_json_schema()
    archived = json.dumps(schema, indent=2, ensure_ascii=False) + "\n"
    wire = json.dumps(schema, separators=(",", ":"))
    got_archived = sha256_bytes(archived.encode("utf-8"))
    got_wire = sha256_bytes(wire.encode("utf-8"))
    if got_archived != SCHEMA_SHA256_ARCHIVED:
        raise Abort(
            "Schema-Hash weicht ab -- der Lauf ist NICHT zu starten, bis die "
            "Abweichung als Amendment (§10) registriert ist.\n"
            f"  IST  {got_archived}\n  SOLL {SCHEMA_SHA256_ARCHIVED}")
    return {
        "archived_sha256": got_archived,
        "wire_sha256": got_wire,
        "wire_matches_registration": str(got_wire == SCHEMA_SHA256_WIRE),
    }


def check_thesis_repo() -> dict[str, str]:
    """masterarbeit porcelain empty and the document invariants at exit 0 (§6.1).

    Narrowed for exactly one path: `data/z1/`. Protocol section 6.1 demands an empty
    porcelain per run, and section 6.4 demands that the same run be archived under
    `masterarbeit/data/z1/`. Both hold at once only if the archive the driver is
    writing right now is exempt -- otherwise no second run could ever start. Every
    OTHER porcelain entry still aborts, and the tolerated entries are listed, never
    swallowed.
    """
    raw = git(REPO, "status", "--porcelain").strip()
    entries = [line for line in raw.splitlines() if line.strip()]
    archive_prefix = rel(ARCHIVE_ROOT)
    tolerated = [e for e in entries if e[3:].strip().strip('"').startswith(archive_prefix)]
    foreign = [e for e in entries if e not in tolerated]
    if foreign:
        raise Abort(
            "Arbeitsbaum masterarbeit ist NICHT leer, ausserhalb der Archivwurzel "
            f"{archive_prefix}/ -- {len(foreign)} Zeile(n), erste: {foreign[0]!r} "
            "(Protokoll §6.1).")
    proc = subprocess.run(
        [sys.executable, str(REPO / "tools" / "check_doc_invariants.py")],
        capture_output=True, text=True, cwd=str(REPO))
    if proc.returncode != 0:
        raise Abort(
            "check_doc_invariants.py meldet Exit "
            f"{proc.returncode}:\n{redact(proc.stdout[-2000:])}")
    return {
        "porcelain_ausserhalb_data_z1": "leer",
        "porcelain_geduldet_unter_data_z1": tolerated,
        "check_doc_invariants": "Exit 0",
    }


def preconditions(root: Path, condition: str | None) -> dict[str, object]:
    """Every stop condition of protocol section 6.1, in order. Abort, never warn."""
    check_worktree_clean(root, "Extractor")
    head = check_head(root, EXTRACTOR_COMMIT)
    blobs = check_input_blobs(root, REGISTERED_BLOBS)
    prompt = check_prompt(root)
    env = environment()
    schema = check_schema_hash()
    thesis = check_thesis_repo()
    return {
        "checked_utc": utcnow(),
        "extractor_root": str(root),
        "extractor_head": head,
        "extractor_porcelain": "leer",
        "input_blobs": blobs,
        "prompt": prompt,
        "environment": env,
        "arch_model_schema": schema,
        "thesis_repo": thesis,
        "condition": condition,
    }


# --- the plan (order 2e) ----------------------------------------------------------------


def slot_dir(condition: str, slot: str) -> Path:
    return ARCHIVE_ROOT / condition / slot


def planned_runs() -> list[dict[str, str]]:
    """The six runs with condition, profile, model and target path."""
    plan = []
    for condition, cfg in CONDITIONS.items():
        for i in range(RUNS_PER_CONDITION):
            plan.append({
                "condition": condition.upper(),
                "model": str(cfg["model"]),
                "profile": str(cfg["provider"]),
                "base_url": str(cfg["base_url"]),
                "run_index": str(i),
                "slot": f"run{i}",
                "target": rel(slot_dir(condition, f"run{i}")),
            })
    return plan


def assert_targets_distinct(plan: list[dict[str, str]]) -> None:
    """All target paths pairwise distinct -- an overwrite is not a run, it is a loss."""
    targets = [row["target"] for row in plan]
    if len(set(targets)) != len(targets):
        dupes = sorted({t for t in targets if targets.count(t) > 1})
        raise Abort(f"Zielpfade nicht paarweise verschieden: {dupes}")


def print_plan() -> None:
    plan = planned_runs()
    assert_targets_distinct(plan)
    say("Z1 --plan · sechs Läufe, zwei Bedingungen, je eine Invocation mit --runs 3")
    say("")
    header = f"{'Bed.':<5} {'Profil':<13} {'Modell':<30} {'run_index':<9} Zielpfad"
    say(header)
    say("-" * len(header))
    for row in plan:
        say(f"{row['condition']:<5} {row['profile']:<13} {row['model']:<30} "
            f"{row['run_index']:<9} {row['target']}")
    say("")
    say(f"Zielpfade paarweise verschieden: {len(set(r['target'] for r in plan))} "
        f"von {len(plan)} — OK")
    say("Aufrufform je Bedingung (Protokoll §6.2, cwd = Extractor):")
    for condition, cfg in CONDITIONS.items():
        say(f"  [{condition.upper()}] llm-arch extract {FIXTURE} "
            f"--provider {cfg['provider']} --model {cfg['model']} --runs 3")
    say("Wiederholungen (§5.4) laufen als Einzelinvocation mit --runs 1 und "
        "landen unter run<i>_w<k>, nie auf einem bestehenden Pfad.")


# --- the parse assertions (protocol section 5.3) ----------------------------------------


def model_field_names(model: type) -> set[str]:
    """Field names AND aliases of a pydantic model -- derived, never transcribed.

    `Relation` carries `populate_by_name=True`, so both `from` (alias) and `from_`
    (field name) are legitimate keys; a transcribed list would call one of them
    foreign and abort a run that never deviated.
    """
    names: set[str] = set()
    for name, field in model.model_fields.items():
        names.add(name)
        if field.alias:
            names.add(field.alias)
    return names


def p1_foreign_keys(document: object) -> list[str]:
    """P1 -- every key of the raw answer against the field set of ArchModel.

    Recursive: top level, then every entry of `components` and of `relations`.
    """
    from llm_arch.abstraction.schema import ArchModel, Component, Relation

    problems: list[str] = []
    if not isinstance(document, dict):
        return [f"Rohantwort ist kein JSON-Objekt, sondern {type(document).__name__}"]

    for key in document:
        if key not in model_field_names(ArchModel):
            problems.append(f"ArchModel: Fremdschlüssel {key!r}")

    for label, model in (("components", Component), ("relations", Relation)):
        entries = document.get(label)
        if entries is None:
            continue
        if not isinstance(entries, list):
            problems.append(f"{label}: kein JSON-Array, sondern {type(entries).__name__}")
            continue
        allowed = model_field_names(model)
        for i, entry in enumerate(entries):
            if not isinstance(entry, dict):
                problems.append(f"{label}[{i}]: kein JSON-Objekt")
                continue
            for key in entry:
                if key not in allowed:
                    problems.append(
                        f"{label}[{i}] ({model.__name__}): Fremdschlüssel {key!r}")
    return problems


def raw_counts(document: object) -> tuple[int, int]:
    """Component and relation count as the RAW answer carries them."""
    if not isinstance(document, dict):
        return (-1, -1)
    comps = document.get("components")
    rels = document.get("relations")
    return (
        len(comps) if isinstance(comps, list) else 0,
        len(rels) if isinstance(rels, list) else 0,
    )


def response_document(raw_response: dict) -> tuple[object | None, str | None]:
    """The model's JSON document out of `choices[0].message.content`."""
    try:
        content = raw_response["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError) as exc:
        return None, f"choices[0].message.content nicht lesbar: {exc}"
    if not isinstance(content, str) or not content.strip():
        return None, "choices[0].message.content ist leer"
    try:
        return json.loads(content), None
    except json.JSONDecodeError as exc:
        return None, f"content ist kein gültiges JSON: {exc}"


def parsed_counts_of(content_doc: object) -> tuple[int, int] | None:
    """What `ArchModel.model_validate_json` makes of the document, counted.

    This reproduces in-process exactly what the extractor did, so an earlier
    attempt (whose parsed model is not archived) can be checked too.
    """
    from pydantic import ValidationError

    from llm_arch.abstraction.schema import ArchModel

    try:
        arch = ArchModel.model_validate(content_doc)
    except ValidationError:
        # abstractor.py substitutes ArchModel(components=[]) on a validation error.
        return (0, 0)
    return (len(arch.components), len(arch.relations))


def assert_attempt(run_dir: Path, index: int, decisive: bool,
                   archived_counts: tuple[int, int] | None) -> dict[str, object]:
    """P1 and P2 for one attempt. `decisive` marks the last attempt (it aborts)."""
    raw_path = run_dir / "attempts" / f"attempt_{index}" / "raw_response.json"
    result: dict[str, object] = {"attempt": index, "decisive": decisive,
                                 "raw_response": rel(raw_path)}
    raw = json.loads(raw_path.read_text(encoding="utf-8"))
    document, parse_error = response_document(raw)

    if parse_error is not None:
        result["P1"] = "FEHL"
        result["P2"] = "FEHL"
        result["reason"] = parse_error
        return result

    foreign = p1_foreign_keys(document)
    result["P1"] = "OK" if not foreign else "FEHL"
    if foreign:
        result["P1_problems"] = foreign

    raw_c, raw_r = raw_counts(document)
    reparsed = parsed_counts_of(document)
    result["raw_counts"] = {"components": raw_c, "relations": raw_r}
    result["reparsed_counts"] = {"components": reparsed[0], "relations": reparsed[1]}

    compare_to = archived_counts if decisive else reparsed
    result["parsed_counts"] = {"components": compare_to[0], "relations": compare_to[1]}
    result["parsed_source"] = "arch_model.json" if decisive else "re-parse"
    p2_ok = (raw_c, raw_r) == compare_to
    result["P2"] = "OK" if p2_ok else "FEHL"
    if not p2_ok:
        result["P2_problems"] = [
            f"components roh {raw_c} vs geparst {compare_to[0]}",
            f"relations roh {raw_r} vs geparst {compare_to[1]}",
        ]
    if decisive and archived_counts is not None and reparsed != archived_counts:
        # Free counter-instance: the archive must equal what re-parsing produces.
        result["archive_vs_reparse"] = "FEHL"
        result["P2"] = "FEHL"
        result.setdefault("P2_problems", []).append(
            f"arch_model.json {archived_counts} != Re-Parse der Rohantwort {reparsed}")
    return result


def check_run(run_dir: Path) -> dict[str, object]:
    """Validity (section 5.2) and the parse assertions (section 5.3) for one run dir.

    Returns a verdict block. Raises InstrumentAbort when `valid_final` is missing.
    """
    meta = json.loads((run_dir / "meta.json").read_text(encoding="utf-8"))
    if "valid_final" not in meta:
        raise InstrumentAbort(
            f"{rel(run_dir)}/meta.json führt KEIN Feld `valid_final`. "
            "Protokoll §5.2: das ist ein ABBRUCH, nicht ein `false` -- der Lauf wird "
            "weder als ungültig gezählt noch als 0 verrechnet.")
    arch = json.loads((run_dir / "arch_model.json").read_text(encoding="utf-8"))
    archived_counts = (len(arch.get("components", [])), len(arch.get("relations", [])))

    attempts_dir = run_dir / "attempts"
    indices = sorted(
        int(p.name.removeprefix("attempt_"))
        for p in attempts_dir.iterdir() if p.name.startswith("attempt_"))
    last = indices[-1]
    attempts = [
        assert_attempt(run_dir, i, decisive=(i == last),
                       archived_counts=archived_counts if i == last else None)
        for i in indices
    ]
    decisive = attempts[-1]
    valid_final = bool(meta["valid_final"])
    ok = valid_final and decisive["P1"] == "OK" and decisive["P2"] == "OK"

    reasons: list[str] = []
    if not valid_final:
        reasons.append("valid_final == false nach allen Versuchen (§5.2)")
    if decisive["P1"] != "OK":
        reasons.append(f"P1 (Fremdschlüssel) im letzten Versuch: "
                       f"{decisive.get('P1_problems') or decisive.get('reason')}")
    if decisive["P2"] != "OK":
        reasons.append(f"P2 (Zählwerte roh vs geparst) im letzten Versuch: "
                       f"{decisive.get('P2_problems') or decisive.get('reason')}")

    return {
        "gueltig": ok,
        "valid_final": meta["valid_final"],
        "valid_raw": meta.get("valid_raw"),
        "attempts_used": meta.get("attempts_used"),
        "P1": decisive["P1"],
        "P2": decisive["P2"],
        "attempts": attempts,
        "gruende": reasons,
        # Counters only -- no metric is computed here (evaluation lock, Z1-A).
        "zaehler": {
            "module_count": meta.get("module_count"),
            "component_count": meta.get("component_count"),
            "prompt_tokens": meta.get("prompt_tokens"),
            "completion_tokens": meta.get("completion_tokens"),
            "latency_ms": meta.get("latency_ms"),
        },
        "provenienz": {
            "timestamp": meta.get("timestamp"),
            "provider": meta.get("provider"),
            "base_url": meta.get("base_url"),
            "model": meta.get("model"),
            "model_version": meta.get("model_version"),
            "temperature": meta.get("temperature"),
            "prompt_version": meta.get("prompt_version"),
            "repo_path": meta.get("repo_path"),
            "repo_commit": meta.get("repo_commit"),
            "run_index": meta.get("run_index"),
        },
    }


# --- journal ----------------------------------------------------------------------------


def journal_path(condition: str) -> Path:
    return ARCHIVE_ROOT / condition / "journal.jsonl"


def journal(condition: str, **entry: object) -> None:
    """Append-only. A journal that can be rewritten is not a record."""
    path = journal_path(condition)
    path.parent.mkdir(parents=True, exist_ok=True)
    entry = {"ts": utcnow(), **entry}
    with path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(entry, ensure_ascii=False, sort_keys=True) + "\n")


# --- invocation -------------------------------------------------------------------------


def child_env(condition: str, root: Path) -> dict[str, str]:
    """Environment for the extractor call -- the key travels here, never in argv."""
    env = dict(os.environ)
    env["PYTHONPATH"] = str(root / "src")
    api_key_env = CONDITIONS[condition]["api_key_env"]
    if api_key_env:
        secrets = load_secrets()
        if api_key_env not in secrets or not secrets[api_key_env]:
            raise Abort(f"{api_key_env} steht nicht in {SECRETS_FILE}.")
        env[str(api_key_env)] = secrets[str(api_key_env)]
    return env


def invoke(condition: str, root: Path, runs: int) -> dict[str, object]:
    """One `llm-arch extract` invocation, streamed and clocked from the outside.

    The console script `llm-arch` maps to `llm_arch.cli:app` (pyproject
    [project.scripts]); it is called here as a module so that nothing has to be
    installed INTO the extractor tree -- the extractor is read-only.

    The external wall clock is measured on the monotonic clock (protocol section
    6.3: never mix an inner and an outer measurement). Per run it is derived from
    the timestamps of the child's own progress lines; that derivation is recorded
    as a derivation, not as a measured value.
    """
    cfg = CONDITIONS[condition]
    argv = [
        sys.executable, "-m", "llm_arch.cli", "extract", FIXTURE,
        "--provider", str(cfg["provider"]), "--model", str(cfg["model"]),
        "--runs", str(runs),
    ]
    before = {p.name for p in (root / "runs").iterdir()} if (root / "runs").exists() else set()

    say(f"  → {' '.join(argv[1:])}   (cwd={root})")
    started_mono = time.monotonic()
    started_utc = utcnow()
    marks: list[tuple[float, str]] = []
    proc = subprocess.Popen(
        argv, cwd=str(root), env=child_env(condition, root),
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)
    assert proc.stdout is not None

    # A reader thread, so "no progress" is a real clock and not a loop that only
    # ticks when a line arrives (K3 stop rule: ten minutes without progress).
    lines: queue.Queue[str | None] = queue.Queue()

    def pump(stream) -> None:
        for raw_line in stream:
            lines.put(raw_line)
        lines.put(None)

    reader = threading.Thread(target=pump, args=(proc.stdout,), daemon=True)
    reader.start()

    stalled = False
    while True:
        try:
            item = lines.get(timeout=STALL_SECONDS)
        except queue.Empty:
            stalled = True
            proc.kill()
            break
        if item is None:
            break
        line = redact(item.rstrip("\n"))
        marks.append((time.monotonic() - started_mono, line))
        say(f"     | {line}")
    proc.wait()
    elapsed = time.monotonic() - started_mono
    finished_utc = utcnow()

    after = {p.name for p in (root / "runs").iterdir()} if (root / "runs").exists() else set()
    new_dirs = sorted(after - before)

    return {
        "argv": argv[1:],           # argv[0] is the interpreter path, not information
        "cwd": str(root),
        "returncode": proc.returncode,
        "stalled": stalled,
        "started_utc": started_utc,
        "finished_utc": finished_utc,
        "external_wall_s_invocation": round(elapsed, 3),
        "output_marks": [{"t_s": round(t, 3), "line": line} for t, line in marks],
        "new_run_dirs": new_dirs,
    }


def per_run_wall_clock(marks: list[dict]) -> dict[str, float]:
    """External seconds per run, derived from the child's own progress lines.

    cli.py prints one "extracted N modules ..." line before the loop and one
    "  run i: ..." line as each run finishes. The window of run 0 therefore starts
    at the "extracted" line (fact extraction and provider setup are outside it),
    every later run starts at its predecessor's line. Derived, not measured --
    the measured value is the whole invocation.
    """
    out: dict[str, float] = {}
    start = None
    for mark in marks:
        line = str(mark["line"])
        if line.startswith("extracted "):
            start = float(mark["t_s"])
        elif line.strip().startswith("run ") and start is not None:
            index = line.strip().split()[1].rstrip(":")
            out[f"run{index}"] = round(float(mark["t_s"]) - start, 3)
            start = float(mark["t_s"])
    return out


# --- archiving (protocol section 6.4, order 2d) -----------------------------------------


def archive_run(source: Path, condition: str, slot: str,
                root: Path | None = None) -> Path:
    """Copy one extractor run directory VERBATIM into data/z1/<cond>/<slot>/extractor/.

    A target path that already exists is a stop, never an overwrite: a run
    artifact that gets replaced is a measurement that was silently lost
    (protocol section 5.4, precedent C4c).
    """
    target = (root / condition / slot) if root else slot_dir(condition, slot)
    if target.exists():
        raise Abort(
            f"Zielpfad existiert bereits: {rel(target)}. "
            "Ein bestehendes Artefakt wird unter KEINEN Umständen ersetzt (§5.4).")
    target.mkdir(parents=True)
    shutil.copytree(source, target / "extractor")
    return target


def write_manifest(target: Path, manifest: dict) -> None:
    (target / "run_manifest.json").write_text(
        redact(json.dumps(manifest, indent=2, ensure_ascii=False, sort_keys=True)) + "\n",
        encoding="utf-8")


def free_slot(condition: str, wanted: int, repeat: int) -> str:
    return f"run{wanted}" if repeat == 0 else f"run{wanted}_w{repeat}"


def valid_slots(condition: str) -> list[str]:
    """Slots whose run_manifest.json records a checked-valid run (resume, order 2c)."""
    base = ARCHIVE_ROOT / condition
    if not base.exists():
        return []
    out = []
    for slot in sorted(p.name for p in base.iterdir() if p.is_dir()):
        manifest = base / slot / "run_manifest.json"
        if not manifest.exists():
            continue
        data = json.loads(manifest.read_text(encoding="utf-8"))
        if data.get("verdikt", {}).get("gueltig") is True:
            out.append(slot)
    return out


# --- the schema smoke against the K3 endpoint (protocol section 3.3 (5)) ----------------


def schema_smoke(condition: str) -> dict[str, object]:
    """One call with the hashed schema against the target endpoint, before K3.

    "Bricht er, ist der Messlauf nicht zu starten." Logged with HTTP status,
    `model` echo, schema hash and pydantic version.
    """
    import pydantic
    from openai import OpenAI

    from llm_arch.abstraction.schema import ArchModel
    from llm_arch.providers.openai_compatible import PROFILES

    cfg = CONDITIONS[condition]
    profile = PROFILES[str(cfg["provider"])]
    api_key_env = cfg["api_key_env"]
    api_key = load_secrets()[str(api_key_env)] if api_key_env else "ollama"
    client = OpenAI(base_url=profile["base_url"], api_key=api_key)
    schema = ArchModel.model_json_schema()

    started = time.monotonic()
    raw = client.chat.completions.with_raw_response.create(
        model=str(cfg["model"]),
        messages=[{"role": "user",
                   "content": "Return an empty architecture: components: []."}],
        temperature=0.0,
        seed=0,
        response_format={"type": "json_schema",
                         "json_schema": {"name": "arch_model", "schema": schema,
                                         "strict": True}},
    )
    elapsed = time.monotonic() - started
    parsed = raw.parse()
    return {
        "http_status": raw.status_code,
        "model_angefordert": str(cfg["model"]),
        "model_echo": parsed.model,
        "echo_zeichengleich": parsed.model == str(cfg["model"]),
        "system_fingerprint": getattr(parsed, "system_fingerprint", None),
        "schema_sha256_archived": SCHEMA_SHA256_ARCHIVED,
        "pydantic": pydantic.VERSION,
        "external_wall_s": round(elapsed, 3),
    }


# --- driving one condition --------------------------------------------------------------


def run_condition(condition: str, root: Path) -> int:
    """Preconditions, invocation(s), assertions, archive, journal. Returns exit code."""
    cfg = CONDITIONS[condition]
    say(f"=== Bedingung {condition.upper()} · {cfg['model']} · Profil {cfg['provider']}")

    done = valid_slots(condition)
    if len(done) >= RUNS_PER_CONDITION:
        say(f"  Bedingung {condition.upper()} ist bereits mit "
            f"{len(done)} gültigen Läufen erhoben -- übersprungen (Wiederaufnahme).")
        return 0

    pre = preconditions(root, condition)
    say(f"  Vorbedingungen OK · HEAD {pre['extractor_head'][:7]} · "
        f"Blobs {pre['input_blobs']['geprueft']} · "  # type: ignore[index]
        f"Schema {SCHEMA_SHA256_ARCHIVED[:8]}… · "
        f"python {pre['environment']['python']} "     # type: ignore[index]
        f"pydantic {pre['environment']['pydantic']} " # type: ignore[index]
        f"openai {pre['environment']['openai']}")     # type: ignore[index]
    journal(condition, event="preconditions_ok", detail=pre)

    smoke = None
    if condition == "k3":
        say("  Schema-Smoke gegen den Zielendpunkt (Protokoll §3.3 (5)) …")
        try:
            smoke = schema_smoke(condition)
        except Exception as exc:                       # noqa: BLE001 -- reported, not swallowed
            raise Abort(f"Schema-Smoke gescheitert: {redact(str(exc))}") from exc
        say(f"    HTTP {smoke['http_status']} · model-Echo {smoke['model_echo']!r} · "
            f"zeichengleich {smoke['echo_zeichengleich']}")
        journal(condition, event="schema_smoke", detail=smoke)

    filled: dict[int, str] = {}
    for slot in valid_slots(condition):
        filled[int(slot.removeprefix("run").split("_")[0])] = slot

    invocations = 0
    repeats = 0
    consecutive_transport_failures = 0
    while len(filled) < RUNS_PER_CONDITION:
        missing = [i for i in range(RUNS_PER_CONDITION) if i not in filled]
        # One invocation per CONDITION with --runs 3 (protocol section 6.2: cli.py:47
        # counts run_index up over the loop, so the three runs carry 0, 1, 2 and are
        # distinguishable -- three single calls would all carry run_index 0, exactly
        # the ambiguity Befund 04 later failed on). Repetitions per section 5.4 run as
        # a single invocation with --runs 1 and are journalled as repetitions.
        first_pass = invocations == 0
        runs = RUNS_PER_CONDITION if first_pass else 1
        if not first_pass:
            repeats += 1
            if repeats > MAX_REPEATS:
                journal(condition, event="condition_not_collected",
                        reason=f"mehr als {MAX_REPEATS} Wiederholungen",
                        filled=sorted(filled.values()))
                say(f"  Bedingung {condition.upper()}: NICHT ERHOBEN -- "
                    f"{MAX_REPEATS} Wiederholungen erschöpft, "
                    f"{len(filled)} von {RUNS_PER_CONDITION} Läufen gültig. "
                    "Kein Nullwert, keine leere Zeile (§5.4).")
                return 2
            say(f"  Wiederholung {repeats}/{MAX_REPEATS} für Slot run{missing[0]}")
            # A repeat re-checks the preconditions: the tree may have moved in between.
            pre = preconditions(root, condition)

        invocations += 1
        result = invoke(condition, root, runs)
        result["external_wall_s_per_run"] = per_run_wall_clock(result["output_marks"])  # type: ignore[arg-type]
        journal(condition, event="invocation", detail={
            k: v for k, v in result.items() if k != "output_marks"})

        new_dirs = list(result["new_run_dirs"])  # type: ignore[arg-type]
        if result["returncode"] != 0 or result["stalled"] or not new_dirs:
            consecutive_transport_failures += 1
            say(f"  Invocation ohne verwertbares Ergebnis "
                f"(returncode={result['returncode']}, stalled={result['stalled']}, "
                f"neue Laufverzeichnisse={len(new_dirs)}) -- "
                f"Transportfehler {consecutive_transport_failures} in Folge.")
            journal(condition, event="transport_failure",
                    consecutive=consecutive_transport_failures,
                    returncode=result["returncode"], stalled=result["stalled"])
            if (consecutive_transport_failures >= MAX_CONSECUTIVE_TRANSPORT_FAILURES
                    or result["stalled"]):
                say(f"  ANHALTEN: {consecutive_transport_failures} Transportfehler in "
                    f"Folge bzw. {STALL_SECONDS}s ohne Fortschritt. "
                    "Zustand berichtet, nicht weiterprobiert.")
                return 3
            continue
        consecutive_transport_failures = 0

        for name in new_dirs:
            source = root / "runs" / name
            meta = json.loads((source / "meta.json").read_text(encoding="utf-8"))
            wanted = int(meta.get("run_index", 0)) if first_pass else missing[0]
            if wanted in filled:
                wanted = [i for i in range(RUNS_PER_CONDITION) if i not in filled][0]
            repeat_index = 0 if first_pass else repeats
            slot = free_slot(condition, wanted, repeat_index)
            while slot_dir(condition, slot).exists():
                repeat_index += 1
                slot = free_slot(condition, wanted, repeat_index)

            target = archive_run(source, condition, slot)
            verdict = check_run(target / "extractor")
            manifest = {
                "schema": "z1-run-manifest/1",
                "bedingung": condition.upper(),
                "slot": slot,
                "modell": cfg["model"],
                "profil": cfg["provider"],
                "base_url_profil": cfg["base_url"],
                "extractor_run_dir": name,
                "vorbedingungen": pre,
                "schema_smoke": smoke,
                "invocation": {k: v for k, v in result.items() if k != "output_marks"},
                "externe_wanduhrzeit_s": {
                    "invocation_gemessen": result["external_wall_s_invocation"],
                    "lauf_abgeleitet": result["external_wall_s_per_run"].get(  # type: ignore[union-attr]
                        f"run{meta.get('run_index', 0)}"),
                    "hinweis": ("Invocation gemessen (monotone Uhr, §6.3); der Laufwert "
                                "ist aus den Fortschrittszeilen des Kindprozesses "
                                "abgeleitet. latency_ms in meta.json ist der Innenwert."),
                },
                "umgebungsparameter": {
                    "seed": 0,
                    "hinweis": ("seed steht NICHT im Laufrecord (29 Felder ohne ihn, "
                                "§3.3 (1)); gesendet, aber nicht als wirksam angenommen."),
                },
                "verdikt": verdict,
            }
            write_manifest(target, manifest)

            if verdict["gueltig"]:
                filled[wanted] = slot
                journal(condition, event="run_recorded", slot=slot,
                        pfad=rel(target), verdikt="gültig",
                        zaehler=verdict["zaehler"])
                say(f"    {slot}: GÜLTIG · valid_final={verdict['valid_final']} · "
                    f"P1={verdict['P1']} P2={verdict['P2']} · "
                    f"module_count={verdict['zaehler']['module_count']} "  # type: ignore[index]
                    f"component_count={verdict['zaehler']['component_count']}")  # type: ignore[index]
            else:
                journal(condition, event="run_rejected", slot=slot,
                        pfad=rel(target), gruende=verdict["gruende"])
                say(f"    {slot}: UNGÜLTIG -- {'; '.join(verdict['gruende'])}")  # type: ignore[arg-type]
                say("      Befund über den Lauf, kein Fehler des Skripts. Rohantwort "
                    "archiviert, Lauf journalisiert, Wiederholung nach §5.4.")

    journal(condition, event="condition_done", slots=sorted(filled.values()))
    say(f"  Bedingung {condition.upper()}: {len(filled)} von {RUNS_PER_CONDITION} "
        f"Läufen gültig -- {', '.join(sorted(filled.values()))}")
    return 0


# --- finalize: SHA256SUMS for one condition ---------------------------------------------


def finalize(condition: str) -> int:
    """Write data/z1/<cond>/SHA256SUMS over everything in that condition block."""
    base = ARCHIVE_ROOT / condition
    if not base.exists():
        raise Abort(f"{rel(base)} existiert nicht.")
    lines = []
    for path in sorted(p for p in base.rglob("*") if p.is_file()):
        if path.name == "SHA256SUMS":
            continue
        lines.append(f"{sha256_file(path)}  {path.relative_to(base)}")
    (base / "SHA256SUMS").write_text("\n".join(lines) + "\n", encoding="utf-8")
    say(f"{rel(base / 'SHA256SUMS')}: {len(lines)} Dateien gehasht")
    proc = subprocess.run(["sha256sum", "-c", "SHA256SUMS"], cwd=str(base),
                          capture_output=True, text=True)
    say(f"sha256sum -c: Exit {proc.returncode}, "
        f"{len([l for l in proc.stdout.splitlines() if l.endswith(': OK')])} OK")
    return proc.returncode


# --- self-test (order 2e) ---------------------------------------------------------------


def _probe(name: str, fn) -> bool:
    """Run one negative probe; it passes when the pre-registered stop fires.

    Two shapes of stop count: an `Abort` raised (precondition and instrument
    class), and a verdict that marks the run invalid with named reasons (run
    finding class -- P1/P2 do not raise, they refuse the run).
    """
    say(f"--- NEGATIVPROBE: {name}")
    try:
        verdict = fn()
    except Abort as exc:
        for line in redact(str(exc)).splitlines():
            say(f"    {line}")
        say("    → ABBRUCH ausgelöst — Probe BESTANDEN")
        return True
    if isinstance(verdict, dict) and verdict.get("gueltig") is False:
        say(f"    P1={verdict['P1']} · P2={verdict['P2']} · "
            f"valid_final={verdict['valid_final']}")
        for reason in verdict["gruende"]:
            say(f"    {reason}")
        say("    → Lauf als UNGÜLTIG zurückgewiesen — Probe BESTANDEN")
        return True
    say("    → KEIN Abbruch — Probe FEHLGESCHLAGEN")
    return False


def selftest(root: Path, scratch: Path) -> int:
    """The six negative probes plus --plan and the invariants checker. No model call."""
    fixtures = REPO / "tests" / "fixtures" / "z1"
    scratch.mkdir(parents=True, exist_ok=True)
    ok = True

    say("=== --plan")
    print_plan()
    say("")

    say("=== Positivprobe: Vorbedingungen gegen den unveränderten Extractor")
    pre = preconditions(root, None)
    say(f"    porcelain leer · HEAD {pre['extractor_head']}")
    say(f"    Messeingänge: {pre['input_blobs']['geprueft']}")   # type: ignore[index]
    say(f"    prompt {pre['prompt']['blob_sha1']} PROMPT_VERSION="  # type: ignore[index]
        f"{pre['prompt']['PROMPT_VERSION']}")                    # type: ignore[index]
    say(f"    Schema archiviert {pre['arch_model_schema']['archived_sha256']}")  # type: ignore[index]
    say(f"    Umgebung {pre['environment']}")
    say(f"    Thesis-Repo {pre['thesis_repo']}")
    say("")

    # (1) P1 fires -- a fixture with a foreign key.
    ok &= _probe("P1 spricht an (Fixture mit Fremdschlüssel `dependencies`)",
                 lambda: check_run(fixtures / "p1_fremdschluessel"))

    # (2) P2 fires -- a fixture in which a relation is lost on parse.
    ok &= _probe("P2 spricht an (Fixture, in der eine Relation beim Parsen verloren geht)",
                 lambda: check_run(fixtures / "p2_verlorene_relation"))

    # (3) A missing `valid_final` aborts -- it is not read as `false`.
    ok &= _probe("fehlendes `valid_final` bricht ab (nicht `false`)",
                 lambda: check_run(fixtures / "fehlendes_valid_final"))

    # (4) A dirty extractor tree aborts -- BEFORE a call can exist.
    def probe_dirty() -> None:
        clone = scratch / "dirty_clone"
        if not clone.exists():
            subprocess.run(["git", "clone", "--quiet", "--no-hardlinks",
                            str(root), str(clone)], check=True,
                           capture_output=True)
        (clone / "src" / "llm_arch" / "eval" / "metrics.py").write_text(
            (clone / "src" / "llm_arch" / "eval" / "metrics.py").read_text() + "\n# dirt\n")
        preconditions(clone, None)
    ok &= _probe("dirty Extractor-Baum bricht ab (Klon im Scratchpad, "
                 "der Extractor selbst bleibt unberührt)", probe_dirty)

    # (5) A deviating blob hash aborts -- falsified expectation against the clean tree.
    def probe_blob() -> None:
        tampered = dict(REGISTERED_BLOBS)
        sha1, sha256 = tampered["src/llm_arch/eval/metrics.py"]
        tampered["src/llm_arch/eval/metrics.py"] = (sha1[:-1] + "0", sha256)
        check_input_blobs(root, tampered)
    ok &= _probe("abweichender Blob-Hash bricht ab (verfälschte Erwartung gegen den "
                 "unveränderten Extractor)", probe_blob)

    # (6) A target path collision aborts -- an artifact is never replaced.
    def probe_collision() -> None:
        # Runs against a scratch archive root: the self-test never writes into data/.
        root_dir = scratch / "kollision"
        target = root_dir / "k2" / "run0"
        target.mkdir(parents=True, exist_ok=True)
        archive_run(fixtures / "p1_fremdschluessel", "k2", "run0", root=root_dir)
    ok &= _probe("Zielpfadkollision bricht ab", probe_collision)

    say("")
    say(f"=== SELBSTTEST {'BESTANDEN' if ok else 'FEHLGESCHLAGEN'}")
    return 0 if ok else 1


# --- CLI --------------------------------------------------------------------------------


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--plan", action="store_true",
                        help="die sechs Läufe mit Bedingung, Profil, Modell, Zielpfaden")
    parser.add_argument("--selftest", action="store_true",
                        help="die Negativproben, ohne Modell-Call")
    parser.add_argument("--condition", choices=sorted(CONDITIONS),
                        help="eine Bedingung erheben")
    parser.add_argument("--finalize", choices=sorted(CONDITIONS),
                        help="SHA256SUMS für einen Bedingungsblock schreiben")
    parser.add_argument("--extractor", default=str(EXTRACTOR),
                        help="Wurzel des Extractor-Klons (nur lesend und ausführend)")
    parser.add_argument("--scratch", default=os.environ.get("Z1_SCRATCH", "/tmp/z1"),
                        help="Arbeitsverzeichnis für die Negativproben")
    args = parser.parse_args()

    root = Path(args.extractor).expanduser().resolve()
    try:
        if args.plan:
            print_plan()
            return 0
        if args.selftest:
            return selftest(root, Path(args.scratch))
        if args.finalize:
            return finalize(args.finalize)
        if args.condition:
            return run_condition(args.condition, root)
    except InstrumentAbort as exc:
        say("")
        say("HARTER ABBRUCH (Instrument):")
        for line in redact(str(exc)).splitlines():
            say(f"  {line}")
        return 4
    except Abort as exc:
        say("")
        say("ABBRUCH:")
        for line in redact(str(exc)).splitlines():
            say(f"  {line}")
        return 1
    parser.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
