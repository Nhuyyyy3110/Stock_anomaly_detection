"""Project-wide paths and configuration."""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
INTERIM_DATA_DIR = DATA_DIR / "interim"
RESULTS_DIR = PROJECT_ROOT / "results"
CONFIG_DIR = PROJECT_ROOT / "configs"
MODELS_DIR = PROJECT_ROOT / "models"
LOGS_DIR = PROJECT_ROOT / "logs"

PARAMS_FILE = CONFIG_DIR / "params.yaml"

STOCK_SOURCE_CANDIDATES = [
    RAW_DATA_DIR / "COPHIEU_BANLE_TIEUDUNG.xlsx",
    RAW_DATA_DIR / "COPHIEU_BANLE_TIEUDUNG(2).xlsx",
]
NEWS_SOURCE_CANDIDATES = [
    RAW_DATA_DIR / "K4_CRAWL_NHOM_4_BAN_LE_TIEU_DUNG_DUOC.xlsx",
    RAW_DATA_DIR / "K4_CRAWL_NHOM_4_BAN_LE_TIEU_DUNG_DUOC(2).xlsx",
]


def first_existing_path(candidates: list[Path]) -> Path:
    """Return the first existing path, or the first candidate as the default."""
    return next((path for path in candidates if path.exists()), candidates[0])


STOCK_SOURCE_FILE = first_existing_path(STOCK_SOURCE_CANDIDATES)
NEWS_SOURCE_FILE = first_existing_path(NEWS_SOURCE_CANDIDATES)

STOCK_CLEANED_FILE = INTERIM_DATA_DIR / "stock_clean.parquet"
NEWS_CLEANED_FILE = INTERIM_DATA_DIR / "news_clean.parquet"
NEWS_TICKER_EXPLODED_FILE = INTERIM_DATA_DIR / "news_ticker_exploded.parquet"
STOCK_FEATURES_FILE = PROCESSED_DATA_DIR / "stock_features.parquet"
ZSCORE_ANOMALIES_FILE = PROCESSED_DATA_DIR / "zscore_anomalies.parquet"
