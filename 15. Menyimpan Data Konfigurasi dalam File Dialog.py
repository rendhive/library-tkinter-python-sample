import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

def save_file():
    file_path = filedialog.asksaveasfilename(title="Simpan Konfigurasi")
    if file_path:
        print(f"Konfigurasi disimpan di: {file_path}")

window = tk.Tk()
save_button = ttk.Button(window, text="Simpan Konfigurasi", command=save_file)
save_button.pack(pady=10)
window.mainloop()
# Fungsi: Menampilkan dialog untuk menyimpan file konfigurasi.
# Kondisi: Ketika Anda ingin membiarkan pengguna memilih lokasi penyimpanan.