# Session Artifacts Protocol

Status: core protocol.
Purpose: define active-session artifact templates, instantiation rules, ownership, archive behavior, reset behavior, and the strict-necessity session surface.


## PROD-L canonical naming decision

The canonical active-session authority artifact is `SESSION_SCOPE.md`. The canonical target requirements artifact name is `REQUIREMENTS.md`, replacing `REQUIREMENTS.md` only where separate requirements authority remains justified.

This file documents the canonical runtime surface for active sessions. Framework wording uses:

```text
SESSION_SCOPE.md       # active session authority
REQUIREMENTS.md        # conditional independent requirements authority
DELIVERY_SCOPE.md      # durable delivery/release authority
```

Rule: do not create default session-level `REQUIREMENTS.md` or `DESIGN.md` for normal implementation sessions. Use `SESSION_SCOPE.md` as the combined scoped authority unless separate requirements/design authority is justified by the work objective, delivery shape, audit need, or shared multi-session adoption need.

## Strict-necessity rule

HIRMOS must not create an active-session artifact merely because a template exists, a topic was discussed, or the model wants a place to think. A separate active-session artifact is justified only when it is strictly necessary for at least one of these reasons:

1. **Authority** — it owns scope, requirements, design, implementation-unit authority record, unresolved-item status, or accepted-state update obligations.
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
  SESSION_SCOPE.md             # required only when a bounded session/phase scope exists
  unresolved-items.md             # conditional; required when session-level unresolved items exist or must be verified
  REQUIREMENTS.md        # conditional independent requirements authority
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
| `SESSION_EXECUTION.md` | any active governed session | Current Continuation Snapshot, command timeline, controls, route-backs, boundary log, close/archive/reset control pointers |
| `SESSION_SCOPE.md` | before implementation authorization and for scoped governed work | session scope, exclusions, acceptance criteria, production-shaped gate, delivery shape decision, close verification |
| `unresolved-items.md` | session-level unresolved items exist or must be explicitly verified | gated items, assumptions, risks, decisions, dispositions, revalidation for the active session only |
| `REQUIREMENTS.md` | requirements materially govern scope; target name `REQUIREMENTS.md` | normalized requirements, source traceability, requirement coverage |
| `DESIGN.md` | substantial design/current-state/technical-review/readiness work is needed | current-state basis, source matrix, design, technical review, implementation readiness basis |
| `EVIDENCE.md` | nontrivial implementation or material claims/evidence exist | command evidence, runtime evidence, production-shaped evidence, claim reconciliation, close evidence handoff |
| `implementation-units/IU-xx.md` | nontrivial implementation unit exists | sealed unit contract authority plus append-only execution, review, retry, handoff records |
| `bootstrap/BOOTSTRAP_REPORT.md` | governed session startup / new chat/context bootstrap | bootstrap findings, complete compact discipline answers, durable recovery sources, and initialization evidence |
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
| close checklist / system-state update / archive manifest | `SESSION_EXECUTION.md` close/archive/reset control pointers and accepted-state artifacts |

Do not recreate those former major artifact sections for new sessions unless a future protocol explicitly reintroduces them.

## Authority rule

- `SESSION_SCOPE.md` owns active session scope, acceptance, coverage, production-shaped engineering gate, delivery shape decision, and close verification.
- `unresolved-items.md` owns unresolved-item details.
- `DESIGN.md` owns design authority, current-state basis, technical review, and implementation-readiness rationale when those are material.
- `EVIDENCE.md` owns material evidence and claim reconciliation for implementation/close claims.
- `SESSION_EXECUTION.md` owns command/lifecycle execution control and archive/reset control pointers only.
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

A governed session is active only when `_hirmos/session/SESSION_EXECUTION.md` exists and records session identity, active command, User Request, canonical interaction posture acknowledgement, lifecycle stage, continuation state, required execution controls, and references to required major artifacts.

`hirmos start` must instantiate `_hirmos/session/SESSION_EXECUTION.md` before lifecycle work begins.

## Mandatory governed-session artifacts

A governed software session must create or update `_hirmos/session/bootstrap/BOOTSTRAP_REPORT.md` during bootstrap/startup and must keep `SESSION_EXECUTION.md` Current Continuation Snapshot current for continuation state. The bootstrap report must include every bootstrap quiz answer with a durable source and recovery method; chat memory, compressed chat summaries, and prior model recollection are not valid bootstrap recovery sources.

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

`hirmos start` and `hirmos continue` instantiate only the artifacts required by the active request path, lifecycle boundary, execution controls, delivery shape, project state, and canonical interaction posture.

Every artifact instantiation must be recorded in `_hirmos/session/SESSION_EXECUTION.md` under `Artifact Instantiation Log` with target artifact, source template, lifecycle stage, reason required, and non-placeholder check status.

## Baseline by lifecycle responsibility

### Bootstrap

Must create or update `_hirmos/session/bootstrap/BOOTSTRAP_REPORT.md` for governed session startup and new-chat/context continuation. Bootstrap report creation does not by itself create an active governed session. Every bootstrap report must include the complete compact discipline answer set recovered from active artifacts, archived bootstrap reports, or core authority/protocol files.

### User Request / source intake

Do not create separate intake support files by default. Record source coverage in `SESSION_SCOPE.md` and source interpretation in `DESIGN.md` or `REQUIREMENTS.md` when material.

### Understand System State

Record current-state-first completion in `SESSION_EXECUTION.md`. Put material current-state findings in `DESIGN.md` when they affect Design or Implementation. Unknowns, contradictions, assumptions, risks, blockers, or user-owned decisions must be captured in `unresolved-items.md`.

### Design / Scope Authority

Create only when Design responsibilities are active:

- `_hirmos/session/DESIGN.md` when substantial design, current-state basis, technical review, or implementation-readiness rationale is needed;
- `_hirmos/session/SESSION_SCOPE.md` before Implementation can be authorized;
- `_hirmos/session/REQUIREMENTS.md` when requirements materially govern scope;
- `_hirmos/session/stack-resolution.json` when stack routing needs machine-readable state.

Durable delivery planning artifacts for multi-session work are system artifacts:

```text
_hirmos/system/delivery/DELIVERY_PLAN.md and _hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md
_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md
```

### Implementation

Create only when Implementation responsibilities are active:

- `_hirmos/session/implementation-units/IU-xx.md` for nontrivial implementation units;
- `_hirmos/session/EVIDENCE.md` for material command, runtime, production-shaped engineering, claim-reconciliation, or close evidence.

Implementation artifacts consume `SESSION_SCOPE.md` and `DESIGN.md`. They must not silently rewrite `SESSION_SCOPE.md`, durable delivery scopes, or accepted current system state.

### Update System State / Close

Do not create separate close-checklist, system-state-update, archive-manifest, claim-reconciliation, or session-scope-review support files for new sessions. Close uses:

- `SESSION_SCOPE.md` close verification;
- `SESSION_EXECUTION.md` close/archive/reset control pointers;
- `EVIDENCE.md` when material evidence/claim reconciliation exists;
- accepted-state artifacts under `_hirmos/system/accepted-state/`;
- archive copy under `_hirmos/system/history/sessions/<session-id>/`.

## Delivery governance artifacts

HIRMOS uses the smallest sufficient governed delivery shape for greenfield, brownfield, mixed, and new-product work. Delivery shape is chosen for the real software work, not for framework testing, inspection, dogfood context, or project-type labels.

Durable delivery authority lives under:

```text
_hirmos/system/delivery/DELIVERY_PLAN.md and _hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md
_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md
```

A durable Delivery Plan is required for `MULTI_SESSION_DELIVERY` and `MULTI_SESSION_DELIVERY_WITH_PHASE_FILES`. Separate phase files are required only for `MULTI_SESSION_DELIVERY_WITH_PHASE_FILES`.

Every implementation-capable session must record the Delivery Shape Decision in `DESIGN.md` when substantial design is active and in `SESSION_SCOPE.md` / `SESSION_EXECUTION.md` before implementation readiness.

## Session Scope and Implementation Unit rule

Every implementation session must have a governed `SESSION_SCOPE.md`. Every non-trivial implementation unit must use one self-contained `implementation-units/IU-xx.md` artifact with separated mutation zones: sealed contract authority, append-only execution record, append-only review record, append-only retry records, and append-only handoff evidence. The contract authority sections must not be edited after seal/material implementation starts unless route-back explicitly reopens or supersedes the contract.

## Naming rules

Use stable names for root session-wide artifacts:

```text
SESSION_STATE.json
SESSION_SCOPE.md
SESSION_EXECUTION.md
unresolved-items.md
REQUIREMENTS.md
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

The strict-necessity model preserves close/archive integrity through SESSION_SCOPE.md close verification, SESSION_EXECUTION.md close/archive/reset control pointers, EVIDENCE.md when material, and accepted-state artifacts.
Archive history is not accepted state by itself.

Claim reconciliation artifact responsibilities now live in EVIDENCE.md and SESSION_SCOPE.md close verification.
Claim reconciliation may list final files in EVIDENCE.md when needed.


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


## Runtime timestamp context

`_hirmos/session/SESSION_STATE.json` → `run_context` records the reliable machine-readable runtime timestamp source for the session. Timestamped session artifacts must derive session dates/timestamps from this state field rather than model memory. `BOOTSTRAP_REPORT.md` records human-readable timestamp capture evidence; it is not the canonical timestamp source.


## Pre-implementation baseline boundary

Before the session scope baseline has been accepted or amended, implementation-unit artifacts must not be created. HIRMOS may record only a compact implementation-shape preview in `SESSION_SCOPE.md` when needed for review. Full implementation-unit artifacts belong only in `_hirmos/session/implementation-units/` after baseline acceptance/amendment.


## Complete active session authority

`SESSION_SCOPE.md` is the complete active session authority and close-verification root. Optional `REQUIREMENTS.md` and `DESIGN.md` may provide detailed sub-authority only for IDs or sections explicitly adopted by `SESSION_SCOPE.md`; they must not create independent session obligations.


## Runtime session focus and active authority

HIRMOS always has a runtime session envelope while commands are active. The active authority depends on `SESSION_STATE.json.session_focus`:

| session_focus | Active authority | SESSION_SCOPE.md required? | unresolved-items.md target |
|---|---|---:|---|
| `minimal_session` | `SESSION_SCOPE.md` when a bounded artifact/output scope is needed | conditional | session-level only if material items exist |
| `session_baseline` | `SESSION_SCOPE.md` | YES | `_hirmos/session/unresolved-items.md` when material items exist |
| `delivery_baseline` | `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md` | NO | `_hirmos/system/delivery/<delivery-id>/unresolved-items.md` |
| `phase_session_baseline` | `PHASE-xx.md` plus `SESSION_SCOPE.md` | YES | `_hirmos/session/unresolved-items.md` for phase/session-specific or inherited items |
| `implementation` | `SESSION_SCOPE.md` plus implementation units when needed | YES | `_hirmos/session/unresolved-items.md` when material items exist |

A delivery-baseline runtime session must not create `_hirmos/session/SESSION_SCOPE.md` merely to have a session artifact. The active scope authority is the delivery scope until the first phase/session is instantiated.

## PROD-L8.11 Delivery-Baseline Optional Authority Location

When `SESSION_STATE.json.session_focus = delivery_baseline`, the active authority is delivery-level. Optional requirements/design authority must be located under `_hirmos/system/delivery/<delivery-id>/` only:

- `_hirmos/system/delivery/<delivery-id>/REQUIREMENTS.md` when separate delivery-level requirements authority is justified.
- `_hirmos/system/delivery/<delivery-id>/DESIGN.md` when separate delivery-level design authority is justified.

During `delivery_baseline`, HIRMOS must not create, update, list, or depend on `_hirmos/session/REQUIREMENTS.md` or `_hirmos/session/DESIGN.md`. If separate optional authority is not justified, requirements and design decisions remain inside `DELIVERY_SCOPE.md` only. Session-level optional authority artifacts become applicable only after the flow advances to a bounded `phase_session_baseline` or `session_baseline` focus.

## PROD-L8.27 Archive Immutability Artifact Rule

Active session artifacts are working authorities until the pre-archive validation gate completes. Once copied to `_hirmos/system/history/sessions/<session-id>/`, the archive is historical evidence.

- Active IU/SESSION/EVIDENCE artifacts may be corrected before archive when validation finds `ACTIVE_FIXABLE` defects.
- Archived artifacts may receive only archive transaction repairs (`ARCHIVE_TRANSACTION_REPAIRABLE`) such as manifest/path/reset-machine-state corrections.
- Archived historical governance/evidence defects (`ARCHIVE_HISTORICAL_IMMUTABLE`) must be recorded as limitations, governance deviations, supersession notes, or carry-forward items; they must not be rewritten in place.

## PROD-L8.28 Generated IU Instantiation and Active Close Concordance

Generated implementation-unit artifacts must be validated while the session is active and before archive. A generated IU is close-eligible only when its sealed contract sections were fully instantiated before execution and its append-only Execution Record and Unit Review contain concrete evidence-backed completion/review results.

Active close must fail closed, downgrade to partial, or route back when IU status contradicts session/phase/delivery close claims. In particular, implementation-complete, phase-accepted, delivery-accepted, or delivery-closed claims are invalid when any applicable IU remains `Execution status: NOT_STARTED`, `Review status: PENDING`, lacks Unit Result, lacks validation/evidence comparison, or lacks a required Test / Fixture / Validator Change Rationale. Historical archives must not be expanded to repair these defects after snapshot; apply PROD-L8.27 archive immutability instead.
