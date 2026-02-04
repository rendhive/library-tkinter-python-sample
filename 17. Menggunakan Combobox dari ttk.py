import tkinter as tk
from tkinter import ttk

def show_selected_item(event):
    selected = combobox.get()
    print(f"Item terpilih: {selected}")

window = tk.Tk()
combobox = ttk.Combobox(window, values=["Item 1", "Item 2", "Item 3"])
combobox.bind("<<ComboboxSelected>>", show_selected_item)
combobox.pack(pady=10)
window.mainloop()
# Fungsi: Menambahkan combobox untuk memilih dari daftar item.
# Kondisi: Ketika Anda ingin menyediakan opsi yang lebih ringkas dalam antarmuka.