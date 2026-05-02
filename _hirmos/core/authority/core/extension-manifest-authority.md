# Extension Manifest Authority

Every extension lives in:

```text
_hirmos/extensions/<extension-id>/
```

Every extension must contain:

```text
extension.yaml
```

## Manifest goals

The manifest should be:
- easy for humans to read;
- easy to write by hand;
- easy for an LLM to inspect;
- structured enough for deterministic discovery;
- strong enough to support coherent runnable extensions and hook-based extension.

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
- required
- unique extension identifier
- allowed characters: lowercase letters, digits, hyphens
- must match the extension folder name

### `version`
- required
- semantic version of the extension itself
- independent from the framework version
- for the broader framework-wide versioning contract, see [Versioning contract — Extension versioning](../framework/versioning-contract.md#extension-versioning)

### `requires_core`
- required
- semantic version range against `_hirmos/VERSION`
- current contract uses a single compatibility field only
- example: `">=1.0.0 <2.0.0"`
- for the broader framework-wide compatibility and release-signal contract, see [Versioning contract — Extension versioning](../framework/versioning-contract.md#extension-versioning)

### `types`
- required
- allowed values:
  - `runnable`
  - `hook`

### `summary`
- required
- short human-readable description
- used by the Core as descriptive metadata

## Optional fields

### `types` coherence rules
- If `types` includes `runnable`, the manifest must expose a runnable entry surface through `entry` or `entrypoints`.
- If `types` includes `hook`, the manifest must declare one or more hook subscriptions under `hooks`.
- `exposes_hooks` does not by itself imply `hook`. Exposing hooks means the extension may be extended by others; `hook` means the extension is itself used through hook subscriptions.
- `types` is an additive capability classification, not a replacement for the structural manifest fields.

## `entry`
- required for `types:
  - runnable`
- not used for `types:
  - hook`
- relative path inside the extension folder
- defines the default public entrypoint

### `entrypoints`
- optional
- map of named public entrypoints
- keys are public entrypoint names
- values are relative paths inside the extension folder

### `requires`
- optional
- list of required installed extension ids
- extension-level only in the current contract

### `runtime`
- optional
- object describing runtime identity/presentation metadata for the active extension layer

#### `runtime.category`
- optional
- broad runtime classification

#### `runtime.identity`
- optional
- short human-readable runtime identity label used by the core when labeling chat-facing execution blocks

### `exposes_hooks`
- optional
- list of hook points exposed by this extension

Each exposed hook must declare:
- `name`
- `phase`
- `summary`

`entrypoint` is optional only when the hook belongs to the extension's default public entrypoint. Use it for named-entrypoint hooks.

Optional exposed-hook fields:
- `effects`
- `when`
- `required_context`

#### Exposed hook example

```yaml
id: design-workflow
version: 1.0.0
requires_core: ">=1.0.0 <2.0.0"
exposes_hooks:
  - name: design-workflow.system-design-cycle.before-requirements-normalization
    entrypoint: system-design-cycle
    phase: before-requirements-normalization
    summary: Runs before requirements intake normalization for system design.
    effects:
      - inspect-inputs
      - generate-derived-input-artifacts
      - enrich-runtime-context
```

### `hooks`
- optional
- list of hook subscriptions declared by this extension

Each hook subscription must declare:
- `target`
- `file`

Optional subscription fields:
- `priority`
- `when`

#### Hook subscription example

```yaml
id: prototype-normalizer
version: 1.0.0
requires_core: ">=1.0.0 <2.0.0"
hooks:
  - target: design-workflow.system-design-cycle.before-requirements-normalization
    file: hooks/system-design-cycle.before-requirements-normalization.md
    priority: 10
```

## Hook object rules

### Exposed hook fields

#### `name`
- full declared hook identifier
- must be unique within the owning extension
- is matched exactly by the Core when resolving subscriptions

#### `entrypoint`
- the owning extension entrypoint where this hook is exposed

#### `phase`
- short readable timing label for when the hook fires inside the owning workflow

#### `summary`
- short human-readable description of why the hook exists

#### `effects`
- optional list of intended bounded effects
- examples:
  - `inspect-inputs`
  - `generate-derived-input-artifacts`
  - `enrich-runtime-context`
  - `add-validation-findings`

### Hook subscription fields

#### `target`
- names the exposed hook point this extension can subscribe to when the owning extension is installed and the active run resolves that hook point
- does not by itself create a hard installation dependency; use `requires` only when another installed extension is truly required

#### `file`
- relative path to the markdown file containing the subscribed hook behavior

#### `priority`
- optional
- default is `10`
- lower numbers run earlier
- higher numbers run later

## Validation rules

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
- for hook-aware runs, every matched hook subscription target must match a declared exposed hook on an installed hook-owning extension;
- hook subscription targets whose owning extension is not installed are dormant optional integrations unless the owner is also listed in `requires`;
- priority values are numeric when provided.

Additional handling rules:
- unknown top-level fields should be ignored with warning for now;
- `requires` values must be extension ids, not entrypoint references;
- hook extensions should omit `entry` unless a future contract explicitly needs it;
- `runtime.identity`, when present, should be short and human-readable.

## Boundary note

This authority file defines the manifest contract as interpreted and validated by the Core.

It may include compact contract examples when they materially clarify shape or validation, but it does not own extension tutorial guidance, extension best practices, or user-facing authoring walkthroughs. Those concerns belong in framework-wide extension doctrine and user-facing Docs.

## Minimal runnable example

```yaml
id: hello-world
version: 1.0.0
requires_core: ">=1.0.0 <2.0.0"
types:
  - runnable
summary: Prints a hello world message.
entry: index.md
```

## Runnable extension with exposed hooks

```yaml
id: design-workflow
version: 1.0.0
requires_core: ">=1.0.0 <2.0.0"
types:
  - runnable
summary: Design workflows and design artifacts.
entry: entrypoints/system-design-cycle.md
entrypoints:
  system-design-cycle: entrypoints/system-design-cycle.md
  requirements-sot: entrypoints/requirements-sot.md
runtime:
  category: agent
  identity: System Design Agent
exposes_hooks:
  - name: design-workflow.system-design-cycle.before-requirements-normalization
    entrypoint: system-design-cycle
    phase: before-requirements-normalization
    summary: Runs before requirements intake normalization for system design.
```

## Hook-only example

```yaml
id: pretty-output
version: 1.0.0
requires_core: ">=1.0.0 <2.0.0"
types:
  - hook
summary: Adds pretty formatting behavior to hello-world.
hooks:
  - target: hello-world.after-main-output
    file: hooks/hello-world.after-main-output.md
    priority: 10
```
