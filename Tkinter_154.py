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
   
for nomor in range(1, 11):
       kolom = 0 if nomor <= 5 else 2
       baris = nomor if nomor <= 5 else nomor - 5

       label = tk.Label(frame, text=f"Nilai Mata Pelajaran {nomor}:")
       label.grid(row=baris, column=kolom, sticky="w", padx=(0, 8), pady=4)
  
       input_nilai = tk.Entry(frame, width=10)
       input_nilai.grid(row=baris, column=kolom + 1, padx=(0, 20), pady=4)
  
tombol = tk.Button(
       frame,
       text="Hasil Prediksi",
