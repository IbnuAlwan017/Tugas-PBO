from matakuliah import Matakuliah

# Entry Data
A = Matakuliah()
A.kodemk = "123243"
A.namamk = "Struktur Data"
A.sks = "4"
A.simpan()
B = A.getAllData()
print(B)