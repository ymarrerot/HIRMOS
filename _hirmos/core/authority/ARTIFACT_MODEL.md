# Artifact Model Authority

Status: core authority.
Purpose: define artifact zones, ownership, and runtime meaning.

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

Source inputs may include:

- user request text;
- uploaded requirements;
- tickets;
- prototypes;
- proof-of-concept code;
- screenshots;
- existing docs;
- existing specs.

Source inputs are evidence and focus signals. They are not governed requirements, Design authority, Implementation authorization, or accepted system state.

## Templates

Files under `_hirmos/core/templates/` are reusable skeletons. They are not runtime evidence and must not be cited as proof that runtime work happened.

## Active session artifacts

Files under `_hirmos/session/` are active runtime artifacts for the current HIRMOS session.

A governed session is active only after `_hirmos/session/SESSION_EXECUTION.md` exists and declares an open or in-progress session. New governed sessions use the contract-centered spine: `SESSION_STATE.json`, `SESSION_CONTRACT.md`, `SESSION_EXECUTION.md`, `unresolved-items.md`, `session-contract-review.md`, plus `implementation-units/`, `checkpoints/`, and `support/` subfolders when needed.

## Accepted system state

Files under `_hirmos/system/accepted-state/` are durable accepted state. They may be updated only through Update System State.

## Session history

Closed sessions are archived under:

```text
_hirmos/system/history/sessions/<session-id>/
```

Archive records preserve session evidence and accepted/carry-forward decisions for future sessions.

## Artifact-backed checkpoint rule

HIRMOS must not tell the user that an artifact exists, is ready, or can be inspected unless the artifact exists and contains non-placeholder content.

## Ownership rule

Each lifecycle stage owns its authority artifacts:

- Understand System State owns current-state evidence artifacts and contributes uncertainty to `unresolved-items.md`.
- Design / Contracting owns requirements, design, delivery/phase contracts, and the active `SESSION_CONTRACT.md`.
- Implementation owns `implementation-units/IU-xx.md` artifacts and support evidence appendices.
- Update System State owns accepted-state update and archive artifacts.
- `SESSION_EXECUTION.md` owns execution control only; it does not own scope or acceptance criteria.

Later stages may reference earlier-stage authority, but must not silently rewrite it. If a later stage discovers a problem, it must route back to the owning stage.

## Accepted state and archive distinction

Archived session artifacts preserve history. They are not automatically accepted current system state.

Accepted system state lives under `_hirmos/system/accepted-state/` and is updated only through governed Update System State.

Close success requires consistency between accepted-state records, archive records, active-session reset state, and the user-facing close output.

## Accepted current-state model

Accepted current system truth lives in `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md`. It may include active development-context pointers to durable delivery plans, but it must not embed the full delivery plan or duplicate session-local contract authority.

Accepted-state responsibilities are intentionally small:

- `CURRENT_SYSTEM_STATE.md` owns current truth, accepted-state navigation, active development-context pointers, and latest-close metadata.
- `CARRY_FORWARD.md` preserves active unresolved items, blockers, assumptions, and future-session instructions only.
- `DECISION_LOG.md` preserves durable accepted, rejected, and superseded decisions.
- `_hirmos/system/history/sessions/<session-id>/` preserves historical evidence and archived session artifacts.

Do not use session archives, chat output, or accepted-state summaries as substitutes for the merged current-state artifact.

## Requirements baseline artifact authority

`REQUIREMENTS_BASELINE.md` is the requirements-control artifact. It owns normalized requirements, source traceability, non-goals, gated/unresolved requirements, delivery mapping, and coverage status.

It does not own architecture, implementation details, evidence status, runtime posture, or accepted current system truth.


## Contract-centered artifact model

HIRMOS rigor must come from authoritative contracts, explicit coverage verification, and fail-closed execution controls rather than a large number of manually synchronized artifacts.

Primary session authority:

```text
SESSION_CONTRACT.md session scope, acceptance, coverage, close verification
unresolved-items.md governed decision/assumption/risk register
session-contract-review.md governed promised-vs-verified session contract review
SESSION_EXECUTION.md command and lifecycle execution-control spine
SESSION_STATE.json machine-readable command state
```

Implementation-unit authority:

```text
implementation-units/IU-xx.md
```

Supporting artifacts must live under `support/` and remain subordinate to `SESSION_CONTRACT.md` and `SESSION_EXECUTION.md`.


## Durable delivery authority

Multi-session delivery authority lives under `_hirmos/system/delivery/<delivery-id>/`.

Required durable delivery artifacts:

```text
_hirmos/system/delivery/<delivery-id>/DELIVERY_PLAN.md
_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md
```

For multi-session work in any project type, a Delivery Plan is needed and separate phase files are required.

`CURRENT_SYSTEM_STATE.md` may point to the active delivery plan and active phase, but it must not duplicate their contents. Session-local delivery files are not canonical delivery authority.


## Root session filename discipline

Root session files must remain intentionally few. New support/evidence artifacts must use lowercase files under `_hirmos/session/support/` unless they are one of the governed root artifacts named by `_hirmos/core/protocol/SESSION_ARTIFACTS.md`.
