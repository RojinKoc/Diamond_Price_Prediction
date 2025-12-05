import tkinter as tk
from tkinter import ttk
import joblib
import numpy as np

model = joblib.load("model.pkl")

cut_dict = {"Fair": 0, "Good": 1, "Very Good": 2, "Premium": 3, "Ideal": 4}
color_dict = {"J": 0, "I": 1, "H": 2, "G": 3, "F": 4, "E": 5, "D": 6}
clarity_dict = {"I1": 0, "SI2": 1, "SI1": 2, "VS2": 3, "VS1": 4, "VVS2": 5, "VVS1": 6, "IF": 7}

def tahmin_et():
    try:
        input_data = np.array([[
            float(entry_carat.get()),
            cut_dict[combo_cut.get()],
            color_dict[combo_color.get()],
            clarity_dict[combo_clarity.get()],
            float(entry_depth.get()),
            float(entry_table.get()),
            float(entry_x.get()),
            float(entry_y.get()),
            float(entry_z.get())
        ]])
        prediction = model.predict(input_data)[0]
        label_sonuc.config(text=f"Tahmini Fiyat: ${prediction:,.2f}")
    except Exception as e:
        label_sonuc.config(text="Hata: " + str(e))

# Pencere ayarları
root = tk.Tk()
root.title("💎 Elmas Fiyat Tahmini")
root.configure(bg="#ffffff")

# Yazı tipi ve renkler
FONT = ("Helvetica", 12)
LABEL_STYLE = {"font": FONT, "bg": "#ffffff", "fg": "#222222"}
ENTRY_STYLE = {"font": FONT, "bg": "#ffffff", "fg": "#000000", "relief": tk.SOLID, "bd": 1}

fields = [
    ("Karat", "entry_carat"),
    ("Derinlik (%)", "entry_depth"),
    ("Taban (%)", "entry_table"),
    ("Uzunluk (x)", "entry_x"),
    ("Genişlik (y)", "entry_y"),
    ("Yükseklik (z)", "entry_z")
]

for i, (label, varname) in enumerate(fields):
    tk.Label(root, text=label, **LABEL_STYLE).grid(row=i, column=0, padx=10, pady=5, sticky="w")
    globals()[varname] = tk.Entry(root, **ENTRY_STYLE)
    globals()[varname].grid(row=i, column=1, padx=10, pady=5)

tk.Label(root, text="Kesim (cut)", **LABEL_STYLE).grid(row=0, column=2, padx=10, pady=5, sticky="w")
combo_cut = ttk.Combobox(root, values=list(cut_dict.keys()), font=FONT, state="readonly")
combo_cut.current(0)
combo_cut.grid(row=0, column=3, padx=10, pady=5)

tk.Label(root, text="Renk (color)", **LABEL_STYLE).grid(row=1, column=2, padx=10, pady=5, sticky="w")
combo_color = ttk.Combobox(root, values=list(color_dict.keys()), font=FONT, state="readonly")
combo_color.current(0)
combo_color.grid(row=1, column=3, padx=10, pady=5)

tk.Label(root, text="Berraklık (clarity)", **LABEL_STYLE).grid(row=2, column=2, padx=10, pady=5, sticky="w")
combo_clarity = ttk.Combobox(root, values=list(clarity_dict.keys()), font=FONT, state="readonly")
combo_clarity.current(0)
combo_clarity.grid(row=2, column=3, padx=10, pady=5)

tk.Button(
    root,
    text="Fiyatı Tahmin Et!",
    font=("Helvetica", 13, "bold"),
    bg="#1f77b4",            # Mavi
    fg="white",
    activebackground="#1f77b4",
    activeforeground="white",
    relief="raised",
    bd=4,
    cursor="hand2",
    command=tahmin_et
).grid(row=7, column=1, pady=20, ipadx=15, ipady=8)

label_sonuc = tk.Label(root, text="Tahmini fiyat burada görünecek.", font=FONT, fg="green", bg="#ffffff")
label_sonuc.grid(row=8, column=0, columnspan=4, pady=10)

# Pencereyi ortala
window_width = 700
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cordinate = int((screen_width / 2) - (window_width / 2))
y_cordinate = int((screen_height / 2) - (window_height / 2))
root.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

root.mainloop()

