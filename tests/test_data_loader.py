import pandas as pd

from src import config
from src.data_loader import load_table, save_table


def test_raw_data_paths_use_expected_excel_files():
    assert config.STOCK_SOURCE_FILE.name in {
        "COPHIEU_BANLE_TIEUDUNG.xlsx",
        "COPHIEU_BANLE_TIEUDUNG(2).xlsx",
    }
    assert config.NEWS_SOURCE_FILE.name in {
        "K4_CRAWL_NHOM_4_BAN_LE_TIEU_DUNG_DUOC.xlsx",
        "K4_CRAWL_NHOM_4_BAN_LE_TIEU_DUNG_DUOC(2).xlsx",
    }


def test_processed_data_paths_use_parquet():
    assert config.STOCK_CLEANED_FILE.suffix == ".parquet"
    assert config.NEWS_CLEANED_FILE.suffix == ".parquet"
    assert config.NEWS_TICKER_EXPLODED_FILE.suffix == ".parquet"
    assert config.STOCK_FEATURES_FILE.suffix == ".parquet"
    assert config.ZSCORE_ANOMALIES_FILE.suffix == ".parquet"


def test_parquet_round_trip(tmp_path):
    expected = pd.DataFrame(
        {"ticker": ["FPT", "MWG"], "price": [100.5, 42.0]}
    )
    path = tmp_path / "nested" / "processed.parquet"

    save_table(expected, path)
    actual = load_table(path)

    pd.testing.assert_frame_equal(actual, expected)


def test_parquet_save_normalizes_mixed_content_hash(tmp_path):
    data = pd.DataFrame({"content_hash": [123, "abc"]})
    path = tmp_path / "processed.parquet"

    save_table(data, path)

    assert load_table(path)["content_hash"].tolist() == ["123", "abc"]
