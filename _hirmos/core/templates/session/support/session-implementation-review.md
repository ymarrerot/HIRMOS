# Session Implementation Review

Status: active-session Implementation review artifact.
Purpose: determine whether the implemented session scope is complete after all implementation units and evidence reviews.

## Governing Session Contract

- Session Contract:
- Implementation Unit Plan:
- Delivery Plan / Phase Contract / Phase Contract:
- Implementation Readiness artifact:

## Unit Coverage

| Scope item | Unit(s) | Review result | Evidence | Notes |
|---|---|---|---|---|

## Implementation Unit Results

| Unit ID | Request artifact | Execution artifact | Review artifact | Result | Retry needed? | Notes |
|---|---|---|---|---|---:|---|

## Evidence Summary

Reference `support/evidence-review.md` and summarize whether required evidence exists.

## Validation / Evidence Gate

| Required evidence | Present? | Result | Limitation | Blocks completion? |
|---|---:|---|---|---:|

## Remaining Issues

List unresolved implementation issues, non-gating limitations, blockers, or route-back triggers.

## Scope Completion Decision

- IMPLEMENTATION_COMPLETE | COMPLETE_WITH_LIMITATIONS | BLOCKED | FAILED | ROUTE_BACK_REQUIRED | NOT_APPLICABLE
- Rationale:
- Remaining limitations:
- User/technical supervisor attention required:
- Next allowed action:

## Handoff to Update System State

State what accepted outcomes, rejected outcomes, evidence-only records, and carry-forward items should be considered by Update System State.

## Update System State Readiness Contribution

- Ready to consider Update System State:
- Required controls satisfied:
- Required controls still pending/blocked:


## Runtime Integration Completion Review

Before claiming Implementation completion, confirm the delivered integration posture matches the Session Contract.

| Area | Authorized posture | Delivered posture | Evidence sufficient? | Completion impact |
|---|---|---|---:|---|

Implementation completion wording must name limitations when material areas remain fixture-backed, boundary-only, local-only, blocked, or unverified.

## Claim Reconciliation

Session implementation completion cannot be claimed until all material unit and session-level implementation claims are reconciled.

| Session claim | Evidence status | Supporting unit/review | Final-file support | Limitation | Result |
|---|---|---|---|---|---|

Record whether build/test success, local runtime verification, user-environment verification, integration verification, and production-readiness verification are distinct and truthful.

## Local setup and role-workflow smoke evidence

Use `LOCAL_TECHNICAL_SETUP_AND_ROLE_WORKFLOW_SMOKE_CHECKS.md` for the governing rules when HIRMOS claims local runtime behavior, user-environment verification, or role workflow readiness.

Required artifacts when applicable:

- `_hirmos/session/support/local-runtime-evidence.md` records local environment, service, migration, seed, dev-server, and route evidence.
- `_hirmos/session/support/role-workflow-smoke.md` records patient/staff/provider/manager/admin workflow smoke evidence.
- `_hirmos/session/support/claim-reconciliation.md` reconciles whether the claim may be surfaced.

Firm rule: tests/build/lint alone do not prove local runtime readiness or role workflow readiness.
