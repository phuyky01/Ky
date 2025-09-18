class TaiKhoan:
    def __init__(self, so_du):
        self.__so_du = so_du   # private (ẩn đi)

    def nap(self, so_tien):
        self.__so_du += so_tien

    def lay_so_du(self):
        return self.__so_du


tk = TaiKhoan(1000)
tk.nap(500)
print(tk.lay_so_du())   # 1500
#print(tk.__so_du)     # ❌ Lỗi, không truy cập trực tiếp
