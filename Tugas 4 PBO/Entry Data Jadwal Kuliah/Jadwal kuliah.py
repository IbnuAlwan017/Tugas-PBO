import tkinter as tk
from tkinter import Label, Entry, Button, Text, END, messagebox

# Fungsi untuk menyimpan data ke file
def simpan_data(nama_file, data):
    with open(nama_file, 'a') as file:
        for item in data:
            file.write(item + '\n')

# Fungsi untuk membaca data dari file
def baca_data(nama_file):
    try:
        with open(nama_file, 'r') as file:
            data = file.readlines()
        return data
    except FileNotFoundError:
        return []

# Fungsi untuk menampilkan jadwal kuliah
def tampilkan_jadwal():
    data_jadwal = baca_data('jadwal.txt')
    jadwal_text.config(state=tk.NORMAL)
    jadwal_text.delete(1.0, tk.END)
    for item in data_jadwal:
        jadwal_text.insert(tk.END, item)
    jadwal_text.config(state=tk.DISABLED)

# Fungsi untuk menyimpan jadwal kuliah
def simpan_jadwal():
    jadwal = [
        "Senin:",
        "1. Komunikasi Data 08.00-09.40",
        "2. Kalkulus II 09.40-11.00",
        "",
        "Selasa:",
        "1. AIK2 08.00-09.40",
        "",
        "Rabu:",
        "1. Arsitektur dan Organisasi Komputer 13.00-15.30",
        "",
        "Kamis:",
        "1. Pemrograman 2 (PBO) 09.00-11.30",
        "",
        "Jumat:",
        "1. Sistem Informasi(APSI) 09.00-11.30",
        "2. Statistik dan Probabilitas 13.00-14.40",
        "",
        "Sabtu:",
        "1. Struktur Data dan Algoritma 08.00-10.30"
    ]

    # Simpan data jadwal ke file
    simpan_data('jadwal.txt', jadwal)

    # Tampilkan jadwal terbaru
    tampilkan_jadwal()

# Membuat GUI
app = tk.Tk()
app.title("Jadwal Kuliah App")
app.geometry("500x500")

label_judul = Label(app, text="Jadwal Kuliah TI22B", font=("Arial", 16, "bold"))
label_judul.pack(pady=10)

btn_simpan = Button(app, text="Simpan Jadwal", command=simpan_jadwal, bg="Green")
btn_simpan.pack(pady=10)

jadwal_text = Text(app, height=20, width=50)
jadwal_text.pack(pady=10)
jadwal_text.config(state=tk.DISABLED)

btn_tampilkan = Button(app, text="Tampilkan Jadwal", command=tampilkan_jadwal)
btn_tampilkan.pack(pady=10)

app.mainloop()