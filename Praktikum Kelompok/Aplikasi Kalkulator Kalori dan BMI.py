from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton, MDIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.menu import MDDropdownMenu

class AplikasiKalkulatorKaloriDan(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Teal"
        self.title = "Kalkulator Kalori dan BMI"
        self.root = Builder.load_string(self._dapatkan_kv())
        return self.root

    def _dapatkan_kv(self):
        return '''
BoxLayout:
    orientation: 'vertical'

    BoxLayout:
        orientation: 'horizontal'
        size_hint_y: None
        height: dp(36)
        padding: dp(8)
        spacing: dp(8)
        elevation: 10
        md_bg_color: app.theme_cls.primary_color

        MDLabel:
            text: 'Kalkulator Kalori dan BMI'
            theme_text_color: "Custom"
            text_color: 0, 0, 0, 1
            font_style: 'H6'
            halign: 'center'

    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(1)

        MDTextField:
            id: height
            hint_text: "Tinggi Badan (cm)"
            input_type: "number"
            text_color: 0, 0, 0, 1  # Mengatur warna teks menjadi hitam

        MDTextField:
            id: weight
            hint_text: "Berat Badan (kg)"
            input_type: "number"
            text_color: 0, 0, 0, 1  # Mengatur warna teks menjadi hitam

        MDTextField:
            id: age
            hint_text: "Umur"
            input_type: "number"
            text_color: 0, 0, 0, 1  # Mengatur warna teks menjadi hitam

        BoxLayout:
            orientation: 'horizontal'
            spacing: dp(16)

            MDLabel:
                text: "Jenis Kelamin"
                theme_text_color: "Secondary"
                font_style: 'Subtitle1'

            MDCheckbox:
                group: "gender"
                id: male
                size_hint: None, None
                size: "56dp", "56dp"
                on_release: app.set_gender("L")

            MDLabel:
                text: "Laki-laki"
                theme_text_color: "Secondary"

            MDCheckbox:
                group: "gender"
                id: female
                size_hint: None, None
                size: "56dp", "56dp"
                on_release: app.set_gender("P")

            MDLabel:
                text: "Perempuan"
                theme_text_color: "Secondary"

        BoxLayout:
            orientation: 'horizontal'
            spacing: dp(20)

            MDLabel:
                text: "Aktivitas Harian"
                theme_text_color: "Secondary"
                font_style: 'Subtitle1'

            MDTextField:
                id: activity
                hint_text: "Aktivitas Harian"
                readonly: True
                on_focus: if self.focus: app.show_activity_menu()

        MDRaisedButton:
            text: "Hitung"
            on_release: app.calculate_calories()
            pos_hint: {'center_x': 0.5}
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            md_bg_color: app.theme_cls.primary_color

    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(16)
        spacing: dp(8)

        MDLabel:
            id: result_label
            theme_text_color: "Primary"
            halign: 'center'
            font_style: 'H6'

        MDLabel:
            id: advice_label
            theme_text_color: "Primary"
            halign: 'center'
            font_style: 'H6'

        MDLabel:
            id: bmi_label
            theme_text_color: "Primary"
            halign: 'center'
            font_style: 'H6'

        MDRaisedButton:
            text: "Hitung Ulang"
            on_release: app.reset_calculator()
            pos_hint: {'center_x': 0.5}
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            md_bg_color: app.theme_cls.primary_color
'''

    def calculate_calories(self):
        try:
            height = float(self.root.ids.height.text)
            weight = float(self.root.ids.weight.text)
            age = float(self.root.ids.age.text)

            # Pilihan jenis kelamin
            gender = "L" if self.root.ids.male.active else "P"

            # Pilihan aktivitas
            activity = self.root.ids.activity.text

            # Perhitungan BMI
            bmi = weight / ((height / 100) ** 2)

            # Hitung kebutuhan kalori
            if gender == "L":
                bmr = 10 * weight + 6.25 * height - 5 * age + 5
            elif gender == "P":
                bmr = 10 * weight + 6.25 * height - 5 * age - 161
            else:
                raise ValueError("Jenis kelamin tidak valid. Gunakan 'L' untuk laki-laki atau 'P' untuk perempuan.")

            # Berdasarkan aktivitas harian
            faktor_aktivitas = {
                "Aktivitas Fisik Sangat Minim": 1.2,
                "Olahraga Ringan Kurang Dari 3 Hari Per Minggu": 1.375,
                "Olahraga Sedang Hampir Setiap Hari Dalam Seminggu": 1.55,
                "Olahraga Keras Setiap Hari": 1.725,
                "Olahraga Berat 2 Kali Per Minggu Atau Lebih": 1.9
            }

            tdee = bmr * faktor_aktivitas.get(activity, 1.2)

            # Status berat badan
            status_berat_badan = "Ideal" if 18.5 <= bmi <= 24.9 else "Kurang Ideal"

            # Tampilkan hasil
            hasil_teks = f"Kebutuhan Kalori Harian: {int(tdee)} kkal"
            saran_teks = f"Status Berat Badan: {status_berat_badan}"
            bmi_teks = f"BMI: {bmi:.2f}"

            self.root.ids.result_label.text = hasil_teks
            self.root.ids.advice_label.text = saran_teks
            self.root.ids.bmi_label.text = bmi_teks

        except ValueError as e:
            self.root.ids.result_label.text = "Input tidak valid. Mohon isi semua field dengan benar."
            self.root.ids.advice_label.text = ""
            self.root.ids.bmi_label.text = ""

    def set_gender(self, selected_gender):
        self.root.ids.male.active = selected_gender == "L"
        self.root.ids.female.active = selected_gender == "P"

    def show_activity_menu(self):
        menu_items = [
            {
                "text": "Aktivitas Fisik Sangat Minim",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="Aktivitas Fisik Sangat Minim": self.set_activity(x),
            },
            {
                "text": "Olahraga Ringan Kurang Dari 3 Hari Per Minggu",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="Olahraga Ringan Kurang Dari 3 Hari Per Minggu": self.set_activity(x),
            },
            {
                "text": "Olahraga Sedang Hampir Setiap Hari Dalam Seminggu",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="Olahraga Sedang Hampir Setiap Hari Dalam Seminggu": self.set_activity(x),
            },
            {
                "text": "Olahraga Keras Setiap Hari",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="Olahraga Keras Setiap Hari": self.set_activity(x),
            },
            {
                "text": "Olahraga Berat 2 Kali Per Minggu Atau Lebih",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="Olahraga Berat 2 Kali Per Minggu Atau Lebih": self.set_activity(x),
            },
        ]
        self.menu = MDDropdownMenu(caller=self.root.ids.activity, items=menu_items, width_mult=4)
        self.menu.open()

    def set_activity(self, selected_activity):
        self.root.ids.activity.text = selected_activity
        self.menu.dismiss()

    def reset_calculator(self):
        # Reset semua input field dan label hasil
        self.root.ids.height.text = ""
        self.root.ids.weight.text = ""
        self.root.ids.age.text = ""
        self.root.ids.male.active = False
        self.root.ids.female.active = False
        self.root.ids.activity.text = ""
        self.root.ids.result_label.text = ""
        self.root.ids.advice_label.text = ""
        self.root.ids.bmi_label.text = ""

if __name__ == "__main__":
    AplikasiKalkulatorKaloriDan().run()
