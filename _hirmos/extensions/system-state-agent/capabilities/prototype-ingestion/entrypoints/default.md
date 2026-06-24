# prototype-ingestion

## Execution Contract

### Purpose

Treat prototypes, POCs, screenshots, generated apps, or demo code as first-class evidence while separating observed behavior from intended behavior and authority.

### Produces

- `_hirmos/session/DESIGN.md`
- `_hirmos/session/DESIGN.md` focus contributions
- `_hirmos/session/unresolved-items.md` updates for prototype conflicts, unclear intent, or preservation risks
- `_hirmos/session/SESSION_EXECUTION.md` updates

### Terminal States

- COMPLETED — prototype evidence extracted with observed/intended/unknown separation and handoff notes.
- NEEDS_USER_DECISION — prototype intent conflicts with request or cannot be interpreted safely.
- BLOCKED — prototype materials are unavailable, unreadable, or too incomplete for reliable extraction.
- NOT_APPLICABLE — no prototype or POC signals exist.

## Activation triggers

- Source inputs include a prototype, POC, demo app, screenshot flow, generated code, exploratory implementation, or AI-generated app.
- Source-material ingestion identifies prototype-like material.
- User Request references “prototype,” “POC,” “demo,” “existing generated app,” “screenshot,” “make this real,” or similar signals.

## Required inputs

- `_hirmos/session/SESSION_SCOPE.md`
- `_hirmos/session/DESIGN.md` when source material exists
- Available prototype/POC materials or an explicit unreadable/missing status

## Execution controls contributed

- prototype/POC input control
- system-state control
- unresolved-item control when needed

## Method

1. Identify prototype artifacts and their source locations.
2. Classify prototype type: screenshot flow, clickable prototype, generated app, exploratory code, mock data, architecture sketch, API sample, or other.
3. Separate observed behavior from intended behavior stated by the user or source materials.
4. Extract user-facing workflows, screens, states, data concepts, integrations, roles, permissions, and non-functional signals.
5. Identify Implementation Details That Are Evidence Only and must not become architecture by accident.
6. Identify conflicts between prototype behavior, User Request, existing system state, and other source materials.
7. Identify preservation expectations when a prototype already has user-visible behavior the user may expect to keep.
8. Record prototype-derived focus areas for Understand System State and Design.
9. Create unresolved items for unclear intent, conflicting behavior, missing domain rules, or prototype-to-production risks.
10. Multiple-prototype normalization path: when more than one prototype candidate exists, record prototype-specific findings for each prototype and then complete the Prototype Set Reconciliation sections: shared core signals, business logic consolidation, data contract consolidation, integration consolidation, workflow consolidation, conflict register, variant register, and normalized requirement candidates.
11. If multiple prototypes exist and prototype-set reconciliation cannot be completed, set the capability to `BLOCKED` or `NEEDS_USER_DECISION`; do not let requirements normalization proceed as if the set reconciliation were optional.

## Required behavior

1. Confirm and record this capability decision under `_hirmos/core/protocol/CAPABILITY_ROUTING.md` in `_hirmos/session/SESSION_EXECUTION.md`.
2. Instantiate or update only the canonical artifacts required by the active request path.
3. Produce non-placeholder content before claiming completion.
4. Preserve lifecycle ownership boundaries; route back in `SESSION_EXECUTION.md` when evidence invalidates an earlier stage.
5. Apply the extension method and this capability-specific execution surface; do not execute from chat summaries or raw inputs alone.

## Interaction-mode visibility

Use the active interaction mode from `_hirmos/core/authority/INTERACTION_MODES.md` and the parent extension default entrypoint visibility rule.

- `domain_expert`: surface only user-owned decisions, blockers, readiness/completion status, and concise artifact pointers.
- `technical_supervisor`: surface capability result, assumptions, artifacts/evidence, and review implications.
- `framework_diagnostics`: surface activation reason, entrypoint path, controls, artifacts, unresolved-item contribution, route-back decisions, and terminal-state basis.

## Unresolved-item producer obligation

This capability is an unresolved-item producer and MUST apply `_hirmos/core/protocol/UNRESOLVED_ITEMS.md`.

Before marking the capability complete, record exactly one producer outcome in `_hirmos/session/unresolved-items.md`: `ITEMS_FOUND`, `NONE_FOUND`, `NOT_APPLICABLE`, or `BLOCKED`.

Record full item fields in `unresolved-items.md`, including current status, downstream impact, and revalidation point; do not duplicate the full field schema in this entrypoint.

## Project Context and Stack Classification

When this capability encounters project-type or stack evidence, record material findings in `DESIGN.md` / `SESSION_SCOPE.md`, `stack-resolution.json` for machine-readable stack routing, or `SESSION_EXECUTION.md` as required by active controls.

User Request labels and prototype technology signals are focus evidence, not final classification authority.
