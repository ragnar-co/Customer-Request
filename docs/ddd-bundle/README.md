# Customer Request Follow-up Dashboard

## Project Name and Description
Dashboard for weekly follow-up of cybersecurity customer requests. It imports a validated CSV, stores the accepted snapshot in DuckDB, summarizes total/completed/overdue requests by service type, and lists overdue requests with owner and days overdue.

## Quick Start
1. Configure the assignment `reference_date` explicitly.
2. Start the application.
3. Upload the source CSV.
4. Confirm validation passes and 12,022 rows are accepted for the supplied dataset.
5. Open the dashboard and test All plus each `request_type` filter.
6. Run automated tests before deployment.

## Prerequisites
Exact application/runtime versions are not supplied by the assignment and must be pinned by the implementation team.

## Installation
Implementation-specific commands are not included because no application framework/repository was supplied with this documentation request.

## Usage
Upload CSV -> validate -> load DuckDB -> choose service type -> review KPI cards -> follow up overdue owners.

## Architecture Overview
`CSV -> validator -> DuckDB fact_customer_request -> canonical SQL metrics -> dashboard`

## Contributing
Do not redefine metric formulas inside UI code. Keep `reference_date` explicit and deterministic. New source values require contract/validation review before acceptance.

## License
`null`; owner = Project Owner.
