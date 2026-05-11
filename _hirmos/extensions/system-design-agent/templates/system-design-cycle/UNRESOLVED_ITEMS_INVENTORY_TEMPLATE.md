# Unresolved Items Inventory Template

Use this template when generating:
- `/_hirmos/artifacts/context/project/UNRESOLVED_ITEMS_INVENTORY.md`

This artifact follows the unresolved-item contract and system-design-cycle spec. Populate it from producer `Unresolved Items` sections before feed reconciliation.

Inventory coverage summaries must be derived from the actual inventory items listed below.
Do not report subsection extraction counts unless the inventory body contains matching entries.
Each inventory item must preserve its producer artifact and source subsection as the canonical attribution source for all later coverage reporting. Later artifacts must not invent, summarize, or suppress producer extraction counts independently of the inventory body. If an item is explicitly rejected, that rejection must remain attributable to the same producer artifact and subsection so coverage counts and rejected counts can be reconstructed from the inventory body alone.
Do not report subsection extraction counts unless the inventory body contains matching entries.

## Template

# UNRESOLVED_ITEMS_INVENTORY

## Producer contribution: `<artifact-path>`

### Assumptions

#### Inventory Item `<inventory-item-id>`
- Producer artifact: `<artifact-path>`
- Source subsection: `Assumptions`
- Source wording: `<source wording>`
- Normalized summary: `<summary>`
- Item type: `explicit-assumption`
- Why it matters: `<why it matters>`
- Impact area: `<requirements | system-shape | architecture | phasing | reporting | privacy | other>`
- Distinctness note: `<distinct | candidate-merge>`
- Provisional merge target: `<inventory-item-id | none>`

### Open Questions

#### Inventory Item `<inventory-item-id>`
- Producer artifact: `<artifact-path>`
- Source subsection: `Open Questions`
- Source wording: `<source wording>`
- Normalized summary: `<summary>`
- Item type: `explicit-open-question`
- Why it matters: `<why it matters>`
- Impact area: `<requirements | system-shape | architecture | phasing | reporting | privacy | other>`
- Distinctness note: `<distinct | candidate-merge>`
- Provisional merge target: `<inventory-item-id | none>`

## Validation-discovered additions

#### Inventory Item `<inventory-item-id>`
- Producer artifact: `<artifact-path | none>`
- Source subsection: `validation-discovered`
- Source wording: `<source wording>`
- Normalized summary: `<summary>`
- Item type: `validation-discovered-gap`
- Why it matters: `<why it matters>`
- Impact area: `<requirements | system-shape | architecture | phasing | reporting | privacy | other>`
- Distinctness note: `<distinct | candidate-merge>`
- Provisional merge target: `<inventory-item-id | none>`
