import tkinter as tk
from tkinter import ttk

def show_choice():
    choice = var.get()
    print(f"Pilihan pengguna: {choice}")

window = tk.Tk()
var = tk.StringVar()
radio1 = ttk.Radiobutton(window, text="Opsi 1", variable=var, value="Opsi 1", command=show_choice)
radio2 = ttk.Radiobutton(window, text="Opsi 2", variable=var, value="Opsi 2", command=show_choice)

radio1.pack(pady=10)
radio2.pack(pady=10)
window.mainloop()
# Fungsi: Menambahkan radio buttons untuk membuat pilihan tunggal dengan `ttk`.
# Kondisi: Ketika Anda ingin pengguna memilih satu dari beberapa opsi.