import os

import pandas as pd
import streamlit as st

import db
import metrics
import validate
from config import DB_PATH, REFERENCE_DATE, SERVICE_TYPE_LABELS, VALID_REQUEST_TYPES

st.set_page_config(page_title="Customer Request Follow-up Dashboard", layout="wide")

os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

st.title("Customer Request Follow-up Dashboard")
st.caption(
    f"Fixed assignment reference date: **{REFERENCE_DATE.isoformat()}** "
    "(configured constant, not the live system date)"
)

with st.expander("Upload CSV", expanded=not metrics.table_exists()):
    uploaded = st.file_uploader("Upload customer request CSV", type="csv")
    if uploaded is not None:
        try:
            raw_df = pd.read_csv(uploaded, dtype=str)
        except Exception as e:
            st.error(f"Could not parse file as CSV: {e}")
            raw_df = None

        if raw_df is not None:
            result = validate.validate_csv(raw_df)
            if not result.accepted:
                st.error(
                    f"Validation failed — {result.row_count} row(s) submitted, upload rejected. "
                    "Previous dataset unchanged."
                )
                for err in result.errors:
                    st.write(f"- {err}")
            else:
                loaded = db.load_snapshot(result.dataframe)
                st.success(
                    f"Validation passed. {loaded} row(s) accepted and loaded into DuckDB "
                    "(snapshot replaced)."
                )

if not metrics.table_exists():
    st.info("No dataset loaded yet. Upload a validated CSV to populate the dashboard.")
    st.stop()

st.divider()

sorted_types = sorted(VALID_REQUEST_TYPES)
type_label_by_value = {t: SERVICE_TYPE_LABELS.get(t, t) for t in sorted_types}
type_value_by_label = {v: k for k, v in type_label_by_value.items()}
type_options = ["All"] + [type_label_by_value[t] for t in sorted_types]

selected_type_label = st.selectbox("Service Type", type_options)
filter_value = None if selected_type_label == "All" else type_value_by_label[selected_type_label]

col1, col2, col3 = st.columns(3)
col1.metric("Total Requests", metrics.get_total_requests(filter_value))
col2.metric("Completed Requests", metrics.get_completed_requests(filter_value))
col3.metric("Overdue Requests", metrics.get_overdue_requests(filter_value))

st.subheader("Requests by Service Type")
breakdown = metrics.get_breakdown_by_type()
breakdown = breakdown.assign(
    request_type=breakdown["request_type"].map(lambda t: SERVICE_TYPE_LABELS.get(t, t))
).rename(columns={"request_type": "Service Type"})
st.bar_chart(breakdown.set_index("Service Type")[["total", "completed", "overdue"]])
st.dataframe(breakdown, use_container_width=True, hide_index=True)

st.subheader("Overdue Request Detail")
owners = ["All"] + metrics.get_owners()
selected_owner = st.selectbox("Owner", owners)
owner_filter_value = None if selected_owner == "All" else selected_owner

detail = metrics.get_overdue_detail(filter_value, owner_filter_value)
detail = detail.assign(
    request_type=detail["request_type"].map(lambda t: SERVICE_TYPE_LABELS.get(t, t))
)
st.dataframe(
    detail.rename(
        columns={
            "request_id": "Request ID",
            "request_type": "Service Type",
            "request_title": "Title",
            "owner": "Owner",
            "due_date": "Due Date",
            "days_overdue": "Days Overdue",
        }
    ),
    use_container_width=True,
    hide_index=True,
)
