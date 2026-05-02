# STACK ARCHITECTURE GUIDANCE

## Purpose

This file gives architecture-facing guidance for the `generic` stack package.

## Guidance

- Preserve broad portability in architecture planning when the stack is uncertain.
- Avoid architecture decisions that assume one framework, runtime, or deployment model without evidence.
- Prefer modular boundaries and clean interfaces that survive later stack clarification.
- Record stack-sensitive architecture uncertainty explicitly instead of hiding it inside confident-looking SoT text.
