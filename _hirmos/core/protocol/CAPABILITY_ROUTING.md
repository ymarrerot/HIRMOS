# Capability Routing Protocol

Status: core protocol.
Purpose: define how HIRMOS routes lifecycle-stage responsibilities to installed extension capabilities without turning capabilities into independent workflow authorities.

Extension capabilities execute inside lifecycle-stage responsibilities. They do not replace the lifecycle and do not own lifecycle authority.

## Core rule

Lifecycle stages define the responsibility boundary. Extension capabilities are activated only when the active lifecycle stage needs specialized work to satisfy that boundary.

Capability routing must answer four questions in order:

1. Which lifecycle stage is active?
2. Which installed extensions support that lifecycle stage?
3. Which capabilities inside those extensions are needed by the active command, evidence, unresolved items, artifacts, and controls?
4. Which capability entrypoints must be read and executed before the lifecycle boundary can safely continue?

The runner must not choose a capability first and justify it afterward.

## When routing is required

Capability routing is required when an advancing command must decide whether an installed extension capability is `REQUIRED`, `OPTIONAL`, `SKIPPED`, `NOT_APPLICABLE`, or `BLOCKED` before the active lifecycle boundary can safely continue.

At minimum, routing is required when:

- moving from Understand System State into Design;
- deciding whether Design can reach implementation-readiness;
- deciding whether Implementation may begin, continue, retry, or complete;
- deciding whether Update System State may accept outcomes, archive, or close;
- selecting requirements, system-design, delivery-baseline, phase-baseline, session-scope, technical-review, implementation-readiness, implementation, validation, evidence, or update-state capabilities;
- a required artifact or execution control names a capability, extension, or entrypoint;
- unresolved items, project type, stack evidence, delivery governance, runtime services, or current-state evidence affects which specialized work must run;
- a capability may produce or update artifacts required for a readiness claim, completion claim, blocker, route-back, or user-facing checkpoint.

If none of these conditions apply, the runner may record capability routing as `NOT_APPLICABLE` for the boundary. The rationale must be artifact-backed when the boundary is user-facing.

## Routing order

HIRMOS routes capabilities from evidence, not from preferred capability names. The routing order is represented by the routing inputs below and applied through the linear routing workflow.

## Routing inputs


Routing must consider:

1. User Request signals.
2. Source input inventory, including uploads, prototypes, references, and POC inputs.
3. General and focused system-state evidence.
4. Active lifecycle boundary.
5. Active command boundary.
6. Unresolved-item state.
7. Project type and stack evidence.
8. Delivery governance and phase state, when active.
9. Runtime integration posture, when material.
10. Existing execution controls in `_hirmos/session/SESSION_EXECUTION.md`.
11. Installed extension manifests.
12. Installed capability manifests.

Project type and stack decisions recorded in `DESIGN.md`, `SESSION_SCOPE.md`, `stack-resolution.json`, and `SESSION_EXECUTION.md` may require, skip, or shape capabilities. They do not replace lifecycle authority.

Rules:

- stack package guidance may affect Implementation and evidence capabilities, but repository evidence governs actual commands;
- stack contexts, when active, must be carried into Design, Implementation Unit artifacts, and Evidence Review;
- large or multi-session routing must use Delivery Units or Phases when the work cannot be safely governed as one bounded session.

## Linear routing workflow

When an advancing command reaches a lifecycle boundary that requires capability routing, follow this workflow:

1. Confirm the active lifecycle stage from `_hirmos/session/SESSION_STATE.json` and `_hirmos/session/SESSION_EXECUTION.md`.
2. Read this protocol before selecting extension or capability entrypoints.
3. Inspect installed extension manifests at `_hirmos/extensions/*/extension.json`.
4. Select candidate extensions whose `lifecycle_stages` includes the active lifecycle stage.
5. Resolve each selected extension's default entrypoint from `extension.json.entrypoints.default`.
6. Read the selected extension entrypoint before running extension-owned routing work.
7. Apply the shared extension method contained in the selected extension default entrypoint.
8. Inspect the selected extension's listed capabilities from `extension.json.capabilities`.
9. For each listed capability, read `_hirmos/extensions/<extension-id>/capabilities/<capability-id>/capability.json`.
10. Compare the capability manifest against the active lifecycle stage, command boundary, activation triggers, required artifacts, active controls, unresolved-item state, project type, stack evidence, delivery state, and runtime posture.
11. Assign one capability decision: `REQUIRED`, `OPTIONAL`, `SKIPPED`, `NOT_APPLICABLE`, or `BLOCKED`.
12. For every `REQUIRED` capability and every selected `OPTIONAL` capability, resolve the runnable entrypoint from `capability.json.entrypoints.default`.
13. Read the capability entrypoint before executing capability-specific work.
14. Run only the capability-specific work needed by the active lifecycle boundary.
15. Record decisions, entrypoint paths, reasons, controls, terminal states, and unresolved-item producer outcomes in `_hirmos/session/SESSION_EXECUTION.md`.
16. Do not claim lifecycle-boundary completion until required capability controls are `SATISFIED`, `BLOCKED`, or `NOT_APPLICABLE` with rationale.

This workflow is the canonical routing path. Command files may point to it, but they must not redefine it.

## Extension discovery

Installed extensions are discovered from:

```text
_hirmos/extensions/*/extension.json
```

An extension is a candidate for the active lifecycle stage when:

- its `lifecycle_stages` includes the active lifecycle stage; and
- the active command boundary may require specialized work owned by that extension.

The extension manifest must declare:

- extension `id`;
- supported `lifecycle_stages`;
- listed `capabilities`;
- default extension entrypoint path under `entrypoints.default`.

Runners must resolve the extension entrypoint from the manifest. They must not infer extension entrypoint paths from memory when the manifest is present.

Example:

```text
Active lifecycle stage: design
Candidate extension: extension manifest whose lifecycle_stages includes design
Reason: manifest lifecycle_stages includes the active stage
Extension entrypoint: manifest entrypoints.default
```

## Capability manifest inspection

After selecting an extension, inspect the capability manifests listed by that extension.

Canonical capability manifests live at:

```text
_hirmos/extensions/<extension-id>/capabilities/<capability-id>/capability.json
```

A capability manifest must define or reference:

- capability `id`;
- owning extension;
- lifecycle stage;
- activation mode and triggers;
- required artifacts, when any;
- produced artifacts, when any;
- execution controls, when any;
- default runnable entrypoint path.

The runner must compare the capability manifest to the active lifecycle boundary and routing inputs before choosing the capability decision.

Capability-specific triggers belong in `capability.json`. The global algorithm for how to inspect and apply those triggers belongs in this protocol.



## PROD-L8.18 Capability Taxonomy

Capability names are runtime dispatch identifiers, not product taxonomy, workflow phases, or user-facing process names. HIRMOS keeps capability names stable unless a rename is required for authority safety. Capability consolidation should happen through documented families and aliases before directory renames.

Canonical capability families:

| Family | Purpose | Baseline capabilities | Notes |
|---|---|---|---|
| Current-state understanding | Establish current state and input context before design or implementation. | `request-intake`, `source-material-ingestion`, `prototype-ingestion`, `understand-system-state` | These capabilities feed Understand System State. They do not produce final scope authority by themselves. |
| Delivery and phase shaping | Decide whether work needs delivery/phase/session governance and create the relevant baseline authority. | `delivery-baseline`, `delivery-design`, `phase-baseline`, `phase-contracting` | Prefer capability-family language in docs. Keep existing IDs as stable dispatch IDs. |
| Session scope and design | Produce bounded session authority and optional requirements/design sub-authority when justified. | `requirements-design`, `system-design`, `technical-review`, `session-scope`, `implementation-readiness` | These capabilities support Design; they do not bypass `SESSION_SCOPE.md` / delivery authority. |
| Implementation execution and review | Plan, execute, validate, review, and retry implementation work under accepted authority. | `implementation-unit-planning`, `implementation-execution`, `implementation-unit-review`, `session-implementation-review`, `validation-review`, `retry-escalation` | IU artifacts must exist before material implementation when IU mode is active. |
| Accepted-state update | Close/archive/update accepted-state navigation and carry-forward after governed work. | `update-system-state` | This family updates navigation/source indexes; it does not create root accepted-state requirements/design authority by default. |

Alias/minimality rules:

- Do not add a new capability ID when an existing capability family and entrypoint can safely own the responsibility.
- Do not rename existing capability directories only to improve wording. Use taxonomy labels and docs aliases first.
- Add a new capability only when the existing family cannot safely own required inputs, produced artifacts, terminal states, or validation controls.
- Capability manifests remain the dispatch source of truth; taxonomy tables are interpretive guidance, not a second manifest.


## Capability decisions

Allowed capability decisions:

```text
REQUIRED
OPTIONAL
SKIPPED
NOT_APPLICABLE
BLOCKED
```

Use these tests:

- `REQUIRED` — the capability must run or be satisfied before the active lifecycle boundary can safely complete. Use this when its output, control, artifact, evidence, or decision is necessary for readiness, completion, route-back, or continuation.
- `OPTIONAL` — the capability could improve the result, but the active lifecycle boundary can safely continue without it. Optional capabilities may run only when doing so does not hide a required decision or over-expand scope.
- `SKIPPED` — the capability is relevant but intentionally not run for an evidence-backed reason. The reason must be recorded.
- `NOT_APPLICABLE` — the capability's lifecycle stage, activation triggers, required artifacts, and controls do not match the active request path or lifecycle boundary.
- `BLOCKED` — the capability should run but cannot safely run because required evidence, artifacts, dependencies, provider configuration, working-copy state, or user decisions are missing.

If a capability is needed to produce or validate an artifact required by the active lifecycle boundary, it is not optional.

If a capability trigger matches but required inputs are missing, the decision is usually `BLOCKED`, not `SKIPPED`.

If no capability trigger matches, the decision is usually `NOT_APPLICABLE`, not `SKIPPED`.

## Capability activity record

Capability decisions are recorded in `_hirmos/session/SESSION_EXECUTION.md`.

Use this shape inside the execution spine:

| Capability | Extension | Stage | Decision | Entrypoint | Reason | Required controls | Status |
|---|---|---|---|---|---|---|---|

Do not create a separate capability plan unless a future governed artifact explicitly defines that artifact, its template, validation rules, and lifecycle conditions.

## Canonical capability entrypoint surface

Runnable capability entrypoints are canonical only at:

```text
extensions/<agent>/capabilities/<capability>/entrypoints/default.md
```

Capability manifests must point directly to `entrypoints/default.md`, and runners must resolve that canonical path. Legacy redirect wrappers at `extensions/<agent>/capabilities/<capability>/entrypoint.md` are not allowed because they create a second discoverable surface without the complete execution surface.

## Entrypoint execution contract

Every runnable capability entrypoint must include:

```text
Purpose
Produces
Terminal States
```

The entrypoint execution surface is not a full lifecycle authority. It tells the runner what the capability does, what artifacts/evidence it may produce, and how it may terminate inside the active lifecycle-stage responsibility.

## Capability completion rule

A capability is not complete just because its entrypoint was read.

A capability is complete only when:

1. required input artifacts were inspected or explicitly determined not applicable;
2. expected artifacts/evidence were produced or explicitly marked not applicable;
3. unresolved-item producer obligations were handled;
4. required execution controls are `SATISFIED` or `NOT_APPLICABLE` with rationale;
5. `_hirmos/session/SESSION_EXECUTION.md` records the capability status.

## Missing or conflicting provider rule

HIRMOS must fail closed when:

- a required lifecycle-stage capability has no installed extension provider;
- multiple installed providers claim the same required capability and no selection rule exists;
- an extension manifest is malformed;
- a capability manifest is malformed;
- a declared extension entrypoint path does not exist;
- a declared capability entrypoint path does not exist;
- required artifacts are missing and cannot be safely instantiated;
- a capability decision contradicts lifecycle, unresolved-item, command-state, or execution-control state.

## Unresolved-item producer rule

Every capability that can discover uncertainty must either:

1. contribute unresolved items to the unresolved register selected by `SESSION_STATE.json.session_focus`; or
2. explicitly record that no material unresolved items were discovered.

When `session_focus = delivery_baseline`, the target is `_hirmos/system/delivery/<delivery-id>/unresolved-items.md`. When the focus is `session_baseline`, `phase_session_baseline`, `implementation`, or single-session work with material uncertainty, the target is `_hirmos/session/unresolved-items.md`.

Capabilities must not hide unresolved items inside local prose.

## Interaction-mode visibility

Interaction modes change how capability routing is surfaced, not whether routing happens.

- `domain_expert` normally hides capability-routing details unless a decision or blocker requires them.
- `technical_supervisor` may summarize active capabilities, artifacts, assumptions, and evidence.
- `framework_diagnostics` should expose capability decisions, entrypoints, skipped/not-applicable reasons, controls, and route-back triggers.

## Governed checkpoint contribution rule

When a capability result creates a user-facing decision, readiness claim, completion claim, blocker, or route-back, the capability must provide enough information for the active Current Continuation Snapshot.

At minimum, the capability must identify:

- produced artifacts;
- unresolved-item contribution or explicit none/not applicable;
- controls affected;
- terminal state reached;
- whether user-facing output is required.

Capability completion cannot be claimed if its unresolved-item producer obligation is missing or contradictory.

## PROD-L8.9 focus-aware routing matrix

Compatibility note: PROD-L8.9 supersedes the original PROD-L4 route shape with focus-aware routing. Historical reports may mention older route labels; runtime routing uses the table below.

## PROD-L8.9 focus-aware routing matrix

Runtime commands must route capabilities from the active `session_focus`, the Delivery Shape Decision, and the active authority before they instantiate artifacts or claim readiness.

| Route / focus | Required capability route | Required authority before next boundary |
|---|---|---|
| `SINGLE_SESSION_MINIMAL` / `minimal_session` | `session-scope` only when a bounded output authority is needed | Minimal `SESSION_SCOPE.md`; no unresolved, requirements, design, delivery, implementation-unit, or evidence artifacts unless strictly necessary |
| `SINGLE_SESSION_VERTICAL_SLICE` / `session_baseline` | `session-scope → implementation-readiness` | `_hirmos/session/SESSION_SCOPE.md` with affirmative single-session safety evidence |
| `SINGLE_SESSION_WITH_IMPLEMENTATION_UNITS` / `session_baseline` | `session-scope → implementation-readiness` | `_hirmos/session/SESSION_SCOPE.md`; full implementation-unit artifacts only after baseline acceptance/amendment |
| `DELIVERY_BASELINE` / `delivery_baseline` | `delivery-baseline` with delivery requirements/design/unresolved/phase-coverage responsibilities as needed | `_hirmos/system/delivery/DELIVERY_PLAN.md`, `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md`, and `_hirmos/system/delivery/<delivery-id>/unresolved-items.md`; optional delivery `REQUIREMENTS.md` / `DESIGN.md` only when justified |
| `DELIVERY_PHASE_SESSION` / `phase_session_baseline` | `phase-baseline → session-scope → implementation-readiness` | accepted delivery baseline, next instantiated `PHASE-xx.md` when phase files are used, and `_hirmos/session/SESSION_SCOPE.md` for the bounded phase/session |

Routing guardrails:

- HIRMOS always has a runtime session envelope, but `SESSION_SCOPE.md` is not required during `delivery_baseline` focus.
- `delivery-baseline` owns creation/update of the delivery roadmap/register, delivery scope, delivery-level unresolved register, and optional delivery-level requirements/design.
- `delivery-baseline` must include a complete phase coverage plan in `DELIVERY_SCOPE.md` before baseline acceptance.
- `phase-baseline` instantiates the next `PHASE-xx.md` just in time after delivery-baseline acceptance; it must not create future phase files by default.
- `session-scope` adopts and narrows accepted delivery/phase authority into the active phase/session; it must not recreate the full delivery authority.
- `implementation-readiness` verifies the focus-specific authority chain and blocks implementation when required artifacts are missing, stale, contradictory, placeholder-only, or unaccepted.
- Single-session routes must not instantiate durable delivery artifacts just to satisfy governance.
- Durable delivery routes must not be downgraded to single-session routing merely because the current user message is short.

Fail-closed rule: if the focus, route, active authority, or Delivery Shape Decision is `UNCERTAIN`, or if the selected route cannot satisfy its authority artifacts, the command must set the relevant capability decision to `BLOCKED` or `ROUTE_BACK_REQUIRED`, record the reason in `SESSION_EXECUTION.md`, and stop before implementation.

Legacy route labels are history only. Runtime routing uses `DELIVERY_BASELINE / delivery_baseline → delivery-baseline` before session scope when durable delivery baseline is not yet accepted, and `DELIVERY_PHASE_SESSION / phase_session_baseline → phase-baseline → session-scope → implementation-readiness` after acceptance. Fail-closed rule: if the Delivery Shape Decision is `UNCERTAIN`, the route must block before implementation.

## PROD-L8.9E/F Checkpoint and Validation Routing

Checkpoint template selection is focus-aware. `delivery_baseline` must use `DELIVERY_BASELINE_CHECKPOINT_OUTPUT.md` and delivery-level unresolved items. `session_baseline` and `phase_session_baseline` must use `SESSION_BASELINE_CHECKPOINT_OUTPUT.md` and session-level unresolved items when created. Validators must fail closed when a delivery baseline creates `SESSION_SCOPE.md`, instantiates `PHASE-xx.md` before baseline acceptance, or stores delivery-level unresolved items in `_hirmos/session/unresolved-items.md`.


## PROD-L8.10 Delivery-Baseline Surface Minimality Routing

When the selected route is `DELIVERY_BASELINE / delivery_baseline`, capability producers must write delivery-level uncertainty to `_hirmos/system/delivery/<delivery-id>/unresolved-items.md`. They must not create `_hirmos/session/unresolved-items.md` or `_hirmos/session/SESSION_SCOPE.md` until the route advances to `DELIVERY_PHASE_SESSION / phase_session_baseline` or another bounded session-scope focus. Status and checkpoints must report session unresolved as `NOT_APPLICABLE` during delivery-baseline focus.

## PROD-L8.11 Delivery-Baseline Optional Authority Location

When `SESSION_STATE.json.session_focus = delivery_baseline`, the active authority is delivery-level. Optional requirements/design authority must be located under `_hirmos/system/delivery/<delivery-id>/` only:

- `_hirmos/system/delivery/<delivery-id>/REQUIREMENTS.md` when separate delivery-level requirements authority is justified.
- `_hirmos/system/delivery/<delivery-id>/DESIGN.md` when separate delivery-level design authority is justified.

During `delivery_baseline`, HIRMOS must not create, update, list, or depend on `_hirmos/session/REQUIREMENTS.md` or `_hirmos/session/DESIGN.md`. If separate optional authority is not justified, requirements and design decisions remain inside `DELIVERY_SCOPE.md` only. Session-level optional authority artifacts become applicable only after the flow advances to a bounded `phase_session_baseline` or `session_baseline` focus.


## PROD-L8.13 Delivery Review Wording

Capability routing outputs must use current-state-first explanations. The model may record project-type classification as supporting evidence, but it must route from the active `session_focus`, inspected current state, scope and validation risk, and artifact-authority need. During `delivery_baseline`, user-facing labels must say Candidate Delivery, Proposed Delivery, or Delivery Under Baseline Review until the baseline is accepted/amended.
