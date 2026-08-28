# First Real Run: MenuGen MVP

This tutorial shows what a realistic HIRMOS run can feel like.

The example uses MenuGen as the project idea. **MenuGen was originally created by Andrej Karpathy**: <https://www.menugen.app/>.

This is not a verbatim transcript. It is a compact tutorial-style reconstruction inspired by HIRMOS dogfood runs. The goal is to show the interaction shape, the decision points, and the artifacts worth inspecting.


The HIRMOS lifecycle shown in this tutorial is:

```text
User Request
↓
Understand System State
→ Design
→ Implementation
→ Update System State
```

## What this example shows

- A broad request can become a Delivery Plan when the work is too large for one honest session.
- HIRMOS separates user decisions from implementation work.
- IU Planning and IU Execution are separate governed steps.
- Runtime issues can be corrected without hiding evidence.
- Close updates system state without claiming production readiness when only a local MVP was proven.

## Starting request

**User**

```text
hirmos start "Build a local MVP of MenuGen: upload a menu image, extract menu items, generate appealing item images with OpenAI, track credits, and show past generated menus."
```

**HIRMOS**

```text
Current-state-first summary:
- Project appears to be a local Next.js app workspace.
- No accepted HIRMOS delivery exists yet.
- Request spans auth, upload, OCR, AI image generation, credits, and history.
- Single-session implementation would be too large for safe evidence-backed close.

Recommended work shape:
- Durable delivery with phases.
- First checkpoint: Delivery Baseline — Review or Change.
```

**Guide**

HIRMOS does not jump into code here. It first decides the smallest honest work shape. A one-line feature can be a single session. A multi-part MVP usually needs a Delivery Baseline.

## Delivery Baseline — Review or Change

**HIRMOS**

```text
Delivery Baseline — Review or Change

Proposed delivery: menugen-local-mvp
Goal: local MVP for upload → menu extraction → generated item images → credits/history.

Proposed phases:
1. Foundation: auth/session, database, upload/job shell.
2. Menu interpretation: extract structured menu items from uploaded menu images.
3. Image generation, credits, gallery, and history.

Gated decisions needing user input:
- Authentication approach: Auth.js/NextAuth, custom auth, or no auth for local MVP?
- Runtime target: local-only MVP or deployment-ready MVP?
- OpenAI model choices for menu interpretation and image generation?
- Credit policy for local MVP?

Non-gating assumptions:
- Local Postgres is acceptable unless user says otherwise.
- Local filesystem storage is acceptable for a local MVP.
- Production billing integration is out of scope.

Next command if accepting baseline:
hirmos continue "Accept delivery baseline and create the next phase/session baseline"
```

**Guide**

This is a decision surface. HIRMOS should show what matters without asking you to answer every possible detail. Gated decisions block affected work; non-gating assumptions let safe work continue while staying visible.

## User decisions

**User**

```text
Use Auth.js/NextAuth. This is local MVP only. Use local Postgres. Use gpt-image-1.5 for image generation. Limit extraction to 3 items per menu. Give each user 10 starting credits.
```

**HIRMOS**

```text
Decision update:
- Auth approach accepted: Auth.js/NextAuth.
- Runtime target accepted: local MVP, not production-ready deployment.
- Credits accepted: 10 starting credits, local accounting.
- Extraction bound accepted: 3 menu items per upload.
- Image model accepted: gpt-image-1.5, subject to runtime API compatibility.

Delivery baseline is ready for phase/session planning.
```

**Guide**

A good HIRMOS run records these decisions as authority. It should not bury them in chat only.

## Phase/session baseline

**HIRMOS**

```text
Session Baseline — Review or Change

Active phase: Phase 01 — Foundation
Scope:
- Configure auth/session baseline.
- Add database schema for users, credits, menus, items, and jobs.
- Add upload/job shell.
- Preserve local-MVP limitation.

Out of scope for this phase:
- Final menu interpretation quality.
- Final generated image UX.
- Production deployment hardening.

Implementation mode:
- Implementation Units required.

Automated-testing posture:
- Reuse the project's existing test framework.
- New or changed isolated auth/job/domain logic requires meaningful automated tests where practical.
- Database/runtime boundaries still require integration/runtime evidence; unit tests do not replace those checks.

Next command if accepting session baseline:
hirmos continue "Accept session baseline and create IU plan"
```

**Guide**

The session baseline is still not implementation authorization when IU mode applies. It authorizes IU planning only.

## IU Planning — Review or Change

**User**

```text
hirmos continue "Accept session baseline and create IU plan"
```

**HIRMOS**

```text
IU Plan — Review or Change

IU planning is complete.
IU execution has not started.
No material project-file edits are authorized until you accept the IU plan.

Created IU files:
- _hirmos/session/implementation-units/IU-01.md — Auth/session foundation
- _hirmos/session/implementation-units/IU-02.md — Database schema and Prisma setup
- _hirmos/session/implementation-units/IU-03.md — Upload and job shell
- _hirmos/session/implementation-units/IU-04.md — Local validation and handoff evidence

Each implementation IU records its automated-testing posture, the behavior that needs isolated tests, relevant existing tests/baselines when practical, and any higher-level evidence still required.

Active generated-artifact validation: PASS

Next command to begin implementation:
hirmos continue "Accept IU plan and begin IU execution"
```

**Guide**

This pause is intentionally strict. It prevents the agent from implementing first and reconstructing IU governance later.

## IU Execution

**User**

```text
hirmos continue "Accept IU plan and begin IU execution"
```

**HIRMOS**

```text
IU execution authorized.
Material implementation may begin under sealed IU files.

Implementation summary:
- Added auth/session configuration.
- Added database schema and generated client.
- Added upload endpoint and job shell.
- Ran validation checks.

Evidence:
- targeted automated tests for changed behavior: PASS where applicable
- npm run build: PASS
- lint/type checks: PASS where available
- material test additions/changes/removals reconciled against the sealed behavioral authority
- IU review rows updated with evidence pointers
```

**Guide**

Implementation evidence belongs in the relevant IU records, `SESSION_LEDGER.md`, and `EVIDENCE.md` when evidence volume justifies a separate evidence surface. The final claim must match the evidence.

## Runtime issue and correction

**HIRMOS**

```text
Runtime correction needed:
- Image generation call failed because one request parameter was incompatible with the selected model/API behavior.
- Scope remains unchanged.
- Correction is authorized under the active IU/session boundary.

Correction result:
- Provider adapter updated.
- Runtime retest completed.
- Evidence recorded.
```

**Guide**

A correction is not a failure by itself. The important behavior is honesty: HIRMOS should identify what failed, keep the scope bounded, fix it under the active authority, and record evidence.

## Close and Update System State

**HIRMOS**

```text
Close readiness:
- Accepted local-MVP outcomes recorded.
- Known limitations preserved.
- No production-readiness claim made.
- Carry-forward items reviewed.
- Current system state updated with pointers to accepted delivery/session artifacts.
- Session archived.

Recommended next command after close:
hirmos start "<next request>"
```

**Guide**

Close is where HIRMOS updates durable state. Current-state files should point to accepted source artifacts and derived indexes; they should not become a duplicate mutable status report.

## What to inspect after a run

Start with these files:

```text
_hirmos/session/SESSION_SCOPE.md
_hirmos/session/SESSION_LEDGER.md
_hirmos/session/unresolved-items.md
_hirmos/session/implementation-units/IU-*.md
_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md
```

When delivery mode applies, also inspect:

```text
_hirmos/system/delivery/DELIVERY_PLAN.md
_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md
_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md
```

## What good behavior looks like

A good HIRMOS run should:

- inspect current state before designing work;
- choose the smallest honest work shape;
- surface gated decisions clearly;
- separate Delivery Baseline, Session Baseline, IU Planning, and IU Execution when they apply;
- avoid material project-file edits before implementation authorization;
- run validation before completion claims;
- preserve limitations instead of overclaiming;
- update durable system state at close.

## What this example does not claim

This tutorial shows a local MVP workflow. It does not claim production readiness. Production work would need additional evidence for deployment, storage, job durability, billing/credit correctness, security, and operational monitoring.
