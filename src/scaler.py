"""Feature scaling helpers."""

from __future__ import annotations

import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler


def scale_features(
    data: pd.DataFrame,
    method: str = "standard",
) -> tuple[pd.DataFrame, StandardScaler | MinMaxScaler]:
    """Scale numeric features and return the transformed frame with its scaler."""
    scaler = MinMaxScaler() if method == "minmax" else StandardScaler()
    scaled = pd.DataFrame(
        scaler.fit_transform(data),
        columns=data.columns,
        index=data.index,
    )
    return scaled, scaler
