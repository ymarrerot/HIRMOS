# Evidence Review

Status: active-session evidence artifact.
Purpose: consolidate evidence claims before readiness, completion, or close is surfaced.

## Evidence Summary

Summarize what was proven, what was not proven, and what remains uncertain.

## Evidence Claims

| Claim | Evidence type | Source artifact/log/output | Result | Confidence |
|---|---|---|---|---|

Evidence types may include:

- command output;
- test result;
- build/typecheck/lint result;
- manual inspection;
- diff summary;
- screenshot/UI observation;
- data/schema verification;
- review artifact;
- not-run rationale.

## Commands Run

| Command | Context | Result | Output/log location | Notes |
|---|---|---|---|---|

## Evidence by Stack Context

Use when stack contexts are active or when evidence differs by project area.

| Stack context | Root path | Stack ID | Evidence command/check | Result | Limitation |
|---|---|---|---|---|---|

Command selection must follow repository evidence first, then stack package guidance, then explicit not-run/not-applicable rationale.

## Not Run / Not Applicable

| Check | Reason not run / not applicable | Risk | Follow-up |
|---|---|---|---|

## Scope Coverage

Map evidence back to Session Contract, Implementation Units, Design criteria, Phase Contract, or Phase Contract.

| Scope / criterion | Evidence | Result | Limitation |
|---|---|---|---|

## Evidence Limitations

List evidence gaps, uncertainty, environment limitations, dependency gaps, or command limitations.

## Blockers

List evidence blockers that prevent readiness, completion, or close.

## Handoff

State whether evidence supports:

- Implementation Completion;
- Update System State readiness;
- route-back;
- retry/escalation;
- fail-closed handling.


## Runtime Integration Evidence Review

For each material integration area, record the evidence status.

| Area | Claimed level | Evidence status | Command/log/artifact | Local runtime verified? | Production verified? | Remaining blocker |
|---|---|---|---|---:|---:|---|

Allowed evidence status values:

```text
not_run
claimed_but_not_logged
logged_command_passed
local_runtime_verified
provider_runtime_verified
production_readiness_verified
blocked
not_applicable
```

A build/typecheck/test pass is not sufficient by itself for local runtime or production-provider verification.

## Claim Reconciliation

Use this section or `_hirmos/session/support/claim-reconciliation.md` before surfacing material readiness/completion claims.

| Claim | Claim family | Evidence status | Final-file support | Runtime verified? | User environment verified? | Production readiness verified? | Result |
|---|---|---|---|---:|---:|---:|---|

Allowed evidence status values:

```text
NOT_CLAIMED
NOT_RUN
CLAIMED_NOT_LOGGED
LOGGED_COMMAND_PASSED
LOGGED_COMMAND_FAILED
LOCAL_RUNTIME_VERIFIED
USER_ENVIRONMENT_VERIFIED
PRODUCTION_READINESS_VERIFIED
BLOCKED
NOT_APPLICABLE
```

A claim with `CLAIMED_NOT_LOGGED`, `NOT_RUN`, `LOGGED_COMMAND_FAILED`, or `BLOCKED` must be downgraded or block the boundary unless explicitly outside the authorized scope.

## Autonomous Progress Evidence

| Technical action | Evidence state | Supporting artifact/log | Limitation | Claim allowed |
|---|---|---|---|---|

Use canonical evidence states from `support/claim-reconciliation.md`. Do not treat autonomous action as verified unless the evidence supports the claim.

## Local setup and role-workflow smoke evidence

Use `LOCAL_TECHNICAL_SETUP_AND_ROLE_WORKFLOW_SMOKE_CHECKS.md` for the governing rules when HIRMOS claims local runtime behavior, user-environment verification, or role workflow readiness.

Required artifacts when applicable:

- `_hirmos/session/support/local-runtime-evidence.md` records local environment, service, migration, seed, dev-server, and route evidence.
- `_hirmos/session/support/role-workflow-smoke.md` records patient/staff/provider/manager/admin workflow smoke evidence.
- `_hirmos/session/support/claim-reconciliation.md` reconciles whether the claim may be surfaced.

Firm rule: tests/build/lint alone do not prove local runtime readiness or role workflow readiness.

## Canonical Evidence Review Gate

Evidence/status fields must use only canonical values from `support/claim-reconciliation.md`.

| Evidence area | Noncanonical value found | Canonical replacement | Rationale / limitation | Pass / Blocked |
|---|---|---|---|---|
| | none / value | NOT_CLAIMED / NOT_RUN / CLAIMED_NOT_LOGGED / LOGGED_COMMAND_PASSED / LOGGED_COMMAND_FAILED / LOCAL_RUNTIME_VERIFIED / USER_ENVIRONMENT_VERIFIED / PRODUCTION_READINESS_VERIFIED / BLOCKED / NOT_APPLICABLE | | |

Do not use `observed`, `build pass`, `accepted`, `ACCEPTED_AT_CLOSE`, or similar shorthand as evidence states.
