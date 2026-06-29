# Evidence

Status: conditional active-session evidence artifact.
Purpose: compact source authority for material command, runtime, provider, production-shaped engineering, claim reconciliation, review-gate, and close/archive evidence.

Use this artifact only when evidence is nontrivial or cannot be captured clearly in implementation-unit records. Do not duplicate scope, IU contracts, session ledger events, delivery posture, or accepted-state summaries. `SESSION_LEDGER.md` records only gate/event pointers to this artifact.

## Evidence Scope

| Field | Value |
|---|---|
| Session ID | |
| Session Scope | `_hirmos/session/SESSION_SCOPE.md` |
| Design authority | none / path |
| Implementation units covered | none / IU paths |
| Evidence owner / command pass | |

## Command Evidence

| Evidence ID | Command/check | Working directory | Result | Output/log path or summary | Claim supported |
|---|---|---|---|---|---|
| EV-001 | | | NOT_RUN / PASSED / FAILED / BLOCKED / NOT_APPLICABLE | | |

## Runtime Integration and Provider Evidence

Record only material runtime/provider/storage/database/job/environment evidence. Do not create separate runtime-readiness, local-runtime, or role-smoke major artifact sections.

## Runtime and Critical-Flow Evidence

| Flow / area | Evidence performed | Result | Supports production-shaped claim? | Gaps / limitations |
|---|---|---|---:|---|
| | | NOT_RUN / PASSED / FAILED / BLOCKED / NOT_APPLICABLE | YES / NO | |

## Production-Shaped Engineering Evidence

| Gate area | Evidence | Result | Limitation / carry-forward if not production-shaped |
|---|---|---|---|
| Persistence / database | | | |
| Auth / authorization | | | |
| Background jobs / long-running work | | | |
| Usage / credits / quotas / billing | | | |
| Provider APIs / external services | | | |
| File or object storage | | | |
| Secrets and environment configuration | | | |
| Tests / smoke / critical flows | | | |
| Deployment / production constraints | | | |

## Evidence Claims

Record every material implementation, runtime, provider, production, package, or close claim that needs evidence. Keep claims compact and source-linked.

## Claim Reconciliation Summary

| Claim | Evidence status | Supported? | Current truth | Downgrade/blocker/action |
|---|---|---:|---|---|
| | NOT_CLAIMED / NOT_RUN / CLAIMED_NOT_LOGGED / LOGGED_COMMAND_PASSED / LOGGED_COMMAND_FAILED / LOCAL_RUNTIME_VERIFIED / USER_ENVIRONMENT_VERIFIED / PRODUCTION_READINESS_VERIFIED / BLOCKED / NOT_APPLICABLE | YES / NO | | |

## Evidence Claim Reconciliation Freshness

When a blocked/not-run claim later becomes passed, or a passed claim is later contradicted, reconcile the earlier record instead of leaving both statuses as current truth.

| Claim / check | Previous status | New status | Current truth | Evidence pointer | Reconciliation action |
|---|---|---|---|---|---|
| | NOT_RUN / BLOCKED / LOGGED_COMMAND_PASSED / LOCAL_RUNTIME_VERIFIED | | | | |

A material claim cannot simultaneously be current `LOGGED_COMMAND_PASSED` and current `NOT_RUN` / `BLOCKED`.

## Not Run / Not Applicable Checks

- Scope Coverage:
- Evidence Limitations:

| Check / flow | Status | Reason | Carry-forward / limitation | Source |
|---|---|---|---|---|
| | NOT_RUN / NOT_APPLICABLE / BLOCKED | | | |

## Evidence by Stack Context

Record repository evidence first, then command/runtime evidence by active stack context.

- repository evidence first:

## Runtime Integration Evidence Review

| Material Integration Areas | Current-Session Authorization | Production Readiness Checkpoint Basis | Update System State Carry-Forward |
|---|---|---|---|
| | | | |

## Claim Summary

| Claim Summary | Final-File Reconciliation | Command / Log Reconciliation | Runtime Verification Reconciliation | Downgraded Claims |
|---|---|---|---|---|
| | | | | |

## Close Evidence Handoff

| Accepted evidence | Evidence-only observations | Rejected / not-applied claims | Carry-forward evidence gaps | Accepted-state update implication |
|---|---|---|---|---|
| | | | | |

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

## PROD-L8.21 Acceptance Evidence Semantics

HIRMOS must distinguish three acceptance levels and must not collapse them into a single `PASS` claim: implementation accepted, runtime verified, production verified. A delivery or phase may be implementation-accepted while runtime/provider/production verification remains pending, partial, blocked, or carry-forward.

## PROD-L8.22 Review Gate Evidence

Use this section when a session, phase, or delivery review depends on evidence in this artifact.

| Review boundary | Source authority reviewed | IU/session evidence reviewed | Actual codebase reviewed | Scope coverage result | Runtime evidence level | Production evidence level | Final result | Not claimed |
|---|---|---|---|---|---|---|---|---|
| Session implementation review | | | YES / NO / NOT_APPLICABLE | PASS / PARTIAL / BLOCKED / FAILED | NOT_CLAIMED / NOT_RUN / LOCAL_RUNTIME_VERIFIED / BLOCKED / NOT_APPLICABLE | NOT_CLAIMED / NOT_RUN / PRODUCTION_READINESS_VERIFIED / BLOCKED / NOT_APPLICABLE | PASS / PARTIAL / BLOCKED / FAILED | |
| Phase review gate | | | YES / NO / NOT_APPLICABLE | PASS / PARTIAL / BLOCKED / FAILED | NOT_CLAIMED / NOT_RUN / LOCAL_RUNTIME_VERIFIED / BLOCKED / NOT_APPLICABLE | NOT_CLAIMED / NOT_RUN / PRODUCTION_READINESS_VERIFIED / BLOCKED / NOT_APPLICABLE | PASS / PARTIAL / BLOCKED / FAILED | |
| Delivery review gate | | | YES / NO / NOT_APPLICABLE | PASS / PARTIAL / BLOCKED / FAILED | NOT_CLAIMED / NOT_RUN / LOCAL_RUNTIME_VERIFIED / BLOCKED / NOT_APPLICABLE | NOT_CLAIMED / NOT_RUN / PRODUCTION_READINESS_VERIFIED / BLOCKED / NOT_APPLICABLE | PASS / PARTIAL / BLOCKED / FAILED | |

Review gate evidence must explain why the final result is honest. Do not use `PASS` when the evidence only supports a narrower claim. Review gate rows must include: What is not claimed.


## Conditional Evidence Detail Rule

Active `EVIDENCE.md` detail is required only when evidence volume, claim reconciliation, review-gate evidence, or close/archive handoff cannot be represented safely as `SESSION_LEDGER.md` evidence pointers. Otherwise, the ledger records evidence pointers and close/archive artifacts preserve the durable evidence handoff.

Evidence detail must not duplicate session scope, IU contracts, delivery status, phase progress, current-state summaries, or carry-forward detail.

## PROD-L8.32L Evidence JIT Creation Rule

Do not create this artifact by default. Create active `EVIDENCE.md` only when evidence detail cannot be represented safely by IU review rows, `SESSION_LEDGER.md` evidence pointers, command output snippets, or archive handoff metadata.

If this artifact is absent because it is not yet applicable, ledger/status output must say evidence detail is represented by pointers or is not applicable. If a material claim needs claim reconciliation, review-gate evidence, runtime/provider evidence, production-shaped evidence, or close/archive evidence handoff, create this artifact before surfacing the claim.
