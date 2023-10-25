print("Aplikasi Penghitung Luas dan Volume Kerucut\n")

# Nilai Variabel
phi = 3.14
print("Nilai Phi nya :", phi)
r = float(input("Nilai jari-jarinya :"))
s = float(input("Nilai garis pelukisnya :"))
T = float(input("Nilai tingginya :"))
print("---------------------------\n")

# Rumus
Luas_Selimut = phi * r * s
Luas_Permukaan = (phi * r * s) + (phi * r**2)
Volume_Kerucut = 1/3 * (phi * r**2 * T)

# Output
print("Hasilnya :")
print("Luas selimutnya :", Luas_Selimut)
print("Luas permukaannya :", Luas_Permukaan)
print("Volume kerucutnya :", Volume_Kerucut)