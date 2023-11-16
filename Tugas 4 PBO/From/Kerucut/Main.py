from tkinter import Tk, Frame, Label, Entry, Button, END, W
from Fungsi import hitung, hitung_luas_permukaan, hitung_luas_selimut, hitung_volume

app = Tk()

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
txtr.grid(row=1, column=1, sticky=W, padx=5, pady=5)

txtt = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txtt.grid(row=2, column=1, sticky=W, padx=5, pady=5)

txts = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txts.grid(row=3, column=1, sticky=W, padx=5, pady=5)

hitung_button = Button(frame, text="Hitung", command=lambda: hitung(txtr, txtt, txts, txtLP, txtLS, txtVolume), bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
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

app.bind('<Return>', lambda event: hitung(txtr, txtt, txts, txtLP, txtLS, txtVolume)) 

app.mainloop()