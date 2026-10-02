# DDD Scope — Customer Request Follow-up Dashboard

- Selected blueprint: `ddd-data-analytics-v2.4.0` (corrected 2026-10-02 — the blueprint file actually present in this repo at `docs/ddd-blueprints/ddd-data-analytics-v2.4.0.json` is v2.4.0; the previous reference to `v2.8.0` did not match any file in the repo and has been corrected to avoid citing an unverifiable version)
- Project: `Customer Request Follow-up Dashboard`
- Source file used: `eclair_customer_requests_2_3MB.csv`
- Source row count: 12,022
- Storage choice: DuckDB
- Source schema: `request_id`, `request_type`, `request_title`, `owner`, `due_date`, `status`
- Observed `request_type`: `assessment`, `report`, `clarification`
- Observed `status`: `done`, `in_progress`, `open`
- `request_id`: 12,022 unique values, no duplicates observed
- Nulls in the six source columns: none observed
- `due_date` observed range: 2026-06-06 through 2026-10-22

## Resolved input: reference_date

`reference_date = 2026-10-02` (confirmed by Project Owner, 2026-10-02). Configured as `APP_REFERENCE_DATE` (see `app/config.py`), with that same fixed value as the compiled-in default — never derived from the runtime system clock. Overridable only via explicit, deliberate configuration (`.env` / environment variable), per the original constraint below.

The assignment says to use the reference date specified by the assignment so results are reproducible. The application must accept one fixed configured reference date and must not silently substitute the runtime system date — this constraint remains in force even though the open question is now resolved.

## Document set

This bundle is an implementation-focused DDD subset produced in dependency order. It is not claimed to be the official "minimum central-condition" set because those central conditions were not supplied.

## Blueprint boundary note (added 2026-10-02, Project Validation Report follow-up)

`CONSTRAINTS.md` and `TASKS.md` in this bundle are **not** part of the `ddd-data-analytics` blueprint's document set (see `docs/ddd-blueprints/ddd-data-analytics-v2.4.0.json` — its `generation_order` has no `constraints` or `tasks` entries). Both documents match `ddd-web-app`'s document IDs/filenames instead (`docs/ddd-blueprints/ddd-web-app-v2.4.0.json`).

This is a deliberate, documented exception, not an undetected blueprint mix: `CONSTRAINTS.md` and `TASKS.md` are retained as supplementary engineering documents because this project needed a constraints record and a task breakdown that the `ddd-data-analytics` document set does not otherwise provide, and recreating that content under `ddd-web-app`'s full generation order was out of scope. No other `ddd-web-app` document (PRD, ARCHITECTURE, ADR, UI_SPEC, SECURITY, API_SPEC, AGENTS, DEPLOYMENT, etc.) exists in this bundle, and this project is not a `ddd-web-app` project. Every other document in this bundle belongs exclusively to `ddd-data-analytics`.
