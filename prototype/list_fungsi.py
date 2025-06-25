import time, os, sys, requests, json
from datetime import datetime


judul = r'''
            ██╗░░██╗  ███████╗  ██╗░░░░░  ░█████╗░  ███╗░░░███╗  ██████╗░  ░█████╗░  ██╗░░██╗   ░░███╗░░
            ██║░██╔╝  ██╔════╝  ██║░░░░░  ██╔══██╗  ████╗░████║  ██╔══██╗  ██╔══██╗  ██║░██╔╝   ░████║░░
            █████═╝░  █████╗░░  ██║░░░░░  ██║░░██║  ██╔████╔██║  ██████╔╝  ██║░░██║  █████═╝░   ██╔██║░░
            ██╔═██╗░  ██╔══╝░░  ██║░░░░░  ██║░░██║  ██║╚██╔╝██║  ██╔═══╝░  ██║░░██║  ██╔═██╗░   ╚═╝██║░░
            ██║░╚██╗  ███████╗  ███████╗  ╚█████╔╝  ██║░╚═╝░██║  ██║░░░░░  ╚█████╔╝  ██║░╚██╗   ███████╗
            ╚═╝░░╚═╝  ╚══════╝  ╚══════╝  ░╚════╝░  ╚═╝░░░░░╚═╝  ╚═╝░░░░░  ░╚════╝░  ╚═╝░░╚═╝   ╚══════╝
                           ___      _                            _        _                  
                          / __\___ (_)_ __  _ __ ___   __ _ _ __| | _____| |_ ___ __ _ _ __  
                         / /  / _ \| | '_ \| '_ ` _ \ / _` | '__| |/ / _ \ __/ __/ _` | '_ \ 
                        / /__| (_) | | | | | | | | | | (_| | |  |   <  __/ || (_| (_| | |_) |
                        \____/\___/|_|_| |_|_| |_| |_|\__,_|_|  |_|\_\___|\__\___\__,_| .__/ 
                                                                                      |_|    
                        - - - -- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
'''
# Setting headers
endpoint_konversi = 'https://pro-api.coinmarketcap.com/v1/tools/price-conversion'
endpoint_map = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'

## PANGGIL APIKEY CMC
def load_apikey():
    """Membaca API key dari file apikey.json dan mengembalikan headers."""
    with open('apikey.json', 'r') as f:
        key_data = json.load(f)
    return {
        'X-CMC_PRO_API_KEY': key_data['X-CMC_PRO_API_KEY']
    }
headers = load_apikey()
    
    
    
    
def menu ():
    print('\n\n')
    print('\t𝗠 𝗘 𝗡 𝗨  𝗣 𝗥 𝗢 𝗚 𝗥 𝗔 𝗠')
    jarak0 = (len('𝗠 𝗘 𝗡 𝗨  𝗣 𝗥 𝗢 𝗚 𝗥 𝗔 𝗠') / 2)
    print('\t'+'~ '*int(jarak0+1)+'\n\n')
    print('1. Konversi Harga')
    print('2. Cek Data Harga')
    print('3. (DESKTOP) aplikasi'.upper())
    print('- - - - - - - - - - - - - - - - - -')
    print('4. Keluar\n\n\n\n')



# fungsi bersihkan layar
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(judul)
    
# fungsi loading
def loading(n):
    for i in range(n, 0, -1):
        os.system('cls' if os.name == 'nt' else 'clear')
        sys.stdout.write(f'\n\n\n\n\n\n\rＬｏａｄｉｎｇ . . . ({i}) ')
        sys.stdout.flush()
        time.sleep(1)

# fungsi processing
def processing(n):
    for i in range(n, 0, -1):
        print(f'\rＰｒｏｃｅｓｓｉｎｇ . . . ({i}) ', end='', flush=True)
        time.sleep(1)
    print('\r' + ' ' * 30, end='', flush=True)

# Fungsi untuk menyimpan cache ke dalam file
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

# Fungsi untuk mendapatkan data harga dari CACHE (jika ada) dan dari API jika tidak ada
cache = load_cache_from_file()
def data_harga(symbol):
    # Jika data sudah ada dalam cache dan belum kadaluarsa, kembalikan data tersebut
    if symbol in cache:
        cached_data = cache[symbol]
        cached_time = cached_data['timestamp']
        current_time = datetime.now().timestamp()
        # Set batasan waktu cache di sini, contohnya 86400 detik (24 Jam)
        cache_limit = 86400
        
        if current_time - cached_time <= cache_limit:
            return cached_data['price']
    
    parameters_harga = {
        'amount': 1,
        'symbol': symbol,
        'convert': 'IDR'
    }

    response = requests.get(endpoint_konversi, headers=headers, params=parameters_harga)
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


# FUNGSI OPENING
def opening():
    os.system('cls' if os.name == 'nt' else 'clear')    
    print('''
\n\n
        █▄▀ █▀▀ █░░ █▀█ █▀▄▀█ █▀█ █▀█ █▄▀   ▄█   ▀
        █░█ ██▄ █▄▄ █▄█ █░▀░█ █▀▀ █▄█ █░█   ░█   ▄\n\n    
        Ａｈｍａｄ Ｎｕｒ Ｉｋｈｓａｎ     ⁽ 𝟭 𝟭 𝟮 𝟮 𝟬 𝟳 𝟵 𝟲 ⁾
        Ｍａｒａｔｕａ Ｎａｓｕｔｉｏｎ    ⁽ 𝟭 𝟭 𝟮 𝟮 𝟬 𝟴 𝟮 𝟴 ⁾
        Ｙａｙａｎ Ｓｕｒａｈｍａｎ        ⁽ 𝟭 𝟭 𝟮 𝟮 𝟬 𝟵 𝟴 𝟱 ⁾
        Ｈａｄｉ                           ⁽ 𝟭 𝟭 𝟮 𝟮 𝟬 𝟵 𝟮 𝟳 ⁾
                ''')

# FUNGSI ENDING
def ending():
    os.system('cls' if os.name == 'nt' else 'clear')    
    print('''
                \n\n\n\n
                                Ｐｒｅｓｅｎｔｅｄ Ｂｙ： Ｋｅｌｏｍｐｏｋ １\n
        ▀▀█▀▀ 　 ▒█▀▀▀ 　 ▒█▀▀█ 　 ▀█▀ 　 ▒█▀▄▀█ 　 ░█▀▀█ 　 ▒█░▄▀ 　 ░█▀▀█ 　 ▒█▀▀▀█ 　 ▀█▀ 　 ▒█░▒█ 　 █ █ 
        ░▒█░░ 　 ▒█▀▀▀ 　 ▒█▄▄▀ 　 ▒█░ 　 ▒█▒█▒█ 　 ▒█▄▄█ 　 ▒█▀▄░ 　 ▒█▄▄█ 　 ░▀▀▀▄▄ 　 ▒█░ 　 ▒█▀▀█ 　 ▀ ▀ 
        ░▒█░░ 　 ▒█▄▄▄ 　 ▒█░▒█ 　 ▄█▄ 　 ▒█░░▒█ 　 ▒█░▒█ 　 ▒█░▒█ 　 ▒█░▒█ 　 ▒█▄▄▄█ 　 ▄█▄ 　 ▒█░▒█ 　 ▄ ▄
                \n\n\n
                                ''')
# FUNGSI CLOSING PROGRAM 1
def closing(nomor):
    print(f'''
        \n\n\n\n
                                        Ｐｒｏｇｒａｍ  {nomor} ： ＳＥＬＥＳＡＩ！
        \n\n\n
        ''')                


def program1():
    # Form input
    while True:
        clear_screen()    
        print('\n\n\t\t\t\tＰｒｏｇｒａｍ １ （ＰＲＩＣＥ ＣＯＮＶＥＲＴＥＲ）\n\n\n')
        print('\t    F O R M  I N P U T')
        panjang = len('F O R M  I N P U T') / 2
        print('\t    ' + ('~ ' * int(panjang)) + '\n')
        
        #  Input simbol currency
        panjang_karakter = len(f'Simbol Mata Uang')
        jarak = ' ' * (30 - panjang_karakter)
        simbol_asal = input(f'Simbol Mata Uang{jarak}: ').upper()

        #  input simbol tujuan konversi
        panjang_karakter2 = len(f'Konversi Ke')
        jarak2 = ' ' * (30 - panjang_karakter2)
        simbol_tujuan = input(f'Konversi Ke{jarak2}: ').upper()

        #  input jumlah yang dikonversi
        panjang_karakter3 = len(f'Jumlah {simbol_asal} yang dikonversi')
        jarak3 = ' ' * (30 - panjang_karakter3)
        jumlah_konversi = float(input(f'Jumlah {simbol_asal} yang dikonversi{jarak3}: '))
        print('\n')
        
        # Garis Batas
        print(' - ' * 20)
        print('\n')

        # Setting parameter
        parameter = {
            'symbol': simbol_asal,
            'convert': simbol_tujuan,
            'amount': jumlah_konversi
        }

        # Kirim request ke API
        respon = requests.get(endpoint_konversi, headers=headers, params=parameter)
        data_respon = respon.json()


        # Validasi DATA dengan pengecekan status, apakah error atau tidak
        # Jika Request API berhasil, eksekusi kode dibawah
        # Jika Request Gagal, Go to ELSE.
        
        if data_respon['status']['error_code'] == 0:
            data = data_respon['data']
            symbol = data['symbol']
            name = data['name']
            amount = data['amount']
            price = data['quote'][simbol_tujuan]['price']
            
            processing(2)
            
            # Tampilkan HASIL KONVERSI
            panjang_karakter4 = len(f'Nama Asset / Fiat')
            jarak4 = ' ' * (29 - panjang_karakter4)
            print('\n\t H A S I L  K O N V E R S I')
            pjg = int(len('H A S I L  K O N V E R S I')) / 2
            print('\t'+' ~' * int(pjg) +'\n')
            
            print(f'Nama Asset / Fiat {jarak4}: {name} ({symbol})')
            panjang_karakter5 = len(f'{amount} {name}')
            jarak5 = ' ' * (29 - panjang_karakter5)
            
            
            # Validasi Input
            # 1. Jika dikonversi ke USDT , maka tampilkan harga dalam 2 decimal
            # 2. Jika dikonversi ke IDR , maka tampilkan harga dalam bilangan bulat
            # 3. Jika dikonversi bukan ke IDR / USDT , maka tampilkan harga dalam 5 decimal
            
            if simbol_tujuan == 'USDT':
                print(f'{amount} {name}{jarak5} : {price:,.2f} {simbol_tujuan}')
            elif simbol_tujuan == 'IDR':
                price = int(price)
                print(f'{amount} {name}{jarak5} : {price:,} {simbol_tujuan}\n')
            else:
                print(f'{amount} {name}{jarak5} : {price:,.5f} {simbol_tujuan}')


            # Validasi Input selain konversi ke IDR
            # Jika bukan dikonversi bukan ke IDR, lanjutkan proses konversi sampai dapat nilai IDR
            
            if simbol_tujuan != 'IDR':
                idr_respon = requests.get(endpoint_konversi, headers=headers,params={'symbol': simbol_tujuan, 'convert': 'IDR', 'amount': price})
                idr_data_respon = idr_respon.json()
                idr_data = idr_data_respon['data']
                idr_price = idr_data['quote']['IDR']['price']

                if simbol_tujuan == 'USDT':
                    panjang_karakter6 = len(f'{price:,.2f} {simbol_tujuan}')
                    jarak6 = ' ' * (29 - panjang_karakter6)
                    print(f'{price:,.2f} {simbol_tujuan}{jarak6} : {idr_price:,.0f} IDR\n')
                else:
                    panjang_karakter7 = len(f'{price:,.5f} {simbol_tujuan}')
                    jarak7 = ' ' * (29 - panjang_karakter7)
                    print(f'{price:,.5f} {simbol_tujuan}{jarak7} : {idr_price:,.0f} IDR\n')

            #  Garis Batas
            print('\n')
            print(' - ' * 20)
            print('\n')
            
        # Jika Respon API Gagal 
        else:
            processing(2)
            print(f'\nGagal, kode kesalahan {respon.status_code}')
            print(f'Reason: {respon.reason}')
            print('\nPeriksa kembali INPUT, API KEY, dan URL\nLalu Coba Lagii... ')
            print('\n')
            print(' - ' * 20)
            print('\n')
            
            # Opsi Ulangi program atau keluar
            # 1. Jika y/Y , Ulangi program dari form input
            # 2. Selaiin itu, program berhenti dan print penutup
        
        ulangi = input('Konversi lagi? (y/n) ').lower()
        if ulangi.lower() != 'y':
            clear_screen()
            closing(1)
            input('Kembali Ke Menu Awal ... ')
            break













def program2():
    while True:
        clear_screen()
        print('\n\n\t\t\t\tＰｒｏｇｒａｍ ２ （ＰＲＩＣＥ ＲＥＡＬＴＩＭＥ）\n\n\n')
        print('1. Cetak Data Harga')
        print('2. Cetak berdasarkan Simbol')
        pilihan = int(input('\nPilih : '))
        
        if pilihan == 1:
            while True:
                print('\n'+' - ' * 20 + '\n')
                limit = int(input('Berapa banyak yang ingin dicetak (Maks 5000? : '))
                start = int(input('Mulai Dari Rank Berapa?  : '))
                print('\n')
                processing(2)
                print('\n')
                parameter2 = {
                    'limit': limit,
                    'start':start,
                    'sort': 'cmc_rank'}
                
                respon = requests.get(endpoint_map, headers=headers, params=parameter2)
                data_map = respon.json()
                
                if data_map['status']['error_code'] == 0:
                    print("\t\tD A T A  H A R G A")
                    print('\t\t'+'- '*10)
                    print(f'\n{"RANK":<10}{"NAMA":<25}{"SIMBOL":<10}{"HARGA"}')
                    length = len(f'{"RANK":<10}{"NAMA":<25}{"SIMBOL":<10}{"HARGA"}')
                    print('-'*int(length))
                    
                    for data in data_map['data']:
                        rank = int(data['rank'])
                        name = data['name']
                        symbol = data['symbol']
                        
                        
                        harga = data_harga(symbol)
                        if harga is not None:
                            last_updated = datetime.fromtimestamp(cache[symbol]['timestamp'])
                            last_updated_str = last_updated.strftime("%Y-%m-%d  %H:%M:%S")
                            print(f'{str(rank):<10}{name:<25}{(symbol):<10}Rp {harga:,.0f}'.replace(",", "."))
                    print(f"\n\nLast Updated : {last_updated_str}")
                    print(' - ' * 20)
                    
                    # AKTIFKAN KODE INI UNTUK CLEAR CACHE DAN HARGA TERBARU
                    update = input('Update Data? (y/n) ').lower()
                    if update == 'y':
                        cache.clear()
                        print('\n')
                        processing(2)
                        print('\n')
                        
                        print("\t\tD A T A  H A R G A")
                        print('\t\t'+'- '*10)
                        print(f'\n{"RANK":<10}{"NAMA":<25}{"SIMBOL":<10}{"HARGA"}')
                        length = len(f'{"RANK":<10}{"NAMA":<25}{"SIMBOL":<10}{"HARGA"}')
                        print('-'*int(length))
                        
                        
                        for data in data_map['data']:
                            rank = int(data['rank'])
                            name = data['name']
                            symbol = data['symbol']
                            
                            
                            harga = data_harga(symbol)
                            if harga is not None:
                                last_updated = datetime.fromtimestamp(cache[symbol]['timestamp'])
                                last_updated_str = last_updated.strftime("%Y-%m-%d  %H:%M:%S")
                                print(f'{str(rank):<10}{name:<25}{(symbol):<10}Rp {harga:,.0f}'.replace(",", "."))
                        print(f"\nLast Updated : {last_updated_str}")
                        print(' - ' * 20)
                        break
                    
                    else:
                        break
                else:
                    print("\nTerjadi kesalahan saat mengambil data.")
            
            
        
        elif pilihan == 2:
            while True:
                print(' - ' * 20)
                symbol = input(F"\nSimbol (Pemisah koma) jika lebih dari 1 : ").upper()
                symbol_list = symbol.split(',')
                parameter3 = {
                    'symbol':symbol,
                    'sort': 'cmc_rank'}
                
                print('\n')
                processing(2)
                print('\n')
                
                respon = requests.get(endpoint_map, headers=headers, params=parameter3)
                data_map = respon.json()
                
                if data_map['status']['error_code'] == 0:
                    print("\t\tD A T A  H A R G A")
                    print('\t\t'+'- '*10)
                    print(f'{"RANK":<10}{"NAMA":<25}{"SIMBOL":<10}{"HARGA"}')
                    length = len(f'{"RANK":<10}{"NAMA":<25}{"SIMBOL":<10}{"HARGA"}')
                    print('-'*int(length))
                    sorted_data = sorted(data_map['data'], key=lambda x: x['rank'] if x['rank'] is not None else float('inf'))
                    
                    for data in sorted_data:
                        rank = data['rank']
                        name = data['name']
                        symbol = data['symbol']
                        
                        if rank is not None:
                            harga = data_harga(symbol)
                            if harga is not None:
                                last_updated = datetime.fromtimestamp(cache[symbol]['timestamp'])
                                last_updated_str = last_updated.strftime("%Y-%m-%d  %H:%M:%S")
                                print(f'{str(rank):<10}{name:<25}{(symbol):<10}Rp {harga:,.0f}'.replace(",", "."))
                    print(f"\n\nLast Updated : {last_updated_str}")
                    print(' - ' * 20)
                    
                    # AKTIFKAN KODE INI UNTUK CLEAR CACHE DAN HARGA TERBARU
                    update = input('Update Data? (y/n) ').lower()
                    if update == 'y':
                        cache.clear()
                        print('\n')
                        processing(2)
                        print('\n')
                        
                        print("\t\tD A T A  H A R G A")
                        print('\t\t'+'- '*10)
                        print(f'\n{"RANK":<10}{"NAMA":<25}{"SIMBOL":<10}{"HARGA"}')
                        length = len(f'{"RANK":<10}{"NAMA":<25}{"SIMBOL":<10}{"HARGA"}')
                        print('-'*int(length))
                        
                        for data in sorted_data:
                            rank = data['rank']
                            name = data['name']
                            symbol = data['symbol']
                            
                            if rank is not None:
                                harga = data_harga(symbol)
                                if harga is not None:
                                    last_updated = datetime.fromtimestamp(cache[symbol]['timestamp'])
                                    last_updated_str = last_updated.strftime("%Y-%m-%d  %H:%M:%S")
                                    print(f'{str(rank):<10}{name:<25}{(symbol):<10}Rp {harga:,.0f}'.replace(",", "."))
                        print(f"\n\nLast Updated : {last_updated_str}")
                        print(' - ' * 20)
                        break
                    
                    else:
                        break
                else:
                    print("\nTerjadi kesalahan saat mengambil data.")



        ulangi = input('Ulang Program 2? (y/n) ').lower()
        if ulangi.lower() != 'y':
            clear_screen()
            closing(2)                
            input('Kembali Ke Menu Awal ... ')
            break