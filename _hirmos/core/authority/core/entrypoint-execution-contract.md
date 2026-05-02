# Entrypoint Execution Contract

## Purpose

Define the minimum public execution-facing contract that the Core expects every runnable public entrypoint to expose once the Core resolves that entrypoint for execution.

This authority file is Core-local because it governs what the Core looks for, interprets, and relies on at runtime when it loads a runnable public entrypoint.

## Scope

This contract applies to:
- the default public entrypoint declared by `entry`
- every named public entrypoint declared by `entrypoints`
- runnable extensions only

This contract does not apply to:
- private helper files
- hook files
- templates
- extension-local specs as primary runtime surfaces
- non-runnable extensions unless they also expose runnable public entrypoints

## Required execution section

Every runnable public entrypoint must include a dedicated `## Execution Contract` section near the top of the entry file.

That section must define exactly these three fields:
- `Purpose`
- `Produces`
- `Terminal States`

## Required fields

### Purpose

The Core interprets `Purpose` as the concise statement of what the resolved entrypoint is trying to do.

### Produces

The Core interprets `Produces` as the concise statement of the main visible result the resolved entrypoint is expected to produce or surface.

### Terminal States

The Core interprets `Terminal States` as the allowed honest run endings for that resolved entrypoint.

Each listed state must include the minimum honest condition for ending in that state.

Use only run states allowed by the [Run result contract](./identity-display-execution-control.md).

## Core interpretation rule

After the Core resolves a runnable public entrypoint, the loaded entry file remains the primary instruction source.

The entrypoint's `Execution Contract` section is the minimum execution-facing contract that the Orchestrator must use to interpret:
- what the entrypoint is trying to do
- what visible result counts as execution
- which terminal states are honest for this entrypoint

Local extension specs may add detail and stricter local rules, but they do not remove the requirement for the entrypoint itself to expose this minimal contract.

## Core validation expectations

A runnable public entrypoint fails this Core contract when any of the following is true:
- the required `## Execution Contract` section is missing
- one or more required fields are missing
- `Terminal States` uses a run state outside the [Run result contract](./identity-display-execution-control.md)
- the section is present but too incomplete for the Core to determine purpose, visible result, or honest terminal states

## Boundary note

This authority file defines what the Core requires and interprets at runtime.

It does not define extension-side best practices for writing strong execution contracts, tutorial examples for extension authors, or user-facing guidance for how to structure entrypoints in practice. Those concerns belong in framework-wide extension doctrine and user-facing Docs, not in Core-local authority files.
