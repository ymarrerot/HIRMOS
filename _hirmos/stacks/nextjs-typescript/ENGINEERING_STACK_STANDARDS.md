# ENGINEERING STACK STANDARDS

## Purpose

These standards define engineering expectations for the `nextjs-typescript` stack package.

They complement framework-wide engineering standards with TypeScript and Next.js specific discipline.

## Standards

### 1. Preserve Type Safety

Prefer correct types over `any`, unsafe casts, or suppression-based shortcuts.

When a type compromise is unavoidable, it should be narrow and justified.

### 2. Respect Routing Structure

Preserve the project's routing model.

Do not casually mix conventions across:

- app router boundaries
- pages router boundaries
- API route structures

### 3. Keep Client and Server Concerns Clear

Do not blur client/server boundaries carelessly.

Where relevant, preserve the intended execution context of components, routes, and data access.

### 4. Prefer Minimal Dependency Change

Do not introduce new libraries when existing platform or repository utilities already solve the problem adequately.

### 5. Keep Buildability in Mind

Changes should be compatible with the repository's likely lint, typecheck, and build expectations.

Even if all checks cannot be run, changes should be designed to survive them.
