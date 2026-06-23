# Next.js TypeScript Engineering Stack Standards

Status: stack guidance.
Purpose: define production-shaped engineering standards for Next.js projects using TypeScript and common React app structure.

Stack guidance is not repository authority. Repository evidence and accepted HIRMOS system state govern actual commands, structure, and constraints. When repository evidence is absent or incomplete, these standards define the HIRMOS default posture for Next.js TypeScript work.

## Core posture

Next.js TypeScript work should be production-shaped by default. Demo-only, fixture-only, local-only, or throwaway implementation is allowed only when explicitly authorized by the Session Scope and preserved at close.

Production-shaped does not require deployment, cloud services, or enterprise architecture in every session. It requires that local implementation choices preserve the architecture shape needed for production where practical.

## Persistence and database

- Durable business data should use durable persistence from the start.
- If the production recommendation is PostgreSQL, local development should prefer local PostgreSQL over SQLite unless SQLite is explicitly authorized as a local/demo limitation.
- In-memory stores, JSON files, browser storage, or temporary fixtures are acceptable only for prototypes, tests, or explicitly scoped demo behavior.
- Schema changes should be represented through the repository's migration/tooling path when available.
- Data access should go through a bounded repository/service layer when the app has material business behavior.

## Long-running work and background processing

- AI/provider calls, image/video generation, imports, exports, email/SMS bursts, billing operations, and other long-running work should not be hidden inside synchronous request/response paths.
- Prefer a persisted job model with statuses, retry/error state, ownership/account linkage, and a worker/cron/queue execution path appropriate to project size.
- A simple local worker, cron route, or polling-compatible job processor is acceptable for an MVP if it preserves the production architecture shape and limitations are explicit.
- Claim/lock or idempotency behavior is required when multiple workers or repeated invocations can process the same job.

## Metered state, usage, billing, quotas, and account balances

- Metered-state, billing, inventory, and account-balance mutations must be transactional, idempotent, or explicitly concurrency-limited.
- Preflight checks alone are not sufficient when multiple requests can pass before deduction/reservation.
- Prefer reservation/finalization or atomic decrement patterns when long-running work consumes usage allowances.
- Failed, retried, and partially completed jobs must have defined metered-state semantics.

## Provider boundaries and external services

- External providers should be behind small service/adapter boundaries.
- Provider mode must be explicit: mock, fixture, local real, sandbox, or production provider.
- Environment validation should fail clearly when required provider configuration is missing.
- Provider-generated artifacts and errors should be captured enough for user-visible status and debugging without leaking secrets.

## File upload, storage, and generated assets

- Validate uploaded file type, size, and path handling.
- Do not trust user-controlled filenames for storage paths.
- Store generated/runtime assets outside tracked source unless repository design intentionally includes fixtures.
- Handoff/release packages must exclude secrets, generated runtime uploads, generated images, database files, caches, and OS metadata unless explicitly attached as evidence.

## Authentication and authorization

- Protected data and account-scoped workflows require authorization checks on server-side operations.
- Auth configuration should be environment-driven and fail clearly when required secrets/configuration are missing.
- Do not rely only on client-side hiding for protected actions.

## Environment and configuration hygiene

- Provide `.env.example` when environment variables are required.
- Do not include `.env`, `.env.local`, secrets, tokens, generated databases, or user runtime data in release/handoff packages.
- Ensure `.gitignore` preserves `.env.example` while ignoring real environment files.

## Evidence expectations

For material Next.js work, evidence should include the strongest available repository-backed checks, such as:

- install/build/typecheck/lint commands;
- unit/integration tests where present or added;
- smoke evidence for critical user flows;
- database migration/schema validation when persistence changed;
- provider-boundary/mock/sandbox/production posture evidence when integrations changed;
- packaging/handoff hygiene checks when files are prepared for sharing or release.
