# Session Artifacts Protocol

Status: core protocol.
Purpose: define active-session artifact templates, instantiation rules, ownership, archive behavior, reset behavior, and the contract-centered session spine.

## Core distinction

HIRMOS uses four artifact classes:

1. **Templates** in `_hirmos/core/templates/` are reusable shells.
2. **Active session artifacts** in `_hirmos/session/` are runtime authority/evidence for the active session.
3. **Accepted-state artifacts** in `_hirmos/system/accepted-state/` are durable accepted current truth.
4. **Archived session artifacts** in `_hirmos/system/history/sessions/<session-id>/` are durable history.

Templates are not evidence. Active session artifacts are evidence only when instantiated and populated with non-placeholder content. Archived artifacts preserve history; they do not remain active runtime authority.

## Artifact class and filename convention

HIRMOS uses filename placement to make runtime importance visible:

- root session files are only main/governed orchestration surfaces;
- support files live under `support/` and should use lowercase kebab-case names;
- checkpoints live under `checkpoints/`;
- implementation units live under `implementation-units/`;
- bootstrap reports live under `bootstrap/`;
- durable delivery artifacts live under `_hirmos/system/delivery/<delivery-id>/`, not under the active session root.

Canonical active-session root files are:

```text
SESSION_STATE.json
SESSION_CONTRACT.md
SESSION_EXECUTION.md
unresolved-items.md
session-contract-review.md
REQUIREMENTS_BASELINE.md   # conditional, only when requirements materially govern scope
```

`REQUIREMENTS_BASELINE.md` remains a conditional root artifact because it is requirements authority, not a support appendix. Other evidence, review, setup, smoke, claim, and checkpoint details must not accumulate as uppercase files in the session root for new sessions.

## Contract-centered session spine

New governed sessions use this active-session spine:

```text
_hirmos/session/
  SESSION_STATE.json
  SESSION_CONTRACT.md
  SESSION_EXECUTION.md
  unresolved-items.md
  implementation-units/
  checkpoints/
  support/
```

The root contains only machine state, main session contract, execution spine, and the governed unresolved-item register. Supporting details live under subfolders for progressive disclosure.

### Spine artifact roles

| Artifact | Class | Role |
|---|---|---|
| `SESSION_STATE.json` | orchestration | machine-readable command/lifecycle state |
| `SESSION_CONTRACT.md` | Main Artifact | Session Contract scope, acceptance criteria, coverage, close verification |
| `SESSION_EXECUTION.md` | orchestration | linear execution-control spine, self-validation, fail-closed controls |
| `unresolved-items.md` | governed register | gated items, non-gating assumptions, dispositions, revalidation |
| `implementation-units/IU-xx.md` | Main Artifact | unit contract, evidence, review, retries |
| `checkpoints/CHECKPOINT-<boundary>.md` | checkpoint | user-facing lifecycle boundary receipt |
| `support/*.md` | support | appendices only; no independent scope authority |

## Authority rule

- `SESSION_CONTRACT.md` owns active-Session Contract scope and acceptance.
- `unresolved-items.md` owns unresolved-item details.
- `SESSION_EXECUTION.md` owns command/lifecycle execution control.
- `SESSION_STATE.json` owns machine-readable command state.
- `CURRENT_SYSTEM_STATE.md` owns durable current system truth.

Artifacts may summarize or link to other authorities, but must not duplicate or override them.

## Fresh installed state

A fresh installed framework may contain only minimal active-session scaffolding:

```text
_hirmos/session/.gitkeep
_hirmos/session/SESSION_STATE.json
_hirmos/session/bootstrap/.gitkeep
_hirmos/session/checkpoints/.gitkeep
_hirmos/session/implementation-units/.gitkeep
_hirmos/session/support/.gitkeep
```

A fresh framework must not ship with pre-populated runtime artifacts such as `SESSION_CONTRACT.md`, `SESSION_EXECUTION.md`, `DESIGN.md`, `unresolved-items.md`, `support/system-state.md`, or implementation evidence. Those files are created only when a governed session needs them.

## Command-state machine integration

`SESSION_STATE.json` must follow `_hirmos/core/protocol/COMMAND_STATE_MACHINE.md`. Active session artifacts must match the machine state. Idle sessions may contain only the allowed scaffold. Active sessions must contain the canonical root artifacts required by their lifecycle stage.

## Governed session activation

A governed session is active only when `_hirmos/session/SESSION_EXECUTION.md` exists and records:

- session identity;
- active command;
- User Request;
- interaction mode;
- active lifecycle boundary;
- continuation state;
- required execution controls;
- references to `SESSION_CONTRACT.md` and `unresolved-items.md` when the lifecycle boundary requires them.

`hirmos start` must instantiate `_hirmos/session/SESSION_EXECUTION.md` before lifecycle work begins.

## Mandatory governed-session artifacts

A governed software session must instantiate these artifacts before claiming Implementation Readiness:

```text
_hirmos/session/SESSION_CONTRACT.md
_hirmos/session/unresolved-items.md
```

`SESSION_CONTRACT.md` must include only a compact Unresolved Items Control summary and must point to `_hirmos/session/unresolved-items.md`. HIRMOS must read the unresolved register directly before every lifecycle boundary.

## Project context and stack artifacts

When project-type or stack controls are active, instantiate the relevant active-session artifacts:

- `support/project-context.md` records evidence-backed project-type and stack-context classification.
- `support/stack-resolution.json` records active stack selection, confidence, evidence, conflicts, and optional stack contexts.

These artifacts guide routing and evidence. They are not requirements, Design, Implementation, or accepted-state authority by themselves.

## Artifact-backed checkpoint rule

Governed checkpoint artifacts use `_hirmos/core/templates/session/checkpoints/CHECKPOINT.md` and should be instantiated as `_hirmos/session/checkpoints/CHECKPOINT_<checkpoint-id>.md` when a checkpoint asks for decisions, claims readiness/completion, fails closed, or changes continuation state.

HIRMOS must not tell the user that an artifact exists, is ready, can be inspected, or authorizes continuation unless the artifact exists in `_hirmos/session/` and contains non-placeholder content.

If an artifact is planned but not yet created, HIRMOS may say it is planned. It must not present the artifact as available or authoritative.

## Instantiation principle

`hirmos start` and `hirmos continue` instantiate only the artifacts required by the active request path, lifecycle boundary, execution controls, project type, and interaction mode.

Do not instantiate every template by default. Instantiating unused artifacts creates false authority and confuses weaker models.

Every artifact instantiation must be recorded in `_hirmos/session/SESSION_EXECUTION.md` under `Artifact Instantiation Log` with:

- target artifact;
- source template;
- lifecycle stage;
- reason required;
- non-placeholder check status.

## Baseline artifact set by lifecycle stage

### Bootstrap

Bootstrap may create:

- `_hirmos/session/bootstrap/BOOTSTRAP_REPORT.md`

Bootstrap report creation does not by itself create an active governed session. `SESSION_EXECUTION.md` is created by `hirmos start` when a governed session begins.

### User Request / request intake

Create when the User Request or source inputs need durable extraction:

- `_hirmos/session/support/request-intake.md`
- `_hirmos/session/support/source-materials.md`
- `_hirmos/session/support/prototype-ingestion.md` when prototype or POC inputs exist

These artifacts are inputs/evidence. They are not governed requirements or Design authority.

### Understand System State

Create when governed software work begins:

- `_hirmos/session/support/system-state.md`
- `_hirmos/session/unresolved-items.md` always for governed sessions
- `_hirmos/session/session-contract-review.md` always for governed sessions

`support/system-state.md` must include both general system-state understanding and User Request-focused system-state understanding. Unknowns, contradictions, assumptions, risks, blockers, or user-owned decisions must be captured in `unresolved-items.md`.

### Design / Contracting

Create only when Design responsibilities are active:

- `_hirmos/session/DESIGN.md` when substantial design is needed
- `_hirmos/session/SESSION_CONTRACT.md` before Implementation can be authorized
- `_hirmos/session/support/technical-review.md` when technical assumptions, risks, or reviewer-facing details exist
- `_hirmos/session/support/implementation-readiness.md` before claiming Ready for Implementation


Delivery planning artifacts for multi-session work are durable system artifacts, not session-local authority:

```text
_hirmos/system/delivery/<delivery-id>/DELIVERY_PLAN.md
_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md
```


### Implementation

Create only when Implementation responsibilities are active:

- `_hirmos/session/implementation-units/IU-xx.md`
- `_hirmos/session/support/implementation-evidence.md` when evidence is substantial
- `_hirmos/session/support/local-runtime-evidence.md` when runtime setup/integration validation matters
- `_hirmos/session/support/role-workflow-smoke.md` when user/operator workflow validation matters
- `_hirmos/session/support/claim-reconciliation.md` when completion claims are complex or risky
- `_hirmos/session/session-contract-review.md` for fast-access governed Session Contract Review

Implementation artifacts consume `SESSION_CONTRACT.md`. They must not silently rewrite `SESSION_CONTRACT.md`, `DESIGN.md`, durable delivery contracts, or accepted current system state.

### Governed checkpoints

Create when a user-facing checkpoint asks for decisions, claims readiness/completion, fails closed, or changes continuation state:

- `_hirmos/session/checkpoints/CHECKPOINT_<checkpoint-id>.md`

Checkpoint artifacts summarize what can be surfaced and must be backed by non-placeholder session artifacts and current execution controls.

### Update System State / Close

Create or update when Update System State responsibilities are active:

- `session-contract-review.md` promised-vs-verified review and fail-closed verdict
- `SESSION_CONTRACT.md` review control mirror
- `SESSION_EXECUTION.md` close/reset controls
- supporting close appendices only when needed

`support/system-state-update.md` and `support/close-checklist.md` must not be instantiated as active-session authority under the contract-centered session model. New-session close behavior uses `SESSION_CONTRACT.md` close verification and `SESSION_EXECUTION.md` close controls, with generated archive/checklist artifacts where tooling supports them.


## Delivery governance artifacts

For multi-session work in any project type, a Delivery Plan is needed and separate phase files are required.

Durable delivery authority lives under:

```text
_hirmos/system/delivery/<delivery-id>/DELIVERY_PLAN.md
_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md
```

`SESSION_CONTRACT.md` may be sourced from a durable `PHASE-xx.md`, but implementation authority still flows through the Session Contract and implementation units.

Session-local delivery artifacts are not canonical delivery authority and must not be newly produced as authoritative delivery plans, phase plans, delivery status files, phase contracts, or delivery unit contracts.

Every implementation-capable session must record Delivery-Need Classification in `SESSION_CONTRACT.md`, `SESSION_EXECUTION.md`, and `session-contract-review.md` before implementation readiness.


## Artifact ownership

| Lifecycle responsibility | Owns | May consume | Must not silently rewrite |
|---|---|---|---|
| User Request / intake | request/source/prototype evidence artifacts | raw inputs | governed requirements/design/session contract authority |
| Understand System State | `support/system-state.md`, state evidence, state confidence | request/source/prototype artifacts, current system state | Design or Implementation authority |
| Design / Contracting | `DESIGN.md`, `SESSION_CONTRACT.md`, implementation readiness, durable delivery/phase contracts when applicable | system state and unresolved items | active implementation evidence or accepted system state |
| Implementation | `implementation-units/IU-xx.md`, supporting evidence, retries | `SESSION_CONTRACT.md`, Design authority, unresolved items | system state or Design authority without route-back |
| Update System State | accepted-state update, close verification, archive record | reviewed session outcomes and evidence | Design or Implementation work |

Later stages may identify issues in earlier-stage authority. They must record a route-back in `SESSION_EXECUTION.md`, reset affected downstream controls, and return to the owning stage instead of silently editing upstream authority.

## Durable phase contract rule

A durable Phase Contract may source a `SESSION_CONTRACT.md`, but active-session implementation authority must flow through the Session Contract before implementation units begin. Durable delivery phase contracts should live under `_hirmos/system/delivery/<delivery-id>/phases/`.

## Session Contract and Implementation Unit rule

Every implementation session must have a governed `SESSION_CONTRACT.md`. Every non-trivial implementation unit must use one self-contained `implementation-units/IU-xx.md` artifact that includes the unit contract, evidence, review, result, and retries when needed.

## Session Contract Review rule

Every governed session must have `_hirmos/session/session-contract-review.md`. It is the governed fast-access review artifact for promised-vs-verified coverage, unresolved-item reconciliation, final review verdict, and fail-closed result. It must be completed before implementation-completion, close-readiness, or close success can be claimed.

The Session Contract may contain only a control pointer and final-verdict mirror for the review. Detailed review belongs in `session-contract-review.md`.

## Naming rules

Use stable names for root session-wide artifacts:

```text
SESSION_STATE.json
SESSION_CONTRACT.md
SESSION_EXECUTION.md
unresolved-items.md
session-contract-review.md
```

Use subfolders for progressive disclosure:

```text
implementation-units/IU-xx.md
checkpoints/CHECKPOINT_<checkpoint-id>.md
support/implementation-evidence.md
support/local-runtime-evidence.md
support/role-workflow-smoke.md
support/claim-reconciliation.md
```

active-session artifacts must follow the contract-centered model. Authoritative new-session artifacts are `SESSION_CONTRACT.md`, `unresolved-items.md`, `session-contract-review.md`, and self-contained `implementation-units/IU-xx.md`.

## Archive and reset

`hirmos close` archives the active session under:

```text
_hirmos/system/history/sessions/<session-id>/
```

The archive must preserve:

- `SESSION_EXECUTION.md`;
- `SESSION_CONTRACT.md`;
- `unresolved-items.md`;
- `session-contract-review.md`;
- implementation-units, checkpoints, and support subfolders when present;
- all active session artifacts;
- unresolved-item disposition and carry-forward records;
- enough evidence for future sessions to understand what was accepted, rejected, carried, or left unresolved.

After a successful normal close, `_hirmos/session/` resets to clean idle state:

```text
_hirmos/session/.gitkeep
_hirmos/session/SESSION_STATE.json
_hirmos/session/bootstrap/.gitkeep
_hirmos/session/checkpoints/.gitkeep
_hirmos/session/implementation-units/.gitkeep
_hirmos/session/support/.gitkeep
```

Any remaining active-session runtime artifact after close is stale and blocks normal close success unless the close is explicitly blocked or aborted.

Abort close must archive available state and blocked reasons, but must not present aborted work as accepted system state.

## Runtime integration readiness artifact

When an active request involves material runtime services such as database, auth, messaging, storage, payments, deployment, secrets, cron/jobs, or external providers, instantiate runtime integration readiness evidence as a support appendix or legacy artifact according to the active protocol. Runtime evidence must remain subordinate to `SESSION_CONTRACT.md` acceptance criteria and `SESSION_EXECUTION.md` execution controls.

## Close / archive integrity extension

The contract-centered session spine does not weaken close/archive integrity. Close must still preserve archive evidence, update accepted state through governed controls, normalize archived session status, and reset the active session to the idle scaffold.

Archive history is not accepted state by itself. Accepted current truth remains in `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md`.

## Claim reconciliation artifact

For new sessions, claim reconciliation detail should live under `_hirmos/session/support/claim-reconciliation.md` when needed. It remains a support appendix and must not override `SESSION_CONTRACT.md` or `SESSION_EXECUTION.md`.

Claim reconciliation may list final files when needed, but file claims must be evidence-backed and subordinate to the Session Contract Review.

## current-system-state-first artifact rule

`CURRENT_SYSTEM_STATE.md` must be read before meaningful Design or Implementation. `SESSION_EXECUTION.md` records the control result; `SESSION_CONTRACT.md` must be built from that current-state understanding when implementation is in scope.

evidence artifact names `support/local-runtime-evidence.md` and `support/role-workflow-smoke.md` must not be instantiated as new active-session support artifacts. New sessions use `support/local-runtime-evidence.md` and `support/role-workflow-smoke.md` when applicable.

## canonical artifact and role-smoke instantiation rule

When local runtime or role-workflow smoke evidence materially affects acceptance, instantiate the appropriate support appendix and reference it from `SESSION_CONTRACT.md` and `SESSION_EXECUTION.md`.

## close-time evidence materialization rule

Close must not claim local runtime or role-workflow smoke evidence unless that evidence is materialized in the session archive or explicitly marked NOT_RUN with rationale.

## Requirements baseline artifact rule

When requirements materially affect scope, establish a requirements baseline before `SESSION_CONTRACT.md` claims coverage. The Session Contract must answer whether it covers the applicable requirements artifact.

`REQUIREMENTS_BASELINE.md` remains the legacy/canonical requirements-control artifact until a later accepted-state simplification phase renames or consolidates it.
