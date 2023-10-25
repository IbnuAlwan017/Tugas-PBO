print("Aplikasi penghitung Luas dan Volume Silinder\n")

print("Diketahui :")
phi = 3.14
print("Nilai Phi nya :", phi)
r = float(input("Nilai jari-jarinya :"))
T = float(input("Nilai tingginya :"))
print("---------------------------\n")

Luas_Selimut = 2 * (phi * r * T)
Luas_Permukaan = (2 * phi * r * T) + (2 * phi * r**2)
Volume_Silinder = phi * r**2 * T

# Output
print("Hasilnya :")
print("Luas selimutnya :", Luas_Selimut)
print("Luas permukaannya :", Luas_Permukaan)
print("Volume silindernya :", Volume_Silinder)