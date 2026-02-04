import tkinter as tk
from tkinter import ttk

window = tk.Tk()

label1 = ttk.Label(window, text="Bagian Atas")
label1.pack(pady=10)

separator = ttk.Separator(window, orient='horizontal')
separator.pack(fill='x', padx=5, pady=10)

label2 = ttk.Label(window, text="Bagian Bawah")
label2.pack(pady=10)

window.mainloop()
# Fungsi: Menambahkan pemisah visual antara konten.
# Kondisi: Ketika Anda ingin memisahkan bagian antarmuka dengan cara visual.