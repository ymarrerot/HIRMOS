# Spec: Requirements

## Purpose

Govern the HIRMOS **Requirements** step for Orchestrated Spec-Driven Development.

The Requirements step transforms user-provided goals, context, notes, prototypes, user stories, files, attachments, bounded repository context, and constraints into requirements artifacts suitable for System Design.

This spec governs the public default command:

```text
hirmos requirements
```

## Scope

This step owns requirements intake, requirements normalization, requirements baseline generation, and requirements-stage unresolved-item governance.

It produces or refines:

- _hirmos/artifacts/context/requirements-agent/REQUIREMENTS_INPUT_PACK.md (`/_hirmos/artifacts/context/requirements-agent/REQUIREMENTS_INPUT_PACK.md`)
- _hirmos/artifacts/sot/REQUIREMENTS_SOT.md (`/_hirmos/artifacts/sot/REQUIREMENTS_SOT.md`)
- project-level unresolved-item artifacts under _hirmos/artifacts/context/requirements-agent/requirements/ when unresolved assumptions, open questions, or gating decisions exist

This step does **not** own System Design, architecture design, phase design, or implementation planning.

## Required Governing Files

Before running this step, read:

- `/_hirmos/core/authority/core/core-rules.md`
- `/_hirmos/core/command-protocol.md`
- `/_hirmos/core/execution-model.md`
- `/_hirmos/core/authority/core/execution-controls.md`
- `/_hirmos/extensions/requirements-agent/entrypoints/requirements.md`
- `/_hirmos/extensions/requirements-agent/entrypoints/requirements-input-pack.md`
- `/_hirmos/extensions/requirements-agent/entrypoints/requirements-sot.md`
- `/_hirmos/extensions/requirements-agent/specs/requirements-input-pack.spec.md`
- `/_hirmos/extensions/requirements-agent/specs/requirements-sot.spec.md`
- `/_hirmos/extensions/requirements-agent/specs/unresolved-item-contribution-contract.md`
- `/_hirmos/core/authority/extensions/unresolved-item-contribution-contract.md`

If any required governing file is missing or unreadable, stop and surface grounded failure.

## Core Principles

- Keep requirements grounded in readable user inputs, project context, and readable governing files.
- Preserve clear boundaries between confirmed facts, assumptions, research-backed defaults, advisory proposals, and final requirements truth.
- Apply the Beyond Clear Specs pattern: clear entry contract, intermediate templates, surfaced terminal-output shape, required self-validation, and fail-closed behavior.
- Optional installed extensions may contribute bounded, traceable enrichment through declared hook execution, but Requirements remains responsible for governed requirements truth.
- Do not pretend the Requirements step is complete when gating requirements items remain unresolved.
- Do not bypass the shared unresolved-item governance pattern or create extension-local unresolved-decision lanes.

## Required Producer Responsibilities

The Requirements step must perform or reuse these producer responsibilities:

1. Requirements input-pack generation/refinement governed by `specs/requirements-input-pack.spec.md`.
2. Requirements SoT generation/refinement governed by `specs/requirements-sot.spec.md`.
3. Requirements unresolved-item contribution, reconciliation, severity classification, and gating review.
4. Requirements terminal-output validation.

Producer responsibilities must run as a disciplined sequence. Do not skip `REQUIREMENTS_INPUT_PACK.md` when source inputs are diverse, conflicting, research-backed, prototype-derived, presentation-derived, or otherwise not already normalized enough for `REQUIREMENTS_SOT.md`.

## Input Alignment Rules

Primary Requirements inputs include:

- the user prompt and collaborative reasoning from the current session;
- optional command argument tail after `hirmos requirements`;
- online-service attachments visible in the current LLM session, such as screenshots, PDFs, docs, exported notes, or prototype artifacts;
- files under `_hirmos/inputs/requirements-agent/requirements/` when present;
- explicit bounded local file paths or repository-context references surfaced by the user or Orchestrator;
- project context, notes, prototypes, user stories, screenshots, or local file references surfaced by the Orchestrator;
- derived input artifacts produced by declared hook execution;
- prototype-derived SoT artifacts when installed prototype-ingestion hooks produce them;
- presentation-derived artifacts when installed presentation-design hooks produce them and they materially affect requirements.

### Runtime input folder responsibility

The preferred local runtime input folder for reusable Requirements source material is:

```text
_hirmos/inputs/requirements-agent/requirements/
```

Do not ship this folder inside the `requirements-agent` extension package. Runtime input folders are project runtime surfaces governed by `/_hirmos/core/command-protocol.md`. The Core/entrypoint path must create missing runtime folders during init or first run when the active workflow needs them.

If the folder is absent and no local runtime files are needed for the active run, continue using prompt/session inputs, attachments, explicit bounded references, and hook-derived artifacts. If local runtime files are required but the folder cannot be created or read, pause and state the missing or inaccessible path.

### Command argument tail

Core treats any trailing text after `hirmos requirements` as an opaque argument tail and passes it to the active entrypoint. `requirements-agent:requirements` treats that argument tail as direct Requirements prompt input for the active run.

Examples:

```text
hirmos requirements Build a menu management app for a small restaurant.
hirmos requirements Create requirements for a SaaS admin dashboard with role-based access.
```

Use the argument tail for short requirements. For longer or reusable requirements, prefer the session prompt, online attachments, or files under `_hirmos/inputs/requirements-agent/requirements/`.

### Local repository context

Requirements may use local files or repository context only when the scope is bounded. Bounded sources include:

- files placed under `_hirmos/inputs/requirements-agent/requirements/`;
- explicit local file paths provided by the user or Orchestrator;
- explicit bounded directories or file sets provided by the user or Orchestrator;
- derived context artifacts produced by installed extensions through declared hooks.

Do not automatically scan or ingest the full repository by default. If the user asks to use repository context without a bounded scope, pause for scope or create a bounded discovery plan before treating repository content as Requirements input.

### Online-service attachments

When running in an online LLM environment such as ChatGPT or Claude, manually attached files count as session-provided Requirements inputs even if they do not exist under `_hirmos/inputs/requirements-agent/requirements/`. If an attachment is referenced as required but is not visible or readable in the current session, pause and state exactly what is missing.

Raw optional source materials are not automatically Source of Truth. If optional installed extensions derive additional planning artifacts or context through declared hooks, downstream requirements generation should consume the derived artifacts or context, not silently treat raw optional sources as authoritative truth.

If `_hirmos/artifacts/context/requirements-agent/REQUIREMENTS_INPUT_PACK.md` already exists as a generated or refined artifact, treat it as the primary normalized requirements-intake artifact. Raw files under `_hirmos/inputs/requirements-agent/requirements/` remain supporting discovery material and must not implicitly override a curated existing pack.

## Step 0 — Upstream Normalization

Under uncertainty during `requirements-agent:requirements`, apply the bootstrap framework-wide uncertainty rule before proceeding at producer transitions, state transitions, validation points, or surfaced run-state claims.

If the required normalized intake artifact does not yet exist, generate or refine it before requirements SOT generation when the current input state requires normalization.

If a normalized intake artifact already exists, determine whether it is still current for the active working state. If materially stale, either refresh it or pause with a clear explanation of the stale/missing input condition.

## Required Normalized Intake Artifacts

For normal greenfield Requirements, the expected normalized intake artifact is:

```text
/_hirmos/artifacts/context/requirements-agent/REQUIREMENTS_INPUT_PACK.md
```

`REQUIREMENTS_INPUT_PACK.md` must follow the canonical requirements input pack template closely enough to support trustworthy requirements generation.

Downstream narrative sections in `REQUIREMENTS_SOT.md` must not substitute for a required normalized intake artifact when input normalization is needed.

## Hook Participation

The Requirements step exposes and must honor these hook points when declared hook subscribers are installed:

```text
requirements-agent.requirements.before-input-discovery
requirements-agent.requirements.before-requirements-normalization
requirements-agent.requirements.contribute-unresolved-items
requirements-agent.requirements.before-final-gating-review
```

Hook effects must remain bounded, additive, and visible in the Requirements run trace or terminal summary when materially relevant.

Hooks must not silently resolve gating items, overwrite Requirements authority, bypass unresolved-item governance, or create extension-local unresolved-decision lanes.

## Hook Subscriber Matching Validation

When the active working copy contains an installed extension whose manifest declares a hook subscription target that exactly matches a hook point exposed for the current Requirements run, the run must not record `Matched subscribers: none` for that hook point unless the run also records an explicit rejection reason for the installed matching subscriber.

Before pause or completion may be surfaced, fail closed if:

- an installed extension manifest declares an exact matching hook target for a resolved Requirements hook point;
- `HOOK_EXECUTION_CONTROL.md`, `RUN_TRACE.md`, or `VALIDATION_TRACE.md` claims there were no matched subscribers for that hook point;
- and no explicit rejection reason is recorded for the installed matching subscriber.

`HOOK_EXECUTION_CONTROL.md`, `RUN_TRACE.md`, and `VALIDATION_TRACE.md` must agree on subscriber-resolution outcomes for the current run, including explicit rejection reasons.

## Input-Pack Discovery Validation

When the active working copy contains candidate requirement-shaping inputs under known input locations, the Requirements run must not report that no relevant inputs were found unless:

- no candidate inputs were actually present, or
- every discovered candidate was explicitly rejected with a recorded reason.

This validation applies to requirement-relevant direct inputs and to installed enrichment extensions that are expected to produce normalized derived artifacts.

## Step 0B — Determine Whether This Is a Rerun

If the Requirements step has been run before for the current working state, determine whether this execution is a governed rerun.

If so:

- identify the rerun trigger;
- identify changed inputs or changed requirements conditions;
- use that information to guide refinement rather than broad repetition;
- refresh run execution controls for the rerun state.

## Repeatable Producer Unit

Generate or refine one required Requirements producer artifact, then validate it against:

- its governing spec and local artifact wrapper;
- its local quality bar;
- its input alignment rules;
- its unresolved-item contribution obligation.

Repeat until locally acceptable, then continue to the next required producer.

## Immediate Producer Contribution Refresh

When either of the following artifacts is created or materially updated during `requirements-agent:requirements`:

- `_hirmos/artifacts/context/requirements-agent/REQUIREMENTS_INPUT_PACK.md`
- `_hirmos/artifacts/sot/REQUIREMENTS_SOT.md`

then the run must immediately re-scan that producer's canonical unresolved-item sections and refresh that producer's own contribution block in `UNRESOLVED_ITEMS_INVENTORY.md` before moving on to the next producer, final requirements review, or final gating review.

Later cross-file rediscovery is not an acceptable primary collection mechanism. Inline producer contribution refresh is required while the producer context is still active.

## Requirements-Level Review

After required Requirements artifacts have passed local quality checks, run a final requirements-level coherence review.

That review must check:

- internal coherence across `REQUIREMENTS_INPUT_PACK.md` and `REQUIREMENTS_SOT.md`;
- readiness for System Design;
- unresolved contradictions;
- whether assumptions, research-backed defaults, and confirmed requirements remain clearly separated;
- whether prototype-derived or presentation-derived signals were included or explicitly rejected when relevant.

## Unresolved-Item Governance

Requirements unresolved items must use the existing unresolved-item governance pattern.

Do not create any separate artifact such as:

```text
a Requirements-only unresolved-decision bypass artifact
```

When unresolved items exist, use project-level unresolved artifacts under:

```text
_hirmos/artifacts/context/requirements-agent/requirements/
```

with existing artifact names such as:

```text
UNRESOLVED_ITEMS_INVENTORY.md
UNRESOLVED_ITEMS_RECONCILIATION_WORKLIST.md
UNRESOLVED_ITEMS_FEED.md
UNRESOLVED_ITEMS_LEDGER.md
```

## Shared Unresolved-Item Contract

The shared unresolved-item schemas and traceability requirements are governed by:

```text
/_hirmos/core/authority/extensions/unresolved-item-contribution-contract.md
```

The Requirements lifecycle binding is defined by:

```text
/_hirmos/extensions/requirements-agent/specs/unresolved-item-contribution-contract.md
```

## Unresolved-Item Centralization Before Completion

Before completion, `requirements-agent:requirements` must perform the following sequence:

1. identify the required unresolved-item producers for the current Requirements run;
2. inspect each producer's `## Unresolved Items` section;
3. extract both `### Assumptions` and `### Open Questions`;
4. build `UNRESOLVED_ITEMS_INVENTORY.md`;
5. run the validation backstop for materially relevant unresolved items not properly surfaced by producers;
6. build `UNRESOLVED_ITEMS_RECONCILIATION_WORKLIST.md`;
7. build `UNRESOLVED_ITEMS_FEED.md`;
8. append `UNRESOLVED_ITEMS_LEDGER.md`;
9. perform final self-validation before allowing completion.

Producer `Assumptions` and `Open Questions` are canonical Requirements-level unresolved-item inputs.

## Producer-in-Lifecycle Timing Rule

When a Requirements-participating producer is executed during `requirements-agent:requirements`, its canonical unresolved items should be contributed into the project-level canonical inventory structure before the producer exits.

Later Requirements-level centralization must validate and continue from those producer-scoped contribution records rather than depending on a fresh re-read of every producer artifact as the primary reliability mechanism.

If a producer executed during the run surfaced canonical unresolved items locally but did not update its producer-scoped inventory contribution truthfully before exit, the Requirements step must fail closed.

## Unresolved-Item Contribution Sources

The Requirements-level unresolved-item sources are:

- producer `## Unresolved Items`
  - `### Assumptions`
  - `### Open Questions`
- declared hook contributors when applicable
- validation-discovered gaps as a backstop only

Local producer `Assumptions` and `Open Questions` are not just readability aids. They are canonical Requirements-level unresolved-item inputs.

## Pending Confirmation Severity Evaluation

Before finalizing Requirements artifacts, evaluate unresolved Pending Confirmation Items for severity:

- **Safe-to-assume**
- **Proceed-with-caution**
- **Gating / decision-required**

Severity evaluation must consider unresolved items extracted from producer `Unresolved Items` sections, not only items already present in a reconciled feed.

Both `Assumptions` and `Open Questions` are canonical unresolved-item inputs for this evaluation.

## Gating Rules

The Requirements step must pause when unresolved items materially affect one or more of:

- core scope boundaries;
- actor or identity model;
- workflow shape;
- requirements acceptance expectations;
- data requirements;
- security/privacy/compliance posture;
- delivery-target feasibility;
- downstream System Design validity.

If a safe assumption is made, it must be explicitly recorded and preserved for downstream review.

## Gating-Default Categories

The following categories are gating by default when they remain materially unresolved during Requirements:

- core scope boundaries
- actor or identity model
- core workflow shape
- acceptance expectations
- data requirements
- privacy, security, or compliance posture
- delivery-target feasibility
- downstream System Design validity

These categories may be classified below `Gating / decision-required` only when the run records a strong explicit downgrade justification that explains why Requirements completion is still honest.

## Severity Downgrade Justification Rule

If an unresolved item materially affects a gating-default category but is classified as `Safe-to-assume` or `Proceed-with-caution`, the run must record an explicit downgrade justification.

That justification must explain:

- why the item is not gating for this run;
- why Requirements completion is still honest;
- what concrete scope-bounding or constrained handling prevents false completion.

Silent downgrade is invalid.

## Bounded-Requirements Downgrade Rule

It is not enough to say that System Design can still proceed in a bounded way.

If bounded requirements are used to justify non-gating treatment, the run must explicitly state:

- what is bounded;
- what is deferred;
- what is intentionally excluded from current requirements truth claims;
- why the remaining uncertainty does not invalidate completed-state Requirements honesty.

Feature-variation uncertainty should not automatically be treated as minor. If unresolved feature-shape variation would materially change user workflows, validation expectations, data assumptions, reporting/export needs, privacy/compliance posture, or downstream design validity, escalate it to **Gating / decision-required**.

Allowed handling outcomes for gating items are:

- **Use assumption**
- **Ask customer**
- **Defer and constrain**

For non-gating unresolved items, the run must still record a documented handling answer. Safe-to-assume and Proceed-with-caution describe risk, not the final answer.

The Requirements step may complete only after either no gating items remain unresolved or an Orchestrator decision has been recorded for each gating item.

## Decision Absorption Recording

When the Orchestrator/user provides decisions for Requirements-stage unresolved items, record how each decision was absorbed into:

- `REQUIREMENTS_INPUT_PACK.md`, when relevant;
- `REQUIREMENTS_SOT.md`;
- unresolved-item ledger outcomes;
- terminal output summary.

If a decision affects downstream System Design risk, preserve a downstream note rather than silently dropping the decision context.

## Required Runtime Trust Artifacts

The Requirements run must preserve runtime trust artifacts sufficient to support Evidence-backed Review and downstream handoff.

At minimum, when applicable, the run must keep these surfaces consistent:

- `RUN_EXECUTION_CONTROLS.md`
- `HOOK_EXECUTION_CONTROL.md`
- `RUN_TRACE.md`
- `VALIDATION_TRACE.md`
- project-level unresolved-item artifacts
- terminal output

Do not surface completed if any required control remains pending or contradictory.

## Cross-Artifact Producer-Attribution Consistency Rule

Coverage summaries in unresolved-item artifacts must be derived from the actual inventory items.

Later unresolved-item artifacts must not invent, summarize, or suppress producer extraction counts independently of the inventory body.

Each unresolved item must preserve producer artifact and source subsection attribution so later coverage, rejection, or merge decisions remain reconstructable.

## Core-Owned Surfaced-Output Boundary

Surfaced chat-facing output is governed through Core run execution controls, including identity display execution control and active Core-owned controls such as hook execution control when applicable.

This entrypoint owns only its governed response body structure, local truthfulness, and extension-owned validation concerns.

## Terminal-State Composition

### completed

Allowed only when:

- `REQUIREMENTS_INPUT_PACK.md` is generated/refined when needed;
- `REQUIREMENTS_SOT.md` is generated/refined;
- mandatory local validation passes for each Requirements producer;
- Requirements-level coherence review passes;
- hook subscriber matching validation passes when applicable;
- unresolved items are recorded through the unresolved-item governance path;
- no gating requirements decisions remain unresolved;
- required runtime controls are executed and not pending;
- final surfaced output self-validation passes.

### paused

Required when:

- required inputs are missing;
- gating requirements decisions remain unresolved;
- hook obligations are incomplete or contradictory;
- validation finds an issue that can be remediated with bounded user/Orchestrator input;
- a required normalized input artifact is stale or missing and cannot be safely regenerated without input.

### failed

Required when:

- the Requirements step cannot safely complete;
- no bounded pause/remediation path exists;
- required artifacts cannot be produced or validated;
- hook execution or runtime controls contradict the surfaced result and cannot be repaired.

## Local Quality Bar

Requirements completion is invalid unless:

- requirements are specific enough to support System Design;
- requirements separate confirmed facts from assumptions and research-backed defaults;
- actors, workflows, capabilities, constraints, and acceptance expectations are visible;
- unresolved items are captured, classified, and handled;
- downstream System Design can consume `REQUIREMENTS_SOT.md` without guessing at core scope.

## Final Surfaced Output Self-Validation

Before surfacing final output, validate that the response:

- states the terminal state honestly;
- lists artifacts produced or updated;
- summarizes unresolved-item status;
- identifies any decisions still required;
- summarizes validation evidence;
- points to `hirmos system-design` only when completion is honest;
- does not claim System Design or implementation readiness beyond what the Requirements artifacts support.

## Next Step

When completed, the next workflow step is:

```text
hirmos system-design
```
