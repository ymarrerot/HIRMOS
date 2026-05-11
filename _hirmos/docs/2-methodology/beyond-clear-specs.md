# Beyond Clear Specs

Beyond Clear Specs is the reliability pattern behind Orchestrated Spec-Driven Development.

The pattern starts from a practical lesson:

```text
Clear Specs are necessary, but not sufficient.
```

In the SDD context, the same lesson becomes:

```text
Specs are necessary, but not enough.
```

A Clear Spec can tell an agent what should be built. The rest of the pattern makes the workflow preserve, surface, validate, and enforce whether it actually happened.

## Why this pattern exists

There are two reasons specs are not enough on their own.

The durable reason is that serious AI-assisted software development needs orchestration. The work should leave durable artifacts, surface important decisions in reviewable forms, validate before claiming completion, and stop honestly when the conditions for safe progress are not met.

The practical reason today is that AI agents can still skip context, make silent assumptions, miss unresolved decisions, overclaim completion, or hide weak validation. Those failures are real, and HIRMOS is designed to reduce them.

So Beyond Clear Specs is not just a workaround for today's models. It is a practical pattern for making AI-assisted work traceable, reviewable, and trustworthy as the work becomes faster, larger, and more consequential.

## The five pillars

Beyond Clear Specs introduces five pillars that work together.

### 1. Clear Specs

Clear Specs make the agent’s target explicit enough to guide work without relying on hidden assumptions.

A Clear Spec should define the goal, scope, constraints, acceptance expectations, and known open questions clearly enough that the agent does not have to silently guess. In HIRMOS, Clear Specs may appear as requirement artifacts, local specs, prompt-scoped requirements, entrypoint execution contracts, workflow rules, or artifact requirements. They may be structured, testable, executable, formal, or robust when the situation requires it, but clarity is the foundation.

Clear Specs are mandatory, but they are the first pillar, not the whole pattern.

### 2. Durable artifacts

Durable artifacts preserve important reasoning, inputs, decisions, and collected material before they are summarized or lost.

They prevent the workflow from jumping straight from many sources to a final answer without leaving a reviewable trail.

Examples include input packs, inventories, worklists, ledgers, traces, and normalized context artifacts.

The point is not to produce paperwork. The point is to keep the important project memory visible enough that later steps, future runs, and human reviewers can understand what the work relied on.

### 3. Required surfaced outputs

Required surfaced outputs force important results to appear in a stable, reviewable shape.

If a workflow must expose assumptions, unresolved decisions, validation results, terminal state, or next actions, those items should not remain hidden inside prose.

Required surfaced outputs make the workflow easier to review and harder to fake.

### 4. Self-validation

Self-validation makes the workflow check whether it followed its own rules before claiming completion.

The workflow should compare its actual work against the required inputs, artifacts, outputs, validation rules, and terminal-state conditions.

Self-validation does not make the agent perfect. It creates a disciplined review point before the workflow asks the user to trust the result.

### 5. Fail-closed behavior

Fail-closed behavior means the workflow must not claim success when required evidence, decisions, or validation are missing.

In Orchestrated SDD, fail-closed behavior is a HIRMOS design principle.

When the workflow cannot safely continue, it should pause, surface what is missing, and explain what decision or evidence is needed next.

When the workflow cannot complete honestly, it should say so.

## Governance backbone and execution discipline

The five pillars can be understood in two practical groups.

The governance backbone keeps the work reviewable and honest:

- Durable artifacts;
- Required surfaced outputs;
- Fail-closed behavior.

The execution-discipline pillars improve the quality of work before and during execution:

- Clear Specs;
- Self-validation.

Both groups remain important. The amount of scaffolding can scale with project risk, team needs, and model capability, but the underlying discipline does not disappear.

## Practical example

A user says:

> Build the onboarding flow from these notes. Ask before making assumptions.

A Clear Spec can capture the goal, constraints, and acceptance expectations.

But the workflow still needs more than the spec:

- Durable artifacts preserve the notes, assumptions, and unresolved questions.
- Required surfaced outputs show what the workflow understood and what still needs review.
- Self-validation checks whether the workflow actually asked or paused when required.
- Fail-closed behavior prevents the workflow from pretending implementation is ready when a blocking decision is still unresolved.

That is Beyond Clear Specs in practice.

## Why this matters for Orchestrated SDD

The point is not that specs are weak.

The point is that specs define the intended work, while orchestration governs how the work proceeds and evidence shows whether completion can be trusted.

That is why Orchestrated SDD uses more than Clear Specs. It uses a workflow that preserves context, surfaces decisions, validates progress, and fails closed when trust would otherwise be compromised.
