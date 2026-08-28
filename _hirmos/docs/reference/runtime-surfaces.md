# Runtime Surfaces Reference

This reference maps the runtime surfaces HIRMOS uses during a governed run.

## Command surface

The compact runtime command authority is:

```text
_hirmos/core/commands/
```

The command files for `start`, `continue`, `status`, and `close` are the first command-specific authority the agent should follow. Protocol files under `_hirmos/core/protocol/` are deeper reference authority and should be read when the command or a gate requires them.

## Most important active runtime surfaces

1. `_hirmos/session/SESSION_STATE.json` — minimal machine command/lifecycle state and derived command-state cache.
2. `_hirmos/session/SESSION_SCOPE.md` — active session scope, acceptance, production-shaped gate, and close verification authority.
3. `_hirmos/session/SESSION_LEDGER.md` — human-readable command/gate ledger, evidence handoff pointers, and close/update control pointers.
4. `_hirmos/session/unresolved-items.md` — governed unresolved-item register when material unresolved items exist.
5. `_hirmos/session/DESIGN.md` — conditional governed Design authority.
6. `_hirmos/session/EVIDENCE.md` — conditional evidence surface for nontrivial implementation/runtime/close evidence.
7. `_hirmos/session/implementation-units/` — conditional implementation unit authority records, evidence, reviews, and retries.
8. `_hirmos/session/bootstrap/` — required session infrastructure for startup/bootstrap evidence.
9. `_hirmos/session/stack-resolution.json` — conditional machine-readable stack-routing state only.
10. `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md` — durable accepted-state navigation.
11. `_hirmos/system/history/sessions/<session-id>/` — archived evidence and closed session artifacts.

New sessions use the smallest strict-necessity surface that can preserve governance, engineering quality, evidence, and continuity.

## Delivery authority surface

```text
_hirmos/system/delivery/
  DELIVERY_PLAN.md              # durable project delivery roadmap/register and pointer surface
  <delivery-id>/
    DELIVERY_SCOPE.md           # stable authority for one delivery/release
    unresolved-items.md         # delivery-level unresolved register
    phases/
      PHASE-xx.md               # conditional phase authority created just in time
```

`DELIVERY_PLAN.md` should not be a duplicate mutable status log. `DELIVERY_SCOPE.md` should not mirror runtime completion state. Phase files should not duplicate parent delivery status. Completion posture should be derived from accepted source artifacts.

## Focus-aware runtime surfaces

The active `SESSION_STATE.json.session_focus` determines which surfaces are required.

| `session_focus` | Required surfaces | Surfaces not created by default |
|---|---|---|
| `minimal_session` | `SESSION_STATE.json`, `SESSION_LEDGER.md`, and `SESSION_SCOPE.md` only when bounded output authority is needed | delivery artifacts, implementation units, optional requirements/design unless justified |
| `session_baseline` | `SESSION_STATE.json`, `SESSION_LEDGER.md`, `SESSION_SCOPE.md`; session unresolved items only when material items exist | delivery artifacts unless adopted; implementation units before acceptance |
| `delivery_baseline` | `SESSION_STATE.json`, `SESSION_LEDGER.md`, `DELIVERY_PLAN.md`, `<delivery-id>/DELIVERY_SCOPE.md`, `<delivery-id>/unresolved-items.md` | `SESSION_SCOPE.md`, session unresolved items, `PHASE-xx.md`, implementation units |
| `phase_session_baseline` | accepted delivery scope, next instantiated phase file, `SESSION_SCOPE.md`, session unresolved items when needed | future phase files and implementation units before acceptance |
| `implementation` | accepted `SESSION_SCOPE.md`, implementation controls, evidence/unit surfaces as needed | new authority artifacts unless the session is amended |

## IU implementation route

When implementation units are required:

```text
Session Baseline accepted
→ IU Planning only
→ IU Plan — Review or Change
→ IU Plan accepted
→ IU Execution
```

IU Planning creates/validates the IU files and pauses. It is not material implementation authorization.

For software implementation, `SESSION_SCOPE.md` carries the session-level automated-testing posture. When IU mode applies, each sealed IU refines that posture into concrete behavioral test obligations, relevant existing-test baselines when practical, and any higher-level validation still required. Test execution and test-delta review remain part of Implementation rather than a separate testing phase.

## Integration surface

AI-tool integration templates live in the framework payload under:

```text
_hirmos/integrations/agent-tools/
```

The terminal CLI reads that surface during `hirmos init` and `hirmos update` to generate or reconcile tool-specific files such as `AGENTS.md`, `CLAUDE.md`, Cursor rules, Copilot instructions, and other supported integration outputs.

## Derived pointer surfaces

Pointer indexes in Current System State, Delivery Plan, Phase files, and ledger status surfaces are derived navigation caches. If a pointer conflicts with a source artifact, the source artifact wins and validation should fail closed instead of preserving a stale pointer.

## Protocol ownership and minimality

HIRMOS has private protocols because they protect different failure modes. The ownership rule is: one canonical owner per concern, with secondary documents pointing to that owner instead of restating full governance.

The intended result is not fewer checks at any cost. It is fewer duplicate rules, fewer brittle wording checks, and stronger authority-safety/freshness checks.


Canonical reference phrases: HIRMOS uses `_hirmos/session/SESSION_SCOPE.md`, `_hirmos/session/unresolved-items.md`, self-contained `implementation-units/IU-xx.md`, and accepted-state navigation in `CURRENT_SYSTEM_STATE.md` as key runtime references.


Source authority is kept at the narrowest safe level: delivery/session/archive artifacts own detailed scope and evidence, while current-state artifacts own navigation and traceability.


## Focus-aware runtime command and capability routing

Commands select the active focus and route capabilities accordingly. `hirmos status` reports route readiness, blocked capabilities, artifact concordance, and one next command.


## Capability taxonomy and source authority minimality

HIRMOS uses capability families to explain routing without expanding the runtime surface. Capability IDs remain stable dispatch identifiers, while capability families help reviewers see whether a new responsibility can reuse an existing capability.
