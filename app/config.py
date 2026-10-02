"""Fixed project configuration.

Per CONSTRAINTS.md / METRIC_LOGIC.md: reference_date must be a single fixed,
configured value — never the live system clock — so that "overdue" results
are reproducible. It may be set explicitly via APP_REFERENCE_DATE (.env);
absent that, it falls back to the confirmed assignment default below —
never to datetime.now()/date.today().
"""
import os
from datetime import date, datetime
from pathlib import Path

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

PROJECT_ROOT = Path(__file__).resolve().parent.parent

_DEFAULT_REFERENCE_DATE = date(2026, 10, 2)
_env_reference_date = os.environ.get("APP_REFERENCE_DATE")
REFERENCE_DATE = (
    datetime.strptime(_env_reference_date, "%Y-%m-%d").date()
    if _env_reference_date
    else _DEFAULT_REFERENCE_DATE
)

REQUIRED_COLUMNS = [
    "request_id",
    "request_type",
    "request_title",
    "owner",
    "due_date",
    "status",
]

# Approved source contract (DATA_QUALITY.md). Values outside these sets are
# rejected during validation rather than silently coerced.
VALID_REQUEST_TYPES = {"assessment", "report", "clarification"}
VALID_STATUSES = {"done", "in_progress", "open"}

# Display-only labels for request_type (UI presentation, not a data remap —
# underlying values/filters still operate on the raw request_type strings).
SERVICE_TYPE_LABELS = {
    "assessment": "Vulnerability Assessment",
    "report": "Security Report",
    "clarification": "Support",
}

DB_PATH = os.environ.get("APP_DB_PATH", str(PROJECT_ROOT / "output" / "customer_requests.duckdb"))
