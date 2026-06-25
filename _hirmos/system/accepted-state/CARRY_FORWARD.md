> Accepted-State Artifact Invariants:
> - This file is part of durable accepted state.
> - Preserve this invariant block during Update System State.
> - Do not replace this file with a chat summary or session-local artifact.
> - Use canonical runtime posture values from `RUNTIME_INTEGRATION_AND_PRODUCTION_READINESS.md`.
> - Use canonical evidence states from `EVIDENCE.md` claim reconciliation.
> - Keep accepted-state decision classifications separate from evidence status.


# Carry-Forward Items

Status: durable accepted-state support record.
Purpose: preserve active unresolved items, assumptions, risks, production-readiness blockers, and future-session instructions that remain after close. Closed carry-forward history belongs in session archives and `CURRENT_SYSTEM_STATE.md` history, not in this active register.

## Active Carry-Forward Items

| ID | Type | Owner | Future-session instruction | Source archive |
|---|---|---|---|---|


## Active-Only Rule

This file contains active carry-forward items only. When an item is resolved, remove it from this active table and record the resolution in the closing session archive and `CURRENT_SYSTEM_STATE.md` History / Traceability / Merge Notes. Do not maintain a closed carry-forward table here.

## PROD-L8.21 Carry-Forward Template Concordance

`CARRY_FORWARD.md` must preserve the exact `Active-Only Rule` invariant while keeping closed/resolved/deferred items out of the active register. If no active carry-forward exists, state that explicitly instead of leaving placeholders.
