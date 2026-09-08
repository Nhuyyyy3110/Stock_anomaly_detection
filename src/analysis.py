"""Statistical summaries and comparisons."""

import pandas as pd


def summary_statistics(data: pd.DataFrame) -> pd.DataFrame:
    """Return descriptive statistics for numeric columns."""
    return data.describe(include="number").transpose()
