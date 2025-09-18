class Nguoi:
    def __init__(self, ten):
        self.ten = ten
    print("{self.ten} đã được tạo!")

    def __del__(self):
        print(f"{self.ten} đã bị hủy!")

a = Nguoi("An")
del a # Gọi hàm hủy