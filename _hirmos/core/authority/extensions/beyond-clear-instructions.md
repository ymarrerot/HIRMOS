# Beyond Clear Instructions

*Canonical extension doctrine for when clear instructions alone are not sufficient.*

## What this is

This is the authoritative framework pattern for situations where clear instructions alone are not reliable enough.

Use this authority file when deciding whether an extension should rely on instructions alone or should instead add stronger supporting controls around those instructions.

This doctrine has a baseline and an escalation path:
- baseline: clear instructions plus local self-validation whenever the run can honestly validate whether those instructions were followed;
- escalation: add governed intermediate synthesis structures, governed surfaced-output structures, and fail-closed behavior when the work is more synthesis-heavy or trust-sensitive.

## Problem this solves

Clear instructions alone often fail once an entrypoint must:
- collect information from multiple producers;
- combine contributions from multiple execution branches;
- summarize material from both the main entrypoint path and subscribed hooks; or
- surface a result whose omissions or overstatements would mislead the Orchestrator.

Instruction clarity remains mandatory, but for these cases it is not sufficient.

## When this applies

Apply the baseline form whenever a runnable entrypoint gives concrete instructions that can be checked locally before the result is surfaced.

Escalate to the fuller pattern when one or more of these conditions is true:
- the entrypoint summarizes material from multiple producers;
- the entrypoint combines the main execution path with hook contributions;
- the final result is decision-shaping or trust-sensitive;
- omissions would materially change operator decisions; or
- the run must pause, complete, or fail in a way that remains legible and honest.

## Required controls

### 1. Clear instructions

This is mandatory.

The runnable surface and, when needed, the deeper governing local spec or authority must make the required method legible enough for a reviewer or operator to follow.

### 2. Required intermediate templates for multi-source synthesis when applicable

Use these when the entrypoint must collect, normalize, or summarize information from multiple sources before producing a downstream result.

Typical triggers include:
- multiple producers;
- multiple artifact contributors;
- multiple execution branches;
- the main entrypoint path plus one or more subscribed hooks; or
- any run where omissions can occur between collection and final synthesis.

These templates should make it obvious whether every required source contributed, whether the intermediate record is complete, and whether the final synthesis still matches the collected inputs.

Do not add intermediate templates when the run does not actually perform multi-source synthesis.

### 3. Required templates for critical surfaced outputs when applicable

Use these when the final surfaced result needs a stable, governed shape.

Typical examples include:
- paused or completed cycle outputs;
- review reports;
- trust-sensitive summaries; or
- chat-facing outputs where missing sections or drift would mislead the Orchestrator.

Do not add surfaced-output templates when the output is tiny, illustrative, or not trust-sensitive.

### 4. Strict local self-validation at the end of the entrypoint

This is mandatory whenever a runnable entrypoint gives concrete instructions and can locally validate whether they were actually followed.

For heavier workflows, the self-validation step should also verify, at the appropriate level:
- required intermediate synthesis records are complete and not misleading;
- required final output templates were used when applicable;
- required sections are present; and
- the surfaced result does not overclaim completion or hide material gaps.

### 5. Fail closed on material defects

Fail closed when any of the following is true:
- a required intermediate synthesis template is incomplete or misleading;
- a required surfaced-output template is incomplete or misleading;
- strict local self-validation fails; or
- the entrypoint cannot truthfully preserve trust after detecting the defect.

Do not silently continue past a material synthesis or surfaced-output failure.

## When not to overapply it

Do not force the full escalated pattern onto:
- tiny illustrative demos with no real synthesis burden;
- narrow helper entrypoints with no meaningful trust boundary; or
- outputs whose shape is trivial and not trust-sensitive.

Even in those lighter cases, keep the baseline when the run can still self-check whether its clear instructions were followed.

## Output-only subset

A narrower output-only case exists when the main risk is only at the final surfaced-output boundary.

In that narrower case, the same doctrine still applies, but the output-facing subset may be enough:
- clear instructions;
- strict final self-validation before the result is surfaced; and
- required surfaced-output templates when applicable.

Do not treat this subset as a separate competing doctrine. Use it only when intermediate multi-source synthesis is not materially part of the risk.

## Review tests

When reviewing whether this pattern should apply, ask:
- Does the runnable entrypoint give concrete instructions that it can locally self-check?
- Does the run combine multiple producers, branches, or hook contributions?
- Could omissions or drift between collection and final synthesis materially mislead the Orchestrator?
- Does the final surfaced result need a stable governed shape?
- Can the entrypoint locally validate whether the synthesis and surfaced result are complete and honest?
- Should the run fail closed if those checks fail?

## Related doctrine

- [Extension entrypoints](./entrypoints.md)
- [Extension validation](./validation.md)
- [Extension document roles](./extension-document-roles.md)
