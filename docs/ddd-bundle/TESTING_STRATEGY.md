# Testing Strategy

## Unit Tests (SQL)
- total count equals accepted row count.
- completed count includes only `status = done`.
- overdue count excludes `done` requests.
- due date equal to reference date is not overdue.
- `days_overdue` equals calendar-day difference for overdue rows.
- `request_type` filter changes all KPI cards and detail list consistently.

## Integration Tests
1. Upload valid CSV -> validation passes -> DuckDB table replaced atomically.
2. Upload invalid schema -> rejected -> previous valid table remains unchanged.
3. Upload same valid CSV twice -> same row count and same metrics.

## Metric Validation Tests
Create a small golden fixture with a test-only fixed `reference_date` and manually calculated expected counts. The fixture date is test data only and must not be reused as the production assignment reference date.

## Dashboard Acceptance Tests
- cards: Total, Completed, Overdue visible.
- breakdown by `request_type` visible.
- user can select one `request_type` or All.
- overdue detail contains `owner` and `days_overdue`.
- all displayed overdue calculations use the configured assignment `reference_date`.

## Test Automation and CI
- validation/unit/integration tests must block deployment on failure.
- coverage expectation: `null`; owner = Engineering Lead.
