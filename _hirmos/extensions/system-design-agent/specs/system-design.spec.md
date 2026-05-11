# System Design Spec

This Spec governs `system-design-agent:system-design`, the public HIRMOS System Design step in Orchestrated Spec-Driven Development.

## Scope

`system-design-agent:system-design` consumes completed Requirements artifacts and produces the design artifacts needed before Implementation.

It is a lifecycle composition entrypoint. For normal greenfield System Design, it must compose:

```text
system-design-agent:system-design-cycle
system-design-agent:phase-design-cycle
```

It must not own Requirements production. Requirements production belongs to `requirements-agent`.

## Required upstream artifacts

Before System Design may proceed, the runner must verify that the following artifact exists and is usable:

```text
_hirmos/artifacts/sot/REQUIREMENTS_SOT.md
```

When present and relevant, the runner must also inspect:

```text
_hirmos/artifacts/context/requirements-agent/REQUIREMENTS_INPUT_PACK.md
_hirmos/artifacts/context/project/UNRESOLVED_ITEMS_INVENTORY.md
_hirmos/artifacts/context/project/UNRESOLVED_ITEMS_FEED.md
_hirmos/artifacts/context/project/UNRESOLVED_ITEMS_LEDGER.md
```

If required Requirements artifacts are missing or unusable, the entrypoint must pause and direct the Orchestrator to run or repair:

```text
hirmos requirements
```

System Design must not regenerate Requirements.

## Required lifecycle composition

For normal greenfield System Design completion, the public `system-design` entrypoint must execute or perform the responsibilities of:

1. `system-design-agent:system-design-cycle`
2. gated unresolved-item review
3. `system-design-agent:phase-design-cycle`
4. final System Design completion validation

The public step may only surface `completed` after both system-level design and phase-level design are complete, unless the run scope explicitly excludes implementation readiness and records that limitation.

## Required outputs

A completed System Design step must produce or verify the following artifacts when applicable to the run scope:

```text
_hirmos/artifacts/sot/SYSTEM_SOT.md
_hirmos/artifacts/sot/ARCHITECTURE_SOT.md
_hirmos/artifacts/sot/PHASES_SOT.md
_hirmos/artifacts/context/system-design-agent/STAGED_DELIVERY_TARGETS.md  # when staged delivery is relevant
phase-level SOT artifacts under _hirmos/artifacts/phases/
```

It must also produce or verify the relevant runtime trust artifacts for:

```text
_hirmos/artifacts/context/system-design-agent/system-design/
_hirmos/artifacts/context/system-design-agent/system-design-cycle/
_hirmos/artifacts/context/system-design-agent/phase-design-cycle/
```

## Reusable producer and cycle entrypoints

The System Design step may reuse these self-contained producer entrypoints where appropriate:

```text
system-design-agent:staged-delivery-targets
system-design-agent:system-sot
system-design-agent:architecture-sot
system-design-agent:phases-sot
system-design-agent:phase-sot
```

The System Design step must reuse or perform these lifecycle subcycles for normal greenfield completion:

```text
system-design-agent:system-design-cycle
system-design-agent:phase-design-cycle
```

`system-design-cycle` is narrowed to system-level design and must not produce Requirements.

`phase-design-cycle` is required for normal greenfield implementation readiness.

## Phase Design Requirement

For normal greenfield System Design, `phase-design-cycle` is required before System Design may surface completed.

`phase-design-cycle` runs after the narrowed system-design-cycle has produced system-level design artifacts and after all unresolved gated items that block phase design have been resolved.

If unresolved gated items remain, System Design must pause and surface the required decisions instead of running phase design.

If a run scope explicitly excludes implementation readiness, System Design may complete without phase design only if it records that scope limitation, explains why phase design was not required, and does not claim implementation readiness.

## Hook Participation

The public System Design step exposes and must honor these hook points when declared hook subscribers are installed:

```text
system-design-agent.system-design.contribute-unresolved-items
system-design-agent.system-design.before-final-gating-review
```

These hook points are for System Design-stage contributions. Requirements-stage enrichment belongs to `requirements-agent` hook points.

Hook effects must remain bounded, additive, and visible in the System Design run trace or terminal summary when materially relevant.

Hooks must not silently resolve gated decisions, overwrite System Design authority, bypass unresolved-item governance, or create extension-local unresolved-decision lanes.

## Unresolved-item governance

System Design must use the generalized unresolved-item contribution contract for system-design-stage unresolved items.

The narrowed `system-design-cycle` uses the existing artifact names under:

```text
_hirmos/artifacts/context/system-design-agent/system-design-cycle/
```

The public System Design step may summarize or compose those outputs under:

```text
_hirmos/artifacts/context/system-design-agent/system-design/
```

Expected artifact names include:

```text
UNRESOLVED_ITEMS_INVENTORY.md
UNRESOLVED_ITEMS_RECONCILIATION_WORKLIST.md
UNRESOLVED_ITEMS_FEED.md
UNRESOLVED_ITEMS_LEDGER.md
```

Do not create a separate design-decision bypass artifact.

Requirements-stage unresolved outputs are upstream inputs. System Design may reference them, but must not silently reclassify or override Requirements-stage gated decisions.

## Staged delivery handling

System Design must explicitly assess whether staged delivery is relevant.

When staged delivery is relevant, `_hirmos/artifacts/context/system-design-agent/STAGED_DELIVERY_TARGETS.md` must exist and follow `_hirmos/extensions/system-design-agent/templates/STAGED_DELIVERY_TARGETS_TEMPLATE.md` closely enough to support downstream planning.

## Stack handling

When Core resolves an active stack, System Design remains stack-aware only where the governing producer Specs justify stack consumption:

- `architecture-sot` may directly consume stack context;
- `system-sot` remains stack-neutral;
- `phases-sot` primarily inherits stack consequences through architecture outputs;
- downstream phase planning inherits stack consequences primarily through system-level design outputs.

## Preserved reliability discipline

The detailed system-level reliability mechanisms are owned by `system-design-cycle.spec.md`.

This public System Design Spec does not restate that full behavioral contract. Instead, it enforces that the public `system-design` entrypoint may not bypass the narrowed `system-design-cycle`, its producer validation, unresolved-item governance, decision absorption, runtime trust artifacts, fail-closed checks, or final surfaced-output self-validation.

The public System Design step also enforces composition-level reliability that belongs above the subcycles:

- Requirements-to-System-Design traceability before system-level design begins;
- gated unresolved-item review before phase design begins;
- System-to-phase traceability before completion;
- truthful terminal-state composition across `system-design-cycle` and `phase-design-cycle`;
- no completed state while a required subcycle or required run control remains pending.

## Completion validity

System Design may surface `completed` only when:

- required Requirements artifacts are present and usable;
- the narrowed `system-design-cycle` completed truthfully;
- required system-level artifacts are present and locally valid;
- staged delivery artifacts are present and valid when relevant;
- `phase-design-cycle` completed for normal greenfield implementation readiness;
- phase artifacts are present and valid when required for implementation readiness;
- required trust artifacts are present;
- no gated design/phase unresolved items remain without recorded Orchestrator direction;
- final surfaced output does not overclaim implementation readiness.

## Pause validity

System Design must surface `paused` when:

- required Requirements artifacts are missing or unusable;
- upstream Requirements unresolved decisions block honest design;
- narrowed system-design-cycle pauses;
- design unresolved items block phase design;
- phase-design-cycle pauses;
- design or phase unresolved items require Orchestrator/user direction;
- validation fails in a way that requires input or bounded remediation before continuing;
- hook/control obligations cannot be satisfied.

Paused output must clearly state:

- what blocked progress;
- why it matters;
- allowed outcomes or continuation options;
- whether phase design was not run, paused, or completed;
- what must happen before rerun/continuation.

## Failed validity

System Design may surface `failed` only when the step cannot safely complete and cannot identify a bounded pause/remediation path.

## Terminal-state composition

The public `system-design` terminal state is composed from subcycle outcomes:

- If `system-design-cycle` pauses, public System Design must pause.
- If `system-design-cycle` completes but gated unresolved items block phase design, public System Design must pause.
- If `phase-design-cycle` pauses, public System Design must pause.
- If both subcycles complete and final validation passes, public System Design may complete.
- If either subcycle fails unrecoverably and no bounded remediation exists, public System Design must fail.

## Final surfaced output self-validation

Before returning final output, validate:

- exactly one terminal run-state block is present;
- terminal state is truthful;
- artifact paths are real and relevant;
- Requirements artifacts consumed are identified;
- subcycle outcomes are identified;
- phase-design-cycle completion or truthful non-run reason is identified;
- unresolved-item summaries match run artifacts;
- remaining limitations are not hidden;
- next action is clear;
- completed output does not claim implementation can begin if gating design or phase decisions remain.
