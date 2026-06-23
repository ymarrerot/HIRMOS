# First Real Run

This page shows a realistic first HIRMOS run for a broad application slice: a broad production-shaped web application slice with authentication, persistence, provider boundaries, usage limits, delayed processing, and user-facing results.

The point of this example is not to show a finished implementation. The point is to show what a serious `hirmos start` run should produce before implementation begins.

## Example request

```text
hirmos start "Build a production-shaped MVP slice for a web application. Users should be able to submit domain data, process it through a provider-backed workflow, view persisted results on mobile, sign in, use a bounded usage allowance, recover from failures, and preserve provider boundaries. External billing is not required in the first implementation."
```

The request is intentionally broad. A strong HIRMOS run should not jump directly into code. It should first understand the current project state, identify design decisions that materially affect architecture or acceptance criteria, define a bounded session, and pause before implementation.

## 1. User Request

HIRMOS treats the request and any uploaded notes, requirements, screenshots, prototypes, tickets, code samples, or existing docs as source inputs.

Source inputs guide attention, but they are not final authority. HIRMOS must reconcile them through governed session artifacts before implementation.

For this example, the source input says the MVP should include:

- a landing page that explains the product and labels generated outputs as representative;
- mobile source-material upload or capture;
- AI/provider-assisted source interpretation;
- representative generated-output creation for recognized structured items;
- a mobile results surface;
- sign-up/sign-in;
- usage allowance tracking;
- persistent jobs, results, and recent history;
- visible failure states and recovery where reasonable;
- a real database;
- environment variables for provider secrets;
- isolated provider-specific logic;
- no external billing integration in the first implementation.

A good run should preserve the important product truth that generated outputs are representative, not exact source-material replicas.

## 2. Understand System State

Before Design, HIRMOS should establish:

- general system state;
- request-focused system state;
- project type based on evidence;
- stack evidence;
- source material inventory;
- observed, inferred, assumed, and unknown items;
- current-state confidence;
- findings that Design must account for.

For a greenfield project, this may mean recording that no meaningful app exists yet and that the uploaded requirements define the initial design problem.

For a brownfield project, this means inspecting the current app, routes, auth model, database schema, provider integrations, job-processing code, and UI surfaces before designing changes.

For a mixed project, this means preserving what exists while designing the new workflow around it.

A strong run should not assume the project is greenfield merely because the request describes a new product. It should decide project type from the working copy.

## 3. Design

Design owns governed requirements, system/application design, session scope, unresolved-item disposition, technical review information, and implementation readiness.

For this example, the Design stage should recognize that the request is too large for careless one-shot implementation. It crosses product UX, auth, persistence, job processing, provider boundaries, usage allowances, error handling, and mobile UI.

A good Design result should decide whether the work can fit into one bounded session. For a broad application slice, a strong result should first evaluate a single governed session with implementation units before escalating to a multi-session delivery:

```text
Delivery decomposition: evaluate smallest sufficient governed delivery shape.
Reason: the slice spans multiple risk areas: auth, durable job state, usage accounting, provider isolation, generated-output creation, and mobile results UX.

Recommended delivery shape:
- Prefer one bounded session with implementation units if that preserves engineering quality and validation.
- Escalate to multi-session delivery only if one session would weaken quality, continuity, evidence, or accepted-state preservation.
```

### Example capability routing outcome

A `hirmos start` run should resolve capabilities through the canonical routing path:

```text
CAPABILITY_ROUTING.md
→ extension.json
→ extension/entrypoints/default.md
→ capability.json
→ capability/entrypoints/default.md
```

For this example, a reasonable Design routing decision would include:

```text
requirements-design: REQUIRED
Reason: source input contains product requirements that must become governed requirements authority.

system-design: REQUIRED
Reason: auth, jobs, usage allowances, persistence, and provider boundaries require architecture decisions.

delivery-design: CONDITIONAL
Reason: the request is larger than a trivial change; choose the smallest sufficient governed delivery shape.

session-scope: REQUIRED
Reason: implementation must be bounded before `hirmos continue`.

implementation-readiness: BLOCKED
Reason: gated user-owned decisions remain unresolved.
```

### Example `unresolved-items.md` outcome

HIRMOS should not flood the register with every preference. It should record only items that materially affect architecture, scope, implementation order, acceptance criteria, or future production readiness.

A strong run should separate gated decisions from non-gating assumptions.

#### Gated decisions

These block full implementation authorization, or block specific implementation slices, until answered.

```text
GATED-1 — Upload requires sign-in or allows anonymous preview
Question: Should users be required to sign in before uploading source material, or should the MVP allow a limited anonymous preview/trial before sign-in?
Why it matters: affects routing, job ownership, usage checks, history, and first-use UX.
Default if resolved conservatively: require sign-in before upload for the first bounded slice.

GATED-2 — Real providers or provider-ready fallback first
Question: Should the first implementation call real external providers, or implement provider interfaces with deterministic/local fallback behavior until credentials are configured?
Why it matters: affects environment setup, acceptance claims, failure modes, validation, and cost controls.
Default if resolved conservatively: implement provider boundaries and safe fallback behavior; do not claim real provider output unless credentials are configured and validated.

GATED-3 — Background processing depth
Question: Does the bounded slice require real queue-backed processing now, or is durable job state with a lightweight worker/cron/polling-compatible processor acceptable for the first implementation?
Why it matters: affects hosting assumptions, data model, retry behavior, and refresh survival.
Default if resolved conservatively: persist job state and status; use the lightest processor that preserves production shape.

GATED-4 — Database/runtime target
Question: What database/runtime environment should this implementation target, and is a local database available for validation?
Why it matters: the bounded slice requires users, jobs, usage allowances, and results to be persisted and validated.
Default if resolved conservatively: use the same database class locally that is recommended for production.

GATED-5 — Processing limit
Question: What maximum number of structured items or generated outputs should be processed per job in the first bounded slice?
Why it matters: affects cost, runtime duration, result UX, and acceptance criteria.
Default if resolved conservatively: process a bounded number of outputs per job, show a clear limit message, and preserve the unprocessed remainder count.

GATED-6 — Minimum retention/privacy posture
Question: What minimum upload retention, generated-output retention, deletion, and abuse/moderation controls are required for the bounded slice?
Why it matters: the app accepts user-supplied source material and may store generated outputs.
Default if resolved conservatively: retain only what is needed for job/result history, avoid public sharing, and document production privacy controls as not complete.
```

#### Non-gating assumptions

These are safe to carry for a first bounded slice as long as they remain visible and are revalidated later.

```text
ASSUMPTION-1 — Responsive web app, not native mobile
The example app is a mobile-first responsive web app, not a native iOS/Android app.

ASSUMPTION-2 — Representative output labeling
Generated outputs must be labeled as representative and not exact source-material replicas.

ASSUMPTION-3 — No real checkout in first implementation
Usage allowance accounting is in scope, but external billing integration is explicitly out of scope for the first implementation.

ASSUMPTION-4 — Usage consumed per generated output
Usage is consumed per generated output, with job-level accounting recorded for support.

ASSUMPTION-5 — Recent history only
History means signed-in users can view recent jobs/results, not a full archive/search/export system.

ASSUMPTION-6 — Basic support visibility
Operator/support visibility means job id, status, timestamps, provider error category, retry state, and usage events. It is not a full observability platform.

ASSUMPTION-7 — Bounded extraction is acceptable
The bounded slice preserves extracted structured items and useful descriptions where available, but does not require perfect extraction correction or complete manual editing in the first slice.

ASSUMPTION-8 — Provider details remain configurable
Provider credentials, model names, callback URLs, rate limits, and production launch settings remain behind environment variables and provider adapters.
```

### Example bounded `SESSION_SCOPE.md` outcome

A strong run should define a bounded contract rather than treating the whole product description as one implementation task.

```text
Session Scope Status: BLOCKED_FOR_GATED_DECISIONS

Authorized after gated decisions are resolved:
- Mobile-first landing page and upload/capture entry point.
- Signed-in user flow, if sign-in-before-upload is accepted.
- Real database schema for users, jobs, results, usage ledger, and usage allowance.
- Durable job status that survives refresh.
- Provider adapter interfaces for source interpretation and generated-output creation.
- Safe fallback behavior when provider credentials are unavailable.
- Visual results surface with representative-output labeling.
- Basic recent history for signed-in users.
- Visible failure and retry/recovery states where reasonable.

Out of scope for the first implementation:
- External billing integration.
- Full admin/support console.
- Native mobile apps.
- Production-grade moderation and retention policy beyond bounded-slice safeguards.
- Perfect extraction correction or complete manual editing.
- Unlimited item processing.
```

### Example implementation units

Even before implementation begins, HIRMOS should propose coherent implementation units.

```text
IU-01 — App foundation, auth, and database schema
Goal: establish signed-in user ownership, jobs, results, usage allowance, and usage ledger.

IU-02 — Upload/capture and durable job creation
Goal: accept source material, create a persisted job, show loading/status, and survive refresh.

IU-03 — Source interpretation provider boundary
Goal: isolate provider-assisted interpretation behind an adapter, store structured outputs, and expose useful failure states.

IU-04 — Generated-output provider boundary and cost guardrails
Goal: generate or safely fallback representative outputs for a bounded item subset and consume usage correctly.

IU-05 — Mobile results, recent history, and retry UX
Goal: show processed results, recent jobs, status/error detail, and reasonable retry/recovery behavior.

IU-06 — Validation and evidence review
Goal: validate auth ownership, job persistence, usage accounting, failure handling, mobile rendering, and secrets/provider boundaries.
```

## 4. Implementation

Implementation activates only when accepted Design authorizes governed realization.

For this example, `hirmos start` should pause before implementation. It should not modify app files yet unless the command explicitly allows a non-implementation preparatory artifact update.

A correct checkpoint would say something like:

```text
Implementation Status: NOT_STARTED
Reason: `hirmos start` completed Understand System State and Design planning, but implementation is not authorized until gated decisions are resolved and the Session Scope is accepted.
```

A good implementation run later should use bounded implementation units. Each unit should define:

- in scope;
- out of scope;
- files or behavior targeted;
- constraints;
- validation/evidence requirements;
- binary acceptance criteria;
- review expectations.

## 5. Update System State

A session should not close by simply saying the work is done. HIRMOS should run Update System State when ready:

- record accepted outcomes;
- record rejected or not-applied outcomes;
- carry forward unresolved items;
- archive the session;
- prepare future sessions with accurate current state.

For the initial `hirmos start` example, Update System State is not reached yet because implementation has not begun.

## What to inspect after `hirmos start`

A strong first run should leave inspectable artifacts such as:

- `SESSION_SCOPE.md` as the active session authority
- `SESSION_EXECUTION.md` with the Current Continuation Snapshot and command timeline
- `unresolved-items.md` for gated, non-gating, and technical-review items
- `EVIDENCE.md` when nontrivial evidence is needed
- `implementation-units/IU-xx.md` files when implementation units are justified
- conditional `DESIGN.md` or `REQUIREMENTS.md` only when separate design or requirements authority is justified

For larger work, also inspect:

- `_hirmos/system/delivery/DELIVERY_PLAN.md`
- `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md`
- `_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md` when phase files are used

Do not count a checkpoint as trustworthy unless the referenced artifacts exist and contain non-placeholder content.

## What good behavior looks like

A strong first real run should not feel magical or hidden. It should be transparent enough that you can answer:

- What did HIRMOS inspect?
- What project type and stack did it infer from evidence?
- Which capabilities activated and why?
- What is in scope now?
- What is excluded?
- What decisions are still unresolved?
- Which assumptions are being carried?
- Why is implementation paused?
- What will the next command do?

## Expected first-run checkpoint

For this example, the expected `hirmos start` checkpoint is:

```text
Checkpoint: Design reached, implementation not started.
Reason: the bounded slice is broad enough to require engineering-risk decomposition and gated user decisions before safe implementation.
Next command: hirmos continue
```

Run `hirmos continue` only after resolving the gated decisions or accepting the conservative defaults HIRMOS proposed.

## What real first runs have taught us

Real first runs with weaker models confirmed the intended HIRMOS behavior: bootstrap completed before work, `hirmos start` paused before implementation, gated decisions were separated from non-gating assumptions, implementation units were planned, corrective `hirmos continue` passes were used for runtime issues, and `hirmos close` archived accepted outcomes.

They also exposed hardening lessons that HIRMOS now treats as framework concerns:

- installed-project validation must check `_hirmos/README.md`, not the application root `README.md`;
- dated session IDs and archive records must use the actual current date, not stale copied dates;
- `SESSION_EXECUTION.md` continuation records are append-only and must not lose earlier pass detail blocks;
- close must reconcile stale checkpoint text before accepted-state/archive claims are surfaced.
