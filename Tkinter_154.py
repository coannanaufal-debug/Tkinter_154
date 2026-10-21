import tkinter as tk


def tampilkan_hasil():
    hasil_var.set("Prodi Teknologi Informasi")



root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.resizable(False, False)

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

judul = tk.Label(
    frame,
    text="Aplikasi Prediksi Prodi Pilihan",
    font=("Arial", 16, "bold"),
   )
judul.grid(row=0, column=0, columnspan=4, pady=(0, 16))
   
