"""CSV schema and value validation (DATA_QUALITY.md).

Checks: required columns, non-null/non-empty completeness, request_id
uniqueness, due_date ISO format, and request_type/status against the
approved contract. A failing file is rejected outright — the caller must
keep the previous valid snapshot in place (PIPELINE_SPEC.md).
"""
from dataclasses import dataclass, field

import pandas as pd

from config import REQUIRED_COLUMNS, VALID_REQUEST_TYPES, VALID_STATUSES

MAX_EXAMPLES = 20


@dataclass
class ValidationResult:
    accepted: bool
    row_count: int = 0
    errors: list = field(default_factory=list)
    dataframe: pd.DataFrame = None


def validate_csv(df: pd.DataFrame) -> ValidationResult:
    row_count = len(df)
    errors = []

    missing_cols = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing_cols:
        errors.append(f"Missing required column(s): {', '.join(missing_cols)}")
        return ValidationResult(accepted=False, row_count=row_count, errors=errors)

    df = df[REQUIRED_COLUMNS].copy()

    # Whitespace normalization: strip leading/trailing whitespace on every
    # required column before any completeness/uniqueness/contract check, so
    # " assessment " / "R1 " are treated identically to "assessment" / "R1".
    # NaN-safe: pandas' .str accessor propagates missing values untouched.
    for col in REQUIRED_COLUMNS:
        df[col] = df[col].str.strip()

    null_masks = {}
    for col in REQUIRED_COLUMNS:
        mask = df[col].isna() | (df[col].astype(str).str.strip() == "")
        null_masks[col] = mask
        if mask.any():
            rows = [i + 2 for i in df.index[mask].tolist()[:MAX_EXAMPLES]]
            errors.append(
                f"Column '{col}' has {int(mask.sum())} null/empty value(s), e.g. CSV row(s) {rows}"
            )

    dup_mask = df["request_id"].duplicated(keep=False) & ~null_masks["request_id"]
    if dup_mask.any():
        dup_ids = sorted(df.loc[dup_mask, "request_id"].unique().tolist())[:MAX_EXAMPLES]
        errors.append(f"Duplicate 'request_id' value(s) found: {dup_ids}")

    parsed_dates = pd.to_datetime(df["due_date"], format="%Y-%m-%d", errors="coerce")
    bad_date_mask = parsed_dates.isna() & ~null_masks["due_date"]
    if bad_date_mask.any():
        rows = [i + 2 for i in df.index[bad_date_mask].tolist()[:MAX_EXAMPLES]]
        errors.append(
            f"Column 'due_date' has {int(bad_date_mask.sum())} value(s) not matching ISO YYYY-MM-DD, e.g. CSV row(s) {rows}"
        )

    # Case is intentionally NOT normalized here: "Assessment"/"Done" are
    # rejected rather than silently folded to "assessment"/"done" (decision
    # confirmed with Project Owner — see DATA_QUALITY.md "Case Normalization
    # Policy"). This matches the project's "do not coerce silently" rule.
    bad_type_mask = ~df["request_type"].isin(VALID_REQUEST_TYPES) & ~null_masks["request_type"]
    if bad_type_mask.any():
        bad_vals = sorted(df.loc[bad_type_mask, "request_type"].unique().tolist())[:MAX_EXAMPLES]
        errors.append(
            f"Column 'request_type' has value(s) outside the approved contract {sorted(VALID_REQUEST_TYPES)}: {bad_vals}"
        )

    bad_status_mask = ~df["status"].isin(VALID_STATUSES) & ~null_masks["status"]
    if bad_status_mask.any():
        bad_vals = sorted(df.loc[bad_status_mask, "status"].unique().tolist())[:MAX_EXAMPLES]
        errors.append(
            f"Column 'status' has value(s) outside the approved contract {sorted(VALID_STATUSES)}: {bad_vals}"
        )

    if errors:
        return ValidationResult(accepted=False, row_count=row_count, errors=errors)

    df["due_date"] = parsed_dates.dt.date
    return ValidationResult(accepted=True, row_count=row_count, dataframe=df)
