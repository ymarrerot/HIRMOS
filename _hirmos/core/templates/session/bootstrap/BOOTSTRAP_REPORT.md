# Bootstrap Report

Status: bootstrap report template.
Purpose: prove that the current agent/context completed HIRMOS bootstrap before any governed command execution.

## Canonical Interaction Posture

- Source: `_hirmos/core/authority/INTERACTION_POSTURE.md`
- Posture: simple by default, transparent by design, rigorous underneath, progressive in disclosure.
- Context-resilience rule: posture and bootstrap discipline must be recovered from durable artifacts or core authority/protocol files, not from chat memory, compressed chat summaries, or assumed prior context.

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

## Bootstrap Discipline Answer Recovery

For each bootstrap quiz answer, record how the answer was recovered. Allowed recovery methods:

- `NEWLY_ANSWERED_FROM_CORE` — answer was created by reading the named core authority/protocol file during this bootstrap.
- `REVALIDATED_FROM_ACTIVE_ARTIFACT` — answer was revalidated from an active durable artifact that exists in the current working copy.
- `REVALIDATED_FROM_ARCHIVED_BOOTSTRAP` — answer was revalidated from an archived bootstrap report under `_hirmos/system/history/sessions/**/bootstrap/BOOTSTRAP_REPORT.md` or equivalent archived session bootstrap path.
- `REANSWERED_FROM_CORE_BECAUSE_PRIOR_BOOTSTRAP_NOT_FOUND` — no reliable active or archived bootstrap answer was found, so the answer was regenerated from the named core authority/protocol file.

Forbidden recovery method: chat memory, compressed chat summary, prior model memory, or unstated recollection.

## Bootstrap Discipline Answers

Answer every quiz question from `_hirmos/core/bootstrap.md#Step 12 — Bootstrap quiz`. Every answer is required in every bootstrap report. Keep answers compact but complete enough to prove comprehension and command readiness.

Each answer must use this format:

```text
Q<number>. <question summary>
Answer: <compact complete answer>
Source: <active artifact, archived bootstrap path, or core authority/protocol file>
Recovery method: NEWLY_ANSWERED_FROM_CORE | REVALIDATED_FROM_ACTIVE_ARTIFACT | REVALIDATED_FROM_ARCHIVED_BOOTSTRAP | REANSWERED_FROM_CORE_BECAUSE_PRIOR_BOOTSTRAP_NOT_FOUND
```

If an archived bootstrap report is used, cite its archive path. If no durable prior bootstrap answer is found or there is uncertainty, reread the corresponding core authority/protocol file and answer again from that file.

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