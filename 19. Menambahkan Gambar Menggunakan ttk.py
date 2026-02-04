import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

window = tk.Tk()
image = Image.open("path/to/image.jpg")
photo = ImageTk.PhotoImage(image)

label = ttk.Label(window, image=photo)
label.pack(pady=10)
window.mainloop()
# Fungsi: Menambahkan gambar ke antarmuka menggunakan `ttk`.
# Kondisi: Ketika Anda ingin menampilkan gambar di aplikasi