# 📘 Dokumentasi Aplikasi

Aplikasi ini terdiri dari tiga fitur utama: konversi harga mata uang kripto, pengecekan harga real-time dari CoinMarketCap, dan tampilan informasi cuaca menggunakan API. Berikut penjelasan masing-masing menu dan cara penggunaannya.

---

## 🛍 Menu Navigasi

1. **HOME** – Halaman utama aplikasi, menampilkan fitur *Price Converter*
2. **(Realtime) CEK HARGA** – Mengecek harga aset dari CoinMarketCap secara real-time atau cache
3. **(Flet) APLIKASI CUACA** – Mengakses aplikasi cuaca berbasis modul Flet
4. **Dokumentasi** – Menampilkan penjelasan penggunaan aplikasi
5. **Tentang** – Informasi tentang tim pengembang

---

## 🔄 Fitur 1: Price Converter

### 📌 Cara Menggunakan:

1. **Input Data**

   * Simbol Asal (contoh: BTC)
   * Simbol Konversi (contoh: IDR)
   * Jumlah yang ingin dikonversi

2. **Proses Konversi**

   * Klik tombol **HITUNG** untuk mengirim request ke API dan memperoleh hasil konversi.

3. **Hasil**

   * Nilai konversi dalam satuan IDR Rupiah
   * Data diambil secara **real-time**

---



## 📈 Fitur 2: Cek Harga Realtime

### 📌 Cara Menggunakan:

1. **Input Data**

   * Jumlah data yang ingin ditampilkan (maksimal 5000)
   * Peringkat awal (sort berdasarkan peringkat CoinMarketCap)

2. **Proses Data**

   * Klik tombol **Proses Data** untuk mengambil data harga

3. **Hasil**

   * Menampilkan tabel berisi peringkat, nama aset, simbol, dan harga (Rp)
   * Terdapat waktu server saat request dilakukan

---



## 🌦️ Fitur 3: Aplikasi Cuaca

### ⚖️ Fitur Utama:

* Menampilkan cuaca terkini berdasarkan lokasi pengguna
* Perkiraan cuaca mingguan
* Lokasi otomatis berbasis GPS (jika diizinkan)
* Informasi detail seperti suhu, kelembapan, kecepatan angin, dll

### 📌 Cara Menggunakan:

* Pilih lokasi kota atau wilayah
* Data cuaca akan diambil dari API dan ditampilkan secara real-time

---

> 📌 *Dokumentasi ini digunakan sebagai panduan penggunaan aplikasi berbasis Python GUI untuk keperluan tugas akhir atau presentasi pengembangan perangkat lunak.*