# Data Contract

## Contract Overview

- Contract parties: Producer = whoever exports/prepares the source CSV (Account Coordinator / upstream export process, not formally named); Consumer = this dashboard application (`app/validate.py`, `app/db.py`, `app/metrics.py`).
- Contract scope: a single file/table, `fact_customer_request`, delivered as one CSV upload per ingestion event. No streaming events, no other tables.
- Contract version: `1.0.0`, effective 2026-10-02 (this document's authoring date). No prior version exists.

## Schema Definitions

| Field Name | Data Type | Allowed Values | Nullable |
|---|---|---|---|
| `request_id` | STRING | any unique string | No |
| `request_type` | STRING (enum) | `assessment`, `report`, `clarification` | No |
| `request_title` | STRING | free text | No |
| `owner` | STRING | any non-empty string | No |
| `due_date` | DATE (ISO `YYYY-MM-DD`) | valid calendar date | No |
| `status` | STRING (enum) | `done`, `in_progress`, `open` | No |

Source: `DATA_MODEL_SPEC.md`. Enforced by: `app/config.py` (`REQUIRED_COLUMNS`, `VALID_REQUEST_TYPES`, `VALID_STATUSES`) and `app/validate.py`.

## SLA Commitments

- Latency SLA: `null`; owner = Account Service Lead. Not formally set — in practice, data becomes available to the dashboard immediately after a successful upload (event-driven, not scheduled), so there is no latency window to miss.
- Availability SLA: `null`; not applicable — this is a manually-triggered upload, not a running service with an uptime commitment.
- Completeness SLA: `null`; owner = Account Service Lead. No "% of rows must be present" threshold has been approved. Current behavior is binary: a file either passes validation in full, or the entire file is rejected (`app/validate.py`) — there is no partial-acceptance mode this SLA would apply to.

## Breaking Change Policy

- Breaking change definition: any change that removes a required column, renames a column, narrows an enum (`VALID_REQUEST_TYPES`/`VALID_STATUSES`), or changes `due_date` format away from ISO `YYYY-MM-DD`.
- Notice period: `null`; owner = Project Owner. No formal process exists yet for announcing contract changes to whoever produces the CSV.
- Migration procedure: `null`; owner = Engineering Lead. Today, a contract change means directly editing `app/config.py` (`REQUIRED_COLUMNS` / `VALID_REQUEST_TYPES` / `VALID_STATUSES`) and `docs/ddd-bundle/DATA_QUALITY.md`, then re-validating with the test suite (`app/tests/test_validate.py`) — there is no versioned migration tooling.
- Versioning strategy: `null`; owner = Project Owner. This contract is currently unversioned in code (no `contract_version` field is read or checked by `app/validate.py`).

## Required Fields

- Required fields per table: all six columns listed in Schema Definitions above — none are optional. Source: `app/config.py:REQUIRED_COLUMNS`.
- Default values: none. A missing column causes outright file rejection (`app/validate.py`, "Missing required column(s)"); there are no per-field defaults substituted for absent data.
- Validation rules: completeness (non-null/non-empty after whitespace normalization), `request_id` uniqueness, ISO date format for `due_date`, and enum membership for `request_type`/`status` — all implemented in `app/validate.py` and exercised by `app/tests/test_validate.py`.

## Data Type Constraints

- Type mapping: CSV is read with every column forced to STRING (`pd.read_csv(..., dtype=str)` in `app/app.py`) to avoid pandas' automatic type inference corrupting IDs or dates; `due_date` is explicitly parsed to a Python `date` only after validation passes, then stored as DuckDB `DATE`. All other fields map to DuckDB `VARCHAR`.
- Precision rules: not applicable — no numeric/decimal fields exist in this contract.
- String constraints: no maximum length is enforced on any field (`request_title`, `owner`, `request_id` are unbounded VARCHAR). Encoding is UTF-8 (the real source file contains Thai-language `request_title` values and is read/written as UTF-8 throughout). Maximum length limit: `null`; owner = Engineering Lead, not currently required by observed data (the real file's longest values are well within any reasonable VARCHAR limit).
