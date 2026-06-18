# Generic Stack Commands

Status: stack guidance.
Purpose: Use when no more specific installed stack can be selected safely or when evidence is insufficient.

Stack guidance is not repository authority. Repository evidence and accepted HIRMOS system state govern actual commands, structure, and constraints.

## Autonomous technical progress guidance

Use repository evidence first. When safe and in scope, HIRMOS should inspect scripts, env examples, migrations, seed commands, and validation commands before asking the user routine setup questions.

Allowed examples when authorized:

- inspect `package.json` scripts;
- identify the package manager from lockfiles;
- inspect `.env.example` or documented env variables;
- run non-destructive `npm run lint`, `npm run test`, `npm run build`, migration, seed, or smoke commands when available and authorized;
- record missing dependencies, missing env variables, runtime errors, and local service blockers as evidence instead of vague future work.

Do not use production secrets or destructive commands without explicit authority.

## Setup/smoke command guidance

Use stack-appropriate commands to gather local setup and smoke evidence when safe and in scope. Prefer non-destructive commands first. Record blocked commands and missing services rather than claiming success.
