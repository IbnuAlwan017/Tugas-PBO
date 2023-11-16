from tkinter import Tk, Frame, Label, Entry, Button, END, W
from fungsi import hitung, hitung_luas, hitung_volume

app = Tk()

app.title("Penghitung Luas dan Volume Bola")
app.geometry("400x450")
app.configure(bg="#f0f0f0")

frame = Frame(app, bg="#f0f0f0")
frame.pack(padx=20, pady=20)

judul = Label(frame, text="Hitung Luas dan Volume Bola", font=("Times New Roman", 12, "bold"), bg="#f0f0f0")
judul.grid(row=0, columnspan=2, pady=10)

jari_jari = Label(frame, text="Jari-jari: ", bg="#f0f0f0")
jari_jari.grid(row=1, column=0, sticky=W, padx=5, pady=5)

txtr = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txtr.grid(row=1, column=1, sticky=W, padx=5, pady=5)

hitung_button = Button(frame, text="Hitung", command=lambda: hitung(txtr, txtLuas, txtVolume), bg="red", fg="black", font=("Arial", 12, "bold"))
hitung_button.grid(row=2, column=1, sticky=W, padx=5, pady=10)

luas = Label(frame, text="Luas: ", bg="#f0f0f0", font=("Arial", 12))
luas.grid(row=3, column=0, sticky=W, padx=5, pady=5)

volume = Label(frame, text="Volume: ", bg="#f0f0f0", font=("Arial", 12))
volume.grid(row=4, column=0, sticky=W, padx=5, pady=5)

txtLuas = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txtLuas.grid(row=3, column=1, sticky=W, padx=5, pady=5)

txtVolume = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txtVolume.grid(row=4, column=1, sticky=W, padx=5, pady=5)

app.bind('<Return>', lambda event: hitung(txtr, txtLuas, txtVolume)) 

app.mainloop()