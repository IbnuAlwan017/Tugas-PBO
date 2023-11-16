import tkinter as tk
from tkinter import Frame, Label, Entry, Button, END, W
import FungsiLimasSegiempat

def hitung_luas():
    ls1 = float(txtls1.get())
    ls2 = float(txtls2.get())
    ls3 = float(txtls3.get())
    ls4 = float(txtls4.get())
    ls5 = float(txtls5.get())

    luas = FungsiLimasSegiempat.hitung_luas(ls1, ls2, ls3, ls4, ls5)
    txtLuas.delete(0, END)
    txtLuas.insert(END, luas)

def hitung_volume():
    La = float(txtLa.get())
    T = float(txtTl.get())

    volume = FungsiLimasSegiempat.hitung_volume(La, T)
    txtVolume.delete(0, END)
    txtVolume.insert(END, volume)

def hitung(event=None):
    hitung_luas()
    hitung_volume()

app = tk.Tk()

app.title("Aplikasi Penghitung Luas dan Volume Limas Segiempat")
app.geometry("450x450")
app.configure(bg="#f0f0f0")

frame = Frame(app, bg="#f0f0f0")
frame.pack(padx=20, pady=20)

judul = Label(frame, text="Penghitung Luas dan Volume Limas Segiempat", font=("Arial", 14, "bold"), bg="#f0f0f0")
judul.grid(row=0, columnspan=2, pady=10)

ls1 = Label(frame, text="Luas Sisi1 nya : ", bg="#f0f0f0")
ls1.grid(row=1, column=0, sticky=W, padx=5, pady=5)

ls2 = Label(frame, text="Luas Sisi2 nya: ", bg="#f0f0f0")
ls2.grid(row=2, column=0, sticky=W, padx=5, pady=5)

ls3 = Label(frame, text="Luas Sisi3 nya: ", bg="#f0f0f0")
ls3.grid(row=3, column=0, sticky=W, padx=5, pady=5)

ls4 = Label(frame, text="Luas Sisi4 nya: ", bg="#f0f0f0")
ls4.grid(row=4, column=0, sticky=W, padx=5, pady=5)

ls5 = Label(frame, text="Luas Sisi5 nya: ", bg="#f0f0f0")
ls5.grid(row=5, column=0, sticky=W, padx=5, pady=5)

La = Label(frame, text="Luas Alas nya: ", bg="#f0f0f0")
La.grid(row=6, column=0, sticky=W, padx=5, pady=5)

T = Label(frame, text="Tinggi Limas nya: ", bg="#f0f0f0")
T.grid(row=7, column=0, sticky=W, padx=5, pady=5)

txtls1 = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txtls1.grid(row=1, column=1, sticky=W, padx=5, pady=5)

txtls2 = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txtls2.grid(row=2, column=1, sticky=W, padx=5, pady=5)

txtls3 = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txtls3.grid(row=3, column=1, sticky=W, padx=5, pady=5)

txtls4 = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txtls4.grid(row=4, column=1, sticky=W, padx=5, pady=5)

txtls5 = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txtls5.grid(row=5, column=1, sticky=W, padx=5, pady=5)

txtLa = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txtLa.grid(row=6, column=1, sticky=W, padx=5, pady=5)

txtTl = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txtTl.grid(row=7, column=1, sticky=W, padx=5, pady=5)

hitung_button = Button(frame, text="Hitung", command=hitung, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
hitung_button.grid(row=8, column=1, sticky=W, padx=5, pady=10)

luas = Label(frame, text="Luas: ", bg="#f0f0f0", font=("Arial", 12))
luas.grid(row=9, column=0, sticky=W, padx=5, pady=5)

volume = Label(frame, text="Volume: ", bg="#f0f0f0", font=("Arial", 12))
volume.grid(row=10, column=0, sticky=W, padx=5, pady=5)

txtLuas = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txtLuas.grid(row=9, column=1, sticky=W, padx=5, pady=5)

txtVolume = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txtVolume.grid(row=10, column=1, sticky=W, padx=5, pady=5)

app.bind('<Return>', hitung)  # Menambahkan binding untuk tombol Enter

app.mainloop()