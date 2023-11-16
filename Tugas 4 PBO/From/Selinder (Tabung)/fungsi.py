from tkinter import Tk, Frame, Label, Entry, Button, END, W
import math

def hitung_luas_permukaan(txtr, txtLP):
    try:
        r = float(txtr.get())
        lp = round(2 * math.pi * r * r, 2)
        txtLP.delete(0, END)
        txtLP.insert(END, lp)
    except ValueError:
        txtLP.delete(0, END)
        txtLP.insert(END, "Masukkan angka")

def hitung_luas_selimut(txtr, txtt, txtLS):
    try:
        r = float(txtr.get())
        t = float(txtt.get())
        ls = round(2 * math.pi * r * t, 2)
        txtLS.delete(0, END)
        txtLS.insert(END, ls)
    except ValueError:
        txtLS.delete(0, END)
        txtLS.insert(END, "Masukkan angka")

def hitung_volume(txtr, txtt, txtVolume):
    try:
        r = float(txtr.get())
        t = float(txtt.get())
        volume = round(math.pi * r * r * t, 2)
        txtVolume.delete(0, END)
        txtVolume.insert(END, volume)
    except ValueError:
        txtVolume.delete(0, END)
        txtVolume.insert(END, "Masukkan angka")

def hitung(txtr, txtt, txtLP, txtLS, txtVolume):
    hitung_luas_permukaan(txtr, txtLP)
    hitung_luas_selimut(txtr, txtt, txtLS)
    hitung_volume(txtr, txtt, txtVolume)
