# Runbook

## Common Failure Scenarios
1. Missing required CSV column.
2. Duplicate `request_id`.
3. Invalid `due_date`.
4. Unknown `status` / `request_type` relative to approved contract.
5. Missing configured `reference_date`.

## Triage Checklist
- capture validation error.
- identify file and row/column.
- verify previous valid snapshot is still active.
- verify reference date configuration separately from source data.

## Recovery Procedures
Correct the source/configuration and re-upload. Re-run validation before replacing the dataset. Verify row count and KPI cards after recovery.

## Escalation Contacts
- data/input issue: Project Owner / Account Service Lead
- application/storage issue: Engineering Lead
- governance issue: Data Governance owner

## Post-Incident Review
Record date, trigger, impact, root cause, fix, verification, and prevention action.

## Retention Enforcement & Archival
Retention period: `null`; owner = Data Governance / Project Owner. No purge schedule is defined until that value is approved.

### Owned enum
`incident_severity`: SEV1 / SEV2 / SEV3
