# Close, Archive, and Accepted State

HIRMOS treats close as a governed state transaction, not as the end of a chat.

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

Accepted state records what future sessions may treat as current truth.

A file in the archive is not automatically accepted truth. `support/system-state-update.md` decides what was accepted, rejected, preserved as evidence only, or carried forward.

## After close

After normal close, `hirmos status` should show no active governed session. It should point to the latest archive and current-state latest-close metadata.


## contract-centered close/reset model

New governed sessions close through the contract-centered artifact model. Close verification starts from:

- `_hirmos/session/SESSION_CONTRACT.md`;
- `_hirmos/session/session-contract-review.md`;
- `_hirmos/session/unresolved-items.md`;
- `_hirmos/session/SESSION_EXECUTION.md`;
- `_hirmos/session/implementation-units/` when Implementation was active;
- `_hirmos/session/support/` only for applicable evidence appendices.

`support/system-state-update.md` and `support/close-checklist.md` are not independent active-session authorities under the contract-centered model. When generated, they are derived close surfaces. The source-of-truth close verdict remains the Session Contract Review plus accepted-state merge evidence.

A normal close must archive all active session artifacts, normalize the archived session state, update accepted state, and reset `_hirmos/session/` to idle scaffolding only. If stale active artifacts remain after reset, the correct result is `Close Blocked`, not close success.
