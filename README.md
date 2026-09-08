# Stock Anomaly Detection

Xây dựng hệ thống phát hiện bất thường trong giao dịch cổ phiếu
và phân tích mối liên hệ với tin tức doanh nghiệp.

## Mục tiêu

- Làm sạch dữ liệu OHLCV của 14 mã cổ phiếu.
- Tạo đặc trưng giao dịch.
- Phát hiện bất thường bằng Z-score và KNN.
- Liên kết phiên bất thường với tin tức doanh nghiệp.
- Hiển thị kết quả bằng Streamlit.

## Dữ liệu

Dự án sử dụng:

- Dữ liệu OHLCV của 14 mã cổ phiếu.
- Dữ liệu tin tức doanh nghiệp.
- Khoảng thời gian phân tích giá: 05/05/2025–04/09/2026.
- Khoảng thời gian tin dùng để liên kết: 01/05/2025–04/09/2026.

Dữ liệu thô không được lưu trên GitHub. Người dùng cần đặt file
vào thư mục `data/raw/`.

## Cài đặt

Tạo môi trường ảo:

```bash
python -m venv .venv
