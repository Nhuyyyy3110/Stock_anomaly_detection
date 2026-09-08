"""Tests for feature engineering."""

import pandas as pd

from src.features import add_return_feature


def test_add_return_feature() -> None:
    result = add_return_feature(pd.DataFrame({"close": [100, 110]}))
    assert result["return"].iloc[1] == 0.1
