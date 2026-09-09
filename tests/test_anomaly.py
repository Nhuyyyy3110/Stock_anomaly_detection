"""Tests for anomaly detection."""

import pandas as pd

from src.anomaly_detection import rolling_zscore, zscore_flags


def test_zscore_flags_returns_boolean_series() -> None:
    result = zscore_flags(pd.Series([1, 1, 1, 10]), threshold=1.0)
    assert result.dtype == bool
    assert result.iloc[-1]


def test_rolling_zscore_uses_only_prior_observations() -> None:
    values = pd.Series([1.0, 2.0, 3.0, 100.0])

    result = rolling_zscore(values, window=3)

    assert result.iloc[:3].isna().all()
    assert result.iloc[3] == 98.0


def test_rolling_zscore_rejects_invalid_window() -> None:
    try:
        rolling_zscore(pd.Series([1.0, 2.0]), window=1)
    except ValueError as error:
        assert str(error) == "window must be at least 2"
    else:
        raise AssertionError("Expected rolling_zscore to reject window=1")
