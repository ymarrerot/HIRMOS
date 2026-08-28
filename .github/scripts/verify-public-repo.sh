#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT="${1:-$(cd "$SCRIPT_DIR/../.." && pwd)}"
cd "$ROOT"

fail() {
  echo "ERROR: $*" >&2
  exit 1
}

require_path() {
  local p="$1"
  [ -e "$p" ] || fail "required path missing: $p"
}

for p in \
  README.md \
  LICENSE \
  .github \
  .github/scripts/verify-public-repo.sh \
  _hirmos \
  _hirmos/AGENTS.md \
  _hirmos/README.md \
  _hirmos/hirmos.config.json \
  _hirmos/CHANGELOG.md \
  _hirmos/UPGRADE_GUIDE.md \
  _hirmos/core \
  _hirmos/docs \
  _hirmos/extensions \
  _hirmos/integrations \
  _hirmos/inputs \
  _hirmos/inputs/README.md \
  _hirmos/inputs/uploads/README.md \
  _hirmos/tools/validate.py; do
  require_path "$p"
done

for p in \
  playbook.md \
  _internal \
  ops \
  tools \
  AGENTS.md \
  HIRMOS_ORCHESTRATOR.md \
  CHANGELOG.md \
  UPGRADE_GUIDE.md; do
  [ ! -e "$p" ] || fail "local-only or obsolete public repo path present: $p"
done

python3 -m json.tool _hirmos/hirmos.config.json >/dev/null
python3 _hirmos/tools/validate.py >/dev/null

# Public-facing markdown should not point users at local maintainer workspace paths.
if grep -RInE '(^|[^[:alnum:]_])(playbook\.md|_internal/|ops/|tools/cli)([^[:alnum:]_]|$)' \
  README.md .github _hirmos/docs _hirmos/integrations/agent-tools \
  --include='*.md' --include='*.yml' --include='*.yaml' >/tmp/hirmos-public-local-paths.txt 2>/dev/null; then
  cat /tmp/hirmos-public-local-paths.txt >&2
  fail "public-facing docs reference local maintainer workspace paths"
fi
rm -f /tmp/hirmos-public-local-paths.txt

# Public documentation must use released behavior names rather than maintainer project-plan identifiers.
# Runtime authority/validator diagnostics may retain internal provenance, but READMEs and docs may not.
: >/tmp/hirmos-public-internal-identifiers.txt
grep -RInE 'PROD-L[0-9]+([.][[:alnum:].-]+)?|(^|[^[:alnum:]_])L[0-9]+[.][0-9]+' \
  _hirmos/docs --include='*.md' >>/tmp/hirmos-public-internal-identifiers.txt 2>/dev/null || true
grep -RInE 'PROD-L[0-9]+([.][[:alnum:].-]+)?|(^|[^[:alnum:]_])L[0-9]+[.][0-9]+' \
  _hirmos --include='README.md' >>/tmp/hirmos-public-internal-identifiers.txt 2>/dev/null || true
grep -nE 'PROD-L[0-9]+([.][[:alnum:].-]+)?|(^|[^[:alnum:]_])L[0-9]+[.][0-9]+' \
  README.md _hirmos/CHANGELOG.md _hirmos/UPGRADE_GUIDE.md >>/tmp/hirmos-public-internal-identifiers.txt 2>/dev/null || true
if [ -s /tmp/hirmos-public-internal-identifiers.txt ]; then
  cat /tmp/hirmos-public-internal-identifiers.txt >&2
  fail "public documentation contains maintainer project-plan identifiers"
fi
rm -f /tmp/hirmos-public-internal-identifiers.txt

echo "PASS: public repository surface is ready"
