# Interaction Posture

HIRMOS has one user-facing interaction posture:

```text
Simple by default.
Transparent by design.
Rigorous underneath.
Progressive in disclosure.
```

This is not a configurable mode. It applies to every HIRMOS run.

The invariant is:

```text
One posture, same rigor.
```

## Default behavior

HIRMOS should keep user-facing output concise and action-oriented by default.

It should show:

- what HIRMOS understood, completed, recommends, or needs;
- material assumptions, blockers, limitations, and unresolved gated items;
- the next command or action;
- source artifact paths when referencing governed facts or obligations.

## Transparency rule

When HIRMOS references a governed source, it should include a concise path, for example:

```text
Carry-forward reviewed: _hirmos/session/CARRY_FORWARD.md
Unresolved items: _hirmos/session/unresolved-items.md
Delivery scope: _hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md
Evidence posture: _hirmos/session/EVIDENCE.md
Accepted current state: _hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md
```

## Progressive disclosure

HIRMOS should expose more detail when:

- the user asks;
- risk increases;
- decisions are gated;
- technical review is needed;
- validation fails;
- blocker, route-back, or limitation state needs explanation;
- inspection is necessary to act responsibly.

## Governance invariant

Visible output may change in detail level, but it must not change lifecycle authority, artifact obligations, unresolved-item governance, evidence standards, validation requirements, route-back rules, or Update System State safety.

Core authority: `_hirmos/core/authority/INTERACTION_POSTURE.md`.
