# Spec: Phase Design Cycle

## Purpose

Run the governed cycle that derives, validates, and refines the full phase set from _hirmos/artifacts/sot/PHASES_SOT.md (`/_hirmos/artifacts/sot/PHASES_SOT.md`).

This cycle orchestrates the generation and refinement of the full phase contract set defined by _hirmos/artifacts/sot/PHASES_SOT.md (`/_hirmos/artifacts/sot/PHASES_SOT.md`). It does not replace the underlying phase artifact Spec.

## Output location

- `_hirmos/artifacts/phases/`

## Rerun validity

This cycle may be rerun when the quality of phase planning is expected to improve because of a meaningful change in roadmap or planning conditions.

Common rerun triggers include:
- a refined _hirmos/artifacts/sot/PHASES_SOT.md (`/_hirmos/artifacts/sot/PHASES_SOT.md`)
- corrected staged-delivery structure
- improved upstream requirements/system planning
- discovery that the prior phase set did not cover the full intended roadmap
- downstream implementation-planning weakness exposing phase-design-cycle weakness

## Required inputs

Use:
- _hirmos/artifacts/sot/PHASES_SOT.md (`/_hirmos/artifacts/sot/PHASES_SOT.md`)
- relevant system-level SoT artifacts
- _hirmos/artifacts/context/system-design-agent/STAGED_DELIVERY_TARGETS.md (`/_hirmos/artifacts/context/system-design-agent/STAGED_DELIVERY_TARGETS.md`) when relevant
- current project context
- _hirmos/artifacts/sot/PRESENTATION_SOT.md (`/_hirmos/artifacts/sot/PRESENTATION_SOT.md`) when normalized presentation constraints materially affect phase boundaries, sequencing, UX-heavy flows, or design-system work

## Required governing files

Before running this cycle, read:
- [_hirmos/extensions/system-design-agent/specs/phase-sot.spec.md](./phase-sot.spec.md)
- [_hirmos/extensions/system-design-agent/specs/PRESENTATION_CONTINUITY_RULE.md](./PRESENTATION_CONTINUITY_RULE.md)

## Readiness check before run

Before this cycle begins, verify that the required governing files and relevant project artifacts are present and readable in the current working state.

Read the governing files before starting the cycle.

If the required files are missing or unreadable, the step must not be treated as properly started.

## Rerun discipline

When this cycle is rerun, make clear:
- why the rerun is happening
- what changed since the prior pass
- whether the new cycle result supersedes the previous phase-design-cycle result

Reruns should refine or replace the phase set intentionally rather than duplicating work without purpose.

## Local cycle quality bar

The Phase Design Cycle is locally acceptable only when:
- each phase artifact passes local validation against `specs/phase-sot.spec.md`
- the full phase set is coherent
- all phases defined in _hirmos/artifacts/sot/PHASES_SOT.md (`/_hirmos/artifacts/sot/PHASES_SOT.md`) are covered unless explicitly scoped otherwise
- downstream implementation planning can begin without major roadmap ambiguity

## Input alignment rules

This step must stay aligned to:
- _hirmos/artifacts/sot/PHASES_SOT.md (`/_hirmos/artifacts/sot/PHASES_SOT.md`)
- relevant system-level SoTs
- staged delivery context when relevant
- normalized presentation constraints when they materially affect roadmap shape, shared UI foundation work, or downstream implementation expectations

It must not use downstream phase artifacts to silently repair a weak roadmap definition.

## Failure / repair expectation

If local phase artifacts are weak or the full phase set is incomplete, incoherent, or misaligned:
- refine the affected artifacts or rerun the cycle as needed before downstream planning proceeds

## Governing principle

The full phase set must be planned as a coherent whole.

This cycle should not plan one isolated phase and then move downstream immediately. It should generate and validate the full phase set first.

When normalized presentation artifacts exist, apply [_hirmos/extensions/system-design-agent/specs/PRESENTATION_CONTINUITY_RULE.md](./PRESENTATION_CONTINUITY_RULE.md) and preserve only the roadmap-shaping consequences needed by this cycle.

## Step 0 — determine whether this is a rerun

If this cycle has already been run for the current working state, determine whether this execution is a governed rerun.

If so:
- identify the rerun trigger
- identify the changed roadmap/planning conditions
- use that information to refine the phase set intentionally

## Repeatable unit

Generate or refine one phase-level SoT artifact, then validate it against:
- the governing phase strategy in _hirmos/artifacts/sot/PHASES_SOT.md (`/_hirmos/artifacts/sot/PHASES_SOT.md`)
- its local phase quality bar
- cross-phase consistency expectations

For each phase artifact, read and follow `specs/phase-sot.spec.md` as the canonical local phase Spec for phase-level generation and validation.

The cycle orchestrates the loop. `phase-sot.spec.md` defines the local phase contract, required structure, local quality bar, and validation expectations.

Repeat until each phase artifact is locally acceptable.

## Phase-set review

After the individual phase artifacts are locally acceptable, run a full phase-set review.

That review must check:
- full and correct coverage of all phases defined in _hirmos/artifacts/sot/PHASES_SOT.md (`/_hirmos/artifacts/sot/PHASES_SOT.md`)
- mutual coherence of the phase set
- alignment with all declared Staged Delivery Targets when relevant

When _hirmos/artifacts/sot/PHASES_SOT.md (`/_hirmos/artifacts/sot/PHASES_SOT.md`) defines phases across multiple Delivery Targets, the Phase Design Cycle must still cover the full phase roadmap unless explicitly scoped otherwise.

Local acceptability for each phase artifact must be judged against `specs/phase-sot.spec.md`, not only against a summarized step-level description.

## Phase-Level Gating Review

Before finalizing the phase set, evaluate whether unresolved pending items materially affect phase boundaries, roadmap grouping, downstream phase-contract shape, or delivery-target feasibility. If they do, request Orchestrator direction rather than silently finalizing a misleading phase roadmap.

If unresolved gating items still materially affect the phase roadmap or downstream phase contracts, the cycle should pause rather than present the phase set as governably complete. Present those items as a structured decision request to the Orchestrator.

## Real-Use Readiness Review

When the phase set includes an early delivery target intended for real operational use, review whether the current phase structure visibly accounts for readiness-critical work before treating that target as feasible.

If not, preserve the readiness gap explicitly or request Orchestrator direction.

## End condition

A completed run is not governably valid if required runtime trust artifacts are missing. Absence of `DECISION_LOG.md` is valid only when `CYCLE_STATUS.md` explicitly records `Decision log status: none required this run`.

If the cycle is reported as `completed`, the completed-state reporting must explicitly record:
- the terminal-state basis
- required runtime trust artifact completeness
- the unresolved-item status basis when relevant
- any residual limitations that remain non-blocking, or explicitly state none

The Phase Design Cycle ends only when:
- the generated phase artifacts fully and correctly cover all phases defined in _hirmos/artifacts/sot/PHASES_SOT.md (`/_hirmos/artifacts/sot/PHASES_SOT.md`)
- the phase set is mutually coherent
- the phase set aligns with all declared Staged Delivery Targets when relevant

Unless explicitly scoped otherwise, this means the step must cover the entire planned phase roadmap, not only an early subset of phases.

## Required Runtime Trust Artifacts

After each run, update the command-scoped runtime trust artifacts under `_hirmos/artifacts/context/system-design-agent/phase-design-cycle/`. Required artifacts are:
- _hirmos/artifacts/context/system-design-agent/phase-design-cycle/CYCLE_STATUS.md (`/_hirmos/artifacts/context/system-design-agent/phase-design-cycle/CYCLE_STATUS.md`)
- _hirmos/artifacts/context/system-design-agent/phase-design-cycle/RUN_TRACE.md (`/_hirmos/artifacts/context/system-design-agent/phase-design-cycle/RUN_TRACE.md`)
- _hirmos/artifacts/context/system-design-agent/phase-design-cycle/VALIDATION_TRACE.md (`/_hirmos/artifacts/context/system-design-agent/phase-design-cycle/VALIDATION_TRACE.md`)
- _hirmos/artifacts/context/system-design-agent/phase-design-cycle/DECISION_LOG.md (`/_hirmos/artifacts/context/system-design-agent/phase-design-cycle/DECISION_LOG.md`) when decisions are made or requested

Use the corresponding templates under `_hirmos/artifacts/context/system-design-agent/phase-design-cycle/templates/` when generating or refining these artifacts. Templates and folder scaffolding do not count as generated runtime artifacts.

If no phase-design-cycle decisions were made or requested during the run, `DECISION_LOG.md` may be omitted only if `CYCLE_STATUS.md` explicitly states `Decision log status: none required this run`.

If the cycle pauses, record that the phase artifacts are useful but not yet governably finalized.


## Failure / repair behavior

If an individual phase artifact fails:
- refine it before continuing

If full phase-set review fails:
- refine the affected phase artifacts and repeat the phase-set review

If required governing files or relevant project artifacts are missing or unreadable in the current working state:
- stop the cycle
- report the issue clearly
- do not claim the cycle was run correctly

If the existing phase set is materially incomplete, misaligned, or weakened by upstream planning issues:
- rerunning the Phase Design Cycle may be the correct governed repair action

## Non-goals

This cycle does NOT:
- generate implementation prompts
- execute implementation work
- act as release control

## Mandatory self-validation

Before treating the cycle as complete, verify that:
- the cycle was properly grounded in readable governing/project files
- every generated or refined phase artifact passed local validation against `phase-sot.spec.md`
- the full phase set correctly covers all phases defined in _hirmos/artifacts/sot/PHASES_SOT.md (`/_hirmos/artifacts/sot/PHASES_SOT.md`), unless explicitly scoped otherwise
- the phase set is mutually coherent
- the phase set aligns with all declared staged delivery targets when relevant
- downstream implementation planning can begin without major roadmap ambiguity
- rerun reporting is included when this execution supersedes a previous cycle result

If any of the above checks fail, refine the affected phase artifacts or stop and report the grounding issue clearly.




## Relationship to public System Design

For normal greenfield System Design, this cycle is required before `system-design-agent:system-design` may surface `completed`.

This cycle runs after the narrowed `system-design-agent:system-design-cycle` has produced system-level design artifacts and after all unresolved gated items that block phase design have been resolved.

If unresolved gated items still materially affect phase boundaries, roadmap grouping, downstream phase-contract shape, or delivery-target feasibility, this cycle must pause rather than present the phase set as governably complete.

If a public System Design run explicitly excludes implementation readiness, the public `system-design` entrypoint may skip this cycle only when it records the scope limitation and does not claim implementation readiness.

## Terminal Output Surfacing

Allowed surfaced terminal states for this entrypoint are:
- `completed`
- `paused`

Required terminal templates:
- `templates/phase-design-cycle/COMPLETED_TEMPLATE.md`
- `templates/phase-design-cycle/PAUSED_TEMPLATE.md`

The selected template is the source of truth for final surfaced output shape.

## Final Surfaced Output Self-Validation

Before treating the cycle response as final, verify that:
- the selected terminal state is truthful
- the surfaced output uses the correct required template
- every required template section is present
- artifact paths and command claims are truthful
- unresolved items are surfaced faithfully
- honest completion is not overstated
- the next action or rerun condition is explicit

If any of the above checks fail, revise the surfaced output before returning it.

## Compact validity checkpoint

Before finalizing the cycle response state, use `specs/CYCLE_VALIDITY_SPINE.md` as a compact validation checkpoint. Behavioral authority remains in this Spec.

## Downstream handoff note

A passing Phase Design Cycle means the phase-level contract set is strong enough for downstream Implementation Planning to proceed.

It does not itself authorize bounded implementation execution.