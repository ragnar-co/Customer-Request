"""Canonical metric queries, ported 1:1 from METRIC_LOGIC.md.

No metric formula is reimplemented independently anywhere else (dashboard
UI, tests) — everything reads through these functions.
"""
import duckdb

from config import DB_PATH, REFERENCE_DATE


def _connect(db_path):
    return duckdb.connect(db_path)


def _type_filter(request_type):
    if request_type and request_type != "All":
        return "AND request_type = ?", [request_type]
    return "", []


def _owner_filter(owner):
    if owner and owner != "All":
        return "AND owner = ?", [owner]
    return "", []


def get_owners(db_path: str = DB_PATH):
    con = _connect(db_path)
    try:
        rows = con.execute(
            "SELECT DISTINCT owner FROM fact_customer_request ORDER BY owner"
        ).fetchall()
        return [r[0] for r in rows]
    finally:
        con.close()


def table_exists(db_path: str = DB_PATH) -> bool:
    con = _connect(db_path)
    try:
        row = con.execute(
            "SELECT COUNT(*) FROM information_schema.tables WHERE table_name = 'fact_customer_request'"
        ).fetchone()
        return row[0] > 0
    finally:
        con.close()


def get_total_requests(request_type=None, db_path: str = DB_PATH) -> int:
    con = _connect(db_path)
    try:
        clause, params = _type_filter(request_type)
        sql = f"SELECT COUNT(*) FROM fact_customer_request WHERE 1=1 {clause}"
        return con.execute(sql, params).fetchone()[0]
    finally:
        con.close()


def get_completed_requests(request_type=None, db_path: str = DB_PATH) -> int:
    con = _connect(db_path)
    try:
        clause, params = _type_filter(request_type)
        sql = f"SELECT COUNT(*) FROM fact_customer_request WHERE status = 'done' {clause}"
        return con.execute(sql, params).fetchone()[0]
    finally:
        con.close()


def get_overdue_requests(request_type=None, reference_date=REFERENCE_DATE, db_path: str = DB_PATH) -> int:
    con = _connect(db_path)
    try:
        clause, extra = _type_filter(request_type)
        sql = f"""
            SELECT COUNT(*) FROM fact_customer_request
            WHERE status <> 'done' AND due_date < CAST(? AS DATE) {clause}
        """
        return con.execute(sql, [reference_date] + extra).fetchone()[0]
    finally:
        con.close()


def get_breakdown_by_type(reference_date=REFERENCE_DATE, db_path: str = DB_PATH):
    con = _connect(db_path)
    try:
        return con.execute(
            """
            SELECT request_type,
                   COUNT(*) AS total,
                   COUNT(*) FILTER (WHERE status = 'done') AS completed,
                   COUNT(*) FILTER (WHERE status <> 'done' AND due_date < CAST(? AS DATE)) AS overdue
            FROM fact_customer_request
            GROUP BY request_type
            ORDER BY request_type
            """,
            [reference_date],
        ).df()
    finally:
        con.close()


def get_overdue_detail(request_type=None, owner=None, reference_date=REFERENCE_DATE, db_path: str = DB_PATH):
    con = _connect(db_path)
    try:
        type_clause, type_params = _type_filter(request_type)
        owner_clause, owner_params = _owner_filter(owner)
        sql = f"""
            SELECT request_id, request_type, request_title, owner, due_date,
                   DATE_DIFF('day', due_date, CAST(? AS DATE)) AS days_overdue
            FROM fact_customer_request
            WHERE status <> 'done' AND due_date < CAST(? AS DATE) {type_clause} {owner_clause}
            ORDER BY days_overdue DESC, request_id
        """
        params = [reference_date, reference_date] + type_params + owner_params
        return con.execute(sql, params).df()
    finally:
        con.close()


def get_row_count(db_path: str = DB_PATH) -> int:
    con = _connect(db_path)
    try:
        return con.execute("SELECT COUNT(*) FROM fact_customer_request").fetchone()[0]
    finally:
        con.close()
