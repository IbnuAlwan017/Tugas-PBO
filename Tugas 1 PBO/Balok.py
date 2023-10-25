print("Aplikasi Penghitung Luas dan Volume Balok\n")

# Nilai Variabel
print("Diketahui :")
panjang = float(input("Panjangnya :"))
tinggi = float(input("Tingginya :"))
lebar = float(input("Lebarnya :"))
print("---------------------------\n")

# Rumus
Luas_Balok = (2 * panjang * lebar) + (2 * panjang * tinggi) + (2 * lebar * tinggi)
Volume_Balok = panjang * lebar * tinggi

# Output
print("Hasilnya :")
print("Luas baloknya :", Luas_Balok)
print("Volume baloknya :", Volume_Balok)