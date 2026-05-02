# STACK COMMANDS

## Purpose

This file defines preferred command patterns for the `nextjs-typescript` stack package.

Repository-defined scripts still take precedence over generic examples.

## Package Manager Detection

Prefer the package manager already indicated by the repository, such as:

- `pnpm-lock.yaml` → pnpm
- `yarn.lock` → yarn
- `package-lock.json` → npm

Do not introduce a different package manager casually.

## Common Command Categories

### Install

Prefer one of:

- `pnpm install`
- `yarn install`
- `npm install`

based on repository evidence.

### Lint

Prefer repository-defined scripts such as:

- `pnpm lint`
- `yarn lint`
- `npm run lint`

### Type Check

Prefer repository-defined scripts when present.

Common patterns may include:

- `pnpm typecheck`
- `yarn typecheck`
- `npm run typecheck`
- `tsc --noEmit`

Use direct TypeScript commands only when repository evidence supports them.

### Test

Prefer repository-defined scripts such as:

- `pnpm test`
- `yarn test`
- `npm test`

### Build

Prefer repository-defined scripts such as:

- `pnpm build`
- `yarn build`
- `npm run build`

### Run / Smoke Check

Use repository-defined dev or preview commands only when appropriate and safe.

## Important Rule

These are preferred command patterns, not permission to ignore repository scripts.

Repository-local commands always win.
