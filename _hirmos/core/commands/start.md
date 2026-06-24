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
8a. `_hirmos/core/templates/checkpoints/START_CHECKPOINT_OUTPUT.md` before surfacing the first implementation-readiness checkpoint
9. `_hirmos/core/protocol/CURRENT_SYSTEM_STATE.md`
10. `_hirmos/core/protocol/REQUIREMENTS.md`
11. `_hirmos/core/protocol/RUNTIME_INTEGRATION_AND_PRODUCTION_READINESS.md` when material runtime services are involved

Read stack, capability, template, and extension files only when the active command controls require them. Capability and extension routing must follow `_hirmos/core/protocol/CAPABILITY_ROUTING.md`; command-triggered routing and adaptive-read discipline must follow `_hirmos/core/protocol/COMMANDS.md`. When Design, Implementation, Update System State, project type, stack, runtime integration, delivery governance, or unresolved-item state requires a specialized capability decision, read `_hirmos/core/protocol/CAPABILITY_ROUTING.md` before selecting extension or capability entrypoints.


## Production-shaped engineering posture

When the command reaches Design, Implementation, or close/update-state for software work, HIRMOS must apply the production-shaped default from `_hirmos/core/authority/LIFECYCLE.md` and `_hirmos/core/protocol/RUNTIME_INTEGRATION_AND_PRODUCTION_READINESS.md`. Do not treat prototype/demo/local-only shortcuts as neutral defaults. They must be explicitly authorized, evidenced, and preserved as limitations or carry-forward items.

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

### Runtime timestamp source

Before creating timestamped session artifacts, `hirmos start` must populate `_hirmos/session/SESSION_STATE.json` → `run_context` from a reliable runtime source: CLI-provided timestamp, shell `date -u`, or explicit user-provided timestamp. Do not infer dates from model memory, prior chat context, or examples. All generated `created_at`, `updated_at`, session-id date segments, authorization dates, checkpoint dates, and close/archive timestamps must derive from `SESSION_STATE.json.run_context`. If no reliable timestamp source is available, stop at `Blocked / Fail-Closed` and request or obtain one before writing timestamped artifacts.

### Required state mutation

### Delivery Shape Decision Gate

Before `hirmos start` may claim `Ready for Implementation` for any implementation-capable request, it must apply `_hirmos/core/protocol/DELIVERY_GOVERNANCE.md` and answer this literal question in `SESSION_EXECUTION.md` and `SESSION_SCOPE.md`:

```text
What is the smallest sufficient governed delivery shape for this request?
Answer: SINGLE_SESSION_VERTICAL_SLICE / SINGLE_SESSION_WITH_IMPLEMENTATION_UNITS / MULTI_SESSION_DELIVERY / MULTI_SESSION_DELIVERY_WITH_PHASE_FILES / UNCERTAIN.
Evidence:
Decision factors:
Smaller-shape safety analysis:
Larger-shape overhead analysis:
Required durable delivery artifacts, if any:
If UNCERTAIN, what must be inspected before deciding?
```

Fail-closed behavior:

- `UNCERTAIN` blocks implementation readiness until resolved.
- `SINGLE_SESSION_VERTICAL_SLICE` requires affirmative bounded-scope safety evidence.
- `SINGLE_SESSION_WITH_IMPLEMENTATION_UNITS` requires implementation units that collectively cover the Session Scope after the session scope baseline has been accepted or amended. Before acceptance, only implementation-shape preview information may be recorded.
- `MULTI_SESSION_DELIVERY` requires a durable Delivery Plan before implementation authorization.
- `MULTI_SESSION_DELIVERY_WITH_PHASE_FILES` requires a durable Delivery Plan and exactly one adopted durable phase file before implementation authorization.

Use the smallest governed delivery shape that preserves engineering quality, implementation truth, reviewability, validation, continuity, and accepted-state integrity.

Capability routing:

- `SINGLE_SESSION_MINIMAL` may route through `session-scope` only when a bounded output authority is needed;
- single-session implementation shapes route through `session-scope → implementation-readiness`;
- durable delivery work starts with `DELIVERY_BASELINE / delivery_baseline → delivery-baseline`;
- after delivery-baseline acceptance or amendment, phase/session work routes through `DELIVERY_PHASE_SESSION / phase_session_baseline → phase-baseline → session-scope → implementation-readiness`.

When `hirmos start` accepts a governable request, it must update `SESSION_STATE.json` to an active session before lifecycle work continues:

- `status = active`;
- `session_id` populated;
- `lifecycle_stage` advanced through the governed start stages as they are reached;
- `status`, `allowed_next_commands`, `recommended_next_command`, `blocking_reason`, and `updated_at` updated at every user-facing boundary;


The final start state depends on `session_focus`:

- `minimal_session`: stop at the minimal governed output checkpoint or completion boundary selected by the request;
- `session_baseline`: stop at `Recommended Baseline — Review or Change`;
- `delivery_baseline`: stop at `Delivery Baseline — Review or Change` with delivery authority as the active authority;
- `phase_session_baseline`: stop at `Session Baseline — Review or Change`.

At every user-facing checkpoint, `allowed_next_commands` must include only safe governed commands, normally `hirmos continue` and `hirmos status`, and `recommended_next_command` must explain what `hirmos continue` will accept or advance.

### Start sequence

1. Verify bootstrap passed for the current agent/context.
2. Capture the User Request from the command argument, current conversation, or declared input files.
3. If the User Request is missing or too unclear to govern, stop at `Request Not Governable` and ask for the missing request.
4. Verify the active working copy and `_hirmos/` installation.
5. Populate `_hirmos/session/SESSION_STATE.json` → `run_context` from a reliable runtime timestamp source before writing timestamped artifacts.
6. Create `_hirmos/session/SESSION_EXECUTION.md` from the session template before lifecycle work begins.
7. Record session id, active command, User Request, interaction mode, active lifecycle boundary, and continuation state.
8. Establish baseline execution controls.
9. Instantiate only the session artifacts required before the first review checkpoint.
10. Run Understand System State before claiming Design authority.
10. During Understand System State, read `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md` first when it exists. If it is missing, record the absence explicitly in `_hirmos/session/DESIGN.md` and `_hirmos/session/SESSION_EXECUTION.md`.
11. Read supporting accepted-state artifacts (`CURRENT_SYSTEM_STATE.md` latest-close metadata, `CARRY_FORWARD.md`, `DECISION_LOG.md`) when present. Use session archives only as history/evidence, not as the primary current-state source.
12. Use the User Request and source inputs to guide focused system-state understanding, but do not treat them as governed requirements.
13. Route to Design only after the system-state and current-system-state-first controls are satisfied, explicitly not applicable with rationale, or blocked.
14. Before Design work selects specialized extension capabilities, apply `_hirmos/core/protocol/CAPABILITY_ROUTING.md` and record material capability decisions in `_hirmos/session/SESSION_EXECUTION.md`.
15. In `domain_expert` mode, attempt to advance through Understand System State and Design until a gated user-owned decision, implementation-readiness, blocker, or non-governable request is reached.
16. Do not begin Implementation during `hirmos start`. Stop at the focus-appropriate checkpoint: `Recommended Baseline — Review or Change` for single-session scope, `Delivery Baseline — Review or Change` for delivery baseline, or `Session Baseline — Review or Change` for a phase/session baseline.


## Mandatory implementation-readiness pause

`hirmos start` must stop before implementation. For single-session work, it stops after creating/updating the required session baseline artifacts and surfacing a governed first-review checkpoint using `_hirmos/core/templates/checkpoints/START_CHECKPOINT_OUTPUT.md`. For durable delivery work, it stops after creating/updating delivery-baseline artifacts and surfacing `Delivery Baseline — Review or Change`; `SESSION_SCOPE.md`, `PHASE-xx.md`, and implementation-unit artifacts are not created by default before delivery-baseline acceptance.

The checkpoint heading must be:

```text
Recommended Baseline — Review or Change
```

Before returning control to the user, `hirmos start` must explain:

- what HIRMOS understood;
- what HIRMOS is going to do;
- what HIRMOS is not going to do;
- recommended delivery shape and why it was selected;
- gated unresolved items from `_hirmos/session/unresolved-items.md#Current Checkpoint Feed`;
- non-gating assumptions from `_hirmos/session/unresolved-items.md#Current Checkpoint Feed`;
- material technical-review items and where to inspect them;
- artifacts worth reviewing before continuation;
- what `hirmos continue` will do;
- exactly one next governed command: `hirmos continue`.

The checkpoint must state that if the user runs `hirmos continue`, HIRMOS will treat the recommended baseline as accepted unless the user requests changes first.

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
| Snapshot-backed checkpoint control | always | user-facing checkpoint references missing/placeholders |
| System-state control | always for governed software work | current-state evidence missing or insufficient |
| Current-system-state-first control | always for governed software work | `CURRENT_SYSTEM_STATE.md` exists but was not read first, missing status was not recorded, or accepted-state contradictions were not classified |
| Unresolved-item control | always for governed sessions | `_hirmos/session/unresolved-items.md` missing, not directly reviewed, gated items unresolved, or classification missing |
| Session Scope control | before Implementation or close | `SESSION_SCOPE.md` missing, placeholder, incomplete, or not coverage-reviewed |
| Delivery Shape Decision control | before Implementation Readiness for implementation-capable sessions | shape missing, UNCERTAIN, unsafe smaller shape, or selected durable-delivery shape without required artifacts |
| Production-Shaped Engineering Gate control | before Implementation Readiness for implementation-capable software sessions | gate missing, material area blocked, or weaker posture not explicitly authorized |
| Design control | when Design is needed | governed requirements/design/session scope missing or blocked |
| Implementation authorization control | before Implementation | Design has not authorized Implementation |
| Validation/evidence control | when evidence is claimed | claimed evidence lacks artifact/log/output |


## Current-system-state-first enforcement

`hirmos start` must treat `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md` as the primary accepted current-state source.

Future sessions must read delivery pointers during Understand System State before deciding that a request is safe for a single-session path. If `Next recommended delivery` and `Next recommended delivery scope` are present, adopt that delivery context unless the user request is clearly unrelated.

Before meaningful Design or Implementation begins:

- `CURRENT_SYSTEM_STATE.md` exists and has been read first; or
- its absence has been explicitly recorded; and
- supporting accepted-state artifacts have been read when present; and
- archive history has not been used as a substitute for current truth; and
- `_hirmos/session/DESIGN.md` records the accepted-state read status, contradictions, confidence, and handoff to Design.

Firm rule: do not claim `Ready for Implementation`, `Implementation Complete`, or `Ready to Update System State` from `hirmos start` while the current-system-state-first control is `PENDING` or `BLOCKED`.

## Readiness and pause rules

Do not claim `Ready for Implementation` unless:

- Understand System State controls are satisfied;
- Design controls are satisfied;
- unresolved gated items are resolved or the command stops at `Needs User Decision`;
- `_hirmos/session/unresolved-items.md` was directly reviewed, not inferred from the Session Scope summary;
- `SESSION_SCOPE.md` exists, covers authorized scope, and authorizes Implementation;
- implementation authorization is recorded;
- the Production-Shaped Engineering Gate is complete for material areas or explicitly not applicable;
- any referenced artifacts exist and are non-placeholder.

If user-owned Domain/Risk/Resource decisions block progress, surface a concise decision checkpoint and stop at `Needs User Decision`.

If system evidence, Design authority, or required artifacts are insufficient, stop at `Blocked / Fail-Closed`.


## Session artifact instantiation rules

`hirmos start` must create `_hirmos/session/SESSION_EXECUTION.md` before lifecycle work begins. It must then instantiate only artifacts required by the active request path.

Common instantiation sequence before the first review checkpoint:

1. `SESSION_EXECUTION.md` always.
2. `_hirmos/session/SESSION_STATE.json#run_context` before timestamped artifacts are written.
3. `unresolved-items.md` always for governed sessions.
4. `SESSION_SCOPE.md` before Implementation can be authorized or close can be claimed.
5. `REQUIREMENTS.md` or `DESIGN.md` only when separate authority is justified, and `SESSION_SCOPE.md` must record the separate authority justification.
6. Durable delivery artifacts under `_hirmos/system/delivery/<delivery-id>/` only when the selected delivery shape requires them.
7. Implementation-shape preview may be recorded in `SESSION_SCOPE.md` only when it helps the user accept or change the baseline.
8. Full implementation-unit artifacts under `_hirmos/session/implementation-units/` must not be created before the session scope baseline has been accepted or amended.
9. Implementation artifacts are created only when Implementation is authorized.
10. Update System State / close major artifact sections only when close/update-state is active.

Implementation-unit artifacts are created only after the session scope baseline is accepted or amended. This prevents stale duplicate plans and keeps detailed implementation-unit planning in one canonical location: `_hirmos/session/implementation-units/`.

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

The first implementation-readiness checkpoint must use `_hirmos/core/templates/checkpoints/START_CHECKPOINT_OUTPUT.md`. It must be sourced from `_hirmos/session/unresolved-items.md#Current Checkpoint Feed`, not from memory or a loose summary.


Before surfacing a checkpoint that asks for a decision, claims readiness/completion, fails closed, or changes continuation state, HIRMOS must:

1. read `_hirmos/core/protocol/GOVERNED_CHECKPOINTS.md`;
2. update `_hirmos/session/SESSION_EXECUTION.md` → `Current Continuation Snapshot` when required;
3. verify the Current Continuation Snapshot is backed by existing non-placeholder session artifacts;
4. verify unresolved-item status from `_hirmos/session/unresolved-items.md` when decisions, assumptions, blockers, or continuation are involved;
5. record the surfaced boundary in `SESSION_EXECUTION.md` Continuation Boundary Log;
6. surface only claims supported by the Current Continuation Snapshot and active controls.


## Project-type and stack controls

When the active request involves software work, the command must ensure project-type and stack controls are represented in `SESSION_EXECUTION.md`.

Required behavior:

- classify project type from evidence, not User Request label alone;
- select stack from repository evidence first, then accepted state, request/config preference, prototype evidence, installed packages, or `generic` fallback;
- record material project-type decisions in `DESIGN.md` / `SESSION_SCOPE.md`, record machine-readable stack routing in `stack-resolution.json` when needed, and record command controls in `SESSION_EXECUTION.md`;
- activate stack contexts only when evidence shows multiple bounded stack areas;
- block or route back when project type, stack, or stack context uncertainty affects authority or evidence.


## Runtime integration controls

When the active request may involve material runtime services, read `_hirmos/core/protocol/RUNTIME_INTEGRATION_AND_PRODUCTION_READINESS.md` and add runtime-integration controls to `SESSION_EXECUTION.md`.

Required behavior:

- instantiate or update `_hirmos/session/DESIGN.md` / `_hirmos/session/EVIDENCE.md` when material integration areas affect Design, Implementation, evidence, production readiness, or close;
- do not silently downgrade real integration requirements to fixtures, mocks, console fallbacks, or boundary-only work;
- do not surface low-level provider choices to Domain Expert users unless the protocol requires surfacing;
- do not claim implementation completion, production readiness, or close success beyond the integration posture supported by evidence.

## Vertical slice and status UX

When the active request uses a Delivery Plan, Phase, Delivery Unit, or implementation slice, read `_hirmos/core/protocol/VERTICAL_SLICE_AND_STATUS_UX.md`.

Required behavior:

- identify the active Delivery Unit / Phase when one exists;
- instantiate or update `_hirmos/system/delivery/DELIVERY_PLAN.md and _hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md status log` when delivery status materially affects the user-facing checkpoint or next action;
- keep `SESSION_EXECUTION.md` aligned with the active slice status;
- recommend exactly one primary next command/action unless blocked;
- do not imply the next Delivery Unit is authorized unless its governing authority and controls support it.

## Claim reconciliation behavior

When this command surfaces a material readiness, progress, implementation, validation, runtime, integration, production-readiness, packaging, update-state, or close claim, it must apply `_hirmos/core/protocol/CLAIM_RECONCILIATION.md`.

Unsupported, unlogged, contradicted, or environment-blocked claims must be downgraded, routed back, or blocked before being shown as complete.

## Requirements-baseline-first Design enforcement

Before meaningful Design for governed software work, `hirmos start` must establish `_hirmos/session/REQUIREMENTS.md` when source requirements, prototype-derived signals, UI design notes, reference materials, or accepted prior requirements materially affect scope.

Required behavior:

- inventory and classify material source inputs;
- read `_hirmos/system/accepted-state/REQUIREMENTS.md` when it exists;
- instantiate `_hirmos/session/REQUIREMENTS.md` before Design relies on source requirements;
- normalize material requirements into stable requirement IDs;
- classify non-goals, gated/unresolved requirements, blocked inputs, duplicates, superseded items, and not-applicable items;
- record source traceability for each material requirement;
- block or route back when Design would otherwise proceed from raw requirements or prototype evidence alone.

Firm rule: do not claim `Ready for Implementation` until material in-scope requirements are mapped to Delivery Units, deferred, blocked, gated, or explicitly not applicable in `REQUIREMENTS.md`.

## Current System State Delivery Pointer Precheck


Before delivery-shape selection, inspect `Last accepted delivery`, `Next recommended delivery`, and `Next recommended delivery scope` from `CURRENT_SYSTEM_STATE.md`. If a next delivery is recommended and the user request is compatible with planned continuation, adopt that delivery as the active context. Do not default to a single-session path while a compatible next recommended delivery is waiting.

Before final Delivery Shape Decision, `hirmos start` must read the Active Development Context and Delivery Pointers in `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md` when present.

If those pointers indicate an active, blocked, or next recommended durable delivery/phase, `hirmos start` must not default to a single-session path merely because the current user request is short. It must either adopt the active durable delivery context or record why the new request is unrelated and safely bounded.

If the pointers reference a missing or contradictory Delivery Plan or Phase file, final start state is `blocked`, and `recommended_next_command` must not be `hirmos continue`.

## Durable Phase Adoption Pre-Implementation Gate

When the selected delivery shape is `MULTI_SESSION_DELIVERY_WITH_PHASE_FILES`, `hirmos start` must not end at implementation readiness until `SESSION_SCOPE.md` adopts exactly one durable phase file.

Required checks:

- read `_hirmos/system/delivery/DELIVERY_PLAN.md and _hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md`;
- read the selected `_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md` directly;
- confirm Current System State active delivery pointers do not contradict the selected phase;
- write the Active Durable Phase Adoption section in `SESSION_SCOPE.md`;
- map adopted phase items to authorized Session Scope items and implementation units;
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

## PROD-L8.9 focus-aware route runtime behavior

`hirmos start` must use the Delivery Shape Decision and `session_focus` to select the runtime capability route before it creates delivery/session authority artifacts.

Required behavior:

1. Read Current System State delivery pointers before shape selection.
2. Apply `_hirmos/core/protocol/CAPABILITY_ROUTING.md` and record a capability routing table in `SESSION_EXECUTION.md`.
3. For `SINGLE_SESSION_MINIMAL`, create only the minimal artifacts needed by the requested output; do not create unresolved, requirements, design, delivery, evidence, or implementation-unit artifacts unless strictly necessary.
4. For single-session implementation shapes, instantiate `SESSION_SCOPE.md` and record delivery governance as `NOT_APPLICABLE` with affirmative bounded-scope safety evidence.
5. For durable delivery baseline, set `session_focus = delivery_baseline`, require `delivery-baseline`, create/update only delivery-baseline artifacts under `_hirmos/system/delivery/<delivery-id>/`, and stop at `Delivery Baseline — Review or Change`.
6. For phase/session work after delivery-baseline acceptance, set `session_focus = phase_session_baseline`, require `phase-baseline → session-scope → implementation-readiness`, instantiate only the next needed `PHASE-xx.md`, create `SESSION_SCOPE.md`, and stop at `Session Baseline — Review or Change` before implementation.
7. If any required capability is `BLOCKED` or `ROUTE_BACK_REQUIRED`, stop before implementation readiness and recommend exactly one safe next command.

`hirmos start` must not create a per-delivery `DELIVERY_PLAN.md` under `<delivery-id>/`, must not create delivery artifacts for a safe single-session request, must not create future phase files before delivery-baseline acceptance by default, and must not overwrite the top-level delivery roadmap/register.

## PROD-L8.9E/F Focus-Aware Checkpoint Output

After `session_focus` is resolved, `hirmos start` must use `START_CHECKPOINT_OUTPUT.md` to select either `DELIVERY_BASELINE_CHECKPOINT_OUTPUT.md` or `SESSION_BASELINE_CHECKPOINT_OUTPUT.md`. A delivery-baseline pause must not create `_hirmos/session/SESSION_SCOPE.md`, concrete future phase files, or implementation-unit artifacts.
