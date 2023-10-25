print("Aplikasi penghitung Luas dan Volume Bola\n")

# Nilai Variabel
print("Diketahui :")
jari_jari = float(input("Panjang jari-jari bola: "))
print("---------------------------\n")

# Rumus
luas = 4 * 3.14 * jari_jari**2
volume = (4/3) * 3.14 * jari_jari**3

# Output
print("Hasilnya :")
print("Luas bolanya : ", luas)
print("Volume bolanya : ", volume)