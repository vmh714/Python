diem = float(input("Nhập điểm số của bạn: "))
print("Sử dụng if-else")
if diem > 10:
    print("Điểm số bạn nhập không hợp lệ")
elif diem >=9:
    print("Xuất sắc")
elif diem >= 8:
    print("Giỏi")
elif diem >= 6.5:
    print("Khá")
elif diem >= 5:
    print("Trung bình")
elif diem >=0 and diem < 5:
    print("Yếu")
else:
    print("Điểm bạn nhập không hợp lệ")

