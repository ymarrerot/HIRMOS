# ARCHIVE_MANIFEST.md

Status: history-only archive manifest.
Purpose: record the normal-close archive transaction and concordance between archived session truth, accepted-state updates, active-session reset, and post-close status.

This file is created inside `_hirmos/system/history/sessions/<session-id>/` during normal close. It is not an active-session authority artifact and must not replace `CURRENT_SYSTEM_STATE.md`, `SESSION_EXECUTION.md` close controls, `SESSION_SCOPE.md` close verification, or accepted-state records.

## 1. Archive Identity

| Field | Value |
|---|---|
| Session ID | |
| Close type | normal / partial / blocked / abort-history-only |
| Source active-session path | `_hirmos/session/` |
| Archive path | `_hirmos/system/history/sessions/<session-id>/` |
| Archive date | |
| Archived by command | `hirmos close` |

## 2. Pre-Close State Preservation

| Field | Value |
|---|---|
| Pre-close SESSION_STATE preserved | YES / NO |
| Pre-close state location | `PRE_CLOSE_SESSION_STATE.json` / `SESSION_EXECUTION.md` archive controls / other |
| Pre-close lifecycle stage | |
| Pre-close recommended command | |

## 3. Archived Artifact Inventory

| Artifact | Archived? | Notes |
|---|---:|---|
| SESSION_STATE.json | YES / NO | |
| SESSION_SCOPE.md | YES / NO / NOT_APPLICABLE | |
| SESSION_EXECUTION.md | YES / NO | |
| unresolved-items.md | YES / NO / NOT_APPLICABLE | |
| implementation-units/ | YES / NO / NOT_APPLICABLE | |
| EVIDENCE.md | YES / NO / NOT_APPLICABLE | |
| stack-resolution.json | YES / NO / NOT_APPLICABLE | |
| bootstrap/ | YES / NO / NOT_APPLICABLE | |

## 4. Accepted-State Application

| Outcome class | Applied to accepted state? | Accepted-state target | Notes |
|---|---:|---|---|
| Accepted outcomes | YES / NO / NOT_APPLICABLE | CURRENT_SYSTEM_STATE.md | |
| Durable decisions | YES / NO / NOT_APPLICABLE | conditional DECISION_LOG.md when active | |
| Active carry-forward items | YES / NO / NOT_APPLICABLE | CARRY_FORWARD.md | |
| Delivery pointer updates | YES / NO / NOT_APPLICABLE | CURRENT_SYSTEM_STATE.md Delivery State | |
| Rejected / not-applied outcomes | YES / NO / NOT_APPLICABLE | CURRENT_SYSTEM_STATE.md / conditional DECISION_LOG.md when active | |

## 5. Delivery / Phase Status Transaction

Use when delivery governance was active.

| Field | Value |
|---|---|
| Delivery roadmap | none / `_hirmos/system/delivery/DELIVERY_PLAN.md` |
| Delivery scope | none / `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md` |
| Adopted phase | none / `_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md` |
| Delivery status updated | YES / NO / NOT_APPLICABLE |
| Phase status updated | YES / NO / NOT_APPLICABLE |
| Current System State pointers refreshed | YES / NO / explicitly verified unchanged / NOT_APPLICABLE |

## 6. Archived Session State Normalization

| Check | Result | Notes |
|---|---|---|
| Archived SESSION_STATE.json is terminal, not active | PASS / BLOCKED |
| Archived lifecycle_stage is closed / archived / history_only | PASS / BLOCKED |
| Archived state does not recommend `hirmos close` as next active command | PASS / BLOCKED |
| Pre-close active truth is preserved separately | PASS / BLOCKED |

## 7. Active-Session Reset Verification

| Check | Result | Notes |
|---|---|---|
| Active SESSION_STATE.json reset to idle | PASS / BLOCKED |
| Active session contains only idle scaffolding | PASS / BLOCKED |
| No stale SESSION_SCOPE.md remains active | PASS / BLOCKED |
| No stale SESSION_EXECUTION.md remains active | PASS / BLOCKED |
| No stale unresolved-items.md remains active | PASS / BLOCKED |

## 8. Post-Close Concordance

| Surface | Concordance result | Notes |
|---|---|---|
| SESSION_SCOPE.md close verification | PASS / PARTIAL / BLOCKED / NOT_APPLICABLE | |
| SESSION_EXECUTION.md close controls | PASS / PARTIAL / BLOCKED | |
| CURRENT_SYSTEM_STATE.md latest close metadata | PASS / PARTIAL / BLOCKED | |
| CARRY_FORWARD.md active items | PASS / PARTIAL / BLOCKED / NOT_APPLICABLE | |
| Conditional DECISION_LOG.md durable decisions | PASS / PARTIAL / BLOCKED / NOT_APPLICABLE | |
| Archive manifest | PASS / PARTIAL / BLOCKED | |
| Active-session reset | PASS / PARTIAL / BLOCKED | |

## 9. Final Archive Verdict

| Field | Value |
|---|---|
| Archive manifest verdict | ACCEPTED / PARTIAL / BLOCKED / ABORT_HISTORY_ONLY |
| Close output may claim normal close success | YES / NO |
| Latest archive pointer eligible for CURRENT_SYSTEM_STATE.md | YES / NO |
| Limitations / notes | |
