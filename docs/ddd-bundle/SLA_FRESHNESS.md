# SLA Freshness

## Freshness Requirements per Dataset
`fact_customer_request` is refreshed when a valid CSV is uploaded. No periodic source refresh is specified.

## Delay Tolerance Matrix
Freshness tolerance: `null`; owner = Account Service Lead / Project Owner.

## Alert Rules
No numeric freshness alert thresholds are defined because none were supplied or calibrated.

## Escalation Procedures
If the latest upload fails validation, keep the previous valid snapshot and show the failure to the dashboard operator.

### Owned enum
`dataset_criticality`: values must be decided in this document when the project owner classifies the dataset; none are assigned in this draft.
