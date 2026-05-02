# Extension Lifecycle and Cycles

## Purpose

Define the framework-wide extension doctrine for lifecycle-shaped extension workflows and the role of cycles as governed high-level runs.

Use this authority file when deciding:
- when an extension should express a lifecycle through cycles
- what makes a cycle a healthy governed default
- how lifecycle-oriented public surfaces should relate to narrower entrypoints

## Role of cycles

A cycle is a high-level governed workflow entrypoint.

Cycles are appropriate when the extension needs a public surface that coordinates multiple meaningful steps while preserving trust surfaces, pause behavior, and coherent completion reporting.

A cycle is not merely a longer entrypoint. It is the governed default path when that default materially improves correctness, truthfulness, or usability.

## Relationship to lower-level entrypoints

A cycle may call or coordinate narrower lower-level entrypoints.

Those lower-level entrypoints should remain bounded and reusable rather than trying to compete with the cycle for the role of default governed path.

## Lifecycle fit

Use cycle-shaped public surfaces when the workflow naturally has:
- a meaningful beginning, middle, and end
- trust artifacts that must persist through the run
- pause conditions that materially matter
- completion criteria that should be surfaced honestly

Do not force cycle terminology onto trivial or purely illustrative workflows.

## Naming guidance

When a public workflow is genuinely a governed cycle, naming that helps the operator understand that role is usually healthy.

For broader naming doctrine, see:
- [Extension naming conventions](./naming-conventions.md)

## Relationship to entrypoint doctrine

This file defines when lifecycle-shaped public runs are healthy.

For broader public-surface doctrine, see:
- [Extension entrypoints](./entrypoints.md)

## Review tests

When reviewing cycle usage, ask:
- Is the cycle a real governed default rather than a renamed ordinary entrypoint?
- Does the lifecycle shape materially improve trust or usability?
- Are lower-level entrypoints kept bounded beneath the higher-level cycle where appropriate?
- Would a simpler public surface be healthier here?
