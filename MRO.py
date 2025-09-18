class DongVat:
    def speak(self, ten):
        self.ten = ten

class Cho(DongVat):
    def __init__(self,ten,giong):
        super().__init__(ten) # Gọi hàm khởi tạo của lớp cha
        self.giong = giong

c = Cho("Buddy", "Golden Retriever")   
print(f"Tên: {c.ten}, Giống: {c.giong}")  # Tên: Buddy, Giống: Golden Retriever 
print(DongVat.mro())