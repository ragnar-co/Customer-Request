# Tasks

## Task Breakdown
| Task ID | Work item | Dependency |
|---|---|---|
| T-001 | Implement CSV schema/value validation | none |
| T-002 | Create DuckDB `fact_customer_request` load | T-001 |
| T-003 | Implement canonical metric queries | T-002 |
| T-004 | Implement `request_type` filter | T-003 |
| T-005 | Build KPI cards and service-type breakdown | T-003 |
| T-006 | Build overdue detail table | T-003 |
| T-007 | Add golden-fixture metric tests | T-003 |
| T-008 | Add upload integration/idempotency tests | T-002 |
| T-009 | Validate dashboard acceptance criteria | T-004,T-005,T-006,T-007 |
| T-010 | Configure assignment `reference_date` | Project Owner input |

## Task Sequence and Dependencies
Validation -> storage -> metric logic -> dashboard/filter -> tests -> acceptance.

## Definition of Done
- valid CSV accepted and invalid CSV rejected with diagnostics.
- DuckDB snapshot is atomic and idempotent.
- dashboard shows Total, Completed, Overdue.
- service-type filter applies consistently.
- overdue rows show owner and days overdue.
- fixed assignment reference date is configured and tested.
- automated tests pass.

## Assignments and Estimates
Assignments and estimates: `null`; owner = Engineering Lead / Project Owner.

### Owned enum
`work_item_status`: not started / in progress / done
