# Artifact Model Reference

HIRMOS uses a strict-necessity, scope-authority artifact model.


## Scope authority model

The canonical target names for new authority surfaces are:

```text
SESSION_SCOPE.md       # active session authority
DELIVERY_SCOPE.md      # one durable delivery/release authority
REQUIREMENTS.md        # conditional independent requirements authority only
DESIGN.md              # conditional independent design authority only
```

`REQUIREMENTS.md` is conditional independent requirements authority. It is not part of the default implementation-session surface; new session authority uses `SESSION_SCOPE.md`.

## Active session artifacts

Active session artifacts are governed by the strict-necessity surface below.

## Active session surface

New active-session artifacts should exist only when they are strictly necessary for one of these purposes:

- authority;
- machine state;
- evidence;
- gating;
- continuity;
- audit/history.

If content is useful but does not need to exist as a separate artifact, keep it inside a major artifact section or omit it.

```text
_hirmos/session/
  SESSION_STATE.json
  SESSION_SCOPE.md        # includes close verification
  SESSION_EXECUTION.md
  unresolved-items.md
  REQUIREMENTS.md   # conditional requirements authority
  DESIGN.md                  # conditional design authority
  EVIDENCE.md                # conditional nontrivial evidence surface
  implementation-units/      # conditional implementation-unit authority records/reviews
  bootstrap/                 # required session infrastructure; bootstrap report required for governed session startup
  stack-resolution.json       # conditional machine-readable stack routing only
```

## Major artifacts

- `SESSION_STATE.json`: minimal machine-readable command/lifecycle state only; it does not carry narrative continuation handoff content.
- `SESSION_SCOPE.md`: active session scope, accepted constraints, completion criteria, production-shaped engineering gate, and close verification.
- `SESSION_EXECUTION.md`: human-readable Current Continuation Snapshot, append-only execution-control spine, command timeline, evidence handoff pointers, close/update control pointers, and next-action discipline.
- `unresolved-items.md`: governed register for gated items, non-gating assumptions, technical-review items, dispositions, and revalidation.
- `REQUIREMENTS.md`: conditional governed requirements and coverage authority.
- `DESIGN.md`: conditional governed design and implementation-readiness authority.
- `EVIDENCE.md`: conditional evidence surface for nontrivial validation, runtime, production-shaped engineering, and close support.
- `implementation-units/IU-xx.md`: conditional unit-level contract, evidence, review, and retry surface.
- `bootstrap/BOOTSTRAP_REPORT.md`: required bootstrap report for governed session startup and new-chat continuity.
- `stack-resolution.json`: conditional machine-readable stack-routing state only.

Former separate support files such as request intake, source materials, technical review, implementation readiness, runtime evidence, close checklist, claim reconciliation, and session-scope review are not part of the default active-session model. Active-session archive manifests are not used; `ARCHIVE_MANIFEST.md` is a history-only close/archive artifact under `_hirmos/system/history/sessions/<session-id>/`. Their responsibilities belong in the major artifacts above.

## Source inputs

Source inputs live under:

```text
_hirmos/inputs/
  uploads/
  prototypes/
  references/
```

Source inputs are evidence and focus signals. They are not requirements authority, design authority, implementation authorization, or accepted current state. HIRMOS may read files from `_hirmos/inputs/uploads/`, `_hirmos/inputs/prototypes/`, and `_hirmos/inputs/references/`, but Design must reconcile material source signals into governed artifacts before they become authorized work.

## Accepted system state

Durable current truth lives in `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md`.

## Delivery plans

Durable multi-session delivery plans live under:

```text
_hirmos/system/delivery/DELIVERY_PLAN.md and _hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md
_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md
```

Use durable delivery artifacts only when the work cannot be safely governed as one session with implementation units. This applies to greenfield, brownfield, mixed, and unknown project types.

## Archive history

Closed sessions are archived under `_hirmos/system/history/sessions/<session-id>/`. Archive history is evidence, not current accepted state by itself.

## Archive history vs accepted state

Archive history preserves evidence. Accepted current system state must be merged into `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md` through governed close/update-state controls.


## PROD-L3 delivery authority surface

```text
_hirmos/system/delivery/
  DELIVERY_PLAN.md              # durable project delivery roadmap/register
  <delivery-id>/
    DELIVERY_SCOPE.md           # scoped authority for one delivery/release
    phases/
      PHASE-xx.md               # conditional phase scope
```

`DELIVERY_PLAN.md` is append/update-oriented and preserves delivery history. `DELIVERY_SCOPE.md` is the default combined delivery authority. Separate delivery-level `REQUIREMENTS.md` and `DESIGN.md` are optional only when independent authority is justified.

## PROD-L4 runtime routing relationship

The artifact model is activated through runtime command routing. Commands must instantiate the smallest authority surface that matches the Delivery Shape Decision:

- single-session shapes use `SESSION_SCOPE.md` only;
- durable delivery shapes use `DELIVERY_PLAN.md`, `DELIVERY_SCOPE.md`, and optionally `PHASE-xx.md`;
- `SESSION_SCOPE.md` adopts and narrows delivery/phase authority when present.


## PROD-L6 accepted-state and archive surfaces

`ARCHIVE_MANIFEST.md` lives inside `_hirmos/system/history/sessions/<session-id>/` and is a history-only archive transaction record. It is evidence for close concordance, not accepted current truth.

Delivery roadmap/register authority lives at `_hirmos/system/delivery/DELIVERY_PLAN.md`. Delivery scope authority lives at `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md`. `CURRENT_SYSTEM_STATE.md` points to those surfaces without duplicating their content.


## PROD-L8.9 delivery baseline focus

HIRMOS always runs inside a governed runtime session envelope, but `SESSION_SCOPE.md` is required only when the active work has a bounded phase/session work scope. Durable delivery-baseline work uses `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md` as active authority and `_hirmos/system/delivery/<delivery-id>/unresolved-items.md` for delivery-level unresolved items.

Before delivery-baseline acceptance, HIRMOS records a complete phase coverage plan inside `DELIVERY_SCOPE.md` and does not instantiate future `PHASE-xx.md` files by default. After acceptance, HIRMOS instantiates the next phase/session authority just in time.

## Delivery baseline artifact responsibilities

Durable delivery authority lives under the delivery folder:

```text
_hirmos/system/delivery/<delivery-id>/
  DELIVERY_SCOPE.md
  unresolved-items.md
  REQUIREMENTS.md   # optional
  DESIGN.md         # optional
  phases/           # phase files created just in time after baseline acceptance by default
```

`DELIVERY_SCOPE.md` is the complete delivery authority and must include enough phase coverage planning to answer whether planned phases cover 100% of the delivery scope. Future phase files are not referenced as concrete paths until they exist.

`<delivery-id>/unresolved-items.md` is the durable delivery-level unresolved register. It survives across sessions and is checked at delivery close. Session unresolved registers own only session-scoped blockers, assumptions, technical-review items, and inherited delivery items that affect the active session.

`SESSION_SCOPE.md` remains the complete active session authority once a bounded phase/session work scope exists. It may adopt delivery or phase authority, but it must not become the home for delivery-wide requirements, design, or unresolved items.

## PROD-L8.11 Delivery-Baseline Optional Authority Location

When `SESSION_STATE.json.session_focus = delivery_baseline`, the active authority is delivery-level. Optional requirements/design authority must be located under `_hirmos/system/delivery/<delivery-id>/` only:

- `_hirmos/system/delivery/<delivery-id>/REQUIREMENTS.md` when separate delivery-level requirements authority is justified.
- `_hirmos/system/delivery/<delivery-id>/DESIGN.md` when separate delivery-level design authority is justified.

During `delivery_baseline`, HIRMOS must not create, update, list, or depend on `_hirmos/session/REQUIREMENTS.md` or `_hirmos/session/DESIGN.md`. If separate optional authority is not justified, requirements and design decisions remain inside `DELIVERY_SCOPE.md` only. Session-level optional authority artifacts become applicable only after the flow advances to a bounded `phase_session_baseline` or `session_baseline` focus.


## PROD-L8.14 accepted-state navigation authority

Durable accepted-state navigation lives in `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md`. It owns current governance pointers, latest-close metadata, Work History Ledger, Source Artifact Index, and concise accepted-state summaries. It does not replace delivery/session requirements, design, scope, unresolved-item, implementation, evidence, or archive artifacts as source authorities.

Default HIRMOS does not create root accepted-state `REQUIREMENTS.md`, `DESIGN.md`, `SYSTEM_SCOPE.md`, `DECISIONS.md`, or `ACCEPTED_CHANGES.md`. Requirements/design/scope remain at the delivery/session/archive level and are discoverable through `CURRENT_SYSTEM_STATE.md`.
