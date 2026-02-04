import tkinter as tk
from tkinter import ttk

def button_action():
    print("Tombol diklik!")

window = tk.Tk()
button = ttk.Button(window, text="Klik Saya", command=button_action)
button.pack(pady=10)
window.mainloop()
# Fungsi: Menambahkan tombol yang mengaktifkan fungsi ketika diklik.
# Kondisi: Ketika Anda ingin memberikan interaksi kepada pengguna.