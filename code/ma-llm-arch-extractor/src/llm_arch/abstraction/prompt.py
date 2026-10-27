"""Versioned prompt templates. Bump PROMPT_VERSION on any change (logged §4.6).

Prompt history (older versions are in git):
- v1: zero-shot abstraction instructions only.
- v2: + Ilograph format idiom rules (disjoint containment, shared infra as a
      sibling component via relation). Format rules only -- no preferred
      decomposition axis (layers vs services stays the model's choice).
- v3: + mandatory, import-derived component relations (Befund 03: stronger
      model omitted all relations -> recall 0.0; the gap is the prompt, not
      capacity). Still no preferred decomposition axis.
"""

import json

from llm_arch.facts.models import ModuleFacts

PROMPT_VERSION = "v3"

SYSTEM = """You are a senior software architect. From raw code facts (modules, \
imports, class/function signatures, docstrings) you derive an ABSTRACTED target \
architecture.

Your job is to ABSTRACT, not to transcribe:
- Group modules into a SMALL number of meaningful components -- NOT one \
component per module. Repeating the module list 1:1 is a failure, not a result.
- Infer each component's role from names and docstrings.
- Summarize dependencies at the component level, not per module.
- Think in abstraction levels (components and their relations).
- Choose whatever decomposition the facts suggest; do not default to any \
particular axis.

Ilograph format rules (follow exactly -- these are FORMAT rules, not a preferred \
architecture):
- Every module belongs to EXACTLY ONE component (disjoint containment). Never \
place the same module in two components.
- Model shared or cross-cutting infrastructure (e.g. a database used by several \
components) as its OWN separate sibling component that the others point to via a \
relation -- do NOT put the same module inside multiple components to express \
sharing.
- Anchor every component to the REAL module names it groups via \
`contained_modules` (use the exact dotted names from the facts).

Component relations are REQUIRED, not optional. Read the `imports` in the facts: \
whenever a module in one component imports a module in another component, emit a \
deduplicated component-level `relation` between those two components. Do NOT \
invent relations that no import supports; do NOT omit relations that imports do \
support. An architecture that has components but an empty `relations` list is \
INCOMPLETE.

Output strictly conforms to the provided JSON schema."""


def build_messages(facts: list[ModuleFacts]) -> list[dict[str, str]]:
    """Build the chat messages for the current prompt version from module facts."""
    facts_json = json.dumps([f.model_dump() for f in facts], indent=2)
    user = (
        "Here are the extracted code facts as JSON:\n\n"
        f"{facts_json}\n\n"
        "Produce the abstracted architecture."
    )
    return [
        {"role": "system", "content": SYSTEM},
        {"role": "user", "content": user},
    ]


def build_retry_feedback(errors: list[str]) -> str:
    """Build the user feedback message that follows an invalid attempt."""
    bullets = "\n".join(f"- {err}" for err in errors)
    return (
        "Your previous output was INVALID for these reasons:\n"
        f"{bullets}\n\n"
        "Fix ONLY these problems and return a corrected architecture that "
        "conforms to the JSON schema. Keep the rest of your decomposition "
        "unchanged."
    )
