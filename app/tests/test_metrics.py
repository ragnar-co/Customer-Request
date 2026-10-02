import sys
from datetime import date
from pathlib import Path

import duckdb
import pandas as pd
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import db
import metrics
import validate

# Test-only fixed reference date — must never be reused as the production
# assignment reference_date (TESTING_STRATEGY.md).
TEST_REFERENCE_DATE = date(2025, 1, 10)

FIXTURE_PATH = Path(__file__).resolve().parent / "fixtures" / "golden_fixture.csv"


@pytest.fixture
def loaded_db(tmp_path):
    db_path = str(tmp_path / "test.duckdb")
    raw_df = pd.read_csv(FIXTURE_PATH, dtype=str)
    result = validate.validate_csv(raw_df)
    assert result.accepted, result.errors
    db.load_snapshot(result.dataframe, db_path=db_path)
    return db_path


def test_total_equals_accepted_row_count(loaded_db):
    assert metrics.get_total_requests(db_path=loaded_db) == 6


def test_completed_only_counts_done(loaded_db):
    assert metrics.get_completed_requests(db_path=loaded_db) == 2


def test_overdue_excludes_done(loaded_db):
    # REQ-006 is done with a due_date far in the past; must not count as overdue.
    overdue = metrics.get_overdue_requests(reference_date=TEST_REFERENCE_DATE, db_path=loaded_db)
    assert overdue == 2  # REQ-002, REQ-005


def test_due_date_equal_reference_date_is_not_overdue(loaded_db):
    detail = metrics.get_overdue_detail(reference_date=TEST_REFERENCE_DATE, db_path=loaded_db)
    assert "REQ-003" not in detail["request_id"].tolist()


def test_days_overdue_matches_calendar_diff(loaded_db):
    detail = metrics.get_overdue_detail(reference_date=TEST_REFERENCE_DATE, db_path=loaded_db)
    by_id = detail.set_index("request_id")["days_overdue"].to_dict()
    assert by_id["REQ-002"] == 5
    assert by_id["REQ-005"] == 21


def test_request_type_filter_is_consistent(loaded_db):
    total_assessment = metrics.get_total_requests("assessment", db_path=loaded_db)
    completed_assessment = metrics.get_completed_requests("assessment", db_path=loaded_db)
    overdue_assessment = metrics.get_overdue_requests(
        "assessment", reference_date=TEST_REFERENCE_DATE, db_path=loaded_db
    )
    assert total_assessment == 2
    assert completed_assessment == 1
    assert overdue_assessment == 1


def test_owner_filter_restricts_overdue_detail(loaded_db):
    # Owner-01 owns REQ-001 (done, not overdue) and REQ-006 (done, not overdue);
    # neither should appear in the overdue detail for Owner-01.
    detail = metrics.get_overdue_detail(
        owner="Owner-01", reference_date=TEST_REFERENCE_DATE, db_path=loaded_db
    )
    assert detail.empty

    detail_owner_02 = metrics.get_overdue_detail(
        owner="Owner-02", reference_date=TEST_REFERENCE_DATE, db_path=loaded_db
    )
    assert detail_owner_02["request_id"].tolist() == ["REQ-002"]


def test_reupload_same_file_is_idempotent(loaded_db):
    raw_df = pd.read_csv(FIXTURE_PATH, dtype=str)
    result = validate.validate_csv(raw_df)
    before = metrics.get_total_requests(db_path=loaded_db)
    db.load_snapshot(result.dataframe, db_path=loaded_db)
    after = metrics.get_total_requests(db_path=loaded_db)
    assert before == after == 6


def test_request_id_has_db_level_primary_key(loaded_db):
    con = duckdb.connect(loaded_db, read_only=True)
    try:
        constraints = con.execute(
            "SELECT constraint_type, constraint_column_names "
            "FROM duckdb_constraints() WHERE table_name = 'fact_customer_request'"
        ).fetchall()
    finally:
        con.close()
    pk_constraints = [c for c in constraints if c[0] == "PRIMARY KEY"]
    assert pk_constraints, f"expected a PRIMARY KEY constraint, found: {constraints}"
    assert pk_constraints[0][1] == ["request_id"]


def test_duplicate_request_id_violates_db_constraint_on_direct_insert():
    # Bypasses validate.py entirely to prove the constraint is enforced by
    # DuckDB itself, not only by the application validation layer.
    import tempfile
    import os

    fd, path = tempfile.mkstemp(suffix=".duckdb")
    os.close(fd)
    os.remove(path)
    try:
        con = duckdb.connect(path)
        con.execute(
            """
            CREATE TABLE fact_customer_request (
                request_id VARCHAR PRIMARY KEY,
                request_type VARCHAR NOT NULL,
                request_title VARCHAR NOT NULL,
                owner VARCHAR NOT NULL,
                due_date DATE NOT NULL,
                status VARCHAR NOT NULL,
                loaded_at TIMESTAMP WITH TIME ZONE NOT NULL
            )
            """
        )
        con.execute(
            "INSERT INTO fact_customer_request VALUES "
            "('R1', 'assessment', 'T', 'Owner-01', '2025-01-01', 'open', now())"
        )
        with pytest.raises(duckdb.ConstraintException):
            con.execute(
                "INSERT INTO fact_customer_request VALUES "
                "('R1', 'report', 'T2', 'Owner-02', '2025-01-02', 'done', now())"
            )
        con.close()
    finally:
        if os.path.exists(path):
            os.remove(path)
