# Evidence-backed Review

Evidence-backed Review is how Orchestrated SDD prevents implementation from ending with an unsupported “done.”

In serious software development, completion should be demonstrated with evidence, not declared by confidence or tone.

Evidence-backed Review means the workflow explains what changed, what was checked, what passed or failed, what remains unresolved, and why the terminal state is honest.

## What it answers

Evidence-backed Review answers questions such as:

- What work was completed?
- What artifacts or files changed?
- What checks ran?
- What passed?
- What failed?
- What was repaired?
- What remains unresolved?
- Is the run completed, paused, or failed?
- What should happen next?

## Why it matters

A reliable workflow should not ask the user to trust tone. It should leave evidence.

This is a permanent completion discipline: if work is important enough to rely on, the result should be reviewable.

It is also a practical answer to a current AI pain point. An agent can sound confident while validation is weak, incomplete, or skipped. Evidence-backed Review makes the workflow show its work before asking the user to trust completion.

## Terminal states

Orchestrated SDD uses honest terminal states.

### Completed

The workflow completed the required work and produced evidence supporting completion.

### Paused

The workflow stopped because it needs input, a decision, approval, or a missing prerequisite.

Paused is not failure. It is the workflow holding its line instead of inventing an answer or hiding uncertainty.

### Failed

The workflow could not complete the required work or could not produce enough evidence to support completion.

Failed is also an honest terminal state. It is better than false success.

## What makes review evidence-backed

A review is evidence-backed when it connects the completion claim to concrete support, such as:

- changed files or artifacts;
- completed phase target;
- validation commands or checks;
- unresolved decisions;
- repair attempts;
- remaining risks;
- final terminal state.

## Why this is not a fourth lifecycle step

The public lifecycle is still:

```text
Requirements → System Design → Implementation
```

Evidence-backed Review is part of Implementation because it answers whether implemented work can be trusted.

Implementation is not complete merely because the agent stopped editing files. It completes when the workflow can honestly show what happened and why the terminal state is valid.
