# implementation-agent entrypoints

This page helps users choose the correct `implementation-agent` entrypoint. Governing behavior remains in the corresponding Specs.

## Start here for the public HIRMOS Implementation step

Use the default public command in most regular-user workflows:

```text
hirmos implementation
```

This resolves to:

```text
implementation-agent:implementation
```

The public Implementation entrypoint is governed by:

```text
entrypoints/implementation.md
specs/implementation.spec.md
templates/implementation/
```

It verifies approved System Design and selected phase context, runs or refreshes planning when needed, pauses for explicit approval after planning, executes the selected/current phase only after approval, validates the result, and surfaces Evidence-backed Review.

## Advanced/reusable entrypoints

Use these only when you intentionally need lower-level control.

### `implementation-planning-cycle`

Use when you need approved scope turned into bounded execution-ready prompts.

This cycle preserves:

- prompt artifacts under `_hirmos/artifacts/prompts/phase-<NN>-<slug>/`
- runtime trust artifacts under `_hirmos/artifacts/context/implementation-agent/implementation-planning-cycle/`

### `implementation-execution-cycle`

Use when implementation planning is already approved and you need one selected phase executed, phase reviewed, and surfaced with a truthful terminal result.

This cycle preserves:

- execution evidence under `_hirmos/artifacts/ops/`
- phase review artifacts under `_hirmos/artifacts/ops/reviews/`
- runtime trust artifacts under `_hirmos/artifacts/context/implementation-agent/implementation-execution-cycle/`

### `prompt-planning`

Use when you need bounded implementation decomposition without running the full planning cycle.

### `agent-prompt`

Use when you need one final execution-ready prompt generated or refined directly.

## Approval boundary

The public `implementation` entrypoint must not silently proceed from planning to execution.

When planning is newly produced or materially refreshed, it must pause and ask for explicit Orchestrator approval before executing the phase.

## Output contracts at a glance

`implementation` preserves public-step trust artifacts under:

```text
_hirmos/artifacts/context/implementation-agent/implementation/
```

Retained subcycles preserve their own cycle-scoped trust artifacts.

Final public Implementation output uses exactly one of:

```text
templates/implementation/COMPLETED_TEMPLATE.md
templates/implementation/PAUSED_TEMPLATE.md
templates/implementation/FAILED_TEMPLATE.md
```

## Boundary reminder

`implementation-agent` owns bounded implementation planning and bounded implementation execution. It consumes approved System Design and phase scope, performs approval-gated execution, preserves evidence, and does not hide remaining material gaps inside a generic completion claim.

When the issue becomes an upstream Requirements/System Design or approval problem, `implementation-agent` must stop and hand control back to the Orchestrator.
