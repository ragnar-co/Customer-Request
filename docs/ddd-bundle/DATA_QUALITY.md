# Data Quality Spec

## Null and Completeness Checks
- `request_id`, `request_type`, `request_title`, `owner`, `due_date`, `status` must be non-null/non-empty.
- Current supplied source: no nulls observed in those columns.

## Range and Validity Checks
- `due_date` must parse as ISO date `YYYY-MM-DD`.
- `request_type` must match the contract values observed/approved for this project.
- `status` must match the contract values observed/approved for this project.
- Whitespace normalization: leading/trailing whitespace is stripped from every required column before completeness, uniqueness, and contract checks run (e.g. `" R1 "` and `"R1"` are the same `request_id`; `" assessment "` is accepted as `assessment`). Implemented in `app/validate.py`.

## Case Normalization Policy (confirmed by Project Owner, 2026-10-02)

Case is **not** normalized. `request_type`/`status` values that differ only in case from the approved contract (e.g. `Assessment`, `Done`) are **rejected**, not silently folded to the canonical lowercase form. This is a deliberate decision, consistent with this document's "do not coerce silently" principle for `due_date` and unknown enum values — the same discipline now explicitly extends to case variants. Implemented in `app/validate.py` (see inline comment above the `request_type`/`status` contract checks).

## Due Date vs. Request Date (confirmed not applicable, 2026-10-02)

The rule "`due_date` must be on or after the request's creation date" **cannot be implemented**: no `request_date` (or any request-creation-date) column exists anywhere in the approved source contract (`request_id, request_type, request_title, owner, due_date, status` — see `DATA_MODEL_SPEC.md`), and the real source file (`eclair_customer_requests_2_3MB.csv`) has no such column. Adding one would be a source-contract change requiring a new Project Owner-approved column, which was explicitly declined during the 2026-10-02 validation follow-up. This is recorded here as a known, intentional scope limitation rather than a missing check.

## Referential Integrity Checks
No foreign keys exist in the single-table model. `request_id` uniqueness is enforced twice: at validation time (`app/validate.py`, rejects the whole file on duplicates) and at the database level (`fact_customer_request.request_id PRIMARY KEY`, defined in `app/db.py`).

## Anomaly Detection Rules
No anomaly threshold is invented. `anomaly_bound = null`; calibration owner = Analytics / Project Owner if anomaly monitoring is later required.

## Quality Dashboards
Upload validation result should show accepted/rejected status, row count, and validation errors.

### Executable assertions
```sql
SELECT request_id, COUNT(*)
FROM fact_customer_request
GROUP BY request_id
HAVING COUNT(*) > 1;

SELECT *
FROM fact_customer_request
WHERE request_id IS NULL OR request_type IS NULL OR request_title IS NULL
   OR owner IS NULL OR due_date IS NULL OR status IS NULL;
```

### Owned enum
`rule_severity`: error / warning
- errors block dataset replacement.
- warnings do not block load but must be visible.
