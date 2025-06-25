import requests
import json
import tkinter as tk
from tkinter import ttk, scrolledtext
from ttkthemes import ThemedStyle
from screeninfo import get_monitors
from tkinter import Menu
from datetime import datetime
import subprocess
import re
from prototype.list_fungsi import load_apikey


endpoint_map = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/map"
base_url = "https://pro-api.coinmarketcap.com/v1/tools/price-conversion"

headers = load_apikey()



def dapatkan_data_harga_konversi():
    simbol = var_simbol.get()
    konversi = var_konversi.get()
    jumlah = var_jumlah.get()

    params = {
        'symbol': simbol,
        'amount': jumlah,
        'convert': konversi
    }
    response = requests.get(base_url, params=params, headers=headers)
    result = response.json()
    return result




def hitung_harga_konversi():
    # Kirim permintaan ke API CoinMarketCap untuk mengambil data harga konversi
    hasil_hitung = dapatkan_data_harga_konversi()

    if hasil_hitung['status']['error_code'] == 0:
        data = hasil_hitung['data']
        symbol = data['symbol']
        name = data['name']
        amount = data['amount']
        konversi = var_konversi.get().upper()  # Mengubah ke huruf besar
        price = data['quote'][konversi]['price']

        s0 = len('Nama Asset / Fiat')
        sp0 = ' ' * (30 - s0)

        s1 = len(f'{amount} {name}')
        sp1 = ' ' * (37 - s1)

        s2 = len(f'{price:,.5f} {konversi}')
        sp2 = ' ' * (26 - s2)

        # Tampilkan hasil tampilan di kotak teks
        tampilan_hasil = (
            f'Nama Asset / Fiat{sp0}: {name} {symbol}\n'
            f'{amount} {name}{sp1}: {price:,.5f} {konversi}\n'
        )
        hasil.delete(1.0, tk.END)  # Hapus teks sebelumnya
        hasil.insert(tk.END, tampilan_hasil)

        # jika dikonvert bukan ke IDR, maka akan otomatis dilanjutkan proses konvert sampai dapat nilai dalam IDR
        if konversi != 'IDR':
            idr_respon = requests.get(base_url, headers=headers, params={'symbol': konversi, 'convert': 'IDR', 'amount': price})
            idr_data_respon = idr_respon.json()
            idr_data = idr_data_respon['data']
            idr_price = idr_data['quote']['IDR']['price']

            # Tampilkan hasil konversi ke IDR di kotak teks
            tampilan_hasil_idr = (
                f'{price:,.5f} {konversi}{sp2}: {idr_price:,.0f} IDR\n'
            )
            hasil.insert(tk.END, tampilan_hasil_idr)
    else:
        error_message = hasil_hitung['status']['error_message']
        hasil.delete(1.0, tk.END)  # Hapus teks sebelumnya
        hasil.insert(tk.END, f'Error: {error_message}\n')




def atur_ukuran_dan_posisi_jendela():
    # Mendapatkan ukuran layar monitor
    monitor = get_monitors()[0]
    lebar_layar = monitor.width
    tinggi_layar = monitor.height

    # Menghitung posisi x, y untuk jendela agar berada di tengah layar
    x_pos = (lebar_layar - 1000) // 2
    y_pos = (tinggi_layar - 600) // 2

    # Menetapkan ukuran dan posisi jendela
    app.geometry(f"1000x600+{x_pos}+{y_pos}")




def dokumentasi():
    hasil.delete(1.0, tk.END)
    
    try:
        with open("docs/doc.md", "r", encoding="utf-8") as f:
            md_content = f.read()

        # Hilangkan simbol markdown untuk tampilan lebih bersih di Tkinter
        plain_text = md_content

        # Konversi dasar markdown ke teks biasa (opsional, bisa ditambah)
        plain_text = re.sub(r"#\s*", "", plain_text)  # Hapus heading #
        plain_text = re.sub(r"\*\*(.*?)\*\*", r"\1", plain_text)  # Bold
        plain_text = re.sub(r"`(.*?)`", r"\1", plain_text)        # Inline code
        plain_text = re.sub(r"---+", "-"*50, plain_text)          # HR
        plain_text = re.sub(r"^> ?", "", plain_text, flags=re.MULTILINE)  # Quote

        hasil.insert(tk.END, plain_text)

    except FileNotFoundError:
        hasil.insert(tk.END, "File dokumentasi.md tidak ditemukan.")



# Fungsi untuk menampilkan menu Tentang Kami
def tentang():
    hasil.delete(1.0, tk.END)

    try:
        with open("docs/about.md", "r", encoding="utf-8") as f:
            md_content = f.read()

        # Konversi sederhana dari markdown ke teks biasa
        plain_text = re.sub(r"#\s*", "", md_content)  # Hapus heading #
        plain_text = re.sub(r"\*\*(.*?)\*\*", r"\1", plain_text)  # Bold
        plain_text = re.sub(r"`(.*?)`", r"\1", plain_text)  # Inline code
        plain_text = re.sub(r"---+", "-"*50, plain_text)  # HR

        hasil.insert(tk.END, plain_text)

    except FileNotFoundError:
        hasil.insert(tk.END, "File tentang.md tidak ditemukan.")
        
        
        
def flowchart():
    hasil.delete(1.0, tk.END)

    try:
        with open("docs/flowchart.md", "r", encoding="utf-8") as f:
            md_content = f.read()

        # Konversi sederhana dari markdown ke teks biasa
        plain_text = re.sub(r"#\s*", "", md_content)  # Hapus heading #
        plain_text = re.sub(r"\*\*(.*?)\*\*", r"\1", plain_text)  # Bold
        plain_text = re.sub(r"`(.*?)`", r"\1", plain_text)  # Inline code
        plain_text = re.sub(r"---+", "-"*50, plain_text)  # HR

        hasil.insert(tk.END, plain_text)

    except FileNotFoundError:
        hasil.insert(tk.END, "File flowchart.md tidak ditemukan.")






def save_cache_to_file(cache_data):
    with open('cache.json', 'w') as file:
        json.dump(cache_data, file)

# Fungsi untuk load cache dari file
def load_cache_from_file():
    try:
        with open('cache.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}




cache = load_cache_from_file()
def data_harga(symbol):
    # Jika data sudah ada dalam cache dan belum kadaluarsa, kembalikan data tersebut
    if symbol in cache:
        cached_data = cache[symbol]
        cached_time = cached_data['timestamp']
        current_time = datetime.now().timestamp()
        # Set batasan waktu cache di sini, contohnya 300 detik (5 menit)
        cache_limit = 86400
        
        if current_time - cached_time <= cache_limit:
            return cached_data['price']
    
    parameters_harga = {
        'amount': 1,
        'symbol': symbol,
        'convert': 'IDR'
    }

    response = requests.get(base_url, headers=headers, params=parameters_harga)
    data_price = response.json()

    if data_price['status']['error_code'] == 0:
        harga = int(data_price['data']['quote']['IDR']['price'])
        
        # Simpan data ke dalam cache bersama dengan informasi timestamp
        cache[symbol] = {
            'price': harga,
            'timestamp': datetime.now().timestamp()
        }
        save_cache_to_file(cache)
        
        return harga
    else:
        print('Gagal memperoleh harga.')
        return None







frame_judul_menu_2 = None
frame_input_menu_2 = None
tombol_proses = None
last_updated_label = None
in_cek_harga = False
cached_data = []  # Inisialisasi list untuk menyimpan data di cache
tree = None
last_updated_label = None

def cek_harga():
    global frame_judul_menu_2, frame_input_menu_2, tombol_proses, last_updated_label, in_cek_harga, tree
    # Hapus widget yang ada sebelumnya di jendela aplikasi
    frame_judul.pack_forget()
    frame_input.pack_forget()
    tombol_hitung.pack_forget()
    frame_hasil.pack_forget()


    # Membuat judul baru
    frame_judul_menu_2 = tk.Frame(app, bg=warna_utama, pady=10)
    frame_judul_menu_2.pack(fill="x")

    label_judul_menu_2 = tk.Label(frame_judul_menu_2, text="Cek Data Harga", font=("Arial", 20), fg="white", bg=warna_utama)
    label_judul_menu_2.pack()

    # Membuat frame untuk input baru
    frame_input_menu_2 = tk.Frame(app, bg=warna_latar)
    frame_input_menu_2.pack(pady=10)

    # Label untuk input baru
    label_limit = tk.Label(frame_input_menu_2, text="Berapa banyak yang ingin dicetak (Maks 5000):", font=("Arial", 12), fg=warna_teks, bg=warna_latar)
    label_limit.grid(row=0, column=0, padx=10, sticky='w')

    var_limit = tk.IntVar()
    input_limit = ttk.Entry(frame_input_menu_2, textvariable=var_limit)
    input_limit.grid(row=0, column=1, padx=10, pady=5)

    label_start = tk.Label(frame_input_menu_2, text="Mulai Dari Rank Berapa:", font=("Arial", 12), fg=warna_teks, bg=warna_latar)
    label_start.grid(row=1, column=0, padx=10, sticky='w')

    var_start = tk.IntVar()
    input_start = ttk.Entry(frame_input_menu_2, textvariable=var_start)
    input_start.grid(row=1, column=1, padx=10, pady=5)

    # Fungsi untuk memproses data setelah mendapatkan input dari pengguna
    def proses_data():
        global tree, cache
        limit = var_limit.get()
        start = var_start.get()
        
        
        for widget in app.winfo_children():
            if isinstance(widget, tk.Label) and widget['text'].startswith("Last Updated"):
                widget.pack_forget()

        # Lakukan pemrosesan sesuai kebutuhan dengan nilai 'limit' dan 'start'
        # Misalnya, panggil fungsi 'processing' dengan parameter '2' seperti pada contoh yang diberikan

        # Setelah pemrosesan, panggil API atau lakukan proses lainnya
        headers = load_apikey()
        parameter2 = {
            'limit': limit,
            'start': start,
            'sort': 'cmc_rank'
        }
        respon = requests.get(endpoint_map, headers=headers, params=parameter2)
        data_map = respon.json()
        
        
        # Lakukan sesuatu dengan data_map yang diperoleh
        if tree is None:
            tree = ttk.Treeview(app)
            tree["columns"] = ("Rank", "Name", "Symbol", "Price")
            tree.heading("Rank", text="RANK")
            tree.heading("Name", text="NAMA")
            tree.heading("Symbol", text="SIMBOL")
            tree.heading("Price", text="HARGA")
            
            tree.column("#0", width=0, stretch=tk.NO)  # Kolom tersembunyi
            tree.column("Rank", anchor='center', width=100)
            tree.column("Name", anchor='center', width=200)
            tree.column("Symbol", anchor='center', width=100)
            tree.column("Price", anchor='center', width=150)
            tree.pack(fill='both', expand=True, side='top')


        if respon.status_code == 200:
            tree.delete(*tree.get_children())  # Clear previous data

            for data in data_map['data']:
                rank = int(data['rank'])
                name = data['name']
                symbol = data['symbol']

                parameters_harga = {
                    'amount': 1,
                    'symbol': symbol,
                    'convert': 'IDR'
                }
                response = requests.get(base_url, headers=headers, params=parameters_harga)
                data_price = response.json()

                if data_price['status']['error_code'] == 0:
                    harga = data_harga(symbol)
                    tree.insert("", tk.END, values=(rank, name, symbol, f"Rp {harga:,.0f}"))

            global last_updated_label
            last_updated = datetime.now().strftime("%Y-%m-%d    %H:%M:%S")
            last_updated_label = tk.Label(app, text=f"Last Updated: {last_updated}", font=("Arial", 12,'bold'), fg=warna_teks, bg=warna_latar)
            last_updated_label.pack()
            

        else:
            error_message = data_map['status']['error_message']
            hasil.delete(1.0, tk.END)  # Hapus teks sebelumnya
            hasil.insert(tk.END, f'Error: {error_message}\n')



    # Tombol untuk memproses data
    tombol_proses = tk.Button(app, text="Proses Data", command=proses_data, bg=warna_tombol, fg="white", font=("Arial", 14))
    tombol_proses.pack(pady=30)
    menu_utama.delete(0,tk.END)
    menu_utama.add_command(label="Kembali", command=kembali_ke_tampilan_default)
    

def aplikasi_cuaca():
    subprocess.Popen(["python", r'prototype/cuaca.py'])


def kembali_ke_tampilan_default():
    global frame_judul_menu_2, frame_input_menu_2, tombol_proses, last_updated_label, in_cek_harga, tree

    # Hapus semua elemen dari frame pada menu 2
    if frame_judul_menu_2:
        frame_judul_menu_2.pack_forget()
    if frame_input_menu_2:
        frame_input_menu_2.pack_forget()
    if tombol_proses:
        tombol_proses.pack_forget()
    if last_updated_label:
        last_updated_label.pack_forget()
        
        
    # Tampilkan kembali elemen-elemen pada tampilan default
    frame_judul.pack(fill="x")
    frame_input.pack(pady=10)
    tombol_hitung.pack(pady=10)
    frame_hasil.pack(padx=10, pady=10, fill='both', expand=True)

    if last_updated_label:
        last_updated_label.pack_forget()

    # Hapus Treeview jika ada
    if tree:
        tree.destroy()
        tree = None

    # Hapus opsi "Kembali" dari menu utama dan tambahkan kembali opsi-opsi lainnya
    menu_utama.delete("Kembali")
    # Tambahkan kembali opsi-opsi lainnya jika tidak di mode cek_harga
    if not in_cek_harga:
        menu_utama.add_command(label="HOME", command='')
        menu_utama.add_command(label="(Realtime) CEK HARGA", command=cek_harga)
        menu_utama.add_command(label="(Flet) APLIKASI CUACA", command=aplikasi_cuaca)
        menu_utama.add_command(label="---------------------", command='')
        menu_utama.add_command(label="Dokumentasi", command=dokumentasi)
        menu_utama.add_command(label="Flowchart APLIKASI", command=flowchart)
        menu_utama.add_command(label="Tentang Kami", command=tentang)
        menu_utama.add_command(label="---------------------", command='')
        menu_utama.add_command(label="Keluar", command=keluar_aplikasi)



def keluar_aplikasi():
    app.destroy()


# Membuat jendela aplikasi utama
app = tk.Tk()
app.title("P R E S E N T A S I      K E L O M P O K     1")

app.geometry("1200x800")  # Menetapkan ukuran jendela secara tetap
app.resizable(False, False)

menu_bar = Menu(app)
app.config(menu=menu_bar)

# Membuat menu utama
menu_utama = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="M E N U", menu=menu_utama)

# Sub-menu untuk Bantuan dan Dokumentasi
menu_utama.add_command(label="HOME", command='')
menu_utama.add_command(label="(Realtime) CEK HARGA", command=cek_harga)
menu_utama.add_command(label="(Flet) APLIKASI CUACA", command=aplikasi_cuaca)
menu_utama.add_command(label="---------------------", command='')
menu_utama.add_command(label="Dokumentasi", command=dokumentasi)
menu_utama.add_command(label="Flowchart APLIKASI", command=flowchart)
menu_utama.add_command(label="Tentang Kami", command=tentang)
menu_utama.add_command(label="---------------------", command='')
menu_utama.add_command(label="Keluar", command=keluar_aplikasi)




style = ThemedStyle(app)
style.set_theme("plastik")

# Mengatur palet warna kustom
warna_utama = "#4CAF50"  # Hijau
warna_teks = "#333333"
warna_latar = "#F5F5F5"
warna_tombol = "#009688"

app.configure(bg=warna_latar)
atur_ukuran_dan_posisi_jendela()

# Membuat frame atas untuk judul
frame_judul = tk.Frame(app, bg=warna_utama, pady=10)
frame_judul.pack(fill="x")

# Label judul
label_judul = tk.Label(frame_judul, text="Aplikasi Price Converter", font=("Arial", 20), fg="white", bg=warna_utama)
label_judul.pack()

# Membuat frame untuk elemen input
frame_input = tk.Frame(app, bg=warna_latar)
frame_input.pack(pady=10)

# Label simbol kripto
label_simbol = tk.Label(frame_input, text="Simbol Asset / FIAT:", font=("Arial", 12), fg=warna_teks, bg=warna_latar)
label_simbol.grid(row=0, column=0, padx=10, pady=5, sticky='w')

var_simbol = tk.StringVar()
input_simbol = ttk.Entry(frame_input, textvariable=var_simbol)
input_simbol.grid(row=0, column=1, padx=10, pady=5)

# Label mata uang konversi
label_konversi = tk.Label(frame_input, text="Mata Uang Konversi:", font=("Arial", 12), fg=warna_teks, bg=warna_latar)
label_konversi.grid(row=1, column=0, padx=10, pady=5, sticky='w')

var_konversi = tk.StringVar()
input_konversi = ttk.Entry(frame_input, textvariable=var_konversi)
input_konversi.grid(row=1, column=1, padx=10, pady=5)

# Label jumlah yang akan dikonversi
label_jumlah = tk.Label(frame_input, text="Jumlah yang akan dikonversi:", font=("Arial", 12), fg=warna_teks, bg=warna_latar)
label_jumlah.grid(row=2, column=0, padx=10, pady=5, sticky='w')

var_jumlah = tk.DoubleVar()
input_jumlah = ttk.Entry(frame_input, textvariable=var_jumlah)
input_jumlah.grid(row=2, column=1, padx=10, pady=5)

# Tombol Hitung
tombol_hitung = tk.Button(app, text="Hitung Harga", command=hitung_harga_konversi, bg=warna_tombol, fg="white", font=("Arial", 14))
tombol_hitung.pack(pady=10)

# Frame untuk menampilkan hasil konversi
frame_hasil = tk.Frame(app, bg=warna_latar)
frame_hasil.pack(padx=10, pady=10, fill='both', expand=True)

# Membuat widget ScrolledText untuk menampilkan hasil konversi
frame_hasil_scroll = tk.Frame(frame_hasil, bg=warna_latar, borderwidth=1, relief='solid')
frame_hasil_scroll.pack(fill='both', expand=True, padx=10, pady=10)

hasil = scrolledtext.ScrolledText(frame_hasil_scroll, wrap=tk.WORD, width=40, height=10, padx=10, pady=10)
hasil.config(font=("Arial", 12), bg=warna_latar, relief="flat")
hasil.pack(fill='both', expand=True)

app.mainloop()