# Validation and Evidence Protocol


## Governance posture for evidence

Evidence is the governed proof trail of authorized work, not an after-the-fact compliance artifact. HIRMOS must not create evidence records to make unauthorized implementation appear governed. If evidence records describe work that occurred before the required command state, scope authority, or IU authority existed, the record must identify a governance deviation/correction before readiness, completion, or close can be claimed.

Status: core protocol.
Purpose: define the minimum evidence discipline for trustworthy HIRMOS claims.

HIRMOS validation is based on:

```text
Execution Controls
+ Evidence Records
+ Boundary Reviews
+ Lightweight Static Validation
```

It does not require heavy runtime output-governance machinery by default.

## Core claim rule

HIRMOS must not claim progress, readiness, implementation-readiness, implementation completion, update-state-readiness, close readiness, validation success, or close success unless the claim is backed by existing artifacts, observed file state, command output, user decision, or explicit not-applicable rationale.

## Evidence vocabulary

Evidence must distinguish:

- `observed` — directly inspected in files, artifacts, command output, or user input;
- `inferred` — reasoned from observed evidence;
- `assumed` — carried without direct proof and recorded as an assumption;
- `unknown` — not known yet;
- `blocked` — cannot proceed without decision, repair, route-back, or evidence;
- `not_run` — command/check was not executed;
- `not_applicable` — check does not apply, with rationale.

## Evidence families

HIRMOS evidence includes:

- current-state evidence;
- Design evidence;
- Implementation evidence;
- Update System State evidence.

## Validation logs

When HIRMOS claims that a test, build, typecheck, lint, migration, or validation command ran, it must record:

- command;
- working directory;
- result;
- relevant output or log path;
- whether dependencies/environment were available;
- whether the result is reproducible from the current working copy.

## Boundary reviews

Before passing major boundaries, HIRMOS must review whether required controls and artifacts are ready for that boundary.

Boundary reviews include, when applicable:

- system-state readiness;
- Design readiness;
- implementation-readiness;
- implementation completion;
- update-state readiness;
- close readiness.

## Static validation

Static validation should check concrete framework and artifact properties first: required files exist, config values are valid, referenced installed stacks exist, session artifacts exist before being referenced, required controls are not unsatisfied at terminal boundaries, and archive paths preserve session evidence.


## Runtime integration evidence

When implementation, readiness, or close claims involve runtime integrations, evidence must identify the actual integration level delivered.

Record whether each material integration area is:

```text
DEMO_FIXTURE
INTEGRATION_BOUNDARY
LOCAL_REAL_INTEGRATION
PRODUCTION_PROVIDER_INTEGRATION
BLOCKED_PENDING_DECISION_OR_CREDENTIALS
NOT_APPLICABLE
```

Evidence must distinguish build/test success from local runtime verification and production-provider verification.

Examples:

- build success alone does not prove database runtime persistence;
- adapter code alone does not prove provider delivery;
- local database migration success does not prove production database readiness;
- console fallback does not prove real email/SMS delivery;
- missing credentials must be recorded as blocked, not silently treated as success.

HIRMOS must not claim production readiness until every material integration area has a production recommendation, accepted decision or review path, required credentials/environment disposition, and evidence or explicit blocker.

## Close and archive evidence

Close evidence must prove a state transaction, not merely a user-facing summary.

Required close evidence includes:

- `SESSION_EXECUTION.md` close/update control pointers accepted/rejected/evidence-only/carry-forward classification;
- `SESSION_EXECUTION.md` close controls close readiness and integrity checks;
- archive manifest under `_hirmos/system/history/sessions/<session-id>/`;
- current-state latest-close metadata and carry-forward updates;
- reset `SESSION_STATE.json` after normal close;
- post-close status expectation.

If these records disagree, close evidence is contradictory and HIRMOS must not claim normal close success.

## Claim reconciliation

When HIRMOS makes or prepares a material claim, it must apply `_hirmos/core/protocol/CLAIM_RECONCILIATION.md`.

Material claims include:

- implementation completion;
- validation success;
- local runtime readiness;
- integration readiness;
- production readiness;
- package completeness;
- update-state readiness;
- close success.

Evidence records must classify each claim as one of:

```text
NOT_CLAIMED
NOT_RUN
CLAIMED_NOT_LOGGED
LOGGED_COMMAND_PASSED
LOGGED_COMMAND_FAILED
LOCAL_RUNTIME_VERIFIED
USER_ENVIRONMENT_VERIFIED
PRODUCTION_READINESS_VERIFIED
BLOCKED
NOT_APPLICABLE
```

HIRMOS must downgrade or block claims that are unsupported, unlogged, contradicted by final files, or dependent on unavailable environment/credentials.

## Local setup and role-workflow smoke evidence

Use `LOCAL_TECHNICAL_SETUP_AND_ROLE_WORKFLOW_SMOKE_CHECKS.md` for the governing rules when HIRMOS claims local runtime behavior, user-environment verification, or role workflow readiness.

Required artifacts when applicable:

- `_hirmos/session/EVIDENCE.md` records local environment, service, migration, seed, dev-server, and route evidence.
- `_hirmos/session/EVIDENCE.md` records role-specific workflow smoke evidence for the relevant end-user, operator, privileged-user, and administrative paths.
- `_hirmos/session/EVIDENCE.md` reconciles whether the claim may be surfaced.

Firm rule: tests/build/lint alone do not prove local runtime readiness or role workflow readiness.

## Validator minimality classes

Validator checks must protect runtime safety and artifact authority before they protect wording. When a check is added or changed, classify it as one of these categories:

| Class | Keep by default? | Purpose | Examples |
|---|---|---|---|
| Authority-safety | Yes | Prevent invalid authority surfaces or unsafe lifecycle progress. | delivery baseline must not create session scope; session optional authority must not appear during delivery baseline; root accepted-state requirements must not exist without explicit governance. |
| Freshness/concordance | Yes | Prevent stale mirrors from contradicting active machine state or evidence. | `SESSION_STATE.json` conflicts with `SESSION_EXECUTION.md`; phase status remains pending after implementation; evidence says both passed and not-run. |
| Structural/status | Yes | Require machine-checkable fields, legal statuses, and referenced paths. | scalar `Entry criteria status`; current phase pointer exists; allowed next command is legal. |
| Exact wording | Avoid unless it protects authority safety | Require particular prose. Convert to structural/status checks when possible. | pre-acceptance delivery should be tested by status + absence of accepted/active labels, not by requiring one exact sentence. |
| Release-marker / plan-marker | Avoid | Historical implementation-plan markers should not be long-term validation authority. | `PROD-Lx` strings are not runtime invariants unless the phrase names a current contract. |

Validator minimality rule: prefer structural/status checks over exact phrase checks. Keep wording checks only when the wording itself prevents an authority-safety failure, and express the failure in terms of state and authority rather than plan history.

## PROD-L8.19 validator responsibility boundaries

Validators should protect authority safety, state legality, freshness/concordance, chronology, and evidence-claim consistency. Validators should not enforce user-managed package/export hygiene as framework governance.

For L8.19, validator-relevant risks are:

- idle `hirmos continue` must not be represented as a legal mutation path;
- IU-governed implementation must not claim normal governance when IU artifacts were created only after material edits;
- material correction commands must be individually traceable in `SESSION_EXECUTION.md`;
- archive/session chronology must be monotonic or explicitly explained;
- delivery-plan active/pointer sections must not remain stale at close.

## PROD-L8.21 Acceptance Evidence Semantics

HIRMOS must distinguish three acceptance levels and must not collapse them into a single `PASS` claim.

| Evidence level | Meaning | Allowed claim |
|---|---|---|
| Implementation accepted | Scope was implemented and code/static evidence passed | implementation accepted |
| Runtime verified | Local runtime/user-flow/provider behavior was exercised and passed | runtime verified |
| Production verified | Deployment/production-like constraints were exercised or explicitly assessed | production verified |

A delivery or phase may be implementation-accepted while runtime/provider/production verification remains pending, partial, blocked, or carry-forward. Close summaries must not claim full MVP/runtime/production acceptance unless the corresponding evidence level is complete.

## PROD-L8.22 Evidence-Backed Review Gate Salvage

Legacy review discipline is preserved through existing HIRMOS surfaces, not through new review artifacts. HIRMOS must not collapse unit success, static validation, runtime behavior, production readiness, and delivery acceptance into one generic `PASS` claim.

### Aggregate review gate rule

A session, phase, or delivery review must be evidence-backed and must include an honest terminal state. A higher-level review may not pass merely because individual implementation units have local completion records. It must review the aggregate scope against the accepted authority and the evidence actually available.

Required review dimensions when applicable:

- source authority reviewed;
- implementation units or session work reviewed;
- actual final codebase/files reviewed: `YES` / `NO` / `NOT_APPLICABLE`;
- scope coverage reviewed;
- cross-unit or cross-phase integration reviewed;
- architecture/preservation alignment reviewed;
- validation evidence reviewed;
- runtime/provider evidence level reviewed;
- production evidence level reviewed;
- unresolved or carry-forward impact reviewed;
- final review result and why that result is honest;
- explicit `not claimed` statements for evidence levels not proven.


### Test / Fixture / Validator Change Rationale

When implementation modifies tests, fixtures, mocks, snapshots, validators, expected-output files, regression fixtures, or generated expected-output artifacts, the owning execution record must include a concise rationale explaining why the change was required and why realism or coverage is preserved or improved. Reviews must explicitly judge whether these changes weakened validation, preserved validation, or improved validation.

### Review result vocabulary

Use review results that preserve terminal-state honesty:

```text
PASS
PARTIAL
BLOCKED
FAILED
NOT_APPLICABLE
```

A `PASS` review requires evidence for the claim level being passed. If runtime or production evidence is missing, the review must be `PARTIAL`, `BLOCKED`, or `PASS` only for the narrower level such as implementation accepted.

### Actual-codebase review rule

When implementation changed project files, review records must state whether the final working copy or final archived file state was inspected. Chat summaries and intended diffs are not sufficient review evidence.


## PROD-L8.23 Generated-Run Runtime Artifact Validation
Validators must distinguish framework-template validation from generated-run validation. A framework can pass static validation while a generated project run fails runtime-artifact validation. When generated artifacts exist, validation should inspect them for authority safety and concordance, including IU authority checkpoints, minimum IU substance, timestamp completeness, phase close freshness, delivery close-log freshness, and evidence-claim honesty.

Runtime generated-artifact validation may fail:

- IU-mode sessions with IU files but no `PROD-L8.21 IU Set Authority Checkpoint`.
- IU-mode sessions missing an authorization decision: `IMPLEMENTATION_AUTHORIZED`, `BLOCKED`, or `LIGHTWEIGHT_NO_IU`.
- IU-mode sessions missing an IU Set Coverage Map from source scope to IU files.
- Generated IU files below the minimum IU contract standard.
- Archived `SESSION_STATE.json` files with null `created_at`, `updated_at`, or missing run context.
- Accepted phase files with current binary exit criteria still `PENDING` or `NOT_ASSESSED` outside explicitly historical sections.
- Delivery status logs that omit material phase close rows when phase files are accepted/closed.


## PROD-L8.24 Pre-Execution Ledger and Generated Review Validation
Generated-run validation must reject retrospective validator compliance. IU-mode generated sessions must contain a `Pre-Material-Edit Ledger Row` before a `Material Edit Start Record`, with `Material implementation started: NO` and `Retrospective checkpoint or IU expansion: NO`. Validator-satisfying IU authority added during close/archive cleanup is not clean governance. Generated phase and delivery close artifacts must instantiate the L8.22 review gates with concrete codebase, scope, integration, runtime, production, final-result, honest-result, and not-claimed fields. Runtime/provider/production claims must be scoped per accepted requirement or DAC item; broad `LOCAL_RUNTIME_VERIFIED` claims are invalid when related critical-flow evidence is `NOT_RUN` or absent.

## PROD-L8.26 Evidence Posture Simplification

Evidence posture must distinguish implementation acceptance from runtime and production verification.

Recommended compact posture dimensions for close summaries:

| Dimension | Allowed compact values |
|---|---|
| Implementation coverage | NOT_STARTED / PARTIAL / COMPLETE / NOT_APPLICABLE |
| Local runtime evidence | NOT_CLAIMED / NOT_RUN / PARTIAL / LOCAL_E2E_VERIFIED / BLOCKED / NOT_APPLICABLE |
| Production evidence | NOT_CLAIMED / NOT_RUN / STAGING_VERIFIED / PRODUCTION_VERIFIED / BLOCKED / NOT_APPLICABLE |
| Final result | CLOSED_ACCEPTED / CLOSED_PARTIAL / BLOCKED / FAILED / DEFERRED / SUPERSEDED |

Do not use `PASS` as a substitute for all three evidence dimensions. If runtime or production evidence is not run, state that limitation and use a narrower implementation-accepted or partial result.

## PROD-L8.27 Pre-Archive Validation and Historical Archive Integrity

Validation is lifecycle-aware. Active artifacts and archived artifacts are not validated with the same mutation semantics.

- `ACTIVE_FIXABLE`: active-session validation failure before archive; HIRMOS may correct the active artifact, route back, block, or close partial.
- `ARCHIVE_TRANSACTION_REPAIRABLE`: archive packaging, manifest, copied-path, reset, or archived-machine-state normalization issue; HIRMOS may repair the archive transaction mechanics and record the repair.
- `ARCHIVE_HISTORICAL_IMMUTABLE`: archived historical authority/evidence was missing, thin, stale, contradictory, or created too late; HIRMOS must not rewrite the historical archive to satisfy validation.

Generated-run validation must run before archive whenever possible. If a generated IU-mode session fails minimum IU contract, sealed-section, pre-material-edit, evidence, or review-gate validation after it has already been archived, the correct result is governance deviation / partial / blocked / corrective note, not retrospective expansion of archived IU files.

Validators should use messages that tell the model whether a failure is active-fixable, archive-transaction-repairable, or archive-historical-immutable. This gives the model an honest non-patching path when validation fails after archive.

## PROD-L8.28 Generated IU Instantiation and Active Close Concordance

Generated implementation-unit artifacts must be validated while the session is active and before archive. A generated IU is close-eligible only when its sealed contract sections were fully instantiated before execution and its append-only Execution Record and Unit Review contain concrete evidence-backed completion/review results.

Active close must fail closed, downgrade to partial, or route back when IU status contradicts session/phase/delivery close claims. In particular, implementation-complete, phase-accepted, delivery-accepted, or delivery-closed claims are invalid when any applicable IU remains `Execution status: NOT_STARTED`, `Review status: PENDING`, lacks Unit Result, lacks validation/evidence comparison, or lacks a required Test / Fixture / Validator Change Rationale. Historical archives must not be expanded to repair these defects after snapshot; apply PROD-L8.27 archive immutability instead.
