import tkinter as tk
from tkinter import messagebox
import random

# Renkler ve fontlar
BG_COLOR = "#113e68"
FG_COLOR = "#FFFFFF"
ACCENT_COLOR = "#3bb290"
ERROR_COLOR = "#ff6666"
FONT_NORMAL = ("Helvetica", 14)
FONT_BOLD = ("Helvetica", 14, "bold")

# HammingCode sınıfı, Hamming kodunun hesaplanması, hataların tespiti ve düzeltilmesi ile ilgili işlemleri gerçekleştirir.
class HammingCode:
    def __init__(self, data):
        self.data = data
        self.r = self.calculate_r()  # Parite bitlerinin sayısını hesapla
        self.hamming_code = self.calculate_hamming_code()  # Hamming kodunu oluştur

    def calculate_r(self):
        m = len(self.data)
        r = 0
        # Parite bitlerinin sayısını belirlemek için döngü
        while (2 ** r) < (m + r + 1):
            r += 1
        return r

    def calculate_hamming_code(self):
        n = len(self.data) + self.r
        arr = ['0'] * n
        j = 0
        k = 0

        # Veri ve parite bitlerini yerleştir
        for i in range(n):
            if i == (2 ** j) - 1:
                j += 1
            else:
                arr[i] = self.data[k]
                k += 1

        # Parite bitlerini hesapla ve yerleştir
        for i in range(self.r):
            val = 0
            for j in range(n):
                if (j + 1) & (2 ** i):
                    val ^= int(arr[j])
            arr[(2 ** i) - 1] = str(val)

        return arr

    def detect_error(self):
        n = len(self.hamming_code)
        error_pos = 0
        # Hatalı bit pozisyonunu bulmak için döngü
        for i in range(self.r):
            val = 0
            for j in range(n):
                if (j + 1) & (2 ** i):
                    val ^= int(self.hamming_code[j])
            error_pos += val * (2 ** i)
        return error_pos

    def correct_error(self):
        error_pos = self.detect_error()
        if error_pos != 0:
            index = error_pos - 1
            # Hatalı biti düzelt
            self.hamming_code[index] = str(1 - int(self.hamming_code[index]))
        return self.hamming_code, error_pos

# Ana uygulama sınıfı
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hamming Code Simulator")
        self.geometry("1000x750")
        self.configure(bg=BG_COLOR)
        self.create_widgets()

    # Uygulama widget'larını oluşturma
    def create_widgets(self):
        title_label = tk.Label(self, text="Hamming Code Simulator", font=("Arial", 28, "bold"), bg=BG_COLOR, fg=FG_COLOR)
        title_label.pack(side="top", pady=20)

        main_frame = tk.Frame(self, bg=BG_COLOR)
        main_frame.pack(padx=20, pady=20, fill='both', expand=True)

        input_frame = tk.LabelFrame(main_frame, text="Veri Girişi", font=FONT_BOLD, bg=BG_COLOR, fg=FG_COLOR, padx=20, pady=20)
        input_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        result_frame = tk.LabelFrame(main_frame, text="Sonuçlar", font=FONT_BOLD, bg=BG_COLOR, fg=FG_COLOR, padx=20, pady=20)
        result_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        visual_frame = tk.Frame(main_frame, bg=BG_COLOR, padx=20, pady=20)
        visual_frame.grid(row=1, column=0, columnspan=2, pady=20, sticky="nsew")

        data_label = tk.Label(input_frame, text="Veri:", font=FONT_NORMAL, bg=BG_COLOR, fg=FG_COLOR)
        data_label.grid(row=0, column=0, pady=10, sticky="w")

        self.data_entry = tk.Entry(input_frame, font=FONT_NORMAL)
        self.data_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        length_label = tk.Label(input_frame, text="Uzunluk:", font=FONT_NORMAL, bg=BG_COLOR, fg=FG_COLOR)
        length_label.grid(row=1, column=0, pady=10, sticky="w")

        self.length_var = tk.StringVar(value="8")
        length_options = ["4", "8", "16"]
        length_menu = tk.OptionMenu(input_frame, self.length_var, *length_options)
        length_menu.config(font=FONT_NORMAL, bg=ACCENT_COLOR, fg=FG_COLOR)
        length_menu.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

        calculate_button = tk.Button(input_frame, text="Hesapla", font=FONT_BOLD, bg=ACCENT_COLOR, fg=FG_COLOR, command=self.calculate_hamming_code)
        calculate_button.grid(row=2, column=0, columnspan=2, pady=10, sticky="ew")

        random_button = tk.Button(input_frame, text="Rastgele Veri Oluştur", font=FONT_BOLD, bg=ACCENT_COLOR, fg=FG_COLOR, command=self.generate_random_data)
        random_button.grid(row=3, column=0, columnspan=2, pady=10, sticky="ew")

        error_button = tk.Button(input_frame, text="Rastgele Hata Oluştur", font=FONT_BOLD, bg=ACCENT_COLOR, fg=FG_COLOR, command=self.generate_random_error)
        error_button.grid(row=4, column=0, columnspan=2, pady=10, sticky="ew")

        correct_button = tk.Button(input_frame, text="Hata Düzelt", font=FONT_BOLD, bg=ACCENT_COLOR, fg=FG_COLOR, command=self.correct_error)
        correct_button.grid(row=5, column=0, columnspan=2, pady=10, sticky="ew")

        for i in range(6):
            input_frame.grid_rowconfigure(i, weight=1)
        input_frame.grid_columnconfigure(1, weight=1)

        self.result_label = tk.Label(result_frame, text="", font=FONT_NORMAL, bg=BG_COLOR, fg=FG_COLOR, wraplength=350, justify="left")
        self.result_label.pack(side="top", pady=10, padx=20, anchor='w')

        self.error_label = tk.Label(result_frame, text="", font=FONT_NORMAL, bg=BG_COLOR, fg=FG_COLOR, wraplength=350, justify="left")
        self.error_label.pack(side="top", pady=10, padx=20, anchor='w')

        self.corrected_label = tk.Label(result_frame, text="", font=FONT_NORMAL, bg=BG_COLOR, fg=FG_COLOR, wraplength=350, justify="left")
        self.corrected_label.pack(side="top", pady=10, padx=20, anchor='w')

        self.canvas = tk.Canvas(visual_frame, bg=BG_COLOR, height=200)
        self.canvas.pack(fill='both', expand=True)

    def calculate_hamming_code(self):
        data = self.data_entry.get()
        # Veri girişinin geçerliliğini kontrol et
        if len(data) in {4, 8, 16} and all(bit in '01' for bit in data):
            hamming = HammingCode(data)
            hamming_code = ''.join(hamming.hamming_code)
            self.result_label["text"] = "Hamming Kodu: " + hamming_code
            self.visualize_code(hamming.hamming_code)
            error_pos = hamming.detect_error()
            if error_pos != 0:
                self.error_label["text"] = f"Hata {error_pos}. bitde: {hamming_code}"
                self.corrected_label["text"] = ""
            else:
                self.error_label["text"] = "Hata Yok"
                self.corrected_label["text"] = ""
        else:
            messagebox.showerror("Hata", "Lütfen 4, 8 veya 16 bit uzunluğunda ve sadece 0 ve 1'lerden oluşan bir veri giriniz.")

    def generate_random_data(self):
        length = int(self.length_var.get())
        # Rastgele veri oluştur
        data = ''.join([str(random.randint(0, 1)) for _ in range(length)])
        self.data_entry.delete(0, tk.END)
        self.data_entry.insert(0, data)

    def generate_random_error(self):
        data = self.data_entry.get()
        # Veri girişinin geçerliliğini kontrol et
        if len(data) in {4, 8, 16} and all(bit in '01' for bit in data):
            hamming = HammingCode(data)
            hamming_code = ''.join(hamming.hamming_code)
            # Rastgele bir bit konumunda hata oluştur
            error_bit = random.randint(0, len(hamming_code) - 1)
            hamming_code = list(hamming_code)
            hamming_code[error_bit] = '0' if hamming_code[error_bit] == '1' else '1'
            self.result_label["text"] = "Hamming Kodu: " + ''.join(hamming_code)
            self.visualize_code(hamming_code, error_bit)
            self.error_label["text"] = f"Hata {error_bit+1}. bitde: " + ''.join(hamming_code)
            self.corrected_label["text"] = ""
        else:
            messagebox.showerror("Hata", "Lütfen 4, 8 veya 16 bit uzunluğunda ve sadece 0 ve 1'lerden oluşan bir veri giriniz.")

    def correct_error(self):
        data = self.data_entry.get()
        # Veri girişinin geçerliliğini kontrol et
        if len(data) in {4, 8, 16} and all(bit in '01' for bit in data):
            hamming = HammingCode(data)
            hamming_code = list(self.result_label["text"].split(": ")[1])
            hamming.hamming_code = hamming_code
            corrected_code, error_pos = hamming.correct_error()
            if error_pos != 0:
                self.corrected_label["text"] = "Düzeltilmiş Kod: " + ''.join(corrected_code)
            else:
                self.corrected_label["text"] = "Hata Yok"
        else:
            messagebox.showerror("Hata", "Lütfen 4, 8 veya 16 bit uzunluğunda ve sadece 0 ve 1'lerden oluşan bir veri giriniz.")

    def visualize_code(self, code, error_bit=None):
        self.canvas.delete("all")
        n = len(code)
        rect_width = 40
        gap = 10
        canvas_width = n * (rect_width + gap) + gap
        self.canvas.config(width=canvas_width)

        x0, y0 = gap, 100
        for i in range(n):
            x1 = x0 + i * (rect_width + gap)
            x2 = x1 + rect_width
            y1 = y0
            y2 = y1 + rect_width
            fill_color = ERROR_COLOR if i == error_bit else 'gray'
            self.canvas.create_rectangle(x1, y1, x2, y2, outline='white', fill=fill_color)
            self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=code[i], fill='white')

app = Application()
app.mainloop()
