from src import config


def test_raw_data_paths_use_expected_excel_files():
    assert config.STOCK_SOURCE_FILE.name in {
        "COPHIEU_BANLE_TIEUDUNG.xlsx",
        "COPHIEU_BANLE_TIEUDUNG(2).xlsx",
    }
    assert config.NEWS_SOURCE_FILE.name in {
        "K4_CRAWL_NHOM_4_BAN_LE_TIEU_DUNG_DUOC.xlsx",
        "K4_CRAWL_NHOM_4_BAN_LE_TIEU_DUNG_DUOC(2).xlsx",
    }
