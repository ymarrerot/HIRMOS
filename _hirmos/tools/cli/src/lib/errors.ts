export class HirmosCliError extends Error {
  constructor(message: string) {
    super(message);
    this.name = "HirmosCliError";
  }
}

export function fail(message: string): never {
  throw new HirmosCliError(message);
}
