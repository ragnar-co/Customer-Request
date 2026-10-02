# Data Pipeline Spec

## Pipeline Overview
`customer_request_csv_ingest`: uploaded CSV -> validation -> DuckDB `fact_customer_request` -> dashboard queries.

## Pipeline Definitions
- source: user-uploaded CSV
- transform_tool: application ingestion layer + DuckDB SQL
- destination: DuckDB table `fact_customer_request`
- schedule: event-driven on upload, not cron
- dependencies: none external
- load strategy: replace current accepted snapshot atomically after full validation

## Source Systems
- Source System Name: Customer Request CSV
- Extraction Method: file upload
- Required columns: `request_id`, `request_type`, `request_title`, `owner`, `due_date`, `status`

## Error Handling and Retry
- Schema/type/value errors are permanent for that file: reject the upload and return row/column diagnostics.
- Storage write errors may be retried by the application; do not expose partially loaded snapshots.
- A failed file must not replace the last valid dataset.

## Credentials & Secret Management
No external source credentials are required by the assignment. If deployment introduces secrets, store them outside the repository and inject by environment configuration.

## Load Strategy
- Full snapshot replace for this assignment-scale CSV.
- Validate before transaction commit.
- Primary key uniqueness on `request_id` prevents duplicate requests.
- Re-uploading the same valid file must produce the same row count and metrics (idempotent snapshot load).
