# Delivery Governance Protocol

Status: core protocol.
Purpose: define how HIRMOS chooses the smallest sufficient governed delivery shape for greenfield, brownfield, and mixed work.


## PROD-L delivery scope direction

HIRMOS is migrating durable delivery governance to this canonical structure:

```text
_hirmos/system/delivery/
  DELIVERY_PLAN.md              # durable project delivery roadmap/register

  <delivery-id>/
    DELIVERY_SCOPE.md           # scoped authority for one delivery/release
    phases/
      PHASE-xx.md
```

`DELIVERY_PLAN.md` is append/update-oriented. It preserves completed, active, deferred, cancelled, and superseded deliveries. When later large greenfield, brownfield, or mixed work requires a new durable delivery, HIRMOS must add a new delivery entry and folder rather than overwrite the roadmap/register.

During the PROD-L migration, older per-delivery `DELIVERY_PLAN.md` layouts remain legacy-compatible. Later PROD-L phases will migrate templates, validators, and docs to the `DELIVERY_PLAN.md` + `<delivery-id>/DELIVERY_SCOPE.md` model.

## Core rule

HIRMOS must use the smallest governed delivery shape that preserves engineering quality, implementation truth, continuity, validation, and accepted-state integrity.

This rule applies equally to:

- greenfield work;
- brownfield work;
- mixed current-state-first work.

HIRMOS must not escalate work to multi-session delivery merely because it is greenfield, broad, or app-like. HIRMOS must also not force work into one session when the smaller shape would hide important risk, weaken validation, fragment accepted-state continuity, or make the work impossible to review safely.

## Delivery shape decision gate

Every implementation-capable `hirmos start` must answer this literal decision before implementation readiness:

```text
What is the smallest sufficient governed delivery shape for this request?
Answer: SINGLE_SESSION_VERTICAL_SLICE / SINGLE_SESSION_WITH_IMPLEMENTATION_UNITS / MULTI_SESSION_DELIVERY / MULTI_SESSION_DELIVERY_WITH_PHASE_FILES / UNCERTAIN.
Evidence:
Decision factors:
Smaller-shape safety analysis:
Larger-shape overhead analysis:
Required durable delivery artifacts, if any:
If UNCERTAIN, what must be inspected before deciding?
```

Fail-closed rules:

- `UNCERTAIN` blocks implementation readiness until the uncertainty is resolved.
- `SINGLE_SESSION_VERTICAL_SLICE` requires affirmative evidence that one bounded vertical slice can be designed, implemented, validated, reviewed, and closed safely.
- `SINGLE_SESSION_WITH_IMPLEMENTATION_UNITS` requires a Session Scope plus implementation units that collectively cover the authorized scope.
- `MULTI_SESSION_DELIVERY` requires a durable Delivery Plan under `_hirmos/system/delivery/<delivery-id>/DELIVERY_PLAN.md`.
- `MULTI_SESSION_DELIVERY_WITH_PHASE_FILES` requires a durable Delivery Plan and separate phase files under `_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md`.
- Missing delivery-shape decision is a fail-closed condition for implementation readiness.

Compatibility note: older artifacts may call this the `Delivery Shape Decision Gate`. New artifacts should use `Delivery Shape Decision Gate`. When both appear, the Delivery Shape Decision controls the result.

## Delivery shape options

### SINGLE_SESSION_VERTICAL_SLICE

Use when the request has one bounded objective, a narrow inspectable scope, low continuity risk, and can be completed with one Session Scope without separate implementation-unit decomposition.

### SINGLE_SESSION_WITH_IMPLEMENTATION_UNITS

Use when the work is nontrivial but still coherent enough to keep architecture, implementation, review, and close together in one governed session.

This is the preferred shape for many coherent MVP vertical slices when the model can safely design the whole slice and implement it with multiple implementation units.

### MULTI_SESSION_DELIVERY

Use when the work needs more than one accepted session, but separate phase files would add overhead without improving implementation truth or continuity. The durable Delivery Plan must define the delivery slices/units, sequence, accepted-state handoff, and next-session selection.

### MULTI_SESSION_DELIVERY_WITH_PHASE_FILES

Use when separate phase contracts materially improve safety, reviewability, or continuity. Phase files have a high threshold. They are justified when each phase needs its own durable contract, acceptance criteria, blockers, and close/update-state boundary.

## Escalation criteria

Escalate from a smaller shape only when the smaller shape would materially weaken at least one of:

- implementation truth;
- production-shaped engineering quality;
- reviewability;
- validation/evidence quality;
- continuity across sessions;
- accepted-state preservation;
- user decision safety;
- preservation/regression safety for existing systems.

If a larger shape is selected, HIRMOS must also explain why the smaller shape is insufficient.

## De-escalation criteria

Avoid multi-session delivery or phase files when:

- the work can be kept coherent as one vertical slice;
- implementation units can provide enough internal structure;
- phase files would split one architecture decision across multiple sessions unnecessarily;
- the user would pay governance overhead without better evidence or safer accepted state;
- the next session would mostly reconstruct context that could have stayed in one Session Scope.

## Greenfield considerations

Greenfield work often has broad unknowns, but greenfield status does not automatically require multi-session delivery.

For app/MVP work, first consider:

```text
SINGLE_SESSION_WITH_IMPLEMENTATION_UNITS
```

Use multi-session delivery only when the app cannot be implemented, validated, and reviewed coherently in one governed session, or when accepted increments are needed.

## Brownfield considerations

Brownfield work often has preservation and regression risk, but brownfield status does not automatically require multi-session delivery.

For targeted changes, prefer the smallest session shape that can prove preservation and implementation truth. Escalate when multiple modules, migrations, integrations, or behavioral preservation boundaries cannot be safely governed in one session.

## Universal escalation triggers

Escalation must be considered when:

- the user explicitly asks for a staged, phased, roadmap, or long-running delivery;
- scope cannot be completed and validated in one bounded session;
- unresolved decisions affect sequencing;
- work must be split into accepted increments;
- a future session must continue from a stable durable boundary;
- validation requires separate environments, roles, integrations, or evidence passes;
- brownfield preservation risk spans multiple areas;
- implementation is likely to exceed the context/attention budget of one session.

These are escalation triggers, not automatic phase-file requirements.

## Single-session eligibility

A request may proceed without a durable Delivery Plan only when all conditions are true:

1. The request has a bounded objective or coherent vertical slice.
2. The affected area is inspectable enough to govern safely.
3. Requirements fit into one Session Scope.
4. Implementation can be decomposed into implementation units if needed.
5. Validation and review can be completed before close.
6. No durable carry-forward boundary is needed before implementation begins.
7. Preservation/regression risk is low or fully covered by the Session Scope and evidence plan.
8. HIRMOS can explain why Delivery Plan/phase governance would add overhead without improving safety.

If any condition is false or uncertain, classification must not select a smaller shape without route-back or additional inspection.

## Banned delivery-shape justifications

HIRMOS must not justify delivery shape only with vague claims such as:

- seems manageable;
- can be handled in one pass;
- broad greenfield means phases;
- user asked to proceed now;
- no existing code means low risk;
- this is just planning;
- implementation can be refined later.

The decision must cite concrete boundedness, risk, validation, continuity, and accepted-state evidence.

## Required surfaces

The delivery-shape decision must appear in:

```text
_hirmos/session/SESSION_SCOPE.md
_hirmos/session/SESSION_EXECUTION.md
_hirmos/session/SESSION_SCOPE.md close verification
```

`SESSION_SCOPE.md` contains the active session delivery-shape authority. `SESSION_EXECUTION.md` records that the decision gate was executed. `SESSION_SCOPE.md` close verification reviews whether the selected shape safely prevented both underplanning and overplanning.

## Durable delivery artifacts

Durable delivery authority lives under:

```text
_hirmos/system/delivery/<delivery-id>/DELIVERY_PLAN.md
_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md
```

A durable Delivery Plan is required for `MULTI_SESSION_DELIVERY` and `MULTI_SESSION_DELIVERY_WITH_PHASE_FILES`.

Separate phase files are required only for `MULTI_SESSION_DELIVERY_WITH_PHASE_FILES`.

Session-local delivery artifacts are not canonical delivery authority. A session may reference or consume durable delivery artifacts, but it must not replace them with session-local phase plans, delivery status files, or informal chat summaries.

## Durable phase adoption rule

When the selected delivery shape is `MULTI_SESSION_DELIVERY_WITH_PHASE_FILES`, every implementation-capable session must adopt exactly one durable phase file before implementation readiness:

```text
_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md
```

The adoption must be explicit in `_hirmos/session/SESSION_SCOPE.md`; implicit references, chat statements, status summaries, or Current System State pointers are not enough.

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

- `ADOPTED` is required before implementation readiness for phase-governed implementation work.
- `NOT_APPLICABLE` is allowed only for non-implementation delivery-design or phase-contracting sessions that explicitly state no implementation is authorized.
- `BLOCKED`, missing adoption fields, multiple adopted active phase files, or mismatch with Current System State delivery pointers blocks implementation readiness.
- If adoption is partial, the Session Scope must record deferred or blocked phase items and must not claim full phase completion.

## Current System State pointer rule

`CURRENT_SYSTEM_STATE.md` must include the active delivery pointer set whenever durable delivery governance is active, a durable Delivery Plan exists, a phase remains active/blocked, or a next delivery slice/phase is recommended.

Required pointer fields:

```text
Delivery governance active: YES / NO / UNCERTAIN / NOT_APPLICABLE
Active delivery ID: <delivery-id>
Delivery plan: _hirmos/system/delivery/<delivery-id>/DELIVERY_PLAN.md
Active phase: _hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md or NOT_APPLICABLE
Active delivery shape: SINGLE_SESSION_VERTICAL_SLICE / SINGLE_SESSION_WITH_IMPLEMENTATION_UNITS / MULTI_SESSION_DELIVERY / MULTI_SESSION_DELIVERY_WITH_PHASE_FILES / UNKNOWN / NOT_APPLICABLE
Active phase lifecycle status: NOT_STARTED / READY_FOR_ADOPTION / ACTIVE / BLOCKED / PARTIAL / READY_FOR_ACCEPTANCE / ACCEPTED / DEFERRED / SUPERSEDED / CANCELLED / NOT_APPLICABLE
Last accepted delivery slice/phase: <id or none>
Last accepted session/archive: <archive path or none>
Next recommended delivery slice/phase: <id or none>
Next governed command: hirmos start / hirmos status / hirmos continue / hirmos close / none
```

These are pointers only. Current System State must not duplicate the Delivery Plan or Phase contract content.

Close-time pointer update is mandatory when a session creates, updates, accepts, blocks, supersedes, or advances durable delivery artifacts. If delivery governance is not active, `CURRENT_SYSTEM_STATE.md` must say `NO` or `NOT_APPLICABLE` and must not retain stale active delivery pointers.

## Delivery / Phase Capability Routing

When the selected delivery shape is `SINGLE_SESSION_VERTICAL_SLICE` or `SINGLE_SESSION_WITH_IMPLEMENTATION_UNITS`, Design may route directly through:

```text
session-scope → implementation-readiness
```

When the selected delivery shape is `MULTI_SESSION_DELIVERY`, Design must route through:

```text
delivery-design → session-scope → implementation-readiness
```

When the selected delivery shape is `MULTI_SESSION_DELIVERY_WITH_PHASE_FILES`, Design must route through:

```text
delivery-design → phase-contracting → session-scope → implementation-readiness
```

## Application vertical-slice reference target

For a broad application slice, the preferred HIRMOS target is not automatically multiple sessions. HIRMOS should first evaluate whether the whole bounded slice can be governed as one session with multiple implementation units:

```text
IU-01 app foundation, data model, and access control
IU-02 input workflow, durable job/state creation, and status surface
IU-03 provider/service boundary and persisted structured output
IU-04 user-facing results, generated output handling, and safety labels
IU-05 usage/limits/history/retry/hardening
```

Escalate only when evidence shows that this shape would weaken engineering quality, validation, continuity, or accepted-state preservation.


Single-session safety evidence now means bounded-scope safety evidence for `SINGLE_SESSION_VERTICAL_SLICE` or implementation-unit coverage for `SINGLE_SESSION_WITH_IMPLEMENTATION_UNITS`.


`hirmos start` and Understand System State must inspect these pointers before selecting a delivery shape or claiming implementation readiness.


## Close-Time Delivery Plan / Phase Status Update Enforcement

Close must update durable delivery status and Current System State pointers when durable delivery artifacts are active.


## Phase Entry Gate Routing

When phase files are selected, route through the Phase Entry Gate. If the result is `BLOCKED` or `UNCERTAIN`, implementation readiness is blocked.


## Preserved phase-governance controls

These controls remain active when the selected delivery shape uses durable phases or delivery status transitions.

### Required close-time status authority chain

Close is blocked if Delivery Plan status, phase status, Current System State delivery pointers, and the session close record are stale or contradictory. Close-time delivery updates remain mandatory whenever durable delivery artifacts are active.

### Phase Lifecycle State Model

Lifecycle status: NOT_STARTED | READY_FOR_ADOPTION | ACTIVE | BLOCKED | PARTIAL | READY_FOR_ACCEPTANCE | ACCEPTED | DEFERRED | SUPERSEDED | CANCELLED

Phase type: GREENFIELD | BROWNFIELD | MIXED | UNKNOWN

Greenfield phases activate MVP boundary, scope, architecture sequencing, and product-maturity controls. Brownfield phases activate preservation, regression, compatibility, and migration-safety controls. Mixed phases activate both control groups.

### Phase Entry Gate Routing

Delivery-Need Classification Gate is a legacy phrase for the Delivery Shape Decision Gate. When phase files are selected, the Phase Entry Gate must pass before implementation readiness. If the result is `BLOCKED` or `UNCERTAIN`, implementation readiness is blocked.


### Phase Progress / Carry-Forward Routing

When a phase-governed session results in PARTIAL, BLOCKED, or DEFERRED status, HIRMOS must preserve the Phase Progress Ledger, Carry-Forward Items, resulting lifecycle status, and explicit carry-forward target before close.

### Phase Acceptance Routing

Phase Acceptance Evidence Gate must be inspected before a phase is accepted. CURRENT_SYSTEM_STATE.md active/next phase pointers must be refreshed after acceptance.

### Phase Lifecycle Status Reporting

Status reporting must use CURRENT_SYSTEM_STATE.md` delivery pointers, Phase Progress Ledger status, and Status Blocked By Phase Lifecycle Conflict when phase lifecycle evidence is missing or contradictory.
