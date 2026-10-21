# Nhập dữ liệu
ma_may = input("Nhập mã máy: ")
cong_suat_raw = input("Nhập công suất W: ")
so_phut_raw = input("Nhập số phút: ")
don_gia_raw = input("Nhập đơn giá kWh: ")

# In kiểu dữ liệu ngay sau khi nhập
print("Kiểu mã máy:", type(ma_may))
print("Kiểu công suất ban đầu:", type(cong_suat_raw))
print("Kiểu số phút ban đầu:", type(so_phut_raw))
print("Kiểu đơn giá ban đầu:", type(don_gia_raw))

# Chuyển kiểu dữ liệu
cong_suat_w = float(cong_suat_raw)
so_phut = int(so_phut_raw)
don_gia_kwh = float(don_gia_raw)

# Tính toán lại
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

print(f"Máy: {ma_may}")
print(f"Điện năng: {dien_nang_kwh} kWh")
print(f"Chi phí: {chi_phi} VND")