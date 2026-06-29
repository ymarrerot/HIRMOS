# system-state-agent

Bundled HIRMOS extension. Core owns lifecycle authority; this extension provides bounded capabilities for `User Request`, `Understand System State`, and `Update System State` responsibilities.

## Runtime identity

System State Agent

## Supported lifecycle responsibilities

- request intake and source-input handling before governed work advances;
- Understand System State through general and request-focused system understanding;
- Update System State after reviewed outcomes are ready to become durable accepted state.

## Capabilities

- `request-intake`
- `source-material-ingestion`
- `prototype-ingestion`
- `understand-system-state`
- `update-system-state`

## Responsibility boundary

This extension does not define the lifecycle. It executes inside Core lifecycle, command, capability-routing, artifact, unresolved-item, execution-control, and validation rules.

This extension may discover request signals, current-state evidence, source-material conflicts, prototype evidence, current-state unknowns, accepted-state update candidates, and carry-forward items.

It must not create governed requirements, Design authority, Implementation authorization, or implementation evidence. Those belong to later lifecycle responsibilities.

## Method summary

The system-state-agent method is:

1. capture the User Request as source input, not authority;
2. inventory source materials and classify their relevance;
3. ingest prototypes or POCs as evidence when present;
4. produce general system understanding sufficient to avoid tunnel vision;
5. produce focused system understanding guided by the User Request and source inputs;
6. separate observed, inferred, assumed, unknown, blocked, and not-applicable evidence;
7. contribute unresolved items when uncertainty affects Design, Implementation, or Update System State;
8. update durable accepted system state only after reviewed outcomes are ready and close controls allow it.

## Rule

Capabilities execute only when selected by Core command, lifecycle, capability-routing, and execution-control rules. Capability completion must be recorded in `_hirmos/session/SESSION_LEDGER.md`.


## Canonical interaction posture

System-state-agent follows the single HIRMOS user-facing posture in `_hirmos/core/authority/INTERACTION_POSTURE.md`: simple by default, transparent by design, rigorous underneath, and progressively disclosed. User-facing summaries should include artifact paths when referencing current-state, unresolved-item, carry-forward, evidence, archive, or accepted-state claims.
