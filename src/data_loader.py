"""Load raw stock and news data."""

from pathlib import Path

import pandas as pd


def load_table(path: Path, sheet_name: str | int = 0) -> pd.DataFrame:
    """Load a CSV, Excel, or Parquet table based on its extension."""
    if path.suffix.lower() in {".xlsx", ".xls"}:
        return pd.read_excel(path, sheet_name=sheet_name)
    if path.suffix.lower() == ".csv":
        return pd.read_csv(path)
    if path.suffix.lower() in {".parquet", ".pq"}:
        return pd.read_parquet(path)
    raise ValueError(f"Unsupported file type: {path.suffix}")


def save_table(data: pd.DataFrame, path: Path) -> None:
    """Save a processed table as Parquet without persisting its index."""
    if path.suffix.lower() not in {".parquet", ".pq"}:
        raise ValueError(f"Processed tables must use Parquet: {path.suffix}")
    path.parent.mkdir(parents=True, exist_ok=True)
    normalized = data.copy()
    if "content_hash" in normalized:
        normalized["content_hash"] = normalized["content_hash"].astype("string")
    normalized.to_parquet(path, index=False)
