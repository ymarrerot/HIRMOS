# Runtime Surfaces

Use this page when you want the practical picture of where HIRMOS runtime materials usually appear during real work. It is most useful after the first serious run, when you want to relate framework artifacts to familiar SDLC stages without needing the full folder doctrine.


## Common runtime surfaces

- `_hirmos/inputs/<extension-id>/...` — raw extension-owned runtime inputs
- `_hirmos/artifacts/context/<extension-id>/...` — normalized extension-owned runtime context
- `_hirmos/artifacts/outputs/<extension-id>/...` — extension-owned result and deliverable surfaces
- `_hirmos/artifacts/sot/` — authoritative source-of-truth artifacts
- `_hirmos/artifacts/phases/` — generated phase contracts
- `_hirmos/artifacts/prompts/` — generated execution prompts
- `_hirmos/artifacts/ops/...` — implementation-stage operational runtime records for execution-oriented extensions
- `_hirmos/STACK_CONFIG.json` and `_hirmos/stacks/` — project-level stack selection and installed stack packages

## How to think about them together

Use `inputs` and `context` to separate raw intake from normalized working state.
Use `outputs` for result surfaces intended for human approval, handoff, or external/system consumption.
Use `sot`, `phases`, and `prompts` for stronger lifecycle artifacts when those lanes are relevant.
Use `ops` only for implementation-stage operational runtime records rather than as a generic review or scratch surface.

## SDLC-oriented mental model

A simple way to place these surfaces is:
- inputs often support early intake, discovery, or requirements grounding
- context supports in-progress work during design, planning, and implementation stages
- source-of-truth and phase artifacts support reviewed handoff between stages
- prompts and ops artifacts are more execution-facing and usually appear later in the flow

## Templates

Use extension-local templates when they are tightly coupled to that extension's own workflow. Use `_hirmos/extensions/_templates/` for central maintainer-facing starter and scaffolding templates.

## Need the deeper folder rules?

Use this page for the practical runtime picture first. When you need exact folder ownership or SoT policy details, use:
- [Top-level folder definitions](../../core/authority/framework/top-level-folder-definitions.md)
- [_hirmos/SOT_CHANGE_POLICY.md](../../SOT_CHANGE_POLICY.md)
