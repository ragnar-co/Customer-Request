# Data Model Spec (Semantic Layer)

## Fact Tables

### `fact_customer_request`
- grain: `1 customer request`
- primary key: `request_id` (enforced both at validation time and as a DuckDB `PRIMARY KEY` constraint — see `app/db.py`)
- source: accepted CSV upload
- columns: `request_id`, `request_type`, `request_title`, `owner`, `due_date`, `status`, `loaded_at`

## Dimension Tables
No separate dimension table is required for the assignment-scale implementation. `request_type` and `owner` are attributes of the request fact and are used as filter/slice fields.

## Relationships
Single-table analytical model for the required dashboard; no joins are required.

## Grain Definitions
One row in `fact_customer_request` represents exactly one `request_id`. The provided source has 12,022 rows and 12,022 unique `request_id` values.

## PDPA Data Classification
The assignment does not specify whether any field is personal data. Classification for all source fields remains `null` pending Data Governance review; owner = Data Governance / Project Owner. See `DATA_GOVERNANCE.md` for the ownership matrix and classification placeholders tracking this open item.

### Owned enums
`scd_type` and `pdpa_classification` are owned here. No project values are declared until governance decisions are available.
