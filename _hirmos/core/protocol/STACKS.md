# Stacks Protocol

Status: core protocol.
Purpose: define evidence-backed stack selection, stack package use, and lightweight multi-stack awareness.

## Core rule

```text
HIRMOS is single-stack by default and multi-stack aware by evidence.
```

Project-wide `active_stack` is the normal path. Stack contexts are optional and activate only when repository evidence, accepted system state, or explicit configuration shows multiple bounded stack areas.


## Production-shaped stack use

Stack packages are not passive suggestions. When a selected stack has engineering standards, HIRMOS must use them to preserve production-shaped implementation unless repository evidence or the Session Scope authorizes a weaker local/demo shape.

Stack standards should influence Design, implementation-unit planning, validation requirements, and close review for material architecture decisions. If the stack standard says a risk area is material, HIRMOS must either satisfy it, mark it not applicable with rationale, or record an authorized limitation/blocker.

## Stack selection priority

1. Repository evidence.
2. Accepted HIRMOS system state.
3. Explicit User Request or run configuration preference.
4. Prototype / POC evidence.
5. Installed stack package availability.
6. `generic` fallback.

Repository evidence overrides request preference. Stack packages guide; repositories govern actual usable commands.

## Installed baseline stacks

Baseline stack packages:

```text
generic
nextjs-typescript
python-backend
```

Additional stack packages may be added later without changing lifecycle authority.

## Stack package surfaces

Each installed stack package should expose:

```text
stack.json
STACK_OVERVIEW.md
ENGINEERING_STACK_STANDARDS.md
STACK_COMMANDS.md
STACK_ARCHITECTURE_GUIDANCE.md
EXECUTION_STACK_RULES.md
EVIDENCE_COMMANDS.md
```

Stack packages are guidance. They are not repository authority.

## Evidence command priority

When claiming validation/evidence, command selection follows:

1. repository-documented commands;
2. repository-defined scripts/task runner commands;
3. stack package evidence command guidance;
4. ecosystem defaults only when strongly supported by repository evidence;
5. `NOT_RUN`, `NOT_APPLICABLE`, or `BLOCKED` with rationale.

HIRMOS must not invent commands because a stack package lists common defaults.

## Stack resolution

When stack controls are active, create or update:

```text
_hirmos/session/stack-resolution.json
```

The stack resolution must record:

- active stack;
- selection source;
- confidence;
- evidence;
- stack package path;
- missing stack surfaces;
- conflicts;
- decision;
- notes.

## Stack contexts

A stack context is a bounded part of the system with its own stack evidence, root path, guidance, commands, and implementation constraints.

Stack contexts are optional.

Activate stack contexts only when evidence shows multiple bounded areas, such as:

- monorepo packages/apps/services;
- multiple package/runtime roots;
- multiple build/test systems;
- service folders with different language/runtime evidence;
- accepted system state already recording multiple contexts;
- explicit User Request involving multiple bounded system areas.

Do not activate stack contexts just because multiple languages appear incidentally.

## Stack context record shape

When active, record stack contexts in System State, Session Scope, Implementation Unit artifacts, and Evidence Review as needed:

```text
context_id
root_path
stack_id
selection_evidence
confidence
in_scope_status
commands_or_evidence_notes
conflicts_or_unknowns
```

Allowed in-scope statuses:

```text
IN_SCOPE
OUT_OF_SCOPE
IMPACTED_NOT_AUTHORIZED
UNKNOWN
```

## Multi-stack implementation rule

When stack contexts exist, each Implementation Unit artifact must name exactly one primary stack context unless a cross-stack unit is explicitly justified.

Cross-stack units must explain:

- why they cannot be split;
- all involved contexts;
- validation evidence required per context;
- preservation risks.

## Interaction-mode visibility

By default, show simple stack/project-type rationale and only material implications. Surface stack evidence, context boundaries, commands, conflicts, implementation implications, full stack-resolution, and context-routing records when requested or when risk, blocker state, validation failure, or inspection need requires it.

## Failure and route-back conditions

Block or route back when:

- configured stack package is missing;
- required stack surfaces are missing;
- stack selection conflicts with repository evidence;
- stack context boundary is uncertain and affects scope or evidence;
- Implementation claims validation without stack/repository-backed commands;
- a cross-stack change is hidden inside a single-context implementation unit.
