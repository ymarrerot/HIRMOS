# Run Execution Controls

- Resolved command:
- Run scope:
- Completion rule: All listed run execution controls must be EXECUTED before trustworthy completion may be surfaced.
- Command-boundary note: This ledger is created only for supported Core commands that successfully passed command identification.
- Truth rule: `EXECUTED` means the governed requirement was truthfully satisfied.
- Verification rule: If truth cannot be verified, keep the control `PENDING`.
- Anti-paperwork rule: Do not mark a control `EXECUTED` merely because a plausible artifact was produced.
- Working-copy continuity note: This run's artifact and readiness claims must be verified against the active cumulative working copy.
- Continuity fail-closed rule: If continuity becomes unclear or verification is missing, the affected control must remain `PENDING` or the run must fail closed.
- Continuity completion rule: Do not mark a control `EXECUTED` if completion depends on file or artifact state that was not verified against the active cumulative working copy.
- Maintenance note: This artifact is initialized and maintained by Core during command execution.
- Rerun refresh rule: On a governed rerun, refresh this artifact for the current run state instead of carrying forward stale prior-state notes.
- State-note rule: Any control notes that mention paused, completed, blocked, or similar run-state-specific conditions must describe the current run truth, not the prior run.

## Identity display execution control
- Governing file: _hirmos/core/authority/core/identity-display-execution-control.md
- Status: PENDING
- Notes: <refresh so this note matches the current run state; do not carry forward stale paused/completed wording from a prior run>

## Extension execution control
- Governing file: <resolved extension entrypoint authority>
- Status: PENDING
- Notes: <refresh so this note matches the current run state; do not carry forward stale paused/completed wording from a prior run>
