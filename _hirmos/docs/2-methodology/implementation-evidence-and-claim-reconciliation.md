# Implementation Evidence and Claim Reconciliation

HIRMOS uses evidence-backed review to avoid overstating what the project can do.

A passing build is useful evidence, but it is not the same as a working local app. A provider adapter is useful implementation work, but it is not the same as verified provider delivery. A close summary is useful, but it is not the same as a consistent archive and accepted-state update.

## The rule

HIRMOS must reconcile material claims before surfacing readiness, implementation completion, production readiness, package readiness, or close success.

It checks:

- what HIRMOS said;
- what files actually exist;
- what session artifacts record;
- what commands/logs prove;
- what runtime behavior was verified;
- what remains not run, blocked, assumed, or not applicable.

## Evidence levels

HIRMOS distinguishes:

```text
not run
claimed but not logged
logged command passed
local runtime verified
user environment verified
production readiness verified
blocked
not applicable
```

This prevents a narrow success from being treated as a wider success.

## Examples

- `npm run build` passed does not prove the app was manually exercised in a browser.
- A database schema file does not prove runtime persistence is active.
- Local PostgreSQL working does not prove production database readiness.
- Console fallback for SMS/email does not prove real provider delivery.
- An archive folder does not prove accepted system state was updated.

## Domain Expert UX

Domain Expert mode should not expose every evidence table by default. It should surface a concise truthful summary:

```text
Implementation is complete for the authorized local MVP slice.
Build/typecheck passed.
Local runtime was not verified because dependency installation failed.
Production provider delivery is not yet ready and is tracked for review.
```

Technical Supervisor and Framework Diagnostics modes can expose deeper evidence records.

## Canonical values in generated artifacts

Generated HIRMOS artifacts must use the canonical evidence states from `EVIDENCE.md` claim reconciliation. Do not use shorthand such as `observed`, `build pass`, `accepted at close`, or `deferred` as evidence states. Translate them into canonical values and explain nuance in rationale fields.

## PROD-L8.21 Acceptance Evidence Semantics

HIRMOS must distinguish three acceptance levels and must not collapse them into a single `PASS` claim.

| Evidence level | Meaning | Allowed claim |
|---|---|---|
| Implementation accepted | Scope was implemented and code/static evidence passed | implementation accepted |
| Runtime verified | Local runtime/user-flow/provider behavior was exercised and passed | runtime verified |
| Production verified | Deployment/production-like constraints were exercised or explicitly assessed | production verified |

A delivery or phase may be implementation-accepted while runtime/provider/production verification remains pending, partial, blocked, or carry-forward. Close summaries must not claim full MVP/runtime/production acceptance unless the corresponding evidence level is complete.

## PROD-L8.22 Review Gate Salvage

HIRMOS preserves legacy evidence-backed review discipline through existing artifacts instead of restoring legacy review files.

Review gates must answer:

- What authority was reviewed?
- What evidence was reviewed?
- Was the final codebase or file state inspected?
- Does the evidence prove unit, session, phase, delivery, runtime, or production claims?
- What remains unproven?
- Why is the terminal state honest?

A passing static check is not a delivery review. A completed implementation unit is not a phase review. A phase review is not a delivery review unless cross-phase behavior and delivery-level acceptance posture are reviewed.


## PROD-L8.23 Generated-Run Validation Boundary
A generated run must be evaluated against its produced artifacts, not only against shipped framework templates. Runtime evidence and IU authority are credible only when the generated session archives contain the required authority checkpoint, substantive IU contracts, coverage mapping, timestamp completeness, and reconciled review/close records.
