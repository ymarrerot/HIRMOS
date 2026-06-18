# Contributing to HIRMOS

Thank you for helping improve HIRMOS.

HIRMOS currently uses a founder-maintainer governance model. The maintainer has final decision authority over Core architecture, bootstrap behavior, command protocol, extension contracts, public package boundaries, and release acceptance.

## What is welcome

- Documentation fixes and onboarding improvements
- Bug reports with clear reproduction steps
- Improvements to bundled framework documentation or examples
- Installation-flow issue reports
- Well-scoped proposals for framework or extension-contract changes

## What needs a proposal first

Open a proposal issue before submitting a pull request that changes:

- Core behavior
- bootstrap behavior
- command protocol
- execution-control governance
- extension manifest or entrypoint contracts
- public package boundaries
- release or installation behavior

## Repository boundary

This public repository contains the public HIRMOS framework payload, public documentation, issue templates, and repository metadata.

Maintainer-only workspace assets are intentionally kept outside this repository. Public-facing docs and PR instructions should only reference paths present in the public repository.

## Pull requests

Small docs fixes can go straight to a PR. For anything larger, open an issue first.

Before opening a PR, run the checks that are available in your local clone. At minimum, framework-content changes should pass:

```bash
python3 _hirmos/tools/validate.py
```

If a change affects generated integration behavior, also test `hirmos init` from the published CLI/package flow described in the README.

Be respectful and constructive. The maintainer may close issues or PRs that are abusive, off-topic, spammy, or inconsistent with HIRMOS project boundaries.
