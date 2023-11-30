import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import pytesseract

class TextExtractorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Text Extractor")
        self.master.geometry("600x400")

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="Pilih gambar untuk ekstraksi teks:")
        self.label.pack(pady=10)

        self.image_path = ""
        self.image_label = tk.Label(self.master)
        self.image_label.pack(pady=10)

        self.browse_button = tk.Button(self.master, text="Pilih Gambar", command=self.browse_image)
        self.browse_button.pack()

        self.extract_button = tk.Button(self.master, text="Ekstrak Teks", command=self.extract_text)
        self.extract_button.pack(pady=10)

        self.result_text = tk.Text(self.master, height=10, width=60)
        self.result_text.pack()

    def browse_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp")])
        if file_path:
            self.image_path = file_path
            image = Image.open(file_path)
            image.thumbnail((300, 300))
            photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo)
            self.image_label.image = photo

    def extract_text(self):
        if self.image_path:
            image = Image.open(self.image_path)
            text = pytesseract.image_to_string(image)
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, text)
        else:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "Pilih gambar terlebih dahulu.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TextExtractorApp(root)
    root.mainloop()
