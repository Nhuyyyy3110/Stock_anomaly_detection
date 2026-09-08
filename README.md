# Phat hien bat thuong giao dich co phieu va lien ket tin tuc

Du an xay dung pipeline phat hien cac phien giao dich co phieu bat thuong trong nhom ban le, tieu dung, duoc va lien ket voi tin tuc doanh nghiep gan thoi diem bat thuong.

## Cau truc thu muc

```text
stock_anomaly_detection/
├── configs/              # Tham so pipeline
├── data/                 # Du lieu raw, interim, processed
├── models/               # Scaler va model da train
├── notebooks/            # Notebook phan tich theo tung buoc
├── src/                  # Ma nguon xu ly du lieu, feature, anomaly, news
├── dashboard/            # Ung dung Streamlit
├── tests/                # Unit tests
├── results/              # Bang, hinh va bao cao dau ra
├── logs/                 # Log pipeline
├── requirements.txt
└── run_pipeline.py
```

## Chay nhanh

```bash
pip install -r requirements.txt
python run_pipeline.py
```

Dashboard:

```bash
streamlit run dashboard/app.py
```
