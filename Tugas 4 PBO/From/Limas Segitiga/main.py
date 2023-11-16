from tkinter import Tk, Frame, Label, Entry, Button, END, W
from fungsi import hitung, hitung_luas, hitung_volume

app = Tk()

app.title("Penghitung Luas dan Volume Limas Segitiga")
app.geometry("400x450")
app.configure(bg="#f0f0f0")

frame = Frame(app, bg="#f0f0f0")
frame.pack(padx=20, pady=20)

judul = Label(frame, text="Hitung Luas dan Volume Limas Segitiga", font=("Times New Roman", 12, "bold"), bg="#f0f0f0")
judul.grid(row=0, columnspan=2, pady=10)

ls1 = Label(frame, text="Luas sisi 1 nya: ", bg="#f0f0f0")
ls1.grid(row=1, column=0, sticky=W, padx=5, pady=5)

ls2 = Label(frame, text="Luas sisi 2 nya: ", bg="#f0f0f0")
ls2.grid(row=2, column=0, sticky=W, padx=5, pady=5)

ls3 = Label(frame, text="Luas sisi 3 nya: ", bg="#f0f0f0")
ls3.grid(row=3, column=0, sticky=W, padx=5, pady=5)

ls4 = Label(frame, text="Luas sisi 4 nya: ", bg="#f0f0f0")
ls4.grid(row=4, column=0, sticky=W, padx=5, pady=5)

a = Label(frame, text="Alas Segitiganya: ", bg="#f0f0f0")
a.grid(row=5, column=0, sticky=W, padx=5, pady=5)

t = Label(frame, text="Tinggi Segitiganya: ", bg="#f0f0f0")
t.grid(row=6, column=0, sticky=W, padx=5, pady=5)

T = Label(frame, text="Tinggi Limasnya: ", bg="#f0f0f0")
T.grid(row=7, column=0, sticky=W, padx=5, pady=5)

txtls1 = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txtls1.grid(row=1, column=1, sticky=W, padx=5, pady=5)

txtls2 = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txtls2.grid(row=2, column=1, sticky=W, padx=5, pady=5)

txtls3 = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txtls3.grid(row=3, column=1, sticky=W, padx=5, pady=5)

txtls4 = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txtls4.grid(row=4, column=1, sticky=W, padx=5, pady=5)

txtalas = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txtalas.grid(row=5, column=1, sticky=W, padx=5, pady=5)

txttinggi_segitiga = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txttinggi_segitiga.grid(row=6, column=1, sticky=W, padx=5, pady=5)

txttinggi_limas = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txttinggi_limas.grid(row=7, column=1, sticky=W, padx=5, pady=5)

hitung_button = Button(frame, text="Hitung", command=lambda: hitung(txtls1,txtls2,txtls3,txtls4,txtLuas,txtalas,txttinggi_segitiga,txttinggi_limas,txtVolume), bg="grey", fg="white", font=("Montserrat", 12, "bold"))
hitung_button.grid(row=8, column=1, sticky=W, padx=5, pady=10)

luas = Label(frame, text="Luas: ", bg="#f0f0f0", font=("Arial", 12))
luas.grid(row=9, column=0, sticky=W, padx=5, pady=5)

volume = Label(frame, text="Volume: ", bg="#f0f0f0", font=("Arial", 12))
volume.grid(row=10, column=0, sticky=W, padx=5, pady=5)

txtLuas = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txtLuas.grid(row=9, column=1, sticky=W, padx=5, pady=5)

txtVolume = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txtVolume.grid(row=10, column=1, sticky=W, padx=5, pady=5)

app.bind('<Return>', lambda event: hitung(txtls1,txtls2,txtls3,txtls4,txtLuas,txtalas,txttinggi_segitiga,txttinggi_limas,txtVolume)) 

app.mainloop()