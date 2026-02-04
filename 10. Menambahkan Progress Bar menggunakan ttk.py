import tkinter as tk
from tkinter import ttk
import time

def start_progress():
    progress['value'] = 0
    for i in range(101):
        progress['value'] = i
        window.update()
        time.sleep(0.05)

window = tk.Tk()
progress = ttk.Progressbar(window, orient='horizontal', length=300, mode='determinate')
progress.pack(pady=10)
button = ttk.Button(window, text="Mulai", command=start_progress)
button.pack(pady=10)
window.mainloop()
# Fungsi: Menggunakan progress bar untuk menunjukkan kemajuan.
# Kondisi: Ketika Anda ingin menunjukkan status proses yang berjalan.