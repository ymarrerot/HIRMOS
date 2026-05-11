# Extension Manifest

Use this page when you want a practical understanding of what `extension.yaml` is for and which fields matter first. The goal is to help authors read or write a manifest without turning this page into a field-by-field doctrine dump.

Need the canonical rules? See [Extension manifests](../../../core/authority/extensions/manifests.md), [Extension manifest authority](../../../core/authority/core/extension-manifest-authority.md), and [Versioning contract](../../../core/authority/framework/versioning-contract.md).

The manifest file is `extension.yaml`.

## Required fields

- `id`
- `version`
- `requires_core`
- `types`
- `summary`

## Common fields

- `entry`
- `entrypoints`
- `hirmos_commands`
- `requires`
- `exposes_hooks`
- `hooks`
- `runtime`

## Manifest-declared HIRMOS commands

The `hirmos_commands` field declares which agent-facing HIRMOS commands an extension exposes:

```yaml
id: system-design-agent
entry: entrypoints/system-design.md
entrypoints:
  system-design: entrypoints/system-design.md
  phase-design-cycle: entrypoints/phase-design-cycle.md
hirmos_commands:
  system-design:
    description: Run the System Design step.
    entrypoint: system-design
    visibility: public
    regular_user_safe: true
    arguments: Optional system design scope or constraints.
```

This makes the regular-user command:

```text
hirmos system-design
```

resolve to the public System Design entrypoint.

## Named entrypoints

The `entrypoints` map exposes named entrypoints for inspection and explicit runs after the command owner is resolved:

```text
hirmos <command>:<entrypoint>
```

Use named entrypoints for advanced/reusable workflows, not as the first regular-user path when a coherent default public entrypoint exists.

## Front-door extension example

The regular-user greenfield extensions use this pattern:

```text
requirements-agent      entrypoints/requirements.md
system-design-agent     entrypoints/system-design.md
implementation-agent    entrypoints/implementation.md
```

## Hook-related fields

- `exposes_hooks` declares the hook points this extension exposes.
- `hooks` declares subscriptions to hook points exposed by other extensions.

Hook declarations must match real hook files. They should remain traceable and should not silently no-op.

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

## Runtime identity

Serious runnable extensions may declare optional runtime identity metadata.

The manifest declares the identity value only. The Core owns runtime identity display behavior and formatting for chat-facing execution blocks.

## Per-extension defaults

The manifest `entry` field remains the extension-local default entrypoint. Public HIRMOS workflow commands are declared separately through `hirmos_commands`, which maps a command name to the entrypoint Core should run.
