ma_may = input("Nhập mã máy: ")
cong_suat_w = float(input("Nhập công suất W: "))
so_phut = int(input("Nhập số phút: "))
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000

print(f"Máy: {ma_may}")
print(f"Điện năng: {dien_nang_kwh:.3f} kWh")

# NHẬT KÝ CHẨN ĐOÁN LỖI
# File: src/cau07_chan_doan_loi.py
# 1. TypeError ở dòng 4: cong_suat_w là chuỗi (str) nên không chia được. Nguyên nhân: Quên ép kiểu float().
# 2. NameError ở dòng 6: dien_nang chưa được định nghĩa. Nguyên nhân: Gõ sai tên biến dien_nang_kwh.
# 3. SyntaxError ở dòng 6: Cú pháp không hợp lệ. Nguyên nhân: Thiếu dấu ngoặc đóng ) cuối lệnh print.