tong_phut = 135
cong_suat_w = 250

# Dùng // và % để tính số giờ trọn vẹn và số phút còn lại
so_gio = tong_phut // 60
phut_con_lai = tong_phut % 60
print(f"Số giờ trọn vẹn: {so_gio} giờ")
print(f"Số phút còn lại: {phut_con_lai} phút")

# Tạo bien su_dung_lau nhận True khi tong_phut > 60
su_dung_lau = tong_phut > 60
print(f"Sử dụng lâu (>60 phút): {su_dung_lau}")

# Tạo bien du_lieu_hop_le nhận True khi cong_suat_w > 0 và tong_phut > 0
du_lieu_hop_le = cong_suat_w > 0 and tong_phut > 0
print(f"Dữ liệu hợp lệ: {du_lieu_hop_le}")

# DỰ ĐOÁN KẾT QUẢ BIỂU THỨC (Trước khi chạy):
# - 100 + 20 * 3  -> Nhân trước cộng sau: 100 + 60 = 160
# - (100 + 20) * 3 -> Ngoặc trước nhân sau: 120 * 3 = 360
# ==========================================
print("Kết quả 100 + 20 * 3 là:", 100 + 20 * 3)
print("Kết quả (100 + 20) * 3 là:", (100 + 20) * 3)
