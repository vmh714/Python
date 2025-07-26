class SinhVien:
    def __init__(self,ma_sv:str, ho_ten:str):
        print(f"Sinh vien moi da duoc tao thanh cong: {ho_ten}, {ma_sv}")
        self.ma_sv = ma_sv
        self.ho_ten = ho_ten
        self.diem_mon_hoc = {}
    def them_diem(self,ten_mon_hoc:str, diem:float):
        self.diem_mon_hoc[ten_mon_hoc] = diem
    def tinh_diem_trung_binh(self):
        if self.diem_mon_hoc:
            return "0"
        diem_trung_binh = sum(self.diem_mon_hoc.values())
        diem_trung_binh /= len(self.diem_mon_hoc)
        return f"{diem_trung_binh:.2f}"
    def hien_thi_thong_tin(self):
        print(f"Ho ten sinh vien la {self.ho_ten} \nMSSV: {self.ma_sv} \nDiem trung binh mon: {self.tinh_diem_trung_binh()}")


# Tạo 2 đối tượng sinh viên
sv1 = SinhVien("2001", "Nguyễn Văn An")
sv2 = SinhVien("2002", "Trần Thị Bình")

# Thêm điểm cho sv1
sv1.them_diem("Toán", 9.0)
sv1.them_diem("Lý", 7.5)
sv1.them_diem("Hóa", 8.0)

# Thêm điểm cho sv2
sv2.them_diem("Văn", 8.5)
sv2.them_diem("Sử", 9.5)

# Hiển thị thông tin
sv1.hien_thi_thong_tin()
# Kết quả mong đợi:
# Mã SV: 2001
# Họ tên: Nguyễn Văn An
# Điểm trung bình: 8.17

sv2.hien_thi_thong_tin()
# Kết quả mong đợi:
# Mã SV: 2002
# Họ tên: Trần Thị Bình
# Điểm trung bình: 9.0


