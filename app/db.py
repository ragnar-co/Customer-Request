"""DuckDB snapshot loader (PIPELINE_SPEC.md).

Full-snapshot replace: the table is recreated with an explicit schema
(PRIMARY KEY on request_id) and repopulated inside a single transaction, so
a failed load rolls back and never leaves a partially-written table or a
schema without the uniqueness constraint. Re-loading the same valid file is
idempotent.
"""
from datetime import datetime, timezone

import duckdb
import pandas as pd

from config import DB_PATH

_SCHEMA_SQL = """
    CREATE OR REPLACE TABLE fact_customer_request (
        request_id VARCHAR PRIMARY KEY,
        request_type VARCHAR NOT NULL,
        request_title VARCHAR NOT NULL,
        owner VARCHAR NOT NULL,
        due_date DATE NOT NULL,
        status VARCHAR NOT NULL,
        loaded_at TIMESTAMP WITH TIME ZONE NOT NULL
    )
"""


def load_snapshot(df: pd.DataFrame, db_path: str = DB_PATH) -> int:
    df = df.copy()
    df["loaded_at"] = datetime.now(timezone.utc)
    con = duckdb.connect(db_path)
    try:
        con.execute("BEGIN TRANSACTION")
        con.execute(_SCHEMA_SQL)
        con.execute("INSERT INTO fact_customer_request SELECT * FROM df")
        con.execute("COMMIT")
    except Exception:
        con.execute("ROLLBACK")
        raise
    finally:
        con.close()
    return len(df)
