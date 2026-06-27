# HIRMOS Bootstrap

Status: mandatory bootstrap authority.
Purpose: give the current agent a linear, quiz-gated path before it performs HIRMOS-governed work.

Read this file in order.

Bootstrap is not complete until the required reads, quiz, and bootstrap report are complete.

## Operating rules

- Do not skip ahead.
- Do not treat partial reading as bootstrap completion.
- Do not begin runtime command execution until bootstrap passes.
- Do not claim command readiness until the bootstrap report says bootstrap passed.
- Do not answer quiz questions from memory when the question names an authority or protocol file.
- Do not treat chat memory, compressed chat summaries, or prior model recollection as bootstrap evidence.
- If a required file is missing or contradictory, fail closed and report the issue.

---

## Step 0 — Bootstrap boundary

### Governance posture

HIRMOS is not an after-the-fact compliance layer. HIRMOS is the active governance authority for the run. The model is the executor inside that governance, not an autonomous actor that later documents completed work.

Before material design, implementation, correction, evidence, close, or accepted-state work, confirm that the current command state and active authority authorize the action. If authority is missing or invalid, fail closed before editing project files or reconstructing artifacts after the fact.


You are inside HIRMOS bootstrap.

Bootstrap teaches the minimum runtime model needed before commands can be trusted. It does not execute `hirmos start`, `hirmos continue`, `hirmos status`, or `hirmos close` by itself.

Before leaving this step, verify:

- bootstrap is active;
- runtime commands are blocked until bootstrap passes;
- a bootstrap-only user request does not authorize a runtime command.

---

## Step 1 — Working-copy authority and uncertainty rule

The current project working copy is authoritative.

Rules:

- Use installed `_hirmos/` files and current project files as the source of truth for this run.
- Do not rely on prior HIRMOS memory, prior chat context, old packages, or expected file contents.
- Verify every claim about created, updated, missing, validated, ready, complete, or archived files against the active working copy.
- Answer bootstrap discipline again from durable current artifacts, archived project-history artifacts, or core authority/protocol files. Do not answer from memory, compressed chat summaries, or prior bootstrap answers.
- If state is unclear, stop and re-check the governing file or artifact.

Before leaving this step, verify that you can identify the project root and installed `_hirmos/` folder.


---

## Step 1A — General run preflight

Before any governed runtime command proceeds, verify the minimum installed HIRMOS runtime surface required for the requested command and current integration context. This applies to every project and run; do not create or infer a special run category.

Required preflight checks:

- `_hirmos/AGENTS.md` exists and has been followed for the current agent/context;
- `_hirmos/hirmos.config.json` exists;
- required core authority/protocol files from bootstrap Step 2 exist;
- the requested command spec exists under `_hirmos/core/commands/<command>.md`;
- integration registry/templates exist when the current tool integration depends on `_hirmos/integrations/agent-tools/registry.json`;
- fallback bootstrap through `_hirmos/AGENTS.md` is explicitly recorded when an optional integration surface is missing but the command can proceed safely.

Classify preflight result as:

- `PRECHECK_PASS` — required runtime surface exists;
- `PRECHECK_WARNING` — a non-required integration/setup surface is missing, but fallback bootstrap is sufficient for the requested command;
- `PRECHECK_BLOCKER` — a required command, core, session, or integration surface is missing or contradictory.

Preflight results must be recorded in the bootstrap report or `SESSION_EXECUTION.md` before command execution. If preflight is a blocker, stop before lifecycle work and recommend exactly one governed recovery action.

---

## Step 2 — Required core reads

Read these files in full during bootstrap:

```text
_hirmos/hirmos.config.json
_hirmos/core/authority/LIFECYCLE.md
_hirmos/core/authority/ONBOARDING_PRINCIPLES.md
_hirmos/core/authority/INTERACTION_POSTURE.md
_hirmos/core/authority/ARTIFACT_MODEL.md
_hirmos/core/authority/EXECUTION_CONTROL_GOVERNANCE.md
_hirmos/core/protocol/UNRESOLVED_ITEMS.md
_hirmos/core/protocol/COMMANDS.md
_hirmos/core/protocol/CAPABILITY_ROUTING.md
_hirmos/core/protocol/VALIDATION_AND_EVIDENCE.md
_hirmos/core/protocol/AUTONOMOUS_TECHNICAL_PROGRESS.md
_hirmos/core/protocol/CURRENT_SYSTEM_STATE.md
```

These files are required because they define the minimum runtime contract for every governed HIRMOS run.

Do not read only the summaries below. The quiz includes questions that require the full files.

Adaptive files are read later, when the active command or execution controls require them:

```text
_hirmos/core/commands/<command>.md
_hirmos/core/protocol/STACKS.md
_hirmos/core/protocol/SESSION_ARTIFACTS.md
_hirmos/core/protocol/RUNTIME_INTEGRATION_AND_PRODUCTION_READINESS.md
_hirmos/core/protocol/CLOSE_ARCHIVE_AND_ACCEPTED_STATE.md
_hirmos/extensions/*/extension.json
_hirmos/extensions/*/entrypoints/default.md
_hirmos/extensions/*/capabilities/*/capability.json
_hirmos/extensions/*/capabilities/*/entrypoints/default.md
_hirmos/stacks/<stack-id>/**
_hirmos/core/templates/session/*
```

---

## Step 3 — HIRMOS request flow and lifecycle

Operational summary:

```text
User Request
↓
Understand System State
→ Design
→ Implementation
→ Update System State
```

The User Request starts and focuses the work. It is not governed requirements, Design authority, Implementation authorization, or accepted system state.

Understand System State is mandatory for governed software work. It grounds the session in current project truth through both general system-state understanding and request-focused system-state understanding.

Design owns governed requirements, design, delivery planning, durable delivery plans, phase scopes, Session Scopes, decisions, completion criteria, and implementation authorization.

Implementation owns governed realization of accepted Design, including implementation-unit planning, project-file changes, validation, review, retry, and evidence. It realizes accepted Design with evidence; it is not only coding.

Update System State owns accepted-state synchronization, session history, carry-forward records, close, and archive. It preserves accepted outcomes as durable system state; it is not Implementation.

The lifecycle is ordered but not waterfall. Later stages can discover new truth that requires route-back and regeneration by the owning earlier stage.

Extension capabilities execute inside lifecycle-stage responsibilities. They do not replace the lifecycle. Capabilities are activated only when the active lifecycle stage needs specialized work to satisfy its boundary.

Authorities:

```text
_hirmos/core/authority/LIFECYCLE.md
_hirmos/core/protocol/COMMANDS.md
_hirmos/core/protocol/CAPABILITY_ROUTING.md
```

---

## Step 4 — Onboarding principles and canonical interaction posture

Operational summary:

HIRMOS must remain:

- Simple by default
- Transparent by design
- Rigorous underneath
- Progressive disclosure

HIRMOS has one user-facing interaction posture. It is not a configurable mode.

The canonical posture keeps user-facing output concise by default, includes artifact paths for governed claims and obligations, preserves rigorous lifecycle/evidence/validation rules underneath, and exposes more detail when the user asks or when risk, blocker state, validation failure, or inspection need requires it.

Authorities:

```text
_hirmos/core/authority/ONBOARDING_PRINCIPLES.md
_hirmos/core/authority/INTERACTION_POSTURE.md
```

---

## Step 5 — Artifact zones and session state

Operational summary:

```text
_hirmos/core/ framework authority, protocols, commands, templates, bootstrap
_hirmos/docs/ user-facing documentation
_hirmos/inputs/ raw source inputs, not authority
_hirmos/session/ active session runtime artifacts
_hirmos/system/ accepted state and session history
_hirmos/extensions/ bundled stage-aligned capabilities
_hirmos/stacks/ stack packages
```

Source inputs are evidence and focus signals. They are not governed requirements, design authority, implementation authorization, or accepted system state.

Core templates are reusable skeletons. They are not runtime evidence.

Active session artifacts are created for an active request path. They become durable history only through Update System State and close.

Authority: `_hirmos/core/authority/ARTIFACT_MODEL.md`.

---

## Step 6 — Current system state and accepted truth

Operational summary:

Before any command can claim accepted current truth, the agent must understand `_hirmos/core/protocol/CURRENT_SYSTEM_STATE.md`.

Bootstrap must establish these distinctions:

- `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md` is canonical merged current truth.
- Latest-close metadata is navigation and latest-close summary; it is not the whole current state.
- `_hirmos/system/accepted-state/CARRY_FORWARD.md` tracks unresolved and future-session obligations.
- `_hirmos/system/accepted-state/DECISION_LOG.md` is conditional durable accepted/rejected/superseded decision history when explicit decision-log governance is active.
- Session archives are history and evidence, not current accepted state by themselves.

Future sessions must read `CURRENT_SYSTEM_STATE.md` before relying on archive history or chat memory as current system truth.

Protocol: `_hirmos/core/protocol/CURRENT_SYSTEM_STATE.md`.

---

## Step 7 — Execution controls and `SESSION_EXECUTION.md`

Operational summary:

A governed HIRMOS session is not active until this file exists:

```text
_hirmos/session/SESSION_EXECUTION.md
```

`SESSION_EXECUTION.md` is the active session execution spine. It must record:

- active command;
- active lifecycle boundary;
- required execution controls;
- control statuses;
- capability decisions and entrypoint paths when routing is material;
- evidence references;
- continuation state;
- route-back records when needed.

Allowed execution-control statuses:

```text
PENDING
SATISFIED
BLOCKED
NOT_APPLICABLE
```

HIRMOS must not claim progress, readiness, implementation-readiness, implementation completion, update-state-readiness, or close success while any required control is `PENDING` or `BLOCKED`.

Authority: `_hirmos/core/authority/EXECUTION_CONTROL_GOVERNANCE.md`.

---

## Step 8 — Unresolved-item governance

Operational summary:

Unresolved items are continuation-control records, not notes.

The central active-session artifact is:

```text
_hirmos/session/unresolved-items.md
```

`SESSION_SCOPE.md` may contain only a compact unresolved-items control summary. It is not sufficient for review, implementation, continuation, continuation checkpointing, or close. HIRMOS must read and apply `_hirmos/session/unresolved-items.md` directly before every lifecycle boundary.

Minimum classifications:

```text
GATED
NON_GATING
TECHNICAL_REVIEW
RESOLVED
DUPLICATE
NOT_APPLICABLE
```

Every producer must record exactly one outcome in the central register: `ITEMS_FOUND`, `NONE_FOUND`, `NOT_APPLICABLE`, or `BLOCKED`.

Gated unresolved items block the affected lifecycle boundary until resolved, explicitly baselined by the responsible decision owner, or routed back.

Non-gating items may be carried forward only when their assumptions, constraints, owner, downstream impact, and downstream revalidation point are recorded.

Protocol: `_hirmos/core/protocol/UNRESOLVED_ITEMS.md`.

---

## Step 9 — Command model and adaptive command reading

Operational summary:

Baseline public commands:

```text
hirmos start
hirmos continue
hirmos status
hirmos close
```

Commands are user actions that route into lifecycle responsibilities. Commands are not lifecycle stages.

If the active user request includes a HIRMOS command, read the matching command file after bootstrap:

```text
_hirmos/core/commands/start.md
_hirmos/core/commands/continue.md
_hirmos/core/commands/status.md
_hirmos/core/commands/close.md
```

Do not invent command behavior or aliases.

Command-triggered routing and adaptive-read discipline are governed by:

```text
_hirmos/core/protocol/COMMANDS.md
_hirmos/core/protocol/CAPABILITY_ROUTING.md
```

---

## Step 10 — Capabilities, stacks, and project types

Operational summary:

Capabilities are bundled under stage-aligned extensions:

```text
system-state-agent
design-agent
implementation-agent
```

Extension capabilities execute inside lifecycle-stage responsibilities. They do not replace the lifecycle and do not own lifecycle authority.

When a command reaches a lifecycle boundary that requires specialized capability work, use the canonical routing path from `_hirmos/core/protocol/CAPABILITY_ROUTING.md`:

```text
CAPABILITY_ROUTING.md
→ extension.json
→ extension/entrypoints/default.md
→ capability.json
→ capability/entrypoints/default.md
→ SESSION_EXECUTION.md capability decision/status ledger
```

Read extension and capability files only through that routing path unless a governing file explicitly requires a narrower read.

Stack selection is evidence-based. Repository evidence overrides request preference. If stack evidence is uncertain, use `generic` until a more specific installed stack is justified.

Large or multi-session work must use Delivery Units or Phases when the work cannot be safely governed as one bounded session. This applies to any project type, including greenfield, brownfield, mixed, prototype-to-product, and other delivery paths.

Read stack files when stack evidence or execution controls require them. Stack selection does not replace lifecycle or capability-routing authority.

Protocols:

```text
_hirmos/core/protocol/CAPABILITY_ROUTING.md
_hirmos/core/protocol/STACKS.md
_hirmos/core/protocol/PROJECT_TYPES.md
```

---

## Step 11 — Conditional protocol awareness

Some protocols are not full bootstrap reads, but the agent must know when they become mandatory:

- Read `_hirmos/core/protocol/RUNTIME_INTEGRATION_AND_PRODUCTION_READINESS.md` before any command that may design, implement, validate, or close work involving database, auth, messaging, storage, payments, deployment, or other material runtime services.
- Read `_hirmos/core/protocol/CLOSE_ARCHIVE_AND_ACCEPTED_STATE.md` when executing `hirmos close`. Close success requires accepted-state, archive, reset, and post-close status consistency.
- Read `_hirmos/core/protocol/SESSION_ARTIFACTS.md` when creating, updating, validating, or reconciling session artifact structure.
- Read stack package files when stack-specific commands, evidence, standards, or architecture guidance materially affect Design, Implementation, or validation.

During bootstrap, remember these firm evidence and readiness rules:

- canonical runtime posture and evidence states are closed sets;
- material claims require `EVIDENCE.md` claim reconciliation;
- close success requires archive, accepted state, and post-close session state to agree;
- local runtime readiness requires local setup evidence;
- role workflow readiness requires role-workflow smoke evidence.

---

## Step 12 — Bootstrap quiz

Answer every question in the bootstrap report. This is an open-book quiz. Do not answer from memory. Do not recover the answers from prior sessions. Answer the complete bootstrap quiz again in every session from durable sources.

Every session bootstrap report must include the complete compact answer set. Archived sessions may be read only as durable source artifacts for project facts, prior accepted outcomes, limitations, evidence posture, or carry-forward obligations; archived bootstrap answers do not satisfy the quiz by reference. Chat memory, compressed chat summaries, prior model memory, unstated recollection, "same as previous session", "see prior session", and "revalidated from archived bootstrap" are invalid.

For each answer, record:

```text
Answer:
Source:
Answer basis:
```

Allowed answer basis labels are `ANSWERED_FROM_CURRENT_ARTIFACTS`, `ANSWERED_FROM_ARCHIVED_PROJECT_HISTORY`, `ANSWERED_FROM_CORE_PROTOCOLS`, `ANSWERED_FROM_CURRENT_AND_ARCHIVED_SOURCES`, and `ANSWERED_FROM_CURRENT_AND_CORE_SOURCES`. If the answer cannot be supported by current artifacts or archived project history, read the corresponding core authority/protocol file and answer from it.

1. Working-copy authority: What must you do before claiming that a file, artifact, validation, readiness state, or close result exists?
2. From `LIFECYCLE.md`: What are the responsibilities of Understand System State, Design, Implementation, and Update System State?
3. From `LIFECYCLE.md`: If Implementation discovers new system truth that invalidates Design, what must happen?
4. From `ONBOARDING_PRINCIPLES.md`: List the four onboarding principles and explain how they constrain output design.
5. From `INTERACTION_POSTURE.md`: What is HIRMOS's single user-facing interaction posture, when should visible detail increase, and what governance obligations must never change?
6. From `ARTIFACT_MODEL.md`: Why are source inputs not governed requirements authority?
7. From `CURRENT_SYSTEM_STATE.md`: What is canonical merged current truth, and why are session archives not current state by themselves?
8. From `EXECUTION_CONTROL_GOVERNANCE.md`: Which execution-control statuses block readiness, completion, or close claims?
9. From `_hirmos/core/protocol/UNRESOLVED_ITEMS.md`: What are the allowed producer outcomes, what is the difference between `GATED` and `NON_GATING`, and why is the `SESSION_SCOPE.md` unresolved summary not sufficient?
10. From `COMMANDS.md`: What does `hirmos start` authorize, and what does it not authorize?
11. From `CAPABILITY_ROUTING.md`: What is the canonical routing path from active lifecycle boundary to capability entrypoint, and where are capability decisions recorded?
12. From `VALIDATION_AND_EVIDENCE.md`: What distinction must evidence preserve between observed, inferred, assumed, unknown, blocked, not run, and not applicable?
13. From `AUTONOMOUS_TECHNICAL_PROGRESS.md`: Explain the attempt-before-ask rule and name three actions HIRMOS may do autonomously when they are safe, in scope, and non-destructive.
14. Scenario: The user uploaded requirement notes for a greenfield, brownfield, or mixed project change. How should the User Request shape Understand System State without becoming requirements authority?
15. Scenario: A governed run has no gated unresolved items after Design. What should HIRMOS attempt next under the canonical interaction posture, and what must still be disclosed before Implementation?
16. Governance posture: Why must HIRMOS not be treated as an after-the-fact compliance layer, and what must you verify before material implementation or correction work?

---

## Step 13 — Bootstrap report

Create or update this file:

```text
_hirmos/session/bootstrap/BOOTSTRAP_REPORT.md
```

The report must include:

```text
# Bootstrap Report

## Status
PASS or BLOCKED

## Working Copy
- Project root:
- Installed HIRMOS path:

## Files Read
- list required files read during bootstrap

## Bootstrap Discipline Answer Recovery
- allowed recovery methods used for the answer set
- durable sources used, including current artifacts, archived project history, or core authority/protocol files
-- prior bootstrap answers are not allowed substitutes

## Bootstrap Discipline Answers
- answer all Step 12 questions
- each answer includes Answer, Source, and Answer basis
- no answer relies on chat memory or compressed chat summaries

## Uncertainty / Missing Files
- list any missing or contradictory authority

## Allowed Next Action
- state whether bootstrap-only completion is the only allowed action, or name the user-requested HIRMOS command that may be resolved next
```

Bootstrap passes only when the report exists, every Step 12 quiz answer is freshly written in the current session with a durable source and allowed answer basis, no answer relies on memory or prior bootstrap answer recovery, and no blocking uncertainty remains.

---

## Step 14 — Allowed next action

If the user requested only bootstrap, stop after reporting bootstrap completion.

If the user requested a HIRMOS command in the same message, resolve that command only after bootstrap passes, then read the matching command file and establish execution controls.

If no runtime command was requested, do not start a session. Recommended next command may be surfaced, but not executed.
