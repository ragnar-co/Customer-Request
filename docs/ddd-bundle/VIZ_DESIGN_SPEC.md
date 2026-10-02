# Visualization Design Spec

## Chart Type Matrix
| Information | chart_type | Reason |
|---|---|---|
| Total / Completed / Overdue | KPI card | Fast meeting scan |
| Request counts by service type | bar | Compare independent categories |
| Overdue request detail | table | Requires request-level owner and days late |

## Color & Theme Spec
Use the application default accessible theme. Do not encode status by color alone.

## Interaction Spec
- single-select `request_type` filter plus All.
- filter applies to all cards, breakdown, and overdue detail.
- overdue table can sort by `days_overdue` descending.

## Accessibility Guidelines
- labels include text, not only color.
- table headers explicit.
- keyboard-accessible filter and table controls.

## Data Literacy Guard Rails
Audience is basic; use basic visualizations only.

### Owned enums
`chart_type`: project-defined by the matrix above.  
`complexity_level`: basic / intermediate / advanced.
