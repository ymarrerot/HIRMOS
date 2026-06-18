# System State

Status: active-session Understand System State artifact.
Lifecycle owner: Understand System State.
Primary capability: `system-state-agent/understand-system-state`.
Purpose: establish current system state, evidence confidence, general understanding, and User Request-focused understanding before Design or Implementation authority is claimed.

Understand System State is mandatory for governed software work. It may be lightweight only when the request is low risk and existing evidence is sufficient.

## Scope of Understanding

- User Request:
- Project type candidate:
- Active stack candidate:
- Source inputs used:
- Prototype / POC inputs used:
- Accepted-state records used:
- CURRENT_SYSTEM_STATE.md read status: READ | MISSING | NOT_APPLICABLE | BLOCKED
- CURRENT_SYSTEM_STATE.md path:
- CURRENT_SYSTEM_STATE.md read first before Design: yes / no / not applicable with rationale
- Supporting accepted-state artifacts read:
- Session archives consulted: yes / no
- Archive use limited to history/evidence: yes / no / not applicable

## Working-Copy Root and Evidence Boundary

- Working-copy root:
- Evidence inspected:
- Evidence not inspected and why:
- Confidence limit:


## Accepted Current-State Source Check

This section is required before Design or Implementation authority is claimed.

| Accepted-state source | Exists? | Read? | Role | Findings / notes |
|---|---:|---:|---|---|
| `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md` | yes / no | yes / no | primary accepted current-state source | |
| `_hirmos/system/accepted-state/CARRY_FORWARD.md` | yes / no | yes / no | unresolved/carry-forward support | |
| `_hirmos/system/accepted-state/DECISION_LOG.md` | yes / no | yes / no | decision support | |
| `_hirmos/system/history/sessions/` | yes / no | yes / no | history/evidence only | |

Required decision:

- Current-system-state-first control status: SATISFIED | BLOCKED | NOT_APPLICABLE
- If `CURRENT_SYSTEM_STATE.md` exists but was not read first, explain why this is not a valid completion state and set terminal state `BLOCKED`.
- If `CURRENT_SYSTEM_STATE.md` is missing, record whether this is an empty/new installation or an integrity issue.
- Contradictions between accepted-state artifacts:
- Contradictions between accepted-state artifacts and repository evidence:
- Impact on Design authority:

## Active Delivery Pointer Discovery

This section is required before Delivery-Need Classification, Design, or Implementation readiness. Read it from `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md` when that file exists.

| Pointer | Value from Current System State | Verified artifact exists? | Notes |
|---|---|---:|---|
| Delivery governance active | YES / NO / UNCERTAIN / NOT_APPLICABLE | n/a | |
| Active delivery ID | none / `<delivery-id>` | n/a | |
| Delivery plan | none / `_hirmos/system/delivery/<delivery-id>/DELIVERY_PLAN.md` | yes / no / not_applicable | |
| Active phase | none / `_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md` | yes / no / not_applicable | |
| Active phase status | NOT_STARTED / ACTIVE / BLOCKED / ACCEPTED / SUPERSEDED / NOT_APPLICABLE | n/a | |
| Last accepted phase/session | none / value | n/a | |
| Next recommended phase | none / value | yes / no / not_applicable | |
| Next governed command | command / none | n/a | |

Required decision:

- Active delivery pointer status: SATISFIED | BLOCKED | NOT_APPLICABLE
- If active delivery pointers exist but the referenced Delivery Plan or Phase file is missing, set this status to `BLOCKED`.
- If a new request appears small but Current System State points to an active or blocked delivery, Delivery-Need Classification must consider that active delivery before allowing a single-session path.
- Impact on Delivery-Need Classification:

## General System State Understanding

Describe the system broadly enough to avoid tunnel vision.

Include:

- repository/project structure;
- app/runtime shape;
- major modules or absence of modules;
- existing docs/specs;
- accepted-state records;
- current system maturity;
- state confidence.

## Focused System State Understanding

Describe the areas directly and indirectly implicated by the User Request and source inputs.

Include:

- directly affected files/modules/workflows;
- indirectly affected areas;
- current behavior to preserve;
- constraints discovered;
- risks relevant to Design.

## Evidence Table

| Claim | Evidence | Type | Confidence | Notes |
|---|---|---|---|---|

Types:

```text
observed
inferred
assumed
unknown
blocked
not_applicable
```

## Project Type and Stack Classification

- Project type:
- Project-type confidence: high | medium | low | unknown
- Classification evidence:
- Active stack:
- Stack confidence: high | medium | low | unknown
- Stack evidence:
- Repository evidence conflicts with request preference: yes / no / not applicable
- Conflicts or uncertainty:
- support/project-context.md updated or not required:
- support/stack-resolution.json updated or not required:

## Stack Contexts

Default: not active.

Use this section only when repository evidence, accepted system state, or explicit configuration shows multiple bounded stack areas.

| Context ID | Root path | Stack ID | Evidence | Confidence | In-scope status | Notes |
|---|---|---|---|---|---|---|

Allowed in-scope statuses:

```text
IN_SCOPE
OUT_OF_SCOPE
IMPACTED_NOT_AUTHORIZED
UNKNOWN
```

Do not activate stack contexts for incidental language files. Activate them only when they affect Design, Implementation, validation, or evidence boundaries.

## Preservation Requirements Discovered

For brownfield, prototype-to-product, or mixed work, list current behavior, data, APIs, workflows, prototype behavior, or user expectations that Design must preserve.

| Requirement | Evidence | Scope | Confidence | Notes |
|---|---|---|---|---|

## Unknowns and Risks

List system-state unknowns, contradictions, or risks. Add unresolved items if they affect Design, Implementation, or Update System State.

| Unknown / risk | Affected lifecycle stage | Gated? | Unresolved item ID | Notes |
|---|---|---|---|---|

## Route-Back Inputs

If this artifact was regenerated because of a later-stage discovery, record what changed and what earlier artifact/content it supersedes.

## Handoff to Design

Explain what Design may use as evidence and what it must not treat as authority.

## Completion

- Terminal state: COMPLETED | NEEDS_USER_DECISION | BLOCKED | ROUTE_BACK_REQUIRED
- Current-system-state-first control satisfied or not applicable: yes / no
- General understanding complete enough: yes / no
- Focused understanding complete enough: yes / no / not applicable with rationale
- SESSION_EXECUTION.md updated: yes / no
- Unresolved-item contribution completed: yes / no / not applicable

## Autonomous Technical Discovery

Record technical facts that may let HIRMOS proceed without asking routine setup questions.

| Area | Evidence inspected | Safe local/default path found? | Suggested next technical action | Needs user/technical decision? | Notes |
|---|---|---:|---|---:|---|

Inspect when relevant:

- package scripts and package manager evidence;
- env examples and non-secret configuration patterns;
- database/auth/provider/storage/deployment surfaces;
- migration, seed, validation, and smoke-test commands;
- local service availability when safe and tools permit it;
- runtime errors that can be fixed inside accepted scope.

System State discovers facts. Design decides what is authorized. Implementation performs authorized technical progress.
