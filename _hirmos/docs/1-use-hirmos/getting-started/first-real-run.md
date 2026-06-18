# First Real Run

This page shows a realistic first HIRMOS run using MenuGen, a mobile-friendly web app that turns a restaurant menu photo into a visual menu with representative generated dish images.

The point of this example is not to show a finished implementation. The point is to show what a serious `hirmos start` run should produce before implementation begins.

## Example request

```text
hirmos start "Build an MVP for MenuGen, a mobile-friendly web app that helps diners understand restaurant menus visually. Users should be able to upload or capture a restaurant menu photo, extract menu items, generate representative dish images, view a mobile visual menu, sign in, use a credit-like allowance, persist jobs/results, recover from failures, and use provider boundaries for external AI/image services. Real payment checkout is not required in the first implementation."
```

The request is intentionally broad. A strong HIRMOS run should not jump directly into code. It should first understand the current project state, identify design decisions that materially affect architecture or acceptance criteria, define a bounded session, and pause before implementation.

## 1. User Request

HIRMOS treats the request and any uploaded notes, requirements, screenshots, prototypes, tickets, code samples, or existing docs as source inputs.

Source inputs guide attention, but they are not final authority. HIRMOS must reconcile them through governed session artifacts before implementation.

For this MenuGen run, the source input says the MVP should include:

- a landing page that explains MenuGen and labels generated images as representative;
- mobile photo upload or capture;
- AI/OCR-style menu interpretation;
- representative image generation for recognized items;
- a mobile visual results gallery;
- sign-up/sign-in;
- credit-like usage tracking;
- persistent jobs, results, and recent history;
- visible failure states and recovery where reasonable;
- a real database;
- environment variables for provider secrets;
- isolated provider-specific logic;
- no real payment checkout in the first implementation.

A good run should preserve the important product truth that generated images are representative, not exact restaurant photos.

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

For a greenfield MenuGen project, this may mean recording that no meaningful app exists yet and that the uploaded requirements define the initial design problem.

For a brownfield MenuGen project, this means inspecting the current app, routes, auth model, database schema, provider integrations, job-processing code, and UI surfaces before designing changes.

For a mixed project, this means preserving what exists while designing the new MenuGen workflow around it.

A strong run should not assume the project is greenfield merely because the request describes a new product. It should decide project type from the working copy.

## 3. Design

Design owns governed requirements, system/application design, session scope, unresolved-item disposition, technical review information, and implementation readiness.

For MenuGen, the Design stage should recognize that the request is too large for careless one-shot implementation. It crosses product UX, auth, persistence, job processing, provider boundaries, credits, error handling, and mobile UI.

A good Design result should decide whether the work can fit into one bounded session. For MenuGen, a strong result would usually decompose delivery like this:

```text
Delivery decomposition: REQUIRED
Reason: The MVP spans multiple risk areas: auth, durable job state, usage accounting, provider isolation, image generation, and mobile results UX.

Recommended delivery shape:
- Current session: define a bounded provider-ready MVP slice and implementation units.
- Later sessions: real payment checkout, production provider configuration, stronger moderation/retention controls, deeper admin/support tooling.
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

For MenuGen, a reasonable Design routing decision would include:

```text
requirements-design: REQUIRED
Reason: source input contains product requirements that must become governed requirements authority.

system-design: REQUIRED
Reason: auth, jobs, credits, persistence, and provider boundaries require architecture decisions.

delivery-design: REQUIRED
Reason: the request is larger than a safe one-shot implementation.

session-contract: REQUIRED
Reason: implementation must be bounded before `hirmos continue`.

implementation-readiness: BLOCKED
Reason: gated user-owned decisions remain unresolved.
```

### Example `unresolved-items.md` outcome

HIRMOS should not flood the register with every preference. It should record only items that materially affect architecture, scope, implementation order, acceptance criteria, or future production readiness.

A strong MenuGen run should separate gated decisions from non-gating assumptions.

#### Gated decisions

These block full implementation authorization, or block specific implementation slices, until answered.

```text
GATED-1 — Upload requires sign-in or allows anonymous preview
Question: Should users be required to sign in before uploading a menu, or should the MVP allow a limited anonymous preview/trial before sign-in?
Why it matters: affects routing, job ownership, credit checks, history, and first-use UX.
Default if resolved conservatively: require sign-in before upload for the first MVP.

GATED-2 — Real providers or provider-ready fallback first
Question: Should the first implementation call real OCR/image-generation providers, or implement provider interfaces with deterministic/local fallback behavior until credentials are configured?
Why it matters: affects environment setup, acceptance claims, failure modes, validation, and cost controls.
Default if resolved conservatively: implement provider boundaries and safe fallback behavior; do not claim real AI output unless credentials are configured and validated.

GATED-3 — Background queue depth
Question: Does the MVP require real background/queue-backed processing now, or is durable job-state with bounded server execution acceptable for the first implementation?
Why it matters: affects hosting assumptions, data model, retry behavior, and refresh survival.
Default if resolved conservatively: persist job state and status; leave real queue as a later production-hardening slice.

GATED-4 — Database/runtime target
Question: What database/runtime environment should this implementation target, and is a local database available for validation?
Why it matters: the MVP requires users, jobs, credits, and results to be persisted and validated.
Default if resolved conservatively: use a real relational database with documented local setup and migrations.

GATED-5 — Menu item processing limit
Question: What maximum number of menu items should be processed per job in the MVP?
Why it matters: affects cost, runtime duration, result UX, and acceptance criteria.
Default if resolved conservatively: process up to 8 items per job, show a clear limit message, and preserve the unprocessed count.

GATED-6 — Minimum retention/privacy posture
Question: What minimum upload retention, generated-image retention, deletion, and abuse/moderation controls are required for the MVP?
Why it matters: the app accepts arbitrary images and may store generated outputs.
Default if resolved conservatively: retain only what is needed for job/result history, avoid public sharing, and document production privacy controls as not complete.
```

#### Non-gating assumptions

These are safe to carry for a first bounded slice as long as they remain visible and are revalidated later.

```text
ASSUMPTION-1 — Responsive web app, not native mobile
MenuGen is a mobile-first responsive Next.js web app, not a native iOS/Android app.

ASSUMPTION-2 — Representative image labeling
Generated dish images must be labeled as representative and not exact restaurant photos.

ASSUMPTION-3 — No real checkout in first implementation
Credit accounting is in scope, but real payment checkout is explicitly out of scope for the first implementation.

ASSUMPTION-4 — Credits consumed per generated item/image
Usage is consumed per generated menu item/image, with job-level accounting recorded for support.

ASSUMPTION-5 — Recent history only
MVP history means signed-in users can view recent menu jobs/results, not a full archive/search/export system.

ASSUMPTION-6 — Basic support visibility
Operator/support visibility means job id, status, timestamps, provider error category, retry state, and usage events. It is not a full observability platform.

ASSUMPTION-7 — Bounded parsing is acceptable
The MVP preserves extracted item names and useful descriptions where available, but does not require perfect OCR correction or manual item editing in the first slice.

ASSUMPTION-8 — Provider details remain configurable
Provider credentials, model names, callback URLs, rate limits, and production launch settings remain behind environment variables and provider adapters.
```

### Example bounded `SESSION_CONTRACT.md` outcome

A strong run should define a bounded contract rather than treating the whole product description as one implementation task.

```text
Session Contract Status: BLOCKED_FOR_GATED_DECISIONS

Authorized after gated decisions are resolved:
- Mobile-first landing page and upload/capture entry point.
- Signed-in user flow, if sign-in-before-upload is accepted.
- Real database schema for users, jobs, results, usage ledger, and credits/allowance.
- Durable job status that survives refresh.
- Provider adapter interfaces for menu interpretation and image generation.
- Safe fallback behavior when provider credentials are unavailable.
- Visual results gallery with representative-image labeling.
- Basic recent history for signed-in users.
- Visible failure and retry/recovery states where reasonable.

Out of scope for the first implementation:
- Real payment checkout.
- Full admin/support console.
- Native mobile apps.
- Production-grade moderation and retention policy beyond MVP safeguards.
- Perfect OCR correction or complete manual menu editing.
- Unlimited menu-item processing.
```

### Example implementation units

Even before implementation begins, HIRMOS should propose coherent implementation units.

```text
IU-01 — App foundation, auth, and database schema
Goal: establish signed-in user ownership, jobs, results, credits/allowance, and usage ledger.

IU-02 — Upload/capture and durable job creation
Goal: accept a menu image, create a persisted job, show loading/status, and survive refresh.

IU-03 — Menu interpretation provider boundary
Goal: isolate AI/OCR interpretation behind an adapter, store structured menu items, and expose useful failure states.

IU-04 — Image generation provider boundary and cost guardrails
Goal: generate or safely fallback representative images for a bounded item subset and consume usage correctly.

IU-05 — Mobile results, recent history, and retry UX
Goal: show the visualized menu, recent jobs, status/error detail, and reasonable retry/recovery behavior.

IU-06 — Validation and evidence review
Goal: validate auth ownership, job persistence, usage accounting, failure handling, mobile rendering, and secrets/provider boundaries.
```

## 4. Implementation

Implementation activates only when accepted Design authorizes governed realization.

For this MenuGen example, `hirmos start` should pause before implementation. It should not modify app files yet unless the command explicitly allows a non-implementation preparatory artifact update.

A correct checkpoint would say something like:

```text
Implementation Status: NOT_STARTED
Reason: `hirmos start` completed Understand System State and Design planning, but implementation is not authorized until gated decisions are resolved and the Session Contract is accepted.
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

For the initial MenuGen `hirmos start` example, Update System State is not reached yet because implementation has not begun.

## What to inspect after `hirmos start`

A strong first run should leave inspectable artifacts such as:

- `support/request-intake.md`
- `support/source-materials.md`
- `support/system-state.md`
- `REQUIREMENTS_BASELINE.md`
- `DESIGN.md`
- `SESSION_CONTRACT.md`
- `SESSION_EXECUTION.md`
- `unresolved-items.md`
- `session-contract-review.md`
- proposed `implementation-units/IU-xx.md` files or equivalent unit planning

For larger work, also inspect:

- `DELIVERY_PLAN.md`
- `phases/PHASE-xx.md`

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

For MenuGen, the expected `hirmos start` checkpoint is:

```text
Checkpoint: Design reached, implementation not started.
Reason: the MVP is broad enough to require delivery decomposition and gated user decisions before safe implementation.
Next command: hirmos continue
```

Run `hirmos continue` only after resolving the gated decisions or accepting the conservative defaults HIRMOS proposed.


## What the real MenuGen run taught us

A real MenuGen run with a weaker model confirmed the intended HIRMOS behavior: bootstrap completed before work, `hirmos start` paused before implementation, gated decisions were separated from non-gating assumptions, implementation units were planned, corrective `hirmos continue` passes were used for runtime issues, and `hirmos close` archived accepted outcomes.

The run also exposed hardening lessons that HIRMOS now treats as framework concerns:

- installed-project validation must check `_hirmos/README.md`, not the application root `README.md`;
- dated session IDs and archive records must use the actual current date, not stale copied dates;
- `SESSION_EXECUTION.md` continuation records are append-only and must not lose earlier pass detail blocks;
- close must reconcile stale checkpoint text before accepted-state/archive claims are surfaced.
