# Dự đoán phép trừ: Kết quả là khoảng thời gian 1 giờ 50 phút -> hiển thị "1:50:00"

from datetime import datetime
thoi_diem = datetime.now()
thoi_diem_text = thoi_diem.strftime("%Y-%m-%d %H:%M:%S")
print(thoi_diem)
print(type(thoi_diem))
print(thoi_diem_text)
print(type(thoi_diem_text))
bat_dau = datetime(2026, 10, 14, 13, 15)
ket_thuc = datetime(2026, 10, 14, 15, 5)
thoi_luong = ket_thuc - bat_dau
print(thoi_luong)
print(type(thoi_luong))

# Giải thích:
# datetime: Đối tượng biểu diễn thời điểm cụ thể (ngày, giờ, phút, giây).
# str: Kiểu chuỗi ký tự (văn bản) thu được sau khi format bằng strftime().
# timedelta: Kiểu dữ liệu đại diện cho khoảng chênh lệch thời gian giữa hai mốc datetime.