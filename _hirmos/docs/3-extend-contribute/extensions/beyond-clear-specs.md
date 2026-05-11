# Applying Beyond Clear Specs in extensions

This page explains how extension authors apply the methodology-level Beyond Clear Specs pattern inside HIRMOS extensions.

For the general methodology explanation, read:

- [Beyond Clear Specs](../../2-methodology/beyond-clear-specs.md)

## Separation of concerns

Methodology explains the pattern.

Extension docs explain how extension authors implement the pattern safely.

This page does not repeat the full methodology. It focuses on what extension authors must do when designing entrypoints, specs, hooks, templates, validation, and terminal outputs.

## The five pillars in extension authoring

### 1. Clear Specs

A runnable extension surface must provide Clear Specs for the work it owns. In extension authoring, that means the target is explicit enough that the agent does not have to silently guess. A spec may be structured, testable, executable, formal, or robust when the extension requires it, but clarity is the foundation.

At minimum, a runnable extension surface must clearly state:

- its purpose;
- what it produces;
- its allowed terminal states;
- the artifacts it reads or writes;
- the conditions that require pause or failure.

For public runnable entrypoints, keep the entrypoint surface clear and navigational. Put deeper behavior in the governing spec.

### 2. Durable artifacts

Use durable artifacts when an extension gathers material from multiple sources before producing a result. These artifacts preserve important inputs, reasoning, decisions, traces, and collected material so the final output is not the first place where combined truth appears.

Examples include:

- input packs;
- normalized context artifacts;
- unresolved-item inventories, feeds, worklists, and ledgers;
- traces and validation records;
- producer-specific SOT artifacts.

Do not let a final summary be the first place where combined truth appears. Serious extensions should leave a reviewable trail of what was gathered, considered, validated, and carried forward.

### 3. Required surfaced outputs

Use required surfaced-output templates when the output is trust-sensitive.

A paused or completed run should not rely on improvised prose when the Orchestrator needs stable sections to make a decision.

A good surfaced output makes clear:

- what happened;
- what was produced;
- what remains unresolved;
- why the terminal state is honest;
- what should happen next.

### 4. Self-validation

If an extension can check its own work before surfacing it, it should.

Self-validation should check whether:

- required artifacts exist;
- required sections are present;
- unresolved items were contributed when relevant;
- outputs match the collected inputs;
- terminal state claims are supported by evidence.

### 5. Fail-closed behavior

If continuing would produce a misleading success, the extension must pause or fail honestly.

Do not let an extension claim completed when required evidence, unresolved decisions, validation, or terminal-output sections are missing.

## Entrypoints

Entrypoints should expose a clear runnable surface.

For public runnable entrypoints, include the minimal execution contract described by the framework:

- Purpose
- Produces
- Terminal States

Entrypoints should not become large behavioral specs. They should point to the governing spec for deep mechanics.

## Specs

Specs own the deeper behavior of serious extension workflows.

A spec should define:

- required inputs;
- required artifacts;
- producer obligations;
- hook-aware behavior when applicable;
- validation requirements;
- terminal-state rules;
- fail-closed conditions.

Specs should preserve the five-pillar pattern without duplicating Core authority.

## Hooks

Hooks may enrich, normalize, validate, or contribute to an active lifecycle stage.

A hook should not become a parallel producer unless that is explicitly its job.

When a hook contributes unresolved items, it should reuse, trigger, refresh, or validate the relevant producer-owned contribution path rather than inventing a second unresolved-item model.

## Templates

Templates are how extensions make important outputs stable and reviewable.

Use templates for:

- durable collection artifacts;
- surfaced terminal output;
- validation reports;
- paused/completed/failed states;
- evidence summaries;
- unresolved-item contribution structures.

A template should make omissions visible.

## Unresolved items

If an extension produces canonical artifacts that include assumptions or open questions, the producer must update its producer/artifact-scoped section in the project-level unresolved-item inventory before leaving the producer workflow.

Canonical project-level unresolved inventory:

```text
_hirmos/artifacts/context/project/UNRESOLVED_ITEMS_INVENTORY.md
```

Do not rely on a later summarization pass to collect unresolved items. Inline contribution is part of the reliability pattern.

## Extension author checklist

Before shipping or modifying a serious extension, check:

- [ ] Does the runnable surface have clear specs?
- [ ] Are durable artifacts used when collection and synthesis are separate?
- [ ] Are important outputs surfaced through required templates?
- [ ] Does the workflow self-validate before claiming completion?
- [ ] Does it pause or fail closed when trust would be lost?
- [ ] Are unresolved items contributed inline when required?
- [ ] Does the extension avoid duplicating Core or methodology authority?

## Related docs

- [Beyond Clear Specs methodology](../../2-methodology/beyond-clear-specs.md)
- [Spec-backed entrypoints](spec-backed-entrypoints.md)
- [Public entrypoints](public-entrypoints.md)
- [Hooks authoring](hooks-authoring.md)
- [Validation rules](validation-rules.md)
