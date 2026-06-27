# Implementation Unit

Status: active-session implementation-unit Main Artifact.
Purpose: define a sealed execution contract for one bounded implementation unit, then preserve append-only execution, review, retry, and handoff records in clearly separated sections.

An Implementation Unit is a bounded execution authority record, not a generic task or prompt.

Governance posture: this file is pre-execution authority, not an after-the-fact compliance report. It is pre-execution authority first. When IU mode is active, the IU Contract sections must exist with non-placeholder authority before material code/configuration changes for this unit begin. After the contract is sealed and material implementation starts, contract sections are immutable unless route-back explicitly reopens or supersedes the contract. Execution, review, retry, and handoff sections are append-only records and must not be used to rewrite sealed authority.

## 1. Unit Identity / Contract Metadata

LLM Write Permission: Mutable only before contract seal; immutable after seal unless route-back records contract reopening or supersession.

- Unit ID:
- Name:
- Governing Session Scope: `_hirmos/session/SESSION_SCOPE.md`
- Session Scope scope item(s):
- Related requirements / delivery / phase source:
- Primary stack context:
- Root path:
- Cross-stack unit: yes / no
- If cross-stack, involved contexts and justification:
- Contract status: DRAFT | SEALED | REOPENED_BY_ROUTE_BACK | SUPERSEDED
- Contract sealed before material edits: YES | NO | NOT_APPLICABLE
- Contract seal timestamp / evidence pointer:
- Contract reopened after material edits: NO | YES_WITH_ROUTE_BACK
- Route-back / supersession pointer, if any:

## 2. Unit Scope / Authority

LLM Write Permission: Immutable after contract seal unless route-back occurs. Do not edit this section to record execution status, evidence, review findings, or validator cleanup.

### Objective

State the exact outcome this unit must produce.

### Context

Provide only context relevant to this unit: current lifecycle boundary, relevant current system state, relevant design decisions, dependencies, and prior units.

### In Scope

List exact files, components, behaviors, tests, docs, configuration, or artifacts this unit may change.

### Out of Scope

List work explicitly forbidden for this unit, including future-phase work and unrelated cleanup.

### Files / Areas

List concrete targets. If unknown, state what inspection must happen before editing.

### Preservation Rules

Record architecture, data, workflow, security, runtime, accepted-state, UX, and compatibility rules this unit must preserve.

### Implementation Requirements

Define required implementation behavior, interfaces, data flow, persistence, APIs, UI, integration details, or artifact changes.

### Verification Commands / Checks

List exact commands or checks. If a command is not available or not applicable, require a recorded rationale.

### Evidence Requirements

List required outputs, logs, diffs, screenshots, observations, or review notes.

### Runtime Integration Posture

| Area | Authorized posture | Allowed fallback | Required environment/config | Evidence required |
|---|---|---|---|---|

The unit must not silently substitute fixture/mock/boundary-only work for a required real integration.

### Binary Acceptance Criteria

| Criterion | Evidence required | Pass/Fail basis |
|---|---|---|

## 3. Pre-Execution Checks

LLM Write Permission: Mutable only before contract seal; immutable after material implementation starts unless route-back occurs.

| Check | Result | Evidence / notes |
|---|---|---|
| Unit authority record is non-placeholder | | |
| Session Scope still governs this unit | | |
| unresolved-items.md has no gated blocker for this unit | | |
| Target files inspected before editing | | |
| Required dependencies/context available | | |
| Out-of-scope guard understood | | |
| Contract status is SEALED before material edits | | |
| Contract sections will remain immutable during execution | | |

## 4. Execution Record

LLM Write Permission: Append-only after execution starts; executor may append implementation actions, changed files, validation, evidence, limitations, and issues. Do not modify sealed contract sections.

### Execution Status

- Execution status: NOT_STARTED | IN_PROGRESS | COMPLETED | BLOCKED | FAILED | ROUTE_BACK_REQUIRED
- Execution start timestamp / evidence pointer:
- Execution completion timestamp / evidence pointer:

### Actions Performed

List concrete actions performed.

### Files / Artifacts Changed

| Path | Change summary | Authorized by | Notes |
|---|---|---|---|

### Scope Conformance Notes

State how execution stayed within this Implementation Unit and the Session Scope.

### Validation / Checks Performed During Execution

| Check / command | Result | Output/log location | Notes |
|---|---|---|---|

### Test / Fixture / Validator Change Rationale

Required when implementation modifies tests, fixtures, mocks, snapshots, validators, expected-output files, regression fixtures, or generated expected-output artifacts.

- Changed test / fixture / validator files:
- Why the change was required:
- Why realism or coverage is preserved or improved:
- Risk that validation was weakened:
- Reviewer attention needed:

### Runtime Integration Execution Evidence

| Area | Delivered posture | Files/config changed | Commands run | Credentials/env available? | Runtime verified? | Limitations |
|---|---|---|---|---:|---:|---|

### Claim Evidence Produced

| Claim supported | Evidence status | Command/log/file | Runtime observed? | Limitation |
|---|---|---|---:|---|

### Issues Encountered

List blockers, deviations, failures, scope risks, or route-back triggers.

### Execution Result

- COMPLETED | BLOCKED | FAILED | ROUTE_BACK_REQUIRED
- Rationale:
- Next required action:

## 5. Unit Review

LLM Write Permission: Append-only after execution completes; reviewer may append evidence-backed review results, retry decision, route-back decision, and honest limitations. Do not modify sealed contract sections.

Does the actual implementation satisfy 100% of this implementation unit authority record?

- Answer: YES | NO | PARTIAL
- Evidence:
- Gaps:
- Deferred items:
- Review status: PENDING | PASS | PASS_WITH_LIMITATIONS | FAIL | BLOCKED | ROUTE_BACK_REQUIRED

### Request-to-Result Review

| Unit authority record requirement | Result | Evidence | Notes |
|---|---|---|---|

### Scope Conformance Review

| Scope item | Result | Evidence | Notes |
|---|---|---|---|

### Validation Review

| Check | Run? | Result | Evidence location | Notes |
|---|---:|---|---|---|

### Test / Fixture / Validator Change Review

| Changed file/category | Rationale present? | Preserves or improves realism/coverage? | Weakening risk | Reviewer result |
|---|---:|---:|---|---|

### Not Run / Not Applicable Checks

| Check | Reason | Risk | Follow-up |
|---|---|---|---|

### Runtime Integration Review

| Area | Requested posture | Delivered posture | Match? | Evidence | Action |
|---|---|---|---:|---|---|

### Claim Reconciliation

| Unit claim | Evidence status | Final-file support | Log/output | Runtime verified? | Result |
|---|---|---|---|---:|---|

### Retry / Route-Back Decision

- Retry required:
- Retry allowed within current sealed scope:
- Route-back required:
- Contract change required:
- Reason:

### Unit Result

- PASS | PASS_WITH_LIMITATIONS | FAIL | BLOCKED | ROUTE_BACK_REQUIRED
- Rationale:
- Follow-up required:

## 6. Retries

LLM Write Permission: Append-only. Retry within sealed scope may be appended here. Scope, source authority, acceptance-criteria, or contract changes require route-back and a new/reopened sealed contract version.

Append retry sections here when a retry is required. Do not create a separate retry artifact. Do not edit sealed contract sections to make a retry pass. If the retry requires changing scope, source authority, acceptance criteria, or implementation requirements, record route-back and create a new/reopened sealed contract version before further material edits.

### Retry <n> Contract

#### Retry Decision

- Triggering failure / blocker:
- Evidence from Failed Attempt:
- Retry decision: RETRY_READY | ESCALATE | ROUTE_BACK_REQUIRED | BLOCKED
- Allowed retry scope:
- Not allowed:
- Changed assumptions / route-back need:
- Contract change required: YES | NO
- Retry steps:
- Verification and evidence:
- Escalation Condition:

### Retry <n> Evidence

| Action / check | Result | Evidence | Notes |
|---|---|---|---|

### Retry <n> Review

- Result: PASS | PASS_WITH_LIMITATIONS | FAIL | BLOCKED | ROUTE_BACK_REQUIRED
- Rationale:
- Follow-up required:

## 7. Handoff

LLM Write Permission: Append-only summary after review; must point to execution/review evidence and must not change sealed contract authority.

- Session Scope coverage item(s) satisfied:
- Remaining gaps:
- Carry-forward candidates:
- `SESSION_SCOPE.md` close verification review impact:


## Phase Acceptance Evidence Contribution

LLM Write Permission: Append-only summary after review; must point to evidence/review records and must not change sealed contract authority.

- Phase acceptance contribution: COMPLETE / PARTIAL / BLOCKED / NOT_APPLICABLE
- Adopted phase item(s) satisfied by this unit: 
- Evidence pointer(s): 
- Remaining gap or carry-forward implication: NONE / RECORDED / BLOCKED / NOT_APPLICABLE


## PROD-L8.19 Pre-Execution Authority Declaration

LLM Write Permission: Append-only governance note; do not use this section to repair sealed contract authority after execution.

This IU must be represented as pre-execution governance before material implementation begins. If the IU contract was created, expanded, sealed, or materially corrected after project-file changes began, that must be recorded as a governance deviation/correction and must not be represented as normal pre-execution governance.

## PROD-L8.21 Minimum IU Contract

LLM Write Permission: Immutable after contract seal unless route-back occurs.

- Source Scope Traceability:
- Minimum Contract Self-Check:
- Failure / route-back condition:

## PROD-L8.23 Generated IU Runtime-Enforcement Notes

LLM Write Permission: Immutable after contract seal unless route-back occurs.

Generated IU artifacts must not rely on thin IU self-attestation. They must contain sealed, non-placeholder contract authority before implementation and append-only execution/review evidence after implementation begins.

## PROD-L8.28 Generated IU Full Instantiation and Active Close Concordance

LLM Write Permission: Immutable after contract seal unless route-back occurs.

Generated IU artifacts must instantiate the full sealed-section model before implementation execution. A thin generated IU stub is invalid even when it says `Contract status: SEALED` or `Contract sealed before material edits: YES`.

Before material implementation starts, each generated IU must contain non-placeholder content for all required contract authority areas: Unit Identity / Contract Metadata, Unit Scope / Authority, Objective, Context, In Scope, Out of Scope, Files / Areas, Preservation Rules, Implementation Requirements, Verification Commands / Checks, Evidence Requirements, Runtime Integration Posture, Binary Acceptance Criteria, Pre-Execution Checks, PROD-L8.21 Minimum IU Contract, and all applicable `LLM Write Permission:` lines.

Before active close can be claimed, each generated IU that contributed to implementation completion must contain append-only Execution Record and Unit Review content with concrete actions, changed files, validation/check evidence, claim evidence, execution result, review status, unit result, and any required Test / Fixture / Validator Change Rationale. A session or phase must not claim implementation completion when any applicable IU remains `Execution status: NOT_STARTED`, `Review status: PENDING`, or lacks an evidence-backed Unit Result.

## Canonical interaction posture visibility

LLM Write Permission: Append-only guidance section; do not use this section to change sealed IU contract authority.

Use `_hirmos/core/authority/INTERACTION_POSTURE.md` when surfacing IU status to the user: keep the user-facing summary concise, include artifact paths for IU authority/evidence/review claims, and disclose additional details when validation failure, blocker state, retry, route-back, or user request requires it.


## PROD-L8.30A IU Action-Gate Correction
Generated IU artifacts must not use `Contract sealed before material edits: YES` unless the session ledger proves full IU contract authority existed before the first material edit. If the session ledger records code-before-IU, retrospective IU creation, retrospective sealed-contract mutation, or after-the-fact authority reconstruction, the IU must record `Contract sealed before material edits: NO` and identify the governance deviation, route-back, or partial/blocking disposition. A false clean-seal claim is invalid even when the IU later contains a complete contract template.
