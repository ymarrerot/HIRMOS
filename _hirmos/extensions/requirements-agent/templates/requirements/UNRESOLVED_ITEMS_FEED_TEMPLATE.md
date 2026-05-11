# Unresolved Items Feed Template

Use this template when generating:
- `/_hirmos/artifacts/context/project/UNRESOLVED_ITEMS_FEED.md`

This artifact is the current-run canonical unresolved-item register for `requirements` after inventory and reconciliation.

## Template

# UNRESOLVED_ITEMS_FEED

## Command
`hirmos requirements`

## Run scope
`current-run canonical unresolved-item register`

## Accepted items

### Item `<feed-item-id>`
- Title / summary: `<summary>`
- Severity classification: `<Safe-to-assume | Proceed-with-caution | Gating / decision-required>`
- Why it matters: `<why it matters>`
- Source inventory item IDs: `<list>`
- Producer coverage: `<derived unique producer-artifact set from the cited source inventory item IDs>`
- Origin classification: `<assumption | open-question | mixed | validation-discovered>`
- Producer coverage derivation rule: `Do not list producer coverage that cannot be reconstructed from the cited source inventory items in UNRESOLVED_ITEMS_INVENTORY.md.`
- Merge note: `<merge note | none>`
