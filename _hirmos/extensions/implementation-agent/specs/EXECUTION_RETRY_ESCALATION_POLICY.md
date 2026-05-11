# EXECUTION_RETRY_ESCALATION_POLICY

## Purpose

Define the bounded retry and escalation rules for `implementation-agent:implementation-execution-cycle`.

This file exists so the retry-budget model and escalation thresholds are not duplicated across the entrypoint and the main cycle Spec. The canonical retry-artifact method lives in `retry-prompt.spec.md`.

## Scope

This policy governs one prompt-level execution unit inside one selected phase.

It does not govern:
- multi-phase execution
- phase review conclusions themselves
- terminal output template selection
- release approval
- cross-extension review architecture ownership

## Core model

For each approved implementation prompt in the selected phase, treat the work as a bounded execution unit:
1. initial execution attempt
2. local review against prompt + relevant phase contract + produced evidence
3. bounded retry only when the failure is locally repairable and still inside scope
4. escalation when local repair is no longer the truthful next move

## Default retry budget

Unless a future governed setting overrides it, use this default budget:
- maximum of **2 retry prompts** for one original prompt-level unit
- total maximum of **3 implementation attempts** for that unit:
  - 1 initial attempt
  - up to 2 retries

This is a default governance rule, not a suggestion.
Unbounded retry behavior is invalid.

## Phase review repair-round budget

When `implementation-execution-cycle` enters the phase-review repair loop after an initial failed phase review, use this default bound unless a future governed rule overrides it:
- maximum of **2 phase-review repair rounds** after the initial failed phase review
- after the second repair round, the cycle must either:
  - reach an honest `completed` result, or
  - stop autonomous repair and surface `paused` or `failed` truthfully

This bound governs the repair loop around phase review. It does not remove the requirement to stop earlier whenever another autonomous repair pass would no longer be honest.

## When a retry is allowed

A retry is allowed only when all of the following are true:
- the local review produced a binary fail result
- the root cause is explicit enough to act on
- the correction remains inside the current approved prompt and selected phase
- the retry can be stated as a minimal targeted correction
- the next attempt is more informed than blind repetition

## When a retry is NOT allowed

Do not generate another retry when any of the following is true:
- the needed correction would materially broaden scope
- the prompt or phase contract needs interpretation from the Orchestrator
- the discovered issue materially affects adjacent planned work or phase strategy
- required evidence cannot be produced truthfully
- the same root cause keeps recurring without meaningful narrowing
- the required correction is no longer a bounded patch-like fix

When a retry is not allowed, escalate instead of pretending the loop is still local.

## Escalation thresholds

Pause the cycle for Orchestrator direction when a prompt-level unit or phase-review repair loop reaches any of these thresholds:
- the unit consumed the retry budget without a local pass
- the phase-review repair loop consumed the allowed repair rounds without reaching an honest completed state
- the second failure shows the problem is architectural or contract-interpretive rather than patch-local
- the next correction would require phase-level reprioritization or strategy change
- stack or repository verification surfaces exist but cannot be resolved truthfully for this unit
- the generated retry would be broad, multi-problem, or phase-shaping rather than targeted

## Failed vs paused

Use `paused`, not `failed`, when the cycle still has a reviewable path forward that requires Orchestrator direction.

Use `failed` only when truthful continuation is not governable at the command level, such as:
- command-critical grounding is absent
- the working state is too incomplete or inconsistent to identify the selected phase or its prompts
- mandatory artifact generation is impossible in a way that blocks any reviewable pause path

## Retry artifact contract

For each generated retry, preserve a retry artifact under:
- `_hirmos/artifacts/ops/retries/<prompt-id>/retry-<n>.md`

The artifact structure and minimum required fields are governed by `retry-prompt.spec.md`.

## Review artifact contract

For each local review attempt, preserve a review artifact under:
- `_hirmos/artifacts/ops/reviews/<prompt-id>/review-<attempt-id>.md`

That artifact must include at minimum:
- prompt identifier
- attempt identifier
- review inputs used
- pass/fail result
- findings
- blocking defects when failed
- evidence references used in the review
- whether another retry is allowed or escalation is required

## Attempt traceability rule

The run, review, and retry records for one prompt-level unit must be cross-referenceable.

At minimum, the artifact set for a unit should make it possible to reconstruct:
- what was attempted
- what changed
- what was reviewed
- why it failed or passed
- why the next move was retry, pause, or cycle failure

## Pause output requirement

When pause happens because a prompt-level unit hit escalation threshold, the surfaced cycle result must state:
- which prompt-level unit triggered the pause
- how many attempts were used
- the dominant root cause
- why another local retry would be invalid
- what Orchestrator guidance is needed

## Future shared-capability note

This policy is owned by `implementation-agent` because it governs the behavior of the execution cycle.

The reusable implementation of review and retry generation is internal to `implementation-agent` in the current architecture. Retry-budget and escalation decisions must remain aligned with this policy even if the internal structure evolves.
