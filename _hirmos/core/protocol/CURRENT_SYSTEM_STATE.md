# Current System State Protocol

Status: core protocol.
Purpose: define the durable accepted-state navigation model that `hirmos close`, `hirmos start`, `hirmos continue`, and `hirmos status` must maintain.

## Core rule

`CURRENT_SYSTEM_STATE.md` is the canonical accepted current truth and accepted-state navigation authority for the software system. HIRMOS close is not complete until accepted session outcomes are registered in `CURRENT_SYSTEM_STATE.md` or explicitly rejected / not applied with rationale.

`CURRENT_SYSTEM_STATE.md` is index-first. It summarizes current state, owns current governance pointers, records latest-close metadata, and maintains a chronological Work History Ledger and Source Artifact Index. It must not become a cumulative requirements catalog, full design document, system-scope substitute, command log, evidence store, or archive manifest.

Session archives are history. Session artifacts are evidence. Delivery and session scope/requirements/design artifacts are source authorities at their level. `CARRY_FORWARD.md` is active future work and unresolved continuation control. `DECISION_LOG.md` is durable decision support when decision-log governance is active. None of those replace `CURRENT_SYSTEM_STATE.md`, and `CURRENT_SYSTEM_STATE.md` does not replace them.

`CURRENT_SYSTEM_STATE.md` also owns accepted-state navigation and latest-close metadata. Accepted-state navigation and latest-close metadata live in `CURRENT_SYSTEM_STATE.md` to prevent drift between latest-close metadata and current truth.

## Required accepted-state artifacts

The baseline accepted-state folder is:

```text
_hirmos/system/accepted-state/
```

It must contain these required files:

| Artifact | Required | Responsibility |
|---|---:|---|
| `CURRENT_SYSTEM_STATE.md` | yes | accepted-state navigation authority, current governance pointers, latest-close metadata, Work History Ledger, Source Artifact Index, and concise current-state summary |
| `CARRY_FORWARD.md` | yes | active unresolved / future-session obligations only |
| `DECISION_LOG.md` | yes | durable accepted/rejected/superseded decision support when decision-log governance is active |

Default HIRMOS must not create root accepted-state `REQUIREMENTS.md`, `DESIGN.md`, `SYSTEM_SCOPE.md`, `DECISIONS.md`, or `ACCEPTED_CHANGES.md`.

If a project explicitly activates cumulative accepted requirements governance in the future, root accepted-state `REQUIREMENTS.md` must include explicit cumulative-governance metadata, source traceability, add/amend/remove/supersede/deprecate controls, and close-time merge verification. Without that explicit governance mode, detailed requirements remain in delivery/session/archive source artifacts and are discoverable through `CURRENT_SYSTEM_STATE.md` Work History Ledger and Source Artifact Index.

## Accepted-state tracks

`CURRENT_SYSTEM_STATE.md` must maintain these tracks:

1. Current State Header.
2. Current Governance Context.
3. Accepted-State Navigation and Latest Close.
4. Accepted State Summary, explicitly marked as a concise navigation summary only.
5. Work History Ledger.
6. Source Artifact Index.
7. Delivery State.
8. Implementation State.
9. Technical / Architecture State.
10. Runtime Integration State.
11. Evidence State.
12. Production Readiness State.
13. Unresolved / Carry-Forward State.
14. History / Traceability / Merge Notes.

The Accepted State Summary must state that it is not the complete requirements, design, scope, implementation, evidence, or decision authority. Detailed source authority remains in the source artifacts referenced by the ledger and index.

## Work History Ledger rule

Every normal close that creates, accepts, amends, completes, defers, blocks, cancels, supersedes, or archives governed HIRMOS work must add or update a chronological Work History Ledger row.

The ledger records governed work outcomes, not every command. Routine `hirmos status` calls do not receive ledger rows unless they materially change accepted state.

The ledger must identify:

- date;
- work id;
- work type;
- status;
- authority path;
- source artifact paths;
- accepted output / result.

This ledger is the default solution to scattered requirements/design/scope/evidence authority. It points to sources rather than copying them into a cumulative root artifact.

## Source Artifact Index rule

`CURRENT_SYSTEM_STATE.md` must keep material source authorities discoverable. The Source Artifact Index may include delivery authorities, phase authorities, session authorities, requirement sources, design sources, and evidence sources.

Requirements, design, and scope sources remain authoritative where originated:

- delivery-level `DELIVERY_SCOPE.md`, optional delivery `REQUIREMENTS.md`, optional delivery `DESIGN.md`;
- phase `PHASE-xx.md`;
- session `SESSION_SCOPE.md`, optional session `REQUIREMENTS.md`, optional session `DESIGN.md`;
- archived source artifacts after close.

On-demand synthesis may be generated from these source artifacts when needed, but a generated synthesis is not source authority unless explicitly adopted by a governed future workflow.

## Close blocking rules

Close is blocked if:

- active governance pointers would be stale or inconsistent after close;
- accepted output lacks a Work History Ledger row;
- material source authorities are not discoverable from the Source Artifact Index or Work History Ledger;
- `CURRENT_SYSTEM_STATE.md` presents a concise summary as complete requirements/design/scope authority;
- root accepted-state `REQUIREMENTS.md`, `DESIGN.md`, `SYSTEM_SCOPE.md`, `DECISIONS.md`, or `ACCEPTED_CHANGES.md` is created without explicit governed activation metadata;
- accepted-state records contradict source artifacts, archive manifest, active carry-forward, or session close verification.

## Future sessions

Future sessions must read these pointers before planning or implementation:

- current governance context;
- Work History Ledger;
- Source Artifact Index;
- active delivery / phase / session pointers;
- latest accepted close metadata;
- active carry-forward items.

Future sessions must not reconstruct current truth from chat memory, old transcripts, or scattered archives when `CURRENT_SYSTEM_STATE.md` exists.

## Accepted-State Artifact Invariants

`CURRENT_SYSTEM_STATE.md`, `CARRY_FORWARD.md`, and `DECISION_LOG.md` must preserve their accepted-state invariant blocks. They must use canonical runtime posture values, canonical evidence states, and separate decision classifications from evidence status.

## PROD-L6 accepted-state delivery pointer model

Delivery roadmap: `_hirmos/system/delivery/DELIVERY_PLAN.md`
Active delivery scope: `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md`
Archive manifest concordance: unknown / PASS / PARTIAL / BLOCKED

## Required pointer fields

Required pointer fields include Active Development Context and Delivery Pointers, Next recommended delivery, Next recommended delivery scope, and Next recommended phase.

## Close-Time Delivery Pointer Refresh

Close must refresh current delivery/phase/session pointers from accepted close evidence or record that each value was explicitly verified unchanged. Missing, stale, or contradictory pointer updates block normal close.

## Phase Progress Pointer Rule

When a multi-session phase closes as partial, blocked, or deferred, `CURRENT_SYSTEM_STATE.md` must point to the still-active phase, the next phase, or explicit carry-forward target.

## Phase Acceptance Pointer Rule

When a phase becomes accepted, `CURRENT_SYSTEM_STATE.md` must record the last accepted phase, next recommended phase, and whether no active phase remains.

## Phase Lifecycle Status Pointer Rule

`hirmos status` must read `CURRENT_SYSTEM_STATE.md` delivery pointers before reporting active delivery work and must surface pointer concordance.

Close is blocked when delivery or phase pointers are not refreshed or explicitly verified unchanged.

Active carry-forward details live in CARRY_FORWARD.md; closed carry-forward history belongs in session archives and CURRENT_SYSTEM_STATE.md Work History Ledger / History / Traceability.
