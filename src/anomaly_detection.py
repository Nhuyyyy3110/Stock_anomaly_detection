"""Z-score and KNN anomaly detection helpers."""

import pandas as pd
from sklearn.neighbors import LocalOutlierFactor


def zscore_flags(values: pd.Series, threshold: float = 3.0) -> pd.Series:
    """Flag values whose absolute standardized score exceeds a threshold."""
    scores = (values - values.mean()) / values.std(ddof=0)
    return scores.abs().gt(threshold)


def knn_flags(data: pd.DataFrame, contamination: float = 0.05) -> pd.Series:
    """Flag local outliers in a numeric feature frame."""
    model = LocalOutlierFactor(contamination=contamination)
    return pd.Series(model.fit_predict(data) == -1, index=data.index)
