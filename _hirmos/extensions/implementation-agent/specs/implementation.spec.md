# Spec: Implementation

This Spec governs `implementation-agent:implementation`, the public HIRMOS Implementation step in Orchestrated Spec-Driven Development.

## Scope

`implementation-agent:implementation` consumes approved System Design and phase artifacts, ensures planning exists, pauses for approval when planning is newly created or refreshed, and executes one selected/current phase only after approval.

It is the default public entrypoint for:

```text
hirmos implementation
```

## Required upstream artifacts

Before Implementation may proceed, the runner must verify that relevant upstream artifacts are present and readable.

Required or expected artifacts include:

- `_hirmos/artifacts/sot/SYSTEM_SOT.md`
- `_hirmos/artifacts/sot/ARCHITECTURE_SOT.md`
- `_hirmos/artifacts/sot/PHASES_SOT.md`
- selected/current phase artifact under `_hirmos/artifacts/phases/`
- active stack context resolved through `_hirmos/project.json` where relevant
- implementation repository or starter codebase context sufficient for grounded implementation work

If required upstream artifacts are missing or unreadable, the entrypoint must pause and identify what must be produced or repaired before Implementation can continue.

## Selected phase requirement

The public Implementation step executes one selected/current phase at a time.

If the selected/current phase is unclear, ambiguous, or missing, the entrypoint must pause and ask the Orchestrator to identify the phase.

Do not select a phase silently when doing so would create material scope risk.

## Reusable implementation cycles

The Implementation step may reuse these existing implementation-agent cycles:

- `implementation-agent:implementation-planning-cycle`
- `implementation-agent:implementation-execution-cycle`

These cycles remain valid reusable internal/advanced surfaces when they do not duplicate the public Implementation lifecycle truth.

## Planning readiness and approval boundary

Implementation planning is an approval boundary.

If implementation planning artifacts are missing, stale, incomplete, or materially refreshed during the current run, the public Implementation step must pause after planning and ask for explicit approval before phase execution.

A run that only completed planning may not surface `completed` as if implementation execution also completed.

Paused planning-approval output must state:

- planning artifacts created or refreshed;
- what the Orchestrator should review;
- what approval is needed;
- what command/continuation should happen next;
- why execution did not proceed yet.

## Execution eligibility

The public Implementation step may proceed to execution only when all are true:

- relevant planning artifacts exist and are readable;
- planning artifacts are approved for the selected/current phase;
- selected/current phase is clear;
- minimum implementation grounding contract is satisfied;
- no approval-bound tradeoff remains unresolved;
- command/runtime controls are satisfied.

If these are not all true, the step must pause or fail truthfully.

## Evidence-backed Review

Evidence-backed Review is a required sub-concept under Implementation.

When execution occurs, the final surfaced output must review the result based on evidence, including:

- what changed;
- what execution artifacts were produced;
- what validation commands/checks ran;
- what passed or failed;
- whether phase review completed;
- whether bounded repair was attempted;
- what unresolved items or material gaps remain;
- why the final terminal state is truthful;
- what should happen next.

Completion must be evidence-backed, not assertion-backed.

## Required outputs

A completed Implementation step must produce or verify, as applicable:

- phase-scoped prompt artifacts under `_hirmos/artifacts/prompts/phase-<NN>-<slug>/`;
- execution records under `_hirmos/artifacts/ops/runs/`;
- review artifacts under `_hirmos/artifacts/ops/reviews/`;
- retry artifacts under `_hirmos/artifacts/ops/retries/` when retries occur;
- phase review artifact under `_hirmos/artifacts/ops/reviews/<phase-id>-phase-review/`;
- run-scoped trust artifacts under `_hirmos/artifacts/context/implementation-agent/implementation/`;
- truthful completed/paused/failed terminal output.

## Terminal states

Allowed final surfaced states are:

- `completed`
- `paused`
- `failed`

### Completed is allowed only when

- selected/current phase execution occurred after planning approval;
- in-scope execution work completed or was escalated truthfully;
- validation and phase review ran where required;
- Evidence-backed Review can truthfully support completion;
- remaining material gaps, if any, are disclosed and non-gating for this terminal state.

### Paused is required when

- planning completed and requires approval before execution;
- required upstream artifacts are missing or unusable;
- selected/current phase is unclear;
- planning artifacts are missing/stale and cannot be completed in the current run;
- approval-bound implementation tradeoffs remain unresolved;
- environment or validation blockers require Orchestrator direction;
- bounded repair is exhausted but a governable pause remains possible.

### Failed is allowed only when

- the step cannot be grounded at all;
- command-critical execution or validation conditions prevent a governable result;
- required reviewability artifacts cannot be produced;
- no truthful pause/remediation path exists.

## Required terminal templates

The final surfaced output must follow exactly one of:

- `templates/implementation/COMPLETED_TEMPLATE.md`
- `templates/implementation/PAUSED_TEMPLATE.md`
- `templates/implementation/FAILED_TEMPLATE.md`

## Mandatory self-validation

Before treating the public Implementation step as complete, verify that:

- the truthful terminal state was selected;
- planning completion was not overstated as execution completion;
- execution did not proceed without explicit planning approval;
- relevant upstream artifacts were readable;
- selected/current phase was clear;
- evidence and validation claims are backed by actual artifacts or disclosed limitations;
- Evidence-backed Review is present for completed execution runs;
- the final surfaced output follows the required template;
- artifact paths and command claims are truthful.

If any check fails, refine, pause, or fail rather than claiming completion.

## Non-goals

This public Implementation step does not:

- perform Requirements;
- perform System Design;
- execute all phases autonomously;
- skip Orchestrator approval after planning;
- replace brownfield-specific repair/new-feature workflows that may be introduced later;
- claim release readiness by itself.
