"""Persist one fully reproducible run to runs/<timestamp>_r<index>/ (§4.6, §2.6).

Every artifact needed to reproduce or audit a run is written: the input facts,
every attempt's prompt + raw response + validation, the final parsed model, the
Ilograph YAML and a meta record (model, tokens, latency, raw/final validity,
retry count, fact-fidelity metrics and optional gold similarity).
"""

import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

from llm_arch.abstraction.abstractor import AbstractionRun
from llm_arch.eval import (
    compression,
    fact_fidelity,
    gold_similarity,
    reduce_arch,
)
from llm_arch.facts import substantive_modules
from llm_arch.facts.models import ModuleFacts


def _git_commit(repo_path: str | Path) -> str | None:
    """Return the HEAD commit of repo_path, or None if it's not a git repo."""
    try:
        out = subprocess.run(
            ["git", "-C", str(repo_path), "rev-parse", "HEAD"],
            capture_output=True,
            text=True,
            check=True,
        )
        return out.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None


def _render_prompt(messages: list[dict[str, str]]) -> str:
    return "\n\n".join(f"### {m['role']}\n{m['content']}" for m in messages)


def log_run(
    *,
    facts: list[ModuleFacts],
    run: AbstractionRun,
    ilograph_yaml: str,
    repo_path: str | Path,
    provider: str,
    model: str,
    temperature: float,
    base_url: str | None = None,
    run_index: int,
    gold: dict[str, str] | None = None,
    runs_dir: str | Path = "runs",
) -> Path:
    """Write one run's artifacts (incl. every attempt) and return its directory."""
    now = datetime.now(timezone.utc)
    out = Path(runs_dir) / f"{now.strftime('%Y%m%dT%H%M%S')}_r{run_index}"
    out.mkdir(parents=True, exist_ok=True)

    (out / "input_facts.json").write_text(
        json.dumps([f.model_dump() for f in facts], indent=2)
    )
    (out / "arch_model.json").write_text(
        json.dumps(run.arch.model_dump(by_alias=True), indent=2)
    )
    (out / "output.ilograph.yaml").write_text(ilograph_yaml)

    # Every attempt fully logged: prompt, raw response, validation errors.
    for i, attempt in enumerate(run.attempts):
        adir = out / "attempts" / f"attempt_{i}"
        adir.mkdir(parents=True, exist_ok=True)
        (adir / "prompt.txt").write_text(_render_prompt(attempt.messages))
        (adir / "raw_response.json").write_text(
            json.dumps(attempt.result.raw_response, indent=2)
        )
        (adir / "validation.json").write_text(
            json.dumps(
                {
                    "valid": attempt.validation.valid,
                    "errors": attempt.validation.errors,
                },
                indent=2,
            )
        )

    required = substantive_modules(facts)
    reduced = reduce_arch(run.arch)
    ff = fact_fidelity(facts, reduced, required)
    comp = compression(facts, reduced, required)
    final_result = run.attempts[-1].result

    meta = {
        "timestamp": now.isoformat(),
        "provider": provider,
        "base_url": base_url,  # the endpoint actually called, not derived from `provider`
        "model": model,
        "model_version": final_result.model,  # model id the API actually served
        "temperature": temperature,
        "prompt_version": run.prompt_version,
        "repo_path": str(repo_path),
        "repo_commit": _git_commit(repo_path),
        "run_index": run_index,
        "prompt_tokens": final_result.usage.prompt_tokens,
        "completion_tokens": final_result.usage.completion_tokens,
        "latency_ms": final_result.latency_ms,
        "valid_raw": run.valid_raw,
        "valid_final": run.valid_final,
        "attempts_used": run.attempts_used,
        "validation_errors": run.attempts[-1].validation.errors,
        "relation_precision": ff.relation_precision,
        "relation_recall": ff.relation_recall,
        "module_coverage": ff.module_coverage,
        "phantom_modules": ff.phantom_modules,
        "module_count": comp.module_count,
        "component_count": comp.component_count,
        "module_compression": comp.module_compression,
        "import_edge_count": comp.import_edge_count,
        "component_relation_count": comp.component_relation_count,
        "relation_compression": comp.relation_compression,
        "gold_similarity": (
            gold_similarity(reduced.module_to_component, gold) if gold else None
        ),
        "gold_similarity_method": "adjusted_rand_index" if gold else None,
    }
    (out / "meta.json").write_text(json.dumps(meta, indent=2))
    return out
