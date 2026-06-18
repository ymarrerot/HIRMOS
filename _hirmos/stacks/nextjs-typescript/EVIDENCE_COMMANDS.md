# Next.js TypeScript Evidence Commands

Status: stack guidance.
Purpose: Guidance for Next.js projects using TypeScript and common React app structure.

Stack guidance is not repository authority. Repository evidence and accepted HIRMOS system state govern actual commands, structure, and constraints.

## Autonomous progress evidence guidance

When HIRMOS attempts safe local technical progress, evidence must record:

- command or inspection performed;
- working directory;
- relevant environment posture without exposing secrets;
- result and raw/log evidence location when available;
- whether the result proves build/test success, local runtime readiness, user-environment verification, or production readiness.

Use canonical evidence states from `support/claim-reconciliation.md`.

## Local setup and role-workflow smoke evidence

When this stack is active, record local setup evidence before claiming local runtime readiness.

Minimum evidence categories:

- dependency install command and result when run;
- environment file / secret handling with redaction notes;
- database or service reachability when relevant;
- migration and seed command result when relevant;
- dev server start/result and route response when relevant;
- role workflow smoke checks for material implemented routes.

Firm rule: a passing build is not a substitute for local setup or role workflow smoke evidence.

## Next.js TypeScript setup/smoke examples

Examples of evidence to record when safe and applicable:

- `npm install` / package-manager equivalent;
- `npm run lint`;
- `npm run test` when available;
- `npm run build`;
- database migration command such as `npx prisma migrate dev`, `prisma db push`, or stack-specific equivalent when authorized;
- seed command when present;
- `npm run dev` and route response checks;
- login, patient, staff, provider, manager/admin route smoke observations.

Do not run destructive resets against unknown data without explicit approval.
