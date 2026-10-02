# Analytics Changelog

## Metric Definition Changes

No metric formula (`metric_total_requests`, `metric_completed_requests`, `metric_overdue_requests`, `metric_days_overdue`) has changed since `METRIC_LOGIC.md` was first written. All entries below are configuration, validation, or schema changes — not metric redefinitions.

## KPI Target Changes

No KPI target changes — `KPI_DICTIONARY.md`'s single KPI ("Customer Request Follow-up Readiness") has never had an approved target (`target: null` in that document, unchanged).

## Pipeline / Configuration Changes

| Change Date | Changed | Change Type | Before → After | Impact | Approved By |
|---|---|---|---|---|---|
| 2026-10-02 | `reference_date` | Configuration resolved | `null` (unresolved) → `2026-10-02`, configurable via `APP_REFERENCE_DATE` | Unblocks all overdue-based metrics; no formula change | Project Owner |
| 2026-10-02 | `app/validate.py` whitespace handling | Validation logic added | No normalization → leading/trailing whitespace stripped on all required columns before validation | Fixes a previously-missing CSV validation rule; does not change metric formulas | Project Owner (via Project Validation Report follow-up) |
| 2026-10-02 | `fact_customer_request` schema (`app/db.py`) | Schema change | `CREATE OR REPLACE TABLE ... AS SELECT` (no constraints) → explicit schema with `request_id PRIMARY KEY` and `NOT NULL` columns, loaded via `BEGIN; CREATE OR REPLACE TABLE; INSERT; COMMIT` | Adds DB-level uniqueness enforcement in addition to the existing validation-layer check; no change to stored data or metric results | Project Owner (via Project Validation Report follow-up) |

## Breaking Changes Log

None of the changes above are breaking: no column was renamed or removed, no metric formula changed, and the real source CSV (`eclair_customer_requests_2_3MB.csv`) continues to load with identical results (Total 12,022 / Completed 5,461 / Overdue 3,650) before and after.
