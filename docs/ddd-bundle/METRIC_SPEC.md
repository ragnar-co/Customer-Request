# Metric Specification

## Metric Profiles

### `metric_total_requests`
- definition: number of accepted requests in the current filter context.
- parent_kpi: Customer Request Follow-up Readiness
- owner: Account Service Lead
- grain: `1 dashboard filter context`
- optional_filters: `request_type`
- refresh_cadence: on successful CSV import
- action_threshold: `null`; owner = Account Service Lead
- metric_status: draft

### `metric_completed_requests`
- definition: number of requests with source `status = done` in current filter context.
- parent_kpi: Customer Request Follow-up Readiness
- owner: Account Service Lead
- grain: `1 dashboard filter context`
- optional_filters: `request_type`
- refresh_cadence: on successful CSV import
- action_threshold: `null`; owner = Account Service Lead
- metric_status: draft

### `metric_overdue_requests`
- definition: number of non-completed requests where `due_date < reference_date`.
- parent_kpi: Customer Request Follow-up Readiness
- owner: Account Service Lead
- grain: `1 dashboard filter context`
- optional_filters: `request_type`
- refresh_cadence: on successful CSV import / configured reference date
- action_threshold: `null`; owner = Account Service Lead
- metric_status: draft

### `metric_days_overdue`
- definition: number of calendar days between `due_date` and `reference_date`, only for overdue requests.
- parent_kpi: Customer Request Follow-up Readiness
- owner: Account Service Lead
- grain: `1 request`
- optional_filters: `request_type`, `owner`
- refresh_cadence: on successful CSV import / configured reference date
- action_threshold: `null`; owner = Account Service Lead
- metric_status: draft

## Formula Reference
- `metric_total_requests = COUNT(*)`
- `metric_completed_requests = COUNT(*) FILTER (WHERE status = 'done')`
- `metric_overdue_requests = COUNT(*) FILTER (WHERE status <> 'done' AND due_date < reference_date)`
- `metric_days_overdue = DATE_DIFF('day', due_date, reference_date)` for rows satisfying overdue predicate.

## Grain and Filter Matrix

| Metric | Grain | Required filter | Optional filter |
|---|---|---|---|
| total_requests | filter context | accepted rows only | request_type |
| completed_requests | filter context | accepted rows only | request_type |
| overdue_requests | filter context | fixed `reference_date` | request_type |
| days_overdue | 1 request | overdue predicate | request_type, owner |

## Action Thresholds
All business action thresholds are `null` in this draft because the assignment does not provide calibrated thresholds. Calibration owner: Account Service Lead.

### Owned enum
`metric_status`: draft / certified / deprecated
