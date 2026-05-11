"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.runInit = runInit;
const fs_1 = __importDefault(require("fs"));
const path_1 = __importDefault(require("path"));
const filesystem_1 = require("../lib/filesystem");
const integration_registry_1 = require("../lib/integration-registry");
const managed_blocks_1 = require("../lib/managed-blocks");
const project_config_1 = require("../lib/project-config");
const source_install_1 = require("../lib/source-install");
const validation_1 = require("../lib/validation");
function runInit(options) {
    const projectRoot = path_1.default.resolve(options.projectPath);
    (0, validation_1.validateProjectRoot)(projectRoot);
    const installResult = (0, source_install_1.ensureHirmosInstalled)(projectRoot, {
        source: options.source,
        version: options.version,
        offline: options.offline
    });
    (0, validation_1.validateHirmosFramework)(projectRoot);
    const hirmosDir = path_1.default.join(projectRoot, "_hirmos");
    const registry = (0, integration_registry_1.loadRegistry)(hirmosDir);
    const selected = (0, integration_registry_1.normalizeSelectedIntegrations)(options.integrations, registry);
    const plannedTargets = (0, integration_registry_1.planTargetUpdates)(projectRoot, hirmosDir, selected, registry);
    const currentConfig = (0, project_config_1.loadProjectConfig)(projectRoot);
    const mergeResult = (0, project_config_1.mergeProjectConfig)(currentConfig, selected, registry);
    const renderedWrites = plannedTargets.map((target) => {
        (0, filesystem_1.assertInsideProject)(projectRoot, target.targetPath);
        const existing = fs_1.default.existsSync(target.targetPath) ? (0, filesystem_1.readText)(target.targetPath) : null;
        const nextContent = (0, managed_blocks_1.updateManagedBlock)(existing, target.templateContent, registry.managed_block, target.target);
        return {
            path: target.targetPath,
            relative: target.target,
            content: nextContent,
            integrationIds: target.integrationIds
        };
    });
    for (const write of renderedWrites) {
        (0, filesystem_1.writeText)(write.path, write.content);
    }
    (0, project_config_1.writeProjectConfig)(projectRoot, mergeResult.config);
    return formatInitSummary(mergeResult.wasFirstInitialization, selected, mergeResult.added, mergeResult.alreadyInstalled, renderedWrites.map((item) => item.relative), installResult);
}
function formatInitSummary(first, selected, added, alreadyInstalled, targets, installResult) {
    const lines = [];
    if (first) {
        lines.push("HIRMOS initialized.", "");
        if (installResult.installed && installResult.sourceDescription) {
            lines.push(`Installed framework from ${installResult.sourceDescription}.`, "");
        }
        lines.push("Installed integrations:");
        for (const id of selected)
            lines.push(`- ${id}`);
        lines.push("", "Generated or updated files:");
        for (const target of targets)
            lines.push(`- ${target}`);
        lines.push("", "Next step:");
        lines.push("Open your AI coding tool in this project and run a HIRMOS workflow command, for example:");
        lines.push("");
        lines.push("hirmos requirements");
        lines.push("hirmos system-design");
        lines.push("hirmos implementation");
        lines.push("");
        lines.push("Fallback initialization:");
        lines.push("If your tool does not automatically pick up the selected agent/tool integration files, copy and paste this prompt into your agent:");
        lines.push("");
        lines.push("Read and follow the instructions on _hirmos/HIRMOS_CORE.md.");
        lines.push("", "To add more integrations later:");
        lines.push("hirmos init --integration claude,cursor,copilot");
        return `${lines.join("\n")}\n`;
    }
    lines.push("HIRMOS integrations updated.", "");
    if (added.length > 0) {
        lines.push("Added:");
        for (const id of added)
            lines.push(`- ${id}`);
        lines.push("");
    }
    if (alreadyInstalled.length > 0) {
        lines.push("Already installed:");
        for (const id of alreadyInstalled)
            lines.push(`- ${id}`);
        lines.push("");
    }
    lines.push("Generated or updated files:");
    for (const target of targets)
        lines.push(`- ${target}`);
    return `${lines.join("\n").replace(/\n+$/u, "")}\n`;
}
