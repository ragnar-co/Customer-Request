import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import validate


def _df(rows):
    return pd.DataFrame(rows)


def test_valid_rows_are_accepted():
    df = _df(
        [
            {
                "request_id": "R1",
                "request_type": "assessment",
                "request_title": "T",
                "owner": "Owner-01",
                "due_date": "2025-01-01",
                "status": "open",
            }
        ]
    )
    result = validate.validate_csv(df)
    assert result.accepted
    assert result.row_count == 1


def test_missing_required_column_is_rejected():
    df = _df(
        [
            {
                "request_id": "R1",
                "request_type": "assessment",
                "owner": "Owner-01",
                "due_date": "2025-01-01",
                "status": "open",
            }
        ]
    )
    result = validate.validate_csv(df)
    assert not result.accepted
    assert any("request_title" in e for e in result.errors)


def test_duplicate_request_id_is_rejected():
    df = _df(
        [
            {
                "request_id": "R1",
                "request_type": "assessment",
                "request_title": "T1",
                "owner": "Owner-01",
                "due_date": "2025-01-01",
                "status": "open",
            },
            {
                "request_id": "R1",
                "request_type": "report",
                "request_title": "T2",
                "owner": "Owner-02",
                "due_date": "2025-01-02",
                "status": "done",
            },
        ]
    )
    result = validate.validate_csv(df)
    assert not result.accepted
    assert any("Duplicate" in e for e in result.errors)


def test_invalid_due_date_is_rejected():
    df = _df(
        [
            {
                "request_id": "R1",
                "request_type": "assessment",
                "request_title": "T",
                "owner": "Owner-01",
                "due_date": "01/01/2025",
                "status": "open",
            }
        ]
    )
    result = validate.validate_csv(df)
    assert not result.accepted
    assert any("due_date" in e for e in result.errors)


def test_unknown_status_is_rejected():
    df = _df(
        [
            {
                "request_id": "R1",
                "request_type": "assessment",
                "request_title": "T",
                "owner": "Owner-01",
                "due_date": "2025-01-01",
                "status": "cancelled",
            }
        ]
    )
    result = validate.validate_csv(df)
    assert not result.accepted
    assert any("status" in e for e in result.errors)


def test_unknown_request_type_is_rejected():
    df = _df(
        [
            {
                "request_id": "R1",
                "request_type": "incident",
                "request_title": "T",
                "owner": "Owner-01",
                "due_date": "2025-01-01",
                "status": "open",
            }
        ]
    )
    result = validate.validate_csv(df)
    assert not result.accepted
    assert any("request_type" in e for e in result.errors)


def test_null_required_field_is_rejected():
    df = _df(
        [
            {
                "request_id": "R1",
                "request_type": "assessment",
                "request_title": "",
                "owner": "Owner-01",
                "due_date": "2025-01-01",
                "status": "open",
            }
        ]
    )
    result = validate.validate_csv(df)
    assert not result.accepted


def test_whitespace_is_stripped_from_all_fields():
    df = _df(
        [
            {
                "request_id": "  R1  ",
                "request_type": " assessment ",
                "request_title": "  T  ",
                "owner": "  Owner-01  ",
                "due_date": " 2025-01-01 ",
                "status": " open ",
            }
        ]
    )
    result = validate.validate_csv(df)
    assert result.accepted, result.errors
    row = result.dataframe.iloc[0]
    assert row["request_id"] == "R1"
    assert row["request_type"] == "assessment"
    assert row["request_title"] == "T"
    assert row["owner"] == "Owner-01"
    assert row["status"] == "open"


def test_whitespace_variants_of_same_id_are_duplicates():
    df = _df(
        [
            {
                "request_id": "R1",
                "request_type": "assessment",
                "request_title": "T1",
                "owner": "Owner-01",
                "due_date": "2025-01-01",
                "status": "open",
            },
            {
                "request_id": "R1 ",
                "request_type": "report",
                "request_title": "T2",
                "owner": "Owner-02",
                "due_date": "2025-01-02",
                "status": "done",
            },
        ]
    )
    result = validate.validate_csv(df)
    assert not result.accepted
    assert any("Duplicate" in e for e in result.errors)


def test_case_variant_values_are_still_rejected():
    # Confirms case normalization is intentionally NOT applied (Project
    # Owner decision, documented in DATA_QUALITY.md).
    df = _df(
        [
            {
                "request_id": "R1",
                "request_type": "Assessment",
                "request_title": "T",
                "owner": "Owner-01",
                "due_date": "2025-01-01",
                "status": "Done",
            }
        ]
    )
    result = validate.validate_csv(df)
    assert not result.accepted
    assert any("request_type" in e for e in result.errors)
    assert any("status" in e for e in result.errors)
