# Hook System v1

Use this page to understand how hooks behave in practice: who declares hook points, who subscribes, and how ordering works during real extension composition. It is a user-facing guide to the behavior you will actually design around.

Need the canonical Core-local rules? See [_hirmos/core/authority/core/hook-execution-control.md](../../../core/authority/core/hook-execution-control.md).

## What v1 includes

- Action Hooks only
- hook points declared by the extension that owns the workflow
- hook subscriptions declared by other installed extensions
- WordPress-style priority ordering
- visible hook execution in traces and run reporting

## What v1 does not include

- Filter Hooks
- hidden value mutation
- a giant predefined global hook list

## Why this direction

A fixed global hook list tends to be either:
- too small to be useful;
- too broad and abstract;
- too central, forcing core to predict future extension seams.

V1 instead lets each extension expose the seams it actually needs.

## Mental model

- **Owning extension:** declares hook points through `exposes_hooks`
- **Subscriber extension:** attaches behavior through `hooks`
- **[Core]** validates, orders, and reports hook execution

## Priority model

The framework uses a WordPress-style priority model:
- lower numbers run earlier
- higher numbers run later
- default priority is `10`
- same-priority subscribers use deterministic tie-breakers

## Why Filters are deferred

Filters add more mutation power and more precedence complexity.

The framework cares about trust, traceability, and governance. Action Hooks are the safer first layer.

## Visibility rule

Hook behavior must stay visible.

If hooks materially changed the run, that should be inspectable in traces and visible in the run summary when relevant.