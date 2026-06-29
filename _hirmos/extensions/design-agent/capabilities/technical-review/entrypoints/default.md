# technical-review

## Execution Contract

### Purpose

Create reviewer-facing technical assumption, risk, decision, and inspection material without overloading Domain Expert output.

### Produces

- `_hirmos/session/DESIGN.md`
- `_hirmos/session/DESIGN.md technical assumptions summary`
- `_hirmos/session/unresolved-items.md technical-review items`
- `_hirmos/session/SESSION_LEDGER.md technical-review control updates`

### Terminal States

- COMPLETED — technical review material is recorded or explicitly not applicable.
- NEEDS_USER_DECISION — technical risk creates a user-owned domain/risk/resource decision.
- BLOCKED — technical evidence is insufficient.
- ROUTE_BACK_REQUIRED — technical review exposes missing system-state or Design evidence.
- NOT_APPLICABLE — no material technical assumptions or review path is needed.

## Activation triggers

- technical assumptions or tradeoffs exist
- security/data/integration/performance/migration/preservation risk exists
- third-party review pointer is needed
- canonical user-facing output should progressively disclose technical detail

## Required inputs

- `_hirmos/session/DESIGN.md`
- `_hirmos/session/DESIGN.md`
- `_hirmos/session/unresolved-items.md`
- stack/project-type evidence when applicable

## Execution controls contributed

- technical-review control
- Design control
- snapshot-backed checkpoint control

## Method

This capability inherits shared extension rules from `_hirmos/extensions/design-agent/entrypoints/default.md`; confirm the parent extension entrypoint has been read before executing this capability.

## Required behavior

Apply the shared Required behavior baseline in `_hirmos/core/authority/SHARED_CAPABILITY_CONTROLS.md`. This entrypoint retains only capability-specific obligations below; do not duplicate the shared checklist here.

## Capability-specific obligations

- Third-party review pointers.
- challenge/change path.

## Canonical interaction posture visibility

Apply the shared interaction-posture rules in `_hirmos/core/authority/SHARED_CAPABILITY_CONTROLS.md` and the canonical posture authority at `_hirmos/core/authority/INTERACTION_POSTURE.md`. Surface rich governed pause/checkpoint outputs when they support user decision-making; do not reduce checkpoint clarity to save tokens.

## Unresolved-item producer obligation

Apply the shared unresolved-item producer obligation in `_hirmos/core/authority/SHARED_CAPABILITY_CONTROLS.md` and the owning protocol: this capability MUST apply `_hirmos/core/protocol/UNRESOLVED_ITEMS.md`. It must record exactly one producer outcome in the focus-appropriate unresolved register: `ITEMS_FOUND`, `NONE_FOUND`, `NOT_APPLICABLE`, or `BLOCKED`. When items exist, preserve current status, downstream impact, and revalidation point.

## Runtime integration responsibilities

Apply the shared runtime-integration responsibilities in `_hirmos/core/authority/SHARED_CAPABILITY_CONTROLS.md` and `_hirmos/core/protocol/RUNTIME_INTEGRATION_AND_PRODUCTION_READINESS.md`. Keep detailed evidence in the owning IU, `EVIDENCE.md`, or accepted-state/archive source; this entrypoint should point rather than duplicate.

## PROD-L8.11 Delivery-Baseline Optional Authority Location

When `SESSION_STATE.json.session_focus = delivery_baseline`, the active authority is delivery-level. Optional requirements/design authority must be located under `_hirmos/system/delivery/<delivery-id>/` only:

- `_hirmos/system/delivery/<delivery-id>/REQUIREMENTS.md` when separate delivery-level requirements authority is justified.
- `_hirmos/system/delivery/<delivery-id>/DESIGN.md` when separate delivery-level design authority is justified.

During `delivery_baseline`, HIRMOS must not create, update, list, or depend on `_hirmos/session/REQUIREMENTS.md` or `_hirmos/session/DESIGN.md`. If separate optional authority is not justified, requirements and design decisions remain inside `DELIVERY_SCOPE.md` only. Session-level optional authority artifacts become applicable only after the flow advances to a bounded `phase_session_baseline` or `session_baseline` focus.
