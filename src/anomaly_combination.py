"""Combine anomaly outputs from multiple detection methods."""

from __future__ import annotations

import pandas as pd


def combine_anomaly_flags(
    data: pd.DataFrame,
    zscore_column: str = "zscore_anomaly",
    knn_column: str = "knn_anomaly",
    output_column: str = "final_anomaly",
) -> pd.DataFrame:
    """Create a final anomaly flag when either configured detector flags a row."""
    result = data.copy()
    result[output_column] = result[[zscore_column, knn_column]].any(axis=1)
    return result
