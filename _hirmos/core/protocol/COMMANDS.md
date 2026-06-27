# Command Protocol

Status: core protocol.
Purpose: define how user command intent routes into HIRMOS lifecycle responsibilities without making commands lifecycle authorities.

Commands are user actions. Commands are not lifecycle stages. Commands activate, continue, inspect, or close governed work by routing into lifecycle responsibilities.

## Public commands

### Governance posture for every command

Commands authorize work; they do not merely label work after it happened. HIRMOS is not an after-the-fact compliance layer. Before a command edits project files, creates implementation evidence, performs a correction, or updates accepted state, the command must confirm that `SESSION_STATE.json`, the active authority artifact, and the command-specific protocol permit the action.

If the command state is invalid, HIRMOS must fail closed or route to the command that creates valid authority. It must not act first and then reconstruct session artifacts, implementation units, evidence, or correction ledgers to satisfy governance afterward.


```text
hirmos start
hirmos continue
hirmos status
hirmos close
```

## Command-intent rule

If user input begins with `hirmos`, treat it as HIRMOS runtime command intent.

Do not downgrade malformed HIRMOS command input into ordinary prose. Fail clearly and recommend supported command forms.

Supported forms:

```text
hirmos start [user request]
hirmos continue
hirmos status
hirmos close
```

## Bootstrap prerequisite

No command may execute until bootstrap has passed for the current agent/context.

Bootstrap completion means the bootstrap report exists, records a passed quiz, includes every bootstrap discipline answer with durable source and allowed recovery method, and does not rely on chat memory or compressed chat summaries. Acknowledging files were read is not enough.


## General run preflight

Before any public command advances work, HIRMOS must verify the minimum installed runtime surface required for the requested command and current integration context. This is a general run rule for every project; HIRMOS must not create special run-category routing or setup semantics.

Required preflight classification:

| Classification | Meaning | Required behavior |
|---|---|---|
| `PRECHECK_PASS` | Required command/core/session/integration surface exists. | Continue to command-state gate. |
| `PRECHECK_WARNING` | A non-required or optional integration/setup surface is missing, but fallback bootstrap authority is sufficient. | Surface the warning, record fallback authority, and continue only if the requested command remains legal. |
| `PRECHECK_BLOCKER` | Required command/core/session/integration surface is missing or contradictory. | Stop before lifecycle work and recommend exactly one governed recovery action. |

Missing integration registry or generated AI-tool files are preflight issues, not implementation/session-governance failures by themselves. If the selected integration depends on `_hirmos/integrations/agent-tools/registry.json` and it is missing, surface the setup action, for example `hirmos init --integration <tool>`, or record that fallback bootstrap through `_hirmos/AGENTS.md` is sufficient for the current command.

## Advancing command rule

`hirmos start`, `hirmos continue`, and `hirmos close` are advancing commands.

Every advancing command must:

1. verify bootstrap completion;
2. read the matching command specification;
3. create or read `_hirmos/session/SESSION_EXECUTION.md` as required by the command;
4. establish command-specific execution controls before doing lifecycle work;
5. read adaptive command, capability, stack, template, and validation files only as controls require them;
6. update `SESSION_EXECUTION.md` before every user-facing readiness, completion, or blocked checkpoint;
7. fail closed if required controls are `PENDING` or `BLOCKED` at a readiness or completion boundary.

## Read-only command rule

`hirmos status` is read-only. It may inspect state and report gaps. It must not advance lifecycle work, satisfy controls by assertion, instantiate new lifecycle artifacts, or mutate accepted system state.

## Command summaries

`hirmos start` starts a governed session from a User Request. It begins with request capture, creates `SESSION_EXECUTION.md`, establishes controls, and starts with Understand System State.

`hirmos continue` advances the current lifecycle boundary only when the active execution controls allow continuation.

`hirmos status` reports active or last-known HIRMOS state without advancing governed work.

`hirmos close` runs Update System State when ready, archives the session, and resets the active session area.


## Command state machine discipline


### command protocol application

Every public command specification must include command-state preconditions, state mutation rules, postconditions, and fail-closed recovery behavior. Command files may describe command-specific work, but they must not redefine the transition matrix in `_hirmos/core/protocol/COMMAND_STATE_MACHINE.md`.

Required command-state discipline for all commands:

| Requirement | Rule |
|---|---|
| Legality check | Read `SESSION_STATE.json` before advancing work and verify the requested command is legal for `status`, `lifecycle_stage`, and `allowed_next_commands`. |
| Artifact-state check | Verify active/idle session scaffold consistency before executing an advancing command. |
| State mutation | Update `SESSION_STATE.json` whenever a command changes lifecycle stage, continuation pass, blocking state, or recommended next command. |
| Execution ledger | Update `SESSION_EXECUTION.md` for every advancing command, and append rather than overwrite command history. |
| Response discipline | Surface exactly one primary next governed command that is legal under the updated `SESSION_STATE.json`. |
| Fail closed | If legality, artifacts, or state are contradictory, stop before lifecycle work and recommend exactly one governed recovery command. |

Command-specific files must use this protocol as their local command authority.

Every command must apply `_hirmos/core/protocol/COMMAND_STATE_MACHINE.md` before recommending or executing a next command. `SESSION_STATE.json` is the machine-readable command-state authority. `SESSION_EXECUTION.md` explains execution history but must not override `SESSION_STATE.json`.

Command legality is determined by:

- `SESSION_STATE.json.status`;
- `SESSION_STATE.json.lifecycle_stage`;
- `SESSION_STATE.json.allowed_next_commands`;
- active-session artifact presence or absence;
- fail-closed controls recorded in `SESSION_EXECUTION.md`.

If command legality is unclear or contradictory, the command must stop at a blocked/fail-closed state and recommend exactly one governed recovery command.

## Mandatory start pause rule

`hirmos start` must not go directly into implementation. For implementation-capable single-session work, it must stop at the session baseline checkpoint after creating the needed Session Scope, execution ledger, runtime timestamp context, and any conditional session requirements/design/unresolved authority justified by the selected route. For durable delivery work, it must stop at the delivery baseline checkpoint with `session_focus = delivery_baseline`, delivery authority under `_hirmos/system/delivery/<delivery-id>/`, and no `SESSION_SCOPE.md` by default.

The user-facing pause must use `_hirmos/core/templates/checkpoints/START_CHECKPOINT_OUTPUT.md` and surface `Recommended Baseline — Review or Change` before implementation begins. If the user runs `hirmos continue`, HIRMOS treats the baseline as accepted unless the user requested changes first.

Full implementation-unit artifacts must not be instantiated before the session scope baseline has been accepted or amended. The next governed command is `hirmos continue`.

## Cumulative continue pass rule

`hirmos continue` is append-only. Each invocation must append a continuation pass record in `SESSION_EXECUTION.md`. Corrections, scope amendments, validation reruns, and route-backs must preserve prior pass history instead of overwriting it.

## Exactly-one-next-command rule

Every command response must recommend exactly one primary governed next command. Prose such as `reply to proceed` is not a governed command.

## Snapshot-backed checkpoint rule

A command must not tell the user that an artifact exists, is ready, can be inspected, or authorizes a next step unless the artifact exists and contains non-placeholder content.

## Terminal-state rule

Every advancing command response must end in one clear terminal state from its command specification.

If no terminal state can be reached safely, the command must enter `Blocked / Fail-Closed` or the command-specific blocked state and explain what control prevents continuation.

## Bootstrap-only boundary

If the user asked only for bootstrap, command execution is not authorized after bootstrap completes.


## Capability routing during commands

Advancing commands route needed work through installed extension capabilities when specialized work is needed to satisfy the active lifecycle boundary. Commands do not select capabilities by memory or preference; they route through `_hirmos/core/protocol/CAPABILITY_ROUTING.md` when routing is material.

Capability routing materially affects lifecycle progress when the command must decide whether any installed extension capability is `REQUIRED`, `OPTIONAL`, `SKIPPED`, `NOT_APPLICABLE`, or `BLOCKED` before the active lifecycle boundary can safely continue.

At minimum, capability routing is material when:

- moving from Understand System State into Design;
- deciding whether Design can reach implementation-readiness;
- deciding whether Implementation may begin, continue, retry, or complete;
- deciding whether Update System State may accept outcomes, archive, or close;
- selecting requirements, system-design, delivery-baseline, phase-baseline, session-scope, technical-review, implementation-readiness, implementation, validation, evidence, or update-state capabilities;
- a required artifact or execution control names a capability, extension, or entrypoint;
- unresolved items, project type, stack evidence, delivery governance, runtime services, or current-state evidence affects which specialized work must run;
- a capability may produce or update artifacts required for a readiness claim, completion claim, blocker, route-back, or user-facing checkpoint.

When routing is material, the runner must read `_hirmos/core/protocol/CAPABILITY_ROUTING.md`, resolve the required extension and capability entrypoints through the installed manifests, and record the capability decision in `_hirmos/session/SESSION_EXECUTION.md`.

Commands must not expose capability routing details by default unless the routing creates a user decision, blocker, validation failure, route-back, or inspectable checkpoint.


## Runtime integration command discipline

Advancing commands must activate runtime integration controls when material services such as database, auth, messaging, storage, payments, deployment, or provider APIs affect the active request.

Commands must not claim implementation completion, production readiness, update-state readiness, or close success beyond the posture and evidence recorded in `_hirmos/session/DESIGN.md` / `_hirmos/session/EVIDENCE.md`, `SESSION_EXECUTION.md`, and relevant review artifacts.

## Vertical slice and status UX discipline

When Delivery Units, Phases, or implementation slices are active, advancing commands must read `_hirmos/core/protocol/VERTICAL_SLICE_AND_STATUS_UX.md` and maintain clear next-action status.

Advancing command responses should recommend exactly one primary next command or terminal next action unless blocked.

Commands must not preserve momentum by hiding blockers. Status summaries must distinguish:

- active slice;
- completed work;
- blocked controls;
- next allowed action;
- next recommended Delivery Unit when known.

## Close / accepted-state integrity discipline

`hirmos close` must read `_hirmos/core/protocol/CLOSE_ARCHIVE_AND_ACCEPTED_STATE.md` before claiming normal close success.

Close success requires a consistent transaction across:

- active session evidence;
- `SESSION_EXECUTION.md` close/update control pointers;
- `SESSION_EXECUTION.md` close controls;
- archive manifest;
- accepted-state records;
- reset `SESSION_STATE.json`;
- post-close `hirmos status` output.

If these surfaces disagree, `hirmos close` must stop at `Close Blocked` or use an explicit abort-close path. It must not present archived artifacts as accepted current state unless Update System State accepted them.

## Claim reconciliation command rule

Any command that surfaces readiness, progress, implementation completion, runtime readiness, production readiness, package completeness, update-state readiness, or close success must apply claim reconciliation before surfacing the claim.

The command must either:

- create or update `_hirmos/session/EVIDENCE.md`;
- point to an existing current claim reconciliation record; or
- record why claim reconciliation is `NOT_APPLICABLE`.

A command must not use chat-only summaries as claim evidence.

## Autonomous technical progress command rule

Advancing commands must apply `_hirmos/core/protocol/AUTONOMOUS_TECHNICAL_PROGRESS.md` when technical setup, runtime integration, validation, local services, environment configuration, or provider adapters affect the active request.

Commands should be firm and direct: make safe progress, fix encountered runtime problems inside accepted scope, record evidence, and recommend the next action.

Commands must not ask the user to make routine technical choices until HIRMOS has checked whether the answer can be safely discovered or a safe default can be applied. Commands must ask or route to technical review when the choice affects domain behavior, cost, compliance, credential/account ownership, destructive operations, or production readiness.

## Local setup and role-workflow smoke evidence

Use `LOCAL_TECHNICAL_SETUP_AND_ROLE_WORKFLOW_SMOKE_CHECKS.md` for the governing rules when HIRMOS claims local runtime behavior, user-environment verification, or role workflow readiness.

Required artifacts when applicable:

- `_hirmos/session/EVIDENCE.md` records local environment, service, migration, seed, dev-server, and route evidence.
- `_hirmos/session/EVIDENCE.md` records role-specific workflow smoke evidence for the relevant end-user, operator, privileged-user, and administrative paths.
- `_hirmos/session/EVIDENCE.md` reconciles whether the claim may be surfaced.

Firm rule: tests/build/lint alone do not prove local runtime readiness or role workflow readiness.

## durable current-system-state current-state command invariant

Commands that surface accepted current truth must use `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md` as the primary source.

`hirmos close` must update or explicitly verify unchanged current system state before claiming success. `hirmos status` must prefer current system state over archive summaries, chat memory, or current-state latest-close metadata summaries.


## Current-date and session-id discipline

Commands that create session identifiers, archive paths, close records, accepted-state timestamps, or dated reports must resolve the actual current date from the runtime environment, available tool context, or explicit user-provided date. They must not reuse example dates, prior session dates, generated template dates, or stale dates from copied artifacts.

If the current date cannot be established, the command must record the uncertainty in `_hirmos/session/SESSION_EXECUTION.md` and avoid date-specific claims until the date is resolved. Session IDs and archive folder names must be consistent with the resolved current date or explicitly documented as user-provided identifiers.

## PROD-L8.9 command-to-capability routing behavior

Runtime commands must treat capability routing as part of command execution, not as optional design commentary.

Command-specific behavior:

- `hirmos start` must perform Delivery Shape Decision and `session_focus` routing before claiming any readiness checkpoint. It creates only the artifacts required by the selected focus and route.
- `hirmos continue` must re-check the active focus and route before delivery-baseline acceptance, phase/session baseline preparation, implementation, retry, or correction work. It must not silently switch from delivery-governed work to single-session work or adopt a different phase without a recorded authority amendment.
- `hirmos status` must report the active session_focus, delivery route when applicable, required capabilities, artifact readiness, blocked capability decisions, and exactly one safe next governed command.
- `hirmos close` must reconcile the route and focus used by the session against the active authority (`DELIVERY_SCOPE.md` or `SESSION_SCOPE.md`), `SESSION_EXECUTION.md`, delivery artifacts, evidence, unresolved items, and accepted-state pointers before close success.

The command surface does not redefine capability methods. It reads `_hirmos/core/protocol/CAPABILITY_ROUTING.md`, resolves installed extension/capability manifests, records the routing decisions in `SESSION_EXECUTION.md`, and follows the selected entrypoints.


## Runtime session envelope and focus rule

HIRMOS always runs commands inside a governed runtime session envelope. A runtime session is not always an implementation session.

`SESSION_STATE.json.session_focus` identifies the active work focus. Supported values are:

```text
minimal_session
session_baseline
delivery_baseline
phase_session_baseline
implementation
correction
close
status
```

`SESSION_SCOPE.md` is required when the session focus has a bounded phase/session work scope or implementation authority. It is not required during `delivery_baseline` focus; in that state the active authority is `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md` and delivery-level unresolved items are recorded in `_hirmos/system/delivery/<delivery-id>/unresolved-items.md`. During `delivery_baseline`, `_hirmos/session/unresolved-items.md` is `NOT_APPLICABLE` and must not be created as an empty placeholder.

Commands must update `SESSION_STATE.json.active_authority`, `active_delivery_id`, `active_delivery_scope`, and `active_phase` when those fields apply. User-facing output must name the active focus and explain what `hirmos continue` will accept or advance.

SESSION_SCOPE.md is required when the session focus has a bounded phase/session work scope.

## PROD-L8.9E/F Checkpoint Template Enforcement

`hirmos start` must select the governed checkpoint template from `START_CHECKPOINT_OUTPUT.md` after resolving `session_focus`. `delivery_baseline` pauses with `Delivery Baseline — Review or Change`. `session_baseline` and `phase_session_baseline` pause with `Session Baseline — Review or Change`. `hirmos continue` must preserve this acceptance boundary and must not skip from delivery-baseline acceptance directly into implementation.


## PROD-L8.10 delivery-baseline session-surface minimality

During `session_focus = delivery_baseline`, commands must preserve a minimal session runtime surface: `SESSION_STATE.json` and `SESSION_EXECUTION.md` only. Delivery-level authority and unresolved items live under `_hirmos/system/delivery/<delivery-id>/`. Do not create `_hirmos/session/SESSION_SCOPE.md` or `_hirmos/session/unresolved-items.md` until the flow advances to `phase_session_baseline` or another bounded session-scope focus. `hirmos status` must report session unresolved as `NOT_APPLICABLE` in delivery-baseline focus and point reviewers to `_hirmos/system/delivery/<delivery-id>/unresolved-items.md`.

L8.10 explicit prohibition: during `session_focus = delivery_baseline`, HIRMOS must not create `_hirmos/session/unresolved-items.md`; delivery unresolved items belong only in `_hirmos/system/delivery/<delivery-id>/unresolved-items.md` until a bounded session baseline exists.

## PROD-L8.11 Delivery-Baseline Optional Authority Location

When `SESSION_STATE.json.session_focus = delivery_baseline`, the active authority is delivery-level. Optional requirements/design authority must be located under `_hirmos/system/delivery/<delivery-id>/` only:

- `_hirmos/system/delivery/<delivery-id>/REQUIREMENTS.md` when separate delivery-level requirements authority is justified.
- `_hirmos/system/delivery/<delivery-id>/DESIGN.md` when separate delivery-level design authority is justified.

During `delivery_baseline`, HIRMOS must not create, update, list, or depend on `_hirmos/session/REQUIREMENTS.md` or `_hirmos/session/DESIGN.md`. If separate optional authority is not justified, requirements and design decisions remain inside `DELIVERY_SCOPE.md` only. Session-level optional authority artifacts become applicable only after the flow advances to a bounded `phase_session_baseline` or `session_baseline` focus.


## PROD-L8.13 Delivery Review Wording

When reporting delivery-baseline state, use status-aware delivery labels. Before baseline acceptance, use Candidate Delivery, Proposed Delivery, or Delivery Under Baseline Review. Use Active Delivery only after the baseline has been accepted/amended and the delivery is in a post-acceptance state. Explain routing from current-state-first evidence and governance need rather than from greenfield/brownfield labels alone.

## Protocol ownership matrix

This matrix is the first authority for resolving protocol-document overlap. It does not add a new runtime layer; it assigns ownership to existing files so future edits reuse the correct surface instead of duplicating governance.

| Concern | Canonical owner | Supporting surfaces | Must not redefine |
|---|---|---|---|
| Lifecycle responsibility boundaries | `core/authority/LIFECYCLE.md` | command files, capability routing | command files, extension entrypoints |
| Command legality, command state, and next-command discipline | `core/protocol/COMMAND_STATE_MACHINE.md` plus the matching `core/commands/<command>.md` | `COMMANDS.md`, `SESSION_STATE.json`, `SESSION_EXECUTION.md` | capability entrypoints |
| Command-to-capability routing algorithm | `core/protocol/CAPABILITY_ROUTING.md` | extension manifests, capability manifests, command files | individual capability entrypoints |
| Accepted-state navigation and current-state spine | `core/protocol/CURRENT_SYSTEM_STATE.md` | `CURRENT_SYSTEM_STATE.md` template, `close.md`, `status.md` | delivery/session source artifacts |
| Close/archive/update-state transaction | `core/protocol/CLOSE_ARCHIVE_AND_ACCEPTED_STATE.md` | `CURRENT_SYSTEM_STATE.md`, `CARRY_FORWARD.md`, `SESSION_EXECUTION.md`, `close.md` | status or continue command docs |
| Delivery authority and delivery-baseline behavior | `core/protocol/DELIVERY_GOVERNANCE.md` | `DELIVERY_SCOPE.md`, `DELIVERY_PLAN.md`, delivery checkpoint template | session scope templates during delivery baseline |
| Phase lifecycle and phase-entry gates | `core/protocol/PHASE_LIFECYCLE.md` | `PHASE-xx.md` template, `continue.md`, `SESSION_SCOPE.md` | delivery plan summaries |
| Session artifact responsibility and active-session surface | `core/protocol/SESSION_ARTIFACTS.md` | `ARTIFACT_MODEL.md`, session templates | accepted-state docs |
| Requirements/design source-authority location | `core/protocol/REQUIREMENTS.md` plus `ARTIFACT_MODEL.md` | delivery/session scope templates | root accepted-state artifacts by default |
| Evidence, validation, and claim reconciliation | `core/protocol/VALIDATION_AND_EVIDENCE.md` plus `CLAIM_RECONCILIATION.md` | `EVIDENCE.md`, IU reviews, close protocol | user-facing status prose alone |
| Runtime integration posture | `core/protocol/RUNTIME_INTEGRATION_AND_PRODUCTION_READINESS.md` | stack packages, evidence template | generic build/test evidence alone |
| Unresolved/gated/non-gating/technical-review items | `core/protocol/UNRESOLVED_ITEMS.md` | unresolved templates, checkpoints, close protocol | informal prose only |
| Project-type classification metadata | `core/protocol/PROJECT_TYPES.md` | routing evidence, templates | primary routing justification |

Ownership rule: one canonical owner per concern. When two documents appear to govern the same concern, update the canonical owner and make the secondary surface point to it. Do not copy full rules into multiple protocol files unless the duplicate text is a short pointer needed for command execution.
