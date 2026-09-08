"""Tests for anomaly detection."""

import pandas as pd

from src.anomaly_detection import zscore_flags


def test_zscore_flags_returns_boolean_series() -> None:
    result = zscore_flags(pd.Series([1, 1, 1, 10]), threshold=1.0)
    assert result.dtype == bool
    assert result.iloc[-1]
