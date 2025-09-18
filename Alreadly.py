class Hinhchunhat:
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong

    def dientich(self):
        return self.dai * self.rong
    
hcn = Hinhchunhat(5, 3)
print(f"Diện tích hình chữ nhật là {hcn.dientich()}")