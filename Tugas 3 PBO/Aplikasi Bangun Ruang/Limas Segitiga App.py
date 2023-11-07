import tkinter as tk
from tkinter import Frame, Label, Entry, Button, END, W, font

def hitung_luas_keempat_sisi():
    try:
        s1 = float(txtsisi1.get())
        s2 = float(txtsisi2.get())
        s3 = float(txtsisi3.get())
        s4 = float(txtsisi4.get())
        ls = s1 + s2 + s3 + s4
        txtLS.delete(0, END)
        txtLS.insert(END, round(ls, 2))
    except ValueError:
        txtLS.delete(0, END)
        txtLS.insert(END, "Masukkan angka")

def hitung_volume_limas():
    try:
        alas = float(txtalas.get())
        tinggi_segitiga = float(txttinggi_segitiga.get())
        tinggi_limas = float(txttinggi_limas.get())
        v = (1/3) * (alas * tinggi_segitiga) * tinggi_limas
        txtVolume.delete(0, END)
        txtVolume.insert(END, round(v, 2))
    except ValueError:
        txtVolume.delete(0, END)
        txtVolume.insert(END, "Masukkan angka")

def hitung(event=None):
    hitung_luas_keempat_sisi()
    hitung_volume_limas()

app = tk.Tk()

app.title("Aplikasi Penghitung Luas dan Volume Limas Segitiga")
app.geometry("500x400")
app.configure(bg="#f0f0f0")

frame = Frame(app, bg="#f0f0f0")
frame.pack(padx=20, pady=20)

judul = Label(frame, text="Penghitung Luas Keempat Sisi dan Volume Limas Segitiga", font=("Arial", 12, "bold"), bg="#f0f0f0")
judul.grid(row=0, columnspan=2, pady=10)

sisi1 = Label(frame, text="Sisi 1: ", bg="#f0f0f0")
sisi1.grid(row=1, column=0, sticky=W, padx=5, pady=5)

sisi2 = Label(frame, text="Sisi 2: ", bg="#f0f0f0")
sisi2.grid(row=2, column=0, sticky=W, padx=5, pady=5)

sisi3 = Label(frame, text="Sisi 3: ", bg="#f0f0f0")
sisi3.grid(row=3, column=0, sticky=W, padx=5, pady=5)

sisi4 = Label(frame, text="Sisi 4: ", bg="#f0f0f0")
sisi4.grid(row=4, column=0, sticky=W, padx=5, pady=5)

alas = Label(frame, text="Alas Segitiga: ", bg="#f0f0f0")
alas.grid(row=5, column=0, sticky=W, padx=5, pady=5)

tinggi_segitiga = Label(frame, text="Tinggi Segitiga: ", bg="#f0f0f0")
tinggi_segitiga.grid(row=6, column=0, sticky=W, padx=5, pady=5)

tinggi_limas = Label(frame, text="Tinggi Limas: ", bg="#f0f0f0")
tinggi_limas.grid(row=7, column=0, sticky=W, padx=5, pady=5)

txtsisi1 = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txtsisi1.grid(row=1, column=1)

txtsisi2 = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txtsisi2.grid(row=2, column=1)

txtsisi3 = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txtsisi3.grid(row=3, column=1)

txtsisi4 = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txtsisi4.grid(row=4, column=1)

txtalas = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txtalas.grid(row=5, column=1)

txttinggi_segitiga = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txttinggi_segitiga.grid(row=6, column=1)

txttinggi_limas = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txttinggi_limas.grid(row=7, column=1)

hitung_button = Button(frame, text="Hitung", command=hitung, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
hitung_button.grid(row=8, column=1, sticky=W, padx=5, pady=10)

luas_selimut = Label(frame, text="Luas Keempat Sisi: ", bg="#f0f0f0", font=("Arial", 12))
luas_selimut.grid(row=9, column=0, sticky=W, padx=5, pady=5)

volume = Label(frame, text="Volume Limas: ", bg="#f0f0f0", font=("Arial", 12))
volume.grid(row=10, column=0, sticky=W, padx=5, pady=5)

txtLS = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txtLS.grid(row=9, column=1, sticky=W, padx=5, pady=5)

txtVolume = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txtVolume.grid(row=10, column=1, sticky=W, padx=5, pady=5)

app.bind('<Return>', hitung)  # Menambahkan binding untuk tombol Enter

app.mainloop()