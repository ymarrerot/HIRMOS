const test = require("node:test");
const assert = require("node:assert/strict");
const { compareSemver, buildUpdateNotice, formatUpdateNotice, normalizeSemver } = require("../dist/lib/update-notice.js");

test("normalizes v-prefixed semver strings", () => {
  assert.equal(normalizeSemver("v1.3.2"), "1.3.2");
});

test("compares semver strings", () => {
  assert.equal(compareSemver("1.3.2", "1.3.1"), 1);
  assert.equal(compareSemver("1.3.1", "1.3.1"), 0);
  assert.equal(compareSemver("1.3.0", "1.3.1"), -1);
});

test("builds a non-blocking update notice only when latest is newer", () => {
  assert.equal(
    buildUpdateNotice("1.3.1", "1.3.2"),
    "A newer HIRMOS CLI is available: 1.3.2.\nUpdate with: npm install -g hirmos@latest"
  );
  assert.equal(buildUpdateNotice("1.3.2", "1.3.2"), null);
  assert.equal(buildUpdateNotice("1.3.3", "1.3.2"), null);
});


test("formats update notice with optional terminal color", () => {
  assert.equal(formatUpdateNotice("Update available", false), "Update available");
  assert.equal(formatUpdateNotice("Update available", true), "\u001b[1m\u001b[33mUpdate available\u001b[0m");
});
