import { fail } from "./errors";

export interface ManagedBlockMarkers {
  start: string;
  end: string;
}

function countOccurrences(content: string, needle: string): number {
  if (!needle) return 0;
  let count = 0;
  let index = 0;
  while (true) {
    const found = content.indexOf(needle, index);
    if (found === -1) return count;
    count += 1;
    index = found + needle.length;
  }
}

export function validateTemplateManagedBlock(template: string, markers: ManagedBlockMarkers, label: string): void {
  const starts = countOccurrences(template, markers.start);
  const ends = countOccurrences(template, markers.end);
  if (starts !== 1 || ends !== 1) {
    fail(`Template ${label} must contain exactly one complete HIRMOS managed block.`);
  }
  if (template.indexOf(markers.start) > template.indexOf(markers.end)) {
    fail(`Template ${label} has malformed HIRMOS managed block markers.`);
  }
}

export function updateManagedBlock(existing: string | null, renderedTemplate: string, markers: ManagedBlockMarkers, targetLabel: string): string {
  validateTemplateManagedBlock(renderedTemplate, markers, targetLabel);

  if (existing === null) {
    return ensureTrailingNewline(renderedTemplate);
  }

  const starts = countOccurrences(existing, markers.start);
  const ends = countOccurrences(existing, markers.end);

  if (starts !== ends) {
    fail(`Target ${targetLabel} has malformed HIRMOS managed block markers.`);
  }
  if (starts > 1) {
    fail(`Target ${targetLabel} contains multiple HIRMOS managed blocks. Refusing to modify it.`);
  }

  if (starts === 1) {
    const startIndex = existing.indexOf(markers.start);
    const endIndex = existing.indexOf(markers.end, startIndex);
    if (endIndex === -1 || startIndex > endIndex) {
      fail(`Target ${targetLabel} has malformed HIRMOS managed block markers.`);
    }
    const afterEnd = endIndex + markers.end.length;
    return ensureTrailingNewline(`${existing.slice(0, startIndex)}${trimTrailingNewline(renderedTemplate)}${existing.slice(afterEnd)}`);
  }

  const separator = existing.trim().length === 0 ? "" : "\n\n";
  return ensureTrailingNewline(`${trimTrailingNewline(existing)}${separator}${trimTrailingNewline(renderedTemplate)}`);
}

function trimTrailingNewline(content: string): string {
  return content.replace(/\n+$/u, "");
}

function ensureTrailingNewline(content: string): string {
  return `${trimTrailingNewline(content)}\n`;
}
