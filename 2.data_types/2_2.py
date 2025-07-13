danh_sach_mua_sam = ["trứng", "sữa", "bánh mì"]
print(f"Danh sách mua sắm gồm: {danh_sach_mua_sam}")
danh_sach_mua_sam.append("thịt bò")
danh_sach_mua_sam.insert(1, "rau củ")
danh_sach_mua_sam.remove("bánh mì")
print(f"Tôi đã mua {danh_sach_mua_sam.pop()}")
danh_sach_mua_sam.sort();
[print(x) for x in danh_sach_mua_sam]

