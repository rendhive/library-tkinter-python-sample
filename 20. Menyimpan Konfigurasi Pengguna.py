import tkinter as tk
from tkinter import ttk
import json

def save_configuration():
    config = {'username': username_entry.get(), 'theme': theme_entry.get()}
    with open('config.json', 'w') as f:
        json.dump(config, f)
    print("Konfigurasi disimpan.")

window = tk.Tk()
ttk.Label(window, text="Nama Pengguna:").pack(pady=5)
username_entry = ttk.Entry(window)
username_entry.pack(pady=5)

ttk.Label(window, text="Tema:").pack(pady=5)
theme_entry = ttk.Entry(window)
theme_entry.pack(pady=5)

save_button = ttk.Button(window, text="Simpan Konfigurasi", command=save_configuration)
save_button.pack(pady=5)

window.mainloop()
# Fungsi: Menyimpan konfigurasi pengguna ke file JSON.
# Kondisi: Ketika Anda ingin menyimpan preferensi pengguna secara permanen.