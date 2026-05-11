"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.ensureDir = ensureDir;
exports.readText = readText;
exports.writeText = writeText;
exports.readJson = readJson;
exports.writeJson = writeJson;
exports.assertInsideProject = assertInsideProject;
exports.pathExists = pathExists;
const fs_1 = __importDefault(require("fs"));
const path_1 = __importDefault(require("path"));
const errors_1 = require("./errors");
function ensureDir(dirPath) {
    fs_1.default.mkdirSync(dirPath, { recursive: true });
}
function readText(filePath) {
    return fs_1.default.readFileSync(filePath, "utf8");
}
function writeText(filePath, content) {
    ensureDir(path_1.default.dirname(filePath));
    fs_1.default.writeFileSync(filePath, content, "utf8");
}
function readJson(filePath, label) {
    try {
        return JSON.parse(readText(filePath));
    }
    catch (error) {
        (0, errors_1.fail)(`Invalid ${label} JSON at ${filePath}: ${error.message}`);
    }
}
function writeJson(filePath, value) {
    writeText(filePath, `${JSON.stringify(value, null, 2)}\n`);
}
function assertInsideProject(projectRoot, targetPath) {
    const relative = path_1.default.relative(projectRoot, targetPath);
    if (relative.startsWith("..") || path_1.default.isAbsolute(relative)) {
        (0, errors_1.fail)(`Refusing to write outside the project root: ${targetPath}`);
    }
}
function pathExists(filePath) {
    return fs_1.default.existsSync(filePath);
}
