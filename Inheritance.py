#Class cha (Parent)
class DongVat:
    def __init__(self, ten):
        self.ten = ten

    def speak(self):
        return f"..."
    
#Class con (Child) kế thừa từ class cha
class Cho(DongVat):
    def speak(self):
        return "Gâu Gâu!"

class Meo(DongVat):
    def speak(self):
        return "Meo Meo!"
    
#Tạo đối tượng từ class con
cho = Cho("Buddy")
meo = Meo("Kitty")

print(f"{cho.ten} nói: {cho.speak()}")  # Buddy nói: Gâu Gâu!
print(f"{meo.ten} nói: {meo.speak()}")  # Kitty nói: Meo Meo!