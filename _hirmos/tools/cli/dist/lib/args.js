"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.parseArgs = parseArgs;
exports.normalizeVersionOption = normalizeVersionOption;
exports.parseIntegrationList = parseIntegrationList;
exports.helpText = helpText;
const path_1 = __importDefault(require("path"));
const errors_1 = require("./errors");
function parseArgs(argv) {
    if (argv.length === 0 || argv[0] === "--help" || argv[0] === "-h") {
        return { command: "help" };
    }
    const command = argv[0];
    if (command !== "init") {
        (0, errors_1.fail)(`Unsupported command: ${command}. This CLI currently supports: hirmos init`);
    }
    let projectPath = ".";
    let projectPathSet = false;
    let integrationValue;
    let source;
    let version = "latest";
    let offline = false;
    for (let i = 1; i < argv.length; i += 1) {
        const arg = argv[i];
        if (arg === "--integration") {
            const value = argv[++i];
            if (!value)
                (0, errors_1.fail)("Missing value for --integration");
            integrationValue = value;
            continue;
        }
        if (arg.startsWith("--integration=")) {
            integrationValue = arg.slice("--integration=".length);
            continue;
        }
        if (arg === "--source") {
            const value = argv[++i];
            if (!value)
                (0, errors_1.fail)("Missing value for --source");
            source = value;
            continue;
        }
        if (arg.startsWith("--source=")) {
            source = arg.slice("--source=".length);
            continue;
        }
        if (arg === "--version") {
            const value = argv[++i];
            if (!value)
                (0, errors_1.fail)("Missing value for --version");
            version = value;
            continue;
        }
        if (arg.startsWith("--version=")) {
            version = arg.slice("--version=".length);
            continue;
        }
        if (arg === "--offline") {
            offline = true;
            continue;
        }
        if (arg === "--help" || arg === "-h") {
            return { command: "help" };
        }
        if (arg.startsWith("-")) {
            (0, errors_1.fail)(`Unsupported option: ${arg}`);
        }
        if (projectPathSet) {
            (0, errors_1.fail)(`Unexpected extra positional argument: ${arg}`);
        }
        projectPath = arg;
        projectPathSet = true;
    }
    const integrations = parseIntegrationList(integrationValue ?? "agents");
    return {
        command: "init",
        projectPath: path_1.default.resolve(projectPath),
        integrations,
        source: source ? path_1.default.resolve(source) : undefined,
        version: normalizeVersionOption(version),
        offline
    };
}
function normalizeVersionOption(value) {
    const normalized = value.trim();
    if (!normalized)
        (0, errors_1.fail)("--version must not be empty");
    return normalized;
}
function parseIntegrationList(value) {
    const ids = value
        .split(",")
        .map((item) => item.trim())
        .filter(Boolean);
    if (ids.length === 0) {
        (0, errors_1.fail)("--integration must include at least one integration id");
    }
    return ids;
}
function helpText() {
    return `HIRMOS CLI\n\nUsage:\n  hirmos init [project-path] [--integration <ids>] [--source <path>] [--version <version>] [--offline]\n\nDefaults:\n  project-path: .\n  integration: agents\n  source: existing _hirmos/ in the project, otherwise the latest GitHub release\n  version: latest\n\nNotes:\n  --source installs from a local _hirmos folder, framework folder, or hirmos-framework.zip.\n  --version selects a GitHub release when _hirmos/ is missing and --source is not provided.\n  --offline disables remote release download and requires an existing _hirmos/ or --source.\n\nThis CLI implements hirmos init. Workflow commands such as hirmos requirements are interpreted by an agent after HIRMOS Core is loaded.\n`;
}
