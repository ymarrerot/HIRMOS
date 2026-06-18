# Role Workflow Smoke Checks

Status: session artifact template.
Purpose: record minimal role-based workflow evidence before HIRMOS claims workflow readiness.

## Smoke Check Scope

| Field | Value |
|---|---|
| Session id | |
| Delivery Unit / Phase | |
| Session Contract path | |
| Roles in scope | |
| Workflows in scope | |

## Role Workflow Matrix

| Role / actor | Workflow / route | Access method | Expected result | Observed result | Evidence state | Limitation / blocker |
|---|---|---|---|---|---|---|
| Primary user / operator | | public / token / account / not_applicable | | | NOT_RUN / CLAIMED_NOT_LOGGED / LOGGED_COMMAND_PASSED / LOGGED_COMMAND_FAILED / LOCAL_RUNTIME_VERIFIED / USER_ENVIRONMENT_VERIFIED / BLOCKED / NOT_APPLICABLE | |
| Secondary role / actor | | | | | NOT_RUN / CLAIMED_NOT_LOGGED / LOGGED_COMMAND_PASSED / LOGGED_COMMAND_FAILED / LOCAL_RUNTIME_VERIFIED / USER_ENVIRONMENT_VERIFIED / BLOCKED / NOT_APPLICABLE | |
| System / agent / service actor | | | | | NOT_RUN / CLAIMED_NOT_LOGGED / LOGGED_COMMAND_PASSED / LOGGED_COMMAND_FAILED / LOCAL_RUNTIME_VERIFIED / USER_ENVIRONMENT_VERIFIED / BLOCKED / NOT_APPLICABLE | |
| External party / integration actor | | | | | NOT_RUN / CLAIMED_NOT_LOGGED / LOGGED_COMMAND_PASSED / LOGGED_COMMAND_FAILED / LOCAL_RUNTIME_VERIFIED / USER_ENVIRONMENT_VERIFIED / BLOCKED / NOT_APPLICABLE | |

## Smoke Check Commands / Observations

| Check | Method | Result | Evidence path / excerpt |
|---|---|---|---|
| | command / browser / user observation / not_run | passed / failed / blocked / not_applicable | |

## Workflow Readiness Decision

| Decision | Value |
|---|---|
| Role workflows verified for implemented scope? | yes / no / partial |
| Unsupported claims downgraded in support/claim-reconciliation.md? | yes / no / not_applicable |
| Blocks implementation completion? | yes / no |
| Blocks production readiness? | yes / no |

Firm rule: do not claim role workflow readiness when this artifact is missing, empty, or only backed by build output.

## Mandatory Instantiation Record

Complete this section whenever role-based workflows are in scope, even if smoke checks are not run.

| Check | Value |
|---|---|
| Role workflows in implementation scope? | yes / no |
| Artifact instantiated before workflow readiness claim? | yes / no / not_applicable |
| If smoke checks not run, canonical state recorded for each workflow? | yes / no / not_applicable |
| Carry-forward pointer created for unrun/blocking smoke checks? | yes / no / not_applicable |

Firm rule: if role workflows are in scope and this artifact is missing, role workflow readiness must be `CLAIMED_NOT_LOGGED` or `BLOCKED` in `support/claim-reconciliation.md`.

## Close-Time Role Workflow Materialization

Complete when role, actor, approval, user journey, or workflow-readiness claims are in scope.

| Question | Value |
|---|---|
| Were role/workflow claims made in user-facing output, current state, or close artifacts? | yes / no |
| Was this artifact instantiated before the workflow-readiness claim? | yes / no / not_applicable |
| Are all applicable workflows listed, including unrun workflows? | yes / no / not_applicable |
| Are all evidence/status fields canonical? | yes / no |
| Unsupported workflow-readiness claims downgraded in `support/claim-reconciliation.md`? | yes / no / not_applicable |

Close must block or downgrade workflow-readiness claims when this artifact is missing, incomplete, or uses noncanonical evidence/status values for applicable workflow claims.

## Cross-Run Smoke Lesson Application

Use this section when smoke tests, scripts, or manual workflow checks are salvaged from another candidate run or prototype.

| Source candidate | Smoke lesson | Requirement / workflow | Adopted check | Meaningful assertion? | Evidence state |
|---|---|---|---|---|---|
| | | | | yes / no / partial | NOT_RUN / LOGGED_COMMAND_PASSED / LOGGED_COMMAND_FAILED / LOCAL_RUNTIME_VERIFIED / USER_ENVIRONMENT_VERIFIED / BLOCKED / NOT_APPLICABLE |

Firm rule: imported or inspired smoke checks must be reviewed for meaningful assertions before they support workflow-readiness claims.
