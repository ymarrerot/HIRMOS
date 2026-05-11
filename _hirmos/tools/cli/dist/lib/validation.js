"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.validateProjectRoot = validateProjectRoot;
exports.validateHirmosFramework = validateHirmosFramework;
const fs_1 = __importDefault(require("fs"));
const path_1 = __importDefault(require("path"));
const errors_1 = require("./errors");
const filesystem_1 = require("./filesystem");
function validateProjectRoot(projectRoot) {
    if (!(0, filesystem_1.pathExists)(projectRoot)) {
        (0, errors_1.fail)(`Project path does not exist: ${projectRoot}`);
    }
    if (!fs_1.default.statSync(projectRoot).isDirectory()) {
        (0, errors_1.fail)(`Project path is not a directory: ${projectRoot}`);
    }
}
function validateHirmosFramework(projectRoot) {
    const required = [
        "_hirmos/HIRMOS_CORE.md",
        "_hirmos/project.json",
        "_hirmos/integrations/agent-tools/registry.json"
    ];
    for (const relative of required) {
        const absolute = path_1.default.join(projectRoot, relative);
        if (!(0, filesystem_1.pathExists)(absolute)) {
            (0, errors_1.fail)(`Required HIRMOS file is missing: ${relative}`);
        }
    }
    const templatesDir = path_1.default.join(projectRoot, "_hirmos", "integrations/agent-tools", "templates");
    if (!(0, filesystem_1.pathExists)(templatesDir) || !fs_1.default.statSync(templatesDir).isDirectory()) {
        (0, errors_1.fail)("Required HIRMOS directory is missing: _hirmos/integrations/agent-tools/templates/");
    }
}
