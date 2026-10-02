# Report Spec

## Scope note

This project has exactly one "report": the interactive dashboard itself (`dashboard_customer_request_followup`, defined in `DASHBOARD_SPEC.md`). No separate scheduled/exported report (PDF, email digest, etc.) exists or has been requested. This document records that scope honestly rather than inventing a distribution mechanism that was never built.

## Report Profiles

| Report Name | Format | Frequency | Target Audience |
|---|---|---|---|
| Customer Request Follow-up Dashboard | Interactive web app (Streamlit, `app/app.py`) | On-demand (viewed live before each weekly customer update meeting — see `STAKEHOLDERS.md` decision_cadence) | Account Coordinator (primary), Internal Service Owner (via Owner filter) |

No PDF export, scheduled email, or Zoho Analytics distribution exists. Format: `null` beyond the interactive app; owner = Project Owner if a static/scheduled export is later required.

## KPI Coverage

| KPI / Metric | Covered by Dashboard? |
|---|---|
| `metric_total_requests` | Yes — Total Requests KPI card |
| `metric_completed_requests` | Yes — Completed Requests KPI card |
| `metric_overdue_requests` | Yes — Overdue Requests KPI card |
| `metric_days_overdue` | Yes — Overdue Request Detail table |

Coverage matrix: all four metrics in `METRIC_SPEC.md` / `KPI_DICTIONARY.md`'s single KPI ("Customer Request Follow-up Readiness") are covered by the one dashboard. Missing coverage: none — there is only one KPI in scope and it is fully covered.

## Distribution Schedule

- Distribution channel: none — the dashboard is accessed directly (local `streamlit run` or the Docker container's exposed port), not pushed to users.
- Deadline: `null`; not applicable, since there is no scheduled generation step to have a deadline.
- Distribution list: `null`; owner = Account Service Lead. Access is currently open to whoever can reach the running app (see `DATA_GOVERNANCE.md`'s Access Control Policy — no authentication layer exists).

## Template Definitions

- Template layout: single page — KPI cards (Total / Completed / Overdue) → Requests by Service Type (bar chart + table) → Overdue Request Detail (filterable table), as defined in `DASHBOARD_SPEC.md`'s Dashboard Profiles.
- Chart types: KPI card, bar chart, table — per `VIZ_DESIGN_SPEC.md`'s Chart Type Matrix. No additional chart types are used.
- Branding: `null`; uses Streamlit's default theme (`VIZ_DESIGN_SPEC.md`: "Use the application default accessible theme"). No custom logo, color scheme, or header/footer has been requested.
