# matrix-tool-query-lab

`matrix-tool-query-lab` explores cli tools in Python. The repository keeps the core rule set compact, then surrounds it with examples that show how the decisions move.

## Matrix Tool Query Lab Notes

The quickest review path is the verifier first, then the fixtures, then the operations note. That order makes it easy to see whether the code, data, and explanation still agree.

## Why This Exists

The goal is to capture the core behavior in code and make the surrounding assumptions obvious. A reader should be able to run the verifier, open the fixtures, and understand why each decision was made.

## Implementation Notes

The project is organized around a compact model rather than a large framework. Inputs are scored, classified, and checked against golden fixtures. The constants live in code and are mirrored in metadata so documentation drift is easy to catch. The Python code favors standard library tools and direct tests over framework weight.

## Example Scenarios

The examples are meant to be readable before they are exhaustive. They cover enough variation to show how latency and risk can pull a decision below the threshold.

## Feature Notes

- Uses fixture data to keep argument shape changes visible in code review.
- Includes extended examples for file input, including `recovery` and `degraded`.
- Documents repeatable reports tradeoffs in `docs/operations.md`.
- Runs locally with a single verification command and no external credentials.
- Stores project constants and verification metadata in `metadata/project.json`.

## Local Setup

Clone the repository, enter the directory, and run the verifier. No database server, cloud account, or token is required.

## Tests

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/audit.ps1
```

The audit command checks repository structure and README constraints before it delegates to the verifier.

## Code Tour

- `src`: primary implementation
- `tests`: verification harness
- `fixtures`: compact golden scenarios
- `examples`: expanded scenario set
- `metadata`: project constants and verification metadata
- `docs`: operations and extension notes
- `scripts`: local verification and audit commands
- `pyproject.toml`: Python project metadata

## Boundaries

This code is local-first. It makes no claim about deployed usage and avoids credentials, hosted state, and environment-specific setup.

## Roadmap

- Add malformed input fixtures so the failure path is as visible as the happy path.
- Split the scoring constants into a typed configuration object and validate it before use.
- Add a comparison mode that shows how decisions change when one signal is adjusted.
- Add one more cli tools fixture that focuses on a malformed or borderline input.

## Try It

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/verify.ps1
```

This runs the language-level build or test path against the compact fixture set.
