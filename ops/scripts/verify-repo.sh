#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"

fail() {
  echo "ERROR: $*" >&2
  exit 1
}

note() {
  echo "[verify-repo] $*"
}

require_path() {
  local p="$1"
  [ -e "$p" ] || fail "required path missing: $p"
}

for p in \
  README.md \
  LICENSE \
  .github \
  ops \
  _hirmos \
  _hirmos/HIRMOS_CORE.md \
  _hirmos/HIRMOS_ORCHESTRATOR.md \
  _hirmos/LICENSE \
  _hirmos/CHANGELOG.md \
  _hirmos/UPGRADE_GUIDE.md \
  _hirmos/VERSION \
  _hirmos/core \
  _hirmos/docs \
  _hirmos/extensions/README.md \
  _hirmos/extensions/_templates \
  _hirmos/extensions/hello-world \
  _hirmos/extensions/pretty-output \
  _hirmos/extensions/requirements-agent \
  _hirmos/extensions/system-design-agent \
  _hirmos/extensions/implementation-agent; do
  require_path "$p"
done

for p in \
  HIRMOS_CORE.md \
  HIRMOS_ORCHESTRATOR.md \
  CHANGELOG.md \
  UPGRADE_GUIDE.md; do
  [ ! -e "$p" ] || fail "obsolete root framework file present: $p"
done

for p in \
  _hirmos/extensions/hirmos-architect \
  _hirmos/extensions/presentation-design \
  _hirmos/extensions/prototype-ingestion \
  _hirmos/extensions/solution-brief; do
  [ ! -e "$p" ] || fail "private/marketplace extension must not be in public Core: $p"
done

if grep -RIn --exclude-dir=.git --exclude-dir=node_modules --exclude-dir=ops 'https://hirmos\.dev/product/' . >/tmp/hirmos-stale-urls.$$; then
  cat /tmp/hirmos-stale-urls.$$
  rm -f /tmp/hirmos-stale-urls.$$
  fail "stale hirmos.dev /product/ URLs found; use /marketplace/ URLs"
fi
rm -f /tmp/hirmos-stale-urls.$$


if grep -RIn --exclude-dir=.git --exclude-dir=node_modules --exclude-dir=ops 'Read and follow the instructions in HIRMOS_CORE\.md\|Read and follow the instructions on HIRMOS_CORE\.md' . >/tmp/hirmos-root-bootstrap.$$; then
  cat /tmp/hirmos-root-bootstrap.$$
  rm -f /tmp/hirmos-root-bootstrap.$$
  fail "stale root HIRMOS_CORE.md bootstrap prompt found"
fi
rm -f /tmp/hirmos-root-bootstrap.$$

if find _hirmos/artifacts -type f \( -name 'bootstrap-report.md' -o -name 'RUN_EXECUTION_CONTROLS.md' \) | grep -q .; then
  find _hirmos/artifacts -type f \( -name 'bootstrap-report.md' -o -name 'RUN_EXECUTION_CONTROLS.md' \)
  fail "runtime execution artifacts found in public Core"
fi

if find _hirmos/inputs -mindepth 2 -type f ! -name 'README.md' ! -name '.gitkeep' | grep -q .; then
  find _hirmos/inputs -mindepth 2 -type f ! -name 'README.md' ! -name '.gitkeep'
  fail "extension-populated runtime inputs found in public Core"
fi

python3 - <<'PY'
from pathlib import Path
from urllib.parse import unquote
import re
import sys

root = Path.cwd()
patterns = [Path('README.md')]
patterns.extend(Path('_hirmos/docs').rglob('*.md'))
patterns.extend(Path('_hirmos/extensions').glob('*/README.md'))
patterns.extend([Path('_hirmos/HIRMOS_CORE.md'), Path('_hirmos/HIRMOS_ORCHESTRATOR.md')])

link_re = re.compile(r'(?<!\!)\[[^\]]*\]\(([^)]+)\)')
broken = []
for path in sorted(set(p for p in patterns if p.exists())):
    text = path.read_text(encoding='utf-8', errors='replace')
    for match in link_re.finditer(text):
        raw = match.group(1).strip()
        if not raw or raw.startswith(('#', 'http://', 'https://', 'mailto:')):
            continue
        target = raw.split('#', 1)[0].strip()
        if not target:
            continue
        target = unquote(target)
        resolved = (path.parent / target).resolve()
        try:
            resolved.relative_to(root.resolve())
        except ValueError:
            broken.append((str(path), raw, 'target escapes repository'))
            continue
        if not resolved.exists():
            broken.append((str(path), raw, 'target does not exist'))

if broken:
    for source, raw, reason in broken:
        print(f'{source}: broken link {raw!r} ({reason})')
    sys.exit(1)
PY

note "public Core checks passed"
