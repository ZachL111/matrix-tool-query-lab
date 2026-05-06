# matrix-tool-query-lab

`matrix-tool-query-lab` is a Python project in cli tools. Its focus is to package a Python local lab for query analysis with seeded input scenarios, deterministic summary checks, and documented operating limits.

## Use Case

The point is to make a small domain rule concrete enough that a reader can change it and immediately see what broke.

## Matrix Tool Query Lab Review Notes

`edge` and `stale` are the cases worth reading first. They show the optimistic and cautious ends of the fixture.

## Highlights

- `fixtures/domain_review.csv` adds cases for file span and terminal width.
- `metadata/domain-review.json` records the same cases in structured form.
- `config/review-profile.json` captures the read order and the two review questions.
- `examples/matrix-tool-query-walkthrough.md` walks through the case spread.
- The Python code includes a review path for `argument risk` and `file span`.
- `docs/field-notes.md` explains the strongest and weakest cases.

## Code Layout

The implementation keeps the scoring rule plain: reward signal and confidence, preserve slack, penalize drag, then classify the result into a review lane.

The added Python path is deliberately direct, with fixtures doing most of the explaining.

## Run The Check

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/verify.ps1
```

## Regression Path

The same command runs the local verification path. The highest-scoring domain case is `edge` at 247, which lands in `ship`. The most cautious case is `stale` at 163, which lands in `ship`.

## Future Work

This remains a local project with deterministic fixtures. It does not depend on credentials, hosted services, or live data. Future work should add richer malformed inputs before widening the public API.
