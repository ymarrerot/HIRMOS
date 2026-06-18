# Session Contract


## Delivery Governance Classification

This section is required for every implementation-capable session before implementation readiness.

Does this request require multi-session delivery governance?
Answer: YES | NO | UNCERTAIN

- Project type: GREENFIELD | BROWNFIELD_TARGETED | BROWNFIELD_MULTISESSION | MIXED | UNKNOWN
- Evidence:
- Decision factors:
- Triggers present:
- Triggers ruled out:
- Single-session safety justification:
- If YES, required Delivery Plan: `_hirmos/system/delivery/<delivery-id>/DELIVERY_PLAN.md`
- Active phase path, if applicable: `_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md`
- Current System State delivery pointer basis: `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md` Active Development Context and Delivery Pointers
- Pointer consistency result: CONSISTENT | BLOCKED | NOT_APPLICABLE
- If UNCERTAIN, what must be inspected before deciding?

Fail-closed rule:

- YES requires a durable Delivery Plan and separate phase file before implementation authorization.
- UNCERTAIN blocks implementation readiness.
- NO requires affirmative single-session safety evidence and trigger review.

For multi-session work in any project type, a Delivery Plan is needed and separate phase files are required.



## Delivery / Phase Capability Routing Evidence


## Active Durable Phase Adoption

Required when Delivery-Need Classification is `YES` and the session is implementation-capable.

- Adoption status: ADOPTED | NOT_APPLICABLE | BLOCKED
- Delivery ID:
- Delivery Plan path: `_hirmos/system/delivery/<delivery-id>/DELIVERY_PLAN.md`
- Active Phase ID:
- Active Phase path: `_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md`
- Current System State active phase pointer:
- Phase source status: NOT_STARTED | ACTIVE | BLOCKED | ACCEPTED | SUPERSEDED | UNKNOWN
- Adoption mode: FULL_PHASE | EXPLICIT_PARTIAL_WITH_DEFERRED_ITEMS | DESIGN_ONLY_NO_IMPLEMENTATION
- Implementation authorized from adopted phase? YES | NO

### Adopted phase scope

| Phase item ID | Phase contract text / summary | Adopted into Session Contract item(s) | Implementation unit(s) | Status |
|---|---|---|---|---|
| PH-ITEM-01 | | SC-01 | IU-01 | PENDING |

### Phase exclusions / deferrals

| Phase item ID | Excluded / deferred / blocked reason | Future phase/session path | User approval / evidence |
|---|---|---|---|
| | | | |

### Durable phase adoption coverage question

Does `SESSION_CONTRACT.md` adopt exactly one active durable `PHASE-xx.md` and cover the intended phase scope without silent omissions?

- Answer: YES | NO | PARTIAL | NOT_APPLICABLE
- Evidence:
- Gaps:
- Deferred / blocked items:
- Fail-closed result: PASS | FAIL | NOT_ASSESSED

Fail-closed rule: delivery-governed implementation is not authorized when this adoption section is missing, `BLOCKED`, `NOT_ASSESSED`, references more than one active phase, contradicts Current System State delivery pointers, or fails to map adopted phase items to authorized Session Contract items.


Required when Delivery-Need Classification is `YES`:

| Capability | Required output | Path / evidence | Status |
| --- | --- | --- | --- |
| delivery-design | Durable Delivery Plan | `_hirmos/system/delivery/<delivery-id>/DELIVERY_PLAN.md` | |
| phase-contracting | Durable phase file | `_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md` | |
| session-contract | Active Session Contract adoption | `_hirmos/session/SESSION_CONTRACT.md` | |
| implementation-readiness | Readiness gate | `_hirmos/session/support/implementation-readiness.md` | |

Status: active-session Main Artifact.
Purpose: define the exact work authorized for the active HIRMOS session, the completion criteria, the coverage obligations, and the close verification basis.

This artifact is the session scope and acceptance authority. Implementation may not begin until this contract exists, is non-placeholder, and the relevant execution controls in `SESSION_EXECUTION.md` are satisfied.

## 1. Session Identity

- Session ID:
- User request / command:
- Interaction mode:
- Session type: design-only | implementation | review | close/update-state | other
- Current lifecycle boundary:

## 2. Parent Authority

Identify every source this session contract must cover.

| Source type | Artifact/path/source | Required? | Coverage obligation |
|---|---|---:|---|
| Current System State | `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md` | yes | Must be read before meaningful work and delivery pointers must be inspected. |
| Requirements | | | |
| Durable Delivery Plan | `_hirmos/system/delivery/<delivery-id>/DELIVERY_PLAN.md` when required | | |
| Durable Phase Contract | `_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md` when applicable | | |
| User request | | | |
| Other | | | |

## 3. Authorized Scope

List exactly what this session is authorized to complete.

| ID | Authorized work item | Source authority | Completion evidence required |
|---|---|---|---|
| SC-01 | | | |

## 4. Explicit Exclusions

List work this session must not do.

| ID | Excluded item | Reason | Future path, if any |
|---|---|---|---|
| EX-01 | | | |

## 5. Brownfield Preservation Rules

Record what existing behavior, files, APIs, data, UX, tests, runtime behavior, artifacts, or framework contracts must not regress.

| ID | Preservation requirement | Affected area | Evidence required |
|---|---|---|---|
| PR-01 | | | |

## 6. Completion Criteria

Use binary or explicitly inspectable criteria. Avoid vague criteria.

| Criterion ID | Criterion | Evidence required | Pass/Fail basis |
|---|---|---|---|
| CC-01 | | | |

## 7. Validation Requirements

List required validation and the allowed evidence posture.

| Validation ID | Command/check/review | Required? | Evidence required | If not run, required rationale |
|---|---|---:|---|---|
| VAL-01 | | | | |

## 8. Implementation Unit Plan

Implementation units are required when implementation is non-trivial, multi-file, risky, or delegated to an implementation agent. Unit files live under `_hirmos/session/implementation-units/`.

| Unit ID | Unit artifact | Purpose | Contract coverage | Dependencies | Status |
|---|---|---|---|---|---|
| IU-01 | `_hirmos/session/implementation-units/IU-01.md` | | | | planned |

### Required implementation-unit coverage question

Do all planned implementation units collectively cover 100% of `SESSION_CONTRACT.md`?

- Answer: YES | NO | PARTIAL | NOT_APPLICABLE
- Evidence:
- Gaps:
- Deferred items:

## 9. Unresolved Items Control

Authoritative register: `_hirmos/session/unresolved-items.md`

This section is only a control summary. It is not sufficient for review, implementation, continuation, or close. HIRMOS must read and apply `_hirmos/session/unresolved-items.md` directly before every lifecycle boundary.

Summary:

- Gated unresolved items:
- Non-gating assumptions/items:
- Technical-review items:
- Resolved items this session:
- Last direct register review boundary:
- Blocking status: BLOCKED | NOT_BLOCKED

Boundary rule:

- If any gated item is unresolved, HIRMOS must fail closed and may only recommend the appropriate governed command for resolution or status.
- If any non-gating item exists, HIRMOS must preserve it, apply its assumption/revalidation rule, and include it in close verification.
- HIRMOS must not infer unresolved-item details from this summary.
- This summary must not contain item-level detail rows. Item-level detail belongs only in `_hirmos/session/unresolved-items.md`.

## 10. Coverage Matrix

Use this matrix to prove source-to-session coverage.

| Source requirement / phase item / user request item | Covered by session contract item(s) | Covered by implementation unit(s) | Evidence method | Status |
|---|---|---|---|---|
| | | | | NOT_ASSESSED |

### Requirements coverage question

Does `SESSION_CONTRACT.md` cover 100% of the applicable Requirements artifact?

- Answer: YES | NO | PARTIAL | NOT_APPLICABLE
- Evidence:
- Gaps:
- Deferred items:

### Phase coverage question

Does `SESSION_CONTRACT.md` cover 100% of the active `PHASE-xx.md` contract?

- Answer: YES | NO | PARTIAL | NOT_APPLICABLE
- Evidence:
- Gaps:
- Deferred items:

## 11. Session Contract Review Control

Authoritative review artifact: `_hirmos/session/session-contract-review.md`

This section is only a control pointer and final-verdict mirror. It is not sufficient for implementation-completion, close-readiness, or close. HIRMOS must read and complete `_hirmos/session/session-contract-review.md` directly before claiming that the session contract was satisfied.

Required review rule:

- `session-contract-review.md` must compare promised work against verified work.
- `session-contract-review.md` must answer: Does the actual completed work satisfy 100% of `SESSION_CONTRACT.md`?
- `session-contract-review.md` must answer the required 100% coverage questions.
- `session-contract-review.md` must reconcile unresolved items by direct review of `_hirmos/session/unresolved-items.md`.
- `session-contract-review.md` must produce a final verdict and fail-closed result.
- HIRMOS must not infer Session Contract Review details from this control section.

Final verdict mirror:

- Review artifact completed? YES | NO
- Final review verdict: COMPLETE | PARTIAL | FAILED | BLOCKED | NOT_REVIEWED
- Fail-closed result: PASS | FAIL | NOT_REVIEWED
- Review artifact path: `_hirmos/session/session-contract-review.md`
- Gaps / carry-forward summary:

Fail-closed rule:

If `session-contract-review.md` is missing, placeholder-only, not directly reviewed, or has a fail-closed result of `FAIL`, HIRMOS must not claim normal implementation completion, close readiness, or close success.


## Autonomous Technical Progress Authorization

- Safe local/default technical progress is authorized only when it remains inside this Session Contract.


## 12. Contract Amendments

Use this section only when a later `hirmos continue "..."` changes scope before close. Do not silently rewrite the original Authorized Scope.

| Amendment ID | Triggering command | Scope change | Accepted into session? | Implementation units affected | Unresolved items affected | Evidence / approval |
|---|---|---|---:|---|---|---|

Fail-closed rule: implementation of new scope is not authorized until the amendment is recorded, unresolved items are updated, and implementation-unit coverage is updated.

## Phase Entry Gate Evidence

When Delivery-Need Classification is `YES`, this session may adopt a durable `PHASE-xx.md` only after directly reading its Phase Entry Gate.

Required evidence:

```text
Phase Entry Gate status: PASS / BLOCKED / UNCERTAIN / NOT_APPLICABLE
Lifecycle status supports adoption: YES / NO
Phase type supports implementation: YES / NO
Entry criteria satisfied: YES / NO
Type-specific entry controls satisfied: YES / NO / NOT_APPLICABLE
Pointer concordance satisfied: YES / NO
Blocking open items absent or resolved: YES / NO
```

Implementation readiness is blocked when any required answer is `NO`, `BLOCKED`, or `UNCERTAIN`.

## Phase Progress and Carry-Forward Control

Required when Delivery-Need Classification is `YES`.

- Previous Phase Progress Ledger inspected: YES / NO / NOT_APPLICABLE
- Expected phase outcome this session: ACCEPTED / PARTIAL / BLOCKED / DEFERRED / SUPERSEDED / CANCELLED / UNKNOWN
- Carry-forward required if not accepted: YES / NO / NOT_APPLICABLE
- Carry-forward target if required:
- Items explicitly excluded from this session:
- Items that must not be silently dropped:

This control does not replace the durable `PHASE-xx.md` Phase Progress Ledger. It records the session-level obligation to update it.


## Phase Acceptance Control

- Proposed phase outcome: ACCEPTED / PARTIAL / BLOCKED / DEFERRED / SUPERSEDED / CANCELLED / UNKNOWN
- Phase acceptance will be evaluated through Phase Acceptance Evidence Gate: YES / NO / NOT_APPLICABLE
- Acceptance cannot be claimed from session narrative alone: yes / no
- Adopted phase exit criteria mapped to Session Contract items: yes / no / not_applicable
- Known exclusions or deferrals recorded before acceptance: yes / no / not_applicable
