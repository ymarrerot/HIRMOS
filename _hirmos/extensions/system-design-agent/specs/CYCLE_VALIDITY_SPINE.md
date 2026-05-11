# Cycle Validity Spine

Use this file as the compact validation checkpoint surface before finalizing any serious `system-design-agent` cycle run.

Cycle Specs remain authoritative for behavioral truth. This file summarizes the minimum checkpoint questions the runner should actively verify before finalizing a terminal cycle state.

## State synchronization lens

- `completed` means the cycle may be finalized as completed only when the governing Spec allows that state and the required trust artifacts and validity conditions are satisfied.
- `paused` means the step must stop without overstating completion, with unresolved items and required Orchestrator direction surfaced explicitly.

## system-design

- **Governing Spec:** `specs/system-design.spec.md`
- **Required runtime trust artifacts:** `CYCLE_STATUS.md`, `RUN_TRACE.md`, `VALIDATION_TRACE.md`, `UNRESOLVED_ITEMS_FEED.md`, `UNRESOLVED_ITEMS_LEDGER.md`
- **Conditional artifacts:** `DECISION_LOG.md` when decisions were made or requested; `CYCLE_STATE_REPORT.md` when the governing Spec/reporting flow requires it
- **Allowed terminal states:** `completed`, `paused`
- **Completed validity checks:** unresolved gating items do not remain; required runtime trust artifacts are present; every accepted unresolved-item feed entry was accounted for; every inventory item received exactly one reconciliation disposition; completed-state reporting does not overclaim validation or readiness; completed-state reporting is invalid if an unresolved item touching a gating-default category was classified below gating without explicit downgrade justification; completed-state reporting is invalid if downgrade justification exists but does not explain why completion remains honest; completed-state reporting is invalid if the final surfaced output omits materially relevant downgraded gating-default limitations
- **Paused validity checks:** paused-run completeness follows the paused template; unresolved items are explicit; rejected invalid contributions remain visible; the need for Orchestrator direction is clear; inventory-to-reconciliation coverage is complete even for a paused run
- **Final surfaced output checks:** exactly one terminal run-state block; updated working-copy link included; rerun reason / what changed / supersession surfaced when relevant
- **Rerun / supersession checks:** reruns clearly state why the cycle is being rerun and whether the new result supersedes the prior result; downstream outputs are not treated as authoritative until required reruns occur
- **Run execution controls refresh checks:** on reruns, `RUN_EXECUTION_CONTROLS.md` notes reflect the current run state and do not preserve stale paused/completed wording from the prior run
- **Validation evidence checks:** local validation, feed reconciliation outcomes, and final coherence review outcomes are reflected in trust artifacts and final reporting; final reporting is invalid if hook/control/trace artifacts claim no active presentation pack was found while a candidate runtime pack directory exists in `_hirmos/inputs/presentation-design/design-packs/` and no rejection reason is recorded; final reporting is invalid if an installed extension manifest declares an exact matching hook target for a resolved hook point but hook/control/trace artifacts record `Matched subscribers: none` without an explicit rejection reason for that installed matching subscriber; final reporting is invalid if a producer that ran during the cycle surfaced canonical unresolved items locally but failed to update its own producer-scoped contribution section in `UNRESOLVED_ITEMS_INVENTORY.md` truthfully before exit; final reporting is invalid if a required SoT producer was created or materially updated during the run, preserved canonical unresolved items, and lacked an immediately refreshed producer-scoped contribution block; final reporting is invalid if producer coverage in `VALIDATION_TRACE.md` is not derived from actual artifact state; final reporting is invalid if `_hirmos/artifacts/sot/PRESENTATION_SOT.md` exists, preserves canonical unresolved items, and lacks a matching producer-scoped contribution block or explicit rejection trail; final reporting is invalid if `_hirmos/artifacts/context/presentation-design/PRESENTATION_INPUT_PACK.md` exists, preserves canonical unresolved items, and lacks a matching producer-scoped contribution block or explicit rejection trail; final reporting is invalid if cycle completion depends on later cross-file rediscovery of producer unresolved items that should already have been contributed inline; final reporting is invalid if any inventory item is absent from reconciliation, appears in more than one reconciliation entry, or if a reconciliation entry references an unknown inventory item ID; final reporting is invalid if the cycle report fails to distinguish content unresolvedness from control-plane invalidity when both are present

## phase-design-cycle

- **Governing Spec:** `specs/phase-design-cycle.spec.md`
- **Required runtime trust artifacts:** `CYCLE_STATUS.md`, `RUN_TRACE.md`, `VALIDATION_TRACE.md`
- **Conditional artifacts:** `DECISION_LOG.md` when decisions were made or requested
- **Allowed terminal states:** `completed`, `paused`
- **Completed validity checks:** required phase artifacts were produced or refined; required runtime trust artifacts are present; no unresolved gating items remain that would make completed-state reporting invalid
- **Paused validity checks:** paused-run completeness follows the paused template; unresolved items are explicit; required Orchestrator direction is clear
- **Final surfaced output checks:** exactly one terminal run-state block; updated working-copy link included; rerun reason / what changed / supersession surfaced when relevant
- **Rerun / supersession checks:** reruns clearly state what changed and whether the new result supersedes the prior result
- **Validation evidence checks:** local validation and full phase-set review outcomes are reflected in trust artifacts and final reporting
