"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.loadProjectConfig = loadProjectConfig;
exports.mergeProjectConfig = mergeProjectConfig;
exports.writeProjectConfig = writeProjectConfig;
const path_1 = __importDefault(require("path"));
const filesystem_1 = require("./filesystem");
const integration_registry_1 = require("./integration-registry");
function loadProjectConfig(projectRoot) {
    return (0, filesystem_1.readJson)(path_1.default.join(projectRoot, "_hirmos", "project.json"), "_hirmos/project.json");
}
function mergeProjectConfig(config, selected, registry) {
    const previousInstalled = Array.isArray(config.integrations?.installed)
        ? config.integrations.installed.filter((id) => typeof id === "string")
        : [];
    const previousSet = new Set(previousInstalled);
    const selectedSet = new Set(selected);
    const added = selected.filter((id) => !previousSet.has(id));
    const alreadyInstalled = selected.filter((id) => previousSet.has(id));
    const knownOrder = (0, integration_registry_1.registryOrder)(registry);
    const allKnown = knownOrder.filter((id) => previousSet.has(id) || selectedSet.has(id));
    const unknownExisting = previousInstalled.filter((id) => !registry.integrations[id]);
    const installed = [...allKnown, ...unknownExisting];
    const nextConfig = {
        ...config,
        integrations: {
            ...(config.integrations ?? {}),
            installed
        }
    };
    return {
        config: nextConfig,
        previousInstalled,
        added,
        alreadyInstalled,
        installed,
        wasFirstInitialization: previousInstalled.length === 0
    };
}
function writeProjectConfig(projectRoot, config) {
    (0, filesystem_1.writeJson)(path_1.default.join(projectRoot, "_hirmos", "project.json"), config);
}
