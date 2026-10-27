import json

from llm_arch.abstraction.abstractor import AbstractionRun, Attempt
from llm_arch.abstraction.schema import ArchModel, Component, Relation
from llm_arch.facts import extract_repo
from llm_arch.ilograph import validate_arch
from llm_arch.logging import log_run
from llm_arch.providers.base import GenerationResult, Usage

FIXTURE = "fixtures/sample_repo"


def _result(call: int) -> GenerationResult:
    return GenerationResult(
        text="{}",
        model="qwen2.5-coder:7b",
        usage=Usage(prompt_tokens=100, completion_tokens=20),
        latency_ms=1234.5,
        raw_response={"call": call},
    )


def _run(facts) -> AbstractionRun:
    """A two-attempt run: invalid first, valid second (covers per-attempt logs)."""
    required = {f.module_name for f in facts if f.classes or f.functions or f.imports}
    known = {f.module_name for f in facts}

    bad = ArchModel(components=[Component(id="d", name="D",
                                          contained_modules=["shop.domain.order"])])
    good = ArchModel(
        components=[
            Component(id="d", name="D", contained_modules=["shop.domain.order"]),
            Component(id="i", name="I",
                      contained_modules=["shop.infrastructure.repository"]),
            Component(id="a", name="A", contained_modules=["shop.api.routes"]),
        ],
        relations=[Relation(from_="a", to="d")],
    )
    attempts = [
        Attempt([{"role": "user", "content": "facts shop.domain.order"}], _result(1),
                bad, validate_arch(bad, required_modules=required, known_modules=known)),
        Attempt([{"role": "user", "content": "fix it"}], _result(2),
                good, validate_arch(good, required_modules=required, known_modules=known)),
    ]
    return AbstractionRun(arch=good, prompt_version="v2", attempts=attempts)


def test_log_run_writes_artifacts_and_metrics(tmp_path):
    facts = extract_repo(FIXTURE)
    out = log_run(
        facts=facts,
        run=_run(facts),
        ilograph_yaml="resources: []\n",
        repo_path=FIXTURE,
        provider="ollama",
        model="qwen2.5-coder:7b",
        temperature=0.0,
        run_index=2,
        gold={"shop.domain.order": "d", "shop.api.routes": "a",
              "shop.infrastructure.repository": "i"},
        runs_dir=tmp_path,
    )

    for name in ("input_facts.json", "arch_model.json", "output.ilograph.yaml",
                 "meta.json"):
        assert (out / name).exists(), name
    # every attempt logged
    for i in (0, 1):
        adir = out / "attempts" / f"attempt_{i}"
        assert (adir / "prompt.txt").exists()
        assert (adir / "raw_response.json").exists()
        assert (adir / "validation.json").exists()

    meta = json.loads((out / "meta.json").read_text())
    assert meta["run_index"] == 2
    assert meta["valid_raw"] is False  # first attempt dropped modules
    assert meta["valid_final"] is True
    assert meta["attempts_used"] == 2
    assert meta["module_coverage"] == 1.0
    assert meta["phantom_modules"] == 0
    assert meta["gold_similarity"] == 1.0  # gold matches the final partition
    assert meta["prompt_version"] == "v2"
    # latency/tokens come from the final attempt
    assert meta["completion_tokens"] == 20
