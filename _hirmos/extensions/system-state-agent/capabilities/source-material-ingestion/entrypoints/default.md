# source-material-ingestion

## Execution Contract

### Purpose

Classify uploaded or referenced source material and extract focus signals without turning source material into governed authority.

### Produces

- `_hirmos/session/DESIGN.md`
- `_hirmos/session/unresolved-items.md` updates when inputs conflict, are unreadable, or create material uncertainty
- `_hirmos/session/SESSION_EXECUTION.md` updates

### Terminal States

- COMPLETED — source materials inventoried with type, relevance, focus signals, conflicts, and handoff notes.
- NEEDS_USER_DECISION — source intent, priority, or conflict blocks safe Design.
- BLOCKED — required material cannot be read, classified, or reconciled.
- NOT_APPLICABLE — no source materials beyond the User Request are present.

## Activation triggers

- Uploaded files, notes, tickets, screenshots, docs, existing specs, code excerpts, or referenced source materials exist.
- Request intake identifies source materials that may affect Understand System State or Design.

## Required inputs

- `_hirmos/session/SESSION_CONTRACT.md`
- Available source materials or explicit statement that no extra source materials exist.

## Execution controls contributed

- source input control
- source-material classification control
- unresolved-item control when needed

## Method

1. Create the Source Material Inventory by inventorying every source material with location, type, readable status, and relevance.
2. Classify material type: requirement notes, prototype, POC, screenshot, ticket, existing spec, documentation, codebase evidence, external reference, conversation instruction, or other.
3. Mark whether the material is primary, supporting, conflicting, stale, unreadable, or not applicable.
4. Extract focus signals for Understand System State.
5. Separate direct relevance from indirect relevance.
6. Identify conflicts between source materials and between source material and the User Request.
7. Record source priority only when supported; otherwise create an unresolved item.
8. Use Prototype / POC Routing for prototypes/POCs/screenshots/generated app inputs to `prototype-ingestion` when present.
9. Record source-material handoff to Understand System State and Design.
10. Preserve intake classifications for confirmed source signals, assumptions, research-backed defaults, declared delivery targets, proposed delivery targets, open questions, and pending confirmation items. Do not collapse these into accepted requirements during source-material ingestion.

## Required behavior

1. Confirm and record this capability decision under `_hirmos/core/protocol/CAPABILITY_ROUTING.md` in `_hirmos/session/SESSION_EXECUTION.md`.
2. Instantiate or update only the canonical artifacts required by the active request path.
3. Produce non-placeholder content before claiming completion.
4. Preserve lifecycle ownership boundaries; route back in `SESSION_EXECUTION.md` when evidence invalidates an earlier stage.
5. Apply the extension method and this capability-specific contract; do not execute from chat summaries or raw inputs alone.

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

When this capability encounters project-type or stack evidence, record material findings in `DESIGN.md` / `SESSION_CONTRACT.md`, `stack-resolution.json` for machine-readable stack routing, or `SESSION_EXECUTION.md` as required by active controls.

User Request labels and prototype technology signals are focus evidence, not final classification authority.
