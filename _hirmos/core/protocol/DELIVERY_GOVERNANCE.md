# Delivery Governance Protocol

Status: core protocol.
Purpose: define how HIRMOS chooses the smallest sufficient governed delivery shape and how durable delivery roadmap/register, delivery scope, phase, and session-scope authority relate.

## Canonical delivery structure

HIRMOS durable delivery governance uses this canonical structure:

```text
_hirmos/system/delivery/
  DELIVERY_PLAN.md              # durable project delivery roadmap/register

  <delivery-id>/
    DELIVERY_SCOPE.md           # scoped authority for one delivery/release
    phases/
      PHASE-xx.md               # conditional phase scope when phase files are selected

    REQUIREMENTS.md             # optional independent requirements authority only when justified
    DESIGN.md                   # optional independent design authority only when justified
```

`DELIVERY_PLAN.md` is append/update-oriented. It preserves completed, active, planned, deferred, cancelled, blocked, and superseded deliveries. When any later durable multi-session work requires a new delivery, HIRMOS must add a new delivery entry and folder rather than overwrite the roadmap/register. This applies equally to new-product work, existing-system change, mixed work, migrations, hardening releases, and other project contexts.

`DELIVERY_SCOPE.md` is the default combined scoped authority for one durable delivery/release. It contains the delivery outcome, scoped requirements, governing design decisions, production-shaped engineering gate, phase plan, session adoption rules, evidence requirements, and delivery-close verification.

Separate delivery-level `REQUIREMENTS.md` and `DESIGN.md` remain conditional, not default. Use them only when independent requirements/design authority is justified by compliance, complexity, shared authority across deliveries, explicit user request, or a dedicated requirements/design session.

## Core rule

HIRMOS must use the smallest governed delivery shape that preserves engineering quality, implementation truth, continuity, validation, accepted-state integrity, and practical user interaction cost.

This rule is project-type neutral and run-purpose neutral. HIRMOS always chooses delivery shape for the real software work at hand; it must not choose a heavier or different shape because the framework is being tested, inspected, or dogfooded. Framework maintainers evaluate HIRMOS through artifacts, transcript review, validation, and repeated real-work runs; HIRMOS itself must not create a separate testing lane.

Multi-session delivery is selected because the work needs durable multi-session governance, not because the project is labeled greenfield, brownfield, large, app-like, existing-system work, or framework evaluation.

HIRMOS must not escalate work to multi-session delivery merely because it is greenfield, broad, app-like, or being used for framework validation. HIRMOS must also not force work into one session when the smaller shape would hide important risk, weaken validation, fragment accepted-state continuity, or make the work impossible to review safely.

## Delivery shape decision gate

Every implementation-capable `hirmos start` must answer this literal decision before implementation readiness:

```text
What is the smallest sufficient governed delivery shape for this request?
Answer: SINGLE_SESSION_VERTICAL_SLICE / SINGLE_SESSION_WITH_IMPLEMENTATION_UNITS / MULTI_SESSION_DELIVERY / MULTI_SESSION_DELIVERY_WITH_PHASE_FILES / UNCERTAIN.
Evidence:
Decision factors:
Technically possible simpler shape:
Why simpler shape is acceptable or insufficient:
Why selected shape is necessary for this real software work:
Larger-shape overhead analysis:
User interaction / token-cost impact:
Required durable delivery artifacts, if any:
If multi-session is selected, smallest honest phase count:
Phase-count options considered:
Why fewer phases are insufficient or acceptable:
Why the selected phase count is the smallest honest count:
Phase merge pressure applied:
Phase-count user interaction / token-cost impact:
Risk if compressed into fewer phases:
If UNCERTAIN, what must be inspected before deciding?
```

Fail-closed rules:

- `UNCERTAIN` blocks implementation readiness until the uncertainty is resolved.
- `SINGLE_SESSION_VERTICAL_SLICE` requires affirmative evidence that one bounded vertical slice can be designed, implemented, validated, reviewed, and closed safely.
- `SINGLE_SESSION_WITH_IMPLEMENTATION_UNITS` requires a Session Scope plus implementation units that collectively cover the authorized scope.
- `MULTI_SESSION_DELIVERY` requires a delivery baseline route that creates/updates `_hirmos/system/delivery/DELIVERY_PLAN.md` and `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md` before any session scope is created.
- `MULTI_SESSION_DELIVERY_WITH_PHASE_FILES` requires a delivery baseline route with a complete phase coverage plan in `DELIVERY_SCOPE.md`; concrete `PHASE-xx.md` files are instantiated just in time after delivery-baseline acceptance, starting with the next active phase/session.
- Missing delivery-shape decision is a fail-closed condition for implementation readiness.
- When a multi-session delivery shape is selected, missing phase-count justification is a fail-closed condition for delivery baseline readiness.

Compatibility note: older artifacts may call this the `Delivery Shape Decision Gate`. New artifacts should use `Delivery Shape Decision Gate`. When both appear, the Delivery Shape Decision controls the result.

## Delivery shape options

### SINGLE_SESSION_VERTICAL_SLICE

Use when the request has one bounded objective, a narrow inspectable scope, low continuity risk, and can be completed with one Session Scope without separate implementation-unit decomposition.

### SINGLE_SESSION_WITH_IMPLEMENTATION_UNITS

Use when the work is nontrivial but still coherent enough to keep architecture, implementation, review, and close together in one governed session.

This is the preferred shape for many coherent MVP vertical slices when the model can safely design the whole slice and implement it with multiple implementation units.

### MULTI_SESSION_DELIVERY

Use when the work needs more than one accepted session, but separate phase files would add overhead without improving implementation truth or continuity. The durable Delivery Plan indexes the delivery, and the delivery's `DELIVERY_SCOPE.md` defines delivery scope, requirements, decisions, acceptance, and next-session selection.

### MULTI_SESSION_DELIVERY_WITH_PHASE_FILES

Use when separate phase scopes materially improve safety, reviewability, or continuity. Phase files have a high threshold. They are justified when each phase needs its own durable contract, acceptance criteria, blockers, and close/update-state boundary. Phase files must not be used to create thin governance checkpoints that could be merged without losing honest validation, reviewability, continuity, or accepted-state integrity.

## Escalation criteria

Escalate from a smaller shape only when the smaller shape would materially weaken implementation truth, production-shaped engineering quality, reviewability, validation/evidence quality, continuity across sessions, accepted-state preservation, user decision safety, or preservation/regression safety for existing systems.

If a larger shape is selected, HIRMOS must also explain why the smaller shape is insufficient for the real software work and why the added governance overhead is worth the user interaction and token cost.

## De-escalation criteria

Avoid multi-session delivery or phase files when the work can be kept coherent as one vertical slice, implementation units provide enough internal structure, phase files would split one architecture decision unnecessarily, or the user would pay governance/token overhead without better evidence, safer accepted state, or materially clearer implementation boundaries.


## Delivery shape honesty and cost-aware routing

Delivery shape selection must be honest to the project, not optimized for framework inspection. HIRMOS must behave the same way for a real user request whether or not a maintainer later audits the run.

When recommending a delivery shape, HIRMOS must surface a compact tradeoff summary:

```text
Recommended delivery shape:
Technically possible simpler shape:
Why simpler shape is acceptable or insufficient:
Why heavier shape is justified, if selected:
User interaction / token-cost impact:
Risk if compressed into a smaller shape:
Artifact paths created only if selected shape requires them:
```

Token and interaction cost are secondary to honest delivery shape, but they are real user costs. HIRMOS must not spend them on avoidable governance surfaces when a simpler governed shape preserves implementation truth, reviewability, validation, continuity, and accepted-state integrity.

## Phase-count honesty and merge pressure

When multi-session delivery is selected, HIRMOS must choose the fewest phases that preserve honest execution, review, validation, continuity, and accepted-state update. Multi-session is a capability, not a default cost center.

A separate phase is justified only when it provides at least one material benefit:

- independent user-visible value;
- independent runtime validation boundary;
- meaningful architectural or provider-risk isolation;
- dependency sequencing that cannot be safely combined;
- human approval point that materially affects downstream work;
- separate close/evidence posture that would be dishonest if merged.

A proposed phase is weak and should be merged when it is mainly:

- a thin wrapper around one small feature;
- setup, smoke, or evidence cleanup that can be resolved during the current session or close;
- provider setup that can be included in the implementation phase it enables;
- UI polish that can be bundled with the user-facing workflow phase;
- carry-forward cleanup that close-time triage can resolve or classify before close.

Every phase after phase 2 must pass explicit merge pressure:

```text
Can this phase be merged into an earlier or later phase without losing honest validation, reviewability, continuity, or accepted-state integrity?
Answer: YES / NO.
If YES, merge it.
If NO, explain the material boundary that requires keeping it separate.
```

When recommending phases, HIRMOS must surface a compact phase-count summary:

```text
Phase count considered:
2 phases: accepted/rejected because...
3 phases: accepted/rejected because...
4+ phases: accepted/rejected because...
Selected phase count:
Why this count is the smallest honest count:
Phase merge pressure result:
Cost / interaction impact:
Risk if compressed further:
```

HIRMOS must not casually choose 4, 5, or 6 phases when 2 or 3 phases would preserve honest delivery. Larger phase counts require explicit evidence that the additional pauses and artifacts materially improve implementation truth, validation, continuity, or user decision safety.


## Delivery activation and update rules

```text
If request fits current active delivery:
  update/adopt existing DELIVERY_SCOPE.md / phase / SESSION_SCOPE.md.

If request is a bounded single-session change:
  use SESSION_SCOPE.md only; no new delivery.

If request is durable multi-session work:
  add a new delivery entry to DELIVERY_PLAN.md and create <delivery-id>/DELIVERY_SCOPE.md.
```

A new delivery should be created only when the new request is materially larger than a single governed session or current active delivery can safely absorb.


## Delivery navigation and next-delivery selection

`DELIVERY_PLAN.md` and `CURRENT_SYSTEM_STATE.md` must make delivery-to-delivery continuation explicit. Domain Expert users are not expected to say that HIRMOS should plan deliveries or start the next planned delivery; HIRMOS infers delivery navigation from accepted state and the delivery roadmap/register.

Required pointer fields:

- Last accepted delivery
- Active delivery ID
- Active delivery scope
- Next recommended delivery
- Next recommended delivery scope
- Next recommended phase, when phase files are active
- Next governed command

Close-time pointer update is mandatory when a session accepts, partially accepts, blocks, defers, supersedes, cancels, or advances a delivery. If one delivery is accepted and the Delivery Index contains a planned follow-up delivery whose relationship follows, depends on, or is sequenced after the accepted delivery, `hirmos close` must update `CURRENT_SYSTEM_STATE.md` with `Next recommended delivery` and `Next recommended delivery scope`, or explicitly record why no next delivery is recommended.

`hirmos start` and Understand System State must inspect these pointers before selecting a delivery shape. If `CURRENT_SYSTEM_STATE.md` identifies a `Next recommended delivery` and the user request is absent, broad, or compatible with continuing planned work, `hirmos start` must adopt that delivery context before considering a single-session path. If the user request is clearly unrelated, HIRMOS must record the override rationale before ignoring the recommendation.

A project may start with multiple planned deliveries, and later add another durable delivery for a major change, migration, hardening pass, release, or other multi-session need. HIRMOS must preserve the existing roadmap and add the new delivery; it must not overwrite historical delivery entries.

## Delivery / Phase Capability Routing

When durable delivery governance is selected, capability routing is focus-aware:

```text
DELIVERY_BASELINE / delivery_baseline
  delivery-baseline

DELIVERY_PHASE_SESSION / phase_session_baseline
  phase-baseline → session-scope → implementation-readiness
```

- `delivery-baseline` creates or updates `_hirmos/system/delivery/DELIVERY_PLAN.md`, `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md`, `_hirmos/system/delivery/<delivery-id>/unresolved-items.md`, and optional delivery-level `REQUIREMENTS.md` / `DESIGN.md` only when justified.
- `delivery-baseline` must stop at `Delivery Baseline — Review or Change`; it must not create `SESSION_SCOPE.md`, `PHASE-xx.md`, or implementation units before baseline acceptance by default.
- `phase-baseline` runs only after delivery-baseline acceptance or amendment. It instantiates the next needed `PHASE-xx.md` when phase files are selected and prepares the bounded phase/session authority.
- `phase-baseline` must write a scalar `Entry criteria status` field in the instantiated phase and refresh `DELIVERY_PLAN.md`, `SESSION_EXECUTION.md`, and Current System State delivery pointers so post-continue artifacts do not retain delivery-baseline-only `PENDING`, `NOT_APPLICABLE`, or `Current phase: none` values.
- `session-scope` adopts and narrows the accepted `DELIVERY_SCOPE.md` and, when applicable, the active `PHASE-xx.md` into `_hirmos/session/SESSION_SCOPE.md`.
- `implementation-readiness` verifies the focus-specific authority chain and blocks implementation when required artifacts are missing, stale, contradictory, placeholder-only, or not accepted/amended.

For single-session work, `session-scope` must record affirmative single-session safety evidence instead of silently skipping durable delivery governance. For minimal non-implementation work, HIRMOS creates only the minimal authority required by the requested output.

## Delivery Scope rules

`DELIVERY_SCOPE.md` must define:

- authorized delivery outcome;
- scoped requirements;
- design and engineering decisions;
- production-shaped engineering gate;
- phase plan when phase files are used;
- session adoption rules;
- evidence and acceptance requirements;
- delivery close verification.

Sessions may not silently expand a delivery. Material additions must update `DELIVERY_SCOPE.md`, create a new delivery, or be recorded as unresolved/carry-forward.

## Phase rules

`PHASE-xx.md` is optional and conditional. It is used only when separate phase scopes materially improve continuity, acceptance, or evidence.

A phase must adopt from `DELIVERY_SCOPE.md`, not from a per-delivery `DELIVERY_PLAN.md`. The phase file records entry criteria, exit criteria, included/excluded scope, adoption constraints, evidence requirements, carry-forward, and close-time status transaction.

Implementation adoption may use only `READY_FOR_ADOPTION`, `ACTIVE`, or `PARTIAL`. Review/close-only work may use `READY_FOR_ACCEPTANCE`. `UNKNOWN`, `NOT_STARTED`, `BLOCKED`, `ACCEPTED`, `DEFERRED`, `SUPERSEDED`, or `CANCELLED` does not authorize implementation readiness.

## Session adoption rules

A delivery-governed `SESSION_SCOPE.md` must include pointers to:

```text
Delivery roadmap: _hirmos/system/delivery/DELIVERY_PLAN.md
Delivery scope: _hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md
Active phase: _hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md or NOT_APPLICABLE
```

The session must adopt and narrow, not duplicate the whole delivery. It must define exactly what the active session may implement, preserve, exclude, and validate.

## Accepted-state pointer rules

`CURRENT_SYSTEM_STATE.md` should summarize delivery state and point to durable authority without duplicating it:

```text
Delivery roadmap:
- _hirmos/system/delivery/DELIVERY_PLAN.md

Completed deliveries:
- mvp: _hirmos/system/delivery/mvp/DELIVERY_SCOPE.md

Active delivery:
- major-brownfield-change: _hirmos/system/delivery/major-brownfield-change/DELIVERY_SCOPE.md
```

For no durable delivery, accepted state does not need delivery pointers. When durable delivery governance exists, accepted state must include last accepted delivery and next recommended delivery pointers whenever those values are known.

## Close rules

A delivery-governed close must verify:

- delivery navigation pointers are refreshed in both `DELIVERY_PLAN.md` and `CURRENT_SYSTEM_STATE.md`;
- accepted deliveries are recorded as `Last accepted delivery` when applicable;
- planned follow-up deliveries are recorded as `Next recommended delivery` when applicable;


- `SESSION_SCOPE.md` satisfied or partial/blocked truthfully recorded;
- implementation units and evidence match the accepted claims;
- adopted `DELIVERY_SCOPE.md` and phase status are updated when applicable;
- `DELIVERY_PLAN.md` roadmap/register reflects active/completed/deferred/superseded delivery state;
- carry-forward and unresolved items are recorded;
- `CURRENT_SYSTEM_STATE.md` delivery pointers are refreshed.

## Canonical delivery authority paths

New templates, docs, validators, and command guidance use only the canonical delivery authority paths:

```text
_hirmos/system/delivery/DELIVERY_PLAN.md
_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md
_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md
```


## Current System State pointer rule

Required pointer fields must include delivery governance active, delivery roadmap, active delivery scope, active phase when applicable, active phase lifecycle status, active phase type, next recommended phase, and pointer consistency result. Close-time pointer update is mandatory. `hirmos start` and Understand System State must inspect these pointers before deciding whether the request fits an active delivery, needs a new delivery, or can remain single-session.

## Durable Phase Adoption Rule

When phase files are used, `SESSION_SCOPE.md` must adopt exactly one durable phase file before implementation unless adoption is explicitly `NOT_APPLICABLE`. Adoption status: ADOPTED / NOT_APPLICABLE / BLOCKED. Multiple adopted active phase files are blocked unless the session is explicitly review-only and records why implementation is not authorized.


## Close-Time Delivery Plan / Phase Status Update Enforcement

Required close-time status authority chain: `SESSION_SCOPE.md` → `PHASE-xx.md` when applicable → `DELIVERY_SCOPE.md` → `DELIVERY_PLAN.md` → `CURRENT_SYSTEM_STATE.md`. Close is blocked if Delivery Plan status, Delivery Scope status, phase status, or current-system-state delivery pointers contradict the accepted close verdict.

## Phase Lifecycle State Model

Lifecycle status: NOT_STARTED | READY_FOR_ADOPTION | ACTIVE | BLOCKED | PARTIAL | READY_FOR_ACCEPTANCE | ACCEPTED | DEFERRED | SUPERSEDED | CANCELLED. Phase type: GREENFIELD | BROWNFIELD | MIXED | UNKNOWN. Greenfield phases activate greenfield controls. Brownfield phases activate preservation/regression controls. Mixed phases activate both control groups. `UNKNOWN` blocks implementation readiness.


## Phase Entry Gate Routing

Delivery-Need Classification Gate must route phase-backed work through the Phase Entry Gate. If the result is `BLOCKED` or `UNCERTAIN`, implementation readiness is blocked. Phase Entry Gate decisions must inspect lifecycle status and phase type.

## Phase Progress / Carry-Forward Routing

Phase Progress Ledger and Carry-Forward Items must be reconciled before continuation or close. CURRENT_SYSTEM_STATE.md active/next phase pointers must agree with phase progress and carry-forward state.

## Phase Acceptance Routing

Phase Acceptance Evidence Gate must be evaluated before marking phase work accepted. CURRENT_SYSTEM_STATE.md active/next phase pointers must be refreshed after acceptance.

## Phase Lifecycle Status Reporting

Status output must report CURRENT_SYSTEM_STATE.md` delivery pointers, Phase Progress Ledger status, Phase Acceptance Evidence Gate status, and Status Blocked By Phase Lifecycle Conflict when authorities disagree.

## PROD-L8.9 runtime command and capability route binding

Delivery governance is enforced at runtime through command behavior and focus-aware capability routing, not by static artifact names alone.

The focus-aware route binding is:

```text
SINGLE_SESSION_MINIMAL / minimal_session
  session-scope only when bounded output authority is needed

SINGLE_SESSION_VERTICAL_SLICE / session_baseline
  session-scope → implementation-readiness

SINGLE_SESSION_WITH_IMPLEMENTATION_UNITS / session_baseline
  session-scope → implementation-readiness

DELIVERY_BASELINE / delivery_baseline
  delivery-baseline

DELIVERY_PHASE_SESSION / phase_session_baseline
  phase-baseline → session-scope → implementation-readiness
```

Runtime commands must use this binding when deciding which artifacts to instantiate, which capability entrypoints to read, what can be claimed at user-facing checkpoints, and what close must reconcile.

`delivery-baseline` must append/update the top-level `DELIVERY_PLAN.md` roadmap/register and create/update one delivery's `DELIVERY_SCOPE.md`, delivery unresolved register, and optional delivery requirements/design when justified. It must not overwrite prior deliveries.

`phase-baseline` may create/update `PHASE-xx.md` only after delivery-baseline acceptance or amendment and only for the next needed active phase/session by default. Future phase files remain uninstantiated until needed unless a narrow exception is justified.

`session-scope` must adopt and narrow accepted delivery/phase authority. It must not duplicate full delivery authority inside the active session.

`implementation-readiness` must fail closed when the selected focus route's authority chain is missing, contradictory, placeholder-only, or not accepted/amended.


## PROD-L8.10 Delivery-Baseline Surface Minimality

Delivery-baseline planning uses the runtime session envelope but delivery authority owns the governed content. During `session_focus = delivery_baseline`, `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md` is the active authority and `_hirmos/system/delivery/<delivery-id>/unresolved-items.md` is the unresolved register. `_hirmos/session/SESSION_SCOPE.md` and `_hirmos/session/unresolved-items.md` are not applicable and must not be created as placeholders. This rule is project-agnostic and applies to any durable delivery, regardless of domain, project type, or feature set.

## PROD-L8.11 Delivery-Baseline Optional Authority Location

When `SESSION_STATE.json.session_focus = delivery_baseline`, the active authority is delivery-level. Optional requirements/design authority must be located under `_hirmos/system/delivery/<delivery-id>/` only:

- `_hirmos/system/delivery/<delivery-id>/REQUIREMENTS.md` when separate delivery-level requirements authority is justified.
- `_hirmos/system/delivery/<delivery-id>/DESIGN.md` when separate delivery-level design authority is justified.

During `delivery_baseline`, HIRMOS must not create, update, list, or depend on `_hirmos/session/REQUIREMENTS.md` or `_hirmos/session/DESIGN.md`. If separate optional authority is not justified, requirements and design decisions remain inside `DELIVERY_SCOPE.md` only. Session-level optional authority artifacts become applicable only after the flow advances to a bounded `phase_session_baseline` or `session_baseline` focus.


## PROD-L8.13 Delivery Review Wording and Current-State-First Generated Artifacts

Delivery artifacts and checkpoints must be status-aware. Before a delivery baseline is accepted, generated text must describe the delivery as a Candidate Delivery, Proposed Delivery, or Delivery Under Baseline Review. `Active Delivery` is reserved for post-acceptance delivery states such as `ACTIVE`, `ACCEPTED`, `PARTIAL`, `BLOCKED`, or accepted carry-forward work.

Generated artifacts must explain delivery shape from current-state-first evidence: inspected system state, scope size, governance need, validation risk, continuity need, authority boundaries, and practical user interaction/token cost. Project-type labels such as greenfield, brownfield, mixed, or unknown may be recorded as supporting evidence metadata or phase-control routing metadata, but they must not be the primary user-facing justification for delivery governance, session scope, or phase creation. Framework testing, inspection, or dogfood context must not be used as a reason to select a heavier delivery shape.

When the delivery status is `READY_FOR_BASELINE_REVIEW`, the roadmap/register may identify the candidate delivery and its delivery authority, but it must not imply implementation authority. Implementation remains unauthorized until the delivery baseline is accepted/amended and narrowed into phase/session authority.
