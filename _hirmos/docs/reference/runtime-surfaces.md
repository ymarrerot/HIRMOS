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
7. `_hirmos/session/implementation-units/` — conditional implementation unit authority records, evidence, reviews, and retries.
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
      PHASE-xx.md               # conditional phase scope
```

`DELIVERY_PLAN.md` is append/update-oriented and preserves delivery history. `DELIVERY_SCOPE.md` is the default combined delivery authority. Separate delivery-level `REQUIREMENTS.md` and `DESIGN.md` are optional only when independent authority is justified.

## PROD-L8.9 focus-aware runtime command and capability routing

Commands execute the delivery authority model through capability routing.

- `hirmos start` selects the delivery shape and required route before implementation readiness.
- `hirmos continue` preserves or explicitly amends the route before implementation/correction work.
- `hirmos status` reports route readiness, blocked capabilities, artifact concordance, and one next command.
- `hirmos close` reconciles the route against session, delivery, phase, evidence, unresolved, and accepted-state artifacts.

Canonical delivery routes:

```text
SINGLE_SESSION_VERTICAL_SLICE → session-scope → implementation-readiness
SINGLE_SESSION_WITH_IMPLEMENTATION_UNITS → session-scope → implementation-readiness
DELIVERY_BASELINE / delivery_baseline → delivery-baseline
DELIVERY_PHASE_SESSION / phase_session_baseline → phase-baseline → session-scope → implementation-readiness
```


## PROD-L8.9 delivery baseline focus

HIRMOS always runs inside a governed runtime session envelope, but `SESSION_SCOPE.md` is required only when the active work has a bounded phase/session work scope. Durable delivery-baseline work uses `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md` as active authority and `_hirmos/system/delivery/<delivery-id>/unresolved-items.md` for delivery-level unresolved items.

Before delivery-baseline acceptance, HIRMOS records a complete phase coverage plan inside `DELIVERY_SCOPE.md` and does not instantiate future `PHASE-xx.md` files by default. After acceptance, HIRMOS instantiates the next phase/session authority just in time.

## Focus-aware runtime surfaces

The active `SESSION_STATE.json.session_focus` determines which surfaces are required.

| `session_focus` | Required surfaces | Surfaces not created by default |
|---|---|---|
| `minimal_session` | `SESSION_STATE.json`, `SESSION_EXECUTION.md`, and `SESSION_SCOPE.md` only when bounded output authority is needed | delivery artifacts, implementation units, optional requirements/design unless justified |
| `session_baseline` | `SESSION_STATE.json`, `SESSION_EXECUTION.md`, `SESSION_SCOPE.md`; session unresolved items only when material items exist | delivery artifacts unless adopted; implementation units before acceptance |
| `delivery_baseline` | `SESSION_STATE.json`, `SESSION_EXECUTION.md`, `DELIVERY_PLAN.md`, `<delivery-id>/DELIVERY_SCOPE.md`, `<delivery-id>/unresolved-items.md` | `SESSION_SCOPE.md`, session unresolved items, `PHASE-xx.md`, implementation units |
| `phase_session_baseline` | accepted delivery scope, next instantiated phase file, `SESSION_SCOPE.md`, session unresolved items when needed | future phase files and implementation units before acceptance |
| `implementation` | accepted `SESSION_SCOPE.md`, implementation controls, evidence/unit surfaces as needed | new authority artifacts unless the session is amended |

This model preserves a single command/session envelope while preventing delivery-level authority from being stored in session-local scope artifacts.
