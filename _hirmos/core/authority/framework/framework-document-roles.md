# Framework Document Roles

## Purpose

Define framework-level document role boundaries.

This file explains the roles of framework-facing document types once content has already been routed into the correct high-level folder.

It does **not** govern folder placement across the active top-level folders. For cross-folder routing, use [Cross-folder rules](../shared/cross-folder-rules.md). For the local rules of `/_hirmos/core/authority/framework/`, use [Folder rules](./folder-rules.md).

## Framework README role {#framework-readme-role}

A framework-level README is a landing page for humans.

It should:
- orient the reader quickly
- establish the main message
- help a first-time visitor understand what the framework is
- point to deeper guidance and doctrine when needed

It should not silently become the deepest doctrine home when a more specific authority file already exists.

### What a framework README should do well {#framework-readme-do-well}

A good framework README should:
- give a clean first impression
- help a reader choose the next useful path
- summarize the framework without trying to own every concept
- link to deeper authority when precision matters

### What a framework README should avoid {#framework-readme-avoid}

A framework README should avoid:
- re-owning doctrine already defined elsewhere
- becoming a dumping ground for every framework detail
- mixing deep procedural rules with first-contact orientation
- acting like a substitute for authority or docs

### Relationship to authority and docs

The README is the front door. Authority files own canonical doctrine. Docs files explain and teach. The README should help the reader reach the right lane quickly.

## Framework guidance docs

Framework guidance docs explain the framework to humans.

They should:
- teach
- summarize
- guide
- illustrate
- point to deeper authoritative doctrine
- provide standalone practical explanations when useful

They should not silently replace the canonical authority files.

## Framework authority files

Framework authority files own canonical framework-wide doctrine that is not purely Core-local and not specifically extension-authoring doctrine.

They should:
- define the exact rule or model
- be referenceable from docs, reviews, and internal guidance
- avoid unnecessary repetition with lighter user-facing docs

## Framework diagrams

Framework diagrams are explanatory surfaces.

They should make a model easier to grasp quickly.

They should not carry critical doctrine that exists nowhere else.

## Framework examples or walkthroughs

Examples and walkthroughs illustrate how the framework behaves in practice.

They are useful for:
- onboarding
- intuition
- showing how multiple framework concepts fit together

They should not override authority.

## Review tests

When reviewing framework document roles, ask:
- Does this file match the role it claims to play?
- Is doctrine owned in authority rather than silently shifted into a README or docs page?
- Does the framework README stay a landing page instead of becoming a doctrine dump?
- Do framework docs teach without trying to replace authority?
- Are examples and diagrams illustrative rather than hidden rule owners?
