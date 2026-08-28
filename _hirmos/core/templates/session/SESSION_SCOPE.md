# Session Scope

Status: active-session Main Artifact.
Purpose: Own the accepted session boundary, scope, exclusions, evidence requirements, and compact IU planning pointers.

Canonical owner: active session scope authority.

This artifact owns what the current session is allowed to accomplish, what is excluded, what evidence is required, and which downstream authority artifacts must be created before implementation. It does not own bootstrap answers, implementation-unit contracts, execution evidence detail, carry-forward detail, delivery close posture, or accepted-state truth.

## Governance Compatibility Markers / Ownership Summary

This file remains the complete active session authority for accepted session scope, exclusions, evidence obligations, optional authority adoption, and close verification.

Optional `REQUIREMENTS.md` and `DESIGN.md` may provide detailed requirement/design authority only when this file explicitly adopts them.

- Adopted requirements / sections:
- Adopted design decisions / sections:

Delivery shape must be justified by the real software work.

- Technically possible simpler shape:
- If multi-session is selected, smallest honest phase count:
- the parent delivery must justify the selected phase count as the smallest honest count

Governance posture: this preview is not implementation authority.

Full IU authority belongs in `_hirmos/session/implementation-units/IU-xx.md`.

Detailed user instructions are scope input, not implementation authorization. `hirmos start` must leave this scope under baseline review; it must not self-accept the scope or authorize material project/source edits.


## 1. Session Identity

- Session ID:
- Command / user request:
- Session type:
- Delivery ID, if applicable:
- Phase ID, if applicable:
- Created:
- Last updated:
- Scope status: DRAFT | UNDER_BASELINE_REVIEW | ACCEPTED | AMENDED | BLOCKED | CLOSED

## 2. Source Inputs and Authority Basis

List only durable inputs used to define this scope. Do not rely on chat memory alone.

| Source | Path / reference | Adopted? | Notes |
|---|---|---:|---|
| User request | | YES / NO | |
| Current system state | `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md` | YES / NO | |
| Delivery scope | `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md` | YES / NO / N/A | |
| Phase file | `_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md` | YES / NO / N/A | |
| Requirements detail | `_hirmos/session/REQUIREMENTS.md` | YES / NO / N/A | |
| Design detail | `_hirmos/session/DESIGN.md` | YES / NO / N/A | |

### Optional authority artifact justification and adoption

Optional session `REQUIREMENTS.md` or `DESIGN.md` files are subordinate detail authorities only when explicitly adopted here.

| Optional artifact | Created? | Adopted into scope? | Why needed | Scope sections covered |
|---|---:|---:|---|---|
| REQUIREMENTS.md | YES / NO | YES / NO | | |
| DESIGN.md | YES / NO | YES / NO | | |

## 3. Authorized Scope / Outcome

State the bounded result this session is authorized to produce.

- Authorized outcome:
- Success posture: ACCEPTED | PARTIAL | BLOCKED | FAILED
- User-visible output expected:
- Project-file mutation authorized before baseline acceptance: NO
- Baseline acceptance authority recorded: YES / NO / PENDING
- Material project/source edit authorization: NOT_AUTHORIZED | AUTHORIZED_WITHOUT_IU | REQUIRES_IU_EXECUTION_AUTHORIZATION | BLOCKED

## 4. Scoped Requirements

| Requirement ID | Requirement / obligation | Source | In scope? | Evidence required |
|---|---|---|---:|---|
| REQ-01 | | | YES / NO | |

### Explicit exclusions

| Exclusion ID | Out-of-scope item | Reason | Carry-forward / delivery pointer |
|---|---|---|---|
| EX-01 | | | |

### Existing-system preservation rules

| Rule ID | Existing behavior / file / invariant to preserve | Evidence / check |
|---|---|---|
| PRES-01 | | |

## 5. Design and Implementation Decisions

Record only decisions that define scope boundaries or implementation permission. Detailed design belongs in `DESIGN.md` when adopted.

| Decision ID | Decision | Reason | Source / approval | Reversible? |
|---|---|---|---|---|
| DEC-01 | | | | YES / NO |

## 6. Delivery Shape Decision

### Current System State delivery pointer basis

- Next recommended delivery:
- Pointer consistency result: PASS | FAIL | BLOCKED | NOT_APPLICABLE


Recommended delivery shape:

- smallest sufficient governed delivery shape:
- Shape: SINGLE_SESSION | SINGLE_SESSION_WITH_IMPLEMENTATION_UNITS | MULTI_SESSION_DELIVERY | MULTI_SESSION_DELIVERY_WITH_PHASE_FILES
- Session focus:
- Simpler shape considered:
- Why simpler shape is acceptable or insufficient:
- Selected shape justification:
- Why selected shape is necessary for this real software work:
- User interaction / token-cost impact:
- Risk if compressed into a smaller shape:

When multi-session delivery is selected, include phase-count honesty:

- Phase count considered:
  - 2 phases: accepted/rejected because...
  - 3 phases: accepted/rejected because...
  - 4+ phases: accepted/rejected because...
- Selected phase count:
- Why this count is the smallest honest count:
- Phase merge pressure result:
- Cost / interaction impact:
- Risk if compressed further:

Phase merge pressure check: every proposed phase after phase 2 must answer whether it can be merged into an earlier or later phase without losing honest validation, reviewability, continuity, or accepted-state integrity. If YES, merge it. If NO, explain the material boundary that requires keeping it separate.

## 7. Production-Shaped Engineering Gate

- Runtime / provider / DB / deployment boundary involved: YES / NO
- Production-shaped risk level: LOW | MEDIUM | HIGH
- Local-only evidence sufficient for this session? YES / NO / PARTIAL
- Runtime/provider evidence required before close:
- Production evidence explicitly not claimed:

### Automated Testing Posture

Required for implementation-capable software sessions; use `NOT_APPLICABLE` for non-software or genuinely non-testable work. Detailed per-IU obligations belong in `implementation-units/IU-xx.md` when IU mode applies.

- Software behavior in scope: YES | NO | PARTIAL
- Existing repository test architecture / commands:
- Unit-test posture: REQUIRED | NOT_APPLICABLE | COVERED_ELSEWHERE
- New or materially changed isolated deterministic logic expected: YES | NO | UNKNOWN
- Material behaviors requiring unit tests / isolated automated tests:
- Relevant existing tests / targeted baseline:
- Reproducible defect regression test expected: YES | NO | NOT_APPLICABLE
- Other required test layers:
- If `NOT_APPLICABLE` or `COVERED_ELSEWHERE`, rationale:
- Repository coverage policy, if any:

HIRMOS does not impose a universal coverage percentage. Existing valid behavioral tests remain protected behavioral evidence unless the governed behavior changes or the test is demonstrably invalid.

## 8. Focus-Aware Capability Routing Evidence and Adoption

- Active command:
- Selected focus: delivery-baseline | phase-baseline | session-scope | implementation-readiness | other
- Capability routing used:
- Why this capability is sufficient:
- Why heavier routing is not needed:
- Artifact paths read:
- Artifact paths created / updated:

### Active Durable Phase Adoption

Does `SESSION_SCOPE.md` adopt exactly one active durable `PHASE-xx.md`? YES | NO | NOT_APPLICABLE


Required only when this session narrows an active durable phase.

- Delivery ID:
- Phase ID:
- Phase status before session:
- Phase status update required: YES / NO / NOT_APPLICABLE

#### Adopted phase scope

| Phase item | Adopted into session? | Session requirement / criterion | Deferred? |
|---|---:|---|---:|
| | YES / NO | | YES / NO |

#### Phase exclusions / deferrals

| Phase item | Reason not in this session | Destination |
|---|---|---|
| | | |

#### Durable phase adoption coverage question

Does this session cover the intended phase slice honestly?

- Answer: YES | NO | PARTIAL | NOT_APPLICABLE
- Evidence:
- Gaps:

### Phase Entry Gate Evidence

- Entry criteria status:
- Blocking unresolved items:
- Required prior evidence:
- Phase Entry Gate status: PASS / BLOCKED / UNCERTAIN / NOT_APPLICABLE
- Entry decision: PASS | FAIL | BLOCKED | NOT_APPLICABLE

### Phase Progress and Carry-Forward Control

- Previous Phase Progress Pointer Index inspected: YES / NO / NOT_APPLICABLE
- Phase progress expected from this session:
- Carry-forward candidates allowed only after close-time triage: YES
- Carry-forward required if not accepted: YES / NO / NOT_APPLICABLE

### Phase Acceptance Control

- Phase acceptance will be evaluated through Phase Acceptance Evidence Gate: YES / NO / NOT_APPLICABLE
- Phase acceptance may be claimed by this session: YES / NO
- Required evidence before phase acceptance:
- Phase status update target:

## 9. Autonomous Technical Progress Authorization

- Is safe local/default technical progress authorized before asking? YES | NO | LIMITED
- Authorized technical defaults:
- Decision recording requirement:
- User approval required before:

## 10. Implementation Boundary and IU Planning Pointers

Legacy marker: Implementation Shape Preview.

Governance posture: Implementation Shape Preview is not execution authority. HIRMOS must not implement from this section and later reconstruct IU artifacts as compliance evidence.

This section exists only to decide whether implementation units are required and to provide compact planning pointers for the user. It must not contain detailed IU contracts, full acceptance criteria per IU, execution steps, sealed-contract language, or implementation-ready task tables. Detailed implementation-unit planning belongs only in `_hirmos/session/implementation-units/IU-xx.md` after scope acceptance/amendment.

- Implementation units required: YES | NO | TO_BE_DETERMINED_AFTER_SCOPE_ACCEPTANCE
- Reason:
- Expected implementation areas, one line each:
  - AREA-01:
- Planned IU pointers, if known before acceptance:

| Planned IU ID | One-line objective | Scope item IDs covered | Full IU file path after acceptance | Status |
|---|---|---|---|---|
| IU-01 | | REQ-01 / AC-01 | `_hirmos/session/implementation-units/IU-01.md` | PLANNED_ONLY |

Boundary rule:

- `SESSION_SCOPE.md` may identify planned IU IDs, one-line objectives, scope item IDs, and future file paths.
- `SESSION_SCOPE.md` must not define IU contract detail or execution authority.
- Full implementation-unit artifacts must not be created until the session scope baseline is accepted or amended.
- Accepted baseline authority is required before any material project/source edit.
- Material implementation may not begin until full IU artifacts exist, are non-placeholder, active generated-artifact validation passes, and the `SESSION_LEDGER.md` IU gate records `IU_EXECUTION_AUTHORIZED` after IU plan review when IU mode applies.

### Required implementation-unit coverage question

Before acceptance:

- Are implementation units required for safe execution? YES | NO
- Is a compact planned-IU pointer list sufficient for baseline review? YES | NO
- If NO, why must the user review more detail before acceptance?

After acceptance/amendment:

Do instantiated implementation units collectively cover 100% of accepted `SESSION_SCOPE.md` implementation scope?

- Answer: YES | NO | PARTIAL | NOT_APPLICABLE
- Evidence pointer: `_hirmos/session/SESSION_LEDGER.md` IU Set Coverage Map and `_hirmos/session/implementation-units/IU-*.md`
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
- `SESSION_LEDGER.md` for execution ledger entries and continuation-state summaries, not as a substitute for material evidence.

## 13. Acceptance Criteria

Use binary or explicitly inspectable criteria. Avoid vague criteria.

| Criterion ID | Criterion | Evidence required | Pass/Fail basis | Status |
|---|---|---|---|---|
| AC-01 | | | | PENDING |

## 14. Scope Amendments

Record every scope change after initial session scope approval. Reuse this section for continuation authority deltas; do not create a separate amendment artifact.

Update this section only when a later `hirmos continue` changes accepted authority: scope promises, exclusions, implementation-unit objectives, acceptance criteria, required validation, unresolved-item disposition, or close-satisfaction criteria. Same-scope corrections that do not change accepted authority belong in `SESSION_LEDGER.md`, affected IU records, unresolved-items, and evidence instead.

| Amendment ID | Trigger / continue pass | Change | User approval / evidence | Impact on criteria / validation / close satisfaction | Ledger pointer |
|---|---|---|---|---|---|
| AM-01 | | | | | |

## 15. Session Satisfaction Review and Close Verification

Close must evaluate satisfaction against `SESSION_SCOPE.md` first. If `SESSION_SCOPE.md` adopts `REQUIREMENTS.md` or `DESIGN.md`, those adopted items are evaluated as part of `SESSION_SCOPE.md` satisfaction.

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

| Promise ID | Fully verified? | Evidence | Gap / caveat | Carry-forward candidate? | Close-time triage disposition |
|---|---|---|---|---|---|
| P-01 | YES | | | YES / NO | AUTO_RESOLVED_NOW / USER_RESOLVED_NOW / APPROVED_CARRY_FORWARD / BLOCKING_UNRESOLVED / NO_LONGER_APPLIES / NOT_APPLICABLE |

Does the actual completed work satisfy 100% of `SESSION_SCOPE.md`?

- Answer: YES | NO | PARTIAL
- Evidence:
- Gaps:
- User-visible caveats:
- Accepted-state impact:
- Carry-forward candidate review completed: YES / NO
- Approved carry-forward required after triage: YES / NO
- Fail-closed result: PASS | FAIL

### Close verdict

- Verdict: ACCEPTED | PARTIAL | BLOCKED | FAILED
- Rationale:
- Accepted-state files updated:
- Archive path:
- Remaining obligations:

## Delivery-Governed Adoption

Required when delivery shape is `MULTI_SESSION_DELIVERY` or `MULTI_SESSION_DELIVERY_WITH_PHASE_FILES`.

- Delivery roadmap: `_hirmos/system/delivery/DELIVERY_PLAN.md`
- Delivery scope: `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md`
- Active phase: `_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md` or `NOT_APPLICABLE`
- Adopted delivery outcome:
- Adopted delivery requirements:
- Adopted delivery design/engineering decisions:
- Session narrowing decision:
- Out-of-scope delivery items preserved for later:

Fail-closed rule: a delivery-governed session must not proceed to implementation unless the Session Scope adopts and narrows the governing `DELIVERY_SCOPE.md` and, when applicable, the selected `PHASE-xx.md`.

## Implementation Shape Preview Reconciliation

This section is retained only as a boundary/reconciliation marker. It must not contain preview-to-IU detail rows that duplicate IU authority.

- Reconciliation owner: `_hirmos/session/SESSION_LEDGER.md` IU Set Coverage Map.
- Contract owner: `_hirmos/session/implementation-units/IU-*.md`.
- Scope owner: this `SESSION_SCOPE.md`.
- Result: PENDING | SATISFIED | PARTIAL | BLOCKED | NOT_APPLICABLE
- Notes:

A planned-IU pointer in `SESSION_SCOPE.md` must not be treated as implementation authority. After IU records exist, reconciliation is satisfied only through the ledger coverage map and the actual IU files.

## PROD-L8.21 Session-to-IU Coverage Requirement

When the selected implementation shape uses implementation units, `SESSION_SCOPE.md` must identify adopted implementation scope items clearly enough for the IU Set Coverage Map in `SESSION_LEDGER.md` to prove coverage before material edits.

Implementation Shape Preview is not execution authority. Execution authority begins only after accepted session scope plus complete IU Set Authority Checkpoint.

SESSION_SCOPE may contain only compact IU planning pointers: planned IU ID, one-line objective, covered scope item IDs, and expected IU file path. It must not contain full IU contracts, binary acceptance detail per IU, execution steps, or sealed-contract authority.

## PROD-L8.31 Planned IU Count Gate

When implementation units are required or planned, record a concrete expected count before implementation:

- IU mode / IU planned: YES / NO / LIGHTWEIGHT_NO_IU
- Planned IU count:
- Planned IU files:
- Scope items covered by planned IUs: scope item IDs only; no IU contract details here.
- Implementation may begin before full IU artifacts exist: NO, unless `LIGHTWEIGHT_NO_IU` was declared before edits.

The planned IU count must match actual full `IU-xx.md` files before material implementation begins. If the count is unknown, implementation is not authorized.

## PROD-L8.32L Optional Artifact Applicability Rule

Session scope may name optional artifacts only as applicability decisions or expected future paths. It must not require empty placeholder artifacts. Session-level `REQUIREMENTS.md`, `DESIGN.md`, `EVIDENCE.md`, `unresolved-items.md`, and IU files are created just in time when their owning concern becomes active and applicable.

For each optional artifact named here, record one of: `created now`, `expected future path`, `not created because not applicable`, or `blocked pending decision`. Do not leave blank placeholder paths that future runs may mistake for active authority.


## PROD-L8.33A Continue Implementation Gate

- `hirmos continue` implementation authority: classify and gate before coding.
- IU required/requested decision: PENDING / REQUIRED / NOT_REQUIRED.
- IU plan status: NOT_APPLICABLE / PENDING / READY_FOR_REVIEW / ACCEPTED.
- No-IU rationale, if applicable: PENDING until recorded before material project/source edits.
- Material project/source edit authority: BLOCKED until accepted baseline authority exists and, when IU mode applies, `IU_EXECUTION_AUTHORIZED` is recorded after IU plan review.
