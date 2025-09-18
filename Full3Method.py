class Nguoi:
    so_nguoi = 0  # Class variable
    def __init__(self, ten):
        self.ten = ten
        Nguoi.so_nguoi += 1

    #Instance method
    def chao(self):
        return f"Xin chào, tôi là {self.ten}"

    #Class method
    @classmethod
    def thong_ke(cls):
        return f"Tổng số người: {cls.so_nguoi}"

    #Static method
    @staticmethod
    def huong_dan():
        return "Dung Nguoi(ten) để tạo đối tượng Nguoi mới."
    
a = Nguoi("An")
b = Nguoi("Binh")

print(a.chao())  # Instance method -> Xin chào, tôi là An
print(Nguoi.thong_ke())  # Class method -> Tổng số người: 2
print(Nguoi.huong_dan())  # Static method -> Dùng người (tên) để tạo đối tượng Nguoi mới.

