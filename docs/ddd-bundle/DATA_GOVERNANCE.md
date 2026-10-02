# Data Governance Spec

## Data Ownership Matrix

| Dataset | Data Owner | Data Steward | Escalation Contact |
|---|---|---|---|
| `fact_customer_request` | Account Service Lead (per KPI_DICTIONARY.md KPI ownership) | Engineering Lead | Project Owner |

No named individuals were supplied for these roles; the role titles above are the same ones already used consistently across `KPI_DICTIONARY.md`, `METRIC_SPEC.md`, and `RUNBOOK.md`. Named-person assignment: `null`; owner = Project Owner.

## Access Control Policy

- Role definitions: `null`; this project has no deployed authentication/authorization layer. The application (`app/app.py`) is a single-user local/Docker Streamlit app with no login, no role separation, and no per-user query restriction.
- Role × dataset access matrix: `null`; owner = Engineering Lead, required before any multi-user or hosted deployment.
- Sensitive data access request process: `null`; owner = Data Governance / Project Owner. No process is required today because no field has been classified as sensitive (see PDPA/PII Classification below), but this must be defined before classification changes that result.

## PDPA and PII Classification

| Column | Classification | Rationale |
|---|---|---|
| `request_id` | `null` (pending) | Synthetic identifier (`Qxxxxxx` pattern); classification not yet approved by Data Governance. |
| `request_type` | Not personal data | Enum value (`assessment` / `report` / `clarification`), carries no individual identity. |
| `request_title` | `null` (pending) | Free text; observed source values are generic/synthetic Thai operational phrases referencing anonymized organization numbers (e.g. "หน่วยงานสมมติ 680"), not customer names. Still requires formal governance sign-off before being treated as definitely non-personal. |
| `owner` | `null` (pending) | Pseudonymous internal assignee label (`Owner-NN`); likely maps to an internal staff member, not a customer. Classification not yet approved. |
| `due_date` | Not personal data | Operational date field. |
| `status` | Not personal data | Enum value. |

This is unchanged from the open item already recorded in `DATA_MODEL_SPEC.md`: **no field has an approved PDPA classification**. The table above records the current best-effort reading of the observed data, not an approved classification — approval remains owned by Data Governance / Project Owner.

- Masking/anonymization: `null`; not implemented. No masking exists in `app/app.py` or `app/metrics.py` — all accepted rows, including `owner` and `request_title`, are shown as-is to anyone who can reach the Streamlit UI.
- Legal basis for retention: `null`; owner = Data Governance / Project Owner (same open item as `CONSTRAINTS.md`'s Compliance & Residency Constraints).

## Data Retention Policy

- Retention period: `null`; owner = Data Governance / Project Owner. Same unresolved item already recorded in `RUNBOOK.md` ("Retention Enforcement & Archival"). No change since that document was written.
- Deletion procedure: `null`; not implemented. The application has no scheduled or manual delete/purge capability — each CSV upload fully replaces the prior snapshot (`app/db.py`), but there is no retention-driven deletion.
- Archival policy: `null`; owner = Data Governance / Project Owner.

## Audit Requirements

- Access logging: `null`; not implemented. No query-level audit log exists.
- Change logging: Partially implemented — every load records a `loaded_at` timestamp on the full snapshot (`app/db.py`), which tells you *when* the current snapshot was loaded, but not what changed between snapshots (no diff/change-event log).
- Audit review cadence: `null`; owner = Data Governance / Project Owner.

## Cost Governance

- Monthly compute budget: `null`; owner = Project Owner. Not applicable at current scale — this is a local/single-container DuckDB file, not a hosted warehouse with metered queries.
- Cost monitoring dashboard/alerts: `null`; not applicable at current scale.
- Query cost guard rails: `null`; not applicable — DuckDB here runs embedded, in-process, against a ~2.6 MB snapshot.
- Cost attribution: `null`; not applicable, no shared/metered infrastructure exists yet.

### Owned enums
`pii_classification_level`: pending / not_personal_data / personal_data / sensitive_personal_data (values used informally above; no approved enum registry exists yet — ownership stays with Data Governance per `BUSINESS_GLOSSARY.md`'s Enumeration Registry convention).
