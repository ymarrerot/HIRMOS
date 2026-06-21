# Current System State Protocol

Status: core protocol.
Purpose: define the durable current system-state model that `hirmos close` must maintain.

## Core rule

`CURRENT_SYSTEM_STATE.md` is the canonical accepted current truth of the software system. HIRMOS close is not complete until accepted session outcomes are merged into `CURRENT_SYSTEM_STATE.md` or explicitly rejected / not applied with rationale.

Session archives are history. Session artifacts are evidence. `CARRY_FORWARD.md` is active future work and unresolved continuation control. `DECISION_LOG.md` is durable decision support. None of those replace `CURRENT_SYSTEM_STATE.md`.

`CURRENT_SYSTEM_STATE.md` also owns accepted-state navigation and latest-close metadata. Accepted-state navigation and latest-close metadata live in `CURRENT_SYSTEM_STATE.md` to prevent drift between latest-close metadata and current truth.

## Required accepted-state artifacts

The baseline accepted-state folder is:

```text
_hirmos/system/accepted-state/
```

It must contain these required files:

| Artifact | Role | When to update | Must not be used as |
|---|---|---|---|
| `CURRENT_SYSTEM_STATE.md` | Primary merged current truth, accepted-state navigation, latest accepted close, and state version | Every normal close that accepts, rejects, supersedes, or carries material system truth | Append-only log, chat summary, session transcript, backlog |
| `CARRY_FORWARD.md` | Active unresolved items, assumptions, risks, blockers, and future-session instructions only | Every close that leaves active follow-up items, and when carried items are resolved | Product backlog, accepted truth, or closed carry-forward history |
| `DECISION_LOG.md` | Durable accepted decision ledger for material domain, technical, integration, production-readiness, and governance decisions | When accepted decisions are made, superseded, or rejected | Full design document or session-local technical review |

Optional expansion files may be added later for large systems, but the baseline framework must start with these three required accepted-state artifacts. Do not split current truth into many required files until self-runs prove the single current-state artifact is too dense.

## Supporting artifact responsibilities

### CURRENT_SYSTEM_STATE.md

Use this file to answer: **what is accepted as true about the system right now?**

It must be merged and current. It is rewritten by accepted-state update. It should not grow as a chronological transcript.

Required sections:

1. Current State Header
2. Accepted-State Navigation and Latest Close
3. Product State
4. Delivery State, including Active Development Context and Delivery Pointers
5. Implementation State
6. Technical / Architecture State
7. Runtime Integration State
8. Evidence State
9. Production Readiness State
10. Unresolved / Carry-Forward State
11. History / Traceability

### CARRY_FORWARD.md

Use this file to answer: **what must a future session not forget?**

It contains active unresolved items, assumptions, blockers, production/go-live blockers, evidence gaps, and required future-session instructions. Closed carry-forward history belongs in session archives and `CURRENT_SYSTEM_STATE.md` History / Traceability, not in this active register.

### DECISION_LOG.md

Use this file to answer: **which durable decisions are accepted, rejected, or superseded?**

Session-local `DESIGN.md` technical review records decisions made during a session. `DECISION_LOG.md` records only accepted durable decisions that future sessions should rely on or revisit.



## Active Development Context and Delivery Pointers

When delivery governance is active, `CURRENT_SYSTEM_STATE.md` is the canonical place where future sessions discover the active durable delivery pointer set. It must record pointers only, not the Delivery Plan or Phase content itself.

Required pointer fields when applicable:

- Delivery governance active
- Active delivery ID
- Delivery plan path
- Active phase path
- Active phase status
- Last accepted phase
- Last accepted session/archive
- Next recommended phase
- Next governed command

Update System State must refresh these pointers during normal close whenever a session creates, updates, accepts, blocks, supersedes, or advances a durable Delivery Plan or Phase file. If the pointers are unchanged, the close artifact must say so with evidence.

Future sessions must read these pointers during Understand System State before deciding that a request is safe for a single-session path. A stale or contradictory delivery pointer is a blocker for Design or Implementation readiness until reconciled.

## Merge model

`Update System State` must merge accepted outcomes into current state.

Required close sequence:

1. Read prior `CURRENT_SYSTEM_STATE.md`.
2. Read `SESSION_EXECUTION.md` close/update controls, `SESSION_EXECUTION.md` close controls, `EVIDENCE.md` claim reconciliation when material claims exist, and relevant session evidence.
3. Classify each material outcome as accepted, rejected / not applied, evidence-only, superseded, or carry-forward.
4. Merge accepted and superseded truth into `CURRENT_SYSTEM_STATE.md`.
5. Update `DECISION_LOG.md` for accepted/rejected/superseded decisions.
6. Update `CARRY_FORWARD.md` for unresolved or future-session items.
7. Update the accepted-state navigation and latest-close sections inside `CURRENT_SYSTEM_STATE.md`.
8. Archive the session.
9. Reset active session state.
10. Verify that current state, carry-forward, decision log, archive manifest, and active session state agree.

## Accepted-state tracks

Do not collapse different truth tracks into one vague claim.

At minimum, `CURRENT_SYSTEM_STATE.md` must distinguish:

| Track | Meaning |
|---|---|
| MVP / delivery completion | Delivery Units accepted as implemented for the agreed MVP scope. |
| Local runtime readiness | App was locally configured and smoke-tested in the recorded environment. |
| Runtime integration posture | Database/auth/messaging/storage/etc. posture using canonical posture values. |
| Production readiness planning | Plan or recommendations exist. This is not go-live approval. |
| Production provider readiness | Production credentials, providers, callbacks, sender identities, secrets, jobs, deployment, and provider evidence are verified. |
| Compliance / go-live readiness | Legal/compliance/operations approval exists when applicable. |

Firm rule: do not state “production ready” when only production-readiness planning was accepted.

## Update classification

Use these classifications for material outcomes:

- `ACCEPTED_CURRENT_TRUTH`
- `SUPERSEDED_CURRENT_TRUTH`
- `REJECTED_NOT_APPLIED`
- `EVIDENCE_ONLY`
- `CARRY_FORWARD`
- `BLOCKED`

Only `ACCEPTED_CURRENT_TRUTH` and `SUPERSEDED_CURRENT_TRUTH` change `CURRENT_SYSTEM_STATE.md`. All others must be recorded in archive, carry-forward, or decision log as appropriate.

## Future-session rule

Future HIRMOS sessions must read `CURRENT_SYSTEM_STATE.md` as the primary accepted current-state source. They may inspect archives for evidence and history, but must not reconstruct current truth from chat memory or archives when `CURRENT_SYSTEM_STATE.md` exists.

## Close blocking rules

Normal close is blocked when:

- `CURRENT_SYSTEM_STATE.md` is missing;
- accepted outcomes are not mapped to current-state sections;
- material claims require `EVIDENCE.md` claim reconciliation but it is missing;
- `CURRENT_SYSTEM_STATE.md` latest-close metadata points to a different latest archive than the close transaction;
- carry-forward items in session artifacts are not reflected in `CARRY_FORWARD.md` or explicitly rejected;
- durable decisions are not reflected in `DECISION_LOG.md` or explicitly rejected;
- production-readiness planning, provider readiness, and go-live readiness are collapsed into one ambiguous state;
- post-close `SESSION_STATE.json` and archive manifest contradict the accepted-state update.

## User-facing status rule

`hirmos status` must prefer `CURRENT_SYSTEM_STATE.md` for accepted current truth. It should show concise current state, active/carry-forward blockers, latest archive, and one primary next action.

## Understand System State enforcement

Before HIRMOS performs meaningful Design or Implementation, Understand System State must resolve the accepted current-state source.

Required sequence:

1. Check `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md`.
2. If it exists, read it first and treat it as the primary accepted current-state source.
3. If it is missing, record whether this is a new installation or an integrity failure.
4. Read `CARRY_FORWARD.md` and `DECISION_LOG.md` as supporting accepted-state artifacts when present.
5. Consult session archives only as history/evidence or to investigate contradictions. Archives are not the current system state.
6. Record source status, contradictions, and confidence in `_hirmos/session/DESIGN.md`.
7. Mark the current-system-state-first execution controls in `_hirmos/session/SESSION_EXECUTION.md`.

Firm rule: HIRMOS must not claim Design readiness, Implementation readiness, Implementation completion, or Update System State readiness unless current-system-state-first controls are satisfied or explicitly not applicable with rationale.

## Accepted-state artifact invariants and canonical value protection

Accepted-state artifacts are update targets, but they are not free-form scratchpads. Every accepted-state artifact must preserve its invariant block when updated.

Required accepted-state invariant block:

```text
Accepted-State Artifact Invariants:
- This file is part of durable accepted state.
- Preserve this invariant block during Update System State.
- Do not replace this file with a chat summary or session-local artifact.
- Use canonical runtime posture values from RUNTIME_INTEGRATION_AND_PRODUCTION_READINESS.md.
- Use canonical evidence states from EVIDENCE.md claim reconciliation.
- Keep accepted-state decision classifications separate from evidence status.
```

`CURRENT_SYSTEM_STATE.md` is the only current-truth artifact and owns accepted-state navigation/latest-close metadata. `CARRY_FORWARD.md` and `DECISION_LOG.md` support it and must preserve their distinct roles.

Canonical accepted-state field rules:

| Field type | Required value source |
|---|---|
| Runtime posture | canonical posture values from `RUNTIME_INTEGRATION_AND_PRODUCTION_READINESS.md` only |
| Evidence state | canonical evidence states from `EVIDENCE.md` claim reconciliation only |
| Update classification | update classifications from this protocol only |
| Decision state | accepted/rejected/superseded decision records in `DECISION_LOG.md`; not evidence status |
| Source note / rationale | free text allowed, but it must not replace canonical status fields |

Before normal close, Update System State must scan accepted-state updates for noncanonical values in status/posture/evidence fields. If found, close is blocked until values are translated.

y copy of current truth.


## Close-Time Delivery Pointer Refresh

`CURRENT_SYSTEM_STATE.md` must be refreshed during close whenever delivery governance was active or required. The refresh must be sourced from `SESSION_EXECUTION.md` close/update controls, the durable Delivery Plan, the adopted Phase file, and archive evidence.

A future session must not trust delivery pointers that were not refreshed or explicitly verified unchanged at the last delivery-governed close.
