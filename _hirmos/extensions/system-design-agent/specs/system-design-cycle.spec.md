# System Design Cycle Spec

This Spec governs `system-design-agent:system-design-cycle`, the narrowed system-level design cycle reused by the public `system-design-agent:system-design` entrypoint.

## Scope

`system-design-agent:system-design-cycle` consumes Requirements artifacts produced by `requirements-agent` and produces/refines the system-level design artifacts required before phase design.

It must not own Requirements production.

Requirements production belongs to:

```text
requirements-agent
```

This cycle may consume:

```text
_hirmos/artifacts/sot/REQUIREMENTS_SOT.md
_hirmos/artifacts/context/requirements-agent/REQUIREMENTS_INPUT_PACK.md
_hirmos/artifacts/context/project/UNRESOLVED_ITEMS_INVENTORY.md
_hirmos/artifacts/context/project/UNRESOLVED_ITEMS_FEED.md
_hirmos/artifacts/context/project/UNRESOLVED_ITEMS_LEDGER.md
prototype/presentation artifacts contributed during Requirements, when relevant
```

This cycle must not produce:

```text
_hirmos/artifacts/sot/REQUIREMENTS_SOT.md
_hirmos/artifacts/context/requirements-agent/REQUIREMENTS_INPUT_PACK.md
```

## Required governing files

Before running this cycle, read:

- `specs/CYCLE_VALIDITY_SPINE.md`
- `specs/unresolved-item-contribution-contract.md`
- `specs/system-sot.spec.md`
- `specs/architecture-sot.spec.md`
- `specs/phases-sot.spec.md`
- `specs/staged-delivery-targets.spec.md` when staged delivery is relevant
- `specs/PRESENTATION_CONTINUITY_RULE.md` when presentation artifacts materially affect system design

The generalized unresolved-item contribution contract is authoritative at:

```text
_hirmos/core/authority/extensions/unresolved-item-contribution-contract.md
```

The local system-design-agent unresolved contract may summarize or specialize it, but must not conflict with it.

## Required upstream artifacts

Before system-level design proceeds, verify that this required artifact exists and is readable:

```text
_hirmos/artifacts/sot/REQUIREMENTS_SOT.md
```

When present or relevant, also inspect:

```text
_hirmos/artifacts/context/requirements-agent/REQUIREMENTS_INPUT_PACK.md
_hirmos/artifacts/context/project/UNRESOLVED_ITEMS_INVENTORY.md
_hirmos/artifacts/context/project/UNRESOLVED_ITEMS_FEED.md
_hirmos/artifacts/context/project/UNRESOLVED_ITEMS_LEDGER.md
_hirmos/artifacts/sot/PROTOTYPE_SOT.md
_hirmos/artifacts/sot/PROTOTYPE_SET_SOT.md
_hirmos/artifacts/sot/PRESENTATION_SOT.md
```

If `REQUIREMENTS_SOT.md` is missing or unusable, pause. Do not regenerate Requirements inside this cycle.

## Required outputs

A completed cycle must produce or verify the applicable system-level artifacts:

```text
_hirmos/artifacts/sot/SYSTEM_SOT.md
_hirmos/artifacts/sot/ARCHITECTURE_SOT.md
_hirmos/artifacts/sot/PHASES_SOT.md
_hirmos/artifacts/context/system-design-agent/STAGED_DELIVERY_TARGETS.md  # when relevant
```

It must also update the run-scoped trust and unresolved-item artifacts under:

```text
_hirmos/artifacts/context/system-design-agent/system-design-cycle/
```

Required runtime trust artifacts:

```text
RUN_TRACE.md
VALIDATION_TRACE.md
CYCLE_STATUS.md
UNRESOLVED_ITEMS_INVENTORY.md
UNRESOLVED_ITEMS_RECONCILIATION_WORKLIST.md
UNRESOLVED_ITEMS_FEED.md
UNRESOLVED_ITEMS_LEDGER.md
CYCLE_STATE_REPORT.md  # when the cycle reaches a paused or completed reviewable state
```

Templates and folder scaffolding do not count as generated runtime artifacts.

## Proven reliability mechanisms that must be preserved

This narrowed cycle preserves the original System Design Cycle's reliability discipline while removing Requirements ownership.

The runner must preserve:

1. Hook-aware enrichment and hook-subscriber validation for System Design hook seams.
2. Input/source inventory discipline, now as consumption of Requirements outputs and relevant enrichment artifacts.
3. Producer-by-producer validation for system-level design artifacts.
4. Immediate unresolved-item contribution refresh after relevant producers.
5. Centralized unresolved-item inventory, reconciliation, feed, and ledger behavior for system-design-stage concerns.
6. Severity classification for assumptions, open questions, and gated unresolved items.
7. Gating-default categories and explicit downgrade justification.
8. Bounded-planning downgrade rules where applicable.
9. System-level coherence and downstream-readiness review.
10. Requirements-to-system-design traceability.
11. System-to-phase traceability through `PHASES_SOT.md` and staged delivery targets.
12. Decision absorption recording during governed reruns.
13. Runtime trust artifacts.
14. Terminal-state fail-closed checks.
15. Final surfaced output self-validation.
16. No completed state while any required control remains pending.

## Rerun discipline

When this cycle is rerun, make clear:

- why the rerun is happening;
- what changed since the prior pass;
- whether the new result supersedes the previous cycle result;
- which Requirements artifact version or relevant upstream decision state is being consumed.

If a rerun absorbs Orchestrator direction for previously unresolved gating items, record for each decision:

- the source decision;
- the disposition: applied / partially applied / deferred;
- the authoritative artifacts updated;
- any related item that remains visible downstream.

This decision-absorption record must appear in runtime trust artifacts, preferably in `RUN_TRACE.md` and validated in `VALIDATION_TRACE.md`.

## Hook participation

The narrowed system-design cycle may receive bounded additive contributions through the public System Design hook seams:

```text
system-design-agent.system-design.contribute-unresolved-items
system-design-agent.system-design.before-final-gating-review
```

Hook effects must remain bounded, additive, and visible in run trace, validation trace, unresolved-item artifacts, or terminal summary when materially relevant.

Hooks must not silently resolve gated decisions, overwrite System Design authority, bypass unresolved-item governance, create extension-local unresolved-decision lanes, or produce Requirements artifacts.

## Stack handling

When Core resolves an active stack, this cycle is stack-aware only at the orchestration layer:

- `architecture-sot` may directly consume stack context;
- `system-sot` remains stack-neutral;
- `phases-sot` primarily inherits stack consequences through architecture outputs;
- downstream phase planning inherits stack consequences through system-level design outputs.

## Staged delivery handling

The cycle must explicitly assess whether staged delivery is relevant.

If staged delivery is relevant, `_hirmos/artifacts/context/system-design-agent/STAGED_DELIVERY_TARGETS.md` must exist and follow `_hirmos/extensions/system-design-agent/templates/STAGED_DELIVERY_TARGETS_TEMPLATE.md` closely enough to support downstream planning.

If staged delivery is relevant and the artifact is missing or stale, run or perform `system-design-agent:staged-delivery-targets` responsibilities before downstream design completion.

## Producer sequence

At minimum, orchestrate these producer entrypoints when relevant for the current project state:

```text
system-design-agent:staged-delivery-targets
system-design-agent:system-sot
system-design-agent:architecture-sot
system-design-agent:phases-sot
```

Do not orchestrate `requirements-agent` from inside this cycle. If Requirements artifacts are missing or unusable, pause.

For each required producer:

1. Generate or refine the artifact.
2. Validate it against its governing Spec-backed local quality bar.
3. Capture assumptions and open questions.
4. Refresh that producer's contribution to `UNRESOLVED_ITEMS_INVENTORY.md`.
5. Iterate until locally acceptable or pause on a bounded blocker.

## Unresolved-item centralization

Producer `Assumptions` and `Open Questions` are equal canonical unresolved-item sources.

Hook contributions are bounded additive sources.

The cycle must generate or refresh:

```text
UNRESOLVED_ITEMS_INVENTORY.md
UNRESOLVED_ITEMS_RECONCILIATION_WORKLIST.md
UNRESOLVED_ITEMS_FEED.md
UNRESOLVED_ITEMS_LEDGER.md
```

The inventory must be built from actual current artifact state, not from memory.

`VALIDATION_TRACE.md` must explicitly record producer extraction completeness for canonical unresolved-item subsections, including whether both `Assumptions` and `Open Questions` were inspected and inventoried.

`VALIDATION_TRACE.md` must also explicitly record reconciliation completeness against the inventory body, including whether orphaned or duplicate inventory item IDs were found.

## Cross-artifact producer-attribution consistency rule

Before pause or completion may be surfaced, validate all of the following:

- for each producer artifact listed in producer extraction coverage, extracted/rejected counts must match reconstructable inventory-body counts;
- for each feed item, source inventory item IDs must resolve to real inventory items;
- feed `Producer coverage` must equal the unique producer artifacts present on cited source inventory items;
- no feed item may list a producer unless at least one cited source inventory item is attributed to that producer;
- no producer extraction coverage line may claim counts that cannot be reconstructed from the inventory body.

Fail closed if any of the above cannot be validated.

## Gating and severity discipline

The cycle must classify unresolved items truthfully.

Gating items include, at minimum, unresolved decisions that materially affect:

- system boundaries;
- architecture choices;
- data model / state model;
- security / privacy posture;
- phase boundaries;
- staged delivery feasibility;
- downstream implementation readiness;
- presentation/prototype constraints when they materially affect architecture or phases.

Downgrading a gating item requires explicit justification in the unresolved ledger/feed.

Bounded-planning downgrades may be used only when the design can proceed safely with clearly recorded assumptions and the limitation remains visible downstream.

## Final system-level review

After local producer gates pass, run a final system-level coherence and downstream-readiness review across:

- `REQUIREMENTS_SOT.md`;
- `SYSTEM_SOT.md`;
- `ARCHITECTURE_SOT.md`;
- `PHASES_SOT.md`;
- `STAGED_DELIVERY_TARGETS.md` when relevant;
- prototype/presentation SOT artifacts when materially relevant;
- unresolved-item inventory/feed/ledger outcomes;
- hook-derived design contributions.

The review must verify:

- requirements-to-system traceability;
- architecture consistency with system behavior;
- phase roadmap consistency with system and architecture decisions;
- no hidden assumptions that should be gated;
- downstream phase design can proceed honestly.

## Relationship to phase design

This cycle does not replace `system-design-agent:phase-design-cycle`.

For the public `system-design-agent:system-design` entrypoint, this cycle is the required system-level design subcycle that must complete or pause truthfully before phase design runs.

If this cycle surfaces `paused`, the public System Design entrypoint must not proceed to `phase-design-cycle`.

If this cycle surfaces `completed`, the public System Design entrypoint must evaluate whether any remaining gated unresolved item blocks phase design. If none do, it must run `phase-design-cycle` for normal greenfield completion.

## Local quality bar

The System Design Cycle is locally acceptable only when:

- required governing files and upstream Requirements artifacts were readable;
- Requirements were consumed but not regenerated;
- each required system-level SOT passed its local quality gate;
- staged delivery relevance was assessed and handled;
- hook-driven enrichment, when present, remained visible and bounded;
- unresolved-item inventory/reconciliation/feed/ledger artifacts are complete and internally consistent;
- final system-level coherence/downstream-readiness review passes;
- rerun behavior is explicit and intentional.

## Terminal Output Surfacing

Allowed surfaced terminal states for this entrypoint are:

- `completed`
- `paused`

Required terminal templates:

- `templates/system-design-cycle/COMPLETED_TEMPLATE.md`
- `templates/system-design-cycle/PAUSED_TEMPLATE.md`

The selected template is the source of truth for final surfaced output shape.

## Final surfaced output self-validation

Before treating the cycle response as final, verify that:

- the selected terminal state is truthful;
- the surfaced output uses the correct required template;
- every required template section is present;
- artifact paths and command claims are truthful;
- Requirements artifacts consumed are identified;
- gated and non-gating items are surfaced faithfully;
- every accepted feed item is accounted for before completion;
- rejected invalid contributions remain visible;
- honest completion is not overstated;
- the next action or rerun condition is explicit;
- active `RUN_EXECUTION_CONTROLS.md` notes match the current run state and do not preserve stale paused/completed wording from a prior run.

If any of these checks fail, revise the surfaced output before returning it.

## End condition

A paused or completed result is not governably valid unless all required runtime trust artifacts for that run state exist and were updated during the run.

If the cycle is reported as `completed`, the completed-state reporting must explicitly record:

- terminal-state basis;
- required runtime trust artifact completeness;
- unresolved-item status basis;
- residual non-blocking limitations, or explicitly state none;
- whether the public `system-design` entrypoint may proceed to phase design.

The cycle ends only when each required system-level SOT has passed its local quality gate and the full system-level set passes final coherence/downstream-readiness review.

## Non-goals

This cycle does not:

- produce Requirements artifacts;
- replace `requirements-agent`;
- replace `phase-design-cycle`;
- generate implementation prompts;
- execute implementation work;
- act as release control.
