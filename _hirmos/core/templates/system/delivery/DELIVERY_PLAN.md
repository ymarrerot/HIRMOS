# Delivery Plan

Roadmap posture: derived from Delivery Index, delivery scopes, phase files, session archives, and accepted-state pointers. Do not maintain a writable roadmap lifecycle status here.
Last pointer refresh source:

## Purpose

Durable project delivery roadmap/register. It indexes deliveries and preserves delivery history. It is not implementation authority.

Canonical location: `_hirmos/system/delivery/DELIVERY_PLAN.md`

## Authority Boundary

`DELIVERY_PLAN.md` owns roadmap/navigation only. Delivery authority lives in `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md`; phase authority lives in instantiated `phases/PHASE-xx.md`; session implementation authority lives in `_hirmos/session/SESSION_SCOPE.md` and IU files.

Authority chain:

```text
CURRENT_SYSTEM_STATE.md
→ DELIVERY_PLAN.md
→ <delivery-id>/DELIVERY_SCOPE.md
→ <delivery-id>/unresolved-items.md
→ DELIVERY_SCOPE.md Phase Plan before phase files exist
→ <delivery-id>/phases/PHASE-xx.md when instantiated
→ SESSION_SCOPE.md
→ implementation-units / EVIDENCE / SESSION_LEDGER.md
```

## Delivery Shape Source

Compatibility label: Delivery-Need Classification Source.

Compact delivery-shape and phase-count decision. Do not duplicate delivery scope or phase contents here.

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

Before baseline acceptance, delivery entries are candidate/proposed only. Future phases are represented by the phase coverage plan in `DELIVERY_SCOPE.md`; concrete future `PHASE-xx.md` paths must not be referenced unless those files exist. After acceptance, instantiate the next phase/session authority just in time.

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

Use status-aware wording. Before baseline acceptance use `Candidate Delivery`, `Proposed Delivery`, or `Delivery Under Baseline Review`; use `Active Delivery` only after accepted/amended post-acceptance status.

- Delivery under review or active delivery ID: none / `<delivery-id>`
- Delivery under review or active delivery scope: none / `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md`
- Current phase: none / `_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md`
- Current/next session source:
- Current blockers:
- Carry-forward items:

## Delivery Navigation

Navigation metadata only; not implementation authority.

- Last accepted delivery: none / `<delivery-id>`
- Delivery under review or active delivery: none / `<delivery-id>`
- Delivery under review or active delivery scope: none / `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md`
- Next recommended delivery: none / `<delivery-id>`
- Next recommended delivery scope: none / `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md`
- Selection rationale:
- User override / unrelated-task rule: if unrelated, run current-state understanding before adopting this recommendation.

## Delivery Coverage Matrix

Compact coverage index only. Detailed scope and acceptance live in `DELIVERY_SCOPE.md` and phase/session/IU artifacts.

| Delivery / accepted-state need | Delivery scope | Covered by phase(s) | Deferred? | Evidence / rationale |
|---|---|---|---:|---|
| | `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md` | none / `PHASE-xx` | NO | |

## Delivery Status Pointer Index

Derived navigation index only. Do not maintain a narrative delivery status update log here. Delivery status transitions are owned by `DELIVERY_SCOPE.md` close posture, phase close records, session archives, and `CURRENT_SYSTEM_STATE.md` latest-close pointers.

| Delivery | Current status label | Owning status source | Latest evidence pointer | Notes |
|---|---|---|---|---|
| `<delivery-id>` | proposed / active / accepted / partial / blocked / deferred / complete | `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md` | archive/evidence pointer | |

## Completion / Close Rules

- A delivery is complete only when its `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md` close verification passes.
- Accepted-state files must point to completed and active deliveries when durable delivery governance exists.
- New durable multi-session work must add or update a delivery entry rather than overwrite prior delivery history.
- When a delivery completes and a related follow-up delivery exists, close must refresh Delivery Navigation and `CURRENT_SYSTEM_STATE.md` next-delivery pointers.
- The roadmap may recommend an active delivery or next phase, but implementation authority must be narrowed into `SESSION_SCOPE.md` before implementation.

## Close-Time Delivery Pointer Refresh

During `hirmos close`, refresh only derived pointer/index rows whose source artifact changed or explicitly mark them derived/stale. Do not maintain a narrative Delivery Delivery Status Pointer Index and do not duplicate close evidence.

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

Freshness rule: after delivery-baseline acceptance/amendment instantiates a phase, `Current phase` must point to the concrete `_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md` path. It must not remain `none` while `SESSION_STATE.json.active_phase`, `CURRENT_SYSTEM_STATE.md`, or `SESSION_SCOPE.md` identifies an active phase.

## PROD-L8.13 Status-Aware Delivery Wording

Generated artifacts must not imply acceptance before baseline acceptance. Framework testing, inspection, or dogfood context must not justify a heavier delivery shape. Delivery shape must be justified by real software work and user interaction / token-cost impact.

## PROD-L8.19 Close-Time Freshness Sweep

Compact sweep; every current pointer must be refreshed, explicitly verified unchanged, or marked not stale or explicitly historical.

| Section / pointer | Required current value | Actual value | Status | Notes |
|---|---|---|---|---|
| Active delivery | accepted/active/completed/deferred/cancelled as applicable | | PENDING | |
| Active phase | current phase or none after completion | | PENDING | |
| Current carry-forward | active item count and pointer | | PENDING | |
| Current accepted-state version / latest close | current `CURRENT_SYSTEM_STATE.md` state/version/close pointer | | PENDING | |
| Delivery Review / Active Context | not stale | | PENDING | |

## PROD-L8.21 Delivery Close Concordance Sweep

At delivery close, `DELIVERY_PLAN.md`, `DELIVERY_SCOPE.md`, phase files, `CURRENT_SYSTEM_STATE.md`, `CARRY_FORWARD.md`, `EVIDENCE.md`, archive manifest, and `SESSION_LEDGER.md` must agree on the delivery/phase result.

## PROD-L8.22 Delivery Review Gate

Review gate pointer only. The detailed review result lives in `DELIVERY_SCOPE.md` and evidence/session artifacts. Required delivery review summary includes End-to-end workflow evidence and What is not claimed.

## PROD-L8.23 Delivery Status Log Completeness

Every delivery status transition must be traceable through owning close/session/archive artifacts and the Delivery Status Pointer Index. Do not duplicate phase close chronology or evidence detail in DELIVERY_PLAN.md.

## PROD-L8.24 Generated Delivery Review Gate Validation

Generated review values must include why the result is honest.

Generated roadmap files must instantiate current status/pointer rows with concrete values when a delivery is accepted, partial, blocked, deferred, superseded, cancelled, or complete.

## PROD-L8.26 Delivery Close Concordance Simplification

`DELIVERY_PLAN.md` remains roadmap/register only; roadmap/register records delivery navigation and status pointers only. It must point to source artifacts instead of duplicating implementation, runtime, production, evidence, unresolved, or session detail.

## PROD-L8.28 Active Close Concordance

Stale active/pointer sections block delivery-close success claims. Close is invalid if active delivery/phase pointers are stale, missing, or inconsistent with `SESSION_STATE.json`, `CURRENT_SYSTEM_STATE.md`, `DELIVERY_SCOPE.md`, or active phase files.

## PROD-L8.32L Derived Delivery Index Contract

`DELIVERY_PLAN.md` owns the roadmap/register, but its status and pointer rows are derived navigation caches over delivery scope files, phase files, current-state pointers, and archive manifests. Do not maintain a narrative delivery status log as independent truth.

When possible, derive the Delivery Index and Delivery Status Pointer Index from filesystem paths under `_hirmos/system/delivery/`, active phase/session pointers, and close/archive manifests. If the derived index conflicts with a delivery or phase source artifact, the source artifact wins and the roadmap row must be reconciled before status, continue, or close claims.


## PROD-L8.32Q Delivery Status Log Removal

`DELIVERY_PLAN.md` is roadmap/register plus derived navigation pointers. It must not contain a narrative `Delivery Status Update Log`. Delivery chronology and completion evidence are traceable through source artifacts: delivery scope close posture, phase files, session archives, archive manifests, evidence records, and accepted-state pointers.

Generated roadmap/register files that recreate a narrative `## Delivery Status Update Log` are stale-surface regressions. Use the Delivery Status Pointer Index and derived concordance output instead.

## PROD-L8.32R Roadmap Status Derivation

`DELIVERY_PLAN.md` must not maintain a writable top-level `Roadmap status:` field. Roadmap posture is derived from Delivery Index rows, delivery scope authority, phase lifecycle status, session archives, archive manifests, and accepted-state pointers. If generated artifacts recreate `Roadmap status: ACTIVE` / `COMPLETE` / similar top-level status while delivery completion is also derived elsewhere, status/close must fail closed and remove the duplicated mutable field.
