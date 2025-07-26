from abc import ABC, abstractmethod
import math

class HinhHoc(ABC):
    @abstractmethod
    def tinh_dien_tich(self):
        pass
    
    @abstractmethod
    def tinh_chu_vi(self):
        pass
    def __str__(self):
        return f"Day la mot hinh hoc"
class HinhTron(HinhHoc):
    def __init__(self, ban_kinh) -> None:
         self.ban_kinh = ban_kinh
    
    def tinh_dien_tich(self):
        dien_tich_hinh_tron = math.pi * self.ban_kinh * self.ban_kinh
        return dien_tich_hinh_tron  #f"{dien_tich_hinh_tron:.2f}"
    def tinh_chu_vi(self):
        chu_vi_hinh_tron = math.pi * self.ban_kinh * 2
        return chu_vi_hinh_tron     #f"{chu_vi_hinh_tron:.2f}"
    def __str__(self,/) -> str:
        return super().__str__() + f" Hinh tron co ban kinh {self.ban_kinh}"

class HinhChuNhat(HinhHoc):
    def __init__(self, chieu_dai, chieu_rong):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong

    def tinh_dien_tich(self):
        dien_tich_hinh_chu_nhat = self.chieu_dai * self.chieu_rong
        return dien_tich_hinh_chu_nhat  #f"{dien_tich_hinh_chu_nhat:.2f}"
    def tinh_chu_vi(self):
        chu_vi_hinh_chu_nhat = 2 * (self.chieu_dai + self.chieu_rong)
        return chu_vi_hinh_chu_nhat     #f"{chu_vi_hinh_chu_nhat:.2f}"
    def __str__(self):
         return super().__str__() + f" Hinh chu nhat co chieu dai la {self.chieu_dai} va chieu rong la {self.chieu_rong}"
    def __eq__(self, other):
        return self.tinh_dien_tich() == other.tinh_dien_tich()

hinh_tron = HinhTron(10)
hinh_cn1 = HinhChuNhat(5, 10)
hinh_cn2 = HinhChuNhat(10, 5)

print(hinh_tron)
print(f"Diện tích: {hinh_tron.tinh_dien_tich():.2f}")
print(f"Chu vi: {hinh_tron.tinh_chu_vi():.2f}")
print("-" * 20)

print(hinh_cn1)
print(f"Diện tích: {hinh_cn1.tinh_dien_tich()}")
print(f"Chu vi: {hinh_cn1.tinh_chu_vi()}")
print("-" * 20)

# So sánh 2 hình chữ nhật bằng magic method __eq__
print(f"Hình chữ nhật 1 có bằng hình chữ nhật 2 không? {hinh_cn1 == hinh_cn2}") # Mong đợi: True

