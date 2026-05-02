# STACK OVERVIEW

## Purpose

The `generic` stack package is the fallback portability package for projects whose stack is:

- unclear
- mixed
- unusual
- still being discovered
- not yet modeled by a more specific stack package

This package exists so the framework can still operate in a governed way even when there is no mature stack-specific package available.

## Use This Package When

Use `generic` when any of the following is true:

- the project stack has not been identified with confidence
- the repository combines multiple technologies without one obvious primary stack
- the project is too custom or too early-stage for a more specific stack package
- a more specific stack package does not yet exist

## What This Package Covers

This package provides:

- minimal stack assumptions
- generic execution discipline
- generic command selection guidance
- generic verification expectations
- generic engineering conventions that are useful across many environments

## What This Package Does Not Do

This package does not:

- define language-specific architecture conventions
- assume a specific package manager, runtime, or framework
- override framework core governance
- replace project-specific SoT or prompt instructions

## Relationship to Framework Core

This package complements the framework core.

Precedence remains:

1. framework core governance
2. subsystem governance
3. selected stack package
4. project SoT and phase artifacts
5. task-specific prompt

The `generic` package should stay thin. It is a practical fallback, not a second framework.
