import tkinter as tk
from tkinter import Frame, Label, Entry, Button, END, W, font
import math

def hitung_luas(txtr,txtLuas):
    try:
        r = float(txtr.get())

        luas = round(4 *(math.pi * r **2), 2)
        txtLuas.delete(0, END)
        txtLuas.insert(END, luas)
    except ValueError:
        txtLuas.delete(0, END)
        txtLuas.insert(END, "Masukkan angka")


def hitung_volume(txtr,txtVolume):
    try:
        r = float(txtr.get())
        
        volume = round((4/3) * math.pi * r**3, 2)
        txtVolume.delete(0, END)
        txtVolume.insert(END, volume)
    except ValueError:
        txtVolume.delete(0, END)
        txtVolume.insert(END, "Masukkan angka")


def hitung(txtr,txtLuas,txtVolume):
    hitung_luas(txtr,txtLuas)
    hitung_volume(txtr,txtVolume)