"""Offline tests of the abstraction step + retry loop with stubbed providers."""

from llm_arch.abstraction import abstract
from llm_arch.facts import extract_repo
from llm_arch.providers.base import GenerationResult, Usage

FIXTURE = "fixtures/sample_repo"

# Valid for sample_repo: places all three substantive modules disjointly.
VALID = """{
  "components": [
    {"id": "domain", "name": "Domain", "kind": "layer",
     "contained_modules": ["shop.domain.order"]},
    {"id": "infra", "name": "Infra", "kind": "layer",
     "contained_modules": ["shop.infrastructure.repository"]},
    {"id": "api", "name": "Api", "kind": "layer",
     "contained_modules": ["shop.api.routes"]}
  ],
  "relations": []
}"""

# Invalid: drops two required modules (completeness failure).
INVALID = """{
  "components": [
    {"id": "domain", "name": "Domain", "contained_modules": ["shop.domain.order"]}
  ],
  "relations": []
}"""


class SequenceProvider:
    """Returns canned responses in order; records schemas it was handed."""

    def __init__(self, texts: list[str]) -> None:
        self.texts = texts
        self.calls = 0
        self.seen_schema: dict | None = None

    def generate(self, messages, json_schema):
        self.seen_schema = json_schema
        text = self.texts[min(self.calls, len(self.texts) - 1)]
        self.calls += 1
        return GenerationResult(
            text=text,
            model="stub",
            usage=Usage(prompt_tokens=10, completion_tokens=5),
            latency_ms=1.0,
            raw_response={"call": self.calls},
        )


def test_valid_first_attempt_no_retry():
    facts = extract_repo(FIXTURE)
    prov = SequenceProvider([VALID])
    run = abstract(facts, prov, max_retries=2)

    assert run.attempts_used == 1
    assert run.valid_raw and run.valid_final
    assert prov.calls == 1
    assert run.prompt_version == "v3"
    assert "properties" in prov.seen_schema
    # facts rendered into the first prompt
    assert "shop.domain.order" in run.attempts[0].messages[-1]["content"]


def test_retry_recovers_after_invalid_attempt():
    facts = extract_repo(FIXTURE)
    prov = SequenceProvider([INVALID, VALID])
    run = abstract(facts, prov, max_retries=2)

    assert run.attempts_used == 2
    assert run.valid_raw is False  # first attempt invalid
    assert run.valid_final is True  # second attempt fixed it
    # the retry prompt carried the validation errors back as feedback
    feedback = run.attempts[1].messages[-1]["content"]
    assert "INVALID" in feedback and "completeness" in feedback


def test_retries_exhausted_stays_invalid():
    facts = extract_repo(FIXTURE)
    prov = SequenceProvider([INVALID])  # always invalid
    run = abstract(facts, prov, max_retries=2)

    assert run.attempts_used == 3  # 1 + 2 retries
    assert run.valid_raw is False and run.valid_final is False


# Endpoint ignores strict JSON schema and emits a stray control char.
MALFORMED = '{"components": [ broken'


def test_unparseable_json_is_invalid_attempt_then_recovers():
    facts = extract_repo(FIXTURE)
    prov = SequenceProvider([MALFORMED, VALID])
    run = abstract(facts, prov, max_retries=2)

    assert run.attempts_used == 2
    assert run.valid_raw is False  # parse failure counts as invalid, not a crash
    assert run.valid_final is True
    assert "not valid JSON" in run.attempts[0].validation.errors[0]
