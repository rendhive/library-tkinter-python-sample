import tkinter as tk
from tkinter import ttk

def update_status(message):
    status_var.set(message)

window = tk.Tk()
status_var = tk.StringVar()
statusbar = ttk.Label(window, textvariable=status_var, relief=tk.SUNKEN, anchor='w')
statusbar.pack(side=tk.BOTTOM, fill=tk.X)
update_status("Aplikasi siap!")

window.mainloop()
# Fungsi: Menambahkan status bar untuk menampilkan pesan status.
# Kondisi: Ketika Anda ingin memberikan pembaruan kepada pengguna tentang status aplikasi.