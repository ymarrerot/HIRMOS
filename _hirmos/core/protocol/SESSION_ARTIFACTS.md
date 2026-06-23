# Session Artifacts Protocol

Status: core protocol.
Purpose: define active-session artifact templates, instantiation rules, ownership, archive behavior, reset behavior, and the strict-necessity session surface.


## PROD-L canonical naming decision

The canonical active-session authority artifact is `SESSION_SCOPE.md`. The canonical target requirements artifact name is `REQUIREMENTS.md`, replacing `REQUIREMENTS_BASELINE.md` only where separate requirements authority remains justified.

This file documents the PROD-L2 runtime surface for active sessions. Historical archives may retain older artifact names and must remain readable. New framework wording should prefer:

```text
SESSION_SCOPE.md       # active session authority
REQUIREMENTS.md        # conditional independent requirements authority
DELIVERY_SCOPE.md      # durable delivery/release authority
```

Migration rule: do not create default session-level `REQUIREMENTS.md` or `DESIGN.md` for normal implementation sessions. Use `SESSION_SCOPE.md` as the combined scoped authority unless separate requirements/design authority is justified by the work objective, delivery shape, audit need, or shared multi-session adoption need.

## Strict-necessity rule

HIRMOS must not create an active-session artifact merely because a template exists, a topic was discussed, or the model wants a place to think. A separate active-session artifact is justified only when it is strictly necessary for at least one of these reasons:

1. **Authority** — it owns scope, requirements, design, implementation-unit contract, unresolved-item status, or accepted-state update obligations.
2. **Machine state** — it records command/lifecycle state that must be machine-readable or fail-closed.
3. **Evidence** — it preserves validation, runtime, production-shaped engineering, or claim evidence that is material to implementation or close.
4. **Gating** — it controls whether implementation, continuation, close, or update-state may proceed.
5. **Continuity** — it is needed for safe continuation across chats/sessions.
6. **Audit/history** — it must be archived to explain what was accepted, rejected, carried forward, blocked, or explicitly limited.

If content is useful but not strictly necessary as a separate artifact, it must live inside the nearest major artifact rather than creating a support file. The default answer to "should this be a new artifact?" is **no** unless one of the strict-necessity reasons applies and the content cannot safely live inside an existing major artifact.

## Artifact classes

HIRMOS uses four artifact classes:

1. **Templates** in `_hirmos/core/templates/` are reusable shells.
2. **Active session artifacts** in `_hirmos/session/` are runtime authority/evidence for the active session.
3. **Accepted-state artifacts** in `_hirmos/system/accepted-state/` are durable accepted current truth.
4. **Archived session artifacts** in `_hirmos/system/history/sessions/<session-id>/` are durable history.

Templates are not evidence. Active session artifacts are evidence only when instantiated and populated with non-placeholder content. Archived artifacts preserve history; they do not remain active runtime authority.

## Canonical active-session surface

New governed sessions use the smallest sufficient active-session surface:

```text
_hirmos/session/
  SESSION_STATE.json              # always present scaffold; machine state
  SESSION_EXECUTION.md            # required for active governed sessions
  SESSION_SCOPE.md             # required before implementation authorization
  unresolved-items.md             # required for governed sessions
  REQUIREMENTS_BASELINE.md        # legacy-compatible conditional requirements authority; target name REQUIREMENTS.md in later PROD-L phases
  DESIGN.md                       # conditional design / current-state / readiness authority
  EVIDENCE.md                     # conditional nontrivial evidence / claim reconciliation
  implementation-units/           # conditional for nontrivial implementation
  bootstrap/                      # required session infrastructure; bootstrap report required for governed session startup
  stack-resolution.json           # conditional machine-readable stack resolution only
```

`stack-resolution.json` is a conditional root session artifact because it is machine-readable routing state. Continuation handoff lives in `SESSION_EXECUTION.md` Current Continuation Snapshot. Other support files are not part of the new default session model.

## Major artifact responsibilities

| Artifact | Required when | Owns |
|---|---|---|
| `SESSION_STATE.json` | installed scaffold / active sessions | machine-readable command state |
| `SESSION_EXECUTION.md` | any active governed session | Current Continuation Snapshot, command timeline, controls, route-backs, boundary log, close/archive/reset controls |
| `SESSION_SCOPE.md` | before implementation authorization and for scoped governed work | session scope, exclusions, acceptance criteria, production-shaped gate, delivery shape decision, close verification |
| `unresolved-items.md` | governed sessions | gated items, assumptions, risks, decisions, dispositions, revalidation |
| `REQUIREMENTS_BASELINE.md` | requirements materially govern scope during transition; target name `REQUIREMENTS.md` in later PROD-L phases | normalized requirements, source traceability, requirement coverage |
| `DESIGN.md` | substantial design/current-state/technical-review/readiness work is needed | current-state basis, source matrix, design, technical review, implementation readiness basis |
| `EVIDENCE.md` | nontrivial implementation or material claims/evidence exist | command evidence, runtime evidence, production-shaped evidence, claim reconciliation, close evidence handoff |
| `implementation-units/IU-xx.md` | nontrivial implementation unit exists | unit contract, evidence, review, retry history, result |
| `bootstrap/BOOTSTRAP_REPORT.md` | governed session startup / new chat bootstrap | bootstrap findings and initialization evidence |
| `stack-resolution.json` | stack selection materially affects routing/evidence | machine-readable stack resolution only |

## Consolidated responsibilities

The following former support-artifact responsibilities are now embedded in major artifacts:

| Former responsibility | New location |
|---|---|
| request intake / source-material summary | `SESSION_SCOPE.md` parent authority and `DESIGN.md` source matrix |
| prototype or external input ingestion | `DESIGN.md` source matrix and requirements/design sections |
| system-state understanding | `DESIGN.md` current-state basis and `SESSION_EXECUTION.md` current-state-first controls |
| technical review | `DESIGN.md` technical review section |
| implementation readiness | `DESIGN.md` readiness basis, `SESSION_SCOPE.md` engineering gate, `SESSION_EXECUTION.md` readiness controls |
| implementation evidence / local runtime evidence / role workflow smoke | `EVIDENCE.md` |
| runtime integration readiness | `DESIGN.md` for planned posture and `EVIDENCE.md` for verified posture |
| claim reconciliation | `EVIDENCE.md` claim reconciliation summary and `SESSION_SCOPE.md` close verification |
| session scope review | `SESSION_SCOPE.md` close verification |
| close checklist / system-state update / archive manifest | `SESSION_EXECUTION.md` close/archive/reset controls and accepted-state artifacts |

Do not recreate those former major artifact sections for new sessions unless a future protocol explicitly reintroduces them.

## Authority rule

- `SESSION_SCOPE.md` owns active session scope, acceptance, coverage, production-shaped engineering gate, delivery shape decision, and close verification.
- `unresolved-items.md` owns unresolved-item details.
- `DESIGN.md` owns design authority, current-state basis, technical review, and implementation-readiness rationale when those are material.
- `EVIDENCE.md` owns material evidence and claim reconciliation for implementation/close claims.
- `SESSION_EXECUTION.md` owns command/lifecycle execution control and archive/reset controls only.
- `SESSION_STATE.json` owns machine-readable command state.
- `CURRENT_SYSTEM_STATE.md` owns durable current system truth.

Artifacts may summarize or link to other authorities, but must not duplicate or override them. If a later stage discovers a problem in an earlier authority, it must route back to the owning artifact/stage rather than silently rewriting it.

## Fresh installed state

A fresh installed framework may contain only minimal active-session scaffolding:

```text
_hirmos/session/.gitkeep
_hirmos/session/SESSION_STATE.json
_hirmos/session/bootstrap/.gitkeep
_hirmos/session/SESSION_EXECUTION.md#current-continuation-snapshot.gitkeep
_hirmos/session/implementation-units/.gitkeep

```

A fresh framework must not ship with pre-populated runtime artifacts such as `SESSION_SCOPE.md`, `SESSION_EXECUTION.md`, `DESIGN.md`, `EVIDENCE.md`, `unresolved-items.md`, or implementation evidence. Those files are created only when a governed session needs them.

## Governed session activation

A governed session is active only when `_hirmos/session/SESSION_EXECUTION.md` exists and records session identity, active command, User Request, interaction mode, lifecycle stage, continuation state, required execution controls, and references to required major artifacts.

`hirmos start` must instantiate `_hirmos/session/SESSION_EXECUTION.md` before lifecycle work begins.

## Mandatory governed-session artifacts

A governed software session must create or update `_hirmos/session/bootstrap/BOOTSTRAP_REPORT.md` during bootstrap/startup and must keep `SESSION_EXECUTION.md` Current Continuation Snapshot current for continuation state.

A governed software session must instantiate these before claiming Implementation Readiness:

```text
_hirmos/session/SESSION_SCOPE.md
_hirmos/session/unresolved-items.md
```

`DESIGN.md` is required when current-state understanding, design decisions, technical review, stack decisions, production-shaped engineering posture, or implementation-readiness rationale are material. `EVIDENCE.md` is required when implementation evidence or close claims are nontrivial.

## Snapshot-backed checkpoint rule

Governed Current Continuation Snapshots use `_hirmos/core/templates/session/SESSION_EXECUTION.md#current-continuation-snapshot` and must be instantiated as `_hirmos/session/SESSION_EXECUTION.md#current-continuation-snapshot` when a checkpoint asks for decisions, claims readiness/completion, fails closed, pauses, or changes continuation state.

HIRMOS must not tell the user that an artifact exists, is ready, can be inspected, or authorizes continuation unless the artifact exists in `_hirmos/session/` and contains non-placeholder content.

## Instantiation principle

`hirmos start` and `hirmos continue` instantiate only the artifacts required by the active request path, lifecycle boundary, execution controls, delivery shape, project state, and interaction mode.

Every artifact instantiation must be recorded in `_hirmos/session/SESSION_EXECUTION.md` under `Artifact Instantiation Log` with target artifact, source template, lifecycle stage, reason required, and non-placeholder check status.

## Baseline by lifecycle responsibility

### Bootstrap

Must create or update `_hirmos/session/bootstrap/BOOTSTRAP_REPORT.md` for governed session startup and new-chat continuation. Bootstrap report creation does not by itself create an active governed session.

### User Request / source intake

Do not create separate intake support files by default. Record source coverage in `SESSION_SCOPE.md` and source interpretation in `DESIGN.md` or `REQUIREMENTS_BASELINE.md` when material.

### Understand System State

Record current-state-first completion in `SESSION_EXECUTION.md`. Put material current-state findings in `DESIGN.md` when they affect Design or Implementation. Unknowns, contradictions, assumptions, risks, blockers, or user-owned decisions must be captured in `unresolved-items.md`.

### Design / Contracting

Create only when Design responsibilities are active:

- `_hirmos/session/DESIGN.md` when substantial design, current-state basis, technical review, or implementation-readiness rationale is needed;
- `_hirmos/session/SESSION_SCOPE.md` before Implementation can be authorized;
- `_hirmos/session/REQUIREMENTS_BASELINE.md` when requirements materially govern scope;
- `_hirmos/session/stack-resolution.json` when stack routing needs machine-readable state.

Durable delivery planning artifacts for multi-session work are system artifacts:

```text
_hirmos/system/delivery/<delivery-id>/DELIVERY_PLAN.md
_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md
```

### Implementation

Create only when Implementation responsibilities are active:

- `_hirmos/session/implementation-units/IU-xx.md` for nontrivial implementation units;
- `_hirmos/session/EVIDENCE.md` for material command, runtime, production-shaped engineering, claim-reconciliation, or close evidence.

Implementation artifacts consume `SESSION_SCOPE.md` and `DESIGN.md`. They must not silently rewrite `SESSION_SCOPE.md`, durable delivery contracts, or accepted current system state.

### Update System State / Close

Do not create separate close-checklist, system-state-update, archive-manifest, claim-reconciliation, or session-scope-review support files for new sessions. Close uses:

- `SESSION_SCOPE.md` close verification;
- `SESSION_EXECUTION.md` close/archive/reset controls;
- `EVIDENCE.md` when material evidence/claim reconciliation exists;
- accepted-state artifacts under `_hirmos/system/accepted-state/`;
- archive copy under `_hirmos/system/history/sessions/<session-id>/`.

## Delivery governance artifacts

HIRMOS uses the smallest sufficient governed delivery shape for greenfield, brownfield, and mixed work.

Durable delivery authority lives under:

```text
_hirmos/system/delivery/<delivery-id>/DELIVERY_PLAN.md
_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md
```

A durable Delivery Plan is required for `MULTI_SESSION_DELIVERY` and `MULTI_SESSION_DELIVERY_WITH_PHASE_FILES`. Separate phase files are required only for `MULTI_SESSION_DELIVERY_WITH_PHASE_FILES`.

Every implementation-capable session must record the Delivery Shape Decision in `DESIGN.md` when substantial design is active and in `SESSION_SCOPE.md` / `SESSION_EXECUTION.md` before implementation readiness.

## Session Scope and Implementation Unit rule

Every implementation session must have a governed `SESSION_SCOPE.md`. Every non-trivial implementation unit must use one self-contained `implementation-units/IU-xx.md` artifact that includes the unit contract, evidence, review, result, and retries when needed.

## Naming rules

Use stable names for root session-wide artifacts:

```text
SESSION_STATE.json
SESSION_SCOPE.md
SESSION_EXECUTION.md
unresolved-items.md
REQUIREMENTS_BASELINE.md
DESIGN.md
EVIDENCE.md
```

Use subfolders only for progressive disclosure where strict necessity applies:

```text
implementation-units/IU-xx.md
bootstrap/BOOTSTRAP_REPORT.md
stack-resolution.json
```

## Archive and reset

`hirmos close` archives the active session under:

```text
_hirmos/system/history/sessions/<session-id>/
```

The archive must preserve all active session artifacts that existed, unresolved-item dispositions, accepted/carry-forward decisions, and enough evidence for future sessions to understand what was accepted, rejected, carried, blocked, or explicitly limited.

After successful normal close, `_hirmos/session/` resets to clean idle state:

```text
_hirmos/session/.gitkeep
_hirmos/session/SESSION_STATE.json
_hirmos/session/bootstrap/.gitkeep
_hirmos/session/SESSION_EXECUTION.md#current-continuation-snapshot.gitkeep
_hirmos/session/implementation-units/.gitkeep

```

Any remaining active-session runtime artifact after close is stale and blocks normal close success unless the close is explicitly blocked or aborted.

Abort close must archive available state and blocked reasons, but must not present aborted work as accepted system state.

Delivery planning artifacts are durable system artifacts, not session-local major artifact sections.

Runtime integration readiness artifact responsibilities now live in DESIGN.md and EVIDENCE.md under the strict-necessity model.

## Close / archive integrity extension

The strict-necessity model preserves close/archive integrity through SESSION_SCOPE.md close verification, SESSION_EXECUTION.md close/archive/reset controls, EVIDENCE.md when material, and accepted-state artifacts.
Archive history is not accepted state by itself.

Claim reconciliation artifact responsibilities now live in EVIDENCE.md and SESSION_SCOPE.md close verification.
Claim reconciliation may list final files in EVIDENCE.md when needed.
