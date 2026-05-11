# HIRMOS_ORCHESTRATOR.md

This file is the human/operator playbook for working with the HIRMOS Core.

## First step

Before asking the framework to run anything, initialize your AI tool by saying:

```text
Read and follow the instructions on _hirmos/HIRMOS_CORE.md
```

This loads `_hirmos/HIRMOS_CORE.md` and starts the Core bootstrap path.

That bootstrap step loads the core rules and command protocol before any extension work begins. `_hirmos/HIRMOS_CORE.md` is only the bootstrap/orchestration entrypoint; the real runtime behavior comes from the core contract and installed extensions.

## Supported command surface

Workflow commands use this shape:

```text
hirmos <command>
hirmos <command>:<entrypoint>
```

Examples:

```text
hirmos requirements
hirmos system-design
hirmos implementation
hirmos system-design:phase-design-cycle
```

Core utility commands:

```text
hirmos list extensions
hirmos describe extension <id>
hirmos describe extension <id>:<entrypoint>
hirmos explain <command>
hirmos explain <command>:<entrypoint>
```

## Command meanings

- `hirmos <command>` runs the manifest-declared workflow command exposed by an installed extension.
- `hirmos <command>:<entrypoint>` resolves the same command owner, then runs a named public entrypoint from that extension.
- `hirmos describe extension ...` inspects an extension or one of its named public entrypoints.
- `hirmos explain ...` shows the resolved plan for a workflow command without executing it.

Use `hirmos list extensions` and `hirmos describe extension <id>` when you need to inspect available commands. Do not assume cycle names, concept names, or extension-spec filenames are valid command aliases.

## Core-owned terminal output wrapper

- The Core owns the final chat-facing terminal output wrapper.
- The wrapper has two fields:
  - `Identity`
  - `Response`
- `Identity` is resolved and rendered by Core.
- `Response` is authored by the active producer.
- The active producer may be Core or an extension.
- `[HIRMOS]` is used for bootstrap, dispatch, and genuinely framework-native/Core-native terminal output.
- When an extension declares `runtime.identity`, the Core uses that manifest-declared identity for extension-produced terminal output.
- If an extension does not declare `runtime.identity`, no extension identity label is shown.
- Missing the required Core-owned terminal output wrapper makes a runnable terminal result invalid or incomplete.
- Treat plain runnable prose that reaches the chat surface without the wrapper as a contract failure, not as an acceptable near-miss.

Canonical rendered example:

```text
[HIRMOS]
Command resolved: hirmos system-design

[System Design Agent]
...response body...
```

## Canonical authority lanes

HIRMOS allows multiple design-oriented or implementation-oriented extensions to be installed in the same project, but canonical project lanes remain single-owner-at-a-time by use, not by installation.

- Multiple system-design-focused extensions may be installed, but only one can be **used as** the design authority at a time.
- The system-design extension currently being used as the design authority owns canonical writes to:
  - `/_hirmos/artifacts/sot/`
  - `/_hirmos/artifacts/phases/`

- Multiple implementation-focused extensions may be installed, but only one can be **used as** the implementation authority for code-changing execution at a time.
- The implementation extension currently being used as the implementation authority owns canonical writes to:
  - `/_hirmos/artifacts/prompts/`
  - `/_hirmos/artifacts/ops/`
  - project code changes

If you want to compare alternatives from other installed extensions, treat those as candidate outputs until you intentionally replace the current canonical project artifacts or code-changing workflow with the new authority in use.

## Operator guidance

- Start with the highest-level coherent command that fits the job.
- Drop to lower-level reusable entrypoints when you need tighter control or a narrower reusable unit.
- Use `hirmos describe extension <id>` before running a command when you want to inspect an extension's public surface.
- Use `hirmos explain <command>` when you want to inspect hooks and execution order before running.
- Prefer adding capabilities as extensions instead of expanding the core.
- Progress updates do not mean a runnable command is finished.
- Treat a runnable command as complete only when a terminal run-state block is emitted.
- If a command response ends without a terminal run-state block, treat it as incomplete and ask the assistant to continue from the current working copy.
- If a runnable command response appears without the Core-owned terminal output wrapper, treat it as incomplete/non-compliant and ask for corrected output from the current working copy.
- The terminal run-state block should identify the command, run state, major artifacts updated, a short summary, and the next action.

## Decision checkpoints

Some cycles may continue autonomously when uncertainty is low enough. Others may pause and request Orchestrator direction when unresolved items materially affect scope, workflow shape, delivery feasibility, compliance posture, or downstream planning truth.

Allowed outcomes:

- **Use assumption** — Proceed with an explicitly labeled Orchestrator-approved planning assumption. It does not become source-confirmed truth.
- **Ask customer** — Pause and produce the exact questions that need confirmation, plus what planning remains unstable until answers arrive.
- **Defer and constrain** — Proceed only if downstream planning is intentionally narrowed so the unresolved item does not silently expand into the design.

When a serious cycle reaches a decision checkpoint, it should pause in chat and request Orchestrator direction directly rather than silently continuing or quietly treating the run as complete. The current trust state should also be reflected in the relevant command-scoped `CYCLE_STATUS.md` artifact under `_hirmos/artifacts/context/system-design-agent/<cycle>/`.

When a serious cycle pauses, the chat-facing pause block must include:

- cycle state
- unresolved items
- why they matter
- allowed outcomes when the entrypoint or extension-local spec defines them
- **Proposed Orchestrator direction**
- **Continuation options**

Any proposed direction is advisory only until the Orchestrator explicitly accepts or modifies it.

## Cycle states

Serious cycles may end in one of these governed states:

- completed
- paused
- failed

Do not treat incomplete output as completion merely because the response sounds confident.
