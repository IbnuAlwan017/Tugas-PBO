import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from moviepy.editor import VideoFileClip

class VideoPlayerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pemutar Video")

        # Variabel untuk menyimpan path file video
        self.video_path = tk.StringVar()

        # Frame untuk menempatkan elemen-elemen GUI
        self.frame = ttk.Frame(root, padding="10")
        self.frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Button untuk memilih video
        self.browse_button = ttk.Button(self.frame, text="Pilih Video", command=self.browse_file)
        self.browse_button.grid(column=0, row=0, columnspan=2, pady=10)

        # Label untuk menampilkan path file video
        self.path_label = ttk.Label(self.frame, textvariable=self.video_path)
        self.path_label.grid(column=0, row=1, columnspan=2)

        # Button untuk memutar video
        self.play_button = ttk.Button(self.frame, text="Putar", command=self.play_video)
        self.play_button.grid(column=0, row=2, pady=10)

        # Button untuk menghentikan pemutaran video
        self.stop_button = ttk.Button(self.frame, text="Stop", command=self.stop_video)
        self.stop_button.grid(column=1, row=2, pady=10)

    def browse_file(self):
        # Membuka dialog untuk memilih file video
        file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4;*.avi;*.mkv")])

        # Menyimpan path file video ke dalam variable
        self.video_path.set(file_path)

    def play_video(self):
        # Mengambil path file video dari variable
        video_file = self.video_path.get()

        # Memutar video menggunakan moviepy
        video_clip = VideoFileClip(video_file)
        video_clip.preview()

    def stop_video(self):
        # Do nothing for now
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoPlayerApp(root)
    root.mainloop()
