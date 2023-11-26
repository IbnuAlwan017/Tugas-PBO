import tkinter as tk

class TemperatureConverterApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Aplikasi Konversi Suhu")

        self.current_unit = tk.StringVar(value="Pilih Pengkonversian")

        self.create_widgets()

    def create_widgets(self):
        # Judul aplikasi
        self.title_label = tk.Label(self.master, text="Aplikasi Konversi Suhu", font=("Arial", 16, "bold"))
        self.title_label.grid(row=0, column=0, columnspan=3, pady=10)

        # Entry untuk input pengguna
        self.input_entry = tk.Entry(self.master, width=15)
        self.input_entry.grid(row=1, column=0, padx=10, pady=10)

        # Label unit suhu
        self.label_unit = tk.Label(self.master, textvariable=self.current_unit)
        self.label_unit.grid(row=1, column=1, padx=10, pady=10)

        # Label hasil konversi
        self.label_result = tk.Label(self.master, text="Hasil:")
        self.label_result.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

        # Tombol konversi
        self.convert_button = tk.Button(self.master, text="Konversi", command=self.convert_temperature)
        self.convert_button.grid(row=3, column=0, columnspan=3, pady=10)

        # Menu pilihan untuk unit suhu
        self.unit_menu = tk.StringVar(value="Pilih Pengkonversian")
        self.unit_menu_options = ["Pilih Pengkonversian", "Celsius ke Fahrenheit", "Fahrenheit ke Celsius",
                                  "Celsius ke Kelvin", "Fahrenheit ke Kelvin", "Kelvin ke Celsius",
                                  "Kelvin ke Fahrenheit"]

        self.unit_menu_dropdown = tk.OptionMenu(self.master, self.unit_menu, *self.unit_menu_options, command=self.update_input_description)
        self.unit_menu_dropdown.grid(row=4, column=0, columnspan=3, pady=10)

    def update_input_description(self, event=None):
        selected_option = self.unit_menu.get()
        if selected_option != "Pilih Pengkonversian":
            input_description = selected_option.split(" ke ")[0]
            self.current_unit.set(f"{input_description}")
        else:
            self.current_unit.set("Pilih Pengkonversian")

    def convert_temperature(self):
        try:
            temperature = float(self.input_entry.get())
            result = 0.0

            current_option = self.unit_menu.get()

            if current_option == "Pilih Pengkonversian":
                self.label_result.config(text="Pilih pengkonversian terlebih dahulu.")
                self.current_unit.set("")
                return

            if "Celsius ke Fahrenheit" in current_option:
                result = (temperature * 9/5) + 32
                unit_symbol = "°F"
            elif "Fahrenheit ke Celsius" in current_option:
                result = (temperature - 32) * 5/9
                unit_symbol = "°C"
            elif "Celsius ke Kelvin" in current_option:
                result = temperature + 273.15
                unit_symbol = "K"
            elif "Fahrenheit ke Kelvin" in current_option:
                result = (temperature - 32) * 5/9 + 273.15
                unit_symbol = "K"
            elif "Kelvin ke Celsius" in current_option:
                result = temperature - 273.15
                unit_symbol = "°C"
            elif "Kelvin ke Fahrenheit" in current_option:
                result = (temperature - 273.15) * 9/5 + 32
                unit_symbol = "°F"

            result_text = f"Hasil: {result:.2f} {unit_symbol}"
            self.label_result.config(text=result_text)
        except ValueError:
            self.label_result.config(text="Input tidak valid. Harap masukkan angka.")
            self.current_unit.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = TemperatureConverterApp(root)
    root.mainloop()
