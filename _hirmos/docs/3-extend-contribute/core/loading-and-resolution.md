# Loading and Resolution

Use this page when you want the practical picture of how HIRMOS finds installed extensions, resolves the active stack, and locates runnable surfaces. This is the behavior behind normal framework use, not a full restatement of command doctrine.

Need the canonical command behavior? See [_hirmos/core/command-protocol.md](../../../core/command-protocol.md).

The core discovers extensions by reading:

```text
_hirmos/extensions/*/extension.yaml
```

The core resolves the active stack by reading:

```text
_hirmos/project.json
_hirmos/stacks/<stack-id>/stack.yaml
```

## Extension resolution sequence

1. locate the target extension manifest
2. validate the target extension
3. load installed extension manifests
4. collect hooks whose `target` matches the requested extension id
5. validate matching hook points and files
6. order matching hooks
7. load the target entry and hook files
8. build the run plan

## Stack resolution sequence

1. read `_hirmos/project.json`
2. resolve the selected stack id
3. load `_hirmos/stacks/<stack-id>/stack.yaml`
4. validate the required declared stack surfaces
5. expose the active stack context to stack-aware extensions

## Why manifests are authoritative

Filenames are useful for people, but the manifest is the authoritative framework contract.
That keeps discovery deterministic.