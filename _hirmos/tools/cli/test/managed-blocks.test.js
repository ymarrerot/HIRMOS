const test = require('node:test');
const assert = require('node:assert/strict');
const { updateManagedBlock } = require('../dist/lib/managed-blocks');

const markers = { start: '<!-- HIRMOS:START -->', end: '<!-- HIRMOS:END -->' };
const template = '<!-- HIRMOS:START -->\n## HIRMOS\n<!-- HIRMOS:END -->\n';

test('creates full file when target is missing', () => {
  assert.equal(updateManagedBlock(null, template, markers, 'AGENTS.md'), template);
});

test('appends managed block to existing file without block', () => {
  const result = updateManagedBlock('# Existing\n', template, markers, 'AGENTS.md');
  assert.match(result, /^# Existing\n\n<!-- HIRMOS:START -->/);
});

test('replaces only existing managed block', () => {
  const existing = 'before\n<!-- HIRMOS:START -->\nold\n<!-- HIRMOS:END -->\nafter\n';
  const result = updateManagedBlock(existing, template, markers, 'AGENTS.md');
  assert.equal(result, 'before\n<!-- HIRMOS:START -->\n## HIRMOS\n<!-- HIRMOS:END -->\nafter\n');
});

test('fails on duplicate managed blocks', () => {
  const existing = `${template}\n${template}`;
  assert.throws(() => updateManagedBlock(existing, template, markers, 'AGENTS.md'), /multiple HIRMOS managed blocks/);
});
