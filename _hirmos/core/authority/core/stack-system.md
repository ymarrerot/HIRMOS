# Stack System

## Purpose

Define the authoritative Core-local stack system for HIRMOS.

Use this file when you need the canonical rule for how the Core resolves the active stack, what a valid stack package must declare, and how extensions should consume stack-owned surfaces.

## What the stack system is

The stack system lets a project declare one active stack package whose surfaces can be consumed by stack-aware extensions.

The Core resolves the active stack. Extensions consume it through canonical surfaces instead of inventing their own stack discovery behavior.

## Stack system rule

The active stack must be selected through the canonical stack config and must resolve to one valid stack package.

The stack package must declare the surfaces it exposes. Consumers should read only the surfaces they actually need.

## Active stack selection

The active stack is selected through `_hirmos/STACK_CONFIG.json`.

Current config shape:

```json
{
  "spec_version": 1,
  "active_stack": "generic"
}
```

Rules:
- exactly one `active_stack` must be declared
- the selected stack id must resolve to one valid stack package

## Stack package contract {#stack-package-contract}

A valid stack package must declare its own contract through `stack.yaml`.

That contract defines:
- the stack's identity
- the surfaces it exposes
- the semantics those surfaces are allowed to carry
- the conditions a consumer may rely on

## Required stack package fields {#required-stack-package-fields}

A valid `stack.yaml` must declare:
- a stable stack identifier
- basic package metadata required by the stack package contract
- the public stack surfaces the package exposes

If a required field is missing, the package should not be treated as a valid active stack.

## Package surface semantics

A stack package should expose only the surfaces it actually owns.

Those surfaces may include things like:
- engineering standards
- framework-specific implementation guidance
- stack-local docs
- stack-local templates or support artifacts

A stack package should not claim surfaces it does not own.

## Stack package validation {#stack-package-validation}

A stack package is valid only if:
- required fields are declared
- all declared surface paths exist and are readable
- surface paths stay within the owning stack package directory
- the package contract is internally coherent

## Consumer contract {#stack-consumer-contract}

Extensions should not invent ad hoc ways of discovering stack information.

A stack consumer should read:
1. `_hirmos/STACK_CONFIG.json`
2. the active stack's `stack.yaml`
3. the declared surfaces it needs

This keeps stack-aware behavior consistent across extensions.

## Assumption discipline

An extension should not hardcode assumptions when the stack manifest or Core-resolved stack surfaces already provide the authoritative mapping.

Read only the stack surfaces the extension actually needs.

## Duplication boundary

Do not duplicate stack-specific doctrine inside an extension when the stack package already provides the authoritative content.

An extension may summarize stack implications locally when that helps its users, but the authoritative stack-owned content should remain in stack surfaces.

## Review tests

When reviewing the stack system, ask:
- Is the active stack resolved through the canonical config path?
- Does the selected stack package satisfy the required package contract?
- Are declared stack surfaces valid and contained within the package?
- Do consumers read stack context through canonical surfaces?
- Does the system avoid duplicating stack-owned doctrine unnecessarily?
