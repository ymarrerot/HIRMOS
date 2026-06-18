# Local Technical Setup Evidence

Status: session artifact template.
Purpose: record concrete local technical setup evidence for runtime claims.

## Setup Context

| Field | Value |
|---|---|
| Session id | |
| Project root | |
| Stack context | |
| Package manager | |
| Node/Python/runtime version when relevant | |
| User environment involved | yes / no / unknown |

## Environment and Secrets

| Variable / file | Required for | Present during run | Redacted before package | Evidence / notes |
|---|---|---|---|---|
| | | yes / no / unknown | yes / no / not_applicable | |

## Local Services

| Service | Detection attempted | Result | Connection / port | Action taken | Evidence state |
|---|---|---|---|---|---|
| Database | yes / no | reachable / not_reachable / not_checked | | created / reused / blocked / not_applicable | |
| Dev server | yes / no | started / failed / not_checked | | | |

## Setup Commands

| Command | Working directory | Result | Evidence state | Log path or excerpt | Notes |
|---|---|---|---|---|---|
| | | passed / failed / not_run / blocked | NOT_RUN / CLAIMED_NOT_LOGGED / LOGGED_COMMAND_PASSED / LOGGED_COMMAND_FAILED / LOCAL_RUNTIME_VERIFIED / USER_ENVIRONMENT_VERIFIED / BLOCKED / NOT_APPLICABLE | | |

## Runtime Setup Claims

| Claim | Supported status | Evidence | Limitation |
|---|---|---|---|
| Dependencies installed | | | |
| Database migrated | | | |
| Database seeded | | | |
| Dev server responds | | | |
| Local app route verified | | | |

## Blockers and Follow-Up

| Blocker | Owner | Required action | Blocks local runtime readiness? | Blocks production readiness? |
|---|---|---|---|---|
| | | | yes / no | yes / no |

Firm rule: build success is not local setup evidence unless the local setup claim is specifically build-only.

## Close-Time Local Setup Materialization

Complete when local setup/runtime evidence is required for close.

| Question | Value |
|---|---|
| Was local setup/runtime claimed in user-facing output, current state, or close artifacts? | yes / no |
| Was this artifact instantiated before the claim? | yes / no / not_applicable |
| Are all evidence/status fields canonical? | yes / no |
| Missing secrets or local blockers carried forward? | yes / no / not_applicable |
| Unsupported local-readiness claims downgraded in `support/claim-reconciliation.md`? | yes / no / not_applicable |

Close must block or downgrade local runtime/setup readiness claims when this section is missing or incomplete for an applicable claim.
