# Requirements and Coverage

HIRMOS requirements are scoped source authorities, not default root accepted-state artifacts.

Default HIRMOS does not create `_hirmos/system/accepted-state/REQUIREMENTS.md`. Requirements originate and remain authoritative at the delivery, phase, session, or archive level unless a future explicit cumulative accepted requirements governance mode is activated.

## Source locations

Requirements may live in:

- `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md`;
- optional `_hirmos/system/delivery/<delivery-id>/REQUIREMENTS.md` when delivery-level requirements need their own authority;
- `_hirmos/session/SESSION_SCOPE.md`;
- optional `_hirmos/session/REQUIREMENTS.md` when session-level requirements need their own authority;
- archived delivery/session artifacts after close.

`CURRENT_SYSTEM_STATE.md` answers where requirement sources are and what accepted work changed. It does not replace those sources as a complete requirements catalog.

## Accepted-state navigation

`_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md` must keep requirements discoverable through its Work History Ledger and Source Artifact Index. It may include concise accepted-state summaries, but those summaries are navigation summaries only.

## Coverage

Coverage should be verified against the active authority level:

- delivery baseline coverage against `DELIVERY_SCOPE.md` and optional delivery `REQUIREMENTS.md`;
- phase/session coverage against `PHASE-xx.md`, `SESSION_SCOPE.md`, and optional session `REQUIREMENTS.md`;
- close-time accepted coverage against source artifacts, evidence, archive manifest, and `CURRENT_SYSTEM_STATE.md` ledger/index updates.

## On-demand synthesis

A complete current requirements artifact may be generated on demand from `CURRENT_SYSTEM_STATE.md`, delivery/session/archive source artifacts, and close records. That generated artifact is a synthesis, not source authority, unless explicitly adopted under a governed future workflow.
