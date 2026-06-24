# requirements-design

## Execution Contract

### Purpose

Convert User Request inputs, source materials, prototype findings, and system-state evidence into governed requirements authority.

### Produces

- `_hirmos/session/DESIGN.md governed requirements section`
- `_hirmos/session/unresolved-items.md updates`
- `_hirmos/session/SESSION_EXECUTION.md Design control updates`

### Terminal States

- COMPLETED — governed requirements are recorded and separated from raw inputs.
- NEEDS_USER_DECISION — user-owned requirement decision blocks safe Design or readiness.
- BLOCKED — required system-state or source evidence is missing.
- ROUTE_BACK_REQUIRED — requirements analysis reveals missing or contradictory system-state understanding.
- NOT_APPLICABLE — request does not require requirements authority changes.

## Activation triggers

- request requires requirements authority
- source inputs include requirement candidates
- prototype/source materials imply behavior that must become governed requirements
- Design must produce or revise requirements before downstream design or implementation

## Required inputs

- `_hirmos/session/SESSION_SCOPE.md`
- `_hirmos/session/DESIGN.md source matrix when source inputs exist`
- `_hirmos/inputs/`, especially `_hirmos/inputs/uploads/`, when raw source files are present`
- `_hirmos/session/DESIGN.md source matrix when prototype/POC inputs exist`
- `_hirmos/session/DESIGN.md`
- `_hirmos/session/unresolved-items.md`

## Execution controls contributed

- Design control
- unresolved-item control
- snapshot-backed checkpoint control

## Method

This capability inherits shared extension rules from `_hirmos/extensions/design-agent/entrypoints/default.md`; confirm the parent extension entrypoint has been read before executing this capability.

## Requirements intake preservation rule

When converting intake artifacts into governed requirements, preserve distinctions between confirmed source signals, assumptions, research-backed defaults, declared delivery targets, proposed delivery targets, open questions, pending confirmation items, prototype observed behavior, prototype intended behavior, prototype variants, and prototype conflicts.

If multiple prototype inputs exist, require prototype-set reconciliation in `_hirmos/session/DESIGN.md` before Design relies on prototype-derived requirements. If reconciliation is missing or blocked, set Design to `ROUTE_BACK_REQUIRED`, `NEEDS_USER_DECISION`, or `BLOCKED`.

Workflow-heavy requirements must not remain vague catalog rows. Add detailed requirement records or route unresolved behavior into `unresolved-items.md`.

## Required behavior

1. Confirm and record this capability decision under `_hirmos/core/protocol/CAPABILITY_ROUTING.md` in `_hirmos/session/SESSION_EXECUTION.md`.
2. Instantiate or update only the canonical artifacts required by the active request path.
3. Produce non-placeholder content before claiming completion.
4. Preserve lifecycle ownership boundaries; route back in `SESSION_EXECUTION.md` when evidence invalidates an earlier stage.
5. Apply the extension method and this capability-specific execution surface; do not execute from chat summaries or raw inputs alone.


## Capability-specific obligations

- Separate requirement inputs from governed requirements authority.
- Map each material requirement to source evidence and system-state findings.

## Interaction-mode visibility

Use the active interaction mode from `_hirmos/core/authority/INTERACTION_MODES.md` and the parent extension default entrypoint visibility rule.

- `domain_expert`: surface only user-owned decisions, blockers, readiness/completion status, and concise artifact pointers.
- `technical_supervisor`: surface capability result, assumptions, artifacts/evidence, and review implications.
- `framework_diagnostics`: surface activation reason, entrypoint path, controls, artifacts, unresolved-item contribution, route-back decisions, and terminal-state basis.

## Unresolved-item producer obligation

This capability is an unresolved-item producer and MUST apply `_hirmos/core/protocol/UNRESOLVED_ITEMS.md`.

Before marking the capability complete, record exactly one producer outcome in the focus-appropriate unresolved register selected by `SESSION_STATE.json.session_focus`: `ITEMS_FOUND`, `NONE_FOUND`, `NOT_APPLICABLE`, or `BLOCKED`.

Record full item fields in the selected unresolved register, including current status, downstream impact, and revalidation point; do not duplicate the full field schema in this entrypoint.

## Runtime integration responsibilities

When material runtime services are involved, follow `_hirmos/core/protocol/RUNTIME_INTEGRATION_AND_PRODUCTION_READINESS.md`.

Record or consume `_hirmos/session/DESIGN.md` / `_hirmos/session/EVIDENCE.md` as required by execution controls.

Do not claim fixture/mock/boundary/local/production integration levels beyond what the active artifacts and evidence support.

## Requirements output

Requirements Design must create or update `_hirmos/session/REQUIREMENTS.md` when material requirements exist.

Minimum required work:

- classify all material source inputs;
- normalize requirements into stable IDs;
- preserve source traceability;
- separate functional, workflow/state, data/domain, UI/UX, integration, security/audit, non-functional, acceptance, non-goal, and constraint requirements;
- record gated/unresolved requirements;
- hand off requirement IDs to Delivery Plan mapping.

Do not treat raw `requirements.txt`, prototype ingestion findings, or UI notes as Design authority until represented in `REQUIREMENTS.md`.

## PROD-L8.11 Delivery-Baseline Optional Authority Location

When `SESSION_STATE.json.session_focus = delivery_baseline`, the active authority is delivery-level. Optional requirements/design authority must be located under `_hirmos/system/delivery/<delivery-id>/` only:

- `_hirmos/system/delivery/<delivery-id>/REQUIREMENTS.md` when separate delivery-level requirements authority is justified.
- `_hirmos/system/delivery/<delivery-id>/DESIGN.md` when separate delivery-level design authority is justified.

During `delivery_baseline`, HIRMOS must not create, update, list, or depend on `_hirmos/session/REQUIREMENTS.md` or `_hirmos/session/DESIGN.md`. If separate optional authority is not justified, requirements and design decisions remain inside `DELIVERY_SCOPE.md` only. Session-level optional authority artifacts become applicable only after the flow advances to a bounded `phase_session_baseline` or `session_baseline` focus.
