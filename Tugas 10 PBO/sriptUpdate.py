from matakuliah import Matakuliah

# Update Data
A = Matakuliah()
kodemk = "1232"
A.namamk = "Kalkulus II"
A.sks = "2"
A.updateByKodeMK(kodemk)
B = A.getAllData()
print(B)