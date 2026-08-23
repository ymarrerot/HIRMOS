> Accepted-State Artifact Invariants:
> - This file is part of durable accepted state.
> - Preserve this invariant block during Update System State.
> - Do not replace this file with a chat summary or session-local artifact.
> - Use canonical runtime posture values from `RUNTIME_INTEGRATION_AND_PRODUCTION_READINESS.md`.
> - Use canonical evidence states from `EVIDENCE.md` claim reconciliation.
> - Keep accepted-state decision classifications separate from evidence status.


# Carry-Forward Items

Status: durable accepted-state support record.
Purpose: preserve active unresolved items, assumptions, risks, production-readiness blockers, future-session instructions, and resolved carry-forward provenance that remain part of accepted-state governance.

`CARRY_FORWARD.md` is the single accepted-state authority for carry-forward lifecycle. It owns active carry-forward items and their resolved carry-forward provenance. `CURRENT_SYSTEM_STATE.md` may summarize this posture, but it must not be treated as the carry-forward authority. Historical session archives remain close-time snapshots and must not be rewritten to show later resolution.

## Carry-Forward ID Rule

Every accepted-state carry-forward item must have a globally unique project-local ID using this format:

```text
CF-YYYYMMDD-NNN
```

Each item must also preserve its source pointer separately:

- `source_session`: the session or archive where the carry-forward was created;
- `source_local_id`: the local close-time carry-forward ID, when present;
- `source_ref`: `<source_session>:<source_local_id>` or a source archive path when no local ID exists.

Bare local IDs such as `CF-01` are not valid accepted-state carry-forward IDs because multiple sessions can reuse them. They may appear only as `source_local_id` / `source_ref` values.

## Active Carry-Forward Register

Only items with close-time disposition `APPROVED_CARRY_FORWARD` may appear here. Carry-forward candidates that were auto-resolved, user-resolved, blocked, or no longer applicable belong in the closing session archive, not this active register.

| CF ID | Type | Owner | Future-session instruction | Evidence needed | Source session | Source local ID | Source ref | Approval / deferral source | Status |
|---|---|---|---|---|---|---|---|---|---|
| none | none | none | none | none | none | none | none | none | none |

## Resolved Carry-Forward Register

Resolved carry-forward remains in this file as provenance. A carry-forward item may not disappear from the Active Carry-Forward Register unless the same `CF ID` appears here with a resolution basis and evidence posture.

| CF ID | Source ref | Resolution basis | Evidence posture | Resolved at | Resolved by / authority | Current-state update pointer | Notes |
|---|---|---|---|---|---|---|---|
| none | none | none | none | none | none | none | none |

## Carry-Forward Lifecycle Rule

This file contains active and resolved carry-forward lifecycle records. The active register contains unresolved carry-forward only. The resolved register preserves post-close resolution provenance.

When an item is resolved through a governed accepted-state maintenance session, move it from the Active Carry-Forward Register to the Resolved Carry-Forward Register in the same transaction, update `CURRENT_SYSTEM_STATE.md` summary pointers, and archive the maintenance session through normal `hirmos close`. Do not rewrite historical session archives to make close-time carry-forward appear resolved retroactively.

## Removal / Resolution Concordance Rule

A carry-forward item may not be removed from Active unless a matching Resolved row exists for the same global `CF ID`. A claim of `USER_ENVIRONMENT_VERIFIED`, `PRODUCTION_READINESS_VERIFIED`, or equivalent post-close resolution for a carry-forward item is invalid unless the matching Resolved row names the evidence posture and resolution basis.

## Accepted-State Maintenance Flow

Carry-forward resolution must use the existing HIRMOS command surface, not a separate command. Use a narrow accepted-state maintenance session:

```text
hirmos start "Record verification that CF-YYYYMMDD-NNN is resolved"
hirmos continue
hirmos close
```

The session may update `_hirmos/system/accepted-state/CARRY_FORWARD.md`, `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md`, and session governance/evidence artifacts only. Product/source edits, historical archive mutation, and delivery/phase scope edits are forbidden unless separately scoped and authorized.

## PROD-L8.21 Carry-Forward Template Concordance

`CARRY_FORWARD.md` must preserve the carry-forward lifecycle invariants while keeping unresolved items in Active and post-close resolution provenance in Resolved. If no active carry-forward exists, state that explicitly instead of leaving placeholders. New active items must point to the close-time carry-forward candidate review row that approved deferral.

## PROD-L8.31 Carry-Forward Approval Source Gate

Every item recorded here as active carry-forward must have disposition `APPROVED_CARRY_FORWARD` and an explicit approval/deferral source.

Accepted approval/deferral sources:

- direct user response approving deferral;
- accepted partial-close decision that names the item;
- accepted baseline clause that explicitly authorizes deferral.

If approval/deferral source is missing, the item is not valid carry-forward and must remain a close-time candidate or blocker.

## PROD-L8.33G Carry-Forward Lifecycle Consolidation

No new carry-forward resolution command or separate resolution artifact is required. `CARRY_FORWARD.md` is the single accepted-state authority for active and resolved carry-forward lifecycle. `hirmos status` detects carry-forward concordance conflicts without repairing them. `hirmos start` / `hirmos continue` / `hirmos close` govern accepted-state maintenance sessions that resolve carry-forward items.
