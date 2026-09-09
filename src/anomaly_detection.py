"""Z-score and KNN anomaly detection helpers."""

import pandas as pd
from sklearn.neighbors import LocalOutlierFactor


def zscore_flags(values: pd.Series, threshold: float = 3.0) -> pd.Series:
    """Flag values whose absolute standardized score exceeds a threshold."""
    scores = (values - values.mean()) / values.std(ddof=0)
    return scores.abs().gt(threshold)


def rolling_zscore(values: pd.Series, window: int = 20) -> pd.Series:
    """Calculate a z-score against a trailing window of prior observations."""
    if window < 2:
        raise ValueError("window must be at least 2")

    history = values.shift(1).rolling(window, min_periods=window)
    history_mean = history.mean()
    history_std = history.std()
    return ((values - history_mean) / history_std).where(history_std.ne(0))


def knn_flags(data: pd.DataFrame, contamination: float = 0.05) -> pd.Series:
    """Flag local outliers in a numeric feature frame."""
    model = LocalOutlierFactor(contamination=contamination)
    return pd.Series(model.fit_predict(data) == -1, index=data.index)
