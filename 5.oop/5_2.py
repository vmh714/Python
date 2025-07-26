class NhanVien:
    def __init__(self,ten ,ma_nv, luong_co_ban) -> None:
        self.ten = ten
        self.ma_nv = ma_nv
        self.luong_co_ban = luong_co_ban
    def tinh_luong(self):
        return self.luong_co_ban
    def hien_thi_thong_tin(self):
        print(f"Ten nhan vien: {self.ten}\nMa nhan vien: {self.ma_nv}")

class LapTrinhVien(NhanVien):
    def __init__(self,ten, ma_nv,luong_co_ban,so_gio_lam_them):
        super().__init__(ten, ma_nv, luong_co_ban)
        self.so_gio_lam_them = so_gio_lam_them
    def tinh_luong(self):
        return super().tinh_luong() +self.so_gio_lam_them * 200000

class QuanLy(NhanVien):
    def __init__(self, ten, ma_nv, luong_co_ban, he_so_chuc_vu):
        super().__init__(ten, ma_nv, luong_co_ban)
        self.he_so_chuc_vu = he_so_chuc_vu
    def tinh_luong(self):
        return super().tinh_luong() * self.he_so_chuc_vu

# Tạo các đối tượng
nv1 = LapTrinhVien("Phát", "LTV01", 15000000, 20)
nv2 = QuanLy("Hưng", "QL01", 20000000, 1.5)
nv3 = NhanVien("Linh", "NV01", 12000000) # Nhân viên thường

# Tạo một danh sách các nhân viên
danh_sach_nhan_vien = [nv1, nv2, nv3]

# Duyệt qua danh sách và tính lương cho mỗi người
# Đây chính là tính đa hình: cùng gọi method tinh_luong() nhưng kết quả khác nhau
# tùy vào đối tượng cụ thể là LapTrinhVien hay QuanLy.
for nv in danh_sach_nhan_vien:
    nv.hien_thi_thong_tin()
    print(f"Lương tháng này: {nv.tinh_luong():,.0f} VND")
    print("-" * 20)
