# Session Scope

Status: active-session Main Artifact.
Purpose: define the authorized outcome, scoped requirements, governing design decisions, implementation boundaries, production-shaped gate, acceptance criteria, and close verification basis for the current HIRMOS session.

This artifact is the active session scope and acceptance authority. Implementation may not begin until this scope exists, is non-placeholder, and the relevant execution controls in `SESSION_EXECUTION.md` are satisfied.

## 1. Session Identity

- Session ID:
- Session title:
- User request / command:
- Interaction mode:
- Session type: design-only | implementation | review | close/update-state | other
- Current lifecycle boundary:
- Current System State basis: `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md`
- Delivery shape:
- Status:

## 2. Source Inputs and Authority Basis

Identify every source this session scope must cover. Source inputs are evidence and focus signals until reconciled here.

| Source type | Artifact/path/source | Required? | Coverage obligation |
|---|---|---:|---|
| Current System State | `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md` | yes | Must be read before meaningful work and delivery pointers must be inspected. |
| User request | | yes | Must be reflected in authorized outcome, requirements, exclusions, and acceptance criteria. |
| Existing accepted-state artifacts | | conditional | Must be adopted when existing state constrains the session. |
| Delivery Scope | `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md` when applicable | conditional | Must be adopted and narrowed when this session belongs to a durable delivery. |
| Durable Phase | `_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md` when applicable | conditional | Must be adopted and narrowed when this session implements a durable phase. |
| Independent Requirements | `_hirmos/session/REQUIREMENTS.md` or delivery-level `REQUIREMENTS.md` when justified | conditional | Use only when separate requirements authority is justified. |
| Independent Design | `_hirmos/session/DESIGN.md` or delivery-level `DESIGN.md` when justified | conditional | Use only when separate design authority is justified. |
| Other | | | |

## 3. Authorized Outcome

Describe the outcome this session is authorized to produce. Keep this session-scoped; do not restate a whole product or delivery unless required for adoption.

- Intended user-visible outcome:
- Intended system-visible outcome:
- Accepted state / artifact outcome:
- Non-goals:

## 4. Scoped Requirements

List the functional, non-functional, and constraint requirements needed to govern this session. Requirement IDs are optional for small/simple work and required when traceability is material.

| ID | Scoped requirement | Source authority | Acceptance evidence required | Status |
|---|---|---|---|---|
| SR-01 | | | | PENDING |

### Explicit exclusions

| ID | Excluded item | Reason | Future path, if any |
|---|---|---|---|
| EX-01 | | | |

### Brownfield preservation rules

Record what existing behavior, files, APIs, data, UX, tests, runtime behavior, artifacts, or framework contracts must not regress.

| ID | Preservation requirement | Affected area | Evidence required |
|---|---|---|---|
| PR-01 | | | |

## 5. Design and Implementation Decisions

Record only design decisions required to authorize this session. Create separate `DESIGN.md` only when design authority needs independent durable review.

| Decision ID | Decision area | Governing decision | Rationale / current-state basis | Evidence required | Status |
|---|---|---|---|---|---|
| SD-01 | Architecture | | | | PENDING |
| SD-02 | Stack / framework | | | | PENDING |
| SD-03 | Data / persistence | | | | PENDING |
| SD-04 | Runtime / integration | | | | PENDING |
| SD-05 | Provider / external service | | | | PENDING |
| SD-06 | Security / privacy | | | | PENDING |

Decisions deferred to unresolved-items.md:

- Gated:
- Non-gating:
- Technical-review:

## 6. Delivery Shape Decision

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
- If `MULTI_SESSION_DELIVERY`, required Delivery Plan: `_hirmos/system/delivery/DELIVERY_PLAN.md` and delivery scope: `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md`
- If `MULTI_SESSION_DELIVERY_WITH_PHASE_FILES`, required Delivery Plan, delivery scope, and active phase path: `_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md`
- Current System State delivery pointer basis: `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md` Active Development Context and Delivery Pointers
- Pointer consistency result: CONSISTENT | BLOCKED | NOT_APPLICABLE
- If UNCERTAIN, what must be inspected before deciding?

Fail-closed rule:

- `UNCERTAIN` blocks implementation readiness.
- `SINGLE_SESSION_VERTICAL_SLICE` requires affirmative bounded-scope safety evidence.
- `SINGLE_SESSION_WITH_IMPLEMENTATION_UNITS` requires implementation units that collectively cover authorized scope.
- `MULTI_SESSION_DELIVERY` requires a durable Delivery Plan and Delivery Scope before implementation authorization.
- `MULTI_SESSION_DELIVERY_WITH_PHASE_FILES` requires a durable Delivery Plan, Delivery Scope, and adopted phase file before implementation authorization.
- The selected shape must be the smallest shape that preserves engineering quality, implementation truth, validation, continuity, and accepted-state integrity.

## 7. Production-Shaped Engineering Gate

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

## 8. Delivery / Phase Capability Routing Evidence and Adoption

Required when the selected delivery shape is `MULTI_SESSION_DELIVERY` or `MULTI_SESSION_DELIVERY_WITH_PHASE_FILES`.

| Capability | Required output | Path / evidence | Status |
|---|---|---|---|
| delivery-design | Durable Delivery Plan / register | `_hirmos/system/delivery/DELIVERY_PLAN.md` | |
| delivery-scope | Durable Delivery Scope | `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md` | |
| phase-contracting | Durable phase file when phase files are selected | `_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md` | |
| session-scope | Active Session Scope adoption | `_hirmos/session/SESSION_SCOPE.md` | |
| implementation-readiness | Readiness gate | `_hirmos/session/SESSION_SCOPE.md` and optional `DESIGN.md` only when justified | |

### Active Durable Phase Adoption

Required when the selected delivery shape is `MULTI_SESSION_DELIVERY_WITH_PHASE_FILES` and the session is implementation-capable.

- Adoption status: ADOPTED | NOT_APPLICABLE | BLOCKED
- Delivery ID:
- Delivery Plan path: `_hirmos/system/delivery/DELIVERY_PLAN.md`
- Delivery Scope path: `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md`
- Active Phase ID:
- Active Phase path: `_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md`
- Current System State active phase pointer:
- Phase source status: NOT_STARTED | ACTIVE | BLOCKED | ACCEPTED | SUPERSEDED | UNKNOWN
- Adoption mode: FULL_PHASE | EXPLICIT_PARTIAL_WITH_DEFERRED_ITEMS | DESIGN_ONLY_NO_IMPLEMENTATION
- Implementation authorized from adopted phase? YES | NO

#### Adopted phase scope

| Phase item ID | Phase contract text / summary | Adopted into Session Scope item(s) | Implementation unit(s) | Status |
|---|---|---|---|---|
| PH-ITEM-01 | | SR-01 | IU-01 | PENDING |

#### Phase exclusions / deferrals

| Phase item ID | Excluded / deferred / blocked reason | Future phase/session path | User approval / evidence |
|---|---|---|---|
| | | | |

#### Durable phase adoption coverage question

Does `SESSION_SCOPE.md` adopt exactly one active durable `PHASE-xx.md` and cover the intended phase scope without silent omissions?

- Answer: YES | NO | PARTIAL | NOT_APPLICABLE
- Evidence:
- Gaps:
- Deferred / blocked items:
- Fail-closed result: PASS | FAIL | NOT_ASSESSED

Fail-closed rule: delivery-governed implementation is not authorized when this adoption section is missing, `BLOCKED`, `NOT_ASSESSED`, references more than one active phase, contradicts Current System State delivery pointers, or fails to map adopted phase items to authorized Session Scope items.


### Phase Entry Gate Evidence

Required when a durable phase is adopted.

- Phase Entry Gate status: PASS / BLOCKED / UNCERTAIN / NOT_APPLICABLE
- Evidence:
- Implementation readiness impact:

### Phase Progress and Carry-Forward Control

Required when a durable phase is adopted or closed.

- Previous Phase Progress Ledger inspected: YES / NO / NOT_APPLICABLE
- Carry-forward required if not accepted: YES / NO / NOT_APPLICABLE
- Carry-forward evidence:

### Phase Acceptance Control

Required when this session claims phase completion or updates phase status.

- Phase acceptance will be evaluated through Phase Acceptance Evidence Gate.
- Evidence:
- Phase status update required: YES / NO / NOT_APPLICABLE

## 9. Autonomous Technical Progress Authorization

- Is safe local/default technical progress authorized before asking? YES | NO | LIMITED
- Authorized technical defaults:
- Decision recording requirement:
- User approval required before:

## 10. Implementation Shape

Implementation units are required when implementation is non-trivial, multi-file, risky, or delegated to an implementation agent. Unit files live under `_hirmos/session/implementation-units/`.

| Unit ID | Unit artifact | Purpose | Scope coverage | Dependencies | Status |
|---|---|---|---|---|---|
| IU-01 | `_hirmos/session/implementation-units/IU-01.md` | | | | planned |

### Required implementation-unit coverage question

Do all planned implementation units collectively cover 100% of `SESSION_SCOPE.md`?

- Answer: YES | NO | PARTIAL | NOT_APPLICABLE
- Evidence:
- Gaps:
- Deferred items:

## 11. Unresolved Items Control

Authoritative register: `_hirmos/session/unresolved-items.md`

This section is only a control summary. It is not sufficient for review, implementation, continuation, or close. HIRMOS must read and apply `_hirmos/session/unresolved-items.md` directly before every lifecycle boundary.

HIRMOS must not infer unresolved-item details from this summary. This summary must not contain item-level detail rows; material `GATED`, `NON_GATING`, and technical-review items belong in `_hirmos/session/unresolved-items.md`.

Summary:

- Gated unresolved items:
- Non-gating assumptions/items:
- Technical-review items:
- Resolved items this session:
- Last direct register review boundary:
- Blocking status: BLOCKED | NOT_BLOCKED

Boundary rule:

- If any gated item is unresolved, HIRMOS must fail closed and may not proceed to Implementation or close.
- `NON_GATING` items are still governed decisions/assumptions and must not be hidden or discarded.
- If a non-gating item materially affects acceptance, evidence, implementation quality, or future work, it must be represented in accepted-state carry-forward or decision records at close.

## 12. Required Evidence

List required validation and the allowed evidence posture.

| Validation ID | Command/check/review | Required? | Evidence required | If not run, required rationale |
|---|---|---:|---|---|
| VAL-01 | | | | |

Evidence destination:

- `_hirmos/session/EVIDENCE.md` when command/runtime/claim/close evidence is material.
- `_hirmos/session/implementation-units/IU-xx.md` when evidence belongs to a specific implementation unit.
- `SESSION_EXECUTION.md` for execution ledger entries and continuation-state summaries, not as a substitute for material evidence.

## 13. Acceptance Criteria

Use binary or explicitly inspectable criteria. Avoid vague criteria.

| Criterion ID | Criterion | Evidence required | Pass/Fail basis | Status |
|---|---|---|---|---|
| AC-01 | | | | PENDING |

## 14. Scope Amendments

Record every scope change after initial session scope approval.

| Amendment ID | Trigger | Change | User approval / evidence | Impact on criteria |
|---|---|---|---|---|
| AM-01 | | | | |

## 15. Session Satisfaction Review and Close Verification

This section must be completed before any `hirmos close` success claim.

### Promised work register

| Promise ID | Promise / scoped requirement / gate | Source section | Required evidence | Status |
|---|---|---|---|---|
| P-01 | | | | PENDING |

### Verified work register

| Verification ID | Verified result | Evidence path / command / observation | Claim supported | Confidence |
|---|---|---|---|---|
| V-01 | | | | |

### Promised vs verified coverage matrix

| Promise ID | Fully verified? | Evidence | Gap / caveat | Required carry-forward |
|---|---|---|---|---|
| P-01 | YES | | | |

Does the actual completed work satisfy 100% of `SESSION_SCOPE.md`?

- Answer: YES | NO | PARTIAL
- Evidence:
- Gaps:
- User-visible caveats:
- Accepted-state impact:
- Carry-forward required:
- Fail-closed result: PASS | FAIL

### Close verdict

- Verdict: ACCEPTED | PARTIAL | BLOCKED | FAILED
- Rationale:
- Accepted-state files updated:
- Archive path:
- Remaining obligations:
