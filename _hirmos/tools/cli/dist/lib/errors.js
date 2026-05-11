"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.HirmosCliError = void 0;
exports.fail = fail;
class HirmosCliError extends Error {
    constructor(message) {
        super(message);
        this.name = "HirmosCliError";
    }
}
exports.HirmosCliError = HirmosCliError;
function fail(message) {
    throw new HirmosCliError(message);
}
