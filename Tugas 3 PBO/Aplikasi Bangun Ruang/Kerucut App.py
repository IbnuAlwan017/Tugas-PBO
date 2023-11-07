import tkinter as tk
from tkinter import Frame, Label, Entry, Button, END, W, font
import math

def hitung_luas_permukaan():
    try:
        r = float(txtr.get())
        s = float(txts.get())
        lp = round(math.pi * r * r + math.pi * r * s, 2)
        txtLP.delete(0, END)
        txtLP.insert(END, lp)
    except ValueError:
        txtLP.delete(0, END)
        txtLP.insert(END, "Masukkan angka")

def hitung_luas_selimut():
    try:
        r = float(txtr.get())
        s = float(txts.get())
        ls = round(math.pi * r * s, 2)
        txtLS.delete(0, END)
        txtLS.insert(END, ls)
    except ValueError:
        txtLS.delete(0, END)
        txtLS.insert(END, "Masukkan angka")

def hitung_volume():
    try:
        r = float(txtr.get())
        t = float(txtt.get())
        volume = round((1/3) * math.pi * r**2 * t, 2)
        txtVolume.delete(0, END)
        txtVolume.insert(END, volume)
    except ValueError:
        txtVolume.delete(0, END)
        txtVolume.insert(END, "Masukkan angka")


def hitung(event=None):
    hitung_luas_permukaan()
    hitung_luas_selimut()
    hitung_volume()

app = tk.Tk()

app.title("Penghitung Luas Selimut, Luas Permukaan, dan Volume Kerucut")
app.geometry("400x450")
app.configure(bg="#f0f0f0")

frame = Frame(app, bg="#f0f0f0")
frame.pack(padx=20, pady=20)

judul = Label(frame, text="Hitung Luas Selimut, Luas Permukaan, dan Volume Kerucut", font=("Arial", 12, "bold"), bg="#f0f0f0")
judul.grid(row=0, columnspan=2, pady=10)

jari_jari = Label(frame, text="Jari-jari: ", bg="#f0f0f0")
jari_jari.grid(row=1, column=0, sticky=W, padx=5, pady=5)

tinggi = Label(frame, text="Tinggi: ", bg="#f0f0f0")
tinggi.grid(row=2, column=0, sticky=W, padx=5, pady=5)

s = Label(frame, text="S: ", bg="#f0f0f0")
s.grid(row=3, column=0, sticky=W, padx=5, pady=5)

txtr = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txtr.grid(row=1, column=1)

txtt = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txtt.grid(row=2, column=1)

txts = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txts.grid(row=3, column=1)

hitung_button = Button(frame, text="Hitung", command=hitung, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
hitung_button.grid(row=4, column=1, sticky=W, padx=5, pady=10)

luas_permukaan = Label(frame, text="Luas Permukaan: ", bg="#f0f0f0", font=("Arial", 12))
luas_permukaan.grid(row=5, column=0, sticky=W, padx=5, pady=5)

luas_selimut = Label(frame, text="Luas Selimut: ", bg="#f0f0f0", font=("Arial", 12))
luas_selimut.grid(row=6, column=0, sticky=W, padx=5, pady=5)

volume = Label(frame, text="Volume: ", bg="#f0f0f0", font=("Arial", 12))
volume.grid(row=7, column=0, sticky=W, padx=5, pady=5)

txtLP = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txtLP.grid(row=5, column=1, sticky=W, padx=5, pady=5)

txtLS = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txtLS.grid(row=6, column=1, sticky=W, padx=5, pady=5)

txtVolume = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txtVolume.grid(row=7, column=1, sticky=W, padx=5, pady=5)

app.bind('<Return>', hitung)  # Menambahkan binding untuk tombol Enter

app.mainloop()