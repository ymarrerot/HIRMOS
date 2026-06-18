# Session Contract Review

Status: active-session governed review artifact.
Purpose: provide fast-access, mandatory promised-vs-verified review for the active Session Contract.

Authoritative contract: `_hirmos/session/SESSION_CONTRACT.md`
Unresolved-item register: `_hirmos/session/unresolved-items.md`
Implementation units: `_hirmos/session/implementation-units/`
Execution spine: `_hirmos/session/SESSION_EXECUTION.md`

This artifact is the governed review surface for session close and implementation-completion claims. It does not define session scope. Scope remains in `SESSION_CONTRACT.md`.

## 1. Review Identity

- Session ID:
- Review boundary: implementation-complete | close-readiness | close | other
- Reviewer / agent:
- Review timestamp:
- Related checkpoint, if any:

## 2. Required Inputs Directly Reviewed

| Input | Path / evidence | Directly reviewed? | Notes |
|---|---|---:|---|
| Session Contract | `_hirmos/session/SESSION_CONTRACT.md` | NO | |
| Unresolved Items | `_hirmos/session/unresolved-items.md` | NO | |
| Session Execution | `_hirmos/session/SESSION_EXECUTION.md` | NO | |
| Implementation Units | `_hirmos/session/implementation-units/` | NOT_APPLICABLE | |
| Validation / evidence appendices | `_hirmos/session/support/` | NOT_APPLICABLE | |
| Current System State | `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md` | NO | |

Allowed reviewed values: `YES`, `NO`, `NOT_APPLICABLE`.

Fail-closed rule: if a required input is marked `NO`, HIRMOS must not claim implementation completion, close readiness, or close success.

## 3. Promised Work Register

List every material promise from `SESSION_CONTRACT.md` Authorized Scope, Completion Criteria, Validation Requirements, and Implementation Unit Plan.

| Promise ID | Promised work / criterion | Source section in `SESSION_CONTRACT.md` | Required evidence | Status |
|---|---|---|---|---|
| SCR-P01 | | | | NOT_VERIFIED |

Allowed statuses: `VERIFIED`, `PARTIAL`, `NOT_VERIFIED`, `DEFERRED_ACCEPTED`, `OUT_OF_SCOPE`, `BLOCKED`.

## 4. Verified Work Register

| Evidence ID | Evidence source | What it verifies | Result | Limitations |
|---|---|---|---|---|
| SCR-E01 | | | | |

Evidence must be concrete: command output, file/path inspection, implementation-unit review, runtime smoke, or explicit user decision.

## 5. Promised vs Verified Coverage Matrix

| Promise ID | Covered by implementation unit(s) | Covered by evidence ID(s) | Coverage status | Gap / deferred item |
|---|---|---|---|---|
| SCR-P01 | | | NOT_VERIFIED | |

Allowed coverage statuses: `FULL`, `PARTIAL`, `NONE`, `DEFERRED_ACCEPTED`, `OUT_OF_SCOPE`, `BLOCKED`.

## 6. Unresolved Items Reconciliation Check

This check must be based on direct review of `_hirmos/session/unresolved-items.md`. Do not infer unresolved-item status from `SESSION_CONTRACT.md` summaries.

| Check | Result | Evidence / notes |
|---|---|---|
| Direct register reviewed | NO | |
| Active gated items blocking this boundary | UNKNOWN | |
| Non-gating assumptions applied or carried | UNKNOWN | |
| Resolved items include disposition history | UNKNOWN | |
| Carry-forward candidates identified | UNKNOWN | |

Allowed results: `YES`, `NO`, `NONE`, `UNKNOWN`, `NOT_APPLICABLE`.

## 7. Coverage Verdict

The coverage verdict must be based on the promised-vs-verified matrix, not on narrative confidence.

## 8. Required Coverage Questions

### Session contract coverage by implementation units

Do all implementation units combined satisfy 100% of `SESSION_CONTRACT.md`?

- Answer: YES | NO | PARTIAL | NOT_APPLICABLE
- Evidence:
- Gaps:
- Deferred items:

### Actual implementation coverage

Does the actual completed work satisfy 100% of `SESSION_CONTRACT.md`?

- Answer: YES | NO | PARTIAL
- Evidence:
- Gaps:
- Deferred items:

### Validation coverage

Were all required validation checks in `SESSION_CONTRACT.md` run or explicitly justified as not run / not applicable?

- Answer: YES | NO | PARTIAL
- Evidence:
- Not-run rationale:

## 9. Final Review Verdict

- Verdict: COMPLETE | PARTIAL | FAILED | BLOCKED
- Rationale:
- Required close action:
- Carry-forward required? YES | NO
- Current System State update required? YES | NO

## 10. Fail-Closed Decision

HIRMOS may claim normal completion or close only if:

- Required inputs were directly reviewed.
- There are no unresolved gated blockers.
- The actual implementation coverage answer is `YES`, or every gap is explicitly deferred, carried forward, rejected as out of scope, or blocked by a documented unresolved item.
- Validation gaps are explicitly recorded with rationale.
- The final verdict is `COMPLETE`, or the user explicitly accepts a non-complete close posture.

Fail-closed result: PASS | FAIL

If `FAIL`, the next governed command must be a route-back, `hirmos status`, or another allowed command that resolves the blocker. HIRMOS must not claim normal close.


## Delivery Governance Classification Review


## Durable Phase Adoption Review

Required when Delivery-Need Classification is `YES`.

- Was exactly one durable phase adopted by `SESSION_CONTRACT.md`? YES | NO | NOT_APPLICABLE
- Adopted Delivery Plan path:
- Adopted Phase path:
- Did the adopted phase match Current System State delivery pointers? YES | NO | NOT_APPLICABLE
- Did verified work satisfy the adopted phase scope for this session? YES | NO | PARTIAL | NOT_APPLICABLE
- Were partial / deferred / blocked phase items explicitly recorded? YES | NO | NOT_APPLICABLE
- Did the review inspect the durable `PHASE-xx.md` directly? YES | NO | NOT_APPLICABLE

| Adopted phase item | Promised in Session Contract | Verified evidence | Result | Gap / deferral |
|---|---|---|---|---|
| | | | NOT_ASSESSED | |

Fail-closed rule: if delivery governance is active and this review cannot prove one adopted phase, direct phase inspection, and promised-vs-verified phase coverage, the final review verdict must not be `COMPLETE`.


Does the Delivery Governance Classification correctly prevent unsafe single-session scope?
Answer: YES | NO | PARTIAL | NOT_APPLICABLE

- Classification answer reviewed: YES | NO | UNCERTAIN | NOT_FOUND
- Evidence reviewed:
- Delivery Plan triggers considered:
- Single-session safety justification adequate? YES | NO | NOT_APPLICABLE
- Required durable Delivery Plan exists when classification is YES? YES | NO | NOT_APPLICABLE
- Required phase file exists when classification is YES? YES | NO | NOT_APPLICABLE
- Required correction:

Fail-closed rule: if this answer is `NO` or `PARTIAL`, or if classification is `UNCERTAIN` at implementation readiness, HIRMOS must block implementation completion and close readiness until corrected.


## Close-Time Delivery Status Review

Required when delivery governance was active.

| Review question | Answer | Evidence |
|---|---|---|
| Does the adopted Phase status match verified work and unresolved-item disposition? | YES / NO / NOT_APPLICABLE | |
| Does the parent Delivery Plan phase row need to change? | YES / NO / NOT_APPLICABLE | |
| Are Current System State delivery pointers ready to be refreshed? | YES / NO / NOT_APPLICABLE | |
| Are carry-forward delivery obligations recorded for future sessions? | YES / NO / NOT_APPLICABLE | |

The final review verdict must not be `PASS` for delivery-governed close if the Delivery Plan, Phase file, or Current System State delivery pointers remain stale or contradictory.

## Phase Entry Gate Review

Review whether the session correctly adopted the durable phase only after satisfying the Phase Entry Gate.

Review questions:

```text
Was the durable PHASE-xx.md read directly?
Was the Phase Entry Gate status PASS?
Did lifecycle status support adoption?
Did phase type support implementation?
Were greenfield controls satisfied when required?
Were brownfield controls satisfied when required?
Were pointer concordance and open blockers checked?
```

If any required check is missing, the review verdict must block implementation or close acceptance.

## Phase Progress / Carry-Forward Review

Required for delivery-governed sessions before normal close.

| Review question | Answer | Evidence / pointer |
|---|---|---|
| Did the session update or verify the durable Phase Progress Ledger? | YES / NO / NOT_APPLICABLE | |
| Were completed, partial, blocked, and deferred items classified? | YES / NO / NOT_APPLICABLE | |
| If phase outcome is not ACCEPTED, are carry-forward obligations recorded? | YES / NO / NOT_APPLICABLE | |
| Do Current System State delivery pointers match the resulting active/next phase? | YES / NO / NOT_APPLICABLE | |

Fail-closed rule: if the phase is `PARTIAL`, `BLOCKED`, or `DEFERRED`, the review cannot pass without recorded carry-forward obligations.


## Phase Acceptance Review

- Phase acceptance verdict: ACCEPTED / PARTIAL / BLOCKED / FAILED / NOT_REVIEWED
- Phase acceptance evidence status: COMPLETE / INCOMPLETE / BLOCKED / NOT_APPLICABLE
- All adopted Session Contract items satisfied or explicitly deferred/excluded: yes / no / not_applicable
- All implementation units reviewed: yes / no / not_applicable
- Unresolved adopted work remaining: yes / no / not_applicable
- Greenfield acceptance evidence complete when applicable: yes / no / not_applicable
- Brownfield acceptance evidence complete when applicable: yes / no / not_applicable
- Acceptance decision can update durable phase to ACCEPTED: yes / no / not_applicable
