# Core Stack Subsystem

Use this page to understand how HIRMOS selects the active stack and how that choice affects stack-aware behavior across the framework. In practical SDLC terms, stack selection helps design, planning, and implementation workflows stay aligned with the project's technical environment.

Need the canonical Core-local rules? See [_hirmos/core/authority/core/stack-system.md](../../core/authority/core/stack-system.md).

## Canonical owner

Core is the canonical owner of stack resolution.

Core owns:
- stack selection config
- stack discovery and validation
- active stack resolution
- normalized stack context exposure

Core does not own stack-specific content.

## Stack package location

```text
_hirmos/STACK_CONFIG.json
_hirmos/stacks/<stack-id>/stack.yaml
```

## Required config shape

```json
{
  "spec_version": 1,
  "active_stack": "generic"
}
```

## Resolution rules

1. read `_hirmos/STACK_CONFIG.json`
2. resolve the selected stack id
3. load `_hirmos/stacks/<stack-id>/stack.yaml`
4. validate required surfaces
5. expose the resolved stack context to consumers

## Required stack surfaces

Every stack package must declare:
- `overview`
- `engineering_standards`
- `commands`

Optional but recommended surfaces:
- `architecture_guidance`
- `execution_rules`

## Surface intent

These surfaces are not decorative.
They provide the main project-level stack context that consumers may need for planning or execution.

Typical use:
- `overview` — scope, fit, and boundaries for the stack package
- `engineering_standards` — stack-specific engineering expectations
- `commands` — command families, verification guidance, and command-precedence rules
- `architecture_guidance` — stack constraints or patterns that can shape planning
- `execution_rules` — execution-time rules that downstream stack-aware agents may follow

## Consumer rule

A stack-aware extension should read:
1. `_hirmos/STACK_CONFIG.json`
2. the active stack's `stack.yaml`
3. the declared surfaces it needs

It should not invent its own ad hoc stack discovery path.
It should also not bypass the manifest by hardcoding direct stack file assumptions when the surface mapping is already declared in `stack.yaml`.