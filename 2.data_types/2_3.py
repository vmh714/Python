khoa_hoc = {
    "ten_khoa_hoc": "Basic Python Program",
    "ma_khoa_hoc": "PYCB01",
    "so_tin_chi": 3,
}
print(f"Course name is {khoa_hoc['ten_khoa_hoc']}, Credit is {khoa_hoc['so_tin_chi']}")

khoa_hoc.update({'giang_vien': 'Nguyen Van B'})
khoa_hoc.update({'so_tin_chi': 4})
#Sử dụng cách ngố
print("Sử dụng cách ngố")
for x in khoa_hoc:
    print(f"{x}: {khoa_hoc[x]}")
#Sử dụng cách chuyên nghiệp
print("Sử dụng cách chuyên nghiệp")
for x,y in khoa_hoc.items():
    print(f"{x}: {y}")