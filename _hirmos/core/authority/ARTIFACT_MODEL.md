# Artifact Model Authority

Status: core authority.
Purpose: define artifact zones, ownership, strict necessity, and runtime meaning.


## PROD-L canonical scope-authority direction

HIRMOS uses a scope-centered authority model. The canonical names are:

```text
SESSION_SCOPE.md       # active session authority
DELIVERY_SCOPE.md      # one durable delivery/release authority
REQUIREMENTS.md        # conditional independent requirements authority only
DESIGN.md              # conditional independent design authority only
```

The active-session authority template is `SESSION_SCOPE.md`. `REQUIREMENTS.md` is conditional independent requirements authority and is not part of the default implementation-session surface.

`DELIVERY_PLAN.md` is the durable project delivery roadmap/register. It must not be overwritten when later durable multi-session work appears; new durable multi-session work adds or updates a delivery entry and creates/updates `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md`.

## Installed framework zones

```text
_hirmos/ installed, self-contained HIRMOS framework
_hirmos/core/ core authority, protocols, commands, templates, bootstrap, validation tools
_hirmos/docs/ user-facing HIRMOS docs inside the installed framework
_hirmos/inputs/ raw source inputs for requests; inputs are not authority
_hirmos/session/ active session runtime artifacts
_hirmos/system/ durable accepted system state and session history
_hirmos/extensions/ bundled capabilities
_hirmos/stacks/ stack packages
```

Framework files must not depend on development-only paths, temporary reports, prior versions, transcripts, or self-review artifacts.

## Source inputs

Source inputs may include user request text, uploaded requirements, tickets, prototypes, proof-of-concept code, screenshots, existing docs, and existing specs.

Source inputs are evidence and focus signals. They are not governed requirements, Design authority, Implementation authorization, or accepted system state until reconciled into a governed artifact.

## Templates

Files under `_hirmos/core/templates/` are reusable skeletons. They are not runtime evidence and must not be cited as proof that runtime work happened.

## Strict-necessity artifact rule

HIRMOS rigor must come from authoritative major artifacts, explicit coverage verification, and fail-closed execution controls, not from a large number of manually synchronized support files.

A separate active-session artifact is justified only when it is strictly necessary for authority, machine state, evidence, gating, continuity, or audit/history. Useful notes that do not meet this threshold must be embedded in the nearest major artifact or omitted.

## Active session artifacts

Files under `_hirmos/session/` are active runtime artifacts for the current HIRMOS session.

A governed session is active only after `_hirmos/session/SESSION_LEDGER.md` exists and declares an open or in-progress session. New governed sessions use the strict-necessity session surface:

```text
SESSION_STATE.json
SESSION_LEDGER.md
SESSION_SCOPE.md
unresolved-items.md
REQUIREMENTS.md      # conditional
DESIGN.md                     # conditional
EVIDENCE.md                   # conditional
implementation-units/         # conditional
bootstrap/                    # required session infrastructure
stack-resolution.json           # conditional machine-readable stack routing only
```

## Ownership rule

Each lifecycle responsibility owns its authority inside the smallest sufficient artifact set:

- Understand System State records the current-state-first control in `SESSION_LEDGER.md` and material state findings in `DESIGN.md` when they affect Design or Implementation.
- Design / Scope Authority owns requirements, design, delivery/phase scopes, production-shaped engineering posture, and the active `SESSION_SCOPE.md`.
- Implementation owns `implementation-units/IU-xx.md` artifacts and `EVIDENCE.md` when evidence is material.
- Update System State owns accepted-state update and archive records through `SESSION_SCOPE.md` close verification, `SESSION_LEDGER.md` close/archive/reset control pointers, `EVIDENCE.md` when needed, and accepted-state artifacts.
- `SESSION_LEDGER.md` owns the human-readable Current Continuation Snapshot, execution-control ledger, and append-only lifecycle history only; it does not own scope or acceptance criteria.

Later stages may reference earlier-stage authority, but must not silently rewrite it. If a later stage discovers a problem, it must route back to the owning stage.

## Major session artifacts

Primary session authority:

```text
SESSION_SCOPE.md scope, acceptance, delivery shape, production-shaped gate, close verification
DESIGN.md current-state basis, source matrix, design authority, technical review, readiness rationale
REQUIREMENTS.md requirements authority when material; target name REQUIREMENTS.md
unresolved-items.md governed decision/assumption/risk register
EVIDENCE.md material validation/runtime/claim/close evidence
SESSION_LEDGER.md command and lifecycle execution-control spine
SESSION_STATE.json minimal machine-readable command state only
```

Implementation-unit authority:

```text
implementation-units/IU-xx.md
```

Session infrastructure is intentionally minimized. `bootstrap/` remains required for startup/bootstrap evidence. `stack-resolution.json` is retained as a conditional root session artifact because stack resolution is machine-readable routing state. `SESSION_STATE.json` remains minimal machine state; continuation handoff lives in `SESSION_LEDGER.md` Current Continuation Snapshot. Other former support responsibilities live in the major artifacts listed above.

## Accepted system state

Files under `_hirmos/system/accepted-state/` are durable accepted state. They may be updated only through Update System State.

Accepted current system truth lives in `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md`. Accepted-state responsibilities are intentionally small:

- `CURRENT_SYSTEM_STATE.md` owns current truth, accepted-state navigation, active development-context pointers, and latest-close metadata.
- `CARRY_FORWARD.md` preserves active unresolved items, blockers, assumptions, and future-session instructions only.
- `DECISION_LOG.md` is conditional durable decision support when explicit decision-log governance is active; it is not a default accepted-state root artifact.
- `_hirmos/system/history/sessions/<session-id>/` preserves historical evidence and archived session artifacts.

Do not use session archives, chat output, or accepted-state summaries as substitutes for the merged current-state artifact.

## Session history

Closed sessions are archived under:

```text
_hirmos/system/history/sessions/<session-id>/
```

Archive records preserve session evidence and accepted/carry-forward decisions for future sessions. Archived session artifacts preserve history. They are not automatically accepted current system state.

Close success requires consistency between accepted-state records, archive records, active-session reset state, and the user-facing close output.

## Durable delivery authority

Multi-session delivery authority lives under `_hirmos/system/delivery/<delivery-id>/`.

Required durable delivery artifacts for delivery-baseline planning:

```text
_hirmos/system/delivery/DELIVERY_PLAN.md
_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md
_hirmos/system/delivery/<delivery-id>/unresolved-items.md
```

Optional delivery-level authority artifacts:

```text
_hirmos/system/delivery/<delivery-id>/REQUIREMENTS.md
_hirmos/system/delivery/<delivery-id>/DESIGN.md
```

Separate phase files are instantiated just in time after delivery-baseline acceptance. Before that, `DELIVERY_SCOPE.md` must carry a phase coverage plan sufficient to verify that planned phases cover 100% of delivery scope.

`CURRENT_SYSTEM_STATE.md` may point to the active delivery plan and active phase, but it must not duplicate their contents. Session-local delivery files are not canonical delivery authority.

## Root session filename discipline

Root session files must remain intentionally few and must be major/governed artifacts only. New auxiliary/evidence artifacts must not be introduced unless they satisfy strict necessity and cannot safely live in `SESSION_SCOPE.md`, `DESIGN.md`, `EVIDENCE.md`, `SESSION_LEDGER.md`, or `implementation-units/IU-xx.md`.

## Accepted state and archive distinction

Archive history is not accepted state by itself.


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


## PROD-L8.9 runtime session focus model

HIRMOS always runs inside a governed runtime session envelope, but `SESSION_SCOPE.md` is not synonymous with the runtime session itself.

A runtime session may focus on delivery-baseline planning, phase/session baseline planning, implementation, correction, close, status, or minimal single-session work. `SESSION_STATE.json.session_focus` records the active focus.

Canonical focus values:

```text
idle
minimal_session
session_baseline
delivery_baseline
phase_session_baseline
implementation
correction
close
status
```

Rule: `SESSION_SCOPE.md` is required only when the active work has a bounded phase/session work scope or implementation authority. During `delivery_baseline` focus, the active authority is `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md`, not `_hirmos/session/SESSION_SCOPE.md`.

Delivery-level uncertainty belongs to `_hirmos/system/delivery/<delivery-id>/unresolved-items.md`. Session-level uncertainty belongs to `_hirmos/session/unresolved-items.md` only after a session scope exists or when the active single-session work has material unresolved items.

## Reuse-First Complexity Control

Before adding any new artifact surface, protocol layer, or capability split, HIRMOS must identify which existing surface already owns the responsibility. Prefer updating existing lifecycle doctrine, command protocols, templates, validators, and artifacts. Add a new governance layer only when no existing surface can safely own the responsibility.

Complexity-pressure risks to review periodically:

- overlapping protocol docs;
- excessive capability names;
- default durable support artifacts such as decision logs;
- validators enforcing wording instead of authority safety;
- project-type language replacing current-state-first routing;
- too many places to express requirements, design, or source authority.
