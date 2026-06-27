# Delivery Plan

Status: DRAFT | PROPOSED | READY_FOR_BASELINE_REVIEW | ACTIVE | ACCEPTED | COMPLETE | PARTIAL | SUPERSEDED | BLOCKED | DEFERRED | CANCELLED
Last updated from session:

## Purpose

This file is the durable project delivery roadmap/register. It indexes one or more durable deliveries and preserves completed, active, planned, deferred, cancelled, superseded, and blocked delivery history.

Canonical location:

```text
_hirmos/system/delivery/DELIVERY_PLAN.md
```

`DELIVERY_PLAN.md` is append/update-oriented. It must not be overwritten when new durable multi-session work appears later. New durable multi-session work adds a new delivery entry and creates a corresponding `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md` while preserving prior delivery entries.

## Authority Boundary

`DELIVERY_PLAN.md` is the roadmap/register. It does not contain the full scoped authority for a delivery and does not authorize implementation by itself.

Authority flows through:

```text
CURRENT_SYSTEM_STATE.md
→ _hirmos/system/delivery/DELIVERY_PLAN.md
→ _hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md
→ _hirmos/system/delivery/<delivery-id>/unresolved-items.md for delivery-level unresolved items
→ phase coverage plan in DELIVERY_SCOPE.md before phase files exist
→ _hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md when instantiated after delivery-baseline acceptance
→ _hirmos/session/SESSION_SCOPE.md when a bounded phase/session scope exists
→ implementation-units / EVIDENCE / SESSION_EXECUTION.md
```

## Delivery Shape Source

Compatibility label: Delivery-Need Classification Source.

- Delivery shape: SINGLE_SESSION_VERTICAL_SLICE | SINGLE_SESSION_WITH_IMPLEMENTATION_UNITS | MULTI_SESSION_DELIVERY | MULTI_SESSION_DELIVERY_WITH_PHASE_FILES
- Why durable delivery governance is / is not necessary for the real software work:
- Technically possible simpler shape:
- Why smaller shape was acceptable or insufficient when delivery governance is active:
- Why added governance is worth / not worth the user interaction and token-cost overhead:
- Why phase files are / are not needed:
- If multi-session, selected phase count:
- Phase-count options considered:
- Why fewer phases are insufficient or acceptable:
- Why selected phase count is the smallest honest count:
- Phase merge pressure result:
- Phase-count user interaction / token-cost impact:
- Risk if compressed into fewer phases:

## Delivery Shape Decision Source

- Classification answer: YES | NO | UNCERTAIN
- Classification evidence:
- New-build / empty-system signals present:
- Existing-system preservation signals present:
- Universal governance triggers present:
- If adopted from prior work, source artifact/session:


## Delivery Baseline Rule

A delivery entry may be `PROPOSED` or `READY_FOR_BASELINE_REVIEW` before the user accepts or amends the delivery baseline. In those states, the roadmap/register and delivery scope may exist, but they do not authorize phase/session implementation.

Before baseline acceptance:

- the delivery may have `DELIVERY_SCOPE.md`, delivery `unresolved-items.md`, and optional delivery-level `REQUIREMENTS.md` / `DESIGN.md`;
- future phases are represented by a phase coverage plan inside `DELIVERY_SCOPE.md`;
- concrete future `PHASE-xx.md` paths must not be referenced unless those files exist;
- `_hirmos/session/SESSION_SCOPE.md` is not required for `session_focus = delivery_baseline`.

After baseline acceptance, HIRMOS marks the delivery `ACTIVE` or accepted/amended as appropriate and instantiates the next phase/session authority just in time.

## Delivery Index

| Delivery ID | Name | Status | Type | Scope file | Current/Final phase | Relationship |
|---|---|---|---|---|---|---|
| `<delivery-id>` | | proposed / ready_for_baseline_review / planned / active / accepted / completed / partial / blocked / deferred / superseded / cancelled | MVP / release / hardening / migration / existing-system-change / other | `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md` | none / `PHASE-xx` | initial / follows / supersedes / depends-on / blocks |

## Delivery Relationships

- Sequence constraints:
- Dependencies between deliveries:
- Supersedes / follows / blocks relationships:
- Shared constraints:

## Accepted-State Pointers

- Current system state: `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md`
- Carry-forward: `_hirmos/system/accepted-state/CARRY_FORWARD.md`
- Decision log: none / `_hirmos/system/accepted-state/DECISION_LOG.md` when explicit decision-log governance is active

## Delivery Review / Active Context

Use status-aware wording in generated artifacts. Before baseline acceptance (`PROPOSED` or `READY_FOR_BASELINE_REVIEW`), describe the delivery as `Candidate Delivery`, `Proposed Delivery`, or `Delivery Under Baseline Review`. Use `Accepted Delivery` or `Active Delivery` only after the delivery baseline has been accepted/amended and the delivery status is `ACTIVE`, `ACCEPTED`, `PARTIAL`, or another post-acceptance status.

- Delivery under review or active delivery ID: none / `<delivery-id>`
- Delivery under review or active delivery scope: none / `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md`
- Current phase: none / `_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md`
- Current/next session source:
- Current blockers:
- Carry-forward items:

## Delivery Navigation

This section makes delivery-to-delivery continuation explicit for future `hirmos start` runs. It is navigation metadata, not implementation authority.

- Last accepted delivery: none / `<delivery-id>`
- Delivery under review or active delivery: none / `<delivery-id>`
- Delivery under review or active delivery scope: none / `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md`
- Next recommended delivery: none / `<delivery-id>`
- Next recommended delivery scope: none / `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md`
- Selection rationale:
- User override / unrelated-task rule: if the user provides an unrelated task, `hirmos start` must run current-state understanding before adopting this recommendation.

## Delivery Coverage Matrix

| Delivery / accepted-state need | Delivery scope | Covered by phase(s) | Deferred? | Evidence / rationale |
|---|---|---|---:|---|
| | `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md` | none / `PHASE-xx` | NO | |

## Delivery Status Update Log

| Date/session | Delivery | Change | Previous status | New status | Evidence |
|---|---|---|---|---|---|
| | | | | | |

## Completion / Close Rules

- A delivery is complete only when its `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md` close verification passes.
- Accepted-state files must point to completed and active deliveries when durable delivery governance exists.
- New durable multi-session work must add or update a delivery entry rather than overwrite prior delivery history.
- When a delivery completes and a planned follow-up delivery is related by `follows`, `depends-on`, or an explicit sequence constraint, close must refresh Delivery Navigation and `CURRENT_SYSTEM_STATE.md` next-delivery pointers.
- The roadmap may recommend an active delivery or next phase, but implementation authority must be narrowed into `SESSION_SCOPE.md` before implementation.

## Close-Time Delivery Status Update

This section must be updated during `hirmos close` whenever a session accepts, partially accepts, blocks, supersedes, defers, cancels, or advances a delivery in this roadmap/register.


## Delivery Decomposition

Compatibility section. Delivery decomposition is represented by Delivery Index entries, each delivery's DELIVERY_SCOPE.md Phase Plan, and conditional PHASE-xx.md files.


## Active Development Context

- Delivery under review or active delivery:
- Delivery under review or active delivery scope:
- Current phase:
- Next recommended delivery:
- Next recommended delivery scope:
- Next recommended phase:
- Current blockers:

Freshness rule: after a delivery-baseline acceptance/amendment instantiates a phase, `Current phase` must point to that concrete `_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md` path. It must not remain `none` while `SESSION_STATE.json.active_phase`, `CURRENT_SYSTEM_STATE.md`, or `SESSION_SCOPE.md` identifies an active phase.

## PROD-L8.13 Status-Aware Delivery Wording

Generated delivery-roadmap text must not imply that a delivery is accepted or active before the delivery baseline is accepted. When a delivery status is `PROPOSED` or `READY_FOR_BASELINE_REVIEW`, headings, summaries, and checkpoint-facing labels must use status-aware terms such as `Candidate Delivery`, `Proposed Delivery`, or `Delivery Under Baseline Review`. Reserve `Active Delivery` for post-acceptance statuses such as `ACTIVE`, `ACCEPTED`, `PARTIAL`, `BLOCKED`, or accepted carry-forward work.

Generated artifacts should use current-state-first evidence to explain delivery shape: current system state, scope size, governance need, validation risk, continuity need, artifact authority, and practical user interaction/token cost. Project-type labels may appear as evidence metadata only when useful; they must not be the primary reason for delivery/session/phase selection. Framework testing, inspection, or dogfood context must not be used as a reason to select a heavier delivery shape.

## PROD-L8.19 Close-Time Freshness Sweep

At every close affecting this delivery, reconcile all active/pointer sections, not only the newest appended note.

| Section / pointer | Required current value | Actual value | Status | Notes |
|---|---|---|---|---|
| Active delivery | accepted/active/completed/deferred/cancelled as applicable | | PENDING | |
| Active phase | current phase or none after completion | | PENDING | |
| Current carry-forward | active item count and pointer | | PENDING | |
| Current accepted-state version / latest close | current `CURRENT_SYSTEM_STATE.md` state/version/close pointer | | PENDING | |
| Delivery Review / Active Context | not stale or explicitly historical | | PENDING | |
| Status Update Log | material phase/session transitions recorded | | PENDING | |

If an older section is retained for history, label it historical. Do not let stale active-context prose remain indistinguishable from current truth.

## PROD-L8.21 Delivery Close Concordance Sweep

At delivery close or phase close affecting this roadmap, all current pointer sections must be reconciled together. It is not enough to append a new close note while earlier active-context or accepted-state pointer sections remain stale.

| Pointer / section | Required close-time truth | Current value | Status | Notes |
|---|---|---|---|---|
| Current system state version / latest close | matches `CURRENT_SYSTEM_STATE.md` | | PENDING | |
| Active / final delivery status | matches delivery close result | | PENDING | |
| Active / final phase pointer | current phase or none after delivery completion | | PENDING | |
| Carry-forward pointer and active item count | matches `CARRY_FORWARD.md` | | PENDING | |
| Delivery Review / Active Context | current or explicitly historical | | PENDING | |
| Active Development Context | current or explicitly historical | | PENDING | |
| Delivery Status Update Log | material phase/session transitions recorded | | PENDING | |

Fail-closed rule: stale active/pointer sections block delivery-close success claims unless they are updated or explicitly labeled historical.

## PROD-L8.22 Delivery Review Gate

Delivery close requires an evidence-backed delivery review gate before claiming delivery acceptance. The delivery review gate aggregates accepted phase review gates, active/carry-forward records, runtime evidence, production posture, and final current-state pointers.

Required fields:

- Delivery reviewed:
- Phases reviewed:
- Accepted source artifacts reviewed:
- Cross-phase integration reviewed: PASS / PARTIAL / BLOCKED / FAILED / NOT_APPLICABLE
- End-to-end workflow evidence: PASS / PARTIAL / BLOCKED / FAILED / NOT_RUN / NOT_APPLICABLE
- Requirements/scope coverage posture: PASS / PARTIAL / BLOCKED / FAILED
- Runtime evidence level: NOT_CLAIMED / NOT_RUN / LOCAL_RUNTIME_VERIFIED / USER_ENVIRONMENT_VERIFIED / BLOCKED / NOT_APPLICABLE
- Production evidence level: NOT_CLAIMED / NOT_RUN / PRODUCTION_READINESS_VERIFIED / BLOCKED / NOT_APPLICABLE
- Carry-forward items affecting acceptance:
- Final delivery result: PASS / PARTIAL / BLOCKED / FAILED
- What is not claimed:
- Why this result is honest:

A delivery review must not claim full MVP/runtime/production acceptance when only implementation acceptance or static validation evidence exists. Stale delivery-plan sections must be reconciled or labeled historical before delivery close success is claimed.


## PROD-L8.23 Delivery Status Log Completeness
Generated delivery plans should make phase close chronology inspectable. When phase files exist with accepted/closed status, the Delivery Status Update Log or equivalent close chronology must include material phase close rows or explicitly state why a phase close row is not applicable. Stale active/pointer sections must be reconciled or explicitly labeled historical before final delivery close claims.


## PROD-L8.24 Generated Delivery Review Gate Validation
A generated delivery close must instantiate the delivery review gate with concrete values, not preserve it as unused template text. Required generated values include phases reviewed, accepted source artifacts reviewed, cross-phase integration reviewed, end-to-end workflow evidence, requirements/scope coverage posture, runtime evidence level, production evidence level, carry-forward impact, final delivery result, what is not claimed, and why the result is honest. The delivery close chronology must include each material phase close or explicitly classify an omitted phase close row as not applicable.

## PROD-L8.26 Delivery Close Concordance Simplification

The roadmap/register records delivery navigation and status history only. It must not duplicate full delivery evidence or full phase close records.

At delivery close, update only the compact delivery status and pointer fields needed for future navigation:

- Delivery status and final/next phase pointer;
- Delivery Status Update Log row;
- Delivery Navigation next-delivery / next-phase recommendation;
- source pointer to `DELIVERY_SCOPE.md` Compact Delivery Close Posture;
- source pointer to archive/evidence/carry-forward records.

If older active-context rows are retained, label them `historical baseline snapshot` or update them. Do not leave stale active context as current truth.

## PROD-L8.28 Active Close Concordance

Delivery/phase close posture must be reconciled with active IU execution and review state before archive. Do not mark a phase or delivery accepted/closed when applicable generated IUs remain thin, unexecuted, unreviewed, status-contradictory, or missing evidence-backed results. Use partial/blocked/route-back posture when evidence does not support clean acceptance.
