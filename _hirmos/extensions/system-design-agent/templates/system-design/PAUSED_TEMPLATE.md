# System Design Paused Template

Use this template for final surfaced `paused` output from `system-design-agent:system-design`.

All required sections below must appear in the final surfaced output.

## Command

`hirmos system-design`

## Run state

`paused`

## Requirements artifacts consumed

- `<artifact path>`

If required Requirements artifacts are missing or unusable, state that explicitly.

## Major artifacts created or refined

- `<artifact path>`
- `<artifact path>`

This list must be materially complete for operator review.

## Step state

`paused pending Orchestrator direction`

## Non-gating unresolved items

- `<item>`
  - Classification: `Safe-to-assume | Proceed-with-caution`
  - Handling outcome: `<use assumption | defer and constrain>`
  - Specific handling answer: `<exact assumption or constrained carry-forward answer>`
  - Visible downstream: `yes | no`

## Gated unresolved items

- `<item>`

Any unresolved item that materially affects a gating-default category should appear here unless the run has recorded an explicit downgrade justification strong enough to support non-gating treatment.

## Why they matter

- `<why this item materially matters>`

## Allowed outcomes

- `use assumption`
- `ask customer`
- `defer and constrain`
- `repair missing Requirements artifacts`

## Proposed Orchestrator direction

- `<item>`: `<use assumption | ask customer | defer and constrain | repair missing Requirements artifacts>`
  - Suggested direction: `<short recommendation>`
  - Rationale: `<why this is the recommended direction>`

## Continuation options

- `Accept all proposed directions`
- `Modify one or more proposed directions`
- `Ask for customer-question drafting for selected items`
- `Run or repair hirmos requirements`

## Summary

`<short run summary>`

## Next action / rerun condition

`<what the Orchestrator should do next before rerunning or continuing System Design>`

## Updated working copy zip

`<artifact package path or generated download link>`
