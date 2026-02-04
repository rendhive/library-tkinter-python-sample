import tkinter as tk
from tkinter import ttk

window = tk.Tk()

ttk.Label(window, text="Nama:").grid(row=0, column=0)
entry1 = ttk.Entry(window)
entry1.grid(row=0, column=1)

ttk.Label(window, text="Usia:").grid(row=1, column=0)
entry2 = ttk.Entry(window)
entry2.grid(row=1, column=1)

window.mainloop()
# Fungsi: Menggunakan layout grid untuk mengatur posisi widget dengan `ttk`.
# Kondisi: Ketika Anda ingin mengatur widget dalam baris dan kolom.