# Cycle Validity Spine

Use this file as the compact validation checkpoint surface before finalizing any serious `implementation-agent` cycle run.

Cycle Specs remain authoritative for behavioral truth. This file summarizes the minimum checkpoint questions the runner should actively verify before finalizing a terminal cycle state.

## State synchronization lens

- `completed` means the cycle may be finalized as completed only when the governing Spec allows that state and the required trust artifacts and validity conditions are satisfied.
- `paused` means the cycle must stop without overstating completion, with unresolved items and required Orchestrator direction surfaced explicitly.
- `failed` applies only to `implementation-execution-cycle`; it means the command cannot continue truthfully because required grounding, execution, or review conditions broke beyond the cycle's governed recovery path.
- Always distinguish the **terminal run state** from the **downstream-authority posture** in final reporting.

## implementation-planning-cycle

- **Governing Spec:** `specs/implementation-planning-cycle.spec.md`
- **Required runtime trust artifacts:** `CYCLE_STATUS.md`, `RUN_TRACE.md`, `VALIDATION_TRACE.md`
- **Conditional artifacts:** `DECISION_LOG.md` when decisions were made or requested
- **Allowed terminal states:** `completed`, `paused`
- **Completed validity checks:** required prompt artifacts were produced or refined; required runtime trust artifacts are present; unresolved gating items do not remain in a way that would invalidate completed-state reporting
- **Paused validity checks:** paused-run completeness follows the paused template; unresolved items are explicit; required Orchestrator direction is clear
- - **Final surfaced output checks:** exactly one terminal run-state block; updated working-copy link included; rerun reason / what changed / supersession surfaced when relevant
- **Rerun / supersession / downstream-authority checks:** reruns clearly state what changed; completed outputs must not overstate downstream authority when inherited upstream uncertainty or planning limitations still matter
- **Validation evidence checks:** local validation and full prompt-set review outcomes are reflected in trust artifacts and final reporting; if no repository-wide test command exists, completed-state reporting says so explicitly

## implementation-execution-cycle

- **Governing Spec:** `specs/implementation-execution-cycle.spec.md`
- **Required runtime trust artifacts:** `CYCLE_STATUS.md`, `RUN_TRACE.md`, `VALIDATION_TRACE.md`
- **Conditional artifacts:** `DECISION_LOG.md` when decisions were made or requested
- **Allowed terminal states:** `completed`, `paused`, `failed`
- **Completed validity checks:** all in-scope prompt-level units for the selected phase are truthfully accounted for; required run/review/retry artifacts are present; required runtime trust artifacts are present; final reporting does not overclaim phase acceptance
- **Paused validity checks:** the stop reason is explicit; unresolved items or escalation conditions are surfaced clearly; required Orchestrator direction is stated
- **Failed validity checks:** failure is reserved for command-level inability to continue truthfully, not for an individual prompt-level review failure that remains within governed retry/escalation behavior
- **Final surfaced output checks:** exactly one terminal run-state block; selected phase is stated explicitly; updated working-copy link included when produced by the run
- **Rerun / supersession / downstream-authority checks:** later retries or reruns clearly state what changed; local prompt success is not treated as final phase acceptance
- **Validation evidence checks:** prompt-level summary, evidence, patch, review, and retry records remain consistent with final reporting
