# Specs are not enough

Specs are necessary. They make the work clearer, reduce ambiguity, and give the agent a stronger target.

Spec-Driven Development is still an evolving practice, and different tools and teams implement it differently. HIRMOS uses the term in its broad methodological sense: specs guide planning, implementation, and validation.

Some SDD implementations already add governance mechanisms, but specs by themselves do not automatically provide enough execution governance.

A spec can say what should happen. It does not, by itself, prove that the workflow actually did it.

## What specs do well

Specs help define:

- what should be built;
- what constraints matter;
- what the system should accept or reject;
- what success should look like;
- what the implementation should satisfy.

That is why Spec-Driven Development is a strong foundation.

## Why orchestration is always required

Specs are not enough because serious software work needs more than a target. It needs a way to carry decisions, evidence, validation, and unresolved questions through the work without losing them.

That requirement is not new. Good engineering teams already use design reviews, architectural decision records, tests, and handoff notes because important decisions need to be visible across sessions, team members, and time.

AI-assisted development inherits that need. The work moves faster, more decisions are made inside short interactions, and the reasoning behind those decisions is not always easy to inspect later.

So Orchestrated SDD adds the workflow layer around the spec:

```text
Specs define the intended work.
Orchestration governs how the work proceeds.
Evidence shows whether completion can be trusted.
```

## Why current AI agents make it more urgent

The durable reason matters even as models improve. But today's pain is also real.

Specs alone do not guarantee that the agent will pause when a decision is unresolved.

Specs alone do not guarantee that assumptions and open questions will be recorded in a durable place.

Specs alone do not guarantee that inputs and outputs from different files, hooks, extensions, or artifacts will be reconciled before completion.

Specs alone do not guarantee that the agent will validate its own output against the workflow rules.

Those are common failure points in current AI-assisted work. HIRMOS addresses them without making the methodology depend on them forever.

## The practical problem

A user may write a Clear Spec like this:

> Identify all unresolved assumptions and open questions before implementation.

The spec requirement is clear.

But if the workflow has no durable unresolved-item inventory, no required surfaced output, and no validation step, the agent may mention some questions in prose, miss others from an attached file, fail to classify which ones block implementation, and still continue.

The failure is not unclear specs. The failure is missing orchestration: nothing in the workflow made the spec's intent provable before the next step began.

## What Orchestrated SDD adds

Orchestrated SDD adds structures that make the workflow prove what happened:

- durable artifacts;
- required surfaced outputs;
- project-level unresolved-decision tracking;
- self-validation;
- fail-closed behavior as a HIRMOS design principle;
- evidence-backed completion.

The goal is not to write longer specs.

The goal is to make AI-assisted work reviewable, traceable, and honest about uncertainty — while still keeping the user-facing workflow practical.
