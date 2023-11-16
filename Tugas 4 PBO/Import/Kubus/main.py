import tkinter as tk
from tkinter import Frame, Label, Entry, Button, END, W, font
import fungsi
def hitung_luas():
    r = float(txtr.get())
    luas = fungsi.hitung_luas(r)
    txtLuas.delete(0, END)
    txtLuas.insert(END, luas)


def hitung_volume():
    r = float(txtr.get())
    volume = fungsi.hitung_volume(r)
    txtVolume.delete(0, END)
    txtVolume.insert(END, volume)

def hitung(event=None):
    hitung_luas()
    hitung_volume()

app = tk.Tk()

app.title("Penghitung Luas dan Volume Kubus")
app.geometry("400x300")
app.configure(bg="#f0f0f0")

frame = Frame(app, bg="#f0f0f0")
frame.pack(padx=20, pady=20)

judul = Label(frame, text="Hitung Luas dan Volume Kubus", font=("Arial", 12, "bold"), bg="#f0f0f0")
judul.grid(row=0, columnspan=2, pady=10)

rusuk = Label(frame, text="Panjang Rusuk: ", bg="#f0f0f0")
rusuk.grid(row=1, column=0, sticky=W, padx=5, pady=5)

txtr = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txtr.grid(row=1, column=1)

hitung_button = Button(frame, text="Hitung", command=hitung, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
hitung_button.grid(row=2, column=1, sticky=W, padx=5, pady=10)

luas = Label(frame, text="Luas: ", bg="#f0f0f0", font=("Arial", 12))
luas.grid(row=3, column=0, sticky=W, padx=5, pady=5)

volume = Label(frame, text="Volume: ", bg="#f0f0f0", font=("Arial", 12))
volume.grid(row=4, column=0, sticky=W, padx=5, pady=5)

txtLuas = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txtLuas.grid(row=3, column=1, sticky=W, padx=5, pady=5)

txtVolume = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txtVolume.grid(row=4, column=1, sticky=W, padx=5, pady=5)

app.bind('<Return>', hitung)  # Menambahkan binding untuk tombol Enter

app.mainloop()