# Extension Manifest

Use this page when you want a practical understanding of what `extension.yaml` is for and which fields matter first. The goal is to help authors read or write a manifest without turning this page into a field-by-field doctrine dump.

Need the canonical rules? See [Extension manifests](../../core/authority/extensions/manifests.md), [Extension manifest authority](../../core/authority/core/extension-manifest-authority.md), and [Versioning contract](../../core/authority/framework/versioning-contract.md).

The manifest file is `extension.yaml`.

## Required fields

- `id`
- `version`
- `requires_core`
- `types`
- `summary`

## Optional fields

- `entry`
- `entrypoints`
- `requires`
- `exposes_hooks`
- `hooks`
- `runtime`

## Hook-related fields

- `exposes_hooks` declares the hook points this extension exposes
- `hooks` declares subscriptions to hook points exposed by other extensions

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
