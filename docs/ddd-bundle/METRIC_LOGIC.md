# Metric Logic Spec (SQL)

## Metric SQL Implementations

```sql
-- Parameter supplied by project configuration; never CURRENT_DATE implicitly.
-- :reference_date must be confirmed from the assignment.

SELECT COUNT(*) AS total_requests
FROM fact_customer_request;

SELECT COUNT(*) AS completed_requests
FROM fact_customer_request
WHERE status = 'done';

SELECT COUNT(*) AS overdue_requests
FROM fact_customer_request
WHERE status <> 'done'
  AND due_date < CAST(:reference_date AS DATE);

SELECT
  request_id,
  request_type,
  request_title,
  owner,
  due_date,
  DATE_DIFF('day', due_date, CAST(:reference_date AS DATE)) AS days_overdue
FROM fact_customer_request
WHERE status <> 'done'
  AND due_date < CAST(:reference_date AS DATE)
ORDER BY days_overdue DESC, request_id;
```

For `request_type` filtering, apply `WHERE request_type = :request_type` to the same canonical query logic, or omit that predicate when filter value is All.

## Edge Case Handling
- `status = done`: never counted as overdue even when its due date is before reference date.
- `due_date = reference_date`: not overdue because rule uses `<`, not `<=`.
- invalid or null `due_date`: reject during validation; do not coerce silently.
- unknown `status`: reject during validation unless source contract is updated.
- missing `reference_date`: block overdue metric calculation and show configuration error.

## Transformation Dependencies
```mermaid
graph LR
  CSV[CSV upload] --> VALIDATE[Validate schema and values]
  VALIDATE --> FACT[fact_customer_request]
  FACT --> METRICS[Canonical metric queries]
  METRICS --> DASH[Dashboard]
```
