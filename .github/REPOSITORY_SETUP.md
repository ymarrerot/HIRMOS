# HIRMOS Public Repository Setup

This file is maintainer-facing repository setup guidance for the public GitHub repository.

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

## Required check

The public repository check runs directly from files present in the public repo. It does not depend on maintainer-only workspace scripts.

The minimum public check is:

```bash
python3 _hirmos/tools/validate.py
```

The GitHub Action runs that check on pull requests and pushes to `main`.
