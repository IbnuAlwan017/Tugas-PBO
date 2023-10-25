print("Aplikasi Penghitung Luas dan Volume Limas Segiempat\n")
"""
Keterangan :
LS1 : Luas Sisi 1 (Segitiga)
LS2 : Luas Sisi 2 (Segitiga)
LS3 : Luas Sisi 3 (Segitiga)
LS4 : Luas Sisi 4 (Segitiga)
LS5 : Luas Sisi 5 (Persegi)
Luas Alas = LS5 (Persegi) 
T = Tinggi
"""

# Nilai Variabel
print("Diketahui :")
LS1 = float(input("Luas Sisi 1 nya adalah :"))
LS2 = float(input("Luas Sisi 2 nya adalah :"))
LS3 = float(input("Luas Sisi 3 nya adalah :"))
LS4 = float(input("Luas Sisi 4 nya adalah :"))
LS5 = float(input("Luas Sisi 5 nya adalah :"))
La = float(input("Luas alasnya adalah :"))
T = float(input("Tingginya adalah :"))
print("---------------------------\n")

# Rumus
Luas_LS = LS1 + LS2 + LS3 + LS4 + LS5
Volume_LS = 1/3 * La * T

# Output
print("Hasilnya :")
print("Luas Limas Segiempatnya :", Luas_LS)
print("Volume Limas Segiempatnya :", Volume_LS)