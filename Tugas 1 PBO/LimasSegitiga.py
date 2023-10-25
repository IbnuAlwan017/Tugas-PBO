print("Aplikasi Penghitung Luas dan Volume Limas Segitiga\n")

# Nilai Variabel
print("Diketahui :")
LS1 = float(input("Luas Sisi 1 nya adalah :"))
LS2 = float(input("Luas Sisi 2 nya adalah :"))
LS3 = float(input("Luas Sisi 3 nya adalah :"))
LS4 = float(input("Luas Sisi 4 nya adalah :"))
a = float(input("Alas Segitiganya adalah :"))
t = float(input("Tinggi segitiganya adalah :"))
T = float(input("Tingginya adalah :"))
print("---------------------------\n")

# Rumus
Luas = LS1 + LS2 + LS3 + LS4
Volume = 1/6 * (a * t * T)

# Output
print("Hasilnya :")
print("Luas Limas Segitiganya :", Luas)
print("Volume Limas Segitiganya :", Volume)