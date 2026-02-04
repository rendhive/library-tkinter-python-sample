import tkinter as tk
from tkinter import ttk

def show_notification():
    notification = tk.Toplevel(window)
    notification.title("Notifikasi")
    label = ttk.Label(notification, text="Ini adalah notifikasi.")
    label.pack(pady=10)
    button = ttk.Button(notification, text="Tutup", command=notification.destroy)
    button.pack(pady=10)

window = tk.Tk()
notify_button = ttk.Button(window, text="Tampilkan Notifikasi", command=show_notification)
notify_button.pack(pady=10)
window.mainloop()
# Fungsi: Menampilkan dialog notifikasi menggunakan Toplevel.
# Kondisi: Ketika Anda ingin memberikan perhatian khusus kepada pengguna dengan pesan.