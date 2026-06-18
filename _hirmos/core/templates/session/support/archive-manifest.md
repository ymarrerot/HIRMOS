# Archive Manifest

Status: archived-session manifest.
Lifecycle owner: Update System State.
Purpose: prove what was archived, what was accepted, what was not applied, and how the active session was reset.

## Archive Identity

- Session ID:
- Close type: NORMAL_CLOSE | ABORT_CLOSE | BLOCKED_CLOSE
- Source active-session path: `_hirmos/session/`
- Archive path: `_hirmos/system/history/sessions/<session-id>/`
- Close command timestamp:

## Archived Files

| File | Included | Reason / exception |
|---|---|---|

## Accepted Outcomes Applied

| Outcome | Accepted-state target | Source artifact | Evidence |
|---|---|---|---|

## Rejected / Not Applied Outcomes

| Outcome | Reason | Future handling |
|---|---|---|

## Evidence-Only Artifacts

| Artifact | Why evidence-only |
|---|---|

## Carry-Forward Items

| Item | Destination | Future-session instruction |
|---|---|---|

## Active-Session Reset Result

- Reset completed: yes / no
- Remaining active-session files:
- Exceptions:

## Post-Close Verification

| Check | Status | Evidence |
|---|---|---|

## Archive Decision

- ARCHIVE_COMPLETE | ARCHIVE_BLOCKED | ABORT_ARCHIVED
- Rationale:

## archive/session-state integrity State Integrity Record

| Field | Value |
|---|---|
| pre_close_session_state_recorded | yes / no / not_applicable |
| pre_close_session_state_location | |
| archived_session_state_status | closed / archived / history_only / missing / conflict |
| active_session_state_after_close | idle / conflict / not_checked |
| accepted_state_update_status | applied / not_applied / blocked |
| post_close_status_result | consistent / conflict / not_checked |
| claim_reconciliation_location | |

Firm rule: the archived `SESSION_STATE.json` must not represent the session as active after normal close. Preserve active/pre-close evidence separately when needed.

## durable current-system-state Accepted-State Merge Record

| Accepted-state artifact | Updated / verified unchanged | Source session artifact | Notes |
|---|---|---|---|
| `CURRENT_SYSTEM_STATE.md` | | | |
| `CARRY_FORWARD.md` | | | |
| `DECISION_LOG.md` | | | |

- Current system state version after close:
- Sections changed:
- Accepted outcomes merged:
- Outcomes rejected / not applied:
- Carry-forward items added / resolved:
- Decisions accepted / rejected / superseded:
- Production readiness tracks updated separately: yes / no

## Accepted-State and Package Integrity Record

| Check | Result | Evidence / location |
|---|---|---|
| Accepted-state invariant blocks preserved after merge | yes / no / not_applicable | |
| Noncanonical evidence values translated | yes / no / not_applicable | |
| Noncanonical runtime posture values translated | yes / no / not_applicable | |
| Role workflow smoke artifact archived when applicable | yes / no / not_applicable | |
| Clean package exclusions checked when package produced | yes / no / not_applicable | |
| Local secrets/noisy generated files excluded or explicitly labeled | yes / no / not_applicable | |

## Close-Time Compliance and Evidence Materialization Record

| Required close-time item | Materialized / checked | Location / evidence | Result |
|---|---|---|---|
| `support/claim-reconciliation.md` for close claim | yes / no / not_applicable | | SATISFIED / BLOCKED / NOT_APPLICABLE |
| `support/session-implementation-review.md` when Implementation active | yes / no / not_applicable | | SATISFIED / BLOCKED / NOT_APPLICABLE |
| `support/evidence-review.md` when evidence claimed | yes / no / not_applicable | | SATISFIED / BLOCKED / NOT_APPLICABLE |
| `support/local-runtime-evidence.md` when local runtime/setup claimed | yes / no / not_applicable | | SATISFIED / BLOCKED / NOT_APPLICABLE |
| `support/role-workflow-smoke.md` when role workflows in scope | yes / no / not_applicable | | SATISFIED / BLOCKED / NOT_APPLICABLE |
| `support/runtime-integration-readiness.md` when integration posture claimed | yes / no / not_applicable | | SATISFIED / BLOCKED / NOT_APPLICABLE |
| Framework validator result recorded | yes / no / not_applicable | | SATISFIED / BLOCKED / NOT_APPLICABLE |
| Canonical structured-value scan completed | yes / no / not_applicable | | SATISFIED / BLOCKED / NOT_APPLICABLE |
| Accepted-state invariants preserved | yes / no / not_applicable | | SATISFIED / BLOCKED / NOT_APPLICABLE |
| Package cleanliness checked when package produced | yes / no / not_applicable | | SATISFIED / BLOCKED / NOT_APPLICABLE |

A normal archive cannot be `ARCHIVE_COMPLETE` unless every required close-time compliance item is `SATISFIED` or `NOT_APPLICABLE` with rationale.


## Archive / Reset Verification

| Field | Value | Evidence |
|---|---|---|
| session_contract_archived | yes / no | |
| session_contract_review_archived | yes / no | |
| unresolved_items_archived | yes / no | |
| session_execution_archived | yes / no | |
| implementation_units_archived | yes / no / not_applicable | |
| support_artifacts_archived | yes / no / not_applicable | |
| pre_close_session_state_recorded | yes / no / not_applicable | |
| archived_session_state_status | closed / archived / history_only / missing / conflict | |
| active_session_state_after_close | idle / conflict / not_checked | |
| active_session_reset_scaffolding_only | yes / no / not_checked | |
| stale_active_artifacts_remaining | none / listed / not_checked | |
| accepted_state_update_status | applied / not_applied / blocked | |
| post_close_status_result | consistent / conflict / not_checked | |

Any value indicating `missing`, `conflict`, `listed`, `not_checked`, or `blocked` blocks normal close success.
