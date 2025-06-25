# 🪙 SuperApps: Price Converter, Cek Harga Cryptocurrency & Cuaca

**SuperApps** adalah aplikasi desktop berbasis Python dengan tiga fitur utama:

1. Konversi harga kripto/fiat
2. Cek harga cryptocurrency real-time
3. Aplikasi cuaca (eksternal berbasis Flet)

Aplikasi ini menggabungkan tampilan GUI (Tkinter) & CLI, serta integrasi API CoinMarketCap dan Flet.

---

## 🚀 Fitur Utama

| Fitur                  | Deskripsi                                                     |
| ---------------------- | ------------------------------------------------------------- |
| 🔄 Price Converter     | Konversi nilai aset kripto/fiat ke mata uang lainnya          |
| 📈 Cek Harga Real-time | Menampilkan harga kripto real-time berdasarkan CoinMarketCap  |
| 🌦️ Aplikasi Cuaca     | Menjalankan aplikasi cuaca eksternal berbasis Flet            |
| 📚 Dokumentasi         | Menampilkan dokumentasi, flowchart, dan informasi tim pembuat |

---

## 📂 Struktur Folder

```
📁 root/
├── 📁 Protoype/
│   ├── list_fungsi.py        # Fungsi utama (API, konversi, cache, menu, dll)
│   ├── presentasi.py         # CLI-based aplikasi utama
│   ├── cuaca.py              # Source-code Aplikasi Cuaca
│   ├── cache.json            # Data Sementara
│   └── __pycache__/
├── 📁 asset/
│   ├── price_converter.png
│   ├── price_checker.png
│   ├── cuaca.png
│   ├── cli.png
│   └── 📁 docs/
│       ├── about.md
│       ├── doc.md
│       └── flowchart.md
├── main.py                   # GUI Tkinter SuperApps
├── cache.json                # Cache lokal untuk harga
├── requirements.txt
├── README.md
├── .gitignore
```

---

## 🔁 Alur Navigasi Aplikasi

### Versi CLI (`presentasi.py`)

```text
     Coinmarketcap

     MENU PROGRAM
     ***************
     1. Konversi Harga
     2. Cek Data Harga
     3. (DESKTOP) APLIKASI
     4. Keluar
```

### Versi GUI (`main.py`)

1. Opening
2. Menu utama:

   * 1: HOME
   * 2: Cek Harga Real-time
   * 3: Aplikasi Cuaca
   * 4: Dokumentasi
   * 5: Flowchart
   * 6: Tentang
   * 7: Keluar

---

## ⚙️ Cara Menjalankan

### A. Via Konsole (CLI)

```bash
cd protoype
python presentasi.py
```

### B. Versi GUI

```bash
python main.py
```

---

## 📦 Instalasi Dependensi

Instal semua dependensi:

```bash
pip install -r requirements.txt
```

**Isi `requirements.txt`:**

```
requests
ttkthemes
screeninfo
flet
```

---

## ⚠️ Catatan Penting

* Pastikan API key CoinMarketCap valid
* Data disimpan sementara di `cache.json` selama 24 jam
* File eksternal cuaca (`API_coinmarketcap.py`) harus berada pada path yang benar

---

## 📸 Screenshot Aplikasi

| Fitur           | Cuplikan                                      |
| --------------- | --------------------------------------------- |
| Price Converter | ![Price Converter](asset/price_converter.png) |
| Price Checker   | ![Price Checker](asset/price_checker.png)     |
| Aplikasi Cuaca  | ![Cuaca](asset/cuaca.png)                     |
| CLI Interface   | ![CLI Version](asset/cli.png)                 |

---

## 👥 Panduan untuk Pengguna Akhir

### 🔄 Price Converter

1. Masukkan **simbol aset kripto** (misalnya `BTC`)
2. Masukkan **mata uang tujuan** (misalnya `IDR`)
3. Masukkan **jumlah yang ingin dikonversi**
4. Hasil konversi ditampilkan real-time berdasarkan API

### 📈 Cek Harga Realtime

1. Masukkan jumlah data yang ingin ditampilkan (maksimal 5000)
2. Masukkan peringkat awal
3. Data harga kripto ditampilkan dalam tabel

### 🌦️ Aplikasi Cuaca

1. Pilih menu aplikasi cuaca (GUI/CLI)
2. Aplikasi eksternal akan terbuka (berbasis Flet)
3. Masukkan lokasi → tampil cuaca real-time

### 📚 Dokumentasi / Flowchart / Tentang

* File markdown akan ditampilkan sesuai pilihan menu

---


## 🔐 Keamanan API Key

**⚠️ Catatan Penting**

Untuk menjaga keamanan **API Key**, file `apikey.json` **tidak disertakan di repository ini** karena bersifat privat. 

### 🔧 Cara Menambahkan API Key

Untuk menjalankan aplikasi ini secara lokal, silakan lakukan langkah berikut:

1. **Buat file bernama `apikey.json`** di direktori utama project.
2. Isi file tersebut dengan struktur JSON berikut:

   ```json
   {
     "weather": "API_KEY_WEATHERAPI_ANDA",
     "coinmarketcap": "API_KEY_COINMARKETCAP_ANDA"
   }


---

## 🔗 Daftar Endpoint API

### 🪙 CoinMarketCap
- `https://pro-api.coinmarketcap.com/v1/tools/price-conversion`
- `https://pro-api.coinmarketcap.com/v1/cryptocurrency/map`

### 🌤️ WeatherAPI
- `http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}`


---

## 💼 Tim Pengembang

**Kelompok 1 – Tugas Akhir Web Service**

| Nama             | NIM              |
| ---------------- | ---------------- |
| Ahmad Nur Ikhsan | ********         |
| Maratua Nasution | ********         |
| Yayan Surahman   | ********         |
| Hadi             | ********         |

---

## 📄 Lisensi

*Aplikasi ini dibuat untuk tujuan akademik sebagai bagian dari* **Tugas Akhir Semester Mata Kuliah Web-Service**.

*Ttd* **AHMAD NUR IKHSAN**