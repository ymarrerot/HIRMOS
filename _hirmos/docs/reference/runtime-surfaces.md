# Runtime Surfaces Reference

The most important runtime surfaces are:

1. `_hirmos/session/SESSION_STATE.json` — machine command/lifecycle state.
2. `_hirmos/session/SESSION_CONTRACT.md` — active session scope and acceptance authority.
3. `_hirmos/session/SESSION_EXECUTION.md` — execution-control spine.
4. `_hirmos/session/unresolved-items.md` — governed unresolved-item register.
5. `_hirmos/session/implementation-units/` — implementation unit contracts and reviews.
6. `_hirmos/session/support/` — subordinate evidence appendices.
7. `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md` — durable current system truth.
8. `_hirmos/system/history/sessions/<session-id>/` — archived evidence.

New sessions use `unresolved-items.md`, `SESSION_CONTRACT.md`, self-contained `implementation-units/IU-xx.md`, root `session-contract-review.md`, and accepted-state navigation in `CURRENT_SYSTEM_STATE.md` as canonical runtime surfaces.


## Command state machine

HIRMOS command legality is governed by `_hirmos/core/protocol/COMMAND_STATE_MACHINE.md` and `_hirmos/session/SESSION_STATE.json`. `hirmos start` pauses at implementation readiness; `hirmos continue` appends cumulative continuation passes; `hirmos close` enforces archive/reset invariants.

## Integration surface

AI-tool integration templates live in the framework payload under:

```text
_hirmos/integrations/agent-tools/
```

The terminal CLI reads that surface during `hirmos init` and generates tool-specific files such as `AGENTS.md`, `CLAUDE.md`, Cursor rules, Copilot instructions, and other supported integration outputs. The published CLI installs this surface; it does not own it.
