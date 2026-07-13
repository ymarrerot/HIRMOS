# Close, Archive, and Accepted State

HIRMOS treats close as a governed state transaction, not as the end of a chat. Close is where a run proves what future sessions may trust.

A successful close must prove four things:

1. reviewed session outcomes are classified correctly;
2. accepted outcomes were written to accepted state;
3. the full active session was archived;
4. the active session area was reset without losing unarchived evidence.

## What close means

`hirmos close` runs **Update System State**.

It does not design missing work, implement missing work, repair evidence, or silently accept incomplete results.

## Accepted state vs archive

The archive preserves what happened.

Accepted state records what future sessions may treat as current truth. That makes accepted-state update a governance act, not a summary-writing task.

A file in the archive is not automatically accepted truth. `SESSION_LEDGER.md` close/update control pointers decides what was accepted, rejected, preserved as evidence only, or carried forward.

## After close

After normal close, `hirmos status` should show no active governed session. It should point to the latest archive and current-state latest-close metadata.


## contract-centered close/reset model

New governed sessions close through the contract-centered artifact model. Close verification starts from:

- `_hirmos/session/SESSION_SCOPE.md`;
- `_hirmos/session/SESSION_SCOPE.md` close verification;
- `_hirmos/session/unresolved-items.md`;
- `_hirmos/session/SESSION_LEDGER.md`;
- `_hirmos/session/implementation-units/` when Implementation was active;
- `_hirmos/session/EVIDENCE.md` when evidence is nontrivial or cannot be captured clearly in implementation-unit artifacts.

Do not create separate close checklist, claim reconciliation, local-runtime evidence, runtime-readiness, archive-manifest, or session-scope-review support files for new sessions. Their responsibilities belong in `SESSION_SCOPE.md`, `SESSION_LEDGER.md`, `EVIDENCE.md`, implementation units, and accepted-state records. The source-of-truth close verdict remains `SESSION_SCOPE.md` close verification plus accepted-state merge evidence.

A normal close must archive all active session artifacts, normalize the archived session state, update accepted state, and reset `_hirmos/session/` to idle scaffolding only. If stale active artifacts remain after reset, the correct result is `Close Blocked`, not close success.


## PROD-L6 archive concordance

Normal close writes `_hirmos/system/history/sessions/<session-id>/ARCHIVE_MANIFEST.md` as a history-only archive manifest. The manifest records archived artifacts, accepted-state application, delivery pointer refresh, archived `SESSION_STATE.json` normalization, active-session reset, and post-close concordance. It supports accepted-state concordance but does not replace `CURRENT_SYSTEM_STATE.md`, `CARRY_FORWARD.md`, or conditional `DECISION_LOG.md` when active.

Accepted-state concordance requires `CURRENT_SYSTEM_STATE.md` latest-close metadata, the archive manifest, active carry-forward records, durable decisions, and post-close idle session state to agree.
