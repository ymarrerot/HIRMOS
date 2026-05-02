# STACK OVERVIEW

## Purpose

The `nextjs-typescript` stack package is for projects primarily built with:

- Next.js
- TypeScript
- modern JavaScript package tooling

It captures common expectations for a typed web application codebase while keeping framework-core governance separate.

## Use This Package When

Use `nextjs-typescript` when the project is primarily a Next.js + TypeScript application or monorepo centered on that stack.

Typical signals include:

- `package.json`
- `tsconfig.json`
- Next.js configuration files
- app or pages router structure
- React/TypeScript web application conventions

## What This Package Covers

This package provides:

- Next.js / TypeScript execution assumptions
- command guidance for common package-manager workflows
- TypeScript-specific engineering discipline
- common validation expectations for modern app repositories

## What This Package Does Not Do

This package does not:

- replace framework core governance
- define project-specific architecture for every Next.js app
- override repository-local conventions without justification

## Relationship to Framework Core

This package refines how the framework is applied to a Next.js + TypeScript project.

It should stay thin and focused on truly stack-specific behavior.
