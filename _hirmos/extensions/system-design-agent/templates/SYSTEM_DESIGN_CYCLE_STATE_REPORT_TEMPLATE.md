# System Design Cycle State Report Template

Use this template when generating _hirmos/artifacts/context/system-design-agent/system-design-cycle/CYCLE_STATE_REPORT.md (`/_hirmos/artifacts/context/system-design-agent/system-design-cycle/CYCLE_STATE_REPORT.md`).

The report is the downloadable, artifact-grade version of the chat-facing cycle-state output.
It should be readable on its own without needing the chat transcript.

Rules:
- The report must align with the chat-facing cycle-state block.
- Include all sections below.
- Non-gating unresolved items and gated unresolved items must be separated.
- All relevant items must be addressed explicitly.
- Include `Coverage Reconciliation`.
- Include `Rejected Invalid Contributions` when any invalid contributions were rejected from the accepted feed.
- Grouping is allowed only if the original items still appear individually in `Coverage Reconciliation`.
- If an item is intentionally excluded from the grouped summary, the exclusion reason must be stated in `Coverage Reconciliation`.
- Governing reporting behavior lives in `specs/system-design-cycle.spec.md`; this template defines report shape.

## Template

# CYCLE_STATE_REPORT

## Command
`hirmos system-design:system-design-cycle`

## Run state
`paused | completed`

## Cycle state
`paused pending Orchestrator direction | completed`

## Major artifacts created or refined
- `<artifact path>`
- `_hirmos/artifacts/context/project/UNRESOLVED_ITEMS_FEED.md`
- `_hirmos/artifacts/context/project/UNRESOLVED_ITEMS_LEDGER.md`
- `<artifact path>`

This list must be materially complete for operator review.
When applicable, include:
- all materially refined system-level SoTs
- normalized intake artifacts used for the run
- hook-derived or extension-derived planning artifacts that materially affected downstream planning
- refreshed runtime trust artifacts such as `RUN_TRACE.md`, `VALIDATION_TRACE.md`, `CYCLE_STATUS.md`, `RUN_EXECUTION_CONTROLS.md`, and `HOOK_EXECUTION_CONTROL.md`

## Non-gating unresolved items
- `<item>`
  - Classification: `Safe-to-assume | Proceed-with-caution`
  - Handling outcome: `<use assumption | defer and constrain>`
  - Specific handling answer: `<exact assumption or constrained carry-forward answer>`
  - Downgrade justification: `<why this item is not gating despite its category impact>`
  - Visible downstream: `yes | no`

## Gated unresolved items
- `<item>`

## Why they matter
- `<why the item materially matters>`

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

## Producer extraction coverage
- `Producer artifact: <path>`
  - `Derivation source: inventory-body reconstruction`
  - `Assumptions subsection status: <present-with-items | present-empty | missing>`
  - `Assumptions extracted count: <n>`
  - `Assumptions rejected count: <n>`
  - `Open Questions subsection status: <present-with-items | present-empty | missing>`
  - `Open Questions extracted count: <n>`
  - `Open Questions rejected count: <n>`
  - `Producer contribution block present: <yes | no>`
  - `Producer contribution refreshed this run: <yes | no>`
  - `Coverage status: <pass | fail>`

If a producer subsection existed but yielded no inventoried items, the report must make clear whether the subsection was empty or whether items were explicitly rejected. Producer coverage must be derived from actual artifact state and matching producer-scoped contribution blocks, not from optimistic expectation. Coverage counts must be reconstructable from `UNRESOLVED_ITEMS_INVENTORY.md` attribution fields, not estimated from producer rereads or later narrative summaries.

## Coverage Reconciliation
- Feed item ID: `<feed-item-id>`
  - Source inventory item IDs: `<list>`
  - Producer coverage: `<unique producer-artifact set derived from the cited source inventory item IDs>`
  - Origin classification: `assumption | open-question | mixed | validation-discovered`
  - Grouped / normalized under: `<grouped summary item | none>`
  - Severity classification: `Safe-to-assume | Proceed-with-caution | Gating / decision-required | none>`
  - Touches gating-default category: `yes | no`
  - Downgrade justification: `<reason | none>`
  - Handling outcome: `use assumption | ask customer | defer and constrain | none>`
  - Specific handling answer: `<answer | none>`
  - Visible downstream: `yes | no`
  - Final disposition: `<handled | carried-forward | escalated | settled>`
  - Merge note: `<merge note | none>`
  - Exclusion reason: `<reason | none>`

## Control-plane invalidity
- `<none | specific skipped producer contribution, invalid validation claim, or other control-plane failure>`

Use this section to distinguish run-control failures from ordinary business-content unresolvedness. If a required producer contribution step was skipped, record it here explicitly even when the cycle is also paused for content reasons.

## Hook / runtime-pack discovery summary
- Presentation runtime-pack discovery: `<accepted packs | none found | rejected with reasons>`
- Inspected path: `<path>`
- Discovered candidates: `<list | none>`
- Rejected candidates with reasons: `<list | none>`

## Summary
`<short run summary>`

## Next action / rerun condition
`<what the Orchestrator should do next>`

## Advisory note
`<if paused, note that proposed directions are advisory only until accepted or modified>`

## Research assumptions / source-trace summary
- `<research-backed default / source summary or 'No external research-backed defaults were used in this run.'>`