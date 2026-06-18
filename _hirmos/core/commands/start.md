# Command: hirmos start

Purpose: start a governed HIRMOS session from a User Request.

## Execution contract

Produces:

- `_hirmos/session/SESSION_EXECUTION.md`
- instantiated session artifacts required by the active request path
- system-state artifacts required by controls
- Design artifacts required by controls
- user-facing checkpoint when HIRMOS needs a decision, reaches implementation-readiness, or is blocked

Terminal states:

- Needs User Decision
- Ready for Implementation
- Blocked / Fail-Closed
- Request Not Governable

## Required reads

Before execution:

1. `_hirmos/core/protocol/COMMANDS.md`
2. `_hirmos/core/protocol/COMMAND_STATE_MACHINE.md`
2. `_hirmos/core/authority/LIFECYCLE.md`
3. `_hirmos/core/authority/EXECUTION_CONTROL_GOVERNANCE.md`
4. `_hirmos/core/authority/INTERACTION_MODES.md`
5. `_hirmos/core/authority/ARTIFACT_MODEL.md`
6. `_hirmos/core/protocol/UNRESOLVED_ITEMS.md`
7. `_hirmos/core/protocol/GOVERNED_CHECKPOINTS.md`
8. `_hirmos/core/protocol/VALIDATION_AND_EVIDENCE.md`
9. `_hirmos/core/protocol/CURRENT_SYSTEM_STATE.md`
10. `_hirmos/core/protocol/REQUIREMENTS_BASELINE.md`
11. `_hirmos/core/protocol/RUNTIME_INTEGRATION_AND_PRODUCTION_READINESS.md` when material runtime services are involved

Read stack, capability, template, and extension files only when the active command controls require them. Capability and extension routing must follow `_hirmos/core/protocol/CAPABILITY_ROUTING.md`; command-triggered routing and adaptive-read discipline must follow `_hirmos/core/protocol/COMMANDS.md`. When Design, Implementation, Update System State, project type, stack, runtime integration, delivery governance, or unresolved-item state requires a specialized capability decision, read `_hirmos/core/protocol/CAPABILITY_ROUTING.md` before selecting extension or capability entrypoints.

## Required behavior


### Command-state gate

Before starting lifecycle work, `hirmos start` must apply `_hirmos/core/protocol/COMMAND_STATE_MACHINE.md` and verify:

- `_hirmos/session/SESSION_STATE.json` exists and is valid;
- `status` is `idle`;
- `lifecycle_stage` is `idle`;
- `hirmos start` appears in `allowed_next_commands`;
- the active session folder contains only the allowed idle scaffold;
- no stale active-session artifacts remain from a previous close.

If any check fails, `hirmos start` must stop at `Blocked / Fail-Closed`, identify the failed precondition, and recommend exactly one governed recovery command. It must not create a new session over an active or stale session.

### Required state mutation

### Delivery-Need Classification Gate

Before `hirmos start` may claim `Ready for Implementation` for any implementation-capable request, it must apply `_hirmos/core/protocol/DELIVERY_GOVERNANCE.md` and answer this literal question in `SESSION_EXECUTION.md` and `SESSION_CONTRACT.md`:

```text
Does this request require multi-session delivery governance?
Answer: YES / NO / UNCERTAIN.
Evidence:
Decision factors:
If NO, why is one bounded session safe?
If YES, required Delivery Plan:
If UNCERTAIN, what must be inspected before deciding?
```

Fail-closed behavior:

- `YES` requires a durable Delivery Plan at `_hirmos/system/delivery/<delivery-id>/DELIVERY_PLAN.md` and at least one phase file under `_hirmos/system/delivery/<delivery-id>/phases/` before implementation can be authorized.
- `UNCERTAIN` blocks implementation readiness until the uncertainty is resolved.
- `NO` requires affirmative single-session safety evidence and a list of Delivery Plan triggers considered and ruled out.

For multi-session work in any project type, a Delivery Plan is needed and separate phase files are required. HIRMOS must bias toward delivery governance when classification is ambiguous. When classification is `YES`, Design must route through `delivery-design → phase-contracting → session-contract → implementation-readiness` before implementation authorization.

When `hirmos start` accepts a governable request, it must update `SESSION_STATE.json` to an active session before lifecycle work continues:

- `status = active`;
- `active_command = hirmos start`;
- `last_command = hirmos start`;
- `session_id` and `session_title` populated;
- `lifecycle_stage` advanced through the governed start stages as they are reached;
- `allowed_next_commands` and `recommended_next_command` updated at every user-facing boundary.

For implementation-capable sessions, the final start state must be `lifecycle_stage = implementation_readiness`, `allowed_next_commands = ["hirmos continue", "hirmos status"]`, and `recommended_next_command = hirmos continue`.

### Start sequence

1. Verify bootstrap passed for the current agent/context.
2. Capture the User Request from the command argument, current conversation, or declared input files.
3. If the User Request is missing or too unclear to govern, stop at `Request Not Governable` and ask for the missing request.
4. Verify the active working copy and `_hirmos/` installation.
5. Create `_hirmos/session/SESSION_EXECUTION.md` from the session template before lifecycle work begins.
6. Record session id, active command, User Request, interaction mode, active lifecycle boundary, and continuation state.
7. Establish baseline execution controls.
8. Instantiate only the session artifacts required by the active request path.
9. Run Understand System State before claiming Design authority.
10. During Understand System State, read `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md` first when it exists. If it is missing, record the absence explicitly in `_hirmos/session/support/system-state.md` and `_hirmos/session/SESSION_EXECUTION.md`.
11. Read supporting accepted-state artifacts (`CURRENT_SYSTEM_STATE.md` latest-close metadata, `CARRY_FORWARD.md`, `DECISION_LOG.md`) when present. Use session archives only as history/evidence, not as the primary current-state source.
12. Use the User Request and source inputs to guide focused system-state understanding, but do not treat them as governed requirements.
13. Route to Design only after the system-state and current-system-state-first controls are satisfied, explicitly not applicable with rationale, or blocked.
14. Before Design work selects specialized extension capabilities, apply `_hirmos/core/protocol/CAPABILITY_ROUTING.md` and record material capability decisions in `_hirmos/session/SESSION_EXECUTION.md`.
15. In `domain_expert` mode, attempt to advance through Understand System State and Design until a gated user-owned decision, implementation-readiness, blocker, or non-governable request is reached.
16. Do not begin Implementation during `hirmos start`; stop at `Ready for Implementation` when Design and Session Contract controls authorize implementation.


## Mandatory implementation-readiness pause

`hirmos start` must stop before implementation. For implementation-capable sessions, the terminal state is `Ready for Implementation` after HIRMOS has created/updated the contract-centered start artifacts and surfaced what it understood.

Before returning control to the user, `hirmos start` must explain:

- what HIRMOS understood;
- what HIRMOS is going to do;
- what HIRMOS is not going to do;
- affected areas/artifacts;
- planned implementation units, when applicable;
- gated unresolved items;
- non-gating assumptions;
- required validation;
- exactly one next governed command: `hirmos continue`.

HIRMOS must not begin implementation during `hirmos start` unless the active request is explicitly design-only or analysis-only and no implementation is being performed.

## Required baseline controls

Record these controls in `SESSION_EXECUTION.md` at minimum:

| Control | Required when | Blocking condition |
|---|---|---|
| Bootstrap control | always | bootstrap report missing or quiz not passed |
| Command control | always | command spec not read or terminal states unknown |
| Working-copy control | always | project root or `_hirmos/` cannot be verified |
| User Request control | always | no governable request |
| Interaction-mode control | always | configured mode missing or unsupported |
| Lifecycle-boundary control | always | active boundary missing or inconsistent |
| SESSION_EXECUTION control | always | execution spine not created or not updated |
| Artifact-backed checkpoint control | always | user-facing checkpoint references missing/placeholders |
| System-state control | always for governed software work | current-state evidence missing or insufficient |
| Current-system-state-first control | always for governed software work | `CURRENT_SYSTEM_STATE.md` exists but was not read first, missing status was not recorded, or accepted-state contradictions were not classified |
| Unresolved-item control | always for governed sessions | `_hirmos/session/unresolved-items.md` missing, not directly reviewed, gated items unresolved, or classification missing |
| Session Contract control | before Implementation or close | `SESSION_CONTRACT.md` missing, placeholder, incomplete, or not coverage-reviewed |
| Delivery-Need Classification control | before Implementation Readiness for implementation-capable sessions | classification missing, UNCERTAIN, unsafe NO, or YES without durable Delivery Plan and phase file |
| Design control | when Design is needed | governed requirements/design/session contract missing or blocked |
| Implementation authorization control | before Implementation | Design has not authorized Implementation |
| Validation/evidence control | when evidence is claimed | claimed evidence lacks artifact/log/output |


## Current-system-state-first enforcement

`hirmos start` must treat `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md` as the primary accepted current-state source.

Before meaningful Design or Implementation begins:

- `CURRENT_SYSTEM_STATE.md` exists and has been read first; or
- its absence has been explicitly recorded; and
- supporting accepted-state artifacts have been read when present; and
- archive history has not been used as a substitute for current truth; and
- `_hirmos/session/support/system-state.md` records the accepted-state read status, contradictions, confidence, and handoff to Design.

Firm rule: do not claim `Ready for Implementation`, `Implementation Complete`, or `Ready to Update System State` from `hirmos start` while the current-system-state-first control is `PENDING` or `BLOCKED`.

## Readiness and pause rules

Do not claim `Ready for Implementation` unless:

- Understand System State controls are satisfied;
- Design controls are satisfied;
- unresolved gated items are resolved or the command stops at `Needs User Decision`;
- `_hirmos/session/unresolved-items.md` was directly reviewed, not inferred from the Session Contract summary;
- `SESSION_CONTRACT.md` exists, covers authorized scope, and authorizes Implementation;
- implementation authorization is recorded;
- any referenced artifacts exist and are non-placeholder.

If user-owned Domain/Risk/Resource decisions block progress, surface a concise decision checkpoint and stop at `Needs User Decision`.

If system evidence, Design authority, or required artifacts are insufficient, stop at `Blocked / Fail-Closed`.


## Session artifact instantiation rules

`hirmos start` must create `_hirmos/session/SESSION_EXECUTION.md` before lifecycle work begins. It must then instantiate only artifacts required by the active request path.

Common instantiation sequence:

1. `SESSION_EXECUTION.md` always.
2. `support/request-intake.md`, `support/source-materials.md`, or `support/prototype-ingestion.md` when request/source/prototype inputs require durable extraction.
3. `support/system-state.md` for governed software work.
4. `unresolved-items.md` always for governed sessions.
5. `SESSION_CONTRACT.md` before Implementation can be authorized or close can be claimed.
6. Design artifacts only when Design is active.
7. Durable delivery artifacts under `_hirmos/system/delivery/<delivery-id>/` when Delivery-Need Classification is YES.
8. Implementation artifacts only when Implementation is authorized.
8. Update System State / close support artifacts only when close/update-state is active.

Every created artifact must be recorded in `SESSION_EXECUTION.md` under `Artifact Instantiation Log`. Do not reference an artifact as inspectable or ready until it exists and contains non-placeholder content.

## Required `SESSION_EXECUTION.md` updates

Before returning control to the user, update:

- Active command;
- Active lifecycle boundary;
- Continuation state;
- Active execution controls and statuses;
- Artifact instantiation log;
- Lifecycle progress;
- Checkpoint record;
- Terminal state.

## Governed checkpoint rules

Before surfacing a checkpoint that asks for a decision, claims readiness/completion, fails closed, or changes continuation state, HIRMOS must:

1. read `_hirmos/core/protocol/GOVERNED_CHECKPOINTS.md`;
2. instantiate `_hirmos/session/checkpoints/CHECKPOINT_<checkpoint-id>.md` when required;
3. verify the checkpoint artifact is backed by existing non-placeholder session artifacts;
4. verify unresolved-item status from `_hirmos/session/unresolved-items.md` when decisions, assumptions, blockers, or continuation are involved;
5. record the checkpoint in `SESSION_EXECUTION.md`;
6. surface only claims supported by the checkpoint artifact and active controls.


## Project-type and stack controls

When the active request involves software work, the command must ensure project-type and stack controls are represented in `SESSION_EXECUTION.md`.

Required behavior:

- classify project type from evidence, not User Request label alone;
- select stack from repository evidence first, then accepted state, request/config preference, prototype evidence, installed packages, or `generic` fallback;
- instantiate `support/project-context.md` and `support/stack-resolution.json` when project-type or stack decisions affect Design, Implementation, validation, or Update System State;
- activate stack contexts only when evidence shows multiple bounded stack areas;
- block or route back when project type, stack, or stack context uncertainty affects authority or evidence.


## Runtime integration controls

When the active request may involve material runtime services, read `_hirmos/core/protocol/RUNTIME_INTEGRATION_AND_PRODUCTION_READINESS.md` and add runtime-integration controls to `SESSION_EXECUTION.md`.

Required behavior:

- instantiate or update `_hirmos/session/support/runtime-integration-readiness.md` when material integration areas affect Design, Implementation, evidence, production readiness, or close;
- do not silently downgrade real integration requirements to fixtures, mocks, console fallbacks, or boundary-only work;
- do not surface low-level provider choices to Domain Expert users unless the protocol requires surfacing;
- do not claim implementation completion, production readiness, or close success beyond the integration posture supported by evidence.

## Vertical slice and status UX

When the active request uses a Delivery Plan, Phase, Delivery Unit, or implementation slice, read `_hirmos/core/protocol/VERTICAL_SLICE_AND_STATUS_UX.md`.

Required behavior:

- identify the active Delivery Unit / Phase when one exists;
- instantiate or update `_hirmos/system/delivery/<delivery-id>/DELIVERY_PLAN.md status log` when delivery status materially affects the user-facing checkpoint or next action;
- keep `SESSION_EXECUTION.md` aligned with the active slice status;
- recommend exactly one primary next command/action unless blocked;
- do not imply the next Delivery Unit is authorized unless its governing contract and controls support it.

## Claim reconciliation behavior

When this command surfaces a material readiness, progress, implementation, validation, runtime, integration, production-readiness, packaging, update-state, or close claim, it must apply `_hirmos/core/protocol/CLAIM_RECONCILIATION.md`.

Unsupported, unlogged, contradicted, or environment-blocked claims must be downgraded, routed back, or blocked before being shown as complete.

## Requirements-baseline-first Design enforcement

Before meaningful Design for governed software work, `hirmos start` must establish `_hirmos/session/REQUIREMENTS_BASELINE.md` when source requirements, prototype-derived signals, UI design notes, reference materials, or accepted prior requirements materially affect scope.

Required behavior:

- inventory and classify material source inputs;
- read `_hirmos/system/accepted-state/REQUIREMENTS_BASELINE.md` when it exists;
- instantiate `_hirmos/session/REQUIREMENTS_BASELINE.md` before Design relies on source requirements;
- normalize material requirements into stable requirement IDs;
- classify non-goals, gated/unresolved requirements, blocked inputs, duplicates, superseded items, and not-applicable items;
- record source traceability for each material requirement;
- block or route back when Design would otherwise proceed from raw requirements or prototype evidence alone.

Firm rule: do not claim `Ready for Implementation` until material in-scope requirements are mapped to Delivery Units, deferred, blocked, gated, or explicitly not applicable in `REQUIREMENTS_BASELINE.md`.

## Current System State Delivery Pointer Precheck

Before final Delivery-Need Classification, `hirmos start` must read the Active Development Context and Delivery Pointers in `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md` when present.

If those pointers indicate an active, blocked, or next recommended durable delivery/phase, `hirmos start` must not default to a single-session path merely because the current user request is short. It must either adopt the active durable delivery context or record why the new request is unrelated and safely bounded.

If the pointers reference a missing or contradictory Delivery Plan or Phase file, final start state is `blocked`, and `recommended_next_command` must not be `hirmos continue`.

## Durable Phase Adoption Pre-Implementation Gate

When Delivery-Need Classification is `YES`, `hirmos start` must not end at implementation readiness until `SESSION_CONTRACT.md` adopts exactly one durable phase file.

Required checks:

- read `_hirmos/system/delivery/<delivery-id>/DELIVERY_PLAN.md`;
- read the selected `_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md` directly;
- confirm Current System State active delivery pointers do not contradict the selected phase;
- write the Active Durable Phase Adoption section in `SESSION_CONTRACT.md`;
- map adopted phase items to authorized Session Contract items and implementation units;
- record deferrals for any phase item not adopted.

Fail-closed rule: if phase adoption is missing, ambiguous, multi-phase, pointer-conflicting, or unmapped, final start state is `blocked` or remains before implementation readiness, and `recommended_next_command` must not be `hirmos continue` for implementation.

## Phase Entry Gate Enforcement

This command must respect the Phase Entry Gate for delivery-governed sessions.

- `hirmos start` must not reach implementation readiness when the adopted phase has no passing Phase Entry Gate.
- `hirmos continue` must re-check Phase Entry Gate concordance before continuing implementation if delivery governance is active.
- `hirmos status` must report whether the active phase is adoptable, blocked, or uncertain based on lifecycle status, phase type, and entry controls.
- `hirmos close` must fail closed if the session implemented a phase without recorded Phase Entry Gate authorization.

Required status terms: Phase Entry Gate, lifecycle status, phase type, entry criteria satisfied, greenfield entry controls, brownfield entry controls, pointer concordance.

## Phase Progress / Carry-Forward Enforcement

This command must respect phase progress and carry-forward enforcement for delivery-governed sessions.

- `hirmos start` must inspect prior Phase Progress Ledger rows before treating a multi-session phase as new work.
- `hirmos continue` must preserve append-only phase progress and must not drop partial, blocked, deferred, or open phase items.
- `hirmos status` must report whether phase progress is accepted, partial, blocked, deferred, or waiting on carry-forward obligations.
- `hirmos close` must fail closed when phase outcome is `PARTIAL`, `BLOCKED`, or `DEFERRED` and carry-forward obligations are missing.

Required status terms: Phase Progress Ledger, Carry-Forward Items, partial phase, blocked phase, deferred phase, resulting lifecycle status, Current System State active/next phase pointer.


## Phase Acceptance Enforcement

`hirmos start` must inspect prior Phase Acceptance Evidence Gate results when continuing a delivery. If the previous phase is `READY_FOR_ACCEPTANCE`, the new session may be review/close-oriented, but it must not implement new work until the phase acceptance decision is resolved or a new phase is explicitly adopted.
