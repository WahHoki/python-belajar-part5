# GUI -> Graphical User Interface

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# Membuat jendela utama
window = tk.Tk()
window.configure(bg="lightblue")
window.geometry("300x200")
window.resizable(False, False)
window.title("Aplikasi GUI Sederhana")

# Frame untuk input
input_frame = ttk.Frame(window)
NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()

# variable dan fungsi
def tombol_click():
       nama_depan = NAMA_DEPAN.get()
       nama_belakang = NAMA_BELAKANG.get()
       showinfo(title="Nama lengkap", message=f"Halo, {nama_depan} {nama_belakang}!")


# Penempatan frame dengan pack
input_frame.pack(padx=15, pady=15, fill="x", expand=True)

# Komponen-komponen GUI
# 1. Label nama depan
nama_depan_label = ttk.Label(input_frame, text="Nama Depan:")
nama_depan_label.pack(padx=10, pady=5, fill="x", expand=True)

# 2. Entry (input teks)
nama_depan_entry = ttk.Entry(input_frame, textvariable=NAMA_DEPAN)
nama_depan_entry.pack(padx=10,fill="x", expand=True)


# 3. Label nama belakang
nama_belakang_label = ttk.Label(input_frame, text="Nama Belakang:")
nama_belakang_label.pack(padx=10, pady=5, fill="x", expand=True)

# 4 Entry (input teks)
nama_belakang_entry = ttk.Entry(input_frame, textvariable=NAMA_BELAKANG)
nama_belakang_entry.pack(padx=10,fill="x", expand=True)

# 5. Button (tombol)

tombol_sapa = ttk.Button(input_frame, text="Sapa", command=tombol_click)
tombol_sapa.pack(padx=10, pady=10, fill="x", expand=True)

window.mainloop()
