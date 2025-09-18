class TaiKhoan:
    def __init__(self, so_du):
        self.__so_du = so_du   # private

    def nap(self, tien):
        self.__so_du += tien

    def xem_so_du(self):
        return self.__so_du

tk = TaiKhoan(1000)
print(tk.xem_so_du())    # ✔ 1000
tk.nap(500)
print(tk.xem_so_du())    # ✔ 1500

#print(tk.__so_du)      # ❌ Lỗi AttributeError
print(tk._TaiKhoan__so_du)  # ⚠ vẫn truy cập được (nhưng không khuyến khích)
