"""Data cleaning and normalization helpers."""

import pandas as pd


def clean_table(data: pd.DataFrame) -> pd.DataFrame:
    """Return a copy with normalized column names and duplicate rows removed."""
    cleaned = data.copy()
    cleaned.columns = [str(column).strip().lower().replace(" ", "_") for column in cleaned.columns]
    return cleaned.drop_duplicates().reset_index(drop=True)
