import tkinter as tk
from tkinter import ttk

def setup_frame_with_widgets():
    frame = ttk.Frame(window)
    frame.pack(padx=10, pady=10)

    label = ttk.Label(frame, text="Masukkan Nama:")
    label.pack()

    entry = ttk.Entry(frame)
    entry.pack()

    button = ttk.Button(frame, text="Kirim", command=lambda: print(entry.get()))
    button.pack()

window = tk.Tk()
setup_frame_with_widgets()
window.mainloop()
# Fungsi: Menggabungkan semua widget ke dalam satu frame untuk organisasi yang lebih baik.
# Kondisi: Ketika Anda ingin mengatur layout dengan lebih terstruktur.