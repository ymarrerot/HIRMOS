# Example Structure: solution-brief

`solution-brief` is a good example of a separate extension that consumes strong upstream planning outputs without taking ownership of upstream design regeneration.

## Why it can be separate

Its public purpose is distinct:

- gather the right planning artifacts
- apply its own local method
- produce a client-facing output artifact

## Good boundary

- verify that the minimum planning-artifact bar is met
- pause when the upstream set is too weak for a credible brief
- run its own Spec-backed method
- produce the client-facing output at the expected runtime path `/_hirmos/artifacts/outputs/solution-brief/solution_brief.md`

## Why this matters

This shows how a focused extension can depend on serious upstream artifacts without collapsing back into the major design extension.