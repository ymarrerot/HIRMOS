# Unresolved Items Ledger Template

Use this template when generating:
- `/_hirmos/artifacts/context/project/UNRESOLVED_ITEMS_LEDGER.md`

This artifact is the long-term historical ledger for unresolved-item lifecycle events across reruns.

## Template

# UNRESOLVED_ITEMS_LEDGER

## Event `<event-id>`
- Run ID: `<run-id>`
- Cycle marker: `<timestamp or cycle marker>`
- Source inventory item IDs: `<list>`
- Reconciliation decision: `<distinct-feed-item | merged-into-existing-item | rejected-invalid | no-longer-current | classified | resolved | constrained | escalated | marked-no-longer-current>`
- Source subsection classification: `<assumption | open-question | mixed | validation-discovered>`
- Notes: `<short note>`
- Merge / rejection rationale: `<note | none>`
