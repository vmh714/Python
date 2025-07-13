cac_thanh_pho = [
    ('Hà Nội',21.0285, 105.8542), 
    ('Đà Nẵng', 16.0544, 108.2022),
    ('TP. Hồ Chí Minh', 10.7769, 106.7009)
]
for x in cac_thanh_pho:
    (thanh_pho, kinh_do, vi_do) = x
    print(f"Tên thành phố là {thanh_pho}, kinh độ là {kinh_do}, vĩ độ là {vi_do}")