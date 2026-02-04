import tkinter as tk
from tkinter import ttk

def create_window_with_label():
    window = tk.Tk()
    label = ttk.Label(window, text="Selamat Datang!")
    label.pack(pady=10)
    window.mainloop()

create_window_with_label()
# Fungsi: Menambahkan label teks menggunakan `ttk`.
# Kondisi: Ketika Anda ingin menampilkan teks modern di antarmuka.