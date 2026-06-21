# Claim Reconciliation Protocol

Status: core protocol.
Purpose: prevent HIRMOS from claiming more progress, readiness, runtime behavior, integration, or close success than the current working copy and evidence records support.

Claim reconciliation is the HIRMOS control that compares:

```text
what HIRMOS says happened
what session artifacts say happened
what project files show
what command/log evidence proves
what remains not run, blocked, assumed, or not applicable
```

## Core rule

HIRMOS must not claim implementation completion, runtime readiness, local app verification, production readiness, update-state readiness, or close success unless the claim has a corresponding evidence record and is not contradicted by final files, active session state, archive state, accepted state, or known environment failures.

If a claim is not reconciled, HIRMOS must downgrade the claim, route back, create a blocker, or fail closed.

## Claim status values

Use these values when reconciling claims:

- `NOT_CLAIMED` — no claim was made;
- `NOT_RUN` — a check or command was expected or useful but not executed;
- `CLAIMED_NOT_LOGGED` — HIRMOS claimed something passed or worked but no evidence record/log is available;
- `LOGGED_COMMAND_PASSED` — a command is recorded with passing output or log;
- `LOGGED_COMMAND_FAILED` — a command is recorded with failing output or log;
- `LOCAL_RUNTIME_VERIFIED` — local runtime behavior was actually exercised and recorded;
- `USER_ENVIRONMENT_VERIFIED` — the user's local environment or provided environment was verified, not merely the agent environment;
- `PRODUCTION_READINESS_VERIFIED` — production-readiness requirements were explicitly verified or accepted with documented evidence;
- `BLOCKED` — evidence cannot be produced without missing dependency, credentials, environment, user decision, or repair;
- `NOT_APPLICABLE` — the check does not apply, with rationale.

## Claim families

Reconcile at least these claim families when applicable:

| Claim family | Examples |
|---|---|
| Artifact claim | artifact exists, artifact is complete, artifact backs a checkpoint |
| Design claim | requirements/design/scope/delivery plan is ready |
| Implementation claim | unit completed, files changed correctly, scope implemented |
| Validation claim | lint/test/typecheck/build/migration/seed passed |
| Runtime claim | app runs locally, route works, database connection works |
| Integration claim | database/auth/email/SMS/storage/payment provider works |
| Close claim | state updated, archive preserved, session reset |
| Packaging claim | package includes expected framework/app files and can be verified |

## Evidence hierarchy

When sources disagree, use this order:

1. Current working-copy files and archived artifacts.
2. Raw command/log evidence when available.
3. Session artifacts and reviews.
4. User-provided observations and environment results.
5. Chat summaries and agent statements.
6. Intended design or planned work.

Chat summaries alone never prove a claim.

## Final-file reconciliation

Before claiming implementation completion or close success, HIRMOS must compare major claims against final files and session state.

Examples:

- If HIRMOS claims PostgreSQL runtime persistence, final files must contain the actual runtime database integration and evidence must show the level verified.
- If HIRMOS claims tests passed, evidence must record command, working directory, result, and output/log or explain why logs are unavailable.
- If HIRMOS claims local runtime works, evidence must say how the app was run and what was verified.
- If HIRMOS claims production readiness, production integration decisions, credentials/environment disposition, and blockers must be reconciled.
- If HIRMOS claims close success, accepted state, archive controls, active session state, accepted-state records, and close controls must agree.

## Runtime verification distinction

HIRMOS must distinguish:

```text
build/typecheck success
unit or integration test success
local runtime server started
specific user workflow verified
user environment verified
production provider verified
production readiness verified
```

One level must not be treated as another.

## Not-run disclosure

A useful but unrun check must be recorded as `NOT_RUN`, not omitted.

If dependencies could not be installed, credentials were missing, or the user's local environment failed, HIRMOS must record the limitation and avoid claiming local app functionality.

## Completion downgrade rule

If evidence supports only partial completion, HIRMOS must say so.

Examples:

- "Implementation complete for static UI only; runtime database persistence is not implemented."
- "Build passed, but local runtime was not verified."
- "Provider adapter exists, but provider delivery was not verified because credentials are missing."
- "Close is blocked because accepted state and archive manifest disagree."

## Control contribution

Claim reconciliation contributes an execution control whenever HIRMOS is about to surface a material readiness, completion, validation, integration, packaging, or close claim.

Allowed control outcomes:

```text
SATISFIED
BLOCKED
NOT_APPLICABLE
```

It is not satisfied when material claims are `CLAIMED_NOT_LOGGED`, contradicted by final files, or dependent on unrecorded assumptions.

## Mandatory instantiation and canonical-state enforcement

`EVIDENCE.md` claim reconciliation is mandatory when HIRMOS surfaces any material claim about:

- implementation completion;
- validation success;
- local runtime readiness;
- user-environment verification;
- runtime integration readiness;
- production readiness;
- package completeness;
- update-state readiness;
- close/archive success.

HIRMOS must instantiate `_hirmos/session/EVIDENCE.md` before the material claim is surfaced. If claim reconciliation is missing, the claim state is `CLAIMED_NOT_LOGGED` or `BLOCKED`; HIRMOS must not upgrade it through chat language.

Canonical claim status values are closed. Noncanonical labels are invalid. Do not use labels such as `VERIFIED_IN_BUILD`, `ACCEPTED_BY_SCOPE`, `LOCAL_REAL`, `CODE_COMPLETE`, `PARTIAL_PASS`, or similar substitutes as claim status values. Translate them into the canonical values in this protocol and record the rationale.

Firm rule: build success proves only the logged build command. It does not prove login, database persistence, provider delivery, role workflow behavior, or production readiness.

## Local setup and role-workflow smoke evidence

Use `LOCAL_TECHNICAL_SETUP_AND_ROLE_WORKFLOW_SMOKE_CHECKS.md` for the governing rules when HIRMOS claims local runtime behavior, user-environment verification, or role workflow readiness.

Required artifacts when applicable:

- `_hirmos/session/EVIDENCE.md` records local environment, service, migration, seed, dev-server, and route evidence.
- `_hirmos/session/EVIDENCE.md` records role-specific workflow smoke evidence for the relevant end-user, operator, privileged-user, and administrative paths.
- `_hirmos/session/EVIDENCE.md` reconciles whether the claim may be surfaced.

Firm rule: tests/build/lint alone do not prove local runtime readiness or role workflow readiness.

## Generated-artifact canonical value enforcement

Canonical evidence status values are not examples. They are the only allowed values for evidence/status fields in generated HIRMOS artifacts.

When HIRMOS encounters shorthand, prose labels, or accepted-state decisions in an evidence/status field, it must translate before advancing:

| Noncanonical value / pattern | Correct handling |
|---|---|
| `observed`, `observed (code)`, `code observed` | Use `LOGGED_COMMAND_PASSED` only when backed by a logged command; otherwise use `CLAIMED_NOT_LOGGED` or move the observation to a notes/source column. |
| `build pass`, `build passed`, `verified in build` | Use `LOGGED_COMMAND_PASSED` for the build command only; do not use it to verify runtime, login, provider delivery, or role workflows. |
| `ACCEPTED_AT_CLOSE`, `accepted`, `accepted by scope` | This is an accepted-state decision, not evidence. Record decision classification separately and keep evidence status canonical. |
| `NOT_IMPLEMENTED`, `deferred`, `future` | Use `NOT_CLAIMED`, `NOT_RUN`, or `BLOCKED` according to whether a claim was made and whether scope is blocked; record carry-forward separately. |
| `PARTIAL`, `PARTIAL_PASS`, `works`, `done` | Translate to the strongest supported canonical evidence value and downgrade unsupported parts. |

Generated artifacts that contain material claim tables must include a canonical-value check or state that the claim is not applicable. If noncanonical evidence values remain in session artifacts, `CURRENT_SYSTEM_STATE.md`, `CURRENT_SYSTEM_STATE.md` latest-close metadata, `CARRY_FORWARD.md`, or `DECISION_LOG.md`, Update System State is blocked until they are translated or explicitly marked as historical/prose notes outside evidence/status fields.

Firm rule: do not invent new evidence states during a run. Add nuance in rationale/notes, not in the status value.

## Close Claim Materialization Record

Close claims are material claims and must be reconciled in `_hirmos/session/EVIDENCE.md` before normal close is surfaced.

The close claim materialization record must cover at least:

- close/archive success;
- accepted-state merge success;
- framework compliance when framework files or accepted-state invariants changed;
- local runtime/setup readiness when claimed;
- role workflow readiness when claimed;
- runtime integration posture when claimed;
- package cleanliness when a package or handoff is produced.

If this section is missing from an archived normal-close session, the close claim is `CLAIMED_NOT_LOGGED` and must not be treated as fully HIRMOS-compliant.

Firm rule: a normal close without claim reconciliation is not a fully reconciled close.

## Cross-run comparison claim discipline

When HIRMOS compares multiple candidate implementations or tool outputs, comparative claims are material claims when they influence baseline selection, delivery planning, or user-facing recommendations.

Examples of material comparative claims:

- best requirements coverage;
- strongest engineering quality;
- best UX/operator usability;
- strongest artifacts/system-state quality;
- selected implementation baseline;
- salvage source for routes, tests, UX, or architecture.

Such claims must identify the evidence basis, known limitations, and whether the claim is static review evidence, executed runtime evidence, user-environment evidence, or production readiness evidence.

Firm rule: a ranking or baseline recommendation must not be treated as implementation evidence unless the relevant implementation/runtime checks were actually performed and recorded with canonical evidence states.
