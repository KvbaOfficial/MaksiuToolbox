import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
import webbrowser
import requests
import json

class VirtualPilotToolbox:
    def __init__(self, root):
        self.root = root
        self.root.title("Maksiu Toolbox 737-800")
        self.root.geometry("550x400")
        self.departure_airport = None
        self.arrival_airport = None
        self.create_widgets()
        self.style_widgets()
        self.create_status_bar()
        self.load_settings()
        self.check_api_status()

    def create_widgets(self):
        # Menu bar
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Plik", menu=file_menu)
        file_menu.add_command(label="Ustaw lotniska", command=self.set_airports)
        file_menu.add_separator()
        file_menu.add_command(label="Zapisz ustawienia", command=self.save_settings)
        file_menu.add_command(label="Wczytaj ustawienia", command=self.load_settings)
        file_menu.add_separator()
        file_menu.add_command(label="Wyjdź", command=self.root.quit)

        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Pomoc", menu=help_menu)
        help_menu.add_command(label="O programie", command=self.show_about)

        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        button_frame = ttk.LabelFrame(main_frame, text="Opcje", padding="10")
        button_frame.pack(fill=tk.BOTH, expand=True, pady=5)

        self.create_animated_button(button_frame, "Ustaw lotniska", self.set_airports)
        self.create_animated_button(button_frame, "Pokaż METAR", self.show_metar)
        self.create_animated_button(button_frame, "Otwórz ChartFox", self.open_chartfox)
        self.create_animated_button(button_frame, "Otwórz SimBrief", self.open_simbrief)
        self.create_animated_button(button_frame, "Wyświetl checklistę", self.show_checklist)
        self.create_animated_button(button_frame, "Wyjdź", self.root.quit)

    def create_animated_button(self, parent, text, command):
        button = ttk.Button(parent, text=text, command=command)
        button.pack(fill=tk.X, pady=5)
        button.bind("<Enter>", lambda e: button.configure(style="Hover.TButton"))
        button.bind("<Leave>", lambda e: button.configure(style="TButton"))

    def style_widgets(self):
        style = ttk.Style()
        style.theme_use("clam")

        style.configure("TButton", font=("Helvetica", 12), padding=10, background="#505050", foreground="white")
        style.map("TButton", background=[("active", "#008eb7")])

        style.configure("Hover.TButton", font=("Helvetica", 12), padding=10, background="#008eb7", foreground="white")

        style.configure("TLabelFrame", font=("Helvetica", 14, "bold"), background="#f0f0f0")
        style.configure("TFrame", background="#f0f0f0")

        self.root.configure(background="#f0f0f0")

    def create_status_bar(self):
        self.status_var = tk.StringVar()
        self.status_var.set("Gotowy")
        status_bar = ttk.Label(self.root, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def set_airports(self):
        self.departure_airport = simpledialog.askstring("Lotnisko wylotu", "Podaj kod ICAO lotniska wylotu:")
        self.arrival_airport = simpledialog.askstring("Lotnisko przylotu", "Podaj kod ICAO lotniska przylotu:")
        if self.validate_icao(self.departure_airport) and self.validate_icao(self.arrival_airport):
            messagebox.showinfo("Lotniska ustawione", f"Lotnisko wylotu: {self.departure_airport}\nLotnisko przylotu: {self.arrival_airport}")
        else:
            messagebox.showerror("Błąd", "Nieprawidłowy kod ICAO.")
            self.departure_airport = None
            self.arrival_airport = None

    def validate_icao(self, code):
        return code and len(code) == 4 and code.isalpha()

    def show_metar(self):
        if not self.departure_airport or not self.arrival_airport:
            messagebox.showwarning("Błąd", "Najpierw ustaw lotniska.")
            return

        metar_departure = self.get_metar(self.departure_airport)
        metar_arrival = self.get_metar(self.arrival_airport)

        messagebox.showinfo("METAR", f"METAR {self.departure_airport}:\n{metar_departure}\n\nMETAR {self.arrival_airport}:\n{metar_arrival}")

    def get_metar(self, airport_code):
        api_key = "TWÓJTOKEN"  # AVWX API key
        url = f"https://avwx.rest/api/metar/{airport_code}?token={api_key}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return data.get('raw', 'Brak danych METAR')
        except requests.RequestException:
            return "Błąd pobierania danych METAR"

    def open_chartfox(self):
        if self.departure_airport and self.arrival_airport:
            url = f"https://chartfox.org/{self.departure_airport}"
            webbrowser.open(url)
        else:
            messagebox.showwarning("Błąd", "Najpierw ustaw lotniska.")

    def open_simbrief(self):
        webbrowser.open("https://www.simbrief.com/home/")

    def show_checklist(self):
        webbrowser.open("https://flyuk.aero/assets/downloads/resources/checklists/UKV-PRD-B737-CHECKLIST-V2.pdf")

    def show_about(self):
        messagebox.showinfo("O programie", "Maksiu Toolbox Boeing 737-800\nWersja 1.0\nAutor: Kubuś Developa")

    def save_settings(self):
        settings = {
            "departure_airport": self.departure_airport,
            "arrival_airport": self.arrival_airport
        }
        with open("settings.json", "w") as f:
            json.dump(settings, f)
        self.status_var.set("Ustawienia zapisane")

    def load_settings(self):
        try:
            with open("settings.json", "r") as f:
                settings = json.load(f)
                self.departure_airport = settings.get("departure_airport")
                self.arrival_airport = settings.get("arrival_airport")
            self.status_var.set("Ustawienia wczytane")
        except FileNotFoundError:
            self.status_var.set("Brak zapisanych ustawień")

    def check_api_status(self):
        api_key = "TuShDpiygV8NTcRVWsxUywhsR-8GMrrBvbaQpHbvP74"  # Replace with your AVWX API key
        url = f"https://avwx.rest/api/metar/KJFK?token={api_key}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            self.status_var.set("Połączenie z API: OK")
        except requests.RequestException:
            self.status_var.set("Połączenie z API: Błąd")

if __name__ == "__main__":
    root = tk.Tk()
    app = VirtualPilotToolbox(root)
    root.mainloop()