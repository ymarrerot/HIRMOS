# Contributing to HIRMOS

Thank you for helping improve HIRMOS.

HIRMOS currently uses a founder-maintainer governance model. The maintainer has final decision authority over Core architecture, bootstrap behavior, command protocol, extension contracts, public package boundaries, and release acceptance.

## What is welcome

- Documentation fixes and onboarding improvements
- Bug reports with clear reproduction steps
- Improvements to the bundled example extensions
- Packaging or install-flow fixes
- Well-scoped proposals for framework or extension-contract changes

## What needs a proposal first

Open a proposal issue before submitting a pull request that changes:

- Core behavior
- bootstrap behavior
- command protocol
- hook behavior
- execution-control governance
- extension manifest or entrypoint contracts
- public package boundaries
- release or installation behavior

## Repository boundary

HIRMOS Core is intentionally small. Contributions that move extension-specific behavior into Core will usually be declined or redirected into an extension proposal.

This public repository is for the open Core, framework docs, starter templates, and bundled example extensions. Marketplace extensions and private owner tooling are not accepted into the public repository.

## Pull requests

Small docs fixes can go straight to a PR. For anything larger, open an issue first.

Before opening a PR, run the relevant checks. At minimum, repository changes should pass:

```bash
bash ops/scripts/verify-repo.sh
```

Be respectful and constructive. The maintainer may close issues or PRs that are abusive, off-topic, spammy, or inconsistent with HIRMOS project boundaries.
