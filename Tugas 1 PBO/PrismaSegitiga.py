print("Aplikasi Penghitung Luas dan Volume Prisma Segiempat\n")

# Nilai Variabel
print("Diketahui :")
S1 = float(input("Sisi 1 nya adalah :"))
S2 = float(input("Sisi 2 nya adalah :"))
S3 = float(input("Sisi 3 nya adalah :"))
T = float(input("Tinggi prismanya adalah :"))
a = float(input("Alas segitiganya adalah :"))
t = float(input("Tinggi segitiganya adalah :"))
print("---------------------------\n")

# Rumus
Ls = (S1 + S2 + S3) * T
Lp = ((S1 + S2 + S3) * T) + (a * t)
Volume = 1/2 * (a * t * T)

# Output
print("Hasilnya :")
print("Luas Selimutnya :", Ls)
print("Luas Permukaannya :", Lp)
print("Volume Prisma Segitiganya :", Volume)