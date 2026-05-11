const test = require('node:test');
const assert = require('node:assert/strict');
const { buildReleaseDownloadUrl, normalizeReleaseVersion } = require('../dist/lib/source-install');

test('normalizes release versions for GitHub tags', () => {
  assert.equal(normalizeReleaseVersion('latest'), 'latest');
  assert.equal(normalizeReleaseVersion('1.3.1'), 'v1.3.1');
  assert.equal(normalizeReleaseVersion('v1.3.1'), 'v1.3.1');
});

test('builds official latest and versioned release asset URLs', () => {
  assert.equal(
    buildReleaseDownloadUrl('latest'),
    'https://github.com/ymarrerot/HIRMOS/releases/latest/download/hirmos-framework.zip'
  );
  assert.equal(
    buildReleaseDownloadUrl('1.3.1'),
    'https://github.com/ymarrerot/HIRMOS/releases/download/v1.3.1/hirmos-framework.zip'
  );
});

test('supports release base URL override for tests and mirrors', () => {
  const previous = process.env.HIRMOS_CLI_RELEASE_BASE_URL;
  process.env.HIRMOS_CLI_RELEASE_BASE_URL = 'https://example.test/releases/';
  try {
    assert.equal(
      buildReleaseDownloadUrl('1.3.1'),
      'https://example.test/releases/v1.3.1/hirmos-framework.zip'
    );
  } finally {
    if (previous === undefined) delete process.env.HIRMOS_CLI_RELEASE_BASE_URL;
    else process.env.HIRMOS_CLI_RELEASE_BASE_URL = previous;
  }
});
