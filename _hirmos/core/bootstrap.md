# HIRMOS Bootstrap Full

Read this file in order.

This file is the assembled bootstrap path that begins at `_hirmos/core/bootstrap.md`.
Use it to complete bootstrap from start to finish before substantive command execution begins.

Operational rules:
- do not skip ahead;
- do not treat partial reading as bootstrap completion;
- do not claim command readiness before the quiz gate and bootstrap proof step is satisfied.
- bootstrap readiness now depends on the quiz-only pre-bootstrap gate recorded in `_hirmos/artifacts/context/core/bootstrap-report.md`.

---

# Step 0 — Framework-wide uncertainty rule

At the slightest uncertainty, do not proceed from memory. Re-check the relevant governing file, artifact, or section before answering, executing, validating, or surfacing results.

Apply this rule especially at:
- extension entrypoints
- state-transition points
- truth-claim points
- validation points

---

# Step 1 — Accept the bootstrap boundary before doing any real work

## Bootstrap rule

You are now inside the Core bootstrap process that begins at `_hirmos/core/bootstrap.md`.

Do not begin substantive command execution until bootstrap is complete.
Do not treat reading one bootstrap file as bootstrap completion.
Do not skip ahead to extension work, stack work, or task execution.

## What the LLM must do now

- continue through this bootstrap in order;
- learn the Core rules that govern command execution before acting on any command;
- wait to claim initialization is complete until the quiz gate and bootstrap proof step is satisfied.

## What the LLM must not do now

- run a framework command;
- improvise a workflow from memory;
- treat partial reading as sufficient initialization;
- claim readiness for substantive work before bootstrap proof is complete.

## Operational rule

Until bootstrap is complete, do not begin substantive command execution or claim command readiness.

## Bootstrap checkpoint

Before leaving Step 1, verify all of the following:

- Core bootstrap is active.
- Substantive command execution is blocked until bootstrap completes.
- Command readiness is blocked until the bootstrap completion report authorizes it.

---

# Step 1A — Establish authoritative cumulative working-copy discipline

## Why this must be understood now

Bootstrap cannot be trusted if the runtime starts from memory, switches between snapshots, or makes artifact/readiness claims without verifying the current cumulative state.

## Operational rule — authoritative cumulative working copy

- For this run, the provided framework files are the authoritative source of truth.
- The active local working copy derived from those framework files is authoritative and cumulative for the run.
- All file, artifact, readiness, and completion claims must be verified against that current cumulative working copy.
- Do not switch back to the original uploaded zip, an earlier extracted snapshot, or another earlier framework state unless the user explicitly replaces the active working copy.
- Do not describe intended updates as completed updates unless they exist in the active cumulative working copy.

## Bootstrap checkpoint

Before leaving Step 1A, verify all of the following:

- I understand that the active local working copy remains authoritative and cumulative for the run.
- I must verify artifact and readiness claims against that current cumulative working copy.
- I must not describe intended changes as completed if they are not present in that working copy.
- If continuity becomes unclear, I must fail closed.

## Fail-closed rule

If the runtime cannot truthfully verify the current cumulative working-copy state, it must not claim artifact creation, bootstrap completion, command readiness, or downstream run continuity.

---

# Step 2 — Understand what the Core is and what it is not

## Why this must be understood now

Do not let the Core absorb business workflow logic, long agent instructions, or domain policies.

## Required understanding

The Core is intentionally small.
It owns runtime coordination, validation, resolution, and execution controls.
It does **not** own workflow-specific intelligence that belongs in extensions or stack packages.

## Core responsibilities

The Core must do only the following:

1. Bootstrap framework operation through `HIRMOS_CORE.md` and `_hirmos/core/bootstrap.md`.
2. Discover installed extensions.
3. Read and validate extension manifests.
4. Resolve public runnable surfaces declared by manifests.
5. Validate required dependencies.
6. Build a deterministic run plan.
7. Initialize and maintain `RUN_EXECUTION_CONTROLS.md` for the active command.
8. Compose hook contributions for the requested extension.
9. Resolve the active stack package and expose normalized stack context.
10. Execute the target extension using the composed context.
11. Emit a concise execution trace.

## Core non-goals

The Core must not contain:
- role-specific long instructions;
- business workflows;
- cycle logic;
- deliverable templates;
- domain-specific policies;
- client-specific behavior;
- stack-specific content.

Those belong in extensions or stack packages.

## Additional Core rules that matter during bootstrap

### Extension ownership rule
If a new capability can be expressed as:
- a new runnable unit;
- a named public entrypoint;
- a hook contribution;
- an optional policy pack;
- a reusable template,

then it should be added as an extension instead of expanding the Core.

### Manifest public-surface rule
The Core must treat extension manifests as authoritative for public runnable surfaces.
That means:
- `entry` defines the default public entrypoint;
- `entrypoints` defines named public entrypoints;
- hooks are public contributions declared by manifests;
- not every internal file inside an extension is publicly runnable.

### Run determinism rule
The same installed extension set should produce the same run plan unless the Orchestrator changes the requested command or inputs.

### Run explainability rule
A run should be explainable in terms of:
- target extension;
- target entrypoint;
- dependencies loaded;
- hook contributors loaded;
- final execution order.

## Operational rule

During bootstrap and later execution, do not let Core absorb extension-side behavior.
If something feels like workflow intelligence, domain policy, or deliverable structure, it probably belongs outside the Core.

## Bootstrap checkpoint

Before leaving Step 2, verify all of the following:

- The Core owns runtime coordination and validation.
- The Core does not own business workflow behavior.
- Public runnable surfaces come from extension manifests, not from arbitrary internal files.

---

# Step 3 — Learn the allowed command surface before interpreting commands

## Why this must be understood now

Do not invent aliases, paraphrase commands into new public commands, or treat extension filenames as public entrypoints.

## Operational rule — command identification

Inputs beginning with `cmd:` must be treated as attempted Core commands.

After removing the `cmd:` prefix and any immediately following whitespace, the remaining text must be matched against the exact supported Core command surface taught in this step.

Do not reinterpret a `cmd:` input as ordinary prose, folder-inspection intent, or best-effort conversational assistance.

Only after a `cmd:` input is successfully matched as a supported Core command may the runtime proceed into the command-resolution and execution-control lifecycle.

## Operational rule — runtime-folder creation boundary

Runtime folders such as `_hirmos/inputs/<extension-id>/`, `_hirmos/artifacts/context/<extension-id>/`, and `_hirmos/artifacts/outputs/<extension-id>/` are project runtime surfaces; Core/entrypoints must create missing runtime folders during init or first run.

## Supported commands

The public Core command surface is:

```text
cmd: list extensions
cmd: describe extension <id>
cmd: describe extension <id>:<entrypoint>
cmd: run extension <id> [arguments...]
cmd: run extension <id>:<entrypoint> [arguments...]
cmd: explain run extension <id> [arguments...]
cmd: explain run extension <id>:<entrypoint> [arguments...]
```

## Command matching rules

- `cmd:` is the Core command-intent prefix.
- Command words after `cmd:` are lowercase.
- Extension ids must match manifest ids.
- Entrypoint names must match manifest `entrypoints` keys when used.
- The Core does not invent aliases.
- Harmless trailing punctuation immediately after an otherwise valid command may be ignored during normalization.
- Unknown names fail clearly.
- If the text after `cmd:` does not exactly match a supported Core command form, fail clearly.

## Fail-closed rule — unsupported or malformed cmd inputs

- If an input begins with `cmd:` but does not match an exact supported Core command form, the runtime must fail closed.
- The runtime must not downgrade the prompt into ordinary prose help.
- The runtime must not best-guess the intended command.
- The runtime must surface a clear invalid-command result instead of a normal answer.
- When corrective guidance is surfaced for an invalid `cmd:` input, recommend only supported `cmd:` public command forms.
- Do not recommend old bare forms such as `list extensions`, `describe extension <id>`, or `describe extension <id>:<entrypoint>`.

## Dependency behavior

`requires` is currently an extension-level dependency field.

Rules:
- every id listed in `requires` must refer to an installed extension;
- if a required extension is missing, fail clearly;
- `requires` does not currently express entrypoint-level dependencies.

## Command semantics the bootstrap must understand

### `cmd: run extension <id> [arguments...]`

Interpretation:
1. resolve the target extension id;
2. capture any trailing argument tail for the active entrypoint;
3. load and validate the target manifest;
4. confirm the target includes `runnable` in `types`;
5. resolve the default public entrypoint from `entry`;
6. validate required dependencies declared in `requires`;
7. resolve the active stack from `_hirmos/STACK_CONFIG.json` and the selected stack package;
8. follow the run execution controls model for the outer command path and any controls added for this run;
9. read and honor the resolved entrypoint's `Execution Contract` section;
10. pass the captured argument tail to the active entrypoint and execute the workflow.

### `cmd: run extension <id>:<entrypoint> [arguments...]`

Interpretation:
1. resolve the target extension id;
2. capture any trailing argument tail for the active entrypoint;
3. load and validate the target manifest;
4. confirm the target includes `runnable` in `types`;
5. resolve the named public entrypoint from `entrypoints.<entrypoint>`;
6. validate required dependencies declared in `requires`;
7. resolve the active stack from `_hirmos/STACK_CONFIG.json` and the selected stack package;
8. follow the run execution controls model for the outer command path and any controls added for this run;
9. read and honor the resolved entrypoint's `Execution Contract` section;
10. pass the captured argument tail to the active entrypoint and execute the workflow.

### `cmd: describe extension <id>`
The response should include:
- extension id;
- types;
- summary;
- default entrypoint if present;
- named public entrypoints if present;
- declared dependencies if present;
- exposed hooks if present;
- hook subscriptions if present.

### `cmd: describe extension <id>:<entrypoint>`
The response should include:
- extension id;
- target entrypoint name;
- resolved relative file path;
- extension summary;
- extension types;
- any exposed hooks relevant to that entrypoint;
- the entrypoint execution-contract summary: purpose, produces, and terminal states.

### `cmd: list extensions`
List installed extensions showing:
- extension id;
- types;
- summary.

### `cmd: explain run extension ...`
The response should include:
- the resolved entry file;
- the active stack id;
- any exposed hooks relevant to the active entrypoint;
- matching hook subscriptions;
- hook order;
- the execution controls that would be added for the run.

## Entrypoint arguments

`cmd: run extension ...` and `cmd: explain run extension ...` may include an optional argument tail after the resolved extension target.

Rules:
- the Core resolves only the extension id and optional entrypoint name;
- any remaining trailing text is treated as the entrypoint argument tail;
- the Core does not assign semantic meaning to that tail;
- argument parsing and validation belong to the owning extension;
- if an entrypoint requires parameters, its entry file and local extension spec must document them clearly.

## Operational rule

From this point onward, the LLM must not invent commands that are not part of the Core command surface.
It must also stop treating internal filenames or workflow nicknames as if they were public commands.
It must not treat bare prose prompts as Core commands by default.

## Bootstrap checkpoint — command intent

Before leaving Step 3, verify all of the following:

- I understand that `cmd:` is the Core command-intent marker.
- I will not interpret a `cmd:` input as ordinary prose.
- I will only treat the text after `cmd:` as a Core command if it matches the exact supported command surface.
- If a `cmd:` input does not match the supported command surface, I must fail closed.
- Extension manifests govern public runnable surfaces.
- Argument meaning belongs to the resolved extension entrypoint, not to the Core.

---

# Step 4 — Learn the outer execution lifecycle before any command can be trusted

## Why this must be understood now

This step defines the Core-owned outer execution lifecycle for running any command.
If this step is skipped, a run can sound correct while missing the controls that make completion trustworthy.

## Mandatory run artifact

Every command must create or refresh `RUN_EXECUTION_CONTROLS.md`.

Use `_hirmos/core/templates/RUN_EXECUTION_CONTROLS_TEMPLATE.md` as the template source.
Create or refresh the run-scoped artifact at:

```text
_hirmos/artifacts/context/<extension-id>/<extension-entrypoint>/RUN_EXECUTION_CONTROLS.md
```

`RUN_EXECUTION_CONTROLS.md` is a Core-owned, run-scoped artifact. It records which execution controls apply to the active run, where each control is governed, and whether each listed control is still `PENDING` or already `EXECUTED`.

When a control is listed in `RUN_EXECUTION_CONTROLS.md`, its governing file becomes mandatory authority for that run.

## Default initialization

Every command starts by seeding `Identity display execution control`.

## Command-specific enrichment

After default initialization, the Core must add every additional execution control required by the resolved command and run characteristics.

Examples:
- `cmd: run extension ...` must add `Extension execution control`;
- hook-aware runs must add `Hook execution control`;
- future commands must add any other Core-owned or command-specific controls they require.

## Execution control status model

Allowed statuses:
- `PENDING`
- `EXECUTED`

Every listed control starts as `PENDING`.

A listed control may be updated to `EXECUTED` only after the LLM has followed that control's governing file sufficiently for trustworthy continuation or completion.

## Outer command sequence

For running any command, the Core owns this outer execution sequence:

1. resolve the command;
2. create or refresh `RUN_EXECUTION_CONTROLS.md`;
3. seed `Identity display execution control`;
4. enrich the control list for the resolved command and run characteristics;
5. follow each listed governing file during execution;
6. update listed controls from `PENDING` to `EXECUTED` when satisfied;
7. validate that every listed control is `EXECUTED`;
8. only then surface trustworthy completion.

## Self-validation before trustworthy completion

Before trustworthy completion is surfaced, the Core must verify:
- `RUN_EXECUTION_CONTROLS.md` exists at the run-scoped path;
- the default baseline control was seeded;
- any additional required controls for the resolved command were added;
- every listed control has been revisited during execution rather than left as an untouched placeholder;
- every listed control is marked `EXECUTED`.

## Fail-closed rule

A run must fail closed if:
- `RUN_EXECUTION_CONTROLS.md` is missing;
- the default baseline control was not seeded;
- a required execution control is not listed;
- any listed control remains `PENDING` at completion time.

## List of built-in execution controls

Built-in execution control names and governing files:

- `Identity display execution control`
  - `_hirmos/core/authority/core/identity-display-execution-control.md`

- `Hook execution control`
  - `_hirmos/core/authority/core/hook-execution-control.md`

- `Extension execution control`
  - governing file varies by resolved extension entrypoint and its governing authority.

## Operational rule

From this point onward, the LLM must treat `RUN_EXECUTION_CONTROLS.md` as mandatory for every command run and must not claim trustworthy completion until every listed control is `EXECUTED`.

## Bootstrap checkpoint

Before leaving Step 4, verify all of the following:

- `RUN_EXECUTION_CONTROLS.md` was created or refreshed.
- `RUN_EXECUTION_CONTROLS.md` was initialized for the active run.
- All required execution controls were added.
- Every governing file required by the listed execution controls was followed.
- The run failed closed if any listed execution control remained `PENDING`.

---

# Step 5 — Learn the Identity display execution control and valid terminal output

## Why this must be understood now

Step 4 established that every command begins with `Identity display execution control`. Satisfy this control before trustworthy completion is surfaced.

## Mandatory template

Use `_hirmos/core/templates/IDENTITY_DISPLAY_EXECUTION_CONTROL_TEMPLATE.md` as the template source for the canonical terminal wrapper shape used by this control.

## Control scope

`Identity display execution control` governs final chat-facing command output. When this control is listed in `RUN_EXECUTION_CONTROLS.md`, the LLM must return to `_hirmos/core/authority/core/identity-display-execution-control.md` and satisfy wrapper-rendering and wrapper-validation requirements before surfaced chat-facing output may be treated as trustworthy.

## Runtime identity declaration

Serious runnable extensions may declare `runtime.identity` in `extension.yaml` when a chat-facing runtime identity helps orientation.

Rules:
- `runtime.identity` declares the short human-readable identity value the Core may use when rendering extension-facing execution blocks;
- `runtime.identity` is optional;
- if present, the value should be stable, human-readable, and aligned with the extension's actual role;
- if absent, the extension still remains runnable, but the Core does not render an extension identity label.

The declared identity value is extension-owned manifest metadata. It is not an instruction for the extension to render its own final terminal identity wrapper.

## Canonical terminal wrapper

The Core owns the final terminal wrapper. The active producer owns the response body placed inside it.

The canonical rendered shape is:

```text
[Identity when applicable]

<Response body>
```

Rules:
- the identity line appears first when the active producer is Core or when the resolved extension declares `runtime.identity`;
- the response body follows after one blank line;
- the response body must not be missing;
- extensions do not own wrapper rendering or wrapper validation.

Allowed identity line behavior:
- `[HIRMOS]` for bootstrap, command dispatch, and genuinely framework-native/Core-native terminal output;
- the manifest-declared identity rendered in brackets, for example `[System Design Agent]`;
- omitted only when the active producer is an extension that does not declare `runtime.identity`.

## Wrapper validation requirements

When satisfying `Identity display execution control`, the Core must validate that:
- the canonical rendered shape is present;
- the identity line is correct for the active producer when applicable;
- the response body is present;
- wrapper and body ownership are coherent.

`Identity display execution control` must remain `PENDING` until wrapper construction and wrapper validation have both succeeded. It may be marked `EXECUTED` only after those requirements are complete.

A runnable command may emit short progress updates while work is in progress, but those updates are non-terminal and must not be treated as command completion. A runnable command is only valid when it ends with exactly one terminal run-state block.

## Operational rule

From this point onward, the LLM must treat final chat-facing output as an execution control, not as a formatting preference.

## Bootstrap checkpoint

Before leaving Step 5, verify all of the following:

- The identity display execution control was treated as mandatory.
- The Core-owned wrapper shape was followed.
- Wrapper construction and wrapper validation both succeeded before the control was marked `EXECUTED`.
- Final runnable output ended with exactly one terminal run-state block.

---

# Step 6 — Learn how runnable extension execution control is resolved under the outer lifecycle

## Why this must be understood now

Step 4 established that `cmd: run extension ...` must add `Extension execution control`. Resolve the runnable extension surface through this step before continuing execution.

## Extension location and manifest requirement

Every extension lives in:

```text
_hirmos/extensions/<extension-id>/
```

Every extension must contain:

```text
extension.yaml
```

## Mandatory run artifacts

`Extension execution control` does not use one Core-owned universal artifact template.
Instead, the resolved extension entrypoint may require extension-owned run artifacts.

When a resolved public entrypoint requires such artifacts, those artifacts are mandatory for trustworthy execution and completion. The LLM must treat extension-defined run artifacts as part of satisfying `Extension execution control`.

## Manifest goals

The manifest should be:
- easy for humans to read;
- easy to write by hand;
- easy for an LLM to inspect;
- structured enough for deterministic discovery;
- strong enough to support coherent runnable extensions and hook-based extensions.

## Canonical manifest shape

```yaml
id: hello-world
version: 1.0.0
requires_core: ">=1.0.0 <2.0.0"
types:
  - runnable
summary: Prints a hello world message.
entry: index.md
entrypoints: {}
requires: []
exposes_hooks: []
hooks: []
runtime: {}
```

## Required fields

### `id`
- required;
- unique extension identifier;
- allowed characters: lowercase letters, digits, hyphens;
- must match the extension folder name.

### `version`
- required;
- semantic version of the extension itself.

### `requires_core`
- required;
- semantic version range against `_hirmos/VERSION`.

### `types`
- required;
- allowed values: `runnable`, `hook`.

### `summary`
- required;
- short human-readable description.

## Key optional fields that affect runtime execution

### `entry`
- required for runnable extensions;
- defines the default public entrypoint.

### `entrypoints`
- optional map of named public entrypoints.

### `requires`
- optional list of required installed extension ids.

### `runtime.identity`
- optional short human-readable runtime identity label used by Core.

### `exposes_hooks`
- optional list of hook points exposed by this extension.

### `hooks`
- optional list of hook subscriptions declared by this extension.

## Validation rules the Core should enforce

The framework should validate:
- manifest exists;
- `id` matches the folder name;
- `version` is present and readable as semantic version text;
- `requires_core` is present;
- `types` is supported;
- `summary` exists;
- `entry` exists for runnable extensions;
- every `entrypoints` path exists;
- every exposed hook has required fields;
- exposed hook names are unique within the owning extension;
- every referenced hook subscription file exists;
- every hook subscription target matches a declared exposed hook;
- priority values are numeric when provided.

Additional handling rules:
- unknown top-level fields should be ignored with warning for now;
- `requires` values must be extension ids, not entrypoint references;
- hook extensions should omit `entry` unless a future contract explicitly needs it;
- `runtime.identity` is metadata, not wrapper ownership.

## Entrypoint resolution rule

When the command is `cmd: run extension <id>`, the Core resolves the manifest `entry` as the public default runnable entrypoint.

When the command is `cmd: run extension <id>:<entrypoint>`, the Core resolves the named file path from the manifest `entrypoints` map.

Once resolved, the runnable public entrypoint becomes the primary workflow instruction surface for local execution. For runnable public entrypoints, the Core must expect and use a minimal execution contract that includes:
- `Purpose`;
- `Produces`;
- `Terminal States`.

## Operational rule

From this point onward, the LLM must not treat arbitrary extension files as public runnable surfaces. Runnable extension execution control must resolve through the manifest first, then follow the resolved public entrypoint and any required extension-defined run artifacts.

## Bootstrap checkpoint

Before leaving Step 6, verify all of the following:

- Runnable extension execution control resolved through `extension.yaml`.
- The resolved public entrypoint became the primary local workflow instruction surface.
- The resolved public entrypoint exposed `Purpose`, `Produces`, and `Terminal States`.
- Any extension-defined mandatory run artifacts were treated as required for trustworthy execution and completion.

---

# Step 7 — Learn the Hook execution control for hook-aware runs

## Why this must be understood now

Step 4 established that hook-aware runs must add `Hook execution control`. Step 6 established how the owning runnable surface is resolved. Satisfy this control before trustworthy completion is surfaced.

## Mandatory run artifact

When a run is hook-aware, the Core must create and maintain `HOOK_EXECUTION_CONTROL.md`.

Use `_hirmos/core/templates/HOOK_EXECUTION_CONTROL_TEMPLATE.md` as the template source.
Create or refresh the run-scoped artifact at:

```text
_hirmos/artifacts/context/<extension-id>/<extension-entrypoint>/HOOK_EXECUTION_CONTROL.md
```

`HOOK_EXECUTION_CONTROL.md` is a Core-owned, run-scoped artifact for hook-aware runs. It records the relevant hook points, matched subscribers, execution order, status, and notes needed to validate hook execution before trustworthy completion is surfaced.

## Hook execution control scope

Hook System v1 supports Action Hooks only.

The Core owns:
- hook-point discovery from the resolved owning extension manifest;
- subscriber matching by exact target string;
- deterministic execution ordering;
- `HOOK_EXECUTION_CONTROL.md` creation and maintenance for hook-aware runs;
- hook-aware visibility and fail-closed completion behavior.

This hook model does not require semantic hook taxonomies, effect-lane doctrine, or extension-specific expectations.

## How hook points are resolved

For a resolved runnable entrypoint, the Core must:
1. load the owning extension manifest;
2. read the extension's declared `exposes_hooks` list;
3. keep only the hook points relevant to the active public entrypoint;
4. match installed hook subscribers whose `hooks.target` equals a declared hook-point name exactly.

## Matching and order rules

- matching is exact;
- the Core does not reinterpret similar hook names;
- subscriber order is deterministic;
- lower `priority` runs earlier;
- higher `priority` runs later;
- equal priority preserves registration order.

## Hook execution artifact shape

The canonical shape is:

```md
# Hook Execution Control

- Owning entrypoint:
- Run scope:
- Resolution source:
- Validation note:

This artifact is maintained by the Hook execution control for hook-aware runs.

Allowed `Status` values:
- `pending`
- `executed`
- `no-subscribers`
- `failed`

## Hook Point: <hook-point-id>
- Workflow location:
- Matched subscribers:
- Rejected matching subscribers:
- Execution order:
- Status:
- Notes:
```

## Subscriber-resolution consistency

If an installed extension manifest declares a hook subscription target that exactly matches a resolved hook point for the active run, `Matched subscribers` must not be `none` for that hook point unless the run records an explicit rejection reason for that installed matching subscriber.

Do not use `no-subscribers` to hide installed exact-match subscribers that were merely skipped, overlooked, or left unexplained.

## Visibility requirements

Hook execution must remain inspectable. At minimum, traces should make visible:
- exposed hooks considered for the active run;
- matching subscribers;
- final execution order;
- material effects, warnings, skips, or failures.

## Failure behavior

If a hook subscription cannot run cleanly, the Core should:
- record the problem in traces;
- surface it in chat-facing output when material;
- pause the active run if trustworthy continuation depends on that hook's contribution;
- otherwise continue with warning.

An incomplete hook execution artifact is a fail-closed condition for a hook-aware run. A hook-aware run must not claim trustworthy completion if the artifact is missing or incomplete. `Hook execution control` must not be marked `EXECUTED` unless `HOOK_EXECUTION_CONTROL.md` is present and complete for the run.

## Operational rule

From this point onward, the LLM must not handwave hooks. If the run is hook-aware, `HOOK_EXECUTION_CONTROL.md` and hook visibility are mandatory parts of trustworthy completion.

## Bootstrap checkpoint

Before leaving Step 7, verify all of the following:

- `HOOK_EXECUTION_CONTROL.md` was created or refreshed for the hook-aware run.
- Matching subscribers were resolved exactly against declared hook targets.
- Installed exact-match subscribers were either matched or explicitly rejected with recorded reasons.
- Deterministic execution order was preserved.
- Hook visibility was preserved through the execution artifact and traces.
- The hook-aware run failed closed if the hook execution artifact was missing or incomplete.

---

# Step 8 — Learn how the active stack is resolved

## Why this must be understood now

The stack system matters for execution, but it is not the first thing the bootstrap reader needs.
Read this only after command resolution, execution controls, and runnable extension surfaces are understood.

## Stack system role

The stack system is a project-level Core subsystem.

Its purpose is to let one project choose one active technical stack package, then expose that resolved stack context to any installed extension that needs stack-aware behavior.

The active stack is not owned by an individual extension.
It is project reality that may affect many stack consumers at once.

## Core-owned stack responsibilities

Core owns:
- stack selection and configuration;
- stack package discovery;
- stack package validation;
- active stack resolution;
- normalized stack context exposure to stack consumers.

Core does not own stack-specific content.
That content lives inside stack packages.

## Stack location

```text
_hirmos/STACK_CONFIG.json
_hirmos/stacks/<stack-id>/stack.yaml
_hirmos/stacks/<stack-id>/...
```

## Active stack resolution

The active stack is resolved from `_hirmos/STACK_CONFIG.json`.

The config must declare exactly one active stack id.

Core then:
1. reads `_hirmos/STACK_CONFIG.json`;
2. resolves `_hirmos/stacks/<stack-id>/stack.yaml`;
3. validates the required declared stack surfaces;
4. exposes the active stack context for stack consumers.

## Normalized stack context

Any stack-aware extension should treat the following as the canonical read path:
1. `_hirmos/STACK_CONFIG.json`
2. `_hirmos/stacks/<active-stack-id>/stack.yaml`
3. the stack surfaces declared by that manifest

Common stack surfaces include:
- `overview`
- `engineering_standards`
- `commands`
- `architecture_guidance`
- `execution_rules`

Not every consumer needs every surface.

## Validation rules

Core-level stack validation must ensure:
- `_hirmos/STACK_CONFIG.json` exists and is readable;
- exactly one active stack id is declared;
- the referenced stack directory exists;
- `stack.yaml` exists and is readable;
- all required declared surfaces resolve to readable files;
- the resolved package declares `kind: stack`.

If the stack config or package is invalid, the framework must report the issue clearly instead of guessing stack context.

## Operational rule

From this point onward, the LLM must not guess stack context.
It must use the Core-resolved active stack path.

## Bootstrap checkpoint

Before leaving Step 8, verify all of the following:

> The active stack is project-level Core state. It comes from `_hirmos/STACK_CONFIG.json` and the selected stack package, and must not be guessed.

---

# Step 9 — Learn the minimum framework navigation needed after bootstrap

## Why this section is intentionally small

This file is trying to reduce cognitive load, not recreate the full docs tree.
So the navigation guidance here is minimal and only supports post-bootstrap orientation.

## The minimum orientation rule

If you are new to HIRMOS, do **not** start by browsing everything in `_hirmos/`.
Start with the lightest path that gets you to a successful first run.

## What `_hirmos/` is

`_hirmos/` is the governed framework install surface inside a project.

## Useful top-level surfaces

- `_hirmos/core/` — minimal framework core and runtime behavior
- `_hirmos/core/authority/` — central authoritative doctrine lanes
- `_hirmos/extensions/` — installed extensions
- `_hirmos/docs/` — user-facing guidance and onboarding
- `_hirmos/inputs/` — raw extension-owned runtime inputs
- `_hirmos/artifacts/` — grouped project/runtime/generated artifact families
- `_hirmos/stacks/` — installed stack packages

## Root README orientation that matters here

The repository root README provides a high-level mental model:
- HIRMOS is modular;
- the Core provides the shared operating model and execution rules;
- extensions add specialized workflow intelligence;
- users do not need to understand the full internal repository structure to begin.

That is useful orientation, but it does not replace bootstrap.

## Operational rule

After bootstrap is complete, use the lightest path needed for the actual task.
Do not browse the whole framework by default.

## Bootstrap checkpoint

Before leaving Step 9, verify all of the following:

- The role of `_hirmos/` is understood.
- Bootstrap does not require broad browsing.
- After initialization, only the lightest path needed for the requested command will be used.

---

# Step 10 — Pass the embedded quiz-only gate and create the mandatory bootstrap completion report before claiming initialization is complete

## Why this step exists

Do not claim bootstrap completion based on partial reading, compliant-sounding language, or internal confidence.

Bootstrap readiness is close-fail and now depends on the embedded open-book, section-targeted, grounded quiz gate recorded in `_hirmos/artifacts/context/core/bootstrap-report.md`.

## Bootstrap close-fail rule

If the required completion report cannot be completed truthfully, do not claim bootstrap completion, do not claim command readiness, and do not soften the failure.

## Mandatory bootstrap report

Create or refresh `bootstrap-report.md`.

Use `_hirmos/core/templates/BOOTSTRAP_REPORT_TEMPLATE.md` as the template source.
Create or refresh the Core bootstrap artifact at:

```text
_hirmos/artifacts/context/core/bootstrap-report.md
```

`bootstrap-report.md` is the mandatory final verification artifact for bootstrap completion.
It is the only artifact allowed to authorize bootstrap completion and command readiness.

## Required report fields

Populate the report using these required fields:

- `BOOTSTRAP_STATUS`
- `QUIZ_GATE_MODE`
- `QUIZ_GATE_STATUS`
- `QUIZ_GATE_READY_FOR_BOOTSTRAP`
- `QUIZ_GATE_FAIL_CLOSED_REASON`
- `CORE_BOUNDARY_CONFIRMED`
- `COMMAND_SURFACE_CONFIRMED`
- `OUTER_EXECUTION_LIFECYCLE_CONFIRMED`
- `RUN_EXECUTION_CONTROLS_ARTIFACT_CONFIRMED`
- `IDENTITY_DISPLAY_EXECUTION_CONTROL_CONFIRMED`
- `RUNNABLE_EXTENSION_EXECUTION_CONTROL_CONFIRMED`
- `HOOK_EXECUTION_CONTROL_CONFIRMED`
- `STACK_RESOLUTION_CONFIRMED`
- `CUMULATIVE_WORKING_COPY_DISCIPLINE_CONFIRMED`
- `REREAD_UNDER_UNCERTAINTY_RULE_CONFIRMED`
- `FAIL_CLOSED_TRIGGERED`
- `NEXT_ALLOWED_STATE`

Allowed confirmation values:

- `YES`
- `NO`

Allowed `BOOTSTRAP_STATUS` values:

- `COMPLETE`
- `FAIL_CLOSED`

Allowed `QUIZ_GATE_STATUS` values:

- `PASS`
- `FAIL`

## Report completion rules

- `QUIZ_GATE_MODE` must be `quiz-only`.
- `BOOTSTRAP_STATUS` = `COMPLETE` only if the quiz gate passes and every required confirmation is satisfied; otherwise `FAIL_CLOSED`.
- `QUIZ_GATE_STATUS` = `PASS` only if the quiz demonstrates grounded, materially accurate understanding of the framework sections required for safe bootstrap completion; otherwise `FAIL`.
- `QUIZ_GATE_READY_FOR_BOOTSTRAP` = `YES` only if `QUIZ_GATE_STATUS` = `PASS`.
- `QUIZ_GATE_FAIL_CLOSED_REASON` must explain the material misunderstanding, ungrounded answer pattern, or reread-discipline failure when the quiz gate fails.
- `CORE_BOUNDARY_CONFIRMED` = `YES` only if Step 2 was completed truthfully.
- `COMMAND_SURFACE_CONFIRMED` = `YES` only if Step 3 was completed truthfully.
- `OUTER_EXECUTION_LIFECYCLE_CONFIRMED` = `YES` only if Step 4 was completed truthfully.
- `RUN_EXECUTION_CONTROLS_ARTIFACT_CONFIRMED` = `YES` only if `RUN_EXECUTION_CONTROLS.md` was created or refreshed, initialized, and treated as mandatory.
- `IDENTITY_DISPLAY_EXECUTION_CONTROL_CONFIRMED` = `YES` only if Step 5 was completed truthfully.
- `RUNNABLE_EXTENSION_EXECUTION_CONTROL_CONFIRMED` = `YES` only if Step 6 was completed truthfully.
- `HOOK_EXECUTION_CONTROL_CONFIRMED` = `YES` only if Step 7 was completed truthfully.
- `STACK_RESOLUTION_CONFIRMED` = `YES` only if Step 8 was completed truthfully.
- `CUMULATIVE_WORKING_COPY_DISCIPLINE_CONFIRMED` = `YES` only if Step 1A was completed truthfully.
- `REREAD_UNDER_UNCERTAINTY_RULE_CONFIRMED` = `YES` only if the runtime accepted and followed the locked reread rule during the quiz gate.
- `FAIL_CLOSED_TRIGGERED` = `YES` if any required verification item is incomplete, untrue, or missing, or if the quiz gate fails.
- `NEXT_ALLOWED_STATE` must state either `Wait for Orchestrator command.` or `Bootstrap failed closed. Do not begin substantive command execution.`

## Embedded quiz-only gate

### Quiz rule
- This is an open-book, section-targeted, grounded quiz gate.
- At the slightest uncertainty, do not answer from memory. You must re-read the relevant section before answering.
- Answers must be grounded in the actual framework files for this run.
- Generic best-practice answers are insufficient if they do not reflect the framework’s actual rules and distinctions.
- Repeated ungrounded answers, repeated reread-discipline failures, or any material misunderstanding of a critical governance area must fail the quiz gate.

### Part 1 — Source of truth and working-copy discipline

#### Q1
Read first: `HIRMOS_CORE.md` and `_hirmos/core/bootstrap.md`

What is the authoritative source of truth for the run, what is the active cumulative working copy, and what must happen before claiming a file was created, updated, verified, or already present?

#### Q2
Read first: `_hirmos/core/bootstrap.md`

What must happen if continuity of the active cumulative working copy becomes unclear during or after bootstrap?

### Part 2 — Command and output discipline

#### Q3
Read first: `_hirmos/core/bootstrap.md`

What does the `cmd:` prefix mean in HIRMOS, and what must happen if a `cmd:` input does not exactly match the supported Core command surface?

#### Q4
Read first: `_hirmos/core/authority/core/identity-display-execution-control.md`

What is the difference between framework-native surfaced output and extension-native surfaced output, and why is that distinction important for truthful execution reporting?

### Part 3 — Hook and runtime-input truth

#### Q5
Read first: `_hirmos/core/authority/core/hook-execution-control.md`

When is `Matched subscribers: none` valid, and when is it invalid if an installed extension manifest declares an exact matching hook target?

#### Q6
Read first: `_hirmos/core/authority/core/hook-execution-control.md`

What discovery evidence must a hook-aware run preserve before it may truthfully say a runtime-input pack was found, accepted, rejected, or absent?

### Part 4 — Execution controls, stacks, and fail-closed runtime discipline

#### Q7
Read first: `_hirmos/core/bootstrap.md`

What must happen before a runnable command may be treated as trustworthy under the outer execution lifecycle?

#### Q8
Read first: `_hirmos/core/bootstrap.md`

How is the active stack resolved, and why must stack context never be guessed from memory?

### Part 5 — Scenario gate

For each scenario, answer:
- `PASS` or `FAIL_CLOSED`
- one short explanation grounded in the framework

#### S1
Read first: `_hirmos/core/bootstrap.md`

The runtime skimmed bootstrap, answered from memory, and claims readiness.

#### S2
Read first: `_hirmos/core/authority/core/hook-execution-control.md`

An installed extension manifest declares an exact matching hook target, but the run records `Matched subscribers: none` and gives no rejection reason.

#### S3
Read first: `_hirmos/core/bootstrap.md`

The runtime claims readiness even though `bootstrap-report.md` is missing or incomplete.

#### S4
Read first: `_hirmos/core/authority/core/identity-display-execution-control.md`

A runnable command reaches the chat surface without the Core-owned wrapper and still claims trustworthy completion.

### Part 6 — Short synthesis

#### Q9
Read first: `_hirmos/core/bootstrap.md`, `_hirmos/core/authority/core/hook-execution-control.md`, and `_hirmos/core/authority/core/identity-display-execution-control.md`

In 200–400 words, explain why HIRMOS requires grounded validation instead of optimistic validation during bootstrap and early runtime. Your answer must include:
- reread-under-uncertainty discipline
- actual artifact-state proof
- hook truth
- surfaced-output truth
- fail-closed readiness

## Negative gate rule

Do not claim any of the following unless `bootstrap-report.md` exists, is complete, and truthfully authorizes readiness:

- bootstrap complete;
- initialized;
- ready;
- command-ready;
- any equivalent readiness claim.

## Bootstrap report verification

Before leaving Step 10, verify all of the following:

- `bootstrap-report.md` was created or refreshed at `_hirmos/artifacts/context/core/bootstrap-report.md`.
- Every required report field was populated.
- The embedded quiz-only gate was completed.
- `QUIZ_GATE_MODE` = `quiz-only`.
- `QUIZ_GATE_STATUS` was populated truthfully.
- `QUIZ_GATE_READY_FOR_BOOTSTRAP` = `YES` only if the quiz gate passed.
- `BOOTSTRAP_STATUS` = `FAIL_CLOSED` if any required confirmation is `NO` or if the quiz gate failed.
- `REREAD_UNDER_UNCERTAINTY_RULE_CONFIRMED` was populated truthfully.

---

# Step 11 — Surface bootstrap completion from the mandatory report

## Why this step exists

Do not improvise the final bootstrap output.
Surface a compact readiness summary derived from `bootstrap-report.md`.

## Required surfaced-output shape

Use `bootstrap-report.md` as the source for the final chat-facing bootstrap completion summary.
The surfaced summary must be compact and must include:

- bootstrap status;
- quiz gate status;
- next allowed state;
- report path: `_hirmos/artifacts/context/core/bootstrap-report.md`.

Do not dump the full report into the final chat-facing output unless the Orchestrator explicitly asks for it.

## Output gate rule

If `BOOTSTRAP_STATUS` is `FAIL_CLOSED`, the final chat-facing output must say bootstrap failed closed and must not claim readiness.
If `BOOTSTRAP_STATUS` is `COMPLETE`, the final chat-facing output may say bootstrap is complete and readiness is granted.

## Bootstrap checkpoint

Before leaving Step 11, verify all of the following:

- The final chat-facing bootstrap output was derived from `bootstrap-report.md`.
- The surfaced summary includes bootstrap status, quiz gate status, next allowed state, and the report path.
- No readiness claim was made unless `BOOTSTRAP_STATUS` is `COMPLETE`.
- A failed bootstrap was surfaced as failed closed rather than softened.

---

# Step 12 — Post-bootstrap behavior

## What happens after bootstrap

Once bootstrap is complete:
- wait for Orchestrator commands;
- follow the Core command protocol;
- use the manifest to resolve runnable surfaces;
- apply the run execution controls model for actual runs;
- keep stack resolution, hook behavior, and output validity inside their Core-owned boundaries.

## What does not happen after bootstrap

Bootstrap completion does **not** mean:
- the requested workflow has already run;
- the target extension has already been resolved;
- the active stack has already been consumed for a specific run;
- hooks have already been executed;
- a terminal run-state block has already been earned for a real command.

Those happen only when an actual command is resolved and executed.

## Operational rule

Bootstrap completion moves the system from uninitialized to ready for Orchestrator commands.
It does not skip or pre-satisfy runtime controls for future commands.

## Bootstrap checkpoint

Before leaving Step 12, verify all of the following:

- Bootstrap is complete only if `bootstrap-report.md` says `BOOTSTRAP_STATUS: COMPLETE`.
- The quiz gate passed only if `bootstrap-report.md` says `QUIZ_GATE_STATUS: PASS`.
- The next allowed state is to wait for an Orchestrator command.
- Bootstrap completion did not pre-satisfy runtime controls for future commands.

---

# Bootstrap sequence summary

Follow this sequence in order:

1. Stop real work and accept that bootstrap comes first.
2. Learn what Core owns and what it must not own.
3. Learn the exact command surface and stop inventing commands.
4. Learn the outer execution lifecycle before any command can be trusted.
5. Learn the Identity display execution control and valid terminal output.
6. Learn how runnable extension execution control is resolved under the outer lifecycle.
7. Learn the Hook execution control for hook-aware runs.
8. Learn how the active stack is resolved.
9. Learn only the minimum navigation needed after bootstrap.
10. Pass the embedded quiz-only gate and create the mandatory bootstrap completion report.
11. Surface bootstrap completion from the mandatory report.
12. Wait for real Orchestrator commands and execute them under Core governance.
