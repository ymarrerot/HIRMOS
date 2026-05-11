# Spec: Retry Prompt

## Purpose

Define the reusable method for generating a bounded retry artifact after implementation review fails.

This Spec is the canonical retry-generation surface for `implementation-agent`. It governs how retry work is derived from failed review findings without broadening scope or weakening review discipline.

This Spec does not own retry budget or escalation thresholds. Those remain in `EXECUTION_RETRY_ESCALATION_POLICY.md`.

## Usage Context

This Spec defines canonical shared loop logic inside `implementation-agent`.

It is used in:
- prompt-level local retry generation inside `implementation-execution-cycle`
- phase-gap recovery follow-up generation when phase review stays repairable inside approved scope

The surrounding workflow differs by review context, but the retry-generation method remains shared.

## Output Location

Retry artifacts belong under:

- `_hirmos/artifacts/ops/retries/<prompt-id>/retry-<n>.md`

## Required Inputs

Retry generation must use:

- the original prompt when applicable
- the failed review artifact
- the review findings
- the relevant phase contract
- the available run summary, evidence, and patch outputs
- relevant SoTs when needed for bounded corrective action

## Local Retry Quality Bar

A retry artifact is locally acceptable only when:

- the root cause is explicit
- corrective scope is minimal and precise
- the generated retry work remains bounded inside the current approved contract
- the corrective action clearly maps to the actual failure
- preserved constraints and must-not-break requirements are explicit

## Input Alignment Rules

Retry generation must stay aligned to:

- the failed execution unit
- the review findings
- the current approved prompt and phase contract
- the actual evidence produced by execution

Retry generation must not:

- silently broaden scope
- restart the whole phase unnecessarily
- invent corrective work unrelated to the actual failure
- use vague rewrite instructions where targeted correction is possible

## Purpose of the retry artifact

A retry artifact is not generic feedback.

It is a bounded corrective execution contract that exists so the local loop can repair a failed execution unit truthfully without pretending that the original failure never happened.

## Retry types

### 1. Prompt Repair Retry

Used when prompt-level review fails but the original execution contract remains fundamentally valid.

Goal:

- fix specific issues in the failed prompt execution
- preserve the original bounded scope

### 2. Phase Gap Recovery Follow-up

Used when phase-level review identifies missing or inconsistent implementation work that can still be repaired inside approved scope.

Goal:

- cover missing required implementation inside the approved phase contract
- preserve phase-bounded corrective scope

Note: phase-gap recovery may produce a new bounded corrective prompt rather than a literal retry of the same prompt id. That broader corrective behavior still must remain inside the approved implementation scope.

## Output Structure

A retry artifact MUST include all of the following:

### 1. Retry Type
- Prompt Repair Retry
- Phase Gap Recovery Follow-up

### 2. Retry Reference
- original prompt id or corrective target id
- retry number when applicable

### 3. Root Cause
Explain what failed and why.

### 4. Failure Evidence
Reference the review findings and supporting evidence that justify the retry.

### 5. Target Scope
State exactly what must be fixed and what remains out of scope.

### 6. Preserved Constraints
State what must remain unchanged, including architecture constraints, delivery-boundary constraints, and prompt-level must-not-break obligations.

### 7. Generated Retry Prompt(s)
Provide the actual bounded retry prompt body to be executed next.

- For Prompt Repair Retry, include one targeted retry prompt.
- For Phase Gap Recovery Follow-up, include the bounded corrective prompt or prompt set needed to repair the uncovered gap.

The generated retry prompt must be executable as written and must not rely on vague implied instructions.

### 8. Corrective Instructions
Provide precise implementation instructions and highlight what changed from the failed attempt.

### 9. Verification Requirements
State what must be re-verified after the retry.

### 10. Coverage Mapping
When the retry repairs a missing requirement or uncovered deliverable, map:
- failed requirement or missing element → corrective work item

## Strict Rules

- Fix only what is broken.
- Keep corrective work minimal and targeted.
- Do not redo the entire phase when a bounded corrective retry is sufficient.
- Do not default to broad rewrites when a precise repair is possible.
- Do not introduce new scope.
- Do not hide the original failure.
- Do not generate a retry artifact that cannot be reviewed against explicit evidence.

## Local Review Relationship

This Spec depends on strict review behavior.

A retry should be generated only from a real failed review result grounded in evidence. If the review result is weak, vague, or insufficiently evidenced, improve the review finding first instead of generating a weak retry.

## Failure / Repair Expectation

If the generated retry is broad, weakly targeted, or disconnected from the actual failure:

- refine it before use
- do not treat vague retry generation as acceptable implementation-loop behavior

## Canonical-loop rule

This Spec defines canonical retry-generation logic for `implementation-agent`. Entrypoints and other Specs should reference this file rather than re-describing retry semantics in weaker or duplicated form.
