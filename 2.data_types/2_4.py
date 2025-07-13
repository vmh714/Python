cau_van = "Python là một ngôn ngữ lập trình Python rất phổ biến và mạnh mẽ."
cau_thuong = cau_van.lower()
cau_sach = cau_thuong.replace(".","")
danh_sach = cau_sach.split(" ")
tu_duy_nhat = set(danh_sach)
print(f"Số lượng từ duy nhất là {len(tu_duy_nhat)}")
print("Danh sách các từ duy nhất là: ")
for x in tu_duy_nhat:
    print(x)