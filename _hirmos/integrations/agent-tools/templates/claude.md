<!-- HIRMOS:START -->
## HIRMOS for Claude

This project uses HIRMOS.

For HIRMOS work, read and follow:

```text
_hirmos/AGENTS.md
```

That file remains the HIRMOS agent instruction authority for this project. This integration file is not a replacement for HIRMOS core authority; it repeats the minimum command gates here because tool-native guidance is often the first instruction surface the coding agent follows.

## HIRMOS pre-edit gate

For any user message that begins with `hirmos`, read `_hirmos/AGENTS.md` first and obey the command boundary before editing files.

- `hirmos start` is non-implementation: it must end at a governed baseline checkpoint and must not edit project/source files outside `_hirmos/`.
- Detailed implementation instructions in a start request are scope input, not implementation authorization.
- Material project/source edits require accepted baseline authority recorded in HIRMOS session artifacts.
- If implementation units are required, baseline acceptance authorizes IU planning only; material edits additionally require IU plan review and `IU_EXECUTION_AUTHORIZED`.
- Never implement first and backfill HIRMOS artifacts afterward.

## hirmos start command gate

When the user runs `hirmos start`:

1. Read `_hirmos/AGENTS.md` and the start command authority.
2. Inspect only the current system state and relevant inputs needed to scope the request.
3. Create or update the required HIRMOS session governance artifacts.
4. Present the governed baseline checkpoint for user review.
5. Stop.

Do not edit product/source files during `hirmos start`, even if the user includes complete implementation instructions.

## hirmos continue command gate

`hirmos continue` must classify and gate before it codes.

Before any product/source edit or implementation claim, the agent must:

1. Read `_hirmos/session/SESSION_STATE.json`, `_hirmos/session/SESSION_SCOPE.md`, and `_hirmos/session/SESSION_LEDGER.md` when present.
2. Classify the continue request as acceptance, amendment, IU planning, IU execution authorization, correction, validation, route-back, close preparation, or blocked.
3. Append the continuation pass record to `SESSION_LEDGER.md` before acting.
4. If the request changes accepted authority, append the corresponding authority delta to `SESSION_SCOPE.md` before implementation continues.
5. Check whether implementation units are required or requested.

IU rules for `hirmos continue`:

- If the user requests implementation units and no accepted IU plan exists, create or revise the IU plan and stop at `IU Plan — Review or Change`.
- If the user does not request implementation units, still evaluate whether IUs are required by scope, risk, multi-file impact, validation complexity, or governance value.
- If IUs are required, baseline acceptance authorizes IU Planning only. It does not authorize product/source edits.
- Product/source edits in IU mode require a later explicit continuation that records `IU_EXECUTION_AUTHORIZED` after IU plan review.
- Never create IU files after material implementation to show compliance.

If implementation units are not required, record a concise no-IU rationale in the existing session governance artifacts before implementation begins.

## hirmos status command gate

`hirmos status` is read-only.

When the user runs `hirmos status`:

1. Read the active HIRMOS state and relevant session/delivery artifacts.
2. Report the current lifecycle stage, active gate, blocker/conflict if any, and exactly one recommended next command.
3. Report whether baseline authority is accepted and whether IU execution is authorized when IU mode applies.
4. Do not edit product/source files.
5. Do not advance lifecycle state.
6. Do not backfill artifacts to make status appear clean.

## hirmos close command gate

`hirmos close` may close only after evidence-backed review supports the completion claim. If evidence, accepted authority, IU execution authorization, or artifact concordance is missing, fail closed and report the next valid command instead of archiving.


## Canonical HIRMOS integration invariant projection

The following invariant excerpt is generated from `_hirmos/integrations/agent-tools/capsules/invariants.md` and must remain aligned with the command and skill projections.

{{INVARIANTS_BODY}}
<!-- HIRMOS:END -->
