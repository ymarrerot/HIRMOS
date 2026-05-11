# Requirements → System Design → Implementation

Orchestrated Spec-Driven Development uses a practical lifecycle:

```text
Requirements → System Design → Implementation
```

The lifecycle is simple on the surface and rigorous underneath.

Each step has a bounded job. Each step produces durable artifacts the next step can rely on. Each step can pause when continuing would reduce trust.

## Requirements

Requirements turns goals, notes, prompts, files, prototypes, screenshots, constraints, repository context, and user intent into structured requirements artifacts.

In HIRMOS, the regular-user command is:

```text
hirmos requirements
```

The Requirements step should clarify what is known, what is assumed, what remains unresolved, and what is safe to pass into System Design.

Good requirements are not just a summary of what the user said. They are the first durable accountability structure for the work that follows.

## System Design

System Design turns requirements into system-level design artifacts, architecture decisions, phase design, and implementation-ready planning context.

In HIRMOS, the regular-user command is:

```text
hirmos system-design
```

System Design should not silently invent decisions that remain unresolved. It should pause when gated decisions block safe phase design or implementation readiness.

A good System Design step does more than produce a design. It carries requirements forward, records the decisions behind the design, and makes the future implementation accountable to that context.

## Implementation

Implementation plans and executes bounded work based on the approved design context.

In HIRMOS, the regular-user command is:

```text
hirmos implementation
```

Implementation must respect the planning approval boundary established by System Design. It validates results against the workflow rules, repairs what can be repaired within its authorized scope, and completes with Evidence-backed Review.

This is where the trust boundary is most visible: bounded work, explicit validation, honest terminal states, and durable evidence of what was built, what passed, and what remains unresolved.

## Why Evidence-backed Review is part of Implementation, not a fourth step

Evidence-backed Review is part of Implementation because it answers whether the implemented work can be trusted.

It is not a separate phase. It is the discipline that prevents Implementation from claiming completion without producing evidence that completion means something.

A workflow that ends with “done” — without a reviewable record of what was checked, what passed, what failed, and what remains — has not completed in a meaningful HIRMOS sense. It has only stopped.

## Why the lifecycle matters

The point is not to add ceremony.

The point is to prevent the agent from jumping from a vague request to delivered code while losing requirements, hiding assumptions, skipping validation, or overclaiming completion.

The lifecycle keeps the work practical:

```text
understand the work → design the work → implement with evidence
```

That is what makes Requirements → System Design → Implementation a simple front door with orchestration underneath.
