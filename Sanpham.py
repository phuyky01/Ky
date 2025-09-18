class SanPham:
    def __init__(self, gia):
        self.__gia = gia # Private attribute

    @property
    def gia(self):
        return self.__gia
    
    @gia.setter
    def gia(self, value):   
        if value > 0:
            self.__gia = value
        else:
            raise ValueError("Giá phải > 0")

sp = SanPham(100)
print(sp.gia)  # getter ✔ 100
sp.gia = 200 # setter ✔
print(sp.gia)  # getter ✔ 200
#print(sp.__gia)  # ❌ Lỗi AttributeError
print(sp._SanPham__gia)  # ⚠ vẫn truy cập được (nhưng không khuyến khích)
  