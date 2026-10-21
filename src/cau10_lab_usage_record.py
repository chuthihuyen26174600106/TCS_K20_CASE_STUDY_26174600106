from datetime import datetime

# Nhập dữ liệu
ma_phien = input("Mã phiên: ")
ma_may = input("Máy: ")
cong_suat_w = float(input("Công suất (W): "))
so_phut = int(input("Thời gian (phút): "))
don_gia_kwh = float(input("Đơn giá (VND/kWh): "))

# Xử lý tính toán
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh
tren_60_phut = so_phut > 60
ghi_nhan_luc = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# In kết quả
print(f"Mã phiên: {ma_phien}")
print(f"Máy: {ma_may}")
print(f"Công suất: {cong_suat_w:.2f} W")
print(f"Thời lượng: {so_phut} phút")
print(f"Điện năng: {dien_nang_kwh:.3f} kWh")
print(f"Chi phí: {chi_phi:.2f} VND")
print(f"Trên 60 phút: {tren_60_phut}")
print(f"Ghi nhận lúc: {ghi_nhan_luc}")