import tkinter as tk
from tkinter import ttk

def show_input():
    user_input = entry.get()
    print(f"Input pengguna: {user_input}")

window = tk.Tk()
entry = ttk.Entry(window)
entry.pack(pady=10)
button = ttk.Button(window, text="Tampilkan Input", command=show_input)
button.pack(pady=10)
window.mainloop()
# Fungsi: Menambahkan input teks dan tombol untuk mengambil nilai.
# Kondisi: Ketika Anda ingin pengguna memasukkan data.