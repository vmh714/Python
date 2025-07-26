class TaiKhoanNganHang:
    def __init__(self, so_tai_khoan, so_du_ban_dau):
        self.so_tai_khoan = so_tai_khoan
        self.__so_du = so_du_ban_dau
    @property
    def so_du(self):
        return self.__so_du
    
    def gui_tien(self, so_tien):
        if so_tien <= 0:
            return 
        self.__so_du += so_tien
    def rut_tien (self, so_tien):
        if so_tien <= 0 or so_tien > self.__so_du:
            return
        self.__so_du -= so_tien
    def hien_thi_so_du(self):
        print(f"So du hien tai la: {self.__so_du}.0f VND")

tk = TaiKhoanNganHang("123456789", 500000)

# Truy cập public attribute
print(f"Số tài khoản: {tk.so_tai_khoan}")

# Dùng property để đọc số dư
print(f"Số dư ban đầu: {tk.so_du:,.0f} VND")

# Thử gán trực tiếp vào property (lỗi vì không có setter)
# tk.so_du = 1000000  # AttributeError

# Thử truy cập trực tiếp vào __so_du (lỗi do name mangling)
# print(tk.__so_du)  # AttributeError

# Dùng method
tk.gui_tien(200000)
tk.hien_thi_so_du()  # 700,000 VND

tk.rut_tien(100000)
tk.hien_thi_so_du()  # 600,000 VND

# Trường hợp lỗi
tk.rut_tien(1000000)  # "Số dư không đủ."
tk.gui_tien(-50000)   # "Số tiền không hợp lệ."
tk.hien_thi_so_du()   # 600,000 VND


