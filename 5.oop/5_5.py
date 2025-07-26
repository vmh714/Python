class Sach:
    def __init__(self, tua_de, tac_gia, nam_xuat_ban) -> None:
        self.tua_de = tua_de
        self.tac_gia = tac_gia
        self.nam_xuat_ban = nam_xuat_ban

    def __str__(self) -> str:
        return f"Tua de: {self.tua_de}, Tac gia: {self.tac_gia} ({self.nam_xuat_ban})"
    def __repr__(self) -> str:
        return f"Sach('{self.tua_de}', '{self.tac_gia}', {self.nam_xuat_ban}"

class ThuVien:
    def __init__(self,ten_thu_vien):
        self.ten_thu_vien = ten_thu_vien
        self._danh_sach_sach = []
    def them_sach(self, sach):
        self._danh_sach_sach.append(sach)
    def tim_sach_theo_tua_de(self, tua_de):
        tua_de_lower = tua_de.lower()
        ket_qua = [sach for sach in self._danh_sach_sach if sach.tua_de.lower() == tua_de_lower ]
        return ket_qua
    def __len__(sefl):
        return len(sefl._danh_sach_sach)
    def __str__(self):
        if not self._danh_sach_sach:
            return "Khong co sach trong thu vien"
        return "/n".join(str(sach) for  sach in self._danh_sach_sach)

# Tạo các đối tượng Sách
sach1 = Sach("Lão Hạc", "Nam Cao", 1943)
sach2 = Sach("Số Đỏ", "Vũ Trọng Phụng", 1936)
sach3 = Sach("Dế Mèn Phiêu Lưu Ký", "Tô Hoài", 1941)

# Tạo đối tượng Thư viện
thu_vien_quoc_gia = ThuVien("Thư viện Quốc gia")

# Thêm sách vào thư viện
thu_vien_quoc_gia.them_sach(sach1)
thu_vien_quoc_gia.them_sach(sach2)
thu_vien_quoc_gia.them_sach(sach3)

# Sử dụng magic method __len__
print(f"Thư viện hiện có {len(thu_vien_quoc_gia)} cuốn sách.")

# Sử dụng magic method __str__
print("\nDanh sách các sách trong thư viện:")
print(thu_vien_quoc_gia)

# Tìm kiếm sách
print("\nTìm kiếm sách 'số đỏ':")
ket_qua = thu_vien_quoc_gia.tim_sach_theo_tua_de("số đỏ")
for sach in ket_qua:
    print(sach)
