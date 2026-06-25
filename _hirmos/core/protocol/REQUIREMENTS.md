# Requirements and Coverage Mapping

Status: core protocol.

## Purpose

`REQUIREMENTS.md` is a conditional normalized requirements-control artifact for a governed HIRMOS delivery or session.

It bridges raw user inputs and Design when requirements are material enough to need their own source authority. It prevents requirement loss when a project has multiple source inputs such as uploaded requirements, notes, prototype material, UI design notes, research notes, prior accepted state, and conversation context.

It is intentionally compact and operational. It is not a heavyweight software requirements specification, and it is not a default root accepted-state artifact.

## Separation of authority

| Surface | Responsibility |
|---|---|
| Raw source inputs | Original user-provided material. Examples: `_hirmos/inputs/uploads/requirements.txt`, prototype files, UI notes, reference material, conversation context. |
| `DELIVERY_SCOPE.md` / `SESSION_SCOPE.md` | Primary scope authority for delivery/session work; may contain requirements when separate requirements authority is not justified. |
| Optional delivery `REQUIREMENTS.md` | Normalized requirement catalog for one delivery when delivery requirements are too complex for `DELIVERY_SCOPE.md`. |
| Optional session `REQUIREMENTS.md` | Normalized requirement catalog for one session when session requirements are too complex for `SESSION_SCOPE.md`. |
| `DESIGN.md` / `DELIVERY_PLAN.md` | Design decisions and delivery decomposition based on accepted scoped requirements. |
| `EVIDENCE.md` / implementation-unit evidence | Evidence for claims that requirements were implemented, verified, blocked, or deferred. |
| `CURRENT_SYSTEM_STATE.md` | Accepted-state navigation authority, Work History Ledger, Source Artifact Index, and concise accepted-state summary. It points to requirement sources but does not replace them. |

Firm rule: raw requirement notes are not governed requirements until normalized into the active delivery/session authority or explicitly classified as out of scope, gated, blocked, duplicate, superseded, or not applicable.

## Required artifact locations

Delivery-level requirements authority, when justified:

```text
_hirmos/system/delivery/<delivery-id>/REQUIREMENTS.md
```

Session-level requirements authority, when justified:

```text
_hirmos/session/REQUIREMENTS.md
```

Default HIRMOS must not create:

```text
_hirmos/system/accepted-state/REQUIREMENTS.md
```

A root accepted-state requirements baseline is allowed only under explicit cumulative accepted requirements governance, with metadata such as `Cumulative accepted requirements governance: ACTIVE` and with close-time add/amend/remove/supersede/deprecate controls.

## Input normalization model

HIRMOS must support multiple requirement sources. Each source item must be classified before Design relies on it.

Canonical source classifications:

```text
RAW_REQUIREMENT_NOTE
PROTOTYPE_DERIVED_SIGNAL
UI_UX_DESIGN_NOTE
REFERENCE_MATERIAL
CONVERSATION_CONTEXT
ACCEPTED_STATE_SOURCE_POINTER
RESEARCH_BACKED_DEFAULT
MIXED_SOURCE
BLOCKED_UNREADABLE
NOT_APPLICABLE
```

Canonical requirement classes:

```text
FUNCTIONAL
WORKFLOW_STATE
DATA_DOMAIN
UI_UX
INTEGRATION
SECURITY_PRIVACY
AUDIT_EVIDENCE
RUNTIME_OPERATIONS
NON_FUNCTIONAL
ACCEPTANCE_CRITERION
NON_GOAL
CONSTRAINT
```

Canonical scope statuses:

```text
IN_SCOPE
OUT_OF_SCOPE
NON_GOAL
GATED
ASSUMPTION_BASED
DEFERRED
BLOCKED
DUPLICATE
SUPERSEDED
NOT_APPLICABLE
```

Canonical coverage statuses:

```text
NOT_STARTED
PLANNED
IN_PROGRESS
IMPLEMENTED
PARTIAL
VERIFIED
DEFERRED
BLOCKED
NOT_APPLICABLE
REJECTED
```

Coverage status is a requirement-coverage status, not evidence status. Evidence status must use canonical claim/evidence states from `EVIDENCE.md` claim reconciliation.

## Requirements required sections

A delivery/session `REQUIREMENTS.md` must include:

1. Requirements Identity
2. Source Inputs and Classification
3. Product Goal
4. Scope Boundary
5. Requirement Catalog
6. Non-Goals and Exclusions
7. Gated / Unresolved Requirements
8. Requirement-to-Delivery/Session Mapping
9. Coverage Status
10. Source Traceability
11. Change / Supersession Log
12. Requirements Self-Check

## Requirement ID rules

Each material requirement must have a stable ID within its authority level.

Recommended prefixes:

```text
REQ-FUNC-###
REQ-WFLOW-###
REQ-DATA-###
REQ-UI-###
REQ-INT-###
REQ-SEC-###
REQ-AUDIT-###
REQ-NFR-###
REQ-ACCEPT-###
REQ-NONGOAL-###
```

IDs must be stable once accepted inside the delivery/session authority. If a requirement changes materially, mark the old requirement `SUPERSEDED` and create or reference the replacement ID.

## Source traceability rule

Every material requirement must include at least one source reference or an explicit rationale for why no source reference exists.

Acceptable source references include:

- uploaded file path and section heading;
- prototype ingestion artifact section;
- source materials artifact section;
- delivery scope section;
- session scope section;
- archived source artifact path;
- Work History Ledger / Source Artifact Index pointer in `CURRENT_SYSTEM_STATE.md`;
- user-approved decision/Current Continuation Snapshot.

Do not silently promote prototype behavior, UI design notes, research-backed defaults, or model assumptions into confirmed requirements.

## Design gating rule

Before Design produces a delivery/session plan for governed software work, every material source-derived requirement must be one of:

- represented in the active delivery/session scope authority;
- represented in optional delivery/session `REQUIREMENTS.md` with an ID;
- classified as a non-goal or out of scope;
- recorded as gated/unresolved;
- recorded as blocked/unreadable;
- recorded as duplicate/superseded/not applicable.

Design must not rely only on raw `requirements.txt`, prototype notes, UI notes, or chat memory when requirements are applicable.

## Delivery/session mapping rule

Before implementation authorization, each `IN_SCOPE`, `ASSUMPTION_BASED`, or `DEFERRED` requirement that affects delivery/session work must be mapped to one or more phases, session scope items, implementation units, or explicit carry-forward records.

A Delivery Plan or Session Scope may intentionally defer a requirement, but the deferral must be visible in the active authority or unresolved/carry-forward path.

## Close/update-state rule

During `hirmos close`, HIRMOS must update requirement coverage for the active delivery/session authority when requirements were material to the session.

Close must not merge durable changes into `_hirmos/system/accepted-state/REQUIREMENTS.md` by default. Instead, close must update `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md` Work History Ledger and Source Artifact Index with the relevant delivery/session/archive requirement source paths and accepted result.

Close may not claim complete requirements coverage while any material requirement remains `NOT_STARTED`, `PARTIAL`, `BLOCKED`, or `DEFERRED` unless that status is explicitly accepted as carry-forward, deferred, blocked, out of scope, or not applicable.

## Current-state relationship

`CURRENT_SYSTEM_STATE.md` points to accepted requirement sources and may summarize coverage posture, but it must not replace the requirement source authority.

`REQUIREMENTS.md` answers at the delivery/session level: what must be satisfied and where is it mapped?

`CURRENT_SYSTEM_STATE.md` answers: what is the current accepted navigation context, what governed work exists chronologically, and where are the source authorities?

## On-demand synthesis

A complete current requirements artifact may be generated on demand from `CURRENT_SYSTEM_STATE.md`, delivery/session/archive requirement sources, delivery/session scopes, and close records. That generated synthesis is not source authority unless explicitly adopted by a governed future workflow.


## PROD-L8.18 Source Authority Location Matrix

HIRMOS uses source-authority location to prevent requirements/design/scope duplication. The matrix below is the default authority map.

| Concern | Default authority | Conditional detailed authority | Must not be default | Close/update behavior |
|---|---|---|---|---|
| Accepted current navigation | `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md` | none by default | root accepted-state `REQUIREMENTS.md`, `DESIGN.md`, `SYSTEM_SCOPE.md` | update pointers, Work History Ledger, Source Artifact Index, and material summary only |
| Delivery scope | `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md` | delivery `REQUIREMENTS.md` / `DESIGN.md` only when justified | session requirements/design during `delivery_baseline` | keep delivery authority current; close records source pointers |
| Phase scope | `_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md` plus adopted `SESSION_SCOPE.md` | none unless explicitly justified by delivery/session authority | future phase files before acceptance | phase status/freshness updated during governed transitions |
| Session scope | `_hirmos/session/SESSION_SCOPE.md` | session `REQUIREMENTS.md` / `DESIGN.md` only when justified | root accepted-state requirements/design | archive source authority at close; record pointer in `CURRENT_SYSTEM_STATE.md` |
| Requirements | active delivery/session scope by default | delivery/session `REQUIREMENTS.md` when normalized catalog is necessary | default accepted-state `REQUIREMENTS.md` | update coverage in source authority; do not merge into root accepted state by default |
| Design | active delivery/session scope by default | delivery/session `DESIGN.md` when independent design authority is necessary | default accepted-state `DESIGN.md` | update source authority and evidence; record pointer rather than duplicating design |
| Unresolved items | delivery or session unresolved register according to focus | carry-forward only for accepted deferrals/blocked items | unresolved details hidden only in narrative text | resolved/deferred/blocked status must reconcile before close success |
| Evidence | session `EVIDENCE.md` and IU evidence | stack-specific evidence commands when needed | accepted-state evidence summaries as source authority | current evidence truth must be reconciled before completion/close claims |

Selection rule: use the narrowest authority that can safely own the concern. Escalate to a separate `REQUIREMENTS.md` or `DESIGN.md` only when the active scope artifact would become ambiguous, oversized, or unable to provide traceable coverage.

On-demand synthesis is allowed, but a generated requirements/design/system-scope synthesis is not source authority unless a future governed workflow explicitly adopts it.
