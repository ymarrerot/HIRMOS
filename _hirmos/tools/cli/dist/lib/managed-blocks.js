"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.validateTemplateManagedBlock = validateTemplateManagedBlock;
exports.updateManagedBlock = updateManagedBlock;
const errors_1 = require("./errors");
function countOccurrences(content, needle) {
    if (!needle)
        return 0;
    let count = 0;
    let index = 0;
    while (true) {
        const found = content.indexOf(needle, index);
        if (found === -1)
            return count;
        count += 1;
        index = found + needle.length;
    }
}
function validateTemplateManagedBlock(template, markers, label) {
    const starts = countOccurrences(template, markers.start);
    const ends = countOccurrences(template, markers.end);
    if (starts !== 1 || ends !== 1) {
        (0, errors_1.fail)(`Template ${label} must contain exactly one complete HIRMOS managed block.`);
    }
    if (template.indexOf(markers.start) > template.indexOf(markers.end)) {
        (0, errors_1.fail)(`Template ${label} has malformed HIRMOS managed block markers.`);
    }
}
function updateManagedBlock(existing, renderedTemplate, markers, targetLabel) {
    validateTemplateManagedBlock(renderedTemplate, markers, targetLabel);
    if (existing === null) {
        return ensureTrailingNewline(renderedTemplate);
    }
    const starts = countOccurrences(existing, markers.start);
    const ends = countOccurrences(existing, markers.end);
    if (starts !== ends) {
        (0, errors_1.fail)(`Target ${targetLabel} has malformed HIRMOS managed block markers.`);
    }
    if (starts > 1) {
        (0, errors_1.fail)(`Target ${targetLabel} contains multiple HIRMOS managed blocks. Refusing to modify it.`);
    }
    if (starts === 1) {
        const startIndex = existing.indexOf(markers.start);
        const endIndex = existing.indexOf(markers.end, startIndex);
        if (endIndex === -1 || startIndex > endIndex) {
            (0, errors_1.fail)(`Target ${targetLabel} has malformed HIRMOS managed block markers.`);
        }
        const afterEnd = endIndex + markers.end.length;
        return ensureTrailingNewline(`${existing.slice(0, startIndex)}${trimTrailingNewline(renderedTemplate)}${existing.slice(afterEnd)}`);
    }
    const separator = existing.trim().length === 0 ? "" : "\n\n";
    return ensureTrailingNewline(`${trimTrailingNewline(existing)}${separator}${trimTrailingNewline(renderedTemplate)}`);
}
function trimTrailingNewline(content) {
    return content.replace(/\n+$/u, "");
}
function ensureTrailingNewline(content) {
    return `${trimTrailingNewline(content)}\n`;
}
