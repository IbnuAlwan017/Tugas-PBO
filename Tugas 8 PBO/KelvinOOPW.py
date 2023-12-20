from tkinter import Frame, Label, Entry, Button, YES, BOTH, END, Tk, W

class FrmSuhu:
    def __init__(self, parent, title):
        self.parent = parent   
        self.parent.geometry("300x200")    
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        
    def aturKomponen(self):
        # Frame dengan padding
        mainFrame = Frame(self.parent, bd=10, relief="ridge", bg="#E6E6E6")
        mainFrame.pack(fill=BOTH, expand=YES)

        # Label untuk unit suhu
        Label(mainFrame, text='Kelvin:', bg="#E6E6E6").grid(row=0, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Celcius:", bg="#E6E6E6").grid(row=2, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Fahrenheit:", bg="#E6E6E6").grid(row=3, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Reamur:", bg="#E6E6E6").grid(row=4, column=0, sticky=W, padx=5, pady=5)

        # Entry untuk input dan output
        self.txtKelvin= Entry(mainFrame)
        self.txtKelvin.grid(row=0, column=1, padx=5, pady=5)
        
        self.txtCelcius = Entry(mainFrame, state='readonly')
        self.txtCelcius.grid(row=2, column=1, padx=5, pady=5)
        
        self.txtFahrenheit = Entry(mainFrame, state='readonly')
        self.txtFahrenheit.grid(row=3, column=1, padx=5, pady=5)
        
        self.txtReamur = Entry(mainFrame, state='readonly')
        self.txtReamur.grid(row=4, column=1, padx=5, pady=5)

        # Tombol untuk perhitungan
        self.btnHitung = Button(mainFrame, text='Hitung', command=self.onHitung, bg="black", fg="white")
        self.btnHitung.grid(row=1, column=1, padx=5, pady=5)

        # Binding tombol Enter ke metode onHitung
        self.parent.bind('<Return>', self.onHitung)

    # Fungsi untuk melakukan konversi suhu
    def onHitung(self, event=None):
        try:
            K = float(self.txtKelvin.get())
            valuec = round((K - 273), 2)
            self.txtCelcius.config(state='normal')
            self.txtCelcius.delete(0, END)
            self.txtCelcius.insert(END, str(valuec))
            self.txtCelcius.config(state='readonly')

            valuef = round(9/5 * (K - 273) + 32, 2)
            self.txtFahrenheit.config(state='normal')
            self.txtFahrenheit.delete(0, END)
            self.txtFahrenheit.insert(END, str(valuef))
            self.txtFahrenheit.config(state='readonly')

            valuer = round(4/5 * (K - 273), 2)
            self.txtReamur.config(state='normal')
            self.txtReamur.delete(0, END)
            self.txtReamur.insert(END, str(valuer))
            self.txtReamur.config(state='readonly')
        except ValueError:
            pass

    # Fungsi untuk menangani penutupan jendela
    def onKeluar(self, event=None):
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = FrmSuhu(root, "Program Konversi Suhu")
    root.mainloop()
