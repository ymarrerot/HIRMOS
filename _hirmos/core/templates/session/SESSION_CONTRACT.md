# Session Contract

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

## 7. Delivery Shape Decision

This section is required for every implementation-capable session before implementation readiness.

What is the smallest sufficient governed delivery shape for this request?
Answer: SINGLE_SESSION_VERTICAL_SLICE | SINGLE_SESSION_WITH_IMPLEMENTATION_UNITS | MULTI_SESSION_DELIVERY | MULTI_SESSION_DELIVERY_WITH_PHASE_FILES | UNCERTAIN

- Project type: GREENFIELD | BROWNFIELD_TARGETED | BROWNFIELD_MULTISESSION | MIXED | UNKNOWN
- Evidence:
- Decision factors:
- Smaller-shape safety analysis:
- Larger-shape overhead analysis:
- Triggers considered:
- Triggers ruled out:
- Selected shape justification:
- If `SINGLE_SESSION_VERTICAL_SLICE`, why is one bounded session safe without separate implementation units?
- If `SINGLE_SESSION_WITH_IMPLEMENTATION_UNITS`, required implementation unit coverage plan:
- If `MULTI_SESSION_DELIVERY`, required Delivery Plan: `_hirmos/system/delivery/<delivery-id>/DELIVERY_PLAN.md`
- If `MULTI_SESSION_DELIVERY_WITH_PHASE_FILES`, required Delivery Plan and active phase path: `_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md`
- Current System State delivery pointer basis: `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md` Active Development Context and Delivery Pointers
- Pointer consistency result: CONSISTENT | BLOCKED | NOT_APPLICABLE
- If UNCERTAIN, what must be inspected before deciding?

Fail-closed rule:

- `UNCERTAIN` blocks implementation readiness.
- `SINGLE_SESSION_VERTICAL_SLICE` requires affirmative bounded-scope safety evidence.
- `SINGLE_SESSION_WITH_IMPLEMENTATION_UNITS` requires implementation units that collectively cover authorized scope.
- `MULTI_SESSION_DELIVERY` requires a durable Delivery Plan before implementation authorization.
- `MULTI_SESSION_DELIVERY_WITH_PHASE_FILES` requires a durable Delivery Plan and adopted phase file before implementation authorization.
- The selected shape must be the smallest shape that preserves engineering quality, implementation truth, validation, continuity, and accepted-state integrity.

## 8. Production-Shaped Engineering Gate

Required for implementation-capable software sessions before implementation authorization and reviewed again at close.

| Gate area | Required production-shaped posture | Session decision / evidence required | Status |
|---|---|---|---|
| Production-shaped default | The session aims for production-shaped implementation unless explicitly scoped otherwise. | Design decision and scope evidence | PENDING |
| Persistence / database | Durable business data uses durable persistence; local mirrors intended production where practical. | Design + implementation evidence | PENDING |
| Auth / authorization | Protected resources have server-side user/resource isolation. | Code/evidence | PENDING |
| Background jobs / long-running work | Long-running AI/provider/file work is outside synchronous request paths. | Architecture + runtime evidence | PENDING |
| Credits / usage / billing / quotas | Mutations are transactional, concurrency-safe, idempotent, or explicitly limited. | Code/evidence | PENDING |
| Provider APIs / external services | Provider boundary, env validation, and failure posture are explicit. | Code/config/evidence | PENDING |
| File or object storage | Uploads/generated assets use validation, safe paths, and handoff hygiene. | Code/package evidence | PENDING |
| Secrets and environment configuration | `.env.example` exists when needed; secrets/runtime data are excluded from handoff/release outputs. | Packaging/handoff evidence | PENDING |
| Critical-flow evidence | Critical product flow has test/smoke/runtime evidence appropriate to scope. | Validation evidence | PENDING |
| Weaker local/demo choices | Any prototype, fixture, demo-only, or local-only shortcut is explicitly authorized. | Authorized limitation/rationale | PENDING |

Implementation is not authorized to claim production-shaped completion beyond this gate. Close must preserve any unresolved or intentionally scoped-down posture as accepted-state limitation or carry-forward work.

## 9. Delivery / Phase Capability Routing Evidence

Required when the selected delivery shape is `MULTI_SESSION_DELIVERY` or `MULTI_SESSION_DELIVERY_WITH_PHASE_FILES`.

| Capability | Required output | Path / evidence | Status |
|---|---|---|---|
| delivery-design | Durable Delivery Plan | `_hirmos/system/delivery/<delivery-id>/DELIVERY_PLAN.md` | |
| phase-contracting | Durable phase file when phase files are selected | `_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md` | |
| session-contract | Active Session Contract adoption | `_hirmos/session/SESSION_CONTRACT.md` | |
| implementation-readiness | Readiness gate | `_hirmos/session/DESIGN.md` | |

## 10. Active Durable Phase Adoption

Required when the selected delivery shape is `MULTI_SESSION_DELIVERY_WITH_PHASE_FILES` and the session is implementation-capable.

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

## 11. Validation Requirements

List required validation and the allowed evidence posture.

| Validation ID | Command/check/review | Required? | Evidence required | If not run, required rationale |
|---|---|---:|---|---|
| VAL-01 | | | | |

## 12. Implementation Unit Plan

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

## 13. Unresolved Items Control

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
- Non-gating items are governed output, not informal notes; they are often where risky assumptions or hidden decisions surface.
- HIRMOS must not infer unresolved-item details from this summary.
- This summary must not contain item-level detail rows. Item-level detail belongs only in `_hirmos/session/unresolved-items.md`.

## 14. Coverage Matrix

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

## 15. Phase Entry Gate Evidence

Record phase entry gate evidence here when durable delivery governance is active. This section replaces any separate phase-entry major artifact section.

- Phase Entry Gate Evidence:
- Lifecycle status:
- Phase type:
- Entry gate status:
- Entry criteria satisfied:
- Phase Entry Gate status: PASS / BLOCKED / UNCERTAIN / NOT_APPLICABLE

## 16. Phase Progress and Carry-Forward Control

- Previous Phase Progress Ledger inspected:
- Carry-forward required if not accepted:
- Carry-forward target:
- Phase result implication:
- Phase Entry Gate status: PASS / BLOCKED / UNCERTAIN / NOT_APPLICABLE

## 17. Phase Acceptance Control

Phase acceptance will be evaluated through Phase Acceptance Evidence Gate when durable delivery governance is active.

- Phase acceptance verdict:
- Phase acceptance evidence status:
- Acceptance gate status:

## 18. Autonomous Technical Progress Authorization

- Autonomous Technical Progress Authorization:
- Safe local/default technical progress authorized:
- Decisions requiring user or technical review:

## 19. Session Satisfaction Review and Close Verification

This section is the governed promised-vs-verified review surface for the session. Do not create a separate `SESSION_CONTRACT.md` section 11 artifact for new sessions.

### Required inputs directly reviewed

| Input | Path / evidence | Directly reviewed? | Notes |
|---|---|---:|---|
| Session Contract | `_hirmos/session/SESSION_CONTRACT.md` | NO | |
| Unresolved Items | `_hirmos/session/unresolved-items.md` | NO | |
| Session Execution | `_hirmos/session/SESSION_EXECUTION.md` | NO | |
| Design authority | `_hirmos/session/DESIGN.md` when applicable | NOT_APPLICABLE | |
| Requirements baseline | `_hirmos/session/REQUIREMENTS_BASELINE.md` when applicable | NOT_APPLICABLE | |
| Implementation Units | `_hirmos/session/implementation-units/` when applicable | NOT_APPLICABLE | |
| Evidence | `_hirmos/session/EVIDENCE.md` when applicable | NOT_APPLICABLE | |
| Current System State | `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md` | NO | |

Allowed reviewed values: `YES`, `NO`, `NOT_APPLICABLE`. If a required input is marked `NO`, HIRMOS must not claim implementation completion, close readiness, or close success.

### Promised work register

List every material promise from Authorized Scope, Completion Criteria, Validation Requirements, Production-Shaped Engineering Gate, and Implementation Unit Plan.

| Promise ID | Promised work / criterion | Source section | Required evidence | Status |
|---|---|---|---|---|
| SCV-P01 | | | | NOT_VERIFIED |

Allowed statuses: `VERIFIED`, `PARTIAL`, `NOT_VERIFIED`, `DEFERRED_ACCEPTED`, `OUT_OF_SCOPE`, `BLOCKED`.

### Verified work register

| Evidence ID | Evidence source | What it verifies | Result | Limitations |
|---|---|---|---|---|
| SCV-E01 | | | | |

Evidence must be concrete: command output, file/path inspection, implementation-unit review, runtime smoke, `EVIDENCE.md`, or explicit user decision.

### Promised vs verified coverage matrix

| Promise ID | Covered by implementation unit(s) | Covered by evidence ID(s) | Coverage status | Gap / deferred item |
|---|---|---|---|---|
| SCV-P01 | | | NOT_VERIFIED | |

Allowed coverage statuses: `FULL`, `PARTIAL`, `NONE`, `DEFERRED_ACCEPTED`, `OUT_OF_SCOPE`, `BLOCKED`.

### Required close questions

- Do all implementation units combined satisfy 100% of `SESSION_CONTRACT.md`? YES | NO | PARTIAL | NOT_APPLICABLE
- Does the actual completed work satisfy 100% of `SESSION_CONTRACT.md`? YES | NO | PARTIAL
- Were all required validation checks run or explicitly justified as not run / not applicable? YES | NO | PARTIAL
- Was `_hirmos/session/unresolved-items.md` directly reviewed and reconciled? YES | NO
- Was the Production-Shaped Engineering Gate reviewed at close? YES | NO | NOT_APPLICABLE
- Are accepted-state updates and carry-forward obligations clear? YES | NO | NOT_APPLICABLE

### Final review verdict

- Verdict: COMPLETE | PARTIAL | FAILED | BLOCKED
- Rationale:
- Required close action:
- Carry-forward required? YES | NO
- Current System State update required? YES | NO
- Fail-closed result: PASS | FAIL

HIRMOS may claim normal completion or close only when this section supports the claim. If `Fail-closed result` is `FAIL`, the next governed command must be a route-back, `hirmos status`, or another allowed command that resolves the blocker.

## 20. Contract Amendments

Use this section only when a governed continuation pass amends the active Session Contract. Amendments must be append-only and must identify affected scope, criteria, implementation units, unresolved items, evidence requirements, and downstream controls reset in `SESSION_EXECUTION.md`.

| Amendment ID | Trigger | Scope effect | Controls reset | Status |
|---|---|---|---|---|
| CA-01 | | | | NOT_APPLICABLE |
