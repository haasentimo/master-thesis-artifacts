"""One adapter for every OpenAI-compatible endpoint.

Switching model/provider is a config entry in PROFILES plus `--model`, not
a code change (acceptance criterion §7). Structured output is requested via
`response_format` with the JSON schema. temperature=0 and a fixed seed keep
runs reproducible (§6).
"""

import os
import time
from typing import Any

from openai import OpenAI

from llm_arch.providers.base import GenerationResult, Usage

# A new provider = a new entry here. `api_key_env` is read from the
# environment; Ollama ignores the key, so a literal placeholder is fine.
PROFILES: dict[str, dict[str, str]] = {
    "ollama": {"base_url": "http://localhost:11434/v1", "api_key": "ollama"},
    "openrouter": {"base_url": "https://openrouter.ai/api/v1",
                   "api_key_env": "OPENROUTER_API_KEY"},
    "digitalocean": {"base_url": "https://inference.do-ai.run/v1",
                     "api_key_env": "DO_MODEL_ACCESS_KEY"},
}


class OpenAICompatibleProvider:
    """Generic provider over the `openai` client with a configurable base_url."""

    def __init__(
        self,
        base_url: str,
        model: str,
        api_key: str = "ollama",
        temperature: float = 0.0,
        seed: int = 0,
    ) -> None:
        self.client = OpenAI(base_url=base_url, api_key=api_key)
        self.model = model
        self.temperature = temperature
        self.seed = seed

    def generate(
        self, messages: list[dict[str, str]], json_schema: dict[str, Any]
    ) -> GenerationResult:
        t0 = time.perf_counter()
        resp = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=self.temperature,
            seed=self.seed,
            response_format={
                "type": "json_schema",
                "json_schema": {
                    "name": "arch_model",
                    "schema": json_schema,
                    "strict": True,
                },
            },
        )
        latency_ms = (time.perf_counter() - t0) * 1000
        usage = resp.usage
        return GenerationResult(
            text=resp.choices[0].message.content or "",
            model=resp.model,
            usage=Usage(
                prompt_tokens=getattr(usage, "prompt_tokens", 0),
                completion_tokens=getattr(usage, "completion_tokens", 0),
            ),
            latency_ms=latency_ms,
            raw_response=resp.model_dump(),
        )


def make_provider(profile: str, model: str, **overrides: Any) -> OpenAICompatibleProvider:
    """Build a provider from a named PROFILES entry plus a model name."""
    if profile not in PROFILES:
        raise KeyError(f"unknown provider profile {profile!r}; have {list(PROFILES)}")
    cfg = dict(PROFILES[profile])
    api_key = cfg.pop("api_key", None)
    if "api_key_env" in cfg:
        api_key = os.environ.get(cfg.pop("api_key_env"), "")
    return OpenAICompatibleProvider(model=model, api_key=api_key, **cfg, **overrides)
