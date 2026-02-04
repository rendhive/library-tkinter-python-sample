import tkinter as tk
from tkinter import ttk

window = tk.Tk()
listbox = tk.Listbox(window)
items = ["Item 1", "Item 2", "Item 3"]
for item in items:
    listbox.insert(tk.END, item)

listbox.pack(pady=10)
window.mainloop()
# Fungsi: Menambahkan listbox untuk memilih dari daftar item.
# Kondisi: Ketika Anda ingin pengguna memilih dari beberapa pilihan.