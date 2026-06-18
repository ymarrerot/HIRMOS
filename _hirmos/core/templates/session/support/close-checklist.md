# Close Checklist

Status: active-session close artifact.
Purpose: verify that Update System State, archive, and active-session reset are safe.


## Contract-Centered Close / Archive / Reset Gate

This checklist is a generated or transition close surface. It must not override `SESSION_CONTRACT.md`, `session-contract-review.md`, `unresolved-items.md`, `SESSION_EXECUTION.md`, or accepted-state artifacts.

| Gate | Required result | Evidence | Status |
|---|---|---|---|
| Session Contract Review completed | `session-contract-review.md` final verdict is `PASS` or explicitly deferred/blocked | | PENDING |
| Unresolved register reconciled | `unresolved-items.md` has no close-blocking gated item | | PENDING |
| Implementation units reviewed | every applicable `implementation-units/IU-xx.md` has Unit Review and Result | | PENDING |
| Accepted-state merge completed | `CURRENT_SYSTEM_STATE.md` latest-close metadata and current truth updated or verified unchanged | | PENDING |
| Active-only carry-forward updated | `CARRY_FORWARD.md` contains active items only | | PENDING |
| Archive manifest created | archive contains `support/archive-manifest.md` with complete artifact inventory | | PENDING |
| Archived session state normalized | archived `SESSION_STATE.json` is closed / archived / history_only | | PENDING |
| Active session reset | active `_hirmos/session/` contains only allowed idle scaffolding | | PENDING |
| Stale active artifacts absent | no `SESSION_CONTRACT.md`, `SESSION_EXECUTION.md`, `unresolved-items.md`, `session-contract-review.md`, `IU-*.md`, checkpoint, or support runtime artifact remains active | | PENDING |

Allowed idle scaffolding after normal close:

```text
_hirmos/session/.gitkeep
_hirmos/session/SESSION_STATE.json
_hirmos/session/bootstrap/.gitkeep
_hirmos/session/checkpoints/.gitkeep
_hirmos/session/implementation-units/.gitkeep
_hirmos/session/support/.gitkeep
```

Firm rule: if any row above is `PENDING`, `BLOCKED`, missing, or contradictory, close success must not be claimed.

## Close Type

- NORMAL_CLOSE | ABORT_CLOSE | BLOCKED_CLOSE
- Requested by:
- Session ID:

## Update System State Readiness

| Check | Status | Evidence | Notes |
|---|---|---|---|

Required checks:

- accepted outcomes identified;
- rejected/not-applied outcomes identified;
- evidence-only artifacts identified;
- carry-forward unresolved items recorded;
- no new Design or Implementation needed during close.

## Archive Readiness

| Check | Status | Evidence | Notes |
|---|---|---|---|

Required checks:

- `SESSION_EXECUTION.md` ready to archive;
- all active session artifacts included;
- implementation subfolder included when present;
- update-state artifacts included;
- archive path available.

## Active Session Reset

State the reset plan for `_hirmos/session/` after successful normal close.

## Blocked / Abort Notes

For blocked or abort close, record what was preserved and why no accepted-state claim is made.

## Close Decision

- CLOSED_ARCHIVED | CLOSE_BLOCKED | ABORT_ARCHIVED
- Archive path:
- Active session reset status:

## System State Update Link

- support/system-state-update.md exists: yes / no
- Accepted outcomes separated from evidence-only artifacts: yes / no
- Carry-forward items recorded: yes / no / not applicable
- Future session readiness stated: yes / no


## Runtime Integration Close Gate

Before normal close, verify:

- material integration posture is recorded or not applicable;
- implementation completion claims do not exceed evidence;
- production-readiness claims are backed by production-readiness evidence;
- unresolved production blockers are carried forward;
- accepted system state records integration limitations.

Close must block or downgrade the claim if integration posture and evidence do not support the claimed outcome.

## Close Output and Next Slice

Before reporting close success, prepare a concise close output that includes:

- accepted outcomes;
- archive path;
- carry-forward unresolved items;
- production-readiness or evidence limitations;
- next recommended Delivery Unit or next command/action.

The next recommendation must be backed by existing Delivery Plan authority and must not imply unauthorized Implementation.

## Accepted-State Integrity Checks

| Check | Status | Evidence | Notes |
|---|---|---|---|
| Accepted outcomes are separated from rejected / not-applied outcomes | PENDING | | |
| Evidence-only artifacts are not treated as accepted state | PENDING | | |
| Current-state latest-close metadata updated only with accepted outcomes | PENDING | | |
| Carry-forward items updated | PENDING | | |
| Runtime integration limitations preserved | PENDING | | |
| Delivery Unit / Phase status reconciled | PENDING | | |

## Archive Manifest Checks

| Check | Status | Evidence | Notes |
|---|---|---|---|
| Archive manifest created | PENDING | | |
| Complete active session artifact set archived | PENDING | | |
| Missing archive exceptions recorded | PENDING | | |
| Archive path agrees with support/system-state-update.md | PENDING | | |

## Post-Close Consistency Checks

| Surface | Expected value | Actual value | Consistent |
|---|---|---|---|
| `SESSION_STATE.json` | idle / no active governed session | | yes / no |
| Archive manifest | archive complete or abort archived | | yes / no |
| Current-state latest-close metadata | accepted outcomes applied | | yes / no |
| Carry-forward record | unresolved/carry-forward items preserved | | yes / no |
| `hirmos status` | latest archive and accepted-state pointer | | yes / no |

If any post-close consistency check fails, close success must not be claimed.

## Claim Reconciliation Close Gate

Before normal close, reconcile close and accepted-state claims.

| Claim | Evidence status | Accepted-state support | Archive support | Session reset support | Result |
|---|---|---|---|---|---|

Close is blocked if close success would contradict accepted state, archive manifest, active session state, carry-forward records, or known evidence gaps.

## archive/session-state integrity Archive-State Consistency Gate

Normal close is blocked unless every item below is satisfied.

| Check | Required result | Actual result | Pass / Blocked |
|---|---|---|---|
| support/claim-reconciliation.md exists when material claims were made | exists / not_applicable | | |
| Pre-close session state preserved | PRE_CLOSE_SESSION_STATE.json or ARCHIVE_MANIFEST section | | |
| Archived SESSION_STATE.json is not active | closed / archived / history_only | | |
| Active `_hirmos/session/SESSION_STATE.json` after close is idle | idle / no active session | | |
| support/archive-manifest.md records post-close verification | consistent | | |
| Current-state latest-close metadata matches accepted outcomes | consistent | | |
| Carry-forward records preserved | consistent / not_applicable | | |

Firm rule: if any result is missing, unchecked, or contradictory, surface `Close Blocked`; do not claim normal close success.



## Delivery Pointer Close Gate


## Durable Phase Adoption Close Gate

Required when Delivery-Need Classification is `YES`.

| Close check | Required evidence | Status |
|---|---|---|
| Exactly one durable phase was adopted for implementation | `SESSION_CONTRACT.md` Active Durable Phase Adoption | PENDING |
| Adopted phase was reviewed directly | `session-contract-review.md` Durable Phase Adoption Review | PENDING |
| Accepted / partial / blocked phase result is recorded | `support/system-state-update.md` and Delivery Plan status update | PENDING |
| Current System State delivery pointers reflect the resulting phase state | `CURRENT_SYSTEM_STATE.md` Active Development Context and Delivery Pointers | PENDING |

Close is blocked if adopted phase status, Delivery Plan status, session-contract-review verdict, and Current System State delivery pointers cannot be reconciled.


Normal close is blocked when delivery governance was active, required, or changed and Current System State delivery pointers are not reconciled.

| Gate | Required result | Evidence | Status |
|---|---|---|---|
| Active delivery ID reconciled | yes / not_applicable | `support/system-state-update.md` Delivery Pointer Accepted-State Update | PENDING |
| Delivery Plan pointer reconciled | yes / not_applicable | `_hirmos/system/delivery/<delivery-id>/DELIVERY_PLAN.md` | PENDING |
| Active phase pointer reconciled | yes / not_applicable | `_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md` | PENDING |
| Active phase status reconciled | yes / not_applicable | phase/session review evidence | PENDING |
| Next phase / next command reconciled | yes / not_applicable | Delivery Plan, `SESSION_STATE.json`, close decision | PENDING |
| Stale delivery pointer scan complete | yes | Current System State pointer section | PENDING |

Firm rule: do not claim close success if Current System State still points to a stale active delivery or phase.

## Local setup and role-workflow smoke evidence

Use `LOCAL_TECHNICAL_SETUP_AND_ROLE_WORKFLOW_SMOKE_CHECKS.md` for the governing rules when HIRMOS claims local runtime behavior, user-environment verification, or role workflow readiness.

Required artifacts when applicable:

- `_hirmos/session/support/local-runtime-evidence.md` records local environment, service, migration, seed, dev-server, and route evidence.
- `_hirmos/session/support/role-workflow-smoke.md` records patient/staff/provider/manager/admin workflow smoke evidence.
- `_hirmos/session/support/claim-reconciliation.md` reconciles whether the claim may be surfaced.

Firm rule: tests/build/lint alone do not prove local runtime readiness or role workflow readiness.

## durable current-system-state Durable Current-State Close Gate

| Gate | Required result | Evidence | Status |
|---|---|---|---|
| `CURRENT_SYSTEM_STATE.md` exists | yes | | PENDING |
| accepted outcomes mapped to current-state sections | yes | | PENDING |
| rejected / evidence-only outcomes excluded from current truth | yes | | PENDING |
| `DECISION_LOG.md` updated for durable decisions | yes / not_applicable | | PENDING |
| `CARRY_FORWARD.md` updated for active carry-forward items | yes / not_applicable | | PENDING |
| `CURRENT_SYSTEM_STATE.md` latest-close metadata points to updated current state and latest archive | yes | | PENDING |
| `CURRENT_SYSTEM_STATE.md` active delivery pointers updated or verified unchanged | yes / not_applicable | | PENDING |
| production readiness tracks remain separated | yes | | PENDING |
| post-close status would report current truth from `CURRENT_SYSTEM_STATE.md` | yes | | PENDING |

Normal close is blocked until these gates are satisfied or explicitly not applicable with rationale.

## Accepted-State Invariant and Canonical Value Gate

Normal close is blocked until these checks pass.

| Check | Required result | Evidence | Status |
|---|---|---|---|
| Accepted-state invariant blocks preserved | yes | | PENDING |
| Runtime posture fields use canonical values only | yes / not_applicable | | PENDING |
| Evidence/status fields use canonical values only | yes / not_applicable | | PENDING |
| Accepted-state decisions are not used as evidence states | yes | | PENDING |
| `support/role-workflow-smoke.md` exists when role workflows are in scope | yes / not_applicable | | PENDING |
| Clean package/review exclusions checked when package is produced | yes / not_applicable | | PENDING |

Firm rule: if any accepted-state invariant gate is missing, unchecked, or contradictory, surface `Close Blocked` instead of claiming normal close success.

## Close-Time Compliance Gate and Evidence Materialization

Normal close is blocked until every applicable row is satisfied.

| Gate | Trigger | Required artifact / result | Actual evidence | Status |
|---|---|---|---|---|
| Close claim reconciliation materialized | normal close | `_hirmos/session/support/claim-reconciliation.md` exists and reconciles close/archive/update-state claims | | PENDING |
| Implementation evidence materialized | Implementation was active | `support/session-implementation-review.md` and `support/evidence-review.md` exist or are explicitly not applicable with rationale | | PENDING |
| Local setup evidence materialized | local runtime/database/provider/setup/seed/dev-server/route/user-environment claim | `support/local-runtime-evidence.md` exists with canonical evidence states | | PENDING |
| Role workflow smoke materialized | role/actor/approval/journey/workflow claim | `support/role-workflow-smoke.md` exists with checked or `NOT_RUN`/`BLOCKED` workflows | | PENDING |
| Runtime integration posture materialized | runtime provider/integration claim | `support/runtime-integration-readiness.md` exists with canonical posture values | | PENDING |
| Framework validator gate | framework files changed or accepted-state invariants involved | `python3 _hirmos/tools/validate.py = PASS` or `NOT_RUN` recorded without compliance claim | | PENDING |
| Canonical structured-value scan | normal close | no noncanonical evidence/status/runtime posture values remain in structured fields | | PENDING |
| Accepted-state invariant scan | normal close | invariant blocks preserved in all accepted-state artifacts | | PENDING |
| Package cleanliness gate | package/export/review package produced | dirty/secret/generated files excluded or explicitly labeled; clean-package claim reconciled | | PENDING |

Firm rule: if any required close-time compliance gate is `PENDING`, `BLOCKED`, missing, or contradictory, surface `Close Blocked`, not close success.

## Requirements Coverage Close Gate

- [ ] `_hirmos/session/REQUIREMENTS_BASELINE.md` exists when material requirements affected the session.
- [ ] Material source inputs are inventoried and classified.
- [ ] In-scope requirements have stable IDs and source references.
- [ ] Delivery mapping is complete or explicitly deferred/blocked/not applicable.
- [ ] Coverage status is updated before close.
- [ ] `_hirmos/system/accepted-state/REQUIREMENTS_BASELINE.md` is updated when requirements remain relevant across sessions.
- [ ] `CURRENT_SYSTEM_STATE.md` references the accepted requirements baseline and does not replace it.


## Delivery Plan / Phase Status Close Gate

Required when delivery governance was active, required, created, changed, accepted, blocked, superseded, or advanced.

| Gate | Required result | Evidence | Status |
|---|---|---|---|
| Close-time delivery transaction recorded | `support/system-state-update.md` Close-Time Delivery / Phase Status Transaction is complete | | PENDING |
| Adopted phase status updated or verified unchanged | active `PHASE-xx.md` Close-Time Phase Status Update Contract | | PENDING |
| Parent Delivery Plan status updated | `DELIVERY_PLAN.md` phase row and Delivery Status Update Log | | PENDING |
| Current System State pointers refreshed | `CURRENT_SYSTEM_STATE.md` Active Development Context and Delivery Pointers | | PENDING |
| Carry-forward delivery obligations recorded | `CARRY_FORWARD.md`, next `PHASE-xx.md`, or unresolved-items disposition | | PENDING |
| Delivery status concordance checked | Delivery Plan, Phase, Session Contract, session-contract-review, IU reviews, and pointers agree | | PENDING |

Close is blocked if any required delivery status surface is missing, stale, contradictory, or only summarized in chat/archive without updating the durable Delivery Plan and Phase file.

## Phase Entry Gate Close Check

For delivery-governed sessions, close must verify that implementation was authorized only after the Phase Entry Gate passed.

Close is blocked if:

- Phase Entry Gate evidence is missing from `SESSION_CONTRACT.md` or `SESSION_EXECUTION.md`.
- The adopted phase lifecycle status did not support adoption.
- Required greenfield/brownfield/mixed entry controls were not satisfied.
- Pointer concordance was not checked before implementation readiness.

## Phase Progress / Carry-Forward Close Check

Required for delivery-governed close.

- Durable Phase Progress Ledger updated or verified unchanged: yes / no / not_applicable
- Completed, partial, blocked, and deferred phase items classified: yes / no / not_applicable
- Carry-forward obligations recorded for non-accepted phase outcome: yes / no / not_applicable
- Delivery Plan agrees with resulting phase status: yes / no / not_applicable
- Current System State points to active/next phase after close: yes / no / not_applicable

Close is blocked when the adopted phase outcome is `PARTIAL`, `BLOCKED`, or `DEFERRED` and carry-forward obligations are missing.


## Phase Acceptance Close Check

If the adopted durable phase is being marked `ACCEPTED`, close is blocked unless:

- Phase Acceptance Evidence Gate is PASS;
- `session-contract-review.md` records Phase acceptance verdict: ACCEPTED;
- `support/system-state-update.md` records Phase acceptance status: ACCEPTED and Phase acceptance evidence status: COMPLETE;
- Delivery Plan / Phase / Current System State updates are applied or explicitly verified unchanged;
- Greenfield acceptance evidence is complete when applicable;
- Brownfield acceptance evidence is complete when applicable;
- no unresolved adopted work remains except explicitly deferred/excluded work with rationale.
