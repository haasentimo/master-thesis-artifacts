"""`llm-arch extract <repo>`: facts -> abstract (+retry) -> serialize -> log."""

import json
from pathlib import Path

import typer

from llm_arch.abstraction import abstract
from llm_arch.facts import extract_repo
from llm_arch.ilograph import to_yaml
from llm_arch.logging import log_run
from llm_arch.providers import make_provider

app = typer.Typer(add_completion=False)


@app.callback()
def _main() -> None:
    """LLM-based architecture extraction (Approach 2)."""


def _load_gold(repo_path: str) -> dict[str, str] | None:
    """Load a sibling `<repo>.gold.json` module->label map if present."""
    gold_path = Path(str(repo_path).rstrip("/") + ".gold.json")
    if gold_path.exists():
        return json.loads(gold_path.read_text())
    return None


@app.command()
def extract(
    repo_path: str,
    model: str = typer.Option("qwen2.5-coder:7b", help="Model name."),
    provider: str = typer.Option("ollama", help="Provider profile (see PROFILES)."),
    runs: int = typer.Option(1, help="Number of runs over the same input."),
    max_retries: int = typer.Option(2, help="Validation-driven retries per run."),
) -> None:
    """Extract an abstracted Ilograph architecture from a Python repo."""
    facts = extract_repo(repo_path)
    gold = _load_gold(repo_path)
    typer.echo(
        f"extracted {len(facts)} modules from {repo_path}"
        f"{' (gold present)' if gold else ''}"
    )
    prov = make_provider(provider, model)

    for i in range(runs):
        run = abstract(facts, prov, max_retries=max_retries)
        ilograph_yaml = to_yaml(run.arch)
        out = log_run(
            facts=facts,
            run=run,
            ilograph_yaml=ilograph_yaml,
            repo_path=repo_path,
            provider=provider,
            model=model,
            temperature=prov.temperature,
            base_url=str(prov.client.base_url),
            run_index=i,
            gold=gold,
        )
        meta = json.loads((out / "meta.json").read_text())
        mc = meta["module_compression"]
        mod_comp = f"{mc:.2f}" if mc is not None else "n/a"
        typer.echo(
            f"  run {i}: {out.name}  "
            f"valid_raw={meta['valid_raw']} valid_final={meta['valid_final']} "
            f"attempts={meta['attempts_used']} "
            f"prec={meta['relation_precision']:.2f} rec={meta['relation_recall']:.2f} "
            f"cov={meta['module_coverage']:.2f} phantom={meta['phantom_modules']} "
            f"mod/comp={mod_comp}"
        )


if __name__ == "__main__":
    app()
