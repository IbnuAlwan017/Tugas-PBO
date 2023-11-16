import tkinter as tk
from tkinter import Frame, Label, Entry, Button, END, W, font
import math

def hitung_luas(txtls1,txtls2,txtls3,txtls4,txtLuas):
    try:
        ls1 = float(txtls1.get())
        ls2 = float(txtls2.get())
        ls3 = float(txtls3.get())
        ls4 = float(txtls4.get())
        luas = ls1 + ls2 + ls3 + ls4
        txtLuas.delete(0, END)
        txtLuas.insert(END, round(luas, 2))
    except ValueError:
        txtLuas.delete(0, END)
        txtLuas.insert(END, "Masukkan angka")


def hitung_volume(txtalas,txttinggi_segitiga,txttinggi_limas,txtVolume):
    try:
        a = float(txtalas.get())
        t = float(txttinggi_segitiga.get())
        T = float(txttinggi_limas.get())
        v = (1/3) * (a * t) * T
        txtVolume.delete(0, END)
        txtVolume.insert(END, round(v, 2))
    except ValueError:
        txtVolume.delete(0, END)
        txtVolume.insert(END, "Masukkan angka")


def hitung(txtls1,txtls2,txtls3,txtls4,txtLuas,txtalas,txttinggi_segitiga,txttinggi_limas,txtVolume):
    hitung_luas(txtls1,txtls2,txtls3,txtls4,txtLuas)
    hitung_volume(txtalas,txttinggi_segitiga,txttinggi_limas,txtVolume)