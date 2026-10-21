# Khai báo biến theo quy tắc snake_case
ma_phien = "LAB026" # src
ma_may = "PC12" # src
cong_suat_w = 250.0 # float
thoi_gian_phut = 90 # int
trang_thai_hoat_dong = True# bool
ghi_chu = None # NoneType

# In giá trị và kiểm tra kiểu dữ liệu
print("Mã phiên:", ma_phien, "| Kiểu:", type(ma_phien))
print("Mã máy:", ma_may, "| Kiểu:", type(ma_may))
print("Công suất (W):", cong_suat_w, "| Kiểu:", type(cong_suat_w))
print("Thời gian (phút):", thoi_gian_phut, "| Kiểu:", type(thoi_gian_phut))
print("Trạng thái:", trang_thai_hoat_dong, "| Kiểu:", type(trang_thai_hoat_dong))
print("Ghi chú:", ghi_chu, "| Kiểu:", type(ghi_chu))

# Gán lại giá trị mới cho thời gian
thoi_gian_phut = 120
print("Thời gian sau khi gán lại (phút):", thoi_gian_phut)