# Paused Output Example

## Purpose

Show a minimal rendered example for `hirmos system-design` paused output without re-owning terminal identity behavior.

## Boundary note

The final identity wrapper is Core-rendered from the resolved manifest identity. This example separates the Core dispatch block from the extension-authored paused body shape.

## Example

```text
[Core]
[Core] command: hirmos system-design
[Core] resolved entrypoint: system-design

[System Design Agent]
Run state: paused

Major artifacts created or refined
- /_hirmos/artifacts/sot/SYSTEM_SOT.md
- /_hirmos/artifacts/sot/ARCHITECTURE_SOT.md
- /_hirmos/artifacts/sot/PHASES_SOT.md
- /_hirmos/artifacts/context/project/UNRESOLVED_ITEMS_INVENTORY.md
- /_hirmos/artifacts/context/system-design-agent/system-design/VALIDATION_TRACE.md

System Design state
- paused pending Orchestrator direction

Gated unresolved items
- <item>

Why they matter
- <reason>

Allowed outcomes
- <allowed outcome>

Proposed Orchestrator direction
- <advisory direction>

Continuation options
- Resolve the gated items and rerun `hirmos system-design`.

Summary
- This paused result preserves progress without claiming authoritative completion.
```
