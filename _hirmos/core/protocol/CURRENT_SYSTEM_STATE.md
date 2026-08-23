# Current System State Protocol

Status: core protocol.
Purpose: define the durable accepted-state navigation model that `hirmos close`, `hirmos start`, `hirmos continue`, and `hirmos status` must maintain.

## Core rule

`CURRENT_SYSTEM_STATE.md` is the canonical accepted current truth and accepted-state navigation authority for the software system. HIRMOS close is not complete until accepted session outcomes are registered in `CURRENT_SYSTEM_STATE.md` or explicitly rejected / not applied with rationale.

`CURRENT_SYSTEM_STATE.md` is index-first. It summarizes current state, owns current governance pointers, records latest-close metadata, and maintains a chronological Work History Ledger and Source Artifact Index. It must not become a cumulative requirements catalog, full design document, system-scope substitute, command log, evidence store, or archive manifest.

Session archives are history. Session artifacts are evidence. Delivery and session scope/requirements/design artifacts are source authorities at their level. `CARRY_FORWARD.md` is active future work and unresolved continuation control. `DECISION_LOG.md` is conditional durable decision support when explicit decision-log governance is active. None of those replace `CURRENT_SYSTEM_STATE.md`, and `CURRENT_SYSTEM_STATE.md` does not replace them.

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
| `CARRY_FORWARD.md` | yes | active/resolved carry-forward lifecycle authority |
| `DECISION_LOG.md` | conditional | durable accepted/rejected/superseded decision support when explicit decision-log governance is active |

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

`CURRENT_SYSTEM_STATE.md` and `CARRY_FORWARD.md` must preserve their accepted-state invariant blocks; `DECISION_LOG.md` must preserve them when explicit decision-log governance is active. They must use canonical runtime posture values, canonical evidence states, and separate decision classifications from evidence status.

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

Active and resolved carry-forward lifecycle details live in CARRY_FORWARD.md. Session archives remain close-time snapshots; CURRENT_SYSTEM_STATE.md summarizes current posture and points to the owning carry-forward rows.

## Current-State-First Navigation Spine

`CURRENT_SYSTEM_STATE.md` must be source-complete, not content-complete. It does not duplicate full requirements, design, scope, evidence, unresolved-item, or archive content. It must contain enough fresh navigation to find those canonical source authorities.

The mandatory navigation spine is:

- Current Governance Context;
- Accepted-State Navigation and Latest Close;
- Work History Ledger;
- Source Artifact Index;
- active carry-forward pointer / carry-forward summary;
- next governed command / next recommended work.

Validators and command protocols should protect this spine without requiring `CURRENT_SYSTEM_STATE.md` to become a cumulative requirements/design/scope artifact.

## Transition Updates vs Close Updates

`CURRENT_SYSTEM_STATE.md` has two update classes:

1. **Active navigation pointer updates** may happen during governed transitions such as `hirmos start` or `hirmos continue` when the active delivery, phase, session scope, unresolved register, or recommended next command changes. These updates keep the next command oriented and do not by themselves claim accepted completion.
2. **Accepted-state outcome updates** happen during `hirmos close`. These include accepted-state summary changes, latest accepted close metadata, final Work History Ledger outcome rows, accepted source index changes, and archive/close concordance.

A transition may refresh active pointers, but it must not claim accepted outcomes that belong to close. Close remains responsible for final accepted-state history, archive concordance, and accepted outcome registration.

## Source Reading Contract for Future Sessions

During Understand System State, HIRMOS must read `CURRENT_SYSTEM_STATE.md` first and then follow the mandatory navigation spine to active and materially relevant source artifacts. HIRMOS may scope historical depth to the request, but it must not design or implement from `CURRENT_SYSTEM_STATE.md` summaries alone when relevant canonical source artifacts exist.

## PROD-L8.19 transition/close update split

`CURRENT_SYSTEM_STATE.md` has two update classes:

1. **Transition navigation updates** — active delivery, active phase, active session scope, carry-forward pointer, and next governed command may update during governed `start` / `continue` transitions.
2. **Accepted-state close updates** — accepted-state summary, Work History Ledger outcome rows, latest-close metadata, completed delivery/session status, and accepted source indexes update during `hirmos close`.

HIRMOS must not use this split to hide stale pointers. Any transition update must preserve source authority links and remain consistent with `SESSION_STATE.json`, `SESSION_LEDGER.md`, delivery artifacts, and phase/session artifacts.

## PROD-L8.32L Artifact Creation / Derived Pointer Doctrine

HIRMOS must not create optional artifacts simply because a template exists. Optional artifacts are created just in time when the current governed boundary makes their owning concern applicable. Derived pointer indexes must be recomputed from canonical source artifacts, filesystem paths, active session state, session ledgers, delivery/phase directories, and archive manifests. Stale pointer rows are defects, not truth.


## PROD-L8.33G Carry-forward lifecycle summary rule

`CURRENT_SYSTEM_STATE.md` summarizes carry-forward posture but does not own carry-forward lifecycle truth. Active and resolved carry-forward records live in `_hirmos/system/accepted-state/CARRY_FORWARD.md`. A claim that a carry-forward item is resolved, user-verified, or production-verified must point to the matching resolved row in `CARRY_FORWARD.md`.
