# System Design Cycle Paused Template

Use this template for final surfaced `paused` output from `system-design-agent:system-design-cycle`.

All required sections below must appear in the final surfaced output.

## Command

`hirmos system-design:system-design-cycle`

## Run state

`paused`

## Major artifacts created or refined

- `<artifact path>`
- `<artifact path>`

This list must be materially complete for operator review.
When applicable, include:
- all materially refined system-level SoTs
- normalized intake artifacts used for the run
- hook-derived or extension-derived planning artifacts that materially affected downstream planning
- refreshed runtime trust artifacts such as `RUN_TRACE.md`, `VALIDATION_TRACE.md`, `CYCLE_STATUS.md`, `RUN_EXECUTION_CONTROLS.md`, and `HOOK_EXECUTION_CONTROL.md`

## Cycle state

`paused pending Orchestrator direction`

## Non-gating unresolved items

- `<item>`
  - Classification: `Safe-to-assume | Proceed-with-caution`
  - Handling outcome: `<use assumption | defer and constrain>`
  - Specific handling answer: `<exact assumption or constrained carry-forward answer>`
  - Visible downstream: `yes | no`

## Gated unresolved items

- `<item>`

Any unresolved item that materially affects a gating-default category should appear here unless the cycle has recorded an explicit downgrade justification strong enough to support non-gating treatment.

## Why they matter

- `<why this item materially matters>`

## Allowed outcomes

- `use assumption`
- `ask customer`
- `defer and constrain`

## Proposed Orchestrator direction

- `<item>`: `<use assumption | ask customer | defer and constrain>`
  - If the proposed direction is `use assumption` or `defer and constrain`, include:
    - Suggested direction: `<short recommendation>`
    - Rationale: `<why this is the recommended direction>`
  - If the proposed direction is `ask customer`, include:
    - Question to confirm: `<specific question the Orchestrator should confirm>`
    - Why this must be asked: `<why this cannot be assumed safely>`

## Continuation options

- `Accept all proposed directions`
- `Modify one or more proposed directions`
- `Ask for customer-question drafting for selected items`

## Summary

`<short run summary>`

## Next action / rerun condition

`<what the Orchestrator should do next>`

## Updated working copy zip

`<artifact label>: <relative-or-repository-artifact-path>`
