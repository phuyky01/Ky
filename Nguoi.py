class Nguoi:
    def __init__(self, ten, tuoi):
        self.ten = ten
        self.tuoi = tuoi
        print("Constructor được gọi!")

a = Nguoi("Ky", 20)
print(a.ten, a.tuoi)
