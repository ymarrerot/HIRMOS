# Creating Your First Extension

This guide is a step-by-step starting path for a first extension. The goal is to help you expose one small governed capability first, then grow it only when a real SDLC need makes that worthwhile.


## Smallest runnable extension

Create this folder:

```text
_hirmos/extensions/my-first-extension/
```

Add `extension.yaml`:

```yaml
id: my-first-extension
version: 1.0.0
requires_core: ">=1.0.0 <2.0.0"
types:
  - runnable
summary: Prints a simple message.
entry: index.md
```

Add `index.md`:

```md
# my-first-extension

## Execution Contract

### Purpose

Print a simple message so the extension can be run and verified easily.

### Produces

- a direct chat-facing output: `My first extension is running.`

### Terminal States

- `completed` — allowed only when the exact message has been produced.

Print this message exactly:

My first extension is running.
```

Optional but recommended:
- `README.md` for local extension documentation

Even for a first extension, use the [Beyond Clear Specs](beyond-clear-specs.md) when the runnable surface can self-check whether its clear specs were followed. As the extension becomes more serious, use the fuller pattern when synthesis or surfaced-output governance also matters.

## SDLC anchor

For a first extension, keep the scope very small. Think of it as adding one runnable capability that supports a recognizable kind of work. Later, when you know the real need, you can grow that into a cycle or a richer surface for a broader SDLC stage.

## Adding a named public entrypoint

Richer extensions may expose named public entrypoints:

```yaml
id: richer-extension
version: 1.0.0
requires_core: ">=1.0.0 <2.0.0"
types:
  - runnable
summary: Demonstrates named entrypoints.
entry: index.md
entrypoints:
  hello: entrypoints/hello.md
```

Not every internal file should be public.

## Optional runtime identity

Serious runnable extensions may declare optional runtime identity metadata:

```yaml
runtime:
  category: agent
  identity: Example Agent
```

This only declares the extension's runtime identity value. The Core handles whether and how that identity is shown during execution.

## Need the deeper rules later?

Use these only when you need the exact contract details:
- [Extension document roles](../../../core/authority/extensions/extension-document-roles.md)
- [Extension README role](../../../core/authority/extensions/extension-document-roles.md#extension-readme-role)
- [Extension entrypoints](../../../core/authority/extensions/entrypoints.md)
- [Extension manifests](../../../core/authority/extensions/manifests.md)
- [Extension manifest authority](../../../core/authority/core/extension-manifest-authority.md)
- [Entrypoint execution contract](../../../core/authority/core/entrypoint-execution-contract.md)
