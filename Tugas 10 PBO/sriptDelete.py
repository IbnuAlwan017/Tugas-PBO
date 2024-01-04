from matakuliah import Matakuliah

# Delete Data
A = Matakuliah()
kodemk = "1001"

A.deleteByKodeMK(kodemk)
B = A.getAllData()
print(B)