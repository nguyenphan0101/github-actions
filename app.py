# # ==============================================================================
# # BÀI LAB BUỔI 10: DOCKER CONTAINERIZATION
# # Cấu trúc thư mục Lab:
# # /fx_extractor_project
# #   ├── app.py          (File code Python)
# #   ├── requirements.txt(Khai báo thư viện)
# #   └── Dockerfile      (Công thức đóng gói Docker)
# # ==============================================================================

# # ------------------------------------------------------------------------------
# # FILE 1: app.py (Logic nghiệp vụ của Script)
# # ------------------------------------------------------------------------------

# import requests
# import time
# import json
# import datetime


# def fetch_exchange_rates():
#     # Lấy thời gian hiện tại để làm mốc log
#     current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     print(f"[{current_time}] Đang gọi API lấy tỷ giá ngân hàng...")

#     try:
#         # Gửi request GET tới API
#         response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")

#         # Bắt buộc check status code, nếu API sập (404, 500) thì văng lỗi ngay
#         response.raise_for_status()

#         data = response.json()

#         # Lấy tỷ giá VND, nếu không có thì trả về 'N/A' để tránh crash code
#         vnd_rate = data["rates"].get("VND", "N/A")
#         print(f"-> THÀNH CÔNG! Tỷ giá USD/VND hiện tại: {vnd_rate}")

#         # TODO: Tương lai sẽ thêm hàm connect và insert vào Database tại đây

#     except requests.exceptions.RequestException as e:
#         # Bắt lỗi của thư viện requests
#         print(f"-> LỖI GỌI API: Tạm thời không thể kết nối. Chi tiết: {e}")


# if __name__ == "__main__":
#     print("🚀 Khởi động luồng mindx-delv3 FX Extractor Container...")

#     # Chạy vòng lặp cào dữ liệu mỗi 5 giây (để demo kiểm thử)
#     for i in range(1, 4):
#         print(f"\n--- Lần chạy thứ {i} ---")
#         fetch_exchange_rates()
#         time.sleep(5)

#     print("\n🛑 Hoàn thành tác vụ. Container đã xử lý xong và chuẩn bị tắt.")


import requests
import datetime


# --- HÀM 1: CHUYÊN XỬ LÝ LOGIC (Để Unit Test) ---
def extract_vnd_rate(json_data):
    """Bóc tách tỷ giá VND từ JSON. Trả về None nếu dữ liệu lỗi."""
    try:
        # rate = json_data["rates"]["VND"]
        rate = json_data["rates"]["VNĐ"]
        return rate if rate > 0 else None
    except (KeyError, TypeError):
        return None


# --- HÀM 2: CHUYÊN GỌI API ---
def fetch_data():
    print(f"[{datetime.datetime.now()}] Đang gọi API lấy tỷ giá...")
    try:
        response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        response.raise_for_status()

        # Đưa cục JSON nhận được vào hàm xử lý
        vnd_rate = extract_vnd_rate(response.json())

        if vnd_rate:
            print(f"-> THÀNH CÔNG: Tỷ giá USD/VND là {vnd_rate}")
        else:
            print("-> LỖI DỮ LIỆU: Không tìm thấy tỷ giá hợp lệ.")
    except Exception as e:
        print(f"-> LỖI KẾT NỐI: {e}")


if __name__ == "__main__":
    fetch_data()
