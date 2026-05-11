# HIRMOS Public Repository Setup

This file is maintainer-facing. It is intentionally kept under `.github/` so the repository root stays clean.

## Day-1 repository settings

Recommended minimal settings for `main`:

- Require pull request before merging.
- Require 1 approval.
- Require status checks to pass after `Repository Check` appears in GitHub.
- Require conversation resolution.
- Block force pushes.
- Block branch deletion.
- Allow admin bypass for emergency maintainer fixes only.

Recommended merge settings:

- Enable squash merge.
- Disable merge commits at first.
- Enable automatic deletion of head branches.

Do not enable GitHub Discussions, Projects, or a formal roadmap until there is enough community volume to justify another maintainer inbox.

## Labels

After pushing this repository, configure the minimal label set with:

```bash
bash ops/scripts/setup-github-labels.sh ymarrerot/HIRMOS
```

This requires the GitHub CLI and an authenticated session.

## Required check

The public repository check is:

```bash
bash ops/scripts/verify-repo.sh
```

The GitHub Action runs the same check on pull requests and pushes to `main`.
