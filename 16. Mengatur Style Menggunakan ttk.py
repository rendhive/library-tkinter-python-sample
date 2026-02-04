import tkinter as tk
from tkinter import ttk

window = tk.Tk()
style = ttk.Style()
style.configure("TButton", padding=10)

button = ttk.Button(window, text="Tombol yang Distil", style="TButton")
button.pack(pady=10)
window.mainloop()
# Fungsi: Mengatur style untuk memodifikasi tampilan widget.
# Kondisi: Ketika Anda ingin menyesuaikan penampilan elemen antarmuka pengguna.