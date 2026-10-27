"""Live smoke test against a local Ollama server.

Skips automatically when no Ollama is reachable (e.g. the dev laptop), so
it only runs where it can actually verify structured output -- the GPU box.
"""

import json
import urllib.error
import urllib.request

import pytest

from llm_arch.providers import make_provider

MODEL = "qwen2.5-coder:3b"  # small model is enough to verify the plumbing


def _ollama_up() -> bool:
    try:
        urllib.request.urlopen("http://localhost:11434/api/tags", timeout=2)
        return True
    except (urllib.error.URLError, OSError):
        return False


@pytest.mark.skipif(not _ollama_up(), reason="no local Ollama server")
def test_structured_output_against_mini_schema():
    schema = {
        "type": "object",
        "properties": {"answer": {"type": "integer"}},
        "required": ["answer"],
        "additionalProperties": False,
    }
    provider = make_provider("ollama", MODEL)
    result = provider.generate(
        messages=[{"role": "user", "content": "Reply with JSON: answer = 2 + 2."}],
        json_schema=schema,
    )
    parsed = json.loads(result.text)
    assert parsed["answer"] == 4
    assert result.usage.prompt_tokens > 0
    assert result.latency_ms > 0
