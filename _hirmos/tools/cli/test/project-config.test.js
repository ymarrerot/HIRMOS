const test = require('node:test');
const assert = require('node:assert/strict');
const { mergeProjectConfig } = require('../dist/lib/project-config');

const registry = {
  integrations: {
    agents: {},
    claude: {},
    cursor: {},
    copilot: {}
  }
};

test('creates integrations.installed and preserves config fields', () => {
  const config = { schema_version: 1, stack: { active_stack: 'generic' }, custom: true };
  const result = mergeProjectConfig(config, ['agents'], registry);
  assert.deepEqual(result.config.integrations.installed, ['agents']);
  assert.deepEqual(result.config.stack, { active_stack: 'generic' });
  assert.equal(result.config.custom, true);
  assert.equal(result.wasFirstInitialization, true);
});

test('appends selected integrations without removing existing ones', () => {
  const config = { integrations: { installed: ['agents'] } };
  const result = mergeProjectConfig(config, ['claude', 'cursor'], registry);
  assert.deepEqual(result.config.integrations.installed, ['agents', 'claude', 'cursor']);
  assert.deepEqual(result.added, ['claude', 'cursor']);
  assert.deepEqual(result.alreadyInstalled, []);
});

test('preserves unknown existing integration ids after known ids', () => {
  const config = { integrations: { installed: ['custom-agent', 'cursor'] } };
  const result = mergeProjectConfig(config, ['agents'], registry);
  assert.deepEqual(result.config.integrations.installed, ['agents', 'cursor', 'custom-agent']);
});
