# Claim Reconciliation

Status: active-session evidence artifact.
Purpose: reconcile HIRMOS claims with final files, evidence records, runtime status, integration posture, accepted state, archive state, and known limitations.

## Reconciliation Identity

- Session ID:
- Lifecycle boundary:
- Reconciliation type:
- Prepared at:
- Prepared by:

## Claim Summary

| Claim ID | Claim | Claim family | Current status | Supported? | Downgraded? | Notes |
|---|---|---|---|---:|---:|---|

Claim families:

```text
artifact
design
implementation
validation
runtime
integration
close
packaging
```

## Evidence Status Values

Use one of:

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

## Final-File Reconciliation

| Claim ID | Files/artifacts inspected | Expected evidence | Actual evidence | Contradiction? | Result |
|---|---|---|---|---:|---|

## Command / Log Reconciliation

| Claim ID | Command | Working directory | Claimed result | Logged result | Log/output location | Reproducible from current working copy? |
|---|---|---|---|---|---|---:|

## Runtime Verification Reconciliation

| Claim ID | Runtime behavior claimed | Verification level | Evidence | Limitation | Follow-up |
|---|---|---|---|---|

Verification/evidence states must use canonical values from `support/claim-reconciliation.md`:

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

Use notes/rationale fields for nuance such as build-only, route-only, code-inspected, or production-provider-specific limitations.

## Runtime Integration Claim Reconciliation

| Area | Claimed integration posture | Evidence status | Final-file support | Production-ready claim allowed? | Blocker / follow-up |
|---|---|---|---|---:|---|

## Close / Archive Claim Reconciliation

Use when close, archive, or Update System State claims are made.

| Close claim | Accepted state evidence | Archive evidence | Active session evidence | Consistent? | Result |
|---|---|---|---|---:|---|

## Downgraded Claims

List any claims that must be downgraded before surfacing output.

| Original claim | Downgraded truthful claim | Reason | Required next action |
|---|---|---|---|

## Blockers

| Blocker | Affected claim | Owner | Required action |
|---|---|---|---|

## Handoff

- Claim reconciliation result: `SATISFIED | BLOCKED | NOT_APPLICABLE`
- Boundary allowed to advance:
- Boundary blocked because:
- User-facing wording required:

## archive/session-state integrity Mandatory Instantiation Check

Complete this before any material completion/readiness/validation/runtime/integration/package/update-state/close claim is surfaced.

| Field | Value |
|---|---|
| Material claim being surfaced | |
| Claim family | artifact / design / implementation / validation / runtime / integration / close / packaging |
| Canonical claim status | NOT_CLAIMED / NOT_RUN / CLAIMED_NOT_LOGGED / LOGGED_COMMAND_PASSED / LOGGED_COMMAND_FAILED / LOCAL_RUNTIME_VERIFIED / USER_ENVIRONMENT_VERIFIED / PRODUCTION_READINESS_VERIFIED / BLOCKED / NOT_APPLICABLE |
| Noncanonical label encountered | none / value |
| Canonical translation and rationale | |
| Raw evidence path or summary | |
| Final-file reconciliation completed | yes / no / not_applicable |
| User-environment verification completed | yes / no / not_applicable |
| Downgrade/block required | yes / no |

Firm rule: if this table is missing for a material claim, the claim is not reconciled.

## Canonical Value Scan

Complete before readiness, completion, update-state, archive, or close claims.

| Artifact inspected | Field inspected | Noncanonical value found | Canonical replacement | Decision/rationale field updated? | Pass / Blocked |
|---|---|---|---|---:|---|
| | | none / value | NOT_CLAIMED / NOT_RUN / CLAIMED_NOT_LOGGED / LOGGED_COMMAND_PASSED / LOGGED_COMMAND_FAILED / LOCAL_RUNTIME_VERIFIED / USER_ENVIRONMENT_VERIFIED / PRODUCTION_READINESS_VERIFIED / BLOCKED / NOT_APPLICABLE | yes / no / not_applicable | |

Invalid evidence/status examples include `observed`, `observed (code)`, `build pass`, `ACCEPTED_AT_CLOSE`, `NOT_IMPLEMENTED`, `deferred`, `PARTIAL_PASS`, and similar shorthand. Translate them before advancing.

Accepted-state decision classifications belong in decision/update fields, not evidence status fields.

## Close Claim Materialization Record

Complete this section before normal close is surfaced.

| Close-time claim | Required artifact / evidence | Evidence status | Satisfied? | Downgrade / block decision |
|---|---|---|---:|---|
| Close/archive success | `support/close-checklist.md`, `support/archive-manifest.md`, active and archived `SESSION_STATE.json` | NOT_CLAIMED / NOT_RUN / CLAIMED_NOT_LOGGED / LOGGED_COMMAND_PASSED / LOGGED_COMMAND_FAILED / LOCAL_RUNTIME_VERIFIED / USER_ENVIRONMENT_VERIFIED / PRODUCTION_READINESS_VERIFIED / BLOCKED / NOT_APPLICABLE | yes / no | |
| Accepted-state merge success | `support/system-state-update.md`, `CURRENT_SYSTEM_STATE.md`, accepted-state support records | NOT_CLAIMED / NOT_RUN / CLAIMED_NOT_LOGGED / LOGGED_COMMAND_PASSED / LOGGED_COMMAND_FAILED / LOCAL_RUNTIME_VERIFIED / USER_ENVIRONMENT_VERIFIED / PRODUCTION_READINESS_VERIFIED / BLOCKED / NOT_APPLICABLE | yes / no | |
| Framework compliance | `python3 _hirmos/tools/validate.py` output when applicable | NOT_CLAIMED / NOT_RUN / CLAIMED_NOT_LOGGED / LOGGED_COMMAND_PASSED / LOGGED_COMMAND_FAILED / LOCAL_RUNTIME_VERIFIED / USER_ENVIRONMENT_VERIFIED / PRODUCTION_READINESS_VERIFIED / BLOCKED / NOT_APPLICABLE | yes / no | |
| Local runtime/setup readiness | `support/local-runtime-evidence.md` when applicable | NOT_CLAIMED / NOT_RUN / CLAIMED_NOT_LOGGED / LOGGED_COMMAND_PASSED / LOGGED_COMMAND_FAILED / LOCAL_RUNTIME_VERIFIED / USER_ENVIRONMENT_VERIFIED / PRODUCTION_READINESS_VERIFIED / BLOCKED / NOT_APPLICABLE | yes / no | |
| Role workflow readiness | `support/role-workflow-smoke.md` when applicable | NOT_CLAIMED / NOT_RUN / CLAIMED_NOT_LOGGED / LOGGED_COMMAND_PASSED / LOGGED_COMMAND_FAILED / LOCAL_RUNTIME_VERIFIED / USER_ENVIRONMENT_VERIFIED / PRODUCTION_READINESS_VERIFIED / BLOCKED / NOT_APPLICABLE | yes / no | |
| Package cleanliness | package report / archive manifest when package is produced | NOT_CLAIMED / NOT_RUN / CLAIMED_NOT_LOGGED / LOGGED_COMMAND_PASSED / LOGGED_COMMAND_FAILED / LOCAL_RUNTIME_VERIFIED / USER_ENVIRONMENT_VERIFIED / PRODUCTION_READINESS_VERIFIED / BLOCKED / NOT_APPLICABLE | yes / no | |

If this section is missing from an archived normal-close session, the close claim is `CLAIMED_NOT_LOGGED` and must not be treated as fully HIRMOS-compliant.

## Requirements Coverage Claims

When HIRMOS claims requirements coverage, record the owning artifact and evidence basis.

| Claim | Requirement IDs | Coverage status source | Evidence state | Notes |
|---|---|---|---|---|
| `<claim>` | `<REQ-IDs>` | `_hirmos/session/REQUIREMENTS_BASELINE.md` | `<canonical evidence state>` | `<notes>` |

Requirement coverage statuses are not evidence states. Evidence states must remain canonical claim/evidence states.

## Comparative / Cross-Run Claims

Use this section when the session ranks, selects, or salvages from multiple candidate implementations, prototypes, generated apps, OpenSpec outputs, or prior self-runs.

| Comparative claim | Candidate/source set | Evidence basis | Limitation | Canonical evidence state | Follow-up / carry-forward |
|---|---|---|---|---|---|
| | | static review / transcript / source inspection / command log / user observation / runtime verification | | NOT_CLAIMED / NOT_RUN / CLAIMED_NOT_LOGGED / LOGGED_COMMAND_PASSED / LOGGED_COMMAND_FAILED / LOCAL_RUNTIME_VERIFIED / USER_ENVIRONMENT_VERIFIED / BLOCKED / NOT_APPLICABLE | |

Firm rule: comparative ranking is not proof of runtime readiness unless runtime evidence exists.
