import tkinter as tk
from tkinter import Frame, Label, Entry, Button, END, W, font

def hitung_luas_selimut():
    try:
        s1 = float(txtsisi1.get())
        s2 = float(txtsisi2.get())
        s3 = float(txtsisi3.get())
        t_segitiga = float(txttinggi_segitiga.get())
        ls = (s1 + s2 + s3) * t_segitiga
        txtLS.delete(0, END)
        txtLS.insert(END, round(ls, 2))
    except ValueError:
        txtLS.delete(0, END)
        txtLS.insert(END, "Masukkan angka")

def hitung_luas_permukaan():
    try:
        s1 = float(txtsisi1.get())
        s2 = float(txtsisi2.get())
        s3 = float(txtsisi3.get())
        a = float(txtalas.get())
        t_prisma = float(txttinggi_prisma.get())
        lp = (s1 + s2 + s3) * t_prisma + a * t_prisma
        txtLP.delete(0, END)
        txtLP.insert(END, round(lp, 2))
    except ValueError:
        txtLP.delete(0, END)
        txtLP.insert(END, "Masukkan angka")

def hitung_volume():
    try:
        a = float(txtalas.get())
        t_segitiga = float(txttinggi_segitiga.get())
        t_prisma = float(txttinggi_prisma.get())
        v = (1/2) * a * t_segitiga * t_prisma
        txtVolume.delete(0, END)
        txtVolume.insert(END, round(v, 2))
    except ValueError:
        txtVolume.delete(0, END)
        txtVolume.insert(END, "Masukkan angka")

def hitung(event=None):
    hitung_luas_selimut()
    hitung_luas_permukaan()
    hitung_volume()

app = tk.Tk()

app.title("Aplikasi Penghitung Luas Selimut, Luas Permukaan, dan Volume Prisma Segitiga")
app.geometry("500x400")
app.configure(bg="#f0f0f0")

frame = Frame(app, bg="#f0f0f0")
frame.pack(padx=20, pady=20)

judul = Label(frame, text="Penghitung Luas Selimut, Luas Permukaan, dan Volume Prisma Segitiga", font=("Arial", 12, "bold"), bg="#f0f0f0")
judul.grid(row=0, columnspan=2, pady=10)

sisi1 = Label(frame, text="Sisi 1: ", bg="#f0f0f0")
sisi1.grid(row=1, column=0, sticky=W, padx=5, pady=5)

sisi2 = Label(frame, text="Sisi 2: ", bg="#f0f0f0")
sisi2.grid(row=2, column=0, sticky=W, padx=5, pady=5)

sisi3 = Label(frame, text="Sisi 3: ", bg="#f0f0f0")
sisi3.grid(row=3, column=0, sticky=W, padx=5, pady=5)

alas = Label(frame, text="Alas Segitiga: ", bg="#f0f0f0")
alas.grid(row=4, column=0, sticky=W, padx=5, pady=5)

tinggi_segitiga = Label(frame, text="Tinggi Segitiga: ", bg="#f0f0f0")
tinggi_segitiga.grid(row=5, column=0, sticky=W, padx=5, pady=5)

tinggi_prisma = Label(frame, text="Tinggi Prisma: ", bg="#f0f0f0")
tinggi_prisma.grid(row=6, column=0, sticky=W, padx=5, pady=5)

txtsisi1 = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txtsisi1.grid(row=1, column=1)

txtsisi2 = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txtsisi2.grid(row=2, column=1)

txtsisi3 = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txtsisi3.grid(row=3, column=1)

txtalas = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txtalas.grid(row=4, column=1)

txttinggi_segitiga = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txttinggi_segitiga.grid(row=5, column=1)

txttinggi_prisma = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txttinggi_prisma.grid(row=6, column=1)

hitung_button = Button(frame, text="Hitung", command=hitung, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
hitung_button.grid(row=7, column=1, sticky=W, padx=5, pady=10)

luas_selimut = Label(frame, text="Luas Selimut: ", bg="#f0f0f0", font=("Arial", 12))
luas_selimut.grid(row=8, column=0, sticky=W, padx=5, pady=5)

luas_permukaan = Label(frame, text="Luas Permukaan: ", bg="#f0f0f0", font=("Arial", 12))
luas_permukaan.grid(row=9, column=0, sticky=W, padx=5, pady=5)

volume = Label(frame, text="Volume: ", bg="#f0f0f0", font=("Arial", 12))
volume.grid(row=10, column=0, sticky=W, padx=5, pady=5)

txtLS = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txtLS.grid(row=8, column=1, sticky=W, padx=5, pady=5)

txtLP = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txtLP.grid(row=9, column=1, sticky=W, padx=5, pady=5)

txtVolume = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txtVolume.grid(row=10, column=1, sticky=W, padx=5, pady=5)

app.bind('<Return>', hitung)  # Menambahkan binding untuk tombol Enter

app.mainloop()