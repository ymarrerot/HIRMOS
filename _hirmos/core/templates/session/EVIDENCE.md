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
