# Business Glossary

## Term Definitions

| Term | Official definition | Common misunderstanding | Authoritative source |
|---|---|---|---|
| Customer Request | One row identified by `request_id` in the accepted CSV | Treating repeated titles as the same request | Source CSV schema |
| Service Type | `request_type` used to segment/filter requests | Confusing service type with status | Source CSV schema |
| Completed Request | Request whose source `status` is `done` | Treating any past-due request as incomplete after it is done | Source CSV observed values + assignment intent |
| Overdue Request | Request not completed and with `due_date < reference_date` | Using the runtime date instead of the assignment reference date | Assignment requirement |
| Days Overdue | Calendar-day difference `reference_date - due_date` for an overdue request | Showing negative values for requests not overdue | Metric definition in this project |
| Owner | Value in source `owner` column identifying the follow-up responsible party | Treating owner as customer identity | Source CSV schema |

## Disputed Terms
No approved disputed-term resolutions were supplied. Do not invent approval dates or resolutions.

## Change Log
No glossary changes recorded yet.

## Enumeration Registry

| Enum name | Owner document |
|---|---|
| `data_literacy_level` | STAKEHOLDERS.md |
| `data_need_priority` | STAKEHOLDERS.md |
| `metric_status` | METRIC_SPEC.md |
| `rule_severity` | DATA_QUALITY.md |
| `dataset_criticality` | SLA_FRESHNESS.md |
| `chart_type` | VIZ_DESIGN_SPEC.md |
| `complexity_level` | VIZ_DESIGN_SPEC.md |
| `incident_severity` | RUNBOOK.md |
| `work_item_status` | TASKS.md |

Registry rule: this table indexes enum ownership only; values are defined only in owner documents.
