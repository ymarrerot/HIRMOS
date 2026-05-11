# system-design-agent:system-design-cycle

## Execution Contract

### Purpose

Run the narrowed **System Design Cycle** for the current working state.

This cycle is the system-level design subcycle used by the public `system-design-agent:system-design` entrypoint. It consumes Requirements artifacts produced by `requirements-agent`, produces or refines system-level design artifacts, and preserves the original system-design reliability discipline without re-owning Requirements production.

### Produces

- `_hirmos/artifacts/sot/SYSTEM_SOT.md`
- `_hirmos/artifacts/sot/ARCHITECTURE_SOT.md`
- `_hirmos/artifacts/sot/PHASES_SOT.md`
- `_hirmos/artifacts/context/system-design-agent/STAGED_DELIVERY_TARGETS.md` when staged delivery is relevant
- cycle trust artifacts under `_hirmos/artifacts/context/system-design-agent/system-design-cycle/`
- project-level unresolved-item artifacts under `_hirmos/artifacts/context/project/`
- a governed cycle result surfaced as `completed` or `paused`

### Terminal States

- `completed` — allowed only when required system-level design artifacts and trust artifacts are in place, producer validation passes, unresolved-item governance is complete, and no unresolved gated item blocks honest downstream phase design.
- `paused` — required when the cycle reaches a governed decision, missing prerequisite, hook/control blocker, unresolved gated item, or grounding stop.

## Run-Critical Checklist

- **Must read first:** `specs/system-design-cycle.spec.md`, `specs/CYCLE_VALIDITY_SPINE.md`, and the governing files referenced by the cycle spec.
- **Must consume Requirements:** read `_hirmos/artifacts/sot/REQUIREMENTS_SOT.md` and relevant `requirements-agent` context artifacts before system-level design proceeds.
- **Must not produce Requirements:** this cycle must not generate `REQUIREMENTS_SOT.md` or `REQUIREMENTS_INPUT_PACK.md`; Requirements production belongs to `requirements-agent`.
- **Must follow unresolved-item governance:** use the generalized unresolved-item contribution contract and the project-level canonical unresolved artifact chain.
- **Must verify grounding:** required cycle files and relevant project files must be present and readable before planning proceeds.
- **Must validate final state:** validate against `specs/CYCLE_VALIDITY_SPINE.md` and `specs/system-design-cycle.spec.md` before responding.
- **Must respect exposed hooks:** declared System Design hook points may host bounded additive behavior from installed extensions, and that activity must remain visible in trust artifacts.
- **Must handle stack context correctly:** when Core resolves an active stack, route that context only to stack-appropriate downstream planning specs.
- **Must not claim:** completion if unresolved gated items remain or if the cycle skipped required producer validation.

## Allowed Final States

- `completed`
- `paused`

## Required Terminal Output Templates

- Completed runs must follow [_hirmos/extensions/system-design-agent/templates/system-design-cycle/COMPLETED_TEMPLATE.md](../templates/system-design-cycle/COMPLETED_TEMPLATE.md).
- Paused runs must follow [_hirmos/extensions/system-design-agent/templates/system-design-cycle/PAUSED_TEMPLATE.md](../templates/system-design-cycle/PAUSED_TEMPLATE.md).
- Do not improvise hybrid terminal outputs.

## Planning Logic

1. Read and follow `specs/system-design-cycle.spec.md`.
2. Verify required governing files, relevant project files, and required Requirements artifacts are present and readable:
   - `_hirmos/artifacts/sot/REQUIREMENTS_SOT.md`
   - `_hirmos/artifacts/context/requirements-agent/REQUIREMENTS_INPUT_PACK.md` when present or relevant
   - project-level unresolved-item artifacts when present
3. If required Requirements artifacts are missing or unusable, stop and surface `paused`; instruct the Orchestrator to run or repair `hirmos requirements`.
4. Determine whether this is a governed rerun. If so, identify why the cycle is being rerun, what changed, and whether the new result supersedes a previous result.
5. Assess staged-delivery relevance from Requirements outputs and project context. If relevant and `_hirmos/artifacts/context/system-design-agent/STAGED_DELIVERY_TARGETS.md` is missing or stale, run or perform `system-design-agent:staged-delivery-targets` responsibilities.
6. If Core resolves an active stack, treat this cycle as stack-aware only at the orchestration layer:
   - provide stack context to `system-design-agent:architecture-sot`
   - keep `system-design-agent:system-sot` stack-neutral
   - let downstream phase planning inherit stack consequences primarily through upstream architecture outputs
7. Honor declared System Design hook points for bounded additive design-stage contributions. Hook contributions must remain visible in run trace, unresolved-item artifacts, or terminal summary when materially relevant.
8. Generate or refine each required system-level SOT by orchestrating the appropriate producer entrypoint/spec:
   - `system-design-agent:system-sot`
   - `system-design-agent:architecture-sot`
   - `system-design-agent:phases-sot`
   - `system-design-agent:staged-delivery-targets` when relevant
9. After each relevant producer, refresh that producer's assumptions/open questions contribution into the project-level canonical unresolved-item inventory. Treat producer `Assumptions` and `Open Questions` as equal canonical unresolved-item sources.
10. Build or refresh the full unresolved-item artifact chain under `_hirmos/artifacts/context/project/`:
   - `UNRESOLVED_ITEMS_INVENTORY.md`
   - `UNRESOLVED_ITEMS_RECONCILIATION_WORKLIST.md`
   - `UNRESOLVED_ITEMS_FEED.md`
   - `UNRESOLVED_ITEMS_LEDGER.md`
11. Classify unresolved items by severity and gating status using the governing unresolved-item contract. Gating items must remain visible; downgrades require explicit justification.
12. Run final system-level coherence and downstream-readiness review across `REQUIREMENTS_SOT.md`, `SYSTEM_SOT.md`, `ARCHITECTURE_SOT.md`, `PHASES_SOT.md`, staged delivery targets, hook-derived design contributions, and unresolved-item outcomes.
13. If final review fails due to artifact weakness, refine affected system-level SOT artifacts and repeat validation.
14. If unresolved gated items block honest phase design or downstream implementation readiness, surface `paused` and request Orchestrator/user direction. Do not allow the public `system-design` entrypoint to continue into `phase-design-cycle` until those blockers are resolved.
15. If the cycle reaches a reviewable paused or completed state, generate `_hirmos/artifacts/context/system-design-agent/system-design-cycle/CYCLE_STATE_REPORT.md` using `templates/SYSTEM_DESIGN_CYCLE_STATE_REPORT_TEMPLATE.md`.
16. Progress updates are allowed while the cycle is running, but they must clearly indicate the cycle is still in progress and must not sound like final completion.

## Relationship to `system-design-agent:system-design`

This cycle is not the full public System Design step. The public `system-design-agent:system-design` entrypoint composes this narrowed system-level cycle with `system-design-agent:phase-design-cycle`.

For normal greenfield System Design completion, this cycle must complete or pause truthfully before `phase-design-cycle` can run. If this cycle pauses on gated design blockers, the public System Design step must pause rather than proceed to phase design.

## Artifact Obligations

Runtime trust artifacts live under `_hirmos/artifacts/context/system-design-agent/system-design-cycle/`. Project-level unresolved-item artifacts live under `_hirmos/artifacts/context/project/`.

Required cycle trust artifacts are:

- `RUN_TRACE.md`
- `VALIDATION_TRACE.md`
- `CYCLE_STATUS.md`
- `CYCLE_STATE_REPORT.md`

Required project-level unresolved-item artifacts are:

- `UNRESOLVED_ITEMS_INVENTORY.md`
- `UNRESOLVED_ITEMS_RECONCILIATION_WORKLIST.md`
- `UNRESOLVED_ITEMS_FEED.md`
- `UNRESOLVED_ITEMS_LEDGER.md` when the cycle reaches a paused or completed reviewable state

Templates and folder scaffolding do not count as generated runtime artifacts.

## Final Surfaced Output Self-Validation

Before treating the cycle response as final, verify that:

- the selected terminal state is truthful
- the surfaced output uses the correct required template
- every required template section is present
- artifact paths and command claims are truthful
- Requirements were consumed but not regenerated
- gated and non-gating items are surfaced faithfully
- every accepted feed item is accounted for before completion
- rejected invalid contributions remain visible
- honest completion is not overstated
- the next action or rerun condition is explicit
- active `RUN_EXECUTION_CONTROLS.md` notes match the current run state and do not preserve stale paused/completed wording from a prior run

If any of the above checks fail, revise the surfaced output before returning it.
