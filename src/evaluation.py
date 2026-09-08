"""Evaluation helpers for anomaly detection results."""

from __future__ import annotations

import pandas as pd


def anomaly_summary(data: pd.DataFrame, anomaly_column: str = "final_anomaly") -> dict[str, int | float]:
    """Return simple counts and anomaly ratio for a result table."""
    total_rows = int(len(data))
    anomaly_count = int(data[anomaly_column].sum()) if anomaly_column in data else 0
    anomaly_rate = anomaly_count / total_rows if total_rows else 0.0
    return {
        "total_rows": total_rows,
        "anomaly_count": anomaly_count,
        "anomaly_rate": anomaly_rate,
    }
