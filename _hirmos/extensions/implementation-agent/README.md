# implementation-agent

The `implementation-agent` provides HIRMOS Implementation-stage capabilities.

Core owns lifecycle authority, command routing, interaction modes, execution controls, unresolved-item governance, and accepted-state update safety. This extension performs bounded Implementation work only when selected by Core routing and active execution controls.

## Shared method

Read `entrypoints/default.md` before running implementation-agent capabilities; it contains the shared Implementation method and routing authority.

## Supported lifecycle stage

- Implementation

## Capabilities

- `implementation-unit-planning`
- `implementation-execution`
- `implementation-unit-review`
- `validation-review`
- `retry-escalation`
- `session-implementation-review`

## Core rule

Implementation means governed realization of accepted Design. It includes implementation planning, project-file changes, validation, review, retry, and evidence. It does not redefine Design authority or update durable system state.
