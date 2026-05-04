# HIRMOS_ORCHESTRATOR.md

This file is the human/operator playbook for working with the HIRMOS Core.

## First step

Before asking the framework to run anything, initialize your AI tool by saying:

```text
Read and follow the instructions on _hirmos/HIRMOS_CORE.md
```

That bootstrap step loads the core rules and command protocol before any extension work begins.
`_hirmos/HIRMOS_CORE.md` is only the bootstrap/orchestration entrypoint; the real runtime behavior comes from the core contract and installed extensions.

## Supported commands

```text
cmd: run extension <id>
cmd: run extension <id>:<entrypoint>
cmd: describe extension <id>
cmd: describe extension <id>:<entrypoint>
cmd: list extensions
cmd: explain run extension <id>
cmd: explain run extension <id>:<entrypoint>
```

## Command meanings
Use the exact public entrypoint names shown by `cmd: describe extension <id>`. Do not assume cycle names, concept names, or extension-spec filenames are valid command aliases.


- `run extension <id>` uses the extension's default public entrypoint.
- `run extension <id>:<entrypoint>` uses a named public entrypoint exposed by that extension.
- `describe ...` inspects an extension or one of its named public entrypoints.
- `explain run ...` shows the resolved plan without executing it.

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
Command resolved: run extension system-design-agent:system-design-cycle

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

- Start with the highest-level coherent entrypoint that fits the job.
- Drop to lower-level reusable entrypoints when you need tighter control or a narrower reusable unit.
- Use `describe` before `run` when you want to inspect an extension's public surface.
- Use `explain run` when you want to inspect hooks and execution order before running.
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

- **Completed** — the cycle is governably finalized for the current dependency state.
- **Paused** — the cycle stopped at a decision checkpoint and is waiting for Orchestrator direction.
- **Provisional** — the cycle was allowed to run despite unresolved upstream gating, so the outputs are useful for exploration and steering but are not yet the current authoritative finalized state.

## Provisional downstream runs

When you ask a downstream cycle to run while upstream gating items still remain unresolved, the framework should allow the command to run, but it must warn you before continuing.

That warning should state:

- the command will run;
- the resulting state will be `provisional`;
- why the state is provisional;
- one short sentence explaining that the outputs are useful for exploration and steering but must not be treated as the current authoritative finalized state.

Once the upstream gating items are later resolved in a materially cycle-shaping way, earlier downstream trust artifacts become **stale by dependency** and should be rerun before being treated as current authoritative status.

## Important boundary

Not every internal file inside an extension is a public runnable surface.

Public runnable surfaces must be declared by the extension manifest:

- `entry` defines the default public entrypoint
- `entrypoints` defines optional named public entrypoints

Serious extensions may use extension-local specs to define local method, validation, and quality expectations for important entrypoints.
