import tkinter as tk
from tkinter import Frame, Label, Entry, Button, END, W, font
import math

def hitung_luas_permukaan(txtr,txts,txtLP):
    try:
        r = float(txtr.get())
        s = float(txts.get())
        lp = round(math.pi * r * r + math.pi * r * s, 2)
        txtLP.delete(0, END)
        txtLP.insert(END, lp)
    except ValueError:
        txtLP.delete(0, END)
        txtLP.insert(END, "Masukkan angka")

def hitung_luas_selimut(txtr,txts,txtLS):
    try:
        r = float(txtr.get())
        s = float(txts.get())
        ls = round(math.pi * r * s, 2)
        txtLS.delete(0, END)
        txtLS.insert(END, ls)
    except ValueError:
        txtLS.delete(0, END)
        txtLS.insert(END, "Masukkan angka")

def hitung_volume(txtr,txtt,txtVolume):
    try:
        r = float(txtr.get())
        t = float(txtt.get())
        volume = round((1/3) * math.pi * r**2 * t, 2)
        txtVolume.delete(0, END)
        txtVolume.insert(END, volume)
    except ValueError:
        txtVolume.delete(0, END)
        txtVolume.insert(END, "Masukkan angka")


def hitung(txtr,txtt,txts,txtLP,txtLS,txtVolume):
    hitung_luas_permukaan(txtr,txts,txtLP)
    hitung_luas_selimut(txtr,txts,txtLS)
    hitung_volume(txtr,txtt,txtVolume)