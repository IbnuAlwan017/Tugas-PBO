import os
from threading import Thread
from tkinter import Tk, Label, filedialog
from tkinter import ttk  # Menambahkan modul ttk
from pygame import mixer


class MP3Player:
    def __init__(self, master):
        self.master = master
        self.master.title("MP3 Player")
        self.master.minsize(width=400, height=200)

        # Konfigurasi gaya untuk tombol ttk
        style = ttk.Style()
        style.configure('TButton', padding=5, width=15)

        # Label untuk menampilkan nama lagu
        self.current_song_label = Label(master, text="Nama Lagu: ", font=("Helvetica", 12))
        self.current_song_label.pack(pady=10)

        # Tombol untuk memilih lagu
        self.choose_button = ttk.Button(master, text="Pilih Lagu", command=self.choose_song)
        self.choose_button.pack(pady=5)

        # Tombol untuk memutar lagu
        self.play_button = ttk.Button(master, text="Play", command=self.play_song)
        self.play_button.pack(pady=5)

        # Tombol untuk menghentikan pemutaran lagu
        self.stop_button = ttk.Button(master, text="Stop", command=self.stop_song)
        self.stop_button.pack(pady=5)

        # Variabel untuk menyimpan path lagu yang dipilih
        self.song_path = None

        # Variabel status pemutaran
        self.playing = False

        # Thread untuk pemutaran lagu
        self.play_thread = None

    def choose_song(self):
        # Fungsi untuk memilih lagu menggunakan file dialog
        self.song_path = filedialog.askopenfilename(defaultextension=".mp3, .flac", filetypes=[("MP3 files", "*.mp3")])
        self.current_song_label.config(text="Nama Lagu: " + os.path.basename(self.song_path))

    def play_song(self):
        # Fungsi untuk memutar lagu
        if self.song_path:
            if not self.playing:
                # Inisialisasi mixer pygame
                mixer.init()
                # Membuat thread untuk memutar lagu
                self.play_thread = Thread(target=self.play_thread_function)
                self.play_thread.start()
                self.playing = True

    def stop_song(self):
        # Fungsi untuk menghentikan pemutaran lagu
        if self.playing:
            mixer.music.stop()
            self.playing = False

    def play_thread_function(self):
        # Fungsi yang dijalankan pada thread untuk pemutaran lagu
        mixer.music.load(self.song_path)
        mixer.music.play()

        # Menunggu hingga lagu selesai diputar
        while mixer.music.get_busy():
            pass

        # Mengubah status pemutaran menjadi False setelah lagu selesai
        self.playing = False


if __name__ == "__main__":
    # Membuat objek Tkinter
    root = Tk()
    # Membuat objek MP3Player
    player = MP3Player(root)
    # Memulai loop utama Tkinter
    root.mainloop()
