# Delivery Governance Protocol

Status: core protocol.
Purpose: define when HIRMOS must use durable multi-session delivery governance and how Delivery Plans and Phase files integrate with greenfield and brownfield work.

## Core rule

For multi-session work in any project type, a Delivery Plan is needed and separate phase files are required.

Durable delivery authority lives under:

```text
_hirmos/system/delivery/<delivery-id>/DELIVERY_PLAN.md
_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md
```

Session-local delivery artifacts are not canonical delivery authority. A session may reference or consume durable delivery artifacts, but it must not replace them with `_hirmos/system/delivery/<delivery-id>/DELIVERY_PLAN.md`, `_hirmos/system/delivery/<delivery-id>/DELIVERY_PLAN.md phase decomposition`, `_hirmos/system/delivery/<delivery-id>/DELIVERY_PLAN.md status log`, `_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md`, or `_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md`.

## Delivery-Need Classification Gate

Every implementation-capable `hirmos start` must answer this literal classification question before claiming implementation readiness:

```text
Does this request require multi-session delivery governance?
Answer: YES / NO / UNCERTAIN.
Evidence:
Decision factors:
If NO, why is one bounded session safe?
If YES, required Delivery Plan:
If UNCERTAIN, what must be inspected before deciding?
```

Fail-closed rules:

- YES: HIRMOS must create, adopt, or follow a durable Delivery Plan before implementation can be authorized.
- UNCERTAIN: HIRMOS must not proceed to implementation readiness until the uncertainty is resolved.
- NO: HIRMOS must provide affirmative evidence that one bounded session is safe and must list the delivery triggers considered and ruled out.

When classification is ambiguous, HIRMOS must bias toward Delivery Plan governance, not single-session implementation.

## Greenfield triggers

A greenfield request requires a durable Delivery Plan and separate phase files when any of these are true:

- building a complete app, product, MVP, pilot, or production-ready system rather than a narrow isolated artifact;
- multiple user roles, workflows, modules, screens, integrations, backend services, or admin surfaces are involved;
- authentication, database persistence, external providers, deployment, or operational UX are part of the target;
- the user asks for staged implementation, production readiness, pilot readiness, or complete system delivery;
- requirements are broad enough that implementation cannot be reviewed safely in one bounded session;
- work needs multiple validation layers such as lint, test, build, smoke, runtime, UX, or role-flow review;
- future sessions must continue from a stable phase boundary.

Greenfield status does not make single-session implementation safe. Lack of existing code can increase risk because accepted current-state truth and phase boundaries are not yet established.

## Brownfield triggers

A brownfield request requires a durable Delivery Plan and separate phase files when any of these are true:

- multiple existing modules, workflows, routes, data models, or integrations are affected;
- preservation risk exists and existing behavior must not regress;
- runtime behavior, database schema, UI, API, auth, background jobs, or external services are involved together;
- the requested change spans more than one coherent implementation unit;
- the model cannot inspect all affected areas confidently before implementation;
- prior runs revealed drift, stale artifacts, incomplete close/update behavior, or incomplete evidence;
- acceptance depends on multiple sessions of implementation, verification, polish, or reconciliation.

Brownfield classification must be evidence-backed. User wording such as "just add", "quickly fix", or "small change" is not sufficient to justify single-session execution.

## Universal triggers

A durable Delivery Plan is required when:

- the user explicitly asks for multi-session, staged, phased, roadmap, delivery program, or long-running work;
- the scope cannot be completed and validated in one bounded session without hiding important risks;
- unresolved decisions affect sequencing;
- work must be split into accepted increments;
- there is a known need for carry-forward across sessions;
- the user asks to avoid stopping mid-task by planning multiple steps or phases.

## Single-session eligibility

A request may proceed without a Delivery Plan only when all conditions are true:

1. The request has one bounded objective.
2. The affected area is narrow and inspectable.
3. Requirements fit into one Session Contract without phase decomposition.
4. Implementation can be completed, validated, reviewed, and closed in one session.
5. No durable carry-forward or future phase boundary is needed.
6. Preservation/regression risk is low or fully covered by the Session Contract.
7. HIRMOS can explain why Delivery Plan governance would add overhead without improving safety.

If any condition is false or uncertain, classification must not be NO.

## Banned single-session justifications

HIRMOS must not justify single-session work only with vague claims such as:

- seems manageable;
- can be handled in one pass;
- user asked to proceed now;
- no existing code means low risk;
- this is just planning;
- implementation can be refined later.

A single-session decision must cite concrete boundedness evidence and list the Delivery Plan triggers considered and ruled out.

## Required surfaces

## Durable Phase Adoption Rule

When Delivery-Need Classification is `YES`, every implementation-capable session must adopt exactly one durable phase file before implementation readiness:

```text
_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md
```

The adoption must be explicit in `_hirmos/session/SESSION_CONTRACT.md`; implicit references, chat statements, status summaries, or Current System State pointers are not enough.

Required adoption fields:

```text
Adoption status: ADOPTED / NOT_APPLICABLE / BLOCKED
Delivery ID:
Delivery Plan path:
Active Phase ID:
Active Phase path:
Phase source status:
Adoption mode: FULL_PHASE / EXPLICIT_PARTIAL_WITH_DEFERRED_ITEMS / DESIGN_ONLY_NO_IMPLEMENTATION
Phase items adopted into this session:
Phase items explicitly out of scope:
Deferred or blocked phase items:
Coverage answer: YES / NO / PARTIAL / NOT_APPLICABLE
```

Fail-closed rules:

- `ADOPTED` is required before implementation readiness for delivery-governed implementation work.
- `NOT_APPLICABLE` is allowed only for non-implementation delivery-design or phase-contracting sessions that explicitly state no implementation is authorized.
- `BLOCKED`, missing adoption fields, multiple adopted active phase files, or mismatch with Current System State delivery pointers blocks implementation readiness.
- If adoption is partial, the Session Contract must record deferred or blocked phase items and must not claim full phase completion.


The classification result must appear in:

```text
_hirmos/session/SESSION_CONTRACT.md
_hirmos/session/SESSION_EXECUTION.md
_hirmos/session/session-contract-review.md
```

`SESSION_CONTRACT.md` contains the active session classification decision. `SESSION_EXECUTION.md` records that the gate was executed. `session-contract-review.md` reviews whether the classification safely prevented underplanning.

## Current System State pointer rule

`CURRENT_SYSTEM_STATE.md` must include the active delivery pointer set whenever delivery governance is active, a durable Delivery Plan exists, a phase remains active/blocked, or a next phase is recommended.

Required pointer fields:

```text
Delivery governance active: YES / NO / UNCERTAIN / NOT_APPLICABLE
Active delivery ID: <delivery-id>
Delivery plan: _hirmos/system/delivery/<delivery-id>/DELIVERY_PLAN.md
Active phase: _hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md
Active phase lifecycle status: NOT_STARTED / READY_FOR_ADOPTION / ACTIVE / BLOCKED / PARTIAL / READY_FOR_ACCEPTANCE / ACCEPTED / DEFERRED / SUPERSEDED / CANCELLED / NOT_APPLICABLE
Active phase type: GREENFIELD / BROWNFIELD / MIXED / UNKNOWN / NOT_APPLICABLE
Last accepted phase: <phase-id or none>
Last accepted session/archive: <archive path or none>
Next recommended phase: <phase-id or none>
Next governed command: hirmos start / hirmos status / hirmos continue / hirmos close / none
```

These are pointers only. Current System State must not duplicate the Delivery Plan or Phase contract content.

Close-time pointer update is mandatory when a session creates, updates, accepts, blocks, supersedes, or advances durable delivery artifacts. If delivery governance is not active, `CURRENT_SYSTEM_STATE.md` must say `NO` or `NOT_APPLICABLE` and must not retain stale active delivery pointers.

`hirmos start` and Understand System State must inspect these pointers before deciding that a new request is safe for a single-session path. `hirmos status` must use these pointers to report active delivery and next phase information.



## Phase Lifecycle State Model

Durable delivery governance uses the canonical phase lifecycle model defined in `_hirmos/core/protocol/PHASE_LIFECYCLE.md`.

Every durable `PHASE-xx.md` must declare:

```text
Lifecycle status: NOT_STARTED | READY_FOR_ADOPTION | ACTIVE | BLOCKED | PARTIAL | READY_FOR_ACCEPTANCE | ACCEPTED | DEFERRED | SUPERSEDED | CANCELLED
Phase type: GREENFIELD | BROWNFIELD | MIXED | UNKNOWN
```

`UNKNOWN` phase type blocks implementation readiness.

Implementation adoption is allowed only when lifecycle status is `READY_FOR_ADOPTION`, `ACTIVE`, or `PARTIAL`. `READY_FOR_ACCEPTANCE` may be used only for review/close-only sessions.

Greenfield phases activate MVP boundary, scope, architecture sequencing, and product-maturity controls. Brownfield phases activate preservation, regression, compatibility, and migration-safety controls. Mixed phases activate both control groups.

Current System State delivery pointers, the Delivery Plan phase row, and the adopted Phase file must agree on phase lifecycle status and phase type.

## Delivery / Phase Capability Routing

When Delivery-Need Classification is `YES`, Design must route capabilities through the durable delivery chain:

```text
delivery-design → phase-contracting → session-contract → implementation-readiness
```

Capability obligations:

- `delivery-design` owns creation or update of the durable Delivery Plan at `_hirmos/system/delivery/<delivery-id>/DELIVERY_PLAN.md`.
- `phase-contracting` owns creation or update of separate phase files under `_hirmos/system/delivery/<delivery-id>/phases/`.
- `session-contract` adopts one durable delivery slice or phase into `_hirmos/session/SESSION_CONTRACT.md` and records whether 100% of the active phase scope is covered.
- `implementation-readiness` blocks when the Delivery Plan, active phase file, or Session Contract adoption evidence is missing, placeholder-only, stale, or contradictory.

A single-session path may skip durable delivery capability routing only when the Delivery-Need Classification Gate records `NO` with affirmative single-session safety evidence.

An `UNCERTAIN` classification must route back to system-state understanding, requirements clarification, delivery-design, or user decision. It must not advance to implementation readiness.


## Close-Time Delivery Plan / Phase Status Update Enforcement

When delivery governance is active, required, created, changed, accepted, blocked, or advanced, `hirmos close` must treat Delivery Plan and Phase status updates as part of the close transaction, not as optional follow-up documentation.

Required close-time status authority chain:

```text
SESSION_CONTRACT.md Active Durable Phase Adoption
→ session-contract-review.md promised-vs-verified phase coverage
→ implementation-units/IU-xx.md unit review results
→ support/system-state-update.md Close-Time Delivery / Phase Status Transaction
→ _hirmos/system/delivery/<delivery-id>/DELIVERY_PLAN.md Delivery Status Update Log
→ _hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md Phase Acceptance Review
→ CURRENT_SYSTEM_STATE.md Active Development Context and Delivery Pointers
```

### Required status updates

Normal close is blocked unless each applicable durable delivery surface is updated or explicitly verified unchanged with evidence:

- the adopted `PHASE-xx.md` status is updated to `ACCEPTED`, `PARTIAL`, `BLOCKED`, `SUPERSEDED`, or left unchanged only with rationale;
- the parent `DELIVERY_PLAN.md` phase row and Delivery Status Update Log record the session outcome;
- `support/system-state-update.md` records the close-time Delivery / Phase Status Transaction;
- `CURRENT_SYSTEM_STATE.md` delivery pointers are refreshed to the resulting active delivery, active phase, last accepted phase, next recommended phase, and next governed command;
- unresolved phase carry-forward items are added to `CARRY_FORWARD.md` or the next phase contract.

### Fail-closed rule

Close is blocked if Delivery Plan status, Phase status, Session Contract adoption, session-contract-review verdict, implementation-unit review results, Current System State delivery pointers, and carry-forward obligations are missing, stale, or contradictory.

A chat summary, archive manifest, or session-local note cannot substitute for updating the durable Delivery Plan and active Phase file when delivery governance was active.

## Phase Entry Gate Routing

When Delivery-Need Classification is `YES`, durable delivery governance must route through a Phase Entry Gate before a session reaches implementation readiness.

Required routing:

```text
Delivery-Need Classification Gate
→ durable Delivery Plan
→ durable Phase file
→ Phase Entry Gate
→ Session Contract phase adoption
→ implementation readiness
```

The Phase Entry Gate must verify pointer concordance, lifecycle status, phase type, entry criteria, adoption constraints, type-specific greenfield/brownfield controls, and unresolved blockers. If the result is `BLOCKED` or `UNCERTAIN`, HIRMOS must not authorize implementation readiness.

For greenfield phases, entry requires bounded MVP/scope/architecture controls. For brownfield phases, entry requires preservation/regression/current-system controls. Mixed phases require both.

## Phase Progress / Carry-Forward Routing

Delivery governance must route every delivery-governed continuation and close through phase progress and carry-forward enforcement.

Required routing:

```text
Delivery-Need Classification YES
→ durable Delivery Plan
→ adopted PHASE-xx.md
→ Phase Entry Gate
→ Phase Progress Ledger
→ Carry-Forward Items when not ACCEPTED
→ Delivery Plan status update
→ CURRENT_SYSTEM_STATE.md active/next phase pointers
```

If a session closes a phase as `PARTIAL`, `BLOCKED`, or `DEFERRED`, `hirmos close` must require carry-forward obligations before close can be reported as normal. If the previous phase was partial, `hirmos start` and `hirmos continue` must inspect the Phase Progress Ledger before adopting or advancing further work.


## Phase Acceptance Routing

Delivery-governed close must route any proposed `ACCEPTED` phase outcome through the Phase Acceptance Evidence Gate. The accepted phase transition must be recorded consistently in `support/system-state-update.md`, the durable `PHASE-xx.md`, the durable `DELIVERY_PLAN.md`, and `CURRENT_SYSTEM_STATE.md` active/next phase pointers.

If acceptance evidence is incomplete, the phase result must remain `PARTIAL`, `BLOCKED`, `DEFERRED`, or another non-accepted lifecycle status with carry-forward obligations recorded.


## Phase Lifecycle Status Reporting

Delivery governance requires `hirmos status` to surface phase lifecycle reporting from durable authority, not from chat memory or session-local summaries. The status path is:

`CURRENT_SYSTEM_STATE.md` delivery pointers → `DELIVERY_PLAN.md` → active `PHASE-xx.md` → `SESSION_CONTRACT.md` adoption → `SESSION_EXECUTION.md` evidence → `session-contract-review.md` review → `support/system-state-update.md` close transaction.

The report must include phase lifecycle status, phase type, Phase Entry Gate status, Phase Progress Ledger status, Carry-Forward Items status, Phase Acceptance Evidence Gate status, blocked controls, pointer concordance, and exactly one recommended next command.

If the durable delivery chain is contradictory, report `Status Blocked By Phase Lifecycle Conflict`.
