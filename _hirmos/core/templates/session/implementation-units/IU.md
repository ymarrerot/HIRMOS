# Implementation Unit

Status: active-session implementation-unit Main Artifact.
Purpose: define, execute, evidence, review, and retry one bounded implementation unit in a single self-contained artifact.

An Implementation Unit is a bounded execution authority record, not a generic task or prompt.


Governance posture: this file is pre-execution authority, not an after-the-fact compliance report. When IU mode is active, this file must exist with non-placeholder authority before material code/configuration changes for this unit begin.

## 1. Unit Identity

- Unit ID:
- Name:
- Governing Session Scope: `_hirmos/session/SESSION_SCOPE.md`
- Session Scope scope item(s):
- Related requirements / delivery / phase source:
- Primary stack context:
- Root path:
- Cross-stack unit: yes / no
- If cross-stack, involved contexts and justification:
- Unit status: planned | approved | in_progress | complete | partial | failed | blocked | route_back_required

## 2. Unit Scope

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

| Check | Result | Evidence / notes |
|---|---|---|
| Unit authority record is non-placeholder | | |
| Session Scope still governs this unit | | |
| unresolved-items.md has no gated blocker for this unit | | |
| Target files inspected before editing | | |
| Required dependencies/context available | | |
| Out-of-scope guard understood | | |

## 4. Execution Record

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

Does the actual implementation satisfy 100% of this implementation unit authority record?

- Answer: YES | NO | PARTIAL
- Evidence:
- Gaps:
- Deferred items:

### Request-to-Result Review

| Unit authority record requirement | Result | Evidence | Notes |
|---|---|---|---|

### Scope Conformance Review

| Scope item | Result | Evidence | Notes |
|---|---|---|---|

### Validation Review

| Check | Run? | Result | Evidence location | Notes |
|---|---:|---|---|---|

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
- Retry allowed within current scope:
- Route-back required:
- Reason:

### Unit Result

- PASS | PASS_WITH_LIMITATIONS | FAIL | BLOCKED | ROUTE_BACK_REQUIRED
- Rationale:
- Follow-up required:

## 6. Retries

Append retry sections here when a retry is required. Do not create a separate retry artifact.

### Retry <n> Contract

#### Retry Decision

- Triggering failure / blocker:
- Evidence from Failed Attempt:
- Retry decision: RETRY_READY | ESCALATE | ROUTE_BACK_REQUIRED | BLOCKED
- Allowed retry scope:
- Not allowed:
- Changed assumptions / route-back need:
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

- Session Scope coverage item(s) satisfied:
- Remaining gaps:
- Carry-forward candidates:
- `SESSION_SCOPE.md` close verification review impact:


## Phase Acceptance Evidence Contribution

- Phase acceptance contribution: COMPLETE / PARTIAL / BLOCKED / NOT_APPLICABLE
- Adopted phase item(s) satisfied by this unit: 
- Evidence pointer(s): 
- Remaining gap or carry-forward implication: NONE / RECORDED / BLOCKED / NOT_APPLICABLE

## PROD-L8.19 Pre-Execution Authority Declaration

This IU must exist as a non-placeholder execution authority before material implementation begins, unless the session explicitly declared lightweight/no-IU mode before implementation.

- IU created before material code changes: YES / NO
- If NO, governance deviation recorded in `SESSION_EXECUTION.md`: YES / NO / NOT_APPLICABLE
- Pre-execution authority complete: YES / NO
- First material edit allowed only after this declaration is YES: YES / NO
- Evidence of pre-execution authority: `<SESSION_EXECUTION.md continuation pass / command ledger / timestamp / diff reference>`

A retrospective IU may document what happened, but it must not be represented as normal pre-execution governance unless it actually existed before the material edits.
