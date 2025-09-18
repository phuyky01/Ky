class Square:
    def __init__(self, side):
        self.side = side

    @classmethod
    def from_area(cls, area):
        side = area ** 0.5
        return cls(side)

h1 = Square(4)
h2 = Square.from_area(25)

print(h1.side)  # 4
print(h2.side)  # 4.0