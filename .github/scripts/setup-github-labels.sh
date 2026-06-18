#!/usr/bin/env bash
set -euo pipefail

if ! command -v gh >/dev/null 2>&1; then
  echo "ERROR: GitHub CLI 'gh' is required. Install it and run 'gh auth login' first." >&2
  exit 1
fi

repo="${1:-}"

gh_label_list() {
  if [ -n "$repo" ]; then
    gh label list --repo "$repo" "$@"
  else
    gh label list "$@"
  fi
}

gh_label_edit() {
  local name="$1"
  shift
  if [ -n "$repo" ]; then
    gh label edit "$name" --repo "$repo" "$@"
  else
    gh label edit "$name" "$@"
  fi
}

gh_label_create() {
  local name="$1"
  shift
  if [ -n "$repo" ]; then
    gh label create "$name" --repo "$repo" "$@"
  else
    gh label create "$name" "$@"
  fi
}

upsert_label() {
  local name="$1"
  local color="$2"
  local description="$3"
  if gh_label_list --search "$name" --json name --jq '.[].name' | grep -Fxq "$name"; then
    gh_label_edit "$name" --color "$color" --description "$description"
  else
    gh_label_create "$name" --color "$color" --description "$description"
  fi
}

upsert_label "type: bug" "d73a4a" "Something is broken or behaves incorrectly."
upsert_label "type: docs" "0075ca" "Documentation, onboarding, or wording improvement."
upsert_label "type: proposal" "a371f7" "Framework, contract, packaging, or design proposal."
upsert_label "type: packaging" "5319e7" "Packaging, release, installer, or distribution workflow."
upsert_label "status: needs-info" "fbca04" "More information is required before review can continue."
upsert_label "status: accepted" "0e8a16" "Accepted by the maintainer."
upsert_label "status: declined" "6e7781" "Declined or not aligned with current project boundaries."
upsert_label "good first issue" "7057ff" "Suitable for a first external contribution."

echo "HIRMOS GitHub labels are configured."
