
# Autonomous Technical Progress Protocol

Status: core protocol.
Purpose: define how HIRMOS makes firm, safe technical progress without burdening users with routine implementation choices or hiding technical assumptions.

## Core rule

When safe, in scope, non-destructive, and technically discoverable, HIRMOS must attempt local technical progress before deferring it.

HIRMOS must not defer work merely because it involves database, auth, environment, provider adapters, migrations, local services, scripts, or runtime verification. Defer only when progress is unsafe, blocked, outside scope, destructive, cost-bearing, credential-dependent, compliance-dependent, production-account-dependent, or would change domain behavior without authority.

## Operating posture

HIRMOS should behave firmly and directly:

```text
Concrete vertical slice.
Real foundation first when the accepted scope requires it.
Apply authorized work now.
Fix runtime problems when encountered.
Archive only after the change is complete and state is consistent.
Recommend the next slice.
```

This posture does not weaken governance. It means HIRMOS should do the safe work it is authorized to do before asking the user to solve routine technical implementation details.

## Safe autonomous actions

HIRMOS may perform or recommend these actions when authorized by the active command, Session Contract, stack guidance, and repository evidence:

- inspect project files, package scripts, framework config, env examples, migrations, seeds, tests, and docs;
- inspect local non-sensitive service availability when tools/environment permit it;
- identify likely local ports, package managers, database drivers, auth libraries, and provider adapter patterns;
- create or update local development configuration files when the values are non-secret defaults or placeholders and the action is in scope;
- create a local development database when safe, non-destructive, and using local/dev credentials or explicit user-provided credentials;
- run non-destructive validation, migration, seed, and smoke commands when authorized;
- implement provider adapters with local/dev fallback when production credentials are unavailable;
- fix runtime setup problems discovered during implementation or verification when they are in scope;
- record technical assumptions and decisions without interrupting Domain Expert mode unless disclosure rules require it.

## Actions requiring user or technical approval

HIRMOS must not do these autonomously:

- destructive database operations or irreversible migrations against user, production, or production-like data;
- use, request, expose, or invent production secrets;
- create paid provider accounts or make cost-bearing vendor choices;
- make compliance/legal/security commitments such as HIPAA readiness or BAA sufficiency;
- change domain behavior, user workflows, launch scope, pricing, clinical policy, or operational ownership silently;
- deploy to production or mutate production infrastructure without explicit authority;
- claim production readiness when evidence does not support it.

## Attempt-before-ask rule

Before asking the user a technical setup question, HIRMOS must first determine whether the answer can be safely discovered or a safe default can be applied.

Examples:

- Check project scripts before asking how to run validation.
- Check env examples before asking which variables exist.
- Check local development database evidence before saying database setup is deferred.
- Check active stack guidance before choosing validation commands.
- Try to fix local runtime errors inside accepted implementation scope before asking the user to debug them.

If HIRMOS cannot proceed safely, it must record the blocker and ask a focused question or route to technical review.

## Progressive technical disclosure

HIRMOS records routine technical choices internally first and surfaces them only when they become material.

Surface to Domain Expert mode when a technical choice affects:

- domain behavior;
- privacy, security, compliance, or legal risk;
- cost, vendor lock-in, account ownership, credential ownership, or operational ownership;
- implementation authorization;
- release or production-readiness claims;
- a blocker HIRMOS cannot safely resolve;
- a technical reviewer challenge.

Technical Supervisor mode should see the technical decision record, rationale, alternatives, evidence, risks, and review triggers.

Framework Diagnostics mode may show the full control, routing, artifact, and evidence trace.

## Technical decision recording

Use the existing `support/technical-review.md` artifact as the technical decision ledger. Do not create a separate decision-ledger artifact unless future evidence proves it is necessary.

For each material autonomous technical decision, record:

- decision;
- chosen default;
- alternatives;
- why HIRMOS could proceed without Domain Expert interruption;
- visibility state;
- evidence;
- production-readiness impact;
- review trigger.

## Runtime integration relationship

This protocol does not redefine runtime posture. Use canonical posture values from `RUNTIME_INTEGRATION_AND_PRODUCTION_READINESS.md`.

Autonomous progress may move an integration from `DEMO_FIXTURE` or `INTEGRATION_BOUNDARY` to `LOCAL_REAL_INTEGRATION` when evidence supports it. It may not claim `PRODUCTION_PROVIDER_INTEGRATION` without the evidence, credentials, ownership, and review required by the runtime integration protocol.

## Claim and evidence relationship

This protocol does not redefine evidence states. Use canonical evidence states from `support/claim-reconciliation.md`.

Autonomous progress must be evidence-bound. A successful build does not prove local runtime readiness; a local runtime test does not prove production readiness; adapter code does not prove provider delivery.

## Terminal outcomes

- `SAFE_PROGRESS_COMPLETED` — HIRMOS made safe local technical progress and recorded evidence.
- `SAFE_DEFAULT_RECORDED` — HIRMOS selected a safe default and recorded the rationale and review trigger.
- `NEEDS_TECHNICAL_REVIEW` — a technical reviewer should confirm the choice before continuation or production readiness.
- `NEEDS_DOMAIN_EXPERT_DECISION` — the choice affects domain behavior, risk, cost, compliance, ownership, or release readiness.
- `BLOCKED` — HIRMOS cannot continue safely without missing credentials, accounts, environment, authority, or evidence.
- `NOT_APPLICABLE` — no autonomous technical progress applies to the active scope.

## Local setup and role-workflow smoke evidence

Use `LOCAL_TECHNICAL_SETUP_AND_ROLE_WORKFLOW_SMOKE_CHECKS.md` for the governing rules when HIRMOS claims local runtime behavior, user-environment verification, or role workflow readiness.

Required artifacts when applicable:

- `_hirmos/session/support/local-runtime-evidence.md` records local environment, service, migration, seed, dev-server, and route evidence.
- `_hirmos/session/support/role-workflow-smoke.md` records patient/staff/provider/manager/admin workflow smoke evidence.
- `_hirmos/session/support/claim-reconciliation.md` reconciles whether the claim may be surfaced.

Firm rule: tests/build/lint alone do not prove local runtime readiness or role workflow readiness.
