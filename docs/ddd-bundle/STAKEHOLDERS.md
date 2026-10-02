# Data Stakeholders

## Stakeholder Profiles

### Account Coordinator / Dashboard User
- team: Customer Account / Cybersecurity Coordination
- data_literacy_level: basic
- critical_questions:
  - How many customer requests exist, are completed, and are overdue?
  - Which service type has pending follow-up?
  - Which overdue request should be followed up and with whom?
- pain_points: weekly status gathering is manual and fragmented.
- preferred_format: interactive dashboard
- decision_cadence: weekly, before customer update meeting

### Internal Service Owner
- team: Cybersecurity Delivery
- data_literacy_level: basic
- critical_questions: Which overdue requests are assigned to me and how many days late are they?
- preferred_format: filtered table
- decision_cadence: weekly / as requested by account coordinator

## Data Needs Matrix

| Stakeholder | Data need | data_need_priority | Freshness requirement |
|---|---|---|---|
| Account Coordinator | total/completed/overdue counts | P0 | Refresh on each accepted CSV import |
| Account Coordinator | breakdown by `request_type` | P0 | Refresh on each accepted CSV import |
| Account Coordinator | overdue detail with `owner` and `days_overdue` | P0 | Refresh on each accepted CSV import |
| Internal Service Owner | assigned overdue requests | P1 | Refresh on each accepted CSV import |

### Owned enums
`data_literacy_level`: basic / intermediate / advanced  
`data_need_priority`: P0 / P1 / P2
