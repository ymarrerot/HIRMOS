# Bootstrap Report

Status: bootstrap report template.
Purpose: prove that the current agent/context completed HIRMOS bootstrap before any governed command execution.

## Canonical Interaction Posture

- Source: `_hirmos/core/authority/INTERACTION_POSTURE.md`
- Posture: simple by default, transparent by design, rigorous underneath, progressive in disclosure.
- Context-resilience rule: posture and bootstrap discipline must be answered again from durable current artifacts, archived project-history artifacts, or core authority/protocol files, not from chat memory, compressed chat summaries, assumed prior context, or prior bootstrap answers.

## Bootstrap Status

- Status: PENDING | PASSED | FAILED
- Agent/context identifier:
- Completed at:
- Working-copy root:


## General Run Preflight

Record the minimum runtime-surface check before command execution. This applies to every project/run; do not label it as special run-category.

- Preflight result: PRECHECK_PASS | PRECHECK_WARNING | PRECHECK_BLOCKER
- Requested command: hirmos start | hirmos continue | hirmos status | hirmos close | bootstrap-only | other
- Core surface checked: YES | NO
- Command spec checked: YES | NO | NOT_APPLICABLE
- Integration surface checked: YES | NO | NOT_APPLICABLE
- Missing/contradictory surface, if any:
- Fallback authority used, if any: `_hirmos/AGENTS.md` / core bootstrap / none
- Recovery action when warning/blocker:

Preflight warnings may be surfaced with a clear limitation when fallback authority is sufficient. Preflight blockers stop command execution before lifecycle work.

## Files Read

List every mandatory bootstrap file read in full.

| File | Read in full? | Notes |
|---|---|---|

## Bootstrap Discipline Answer Sources

Every session must answer the complete bootstrap quiz again. Do not answer from memory. Do not recover the answers from prior sessions. Do not satisfy bootstrap by citing a prior bootstrap report.

Allowed answer basis labels:

- `ANSWERED_FROM_CURRENT_ARTIFACTS` — answer was written for this session using active durable artifacts in the current working copy.
- `ANSWERED_FROM_ARCHIVED_PROJECT_HISTORY` — answer was written for this session using archived project history artifacts such as prior `SESSION_SCOPE.md`, `SESSION_EXECUTION.md`, `EVIDENCE.md`, delivery/phase files, or close records. Do not use archived bootstrap answers as shortcuts.
- `ANSWERED_FROM_CORE_PROTOCOLS` — answer was written for this session by reading the named core authority/protocol file.
- `ANSWERED_FROM_CURRENT_AND_ARCHIVED_SOURCES` — answer was written for this session using both current artifacts and archived project history.
- `ANSWERED_FROM_CURRENT_AND_CORE_SOURCES` — answer was written for this session using both current artifacts and core authority/protocol files.

Forbidden basis: chat memory, compressed chat summary, prior model memory, unstated recollection, the retired archived-bootstrap recovery-chain label, `same as previous session`, `see prior session`, or any prior bootstrap answer used as a substitute for a fresh answer.

## Bootstrap Discipline Answers

Answer every quiz question from `_hirmos/core/bootstrap.md#Step 12 — Bootstrap quiz`. Every answer is required in every bootstrap report. Keep answers compact but complete enough to prove comprehension and command readiness.

Each answer must use this format:

```text
Q<number>. <question summary>
Answer: <compact complete answer written for this session>
Source: <current artifact, archived project-history artifact, or core authority/protocol file>
Answer basis: ANSWERED_FROM_CURRENT_ARTIFACTS | ANSWERED_FROM_ARCHIVED_PROJECT_HISTORY | ANSWERED_FROM_CORE_PROTOCOLS | ANSWERED_FROM_CURRENT_AND_ARCHIVED_SOURCES | ANSWERED_FROM_CURRENT_AND_CORE_SOURCES
```

If current artifacts or archived project history do not support the answer, reread the corresponding core authority/protocol file and answer from that file.

## Uncertainty / Missing Files

Record any missing, contradictory, or unclear bootstrap evidence.

## Runtime Context

- Session-state runtime context path: `_hirmos/session/SESSION_STATE.json#run_context`
- Runtime timestamp source captured? YES | NO
- Runtime timestamp source type: cli | shell-date | user-provided | other
- Date command/evidence when not CLI-provided:

## Allowed Next Action

State the next allowed action after bootstrap.

Bootstrap completion does not itself authorize a runtime command unless the user requested one.