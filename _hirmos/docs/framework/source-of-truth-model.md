# Source-of-Truth Model

Use this page when you want the practical contrast between inputs, context, source-of-truth, phase contracts, prompts, and ops artifacts. This is especially helpful during requirements, design, and planning work, where people often need to distinguish raw materials from approved project truth.


## Quick contrast

HIRMOS keeps different kinds of project memory separate on purpose.

At a glance:
- inputs are useful raw materials
- context is normalized working state
- source-of-truth is approved truth
- phase contracts are bounded downstream delivery contracts
- prompts are execution instructions
- ops artifacts are implementation-stage operational runtime records

## Simplest rule to remember

A useful artifact is not automatically an authoritative artifact.

## Why this helps during real SDLC work

This separation matters most when a project is moving from one stage to another. For example:
- raw requirements notes should not be treated as approved design truth
- working design context should not be treated as final implementation direction
- generated prompts should not replace the stronger artifacts they were derived from

That separation keeps later stages from inheriting accidental or unreviewed decisions as if they were already approved.

## Need the canonical model later?

Use this page for the practical distinction first. When you need the exact framework-wide rule, see the [source-of-truth model authority](../../core/authority/framework/source-of-truth-model.md).
