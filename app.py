from utils import math_tools
print(math_tools.cong(2, 3))
mt = math_tools.MayTinh("Pro")
print(mt.nhan(5, 7))

# Cách 2: import trực tiếp từ __init__.py (đã re-export)
from utils import cong, MayTinh
print(cong(10, 20))
m2 = MayTinh("Standard")
print(m2.nhan(20, 4))

#Cách 3: import sâu
from utils.math_tools import cong, MayTinh as Calc
print(cong(100, 200))
print(Calc().nhan(3, 8))
