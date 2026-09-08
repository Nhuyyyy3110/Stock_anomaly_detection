"""Feature engineering for trading data."""

import pandas as pd


def add_return_feature(data: pd.DataFrame, price_column: str = "close") -> pd.DataFrame:
    """Add a simple percentage return feature when the price column exists."""
    result = data.copy()
    if price_column in result.columns:
        result["return"] = result[price_column].pct_change()
    return result
