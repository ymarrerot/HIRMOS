# System Design Cycle Completed Template

Use this template for final surfaced `completed` output from `system-design-agent:system-design-cycle`.

All required sections below must appear in the final surfaced output.

## Command

`hirmos system-design:system-design-cycle`

## Run state

`completed`

## Major artifacts created or refined

- `<artifact path>`
- `<artifact path>`

This list must be materially complete for operator review.
When applicable, include:
- all materially refined system-level SoTs
- normalized intake artifacts used for the run
- hook-derived or extension-derived planning artifacts that materially affected downstream planning
- refreshed runtime trust artifacts such as `RUN_TRACE.md`, `VALIDATION_TRACE.md`, `CYCLE_STATUS.md`, `RUN_EXECUTION_CONTROLS.md`, and `HOOK_EXECUTION_CONTROL.md`

## Decisions absorbed or important grounding outcome

- `<decision or grounding result>`

## Remaining non-gating limitations

- `<non-gating limitation>`
  - If this limitation touches a gating-default category, include why it is non-gating for this run and why completion is still honest.

## Why completion is still honest

`<why the cycle can truthfully complete despite the listed non-gating limitations, or state that no material non-gating limitations remain. If completion depends on any downgrade-based non-gating treatment for a gating-default category, explain that downgrade logic explicitly.>`

## Summary

`<short run summary>`

## Next action

`<what the Orchestrator should do next>`

## Updated working copy zip

`<artifact label>: <relative-or-repository-artifact-path>`
