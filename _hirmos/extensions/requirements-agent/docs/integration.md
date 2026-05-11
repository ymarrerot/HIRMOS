# requirements-agent Integration

## Front-door position

`requirements-agent` backs the first step of the regular-user HIRMOS workflow:

```text
Requirements → System Design → Implementation
```

## Downstream handoff

When completed, `requirements-agent` hands off to `system-design-agent` through requirements artifacts such as:

```text
_hirmos/artifacts/context/requirements-agent/REQUIREMENTS_INPUT_PACK.md
_hirmos/artifacts/sot/REQUIREMENTS_SOT.md
```

System Design should consume these artifacts rather than re-own requirements production.

## Optional input enrichment

Prototype and presentation extensions can enrich requirements through Requirements-stage hooks such as `requirements-agent.requirements.before-input-discovery` and `requirements-agent.requirements.before-requirements-normalization` when those extensions are installed.

## Unresolved items

Requirements-stage unresolved items must use the existing unresolved-item governance pattern and artifact names. Requirements-specific unresolved decisions must not bypass that pipeline.


## Requirements input sources

`requirements-agent` can use requirement-shaping inputs from:

- the current session prompt and collaborative reasoning;
- optional command argument tail after `hirmos requirements`;
- online-service attachments visible to the current LLM session;
- files under `_hirmos/inputs/requirements-agent/requirements/` when present;
- explicit bounded local file or repository-context references surfaced by the user or Orchestrator;
- derived artifacts contributed by installed extensions through declared hooks.

The runtime input folder is not shipped inside the extension package. Runtime folders such as `_hirmos/inputs/<extension-id>/...` are project runtime surfaces; the active Core/entrypoint path creates them during init or first run when needed.

Do not automatically ingest the full repository. If repository context is requested without a bounded scope, pause for scope or use a bounded discovery plan before treating repository content as Requirements input.
