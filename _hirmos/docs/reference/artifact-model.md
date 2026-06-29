# Artifact Model

HIRMOS artifacts exist to make AI-assisted software work reviewable and continuous.

The artifact model follows three rules:

```text
Create the smallest safe surface.
Keep one canonical owner for each fact.
Point or derive instead of duplicating mutable status.
```

## Active session layout

```text
_hirmos/session/
  SESSION_STATE.json
  SESSION_LEDGER.md
  SESSION_SCOPE.md
  unresolved-items.md          # when material unresolved items exist
  DESIGN.md                    # when separate Design authority is justified
  EVIDENCE.md                  # when evidence volume justifies it
  bootstrap/
  implementation-units/        # when IU mode applies
```

- `SESSION_STATE.json`: minimal machine state and derived command-state cache.
- `SESSION_LEDGER.md`: compact command/gate ledger and evidence pointers.
- `SESSION_SCOPE.md`: active session authority.
- `unresolved-items.md`: governed blockers, assumptions, technical-review items, and carry-forward items.
- `implementation-units/IU-xx.md`: IU authority, execution record, evidence, review, and retry records.

## Delivery layout

```text
_hirmos/system/delivery/
  DELIVERY_PLAN.md
  <delivery-id>/
    DELIVERY_SCOPE.md
    unresolved-items.md
    phases/
      PHASE-xx.md
```

- `DELIVERY_PLAN.md`: project delivery roadmap/register and pointer surface.
- `DELIVERY_SCOPE.md`: stable authority for one delivery/release.
- `PHASE-xx.md`: phase authority created just in time.
- Delivery unresolved register: durable delivery-level unresolved items.

Delivery artifacts should not mirror the same mutable completion status in several places. Completion and concordance should be derived from source artifacts, accepted close evidence, and archive/current-state pointers.

## Accepted-state layout

```text
_hirmos/system/accepted-state/
  CURRENT_SYSTEM_STATE.md
  CARRY_FORWARD.md             # when accepted carry-forward exists
```

`CURRENT_SYSTEM_STATE.md` is durable accepted-state navigation. It points to accepted source artifacts instead of duplicating detailed delivery/session/evidence content.

## History layout

```text
_hirmos/system/history/sessions/<session-id>/
```

Archived session artifacts preserve what happened. Archive content is evidence and history; it becomes accepted current state only through close/update control.

## Work-shape activation

| Work shape | Artifacts created by default |
|---|---|
| Small bounded work | only minimal session surfaces needed for the request |
| Session implementation | `SESSION_SCOPE.md`, `SESSION_LEDGER.md`, unresolved register when needed, IU/evidence surfaces when needed |
| Delivery baseline | delivery plan/scope/unresolved register; no future phase/session artifacts by default |
| Phase/session work | next phase file and session scope just in time |
| IU implementation | IU files during IU Planning, before IU Execution |

## Optional artifacts

Optional artifacts should be created just in time. Empty placeholder artifacts create synchronization burden and can mislead later model actions.

## Source authority rule

If a summary, pointer index, or derived cache conflicts with a source artifact, the source artifact wins. The stale derived surface should be regenerated or validation should fail closed.


## Source inputs

Raw source inputs live under `_hirmos/inputs/`, including `inputs/uploads`, prototypes, and references. Source inputs are not accepted authority until HIRMOS reconciles them into governed scope, design, delivery, or accepted-state artifacts.

## Active session artifacts

Active session artifacts are created under `_hirmos/session/` only when governed work requires them.

## Accepted system state

Accepted system state lives under `_hirmos/system/accepted-state/` and points to accepted source artifacts without duplicating their full content.


## Archive history vs accepted state

Archive history preserves what happened in a closed session. Accepted state records what HIRMOS accepted as durable current truth. A file in history is not automatically accepted current state unless close/update control points to it as accepted.


Closed session archives may include `ARCHIVE_MANIFEST.md` during close/archive to list archived sources and evidence pointers.


Delivery roadmap/register lives in `DELIVERY_PLAN.md`. Delivery scope authority lives in `<delivery-id>/DELIVERY_SCOPE.md`.
