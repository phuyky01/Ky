class Nguoi:
    def __init__(self, ten, tuoi):
        self.ten = ten
        self.tuoi = tuoi

    def gioi_thieu(self):
        return f'Tên: {self.ten}, Tuổi: {self.tuoi}'
    
class NhanVien(Nguoi):
    def __init__(self, ten, tuoi, luong):
        super().__init__(ten, tuoi)  # Gọi hàm khởi tạo của lớp cha __inti__ của Nguoi
        self.luong = luong

    def gioi_thieu(self):
        return super().gioi_thieu() + f". Toi la nhan vien, luong {self.luong}$."
    
#Ke thua nhieu tang: NhanVienIT (tu NhanVien)
class NhanVienIT(NhanVien):
    def __init__(self, ten, tuoi, luong, ngon_ngu):
        super().__init__(ten, tuoi, luong)  # Gọi hàm khởi tạo của lớp cha NhanVien
        self.ngon_ngu = ngon_ngu

    def gioi_thieu(self):
        return super().gioi_thieu() + f". Toi lam viec o phong IT, biet {self.ngon_ngu}."
    
#Thu nghiem
nvit = NhanVienIT("An", 30, 5000, "Python")
nv = NhanVien("Binh", 28, 4000)
print(nvit.gioi_thieu())  # Tên: An, Tuổi: 30. Tôi là nhân viên, lương 5000$. Tôi làm việc ở phòng IT, biết Python.
print(nv.gioi_thieu())    # Tên: Bình, Tuổi: 28. Tôi là nhân viên, lương 4000$.