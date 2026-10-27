"""Provider interface and result type.

The interface is the OpenAI-compatible shape, so a single adapter serves
Ollama, OpenRouter and Gemini -- only base_url/model/api_key differ.
"""

from dataclasses import dataclass
from typing import Any, Protocol


@dataclass
class Usage:
    """Token accounting for one generation (for logging/measurement)."""

    prompt_tokens: int
    completion_tokens: int


@dataclass
class GenerationResult:
    """Everything one generation call produced, for parsing and logging."""

    text: str
    model: str
    usage: Usage
    latency_ms: float
    raw_response: dict[str, Any]


class LLMProvider(Protocol):
    """Anything that turns chat messages + a JSON schema into structured text."""

    def generate(
        self, messages: list[dict[str, str]], json_schema: dict[str, Any]
    ) -> GenerationResult: ...
