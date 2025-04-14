# Floating App Controller

Floating App Controller adalah aplikasi untuk mengatur jendela-jendela aplikasi di Windows agar tetap berada di atas (always-on-top) atau kembali ke posisi normal (unfloat). Aplikasi ini memungkinkan pengguna untuk memilih jendela yang ingin di-float, mencari jendela berdasarkan keyword, serta menggunakan hotkey untuk mengaktifkan fitur ini secara cepat.

## Fitur Utama

- **Daftar Jendela Aktif**: Menampilkan daftar semua jendela aktif yang sedang berjalan di sistem.
- **Float dan Unfloat Jendela**: Memungkinkan pengguna untuk mengubah status jendela menjadi selalu di atas atau kembali ke posisi normal.
- **Auto-Float Berdasarkan Keyword**: Mencari jendela berdasarkan kata kunci dan mengubah statusnya menjadi float atau unfloat.
- **Hotkey Global**: Menggunakan hotkey `Ctrl + Alt + F` untuk mengubah jendela yang sedang aktif menjadi selalu di atas (float).

## Prasyarat

- Python 3.x
- Library yang dibutuhkan:
  - `tkinter` (terinstal secara default di Python)
  - `keyboard`
  - `pywin32`
  - `Pillow` (jika menggunakan format ikon selain `.ico`)

### Instalasi

1. Install Python 3.x jika belum terpasang. Pastikan untuk mencentang opsi "Add Python to PATH" saat instalasi.
2. Install dependensi menggunakan pip:

   ```bash
   pip install keyboard pywin32 pillow
   ```

````

3. Pastikan kamu memiliki file `favicon.ico` untuk ikon aplikasi atau sesuaikan dengan format lain seperti `.png`.

## Cara Penggunaan

1. Jalankan aplikasi dengan menjalankan script Python `main.py`:

   ```bash
   python main.py
   ```

2. Aplikasi akan menampilkan daftar jendela aktif yang tersedia di sistem.
3. Pilih jendela yang ingin diubah statusnya menjadi **always-on-top** atau **normal** dengan tombol yang tersedia.
4. Gunakan fitur **Auto-Float** untuk mencari dan mem-float jendela berdasarkan keyword.
5. Gunakan hotkey `Ctrl + Alt + F` untuk mem-float jendela aktif saat ini.

## Lisensi

Copyright (c) 2025 Ahmad Haikal Rizal
All rights reserved.

## Credits

Aplikasi ini dibuat oleh Ahmad Haikal Rizal sebagai bagian dari proyek pribadi.

```

### Penjelasan
- **Fitur Utama**: Menyebutkan semua fitur yang ada di aplikasi, termasuk float/unfloat dan penggunaan hotkey.
- **Prasyarat dan Instalasi**: Memberikan instruksi tentang dependensi dan cara instalasi.
- **Cara Penggunaan**: Menginstruksikan bagaimana menjalankan aplikasi dan cara penggunaannya.
- **Lisensi dan Credits**: Memberikan informasi hak cipta dan kredit pembuat.
```
````
