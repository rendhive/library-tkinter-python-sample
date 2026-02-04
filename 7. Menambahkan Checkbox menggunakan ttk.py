import tkinter as tk
from tkinter import ttk

def show_checked_status():
    if var.get():
        print("Checkbox dicentang!")
    else:
        print("Checkbox tidak dicentang.")

window = tk.Tk()
var = tk.BooleanVar()
checkbox = ttk.Checkbutton(window, text="Setuju", variable=var, command=show_checked_status)
checkbox.pack(pady=10)
window.mainloop()
# Fungsi: Menambahkan checkbox dan menampilkan statusnya saat diklik.
# Kondisi: Ketika Anda ingin mendapatkan persetujuan pengguna.