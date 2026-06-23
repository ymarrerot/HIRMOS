# Runtime Surfaces Reference


## PROD-L scope-authority naming note

`SESSION_SCOPE.md` is the canonical active session authority. `DELIVERY_SCOPE.md` is the canonical target name for one durable delivery/release authority; `DELIVERY_PLAN.md` is the project delivery roadmap/register.

The most important runtime surfaces are:

1. `_hirmos/session/SESSION_STATE.json` — minimal machine command/lifecycle state only.
2. `_hirmos/session/SESSION_SCOPE.md` — active session scope, acceptance, production-shaped gate, and close verification authority.
3. `_hirmos/session/SESSION_EXECUTION.md` — human-readable Current Continuation Snapshot, execution-control spine, evidence handoff pointers, and close/update control pointers.
4. `_hirmos/session/unresolved-items.md` — governed unresolved-item register.
5. `_hirmos/session/DESIGN.md` — conditional governed Design authority.
6. `_hirmos/session/EVIDENCE.md` — conditional evidence surface for nontrivial implementation/runtime/close evidence.
7. `_hirmos/session/implementation-units/` — conditional implementation unit contracts, evidence, reviews, and retries.
8. `_hirmos/session/bootstrap/` — required session infrastructure for startup/bootstrap evidence.
9. `_hirmos/session/SESSION_EXECUTION.md` Current Continuation Snapshot — required session infrastructure for continuation/continuation snapshot records.
10. `_hirmos/session/stack-resolution.json` — conditional machine-readable stack-routing state only.
11. `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md` — durable current system truth.
12. `_hirmos/system/history/sessions/<session-id>/` — archived evidence.

New sessions use the smallest strict-necessity surface that can preserve governance, engineering quality, evidence, and continuity. Do not create separate active-session support files for request intake, source materials, technical review, implementation readiness, runtime evidence, close checklist, claim reconciliation, or session-scope review. Use history-level `ARCHIVE_MANIFEST.md` only during close/archive.

## Command state machine

HIRMOS command legality is governed by `_hirmos/core/protocol/COMMAND_STATE_MACHINE.md` and `_hirmos/session/SESSION_STATE.json`. `hirmos start` pauses at implementation readiness; `hirmos continue` appends cumulative continuation passes; `hirmos close` enforces archive/reset invariants.

## Integration surface

AI-tool integration templates live in the framework payload under:

```text
_hirmos/integrations/agent-tools/
```

The terminal CLI reads that surface during `hirmos init` and generates tool-specific files such as `AGENTS.md`, `CLAUDE.md`, Cursor rules, Copilot instructions, and other supported integration outputs. The published CLI installs this surface; it does not own it.

Canonical reference phrases: HIRMOS uses `_hirmos/session/SESSION_SCOPE.md`, `_hirmos/session/unresolved-items.md`, self-contained `implementation-units/IU-xx.md`, and accepted-state navigation in `CURRENT_SYSTEM_STATE.md` as key runtime references.


## PROD-L3 delivery authority surface

```text
_hirmos/system/delivery/
  DELIVERY_PLAN.md              # durable project delivery roadmap/register
  <delivery-id>/
    DELIVERY_SCOPE.md           # scoped authority for one delivery/release
    phases/
      PHASE-xx.md               # conditional phase contract
```

`DELIVERY_PLAN.md` is append/update-oriented and preserves delivery history. `DELIVERY_SCOPE.md` is the default combined delivery authority. Separate delivery-level `REQUIREMENTS.md` and `DESIGN.md` are optional only when independent authority is justified.

## PROD-L4 runtime command and capability routing

Commands execute the delivery authority model through capability routing.

- `hirmos start` selects the delivery shape and required route before implementation readiness.
- `hirmos continue` preserves or explicitly amends the route before implementation/correction work.
- `hirmos status` reports route readiness, blocked capabilities, artifact concordance, and one next command.
- `hirmos close` reconciles the route against session, delivery, phase, evidence, unresolved, and accepted-state artifacts.

Canonical delivery routes:

```text
SINGLE_SESSION_VERTICAL_SLICE → session-scope → implementation-readiness
SINGLE_SESSION_WITH_IMPLEMENTATION_UNITS → session-scope → implementation-readiness
MULTI_SESSION_DELIVERY → delivery-design → session-scope → implementation-readiness
MULTI_SESSION_DELIVERY_WITH_PHASE_FILES → delivery-design → phase-contracting → session-scope → implementation-readiness
```
