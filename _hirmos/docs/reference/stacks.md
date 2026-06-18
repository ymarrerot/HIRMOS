# Stacks

A stack is the technical environment HIRMOS uses to guide design, implementation, and evidence expectations.

Baseline installed stacks include:

- `generic`
- `nextjs-typescript`
- `python-backend`

## Stack selection rule

HIRMOS is single-stack by default and multi-stack aware only when evidence requires it.

Stack selection priority:

1. repository evidence;
2. accepted system state;
3. explicit request or run configuration preference;
4. prototype or POC evidence;
5. installed stack availability;
6. `generic` fallback.

Repository evidence overrides request preference when they conflict.

## Stack contexts

Most projects use one active stack. Complex systems may have optional stack contexts when repository evidence shows bounded areas with different stacks, such as a web app and a backend service.

HIRMOS should not activate multi-stack complexity unless evidence requires it.
