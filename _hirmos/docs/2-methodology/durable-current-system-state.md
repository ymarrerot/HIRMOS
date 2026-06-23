# Durable Current System State

HIRMOS maintains accepted current system truth in:

```text
_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md
```

This artifact answers: **what is true about the software system right now?**

## Supporting artifacts

These are the supporting artifacts for durable current-state management.

| Artifact | Use it for | Do not use it for |
|---|---|---|
| `CURRENT_SYSTEM_STATE.md` | canonical merged current truth | session log or backlog |
| `CARRY_FORWARD.md` | unresolved/future-session obligations | accepted feature list |
| `DECISION_LOG.md` | durable accepted/rejected/superseded decisions | full design doc |
| session archives | historical evidence | current truth substitute |

## Close rule

`hirmos close` is not complete until accepted session outcomes are merged into `CURRENT_SYSTEM_STATE.md` or explicitly rejected / not applied.

## Why this exists

Without a durable current-state artifact, future sessions must reconstruct truth from archives, chat history, and summaries. That is exactly what HIRMOS is designed to avoid.


## Current-system-state-first understanding

HIRMOS must read `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md` before meaningful Design or Implementation when the file exists. This keeps future sessions grounded in accepted current truth instead of reconstructing truth from chat memory, old session archives, or repository guesses.

Supporting files have narrower roles:

- `CARRY_FORWARD.md` preserves active unresolved and future-session obligations.
- `DECISION_LOG.md` preserves accepted, rejected, and superseded decisions.
- session archives preserve history/evidence only.

Accepted-state navigation and latest-close metadata now live inside `CURRENT_SYSTEM_STATE.md`, not a separate index file.

If `CURRENT_SYSTEM_STATE.md` is missing, HIRMOS must record whether the workspace is a new installation or whether accepted state is incomplete.

## Accepted-state invariants and canonical values

Accepted-state artifacts are durable records. HIRMOS updates them during close, but must preserve their artifact identity and invariant blocks.

Use canonical runtime posture values only. Use canonical evidence states only. Put nuance in notes/rationale fields instead of inventing new status values.

`CURRENT_SYSTEM_STATE.md` includes accepted-state navigation and latest-close metadata. There is no separate hand-maintained current-state latest-close metadata.

## Active delivery pointers

For multi-session work in any project type, `CURRENT_SYSTEM_STATE.md` must carry the active delivery pointer set: active delivery ID, Delivery Plan path, active Phase path, active phase status, last accepted phase/session, next recommended phase, and next governed command.

These are pointers only. The durable Delivery Plan and Phase files remain the delivery authority under `_hirmos/system/delivery/<delivery-id>/`.

Future sessions must inspect these pointers before deciding a new request can safely run as a single-session effort.

## Delivery phase adoption pointer discipline

When delivery governance is active, Current System State pointers identify the durable Delivery Plan and active Phase. A session may implement only after `SESSION_SCOPE.md` adopts exactly one durable `PHASE-xx.md` and maps that phase scope into authorized session work. Future sessions must treat the Current System State pointer as a discovery aid, not as a replacement for directly reading the Delivery Plan and Phase file.
