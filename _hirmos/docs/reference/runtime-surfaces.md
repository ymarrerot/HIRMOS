# Runtime Surfaces Reference


## PROD-L scope-authority naming note

`SESSION_SCOPE.md` is the canonical target name for active session authority. `SESSION_SCOPE.md` remains legacy-compatible during the PROD-L migration. `DELIVERY_SCOPE.md` is the canonical target name for one durable delivery/release authority; `DELIVERY_PLAN.md` is the project delivery roadmap/register.

The most important runtime surfaces are:

1. `_hirmos/session/SESSION_STATE.json` — minimal machine command/lifecycle state only.
2. `_hirmos/session/SESSION_SCOPE.md` — active session scope, acceptance, production-shaped gate, and close verification authority.
3. `_hirmos/session/SESSION_EXECUTION.md` — human-readable Current Continuation Snapshot, execution-control spine, evidence ledger, and close/update controls.
4. `_hirmos/session/unresolved-items.md` — governed unresolved-item register.
5. `_hirmos/session/DESIGN.md` — conditional governed Design authority.
6. `_hirmos/session/EVIDENCE.md` — conditional evidence surface for nontrivial implementation/runtime/close evidence.
7. `_hirmos/session/implementation-units/` — conditional implementation unit contracts, evidence, reviews, and retries.
8. `_hirmos/session/bootstrap/` — required session infrastructure for startup/bootstrap evidence.
9. `_hirmos/session/SESSION_EXECUTION.md` Current Continuation Snapshot — required session infrastructure for continuation/continuation snapshot records.
10. `_hirmos/session/stack-resolution.json` — conditional machine-readable stack-routing state only.
11. `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md` — durable current system truth.
12. `_hirmos/system/history/sessions/<session-id>/` — archived evidence.

New sessions use the smallest strict-necessity surface that can preserve governance, engineering quality, evidence, and continuity. Do not create separate support files for request intake, source materials, technical review, implementation readiness, runtime evidence, close checklist, claim reconciliation, archive manifest, or session-scope review.

## Command state machine

HIRMOS command legality is governed by `_hirmos/core/protocol/COMMAND_STATE_MACHINE.md` and `_hirmos/session/SESSION_STATE.json`. `hirmos start` pauses at implementation readiness; `hirmos continue` appends cumulative continuation passes; `hirmos close` enforces archive/reset invariants.

## Integration surface

AI-tool integration templates live in the framework payload under:

```text
_hirmos/integrations/agent-tools/
```

The terminal CLI reads that surface during `hirmos init` and generates tool-specific files such as `AGENTS.md`, `CLAUDE.md`, Cursor rules, Copilot instructions, and other supported integration outputs. The published CLI installs this surface; it does not own it.

Canonical reference phrases: HIRMOS uses `_hirmos/session/SESSION_SCOPE.md`, `_hirmos/session/unresolved-items.md`, self-contained `implementation-units/IU-xx.md`, and accepted-state navigation in `CURRENT_SYSTEM_STATE.md` as key runtime references.
