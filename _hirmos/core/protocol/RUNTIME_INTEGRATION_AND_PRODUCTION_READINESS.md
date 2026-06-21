# Runtime Integration and Production Readiness Protocol

Status: core protocol.
Purpose: prevent HIRMOS from silently substituting fixture-backed, mock-only, or boundary-only work for real runtime integration or production readiness.

## Core rule

HIRMOS must not claim an integration is implemented, production-ready, or release-ready unless the active Design authority, Session Contract, Implementation evidence, and Update System State records identify the integration level and support the claim.

HIRMOS may use local-safe defaults and defer production-provider decisions when that preserves progress, but local defaults should preserve the production architecture shape where practical. Weaker demo/local substitutions are allowed only when explicitly authorized by Design and the Session Contract, then preserved at close as limitations or carry-forward items.


## Production-shaped default

For implementation-capable sessions, HIRMOS must prefer production-shaped engineering defaults unless the Session Contract explicitly authorizes a weaker result.

Production-shaped means:

- local/dev infrastructure mirrors intended production infrastructure where practical;
- durable business data uses durable persistence;
- long-running provider, AI, image, video, import/export, billing, or batch work is not hidden inside synchronous request paths;
- credit, usage, quota, billing, inventory, and account-balance mutations are concurrency-safe or explicitly limited;
- secrets, environment variables, generated runtime data, and handoff/release packages have a safe posture;
- limitations are explicit in Design, the Session Contract, evidence, and accepted-state updates.

## User-facing commitment levels

Domain Expert mode should normally expose only simple commitments:

```text
LOCAL_OR_DEMO_SAFE_PROGRESS
PRODUCTION_READY_BEFORE_COMPLETE
TECHNICAL_REVIEW_REQUIRED
```

- `LOCAL_OR_DEMO_SAFE_PROGRESS` means HIRMOS may keep moving with safe local defaults, fixture support, local real integrations, or provider boundaries as authorized by Design. This is not production readiness.
- `PRODUCTION_READY_BEFORE_COMPLETE` means HIRMOS must surface and resolve the material production integration choices before claiming completion for the relevant release/readiness boundary.
- `TECHNICAL_REVIEW_REQUIRED` means HIRMOS recommends a technical reviewer decide or confirm the production option.

Domain Expert users should not be forced to choose low-level technologies unless the choice affects domain behavior, risk, cost, compliance, ownership, implementation authorization, or release readiness.

## Internal runtime integration posture

HIRMOS tracks precise internal posture for every material integration area:

```text
DEMO_FIXTURE
INTEGRATION_BOUNDARY
LOCAL_REAL_INTEGRATION
PRODUCTION_PROVIDER_INTEGRATION
BLOCKED_PENDING_DECISION_OR_CREDENTIALS
NOT_APPLICABLE
```

Definitions:

- `DEMO_FIXTURE`: temporary in-memory, fixture, mock, console fallback, or fake runtime behavior.
- `INTEGRATION_BOUNDARY`: abstraction, schema, adapter, repository, API seam, or provider boundary exists, but runtime still does not use the real service.
- `LOCAL_REAL_INTEGRATION`: the app uses a real local/development integration through environment configuration, such as local PostgreSQL, local Auth.js flow, or a sandbox provider.
- `PRODUCTION_PROVIDER_INTEGRATION`: production-oriented provider/service integration is implemented and externally configurable; production credentials, ownership, compliance, and deployment constraints are represented.
- `BLOCKED_PENDING_DECISION_OR_CREDENTIALS`: HIRMOS cannot responsibly continue or claim readiness without user/technical decision, account, credential, compliance, or environment input.
- `NOT_APPLICABLE`: the integration area is not relevant to the active scope, with rationale.

## Material integration areas

Consider runtime integration posture for any material area in scope or implied by the request, including:

- database / persistence;
- authentication and authorization;
- email / SMS / messaging;
- file or object storage;
- payments or billing;
- AI/provider APIs;
- background jobs / schedulers / queues;
- deployment environment;
- secrets and environment configuration;
- observability, audit, backups, and recovery when relevant.

## Design-stage obligations

Design must identify material integration areas and record:

- current or planned posture;
- recommended production option when meaningful;
- rationale for recommendation;
- alternatives and when a technical reviewer might choose them;
- decision owner;
- whether the item is a domain decision, technical review item, non-gating assumption, gated item, or production-readiness blocker;
- what Implementation is authorized to deliver now.

Design may authorize fixture/demo or boundary work only when the Session Contract and implementation-readiness checkpoint say so explicitly.

## Domain Expert visibility rule

In `domain_expert` mode, HIRMOS should avoid interrupting the user with low-level integration choices while safe local/default progress is possible.

HIRMOS must surface integration choices to the Domain Expert when:

- the choice changes domain behavior;
- the choice affects privacy, security, compliance, or legal risk;
- the choice creates meaningful cost, vendor lock-in, operational ownership, or account/credential ownership;
- the choice blocks implementation progress;
- the user explicitly requests real or production-ready integration;
- the session is approaching production-readiness or release-readiness;
- a technical reviewer changes or challenges the HIRMOS recommendation.

Before production readiness, HIRMOS must surface a checkpoint with each material integration area, current posture, HIRMOS recommendation, alternatives, rationale, decision owner, blockers, and next action.

## Implementation-stage obligations

Implementation Units must state the integration posture they are authorized to deliver.

Implementation may not silently downgrade from a real integration to a fixture, mock, console fallback, or boundary-only implementation.

If the authorized posture cannot be delivered, Implementation must:

1. record evidence;
2. create or update unresolved items;
3. route back to Design or fail closed;
4. avoid claiming more than was implemented.

## Evidence obligations

Evidence must distinguish:

- implementation level delivered;
- environment/configuration used;
- commands run and logs produced;
- whether dependencies were installed;
- whether local runtime was verified;
- whether provider credentials were available;
- whether production provider behavior was verified;
- what remains blocked or not run.

A passing build or typecheck does not prove local runtime integration or production readiness.

## Update System State obligations

Update System State must preserve the final integration posture for material areas in accepted state or carry-forward records.

Close must not claim production readiness when any material integration area is fixture-backed, boundary-only, locally real but not production-reviewed, blocked, or unverified, unless the close explicitly names that limitation.

## Terminal outcomes

- `POSTURE_RECORDED` — material integration areas are classified and authorized for current scope.
- `PRODUCTION_OPTIONS_READY` — production-readiness recommendations, alternatives, and blockers are ready to surface.
- `NEEDS_DECISION` — material decision blocks continuation or production-readiness claim.
- `BLOCKED` — required credentials, accounts, environment, evidence, or review are missing.
- `NOT_APPLICABLE` — no material integration area applies to the active scope.

## Autonomous progress before deferral

When a material integration area is in accepted scope, HIRMOS must attempt safe local technical progress before deferring the integration.

HIRMOS should not leave database, auth, messaging, environment, migration, seed, or runtime setup as vague future work when safe local progress is possible. It must either:

1. implement the authorized posture and record evidence;
2. select a safe local/default path and record the technical decision;
3. implement a provider boundary with truthful fallback and production blocker records; or
4. block with a specific reason such as missing credentials, unsafe operation, compliance review, account ownership, or unavailable environment.

This rule does not authorize production claims. It only prevents premature deferral of safe technical work.

Authority for the attempt-before-ask rule: `_hirmos/core/protocol/AUTONOMOUS_TECHNICAL_PROGRESS.md`.

## Canonical posture enforcement

Runtime posture values are closed. HIRMOS must not invent or use alternate posture labels in session artifacts, reviews, checkpoint output, or accepted state.

Invalid examples include `LOCAL_REAL`, `LOCAL_REAL + console fallback`, `CODE_COMPLETE_DEFERRED`, `PROVIDER_READY`, and similar shorthand. Translate them into canonical posture values from this protocol and record the rationale.

Firm rule: a posture label that is not listed in this protocol is not valid HIRMOS evidence.

## Local setup and role-workflow smoke evidence

Use `LOCAL_TECHNICAL_SETUP_AND_ROLE_WORKFLOW_SMOKE_CHECKS.md` for the governing rules when HIRMOS claims local runtime behavior, user-environment verification, or role workflow readiness.

Required artifacts when applicable:

- `_hirmos/session/EVIDENCE.md` records local environment, service, migration, seed, dev-server, and route evidence.
- `_hirmos/session/EVIDENCE.md` records role-specific workflow smoke evidence for the relevant end-user, operator, privileged-user, and administrative paths.
- `_hirmos/session/EVIDENCE.md` reconciles whether the claim may be surfaced.

Firm rule: tests/build/lint alone do not prove local runtime readiness or role workflow readiness.

## Canonical runtime posture enforcement for generated artifacts

Runtime posture values are closed and must remain closed in generated session and accepted-state artifacts.

Translate shorthand before claiming readiness or close:

| Noncanonical value / pattern | Canonical handling |
|---|---|
| `LOCAL_REAL` | `LOCAL_REAL_INTEGRATION` if real local/dev service evidence exists; otherwise `INTEGRATION_BOUNDARY` or `CLAIMED_NOT_LOGGED` in claim evidence. |
| `LOCAL_REAL + console fallback` | Split by area or capability: the real local integration area may be `LOCAL_REAL_INTEGRATION`; console fallback messaging is `DEMO_FIXTURE` or `INTEGRATION_BOUNDARY` unless provider delivery is verified. |
| `provider-ready`, `adapter-ready`, `code complete deferred` | `INTEGRATION_BOUNDARY` unless runtime/provider evidence supports a higher posture. |
| `production ready pending credentials` | `BLOCKED_PENDING_DECISION_OR_CREDENTIALS`, not `PRODUCTION_PROVIDER_INTEGRATION`. |
| `implemented`, `done`, `accepted` | Not a posture. Translate to a canonical posture and record implementation/evidence status separately. |

Generated artifacts must keep runtime posture separate from evidence status and accepted-state decision classification. If one field combines them, split it before close.

Firm rule: HIRMOS must not close a session with noncanonical runtime posture values in active session artifacts or accepted-state artifacts.

## Close-time runtime posture materialization

Before normal close, any material runtime provider or integration claim must have an owning `DESIGN.md` / `EVIDENCE.md` runtime posture artifact.

`DESIGN.md` / `EVIDENCE.md` runtime posture must use the canonical runtime posture values from this protocol. If a generated artifact or accepted-state file contains shorthand such as `LOCAL_REAL`, `provider ready`, `code complete`, or `console fallback`, close must route back and translate the value before accepted state is updated.

Runtime posture does not replace evidence status. A posture such as `LOCAL_REAL_INTEGRATION` still requires claim evidence from `EVIDENCE.md` claim reconciliation and local setup evidence from `EVIDENCE.md` when local runtime readiness is claimed.

Firm rule: normal close is blocked when material runtime posture is claimed but the owning posture artifact is missing, noncanonical, or unsupported by evidence.
