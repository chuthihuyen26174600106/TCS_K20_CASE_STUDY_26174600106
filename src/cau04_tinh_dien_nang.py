cong_suat_w = 250
so_phut = 90
don_gia_kwh = 3000

# DỰ ĐOÁN KẾT QUẢ TRƯỚC KHI CHẠY:
# - Với so_phut = 90:
#   dien_nang_kwh = 250 * 90 / 60 / 1000 = 0.375 kWh
#   chi_phi = 0.375 * 3000 = 1125.0 VND
# ==========================================

# Tính điện năng tiêu thụ và chi phí điện
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

# In cả giá trị và kiểu dữ liệu của hai kết quả
print("Với số phút = 90:")
print(f"Điện năng: {dien_nang_kwh} | Kiểu: {type(dien_nang_kwh)}")
print(f"Chi phí: {chi_phi} | Kiểu: {type(chi_phi)}")

# Thay so_phut bằng 60 rồi chạy lại và so sánh
so_phut = 60
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

print("\nVới số phút = 60:")
print(f"Điện năng: {dien_nang_kwh} | Kiểu: {type(dien_nang_kwh)}")
print(f"Chi phí: {chi_phi} | Kiểu: {type(chi_phi)}")