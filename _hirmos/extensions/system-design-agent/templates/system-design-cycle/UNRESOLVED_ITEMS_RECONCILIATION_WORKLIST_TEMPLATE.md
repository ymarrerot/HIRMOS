# Unresolved Items Reconciliation Worklist Template

Use this template when generating:
- `/_hirmos/artifacts/context/project/UNRESOLVED_ITEMS_RECONCILIATION_WORKLIST.md`

This artifact follows the unresolved-item contract and system-design-cycle spec.

## Template

# UNRESOLVED_ITEMS_RECONCILIATION_WORKLIST

## Reconciliation coverage check
- Inventory item IDs in scope: `<list>`
- Reconciled inventory item IDs: `<list>`
- Orphaned inventory item IDs: `<list | none>`
- Duplicate-reconciled inventory item IDs: `<list | none>`
- Unknown inventory item IDs referenced by reconciliation: `<list | none>`
- Coverage status: `<pass | fail>`
- Coverage note: `<note>`

### Reconciliation Entry `<entry-id>`
- Source inventory item IDs: `<list>`
- Disposition: `<distinct-feed-item | merged-into-existing-item | rejected-invalid | no-longer-current>`
- Final target ID: `<feed-item-id | none>`
- Justification: `<justification>`
- Merge note: `<merge note | none>`
- Merge-audit shared decision: `<single shared unresolved decision | none>`
- Merge-audit decision domain: `<identity/access | workflow/operations | reporting/export | architecture/deployment | privacy/compliance | readiness/rollout | other | none>`
- Merge-audit concrete shared customer question: `<single concrete customer question that covers all merged items | none>`
- Merge-audit concrete Orchestrator decision: `<single concrete Orchestrator decision that covers all merged items | none>`
- Merge-audit distinctness check: `<why these items are not materially distinct enough to stand alone | none>`
- Merge-audit information preserved: `<what remains visible after merging | none>`
- Merge-audit why not separate: `<why separate feed items would be redundant rather than clearer | none>`
- Rejection / no-longer-current note: `<note | none>`

Merge note: Broad justifications such as `they jointly determine readiness`, `they all affect operational truth`, or `they are all gating` are not sufficient by themselves. A valid merged entry must also show one concrete shared customer question, one concrete Orchestrator decision, or one clearly bounded primary decision domain.
