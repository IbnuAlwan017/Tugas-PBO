import tkinter as tk
from tkinter import Frame, Label, Entry, Button, END, W, font

def hitung_luas():
    try:
        p = float(txtpanjang.get())
        l = float(txtlebar.get())
        t = float(txttinggi.get())
        luas = round(2 * (p * l + p * t + l * t), 2)
        txtLuas.delete(0, END)
        txtLuas.insert(END, luas)
    except ValueError:
        txtLuas.delete(0, END)
        txtLuas.insert(END, "Masukkan angka")

def hitung_volume():
    try:
        p = float(txtpanjang.get())
        l = float(txtlebar.get())
        t = float(txttinggi.get())
        volume = round(p * l * t, 2)
        txtVolume.delete(0, END)
        txtVolume.insert(END, volume)
    except ValueError:
        txtVolume.delete(0, END)
        txtVolume.insert(END, "Masukkan angka")

def hitung(event=None):
    hitung_luas()
    hitung_volume()

app = tk.Tk()

app.title("Aplikasi Penghitung Luas dan Volume Balok")
app.geometry("400x350")
app.configure(bg="#f0f0f0")

frame = Frame(app, bg="#f0f0f0")
frame.pack(padx=20, pady=20)

judul = Label(frame, text="Penghitung Luas dan Volume Balok", font=("Arial", 14, "bold"), bg="#f0f0f0")
judul.grid(row=0, columnspan=2, pady=10)

panjang = Label(frame, text="Panjang: ", bg="#f0f0f0")
panjang.grid(row=1, column=0, sticky=W, padx=5, pady=5)

lebar = Label(frame, text="Lebar: ", bg="#f0f0f0")
lebar.grid(row=2, column=0, sticky=W, padx=5, pady=5)

tinggi = Label(frame, text="Tinggi: ", bg="#f0f0f0")
tinggi.grid(row=3, column=0, sticky=W, padx=5, pady=5)

txtpanjang = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txtpanjang.grid(row=1, column=1)

txtlebar = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txtlebar.grid(row=2, column=1)

txttinggi = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txttinggi.grid(row=3, column=1)

hitung_button = Button(frame, text="Hitung", command=hitung, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
hitung_button.grid(row=4, column=1, sticky=W, padx=5, pady=10)

luas = Label(frame, text="Luas: ", bg="#f0f0f0", font=("Arial", 12))
luas.grid(row=5, column=0, sticky=W, padx=5, pady=5)

volume = Label(frame, text="Volume: ", bg="#f0f0f0", font=("Arial", 12))
volume.grid(row=6, column=0, sticky=W, padx=5, pady=5)

txtLuas = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txtLuas.grid(row=5, column=1, sticky=W, padx=5, pady=5)

txtVolume = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txtVolume.grid(row=6, column=1, sticky=W, padx=5, pady=5)

app.bind('<Return>', hitung)  # Menambahkan binding untuk tombol Enter

app.mainloop()