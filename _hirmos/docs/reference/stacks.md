# Stacks

A stack is the project's selected technical environment.

Examples:
- generic fallback
- Next.js + TypeScript
- Python backend

In HIRMOS, the active stack is a project-level framework concern.

That means:
- core resolves the active stack
- stack packages provide stack-specific content through declared surfaces
- extensions consume the active stack when relevant

A stack is not an ordinary extension.
It is a first-class framework package selected once for the current working state.

## Why stacks matter

Different stacks can affect:
- engineering standards
- command selection and verification paths
- architecture constraints
- implementation-time expectations

This makes stack awareness useful for many consumers, not just one extension.

## How stack content is organized

Each stack package declares its own surfaces in `stack.yaml`.

Common surfaces include:
- `overview`
- `engineering_standards`
- `commands`
- `architecture_guidance`
- `execution_rules`

Consumers should rely on the declared surface mapping, not assume hardcoded file names outside the stack package contract.

## Where the active stack lives

```text
_hirmos/project.json
_hirmos/stacks/<stack-id>/stack.yaml
```

## Learn more

- `../core/stacks.md`
- `../getting-started/selecting-a-stack.md`
- `../extensions/stack-consumption.md`
