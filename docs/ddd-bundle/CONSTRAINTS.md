# Constraints

## Platform & Tooling Constraints
- Input: CSV upload.
- Local analytical storage: DuckDB.
- Application must expose an interactive dashboard and `request_type` filter.
- `reference_date`: `null`; source/owner = Project Owner / Assessor.

## Scale Constraints
- Observed source size: 12,022 rows, approximately 2.6 MB.
- 1-year projection: `null`; calibration owner = Project Owner.
- 3-year projection: `null`; calibration owner = Project Owner.

## Compliance & Residency Constraints
- Source uses synthetic-looking request titles and pseudonymous owners (`Owner-xx`), but the assignment does not state PDPA classification or residency requirements.
- Data residency: `null`; owner = Data Governance / Project Owner.
- Legal basis: `null`; owner = Data Governance / Project Owner.

## Project Budget & Timeline
- Delivery budget ceiling: `null`; owner = Project Owner.
- Go-live date: `null`; owner = Project Owner / Assessor.

## Integration Constraints
- Required source integration: CSV upload only.
- No external API integration is required by the supplied assignment.
