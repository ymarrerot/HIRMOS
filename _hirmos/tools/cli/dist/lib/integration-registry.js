"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.loadRegistry = loadRegistry;
exports.registryOrder = registryOrder;
exports.normalizeSelectedIntegrations = normalizeSelectedIntegrations;
exports.planTargetUpdates = planTargetUpdates;
const path_1 = __importDefault(require("path"));
const errors_1 = require("./errors");
const filesystem_1 = require("./filesystem");
const managed_blocks_1 = require("./managed-blocks");
function loadRegistry(hirmosDir) {
    const registryPath = path_1.default.join(hirmosDir, "integrations/agent-tools", "registry.json");
    const registry = (0, filesystem_1.readJson)(registryPath, "agent integration registry");
    if (!registry || typeof registry !== "object")
        (0, errors_1.fail)("Agent integration registry is malformed.");
    if (registry.schema_version !== 1)
        (0, errors_1.fail)(`Unsupported agent integration registry schema_version: ${registry.schema_version}`);
    if (!registry.managed_block?.start || !registry.managed_block?.end)
        (0, errors_1.fail)("Agent integration registry is missing managed block markers.");
    if (!registry.integrations || typeof registry.integrations !== "object")
        (0, errors_1.fail)("Agent integration registry is missing integrations.");
    return registry;
}
function registryOrder(registry) {
    return Object.keys(registry.integrations);
}
function normalizeSelectedIntegrations(selected, registry) {
    const selectedSet = new Set();
    for (const id of selected) {
        if (!registry.integrations[id]) {
            (0, errors_1.fail)(`Unknown integration id: ${id}. Valid integrations: ${registryOrder(registry).join(", ")}`);
        }
        selectedSet.add(id);
    }
    return registryOrder(registry).filter((id) => selectedSet.has(id));
}
function planTargetUpdates(projectRoot, hirmosDir, selected, registry) {
    const grouped = new Map();
    for (const id of selected) {
        const integration = registry.integrations[id];
        if (integration.mode !== "managed_block")
            (0, errors_1.fail)(`Unsupported integration mode for ${id}: ${integration.mode}`);
        const templatePath = path_1.default.join(hirmosDir, "integrations/agent-tools", integration.template);
        const templateContent = (0, filesystem_1.readText)(templatePath);
        (0, managed_blocks_1.validateTemplateManagedBlock)(templateContent, registry.managed_block, integration.template);
        const existing = grouped.get(integration.target);
        if (existing) {
            if (existing.templateContent !== templateContent) {
                (0, errors_1.fail)(`Integrations sharing target ${integration.target} use different templates. Refusing ambiguous update.`);
            }
            existing.integrationIds.push(id);
            continue;
        }
        grouped.set(integration.target, {
            target: integration.target,
            targetPath: path_1.default.resolve(projectRoot, integration.target),
            templatePath,
            templateContent,
            integrationIds: [id]
        });
    }
    return Array.from(grouped.values());
}
