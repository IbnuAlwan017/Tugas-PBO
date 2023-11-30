import tkinter as tk
from tkinter import ttk
from gtts import gTTS
import os

def on_enter(e):
    btn.invoke()

def synthesize_text():
    try:
        text = text_input.get('1.0', 'end-1c')
        tts = gTTS(text, lang='id')  # Mengubah bahasa menjadi Indonesia
        tts.save("temp.mp3")
        os.system("start temp.mp3")
    except Exception as e:
        print(e)

app = tk.Tk()
app.title("Text to Speech")
app.geometry("600x400")

style = ttk.Style()
style.configure("TButton", padding=10, font=('Helvetica', 12))

mainframe = ttk.Frame(app, padding="10")
mainframe.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

text_input = tk.Text(mainframe, width=50, height=10, font=('Helvetica', 12))
text_input.grid(column=0, row=0, columnspan=2, pady=10, padx=10, sticky=(tk.W, tk.E))

btn = ttk.Button(mainframe, text="Dengarkan", command=synthesize_text)
btn.grid(column=0, row=1, columnspan=2, pady=10)

app.bind('<Return>', on_enter)
app.mainloop()
