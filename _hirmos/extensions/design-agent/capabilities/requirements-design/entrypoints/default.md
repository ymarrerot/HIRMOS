# requirements-design

## Execution Contract

### Purpose

Convert User Request inputs, source materials, prototype findings, and system-state evidence into governed requirements authority.

### Produces

- `_hirmos/session/DESIGN.md governed requirements section`
- `_hirmos/session/unresolved-items.md updates`
- `_hirmos/session/SESSION_LEDGER.md Design control updates`

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

Apply the shared Required behavior baseline in `_hirmos/core/authority/SHARED_CAPABILITY_CONTROLS.md`. This entrypoint retains only capability-specific obligations below; do not duplicate the shared checklist here.

## Capability-specific obligations

- Separate requirement inputs from governed requirements authority.
- Map each material requirement to source evidence and system-state findings.

## Canonical interaction posture visibility

Apply the shared interaction-posture rules in `_hirmos/core/authority/SHARED_CAPABILITY_CONTROLS.md` and the canonical posture authority at `_hirmos/core/authority/INTERACTION_POSTURE.md`. Surface rich governed pause/checkpoint outputs when they support user decision-making; do not reduce checkpoint clarity to save tokens.

## Unresolved-item producer obligation

Apply the shared unresolved-item producer obligation in `_hirmos/core/authority/SHARED_CAPABILITY_CONTROLS.md` and the owning protocol: this capability MUST apply `_hirmos/core/protocol/UNRESOLVED_ITEMS.md`. It must record exactly one producer outcome in the focus-appropriate unresolved register: `ITEMS_FOUND`, `NONE_FOUND`, `NOT_APPLICABLE`, or `BLOCKED`. When items exist, preserve current status, downstream impact, and revalidation point.

## Runtime integration responsibilities

Apply the shared runtime-integration responsibilities in `_hirmos/core/authority/SHARED_CAPABILITY_CONTROLS.md` and `_hirmos/core/protocol/RUNTIME_INTEGRATION_AND_PRODUCTION_READINESS.md`. Keep detailed evidence in the owning IU, `EVIDENCE.md`, or accepted-state/archive source; this entrypoint should point rather than duplicate.

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
