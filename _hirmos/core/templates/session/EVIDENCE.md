# Evidence

Status: conditional active-session evidence artifact.
Purpose: record implementation, validation, runtime, production-shaped engineering, and close-evidence in `EVIDENCE.md` or implementation units when evidence is nontrivial.

Use this artifact for implementation-capable sessions where build/test/lint/runtime/provider/storage/database/package evidence is material. Do not create it for simple design-only sessions unless evidence needs durable preservation.

## Evidence Scope

- Session ID:
- Session Scope:
- Design authority:
- Implementation units covered:
- Evidence owner / command pass:

## Command Evidence

| Evidence ID | Command/check | Working directory | Result | Output/log path or summary | Claim supported |
|---|---|---|---|---|---|
| EV-001 | | | NOT_RUN / PASSED / FAILED / BLOCKED / NOT_APPLICABLE | | |

## Runtime Integration and Provider Evidence

Record verified posture for material runtime services, provider APIs, storage, background jobs, environment validation, and local/prod parity. Do not create separate runtime-readiness, local-runtime, or role-smoke major artifact sections for new sessions.

## Runtime and Critical-Flow Evidence

| Flow / area | Evidence performed | Result | Supports production-shaped claim? | Gaps / limitations |
|---|---|---|---:|---|
| | | | | |

## Production-Shaped Engineering Evidence

| Gate area | Evidence | Result | Limitation / carry-forward if not production-shaped |
|---|---|---|---|
| Persistence / database | | | |
| Auth / authorization | | | |
| Background jobs / long-running work | | | |
| Usage / quotas / billing / quotas | | | |
| Provider APIs / external services | | | |
| File or object storage | | | |
| Secrets and environment configuration | | | |
| Tests / smoke / critical flows | | | |

## Claim Reconciliation Summary

| Claim | Evidence status | Supported? | Downgrade/blocker/action |
|---|---|---:|---|
| | NOT_CLAIMED / NOT_RUN / CLAIMED_NOT_LOGGED / LOGGED_COMMAND_PASSED / LOGGED_COMMAND_FAILED / LOCAL_RUNTIME_VERIFIED / USER_ENVIRONMENT_VERIFIED / PRODUCTION_READINESS_VERIFIED / BLOCKED / NOT_APPLICABLE | | |

## Close Evidence Handoff

- Accepted evidence:
- Evidence-only observations:
- Rejected / not-applied claims:
- Carry-forward evidence gaps:
- Accepted-state update implication:


## Close / Archive Evidence

Record evidence needed to support close claims, accepted-state updates, archive completeness, and handoff hygiene. Do not create separate close-checklist, system-state-update, archive-manifest, or claim-reconciliation support files for new sessions.

| Close evidence area | Evidence | Result | Accepted-state / carry-forward implication |
|---|---|---|---|
| Accepted outcomes | | | |
| Rejected / not-applied outcomes | | | |
| Carry-forward items | | | |
| Archive completeness | | | |
| Active-session reset readiness | | | |
| Runtime/secrets/package hygiene | | | |

## Evidence Claims

Record every material implementation claim, evidence basis, limitation, downgrade, or route-back here.

## Not Run / Not Applicable Checks

- Not Run / Not Applicable:
- Scope Coverage:
- Evidence Limitations:

## Evidence by Stack Context

Record repository evidence first, then command/runtime evidence by active stack context.

- repository evidence first:

## Runtime Integration Evidence Review

- Material Integration Areas:
- Current-Session Authorization:
- Production Readiness Checkpoint Basis:
- Update System State Carry-Forward:

## Claim Summary

- Claim Summary:
- Final-File Reconciliation:
- Command / Log Reconciliation:
- Runtime Verification Reconciliation:
- Downgraded Claims:

## Evidence Claim Reconciliation Freshness

When a blocked/not-run claim later becomes passed, or a passed claim is later contradicted, HIRMOS must reconcile the earlier record instead of leaving both statuses as current truth.

| Claim / check | Previous status | New status | Current truth | Evidence pointer | Reconciliation action |
|---|---|---|---|---|---|
| | NOT_RUN / BLOCKED / LOGGED_COMMAND_PASSED / LOCAL_RUNTIME_VERIFIED | | | | |

A material claim cannot simultaneously be current `LOGGED_COMMAND_PASSED` and current `NOT_RUN` / `BLOCKED`. Earlier failed or blocked attempts may remain as historical rows, but the current-truth row must be explicit.

## PROD-L8.21 Acceptance Evidence Semantics

HIRMOS must distinguish three acceptance levels and must not collapse them into a single `PASS` claim.

| Evidence level | Meaning | Allowed claim |
|---|---|---|
| Implementation accepted | Scope was implemented and code/static evidence passed | implementation accepted |
| Runtime verified | Local runtime/user-flow/provider behavior was exercised and passed | runtime verified |
| Production verified | Deployment/production-like constraints were exercised or explicitly assessed | production verified |

A delivery or phase may be implementation-accepted while runtime/provider/production verification remains pending, partial, blocked, or carry-forward. Close summaries must not claim full MVP/runtime/production acceptance unless the corresponding evidence level is complete.

## PROD-L8.22 Review Gate Evidence

Use this section when a session, phase, or delivery review depends on evidence in this artifact.

| Review boundary | Source authority reviewed | IU/session evidence reviewed | Actual codebase reviewed | Scope coverage result | Runtime evidence level | Production evidence level | Final result | Not claimed |
|---|---|---|---|---|---|---|---|---|
| Session implementation review |  |  | YES / NO / NOT_APPLICABLE | PASS / PARTIAL / BLOCKED / FAILED | NOT_CLAIMED / NOT_RUN / LOCAL_RUNTIME_VERIFIED / BLOCKED / NOT_APPLICABLE | NOT_CLAIMED / NOT_RUN / PRODUCTION_READINESS_VERIFIED / BLOCKED / NOT_APPLICABLE | PASS / PARTIAL / BLOCKED / FAILED |  |
| Phase review gate |  |  | YES / NO / NOT_APPLICABLE | PASS / PARTIAL / BLOCKED / FAILED | NOT_CLAIMED / NOT_RUN / LOCAL_RUNTIME_VERIFIED / BLOCKED / NOT_APPLICABLE | NOT_CLAIMED / NOT_RUN / PRODUCTION_READINESS_VERIFIED / BLOCKED / NOT_APPLICABLE | PASS / PARTIAL / BLOCKED / FAILED |  |
| Delivery review gate |  |  | YES / NO / NOT_APPLICABLE | PASS / PARTIAL / BLOCKED / FAILED | NOT_CLAIMED / NOT_RUN / LOCAL_RUNTIME_VERIFIED / BLOCKED / NOT_APPLICABLE | NOT_CLAIMED / NOT_RUN / PRODUCTION_READINESS_VERIFIED / BLOCKED / NOT_APPLICABLE | PASS / PARTIAL / BLOCKED / FAILED |  |

Review gate evidence must explain why the final result is honest. Do not use `PASS` when the evidence only supports a narrower claim.

Review gate rows must include: What is not claimed.
