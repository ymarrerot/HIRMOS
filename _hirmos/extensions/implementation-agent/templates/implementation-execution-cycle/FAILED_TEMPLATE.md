# Failed Template — implementation-execution-cycle

Use this template for `implementation-agent:implementation-execution-cycle` when the cycle cannot reach a governable `completed` or `paused` result because a command-critical grounding, execution, validation, or phase-review condition broke beyond the cycle's truthful recovery path.
All required sections below must appear in the final surfaced failed output.

## Command

`hirmos implementation:implementation-execution-cycle`

## Selected phase

State the selected phase exactly.

## Run state

`failed`

## Execution point reached

State where the cycle reached before failing.

## Major artifacts created or refined

List any artifacts that were still created or materially refined before failure.

## Validation or phase review state at failure

Report the validation or phase review state truthfully at the time of failure.

## Failure cause

State the honest failure cause concisely.

## Why pause is not the honest state

Explain why `paused` would be misleading in this case.

## Recovery already attempted

List the recovery already attempted before the cycle concluded in `failed` state.

## What would be required to recover later

State what would have to change before a later recovery attempt could be honest.

## Summary

Provide a concise truthful failure summary.

## Next action

State the next recommended Orchestrator action.

## Updated working copy zip

Include the surfaced download link for the updated full working copy when packaging is available.
