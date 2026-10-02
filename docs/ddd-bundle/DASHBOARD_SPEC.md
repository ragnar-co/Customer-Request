# Dashboard Spec

## Dashboard Inventory
`dashboard_customer_request_followup` — one-page weekly follow-up dashboard for the account coordinator.

## Dashboard Profiles
Components:
1. KPI card: Total Requests
2. KPI card: Completed Requests
3. KPI card: Overdue Requests
4. Bar chart/table: counts by `request_type`
5. Overdue detail table: `request_id`, `request_type`, `request_title`, `owner`, `due_date`, `days_overdue`
6. Filter: `request_type` with All option

Acceptance: all components derive from canonical metrics in METRIC_LOGIC.md; no metric formula is reimplemented independently in the UI.

## Metric Coverage Matrix
| Dashboard component | Metric |
|---|---|
| Total card | `metric_total_requests` |
| Completed card | `metric_completed_requests` |
| Overdue card | `metric_overdue_requests` |
| Overdue table | `metric_days_overdue` + request attributes |

## Drill-down Logic
Selecting a service type filters cards and detail rows to that type. Selecting All removes only the service-type predicate.

## Refresh Schedule
Refresh after each successful CSV ingestion. Performance budget: `null`; calibration owner = Engineering Lead.
