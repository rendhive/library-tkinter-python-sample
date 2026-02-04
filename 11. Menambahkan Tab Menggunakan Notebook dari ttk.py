import tkinter as tk
from tkinter import ttk

window = tk.Tk()
notebook = ttk.Notebook(window)

frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)

notebook.add(frame1, text='Tab 1')
notebook.add(frame2, text='Tab 2')
notebook.pack(pady=10)

label1 = ttk.Label(frame1, text="Isi Tab 1")
label1.pack(pady=10)

label2 = ttk.Label(frame2, text="Isi Tab 2")
label2.pack(pady=10)

window.mainloop()
# Fungsi: Menambahkan antarmuka tab menggunakan widget Notebook.
# Kondisi: Ketika Anda ingin mengelompokkan konten dalam antarmuka pengguna.