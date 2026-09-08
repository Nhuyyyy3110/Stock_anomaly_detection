"""Load raw stock and news data."""

from pathlib import Path

import pandas as pd


def load_table(path: Path, sheet_name: str | int = 0) -> pd.DataFrame:
    """Load a CSV or Excel table based on its extension."""
    if path.suffix.lower() in {".xlsx", ".xls"}:
        return pd.read_excel(path, sheet_name=sheet_name)
    if path.suffix.lower() == ".csv":
        return pd.read_csv(path)
    raise ValueError(f"Unsupported file type: {path.suffix}")
