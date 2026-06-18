# Runtime Integration Readiness

Template status: session artifact template.
Purpose: record material runtime integration posture and production-readiness recommendations for the active session.

## Artifact status

```text
status: draft | ready_for_review | blocked | accepted | not_applicable
lifecycle_stage: Design | Implementation | Update System State
last_updated:
```

## Scope

- User Request:
- Project type:
- Active stack / stack contexts:
- Session Contract:
- Delivery Unit / Phase, if applicable:

## Material Integration Areas

| Area | Applies? | Current posture | Authorized current-session posture | Production recommendation | Decision owner | Status |
|---|---:|---|---|---|---|---|
| Database / persistence | | | | | | |
| Auth / authorization | | | | | | |
| Messaging / email / SMS | | | | | | |
| File/object storage | | | | | | |
| Payments/billing | | | | | | |
| Background jobs / cron / queues | | | | | | |
| Deployment / environment / secrets | | | | | | |
| Observability / audit / backups | | | | | | |
| Other | | | | | | |

Allowed internal posture values:

```text
DEMO_FIXTURE
INTEGRATION_BOUNDARY
LOCAL_REAL_INTEGRATION
PRODUCTION_PROVIDER_INTEGRATION
BLOCKED_PENDING_DECISION_OR_CREDENTIALS
NOT_APPLICABLE
```

## Domain Expert Visibility

For each material area, classify what should be surfaced now:

| Area | Surface now? | Reason | Domain Expert wording | Technical review pointer |
|---|---:|---|---|---|

Do not surface low-level provider choices to Domain Expert users unless they affect domain behavior, risk, cost, compliance, ownership, implementation authorization, or release readiness.

## Recommended Production Options

For every material production integration area, record a primary recommendation.

### Area: <name>

- Current posture:
- HIRMOS primary recommendation:
- Rationale:
- Alternatives:
- When an engineer might choose an alternative:
- Required credentials/accounts/environment:
- Compliance/security/ownership notes:
- Production-readiness evidence required:
- Decision owner:
- Status:

## Current-Session Authorization

What Implementation may deliver in this session:

- Authorized current posture:
- Not authorized:
- Fixture/mock/fallback usage allowed?
- Boundary-only work allowed?
- Local real integration required?
- Production provider integration required?

## Blockers and Unresolved Items

| Item id | Area | Classification | Decision owner | Blocking scope | Required action |
|---|---|---|---|---|---|

## Evidence Requirements

For each material area, list required evidence before the active claim can be surfaced.

| Area | Claim level | Required evidence | Not sufficient by itself |
|---|---|---|---|

Examples:

- build success alone is not local runtime verification;
- adapter code alone is not provider integration;
- local database migration success is not production database readiness;
- console fallback is not message delivery.

## Production Readiness Checkpoint Basis

Use this section when a governed checkpoint will surface production-readiness options.

- Checkpoint id:
- Current implementation level summary:
- Recommendations ready to surface:
- Decisions required before production readiness:
- Technical reviewer path:
- Domain Expert summary:

## Update System State Carry-Forward

Record what future sessions must treat as accepted, assumed, blocked, or requiring production review.

- Accepted integration decisions:
- Carried technical assumptions:
- Production-readiness blockers:
- Evidence-only notes:
- Future-session recommended next action:

## Autonomous Integration Progress

Record what HIRMOS attempted before deferring each material integration.

| Area | Safe progress attempted? | Action taken | Resulting posture | Evidence | Remaining blocker |
|---|---:|---|---|---|---|

Use only canonical posture values from `RUNTIME_INTEGRATION_AND_PRODUCTION_READINESS.md`.

If HIRMOS did not attempt safe progress, explain why: out of scope, unsafe, destructive, credential-dependent, compliance-dependent, cost-bearing, unavailable environment, or not applicable.

## archive/session-state integrity Canonical Posture Enforcement

| Integration area | Canonical posture value | Noncanonical label encountered | Translation rationale | Evidence state |
|---|---|---|---|---|
| | DEMO_FIXTURE / INTEGRATION_BOUNDARY / LOCAL_REAL_INTEGRATION / PRODUCTION_PROVIDER_INTEGRATION / BLOCKED_PENDING_DECISION_OR_CREDENTIALS / NOT_APPLICABLE | none / value | | |

Firm rule: do not write `LOCAL_REAL`, `CODE_COMPLETE_DEFERRED`, `provider-ready`, or other shorthand as posture. Use canonical values only.

## Canonical Runtime Posture Scan

| Artifact inspected | Integration area | Noncanonical posture found | Canonical posture replacement | Evidence status | Pass / Blocked |
|---|---|---|---|---|---|
| | | none / value | DEMO_FIXTURE / INTEGRATION_BOUNDARY / LOCAL_REAL_INTEGRATION / PRODUCTION_PROVIDER_INTEGRATION / BLOCKED_PENDING_DECISION_OR_CREDENTIALS / NOT_APPLICABLE | | |

Invalid posture examples include `LOCAL_REAL`, `LOCAL_REAL + console fallback`, `provider-ready`, `code complete deferred`, and `production ready pending credentials`. Split combined statements into posture, evidence, and blocker fields.

Firm rule: do not carry noncanonical posture values into `support/system-state-update.md`, `CURRENT_SYSTEM_STATE.md`, or `support/close-checklist.md`.
