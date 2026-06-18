# Implementation Readiness

Status: active-session Design readiness artifact.
Purpose: decide whether HIRMOS may move from Design to Implementation.

## Readiness Decision

- Status: READY | NEEDS_USER_DECISION | BLOCKED | NOT_APPLICABLE
- Decided at:
- Decided by stage/capability:

## Required Artifacts

| Artifact | Required? | Exists? | Non-placeholder? | Notes |
|---|---:|---:|---:|---|

At minimum, readiness normally requires:

- `support/system-state.md`;
- `DESIGN.md`;
- `unresolved-items.md` when unresolved items exist;
- `SESSION_CONTRACT.md`;
- delivery/phase/delivery-unit contract when required by project type;
- `support/technical-review.md` when technical assumptions/risks exist.

## Unresolved Item Gate

- Active gated items resolved? YES | NO | NOT_APPLICABLE
- Non-gating assumptions documented? YES | NO | NOT_APPLICABLE
- Technical-review items inspectable? YES | NO | NOT_APPLICABLE
- Carry-forward records ready? YES | NO | NOT_APPLICABLE

## Authorized Scope

Summarize exactly what Implementation is authorized to do.

## Not Authorized

Summarize what Implementation must not do.

## Evidence Criteria

List the evidence Implementation must produce.

## Technical Review Path

Point to reviewer-facing artifacts when applicable.

## Checkpoint Message Basis / Artifact-Backed Checkpoint

Record the artifacts that back any user-facing implementation-readiness checkpoint. Do not surface readiness until this section is backed by existing non-placeholder artifacts.

## Final Gate

Implementation Readiness is READY only when required execution controls are satisfied or explicitly not applicable, gated unresolved items are resolved, artifacts exist, and the Session Contract authorizes the work.

## Decision

State the final readiness decision and next allowed action.


## Runtime Integration Readiness Gate

Before Implementation readiness, verify material integration posture.

- `_hirmos/session/support/runtime-integration-readiness.md` exists when material integration areas exist:
- Current-session authorized posture is clear:
- Production-readiness blockers are classified:
- Domain Expert choices are deferred or surfaced according to interaction mode:
- Technical review path exists when needed:

Readiness decision impact:

```text
READY_FOR_IMPLEMENTATION
NEEDS_DOMAIN_EXPERT_DECISION
NEEDS_TECHNICAL_REVIEW
BLOCKED_BY_INTEGRATION_POSTURE
NOT_APPLICABLE
```

Do not claim implementation-readiness if a material integration posture decision blocks the active implementation scope.

## Vertical Slice Readiness

- Active Phase / Delivery Unit:
- Delivery Unit status before Implementation:
- Session Contract source:
- Why this slice is ready or blocked:
- Next command/action if ready:
- Next command/action if blocked:

Implementation readiness applies to the active slice only. Do not claim the full Delivery Plan is implementation-ready unless each required unit has been reviewed for readiness.

## Claim Reconciliation Readiness Gate

Before surfacing implementation-readiness, reconcile readiness claims.

| Readiness claim | Evidence status | Supporting artifact | Limitation | Result |
|---|---|---|---|---|

Implementation-readiness may be granted only for the scope and integration posture actually supported by Design, unresolved-item disposition, and evidence records.

## Autonomous Technical Progress Gate

Before Implementation begins, record whether safe technical progress is authorized.

- Attempt-before-ask rule applies: YES | NO | NOT_APPLICABLE
- Safe local technical progress authorized by Session Contract: YES | NO | NOT_APPLICABLE
- Technical defaults recorded in support/technical-review.md: YES | NO | NOT_APPLICABLE
- Domain Expert disclosure required before Implementation: YES | NO
- Technical Supervisor review required before Implementation: YES | NO
- Blockers that prevent safe progress:

Implementation readiness should not be blocked by routine technical setup questions when HIRMOS can safely discover or apply a default. It must be blocked when the next technical action is unsafe, destructive, credential/account-dependent, compliance-dependent, or outside scope.

## Local setup and role-workflow smoke evidence

Use `LOCAL_TECHNICAL_SETUP_AND_ROLE_WORKFLOW_SMOKE_CHECKS.md` for the governing rules when HIRMOS claims local runtime behavior, user-environment verification, or role workflow readiness.

Required artifacts when applicable:

- `_hirmos/session/support/local-runtime-evidence.md` records local environment, service, migration, seed, dev-server, and route evidence.
- `_hirmos/session/support/role-workflow-smoke.md` records patient/staff/provider/manager/admin workflow smoke evidence.
- `_hirmos/session/support/claim-reconciliation.md` reconciles whether the claim may be surfaced.

Firm rule: tests/build/lint alone do not prove local runtime readiness or role workflow readiness.
