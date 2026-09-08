"""Tests for preprocessing."""

import pandas as pd

from src.preprocess import clean_table


def test_clean_table_normalizes_columns_and_deduplicates() -> None:
    data = pd.DataFrame({" Close Price ": [10, 10]})
    cleaned = clean_table(data)
    assert list(cleaned.columns) == ["close_price"]
    assert len(cleaned) == 1
