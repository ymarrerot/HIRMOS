# Bootstrap Report

Status: bootstrap report template.
Purpose: prove the current agent/context completed compact HIRMOS bootstrap before governed command execution.

## Runtime Bootstrap Summary
| Field | Value / pointer |
|---|---|
| Status | PENDING / PASSED / FAILED |
| Agent/context identifier | |
| Completed at | |
| Working-copy root | |
| Canonical Interaction Posture source | `_hirmos/core/authority/INTERACTION_POSTURE.md` |
| Posture | simple by default; transparent by design; rigorous underneath; progressive in disclosure |

## General Run Preflight
Record only the command-surface result.
| Field | Value |
|---|---|
| Preflight result | PRECHECK_PASS / PRECHECK_WARNING / PRECHECK_BLOCKER |
| Requested command | hirmos start / hirmos continue / hirmos status / hirmos close / bootstrap-only / other |
| Core surface checked | YES / NO |
| Command spec checked | YES / NO / NOT_APPLICABLE |
| Integration surface checked | YES / NO / NOT_APPLICABLE |
| Missing or contradictory surface | |
| Fallback authority used | `_hirmos/AGENTS.md` / core bootstrap / none |
| Recovery action for warning/blocker | |

Preflight blockers stop command execution before lifecycle work. Preflight warnings may continue only when fallback authority is sufficient and surfaced. Allowed values marker: PRECHECK_PASS | PRECHECK_WARNING | PRECHECK_BLOCKER.

## Files Read
List only mandatory bootstrap/runtime files read in full.
| File | Read in full? | Notes |
|---|---|---|

## Bootstrap Discipline Answer Sources
Every session must answer the complete bootstrap quiz again. Do not answer from memory. Do not recover the answers from prior sessions. Do not satisfy bootstrap by citing a prior bootstrap report.

Allowed answer basis labels: `ANSWERED_FROM_CURRENT_ARTIFACTS`, `ANSWERED_FROM_ARCHIVED_PROJECT_HISTORY`, `ANSWERED_FROM_CORE_PROTOCOLS`, `ANSWERED_FROM_CURRENT_AND_ARCHIVED_SOURCES`, `ANSWERED_FROM_CURRENT_AND_CORE_SOURCES`.
Forbidden basis: chat memory, compressed chat summary, prior model memory, unstated recollection, same as previous session, see prior session, recovered/revalidated archived-bootstrap shortcuts, or any prior bootstrap answer used as a substitute for a fresh answer.

## Bootstrap Discipline Answers
Answer every quiz question from `_hirmos/core/bootstrap.md#Step 12 — Bootstrap quiz`. Keep each answer compact. Every row must include `Answer:`, `Source:`, and `Answer basis:`.

| Question | Answer | Source | Answer basis |
|---|---|---|---|
| Q1. <question summary> | Answer: | Source: | Answer basis: |
| Q2. <question summary> | Answer: | Source: | Answer basis: |
| Q3. <question summary> | Answer: | Source: | Answer basis: |
| Q4. <question summary> | Answer: | Source: | Answer basis: |
| Q5. <question summary> | Answer: | Source: | Answer basis: |
| Q6. <question summary> | Answer: | Source: | Answer basis: |
| Q7. <question summary> | Answer: | Source: | Answer basis: |
| Q8. <question summary> | Answer: | Source: | Answer basis: |
| Q9. <question summary> | Answer: | Source: | Answer basis: |
| Q10. <question summary> | Answer: | Source: | Answer basis: |
| Q11. <question summary> | Answer: | Source: | Answer basis: |
| Q12. <question summary> | Answer: | Source: | Answer basis: |
| Q13. <question summary> | Answer: | Source: | Answer basis: |
| Q14. <question summary> | Answer: | Source: | Answer basis: |
| Q15. <question summary> | Answer: | Source: | Answer basis: |
| Q16. <question summary> | Answer: | Source: | Answer basis: |

If current artifacts or archived project history do not support an answer, reread the corresponding core authority/protocol file and answer from that file.

## Uncertainty / Missing Files
Record missing, contradictory, or unclear bootstrap evidence only.

## Runtime Context
| Field | Value |
|---|---|
| Session-state runtime context path | `_hirmos/session/SESSION_STATE.json#run_context` |
| Runtime timestamp source captured? | YES / NO |
| Runtime timestamp source type | cli / shell-date / user-provided / other |
| Date command/evidence when not CLI-provided | |

## Allowed Next Action
State the next allowed action after bootstrap. Bootstrap completion does not authorize runtime command execution unless the user requested that command.
