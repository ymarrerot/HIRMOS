# Source-of-Truth Model

## Purpose

Define the authoritative framework-wide model for how HIRMOS separates different kinds of project memory and authority.

Use this authority file when you need the canonical framework answer for how working materials, authoritative truth, downstream contracts, and execution records differ.

## Scope and usage rule

This file owns the framework-wide source-of-truth model.

Use it when:
- deciding whether an artifact is authoritative or merely useful
- grounding review criteria about artifact placement and authority boundaries
- explaining how runtime surfaces relate without redefining their folder meanings
- writing user-facing guidance that summarizes the framework’s trust model

## The main artifact categories

### Inputs

Path pattern:
- `_hirmos/inputs/<extension-id>/...`

Inputs are useful raw materials supplied to an extension, but they are not automatically authoritative.

### Context

Path pattern:
- `_hirmos/artifacts/context/<extension-id>/...`

Context is normalized working state and runtime support material. It can be important without becoming source-of-truth.

### Source-of-truth

Path pattern:
- `_hirmos/artifacts/sot/`

Source-of-truth is approved project or design truth.

### Phase contracts

Path pattern:
- `_hirmos/artifacts/phases/`

Phase contracts are bounded downstream delivery contracts derived from higher-level authority.

### Prompts

Path pattern:
- `_hirmos/artifacts/prompts/`

Prompts are generated downstream execution instructions rather than project authority.

### Ops artifacts

Path pattern:
- `_hirmos/artifacts/ops/`

Ops artifacts record governed implementation-stage operational activity rather than design truth.

## Why the separation matters

Without this separation, frameworks drift into confusion such as:
- provisional notes being mistaken for approved truth
- execution artifacts being mistaken for design authority
- review artifacts being mistaken for project requirements
- raw inputs being treated as if they had already been normalized and approved

HIRMOS keeps these surfaces distinct so the framework can remain both flexible and trustworthy.

## The simplest rule to remember

A useful artifact is not automatically an authoritative artifact.

## Relationship to top-level folder definitions

This authority file explains how the categories relate conceptually.

For the authoritative meaning of each top-level framework surface, defer to:
- `framework/top-level-folder-definitions.md`

## Related authority and guidance

Related authority files:
- `framework/top-level-folder-definitions.md`
- `framework/framework-operating-model.md`
- `framework/framework-operating-model.md`

Related user-facing guidance may explain these contrasts in lighter language without replacing them.
