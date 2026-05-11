# Runtime Trace Rules

## Purpose

Define the Core-local expectations for runtime traces, visibility, and execution checkpoints.

## Trace Requirements

Every runnable workflow command should print a short trace before the extension output.

Recommended format for a named entrypoint run:

```text
[Core] command: hirmos requirements
[Core] owning extension: requirements-agent
[Core] target entrypoint: requirements
[Core] entry: entrypoints/requirements.md
[Core] active stack: generic
[Core] exposed hooks:
  - requirements-agent.requirements.before-input-discovery
  - requirements-agent.requirements.before-requirements-normalization
[Core] resolved hook subscriptions:
  - some-extension :: requirements-agent.requirements.before-requirements-normalization :: priority 10
[Core] executing active workflow
```

Recommended format for `hirmos explain <command>`:

```text
[Core] command: hirmos explain system-design:phase-design-cycle
[Core] owning extension: system-design-agent
[Core] target entrypoint: phase-design-cycle
[Core] entry: entrypoints/some-entrypoint.md
[Core] active stack: generic
[Core] matching hooks: 2
[Core] execution not started
```

## Visibility

Hook execution must remain inspectable.

At minimum, command-scoped traces should make visible:
- exposed hooks considered for the active run;
- matching subscribers;
- final execution order;
- material effects, warnings, skips, or failures.

## Decision Checkpoints

When a cycle encounters a real decision checkpoint, that checkpoint must remain visible in runtime reporting.

The Core must not present a run as cleanly completed when the resolved entrypoint or workflow actually paused for required human direction.

## Boundary note

This authority file defines Core-local trace and visibility rules.
It does not define extension-side writing style for human-facing documentation.


## Verified state vs intended work

Runtime trace content must distinguish verified working-copy state from intended next actions.

A trace must not present intended file creation, intended updates, or intended verification as already completed.

When the runtime has not yet verified the active cumulative working copy, the trace must say so explicitly.

If continuity becomes unclear during the run, traces must record that uncertainty instead of implying uninterrupted continuity.


## Runtime-input discovery trace rule

When trace output reports discovery or absence of runtime-input packs, it must reflect verified working-copy state.

If the run claims no active runtime packs were found, traces must make clear:
- what path was inspected
- whether any candidate directories were present
- why any discovered candidates were rejected

Intended shorthand must not replace verified discovery evidence.

## Anti-false-negative rule

A trace must not say “none found” when candidate runtime-pack directories are present but were simply not processed or not mentioned.
