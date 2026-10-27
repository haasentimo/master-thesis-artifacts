"""The abstraction step: facts -> prompt -> structured ArchModel, with retry.

On an invalid attempt the concrete validation errors are fed back to the model
and it regenerates, up to `max_retries` times. The raw (first-attempt) and
final validity are both kept for measurement -- invalid outputs are never
silently discarded.
"""

from dataclasses import dataclass

from pydantic import ValidationError

from llm_arch.abstraction.prompt import (
    PROMPT_VERSION,
    build_messages,
    build_retry_feedback,
)
from llm_arch.abstraction.schema import ArchModel
from llm_arch.facts import substantive_modules
from llm_arch.facts.models import ModuleFacts
from llm_arch.ilograph import ValidationResult, validate_arch
from llm_arch.providers.base import GenerationResult, LLMProvider


@dataclass
class Attempt:
    """One generate+validate cycle."""

    messages: list[dict[str, str]]
    result: GenerationResult
    arch: ArchModel
    validation: ValidationResult


@dataclass
class AbstractionRun:
    """A full abstraction with its retry history (everything the logger needs)."""

    arch: ArchModel  # the final attempt's model
    prompt_version: str
    attempts: list[Attempt]

    @property
    def valid_raw(self) -> bool:
        """Validity of the very first attempt (before any repair)."""
        return self.attempts[0].validation.valid

    @property
    def valid_final(self) -> bool:
        """Validity of the last attempt."""
        return self.attempts[-1].validation.valid

    @property
    def attempts_used(self) -> int:
        return len(self.attempts)


def abstract(
    facts: list[ModuleFacts],
    provider: LLMProvider,
    max_retries: int = 2,
) -> AbstractionRun:
    """Run abstraction with validation-driven retry; return the full history."""
    required = substantive_modules(facts)
    known = {f.module_name for f in facts}
    schema = ArchModel.model_json_schema()

    messages = build_messages(facts)
    attempts: list[Attempt] = []

    for _ in range(max_retries + 1):
        result = provider.generate(messages, schema)
        try:
            arch = ArchModel.model_validate_json(result.text)
            validation = validate_arch(
                arch, required_modules=required, known_modules=known
            )
        except ValidationError as e:
            # Endpoint didn't honour the strict JSON schema (unparseable output).
            # Treat it as an invalid attempt so the retry loop can repair it,
            # rather than crashing the whole run (docstring: never silently drop).
            arch = ArchModel(components=[])
            validation = ValidationResult(
                valid=False, errors=[f"output was not valid JSON for the schema: {e}"]
            )
        attempts.append(Attempt(messages, result, arch, validation))
        if validation.valid:
            break
        messages = messages + [
            {"role": "assistant", "content": result.text},
            {"role": "user", "content": build_retry_feedback(validation.errors)},
        ]

    return AbstractionRun(
        arch=attempts[-1].arch,
        prompt_version=PROMPT_VERSION,
        attempts=attempts,
    )
