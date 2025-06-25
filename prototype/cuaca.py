from flet import *
import requests, json


##PANGGIL APIKEY CUACA
def cuaca():
    with open("apikey.json", "r") as f:
        data = json.load(f)
    return data.get("WEATHER_API_KEY")
    

header = cuaca()
def main(page: Page):
    page.horizontal_alignment = 'center'
    page.window_width = 445
    page.window_height = 585
    page.window_min_width = 445
    page.window_min_height = 585
    # Background warna = white

    def cek_cuaca(city): # fungsi untuk mengambil nama kota yang akan dikirim sebagai request ke API
        link = f'http://api.weatherapi.com/v1/current.json?key={header}&q={city}'
        try:
            r = requests.get(link).json()
            return r
        except: return "Network Error"
    
    def error(error): # fungsi jika error
        page.snack_bar = SnackBar(Text(error, text_align='center', size=20), bgcolor=colors.ERROR)
        page.snack_bar.open = True
        page.update()
    
    def submit(e):
        city.focus()
        if city.value != '':
            report = cek_cuaca(city.value) # dapatkan data laporan cuaca dari API

            if 'No matching location found' in str(report):
                error("Tidak ada Kota yang Ditemukann!") # tampilkan pesan kesalahan
                return
            
            if report == 'network error':
                error('Network error') # tampilkan pesan kesalahan
                return
            
            # cara cek bagaimana struktur endpoin api nya akan dkirim sebagai request
            # dan ternyata, nama kota digunakan sebagai parameter in link, contoh :  https://api.weatherapi.com/v1/current.json?key=apikey&q=london
            # dengan begitu, maka KOTA bisa kita panggil dengan INPUT user denga memformatnya kedalam link/endpoint

            arah_angin = { # Definisi arah Angin
                            'N': 'Utara',
                            'NW': 'Barat Laut',
                            'NNW': 'Utara Barat Laut',
                            'NE': 'Timur Laut',
                            'NNE': 'Utara Timur Laut',
                            'S': 'Selatan',
                            'SW': 'Barat Daya',
                            'SWW': 'Selatan Barat Daya',
                            'SE': 'Tenggara',
                            'SSE': 'Selatan Tenggara',
                            'W': 'Barat',
                            'WNW': 'Barat Laut',
                            'WSW': 'Barat Daya',
                            'E': 'Timur',
                            'ENE': 'Timur Laut',
                            'ESE': 'Tenggara'
                                }

            def ubah_suhu(e):
                if e.control.data == 'C':
                    weather.content.controls[1].controls[1].controls[3].controls[1].value = f"{report['current']['temp_f']} °F"
                    e.control.data = 'F'
                else:
                    weather.content.controls[1].controls[1].controls[3].controls[1].value = f"{report['current']['temp_c']} °C"
                    e.control.data = 'C'
                page.update()

            # LOGIKA UTAMA PROGRAM
            weather.content = Column(
            [
                Row(), #f untuk spasi
                Row(
                [
                    Column(width=4), # untuk spasi
                    Column(
                        [
                            Text(
                                spans=[
                                    TextSpan('Kota: ', style=TextStyle(weight='bold', size=18)), 
                                    TextSpan(report['location']['name'], style=TextStyle(size=17)) # untuk dapatkan data kota
                                ]
                            ),

                            Text(
                                spans=[
                                    TextSpan('Region: ', style=TextStyle(weight='bold', size=18)), 
                                    TextSpan(report['location']['region'], style=TextStyle(size=17)) 
                                ]
                            ),

                            Text(
                                spans=[
                                    TextSpan('Negara: ', style=TextStyle(weight='bold', size=18)), 
                                    TextSpan(report['location']['country'], style=TextStyle(size=17)) 
                                ]
                            ),

                            Row([
                                # tombol ubah suhu CELCIUS dan FAHRENHEIT
                                IconButton( icons.SWAP_HORIZ, on_click=ubah_suhu, data='C'), 
                                Text(f"{report['current']['temp_c']} °C", size= 40, weight='bold', width=160),

                                # icon DAY / NIGH digunakan berdasarkan nilai, in-day dan in-night pada API, untuk referensi icon ada pada link: https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQJG1UZgY9gWlfMuTqTC25NpkU2V-RGfhEpXw&usqp=CAU https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSRNSUclqheK40bl2XJZ1UmpM0FX3CTKIsJ5eFlQSwOqGtXLez83CsdPTvNGc-BQTK9DTo&usqp=CAU
                                # Image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS5n0cu3OEjG6s-QU7Or7iDH4EVojrY7JhJeg&usqp=CAU' if report['current']['is_day'] == 1 else 'https://images.vexels.com/media/users/3/153630/isolated/lists/f157393ba1bbd3471c532c9516b894f2-crescent-moon-flat-icon.png', width=60, height=60, fit=ImageFit.CONTAIN)
                                Image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRj88iBwJ8PbzRZOKOn73Xzg1I31UVRqspkHA&usqp=CAU' if report['current']['is_day'] == 1 else 'https://images.vexels.com/media/users/3/153630/isolated/lists/f157393ba1bbd3471c532c9516b894f2-crescent-moon-flat-icon.png', width=60, height=60, fit=ImageFit.CONTAIN)
                            ]),

                            Text(
                                spans=[
                                    TextSpan('Kondisi: ', style=TextStyle(weight='bold', size=18)), 
                                    TextSpan(report['current']['condition']['text'], style=TextStyle(size=17)) 
                                ]
                            ),

                            Text(
                                spans=[
                                    TextSpan('Waktu Setempat: ', style=TextStyle(weight='bold', size=18)), 
                                    TextSpan(report['location']['localtime'].split()[1], style=TextStyle(size=17)) 
                                ]
                            ),

                            Text(
                                spans=[
                                    TextSpan('Kecepatan Angin: ', style=TextStyle(weight='bold', size=18)), 
                                    TextSpan(f"{report['current']['wind_kph']} kph", style=TextStyle(size=17)),  
                                ]
                            ),
                            Text(
                                spans=[
                                    TextSpan('Hembusan: ', style=TextStyle(weight='bold', size=18)), 
                                    TextSpan(f"{report['current']['gust_kph']} kph", style=TextStyle(size=17)) 
                                ]
                            ),

                            Text(
                                spans=[
                                    TextSpan('Arah Angin: ', style=TextStyle(weight='bold', size=18)), 
                                    TextSpan(arah_angin.get(report['current']['wind_dir']), style=TextStyle(size=17)) 
                                ]
                            ),

                            Text(
                                spans=[
                                    TextSpan('Curah Hujan: ', style=TextStyle(weight='bold', size=18)), 
                                    TextSpan(f"{report['current']['precip_mm']} mm", style=TextStyle(size=17)) 
                                ]
                            ),

                        ]
                    )
                ]
                )
            ],
            width=400,
            height=400
            )
            page.update() # update setalah ada perulanagan input / perubahan data

    #a ppbar
    page.appbar = AppBar(
        title = Text('Aplikasi Cuaca', weight='bold', size=30),
        bgcolor = colors.PRIMARY_CONTAINER,
        center_title = True
    )

    # textfield untuk menyimpan nama kota berdasarkan input user
    city = TextField(
        hint_text="Cari Kota",
        hint_style=TextStyle(color='white'),
        width=235,
        text_size=20,
        height=60,
        border_color='white',
        cursor_color='white',
        focused_border_color='white',
        on_submit=submit
    )

    # tombol SUBMIT / KIRIM permintaan ke API
    button = OutlinedButton(
        content=Text('Cek Cuaca', size=18, color='white'),
        on_click=submit,
        height=60,
        style=ButtonStyle(shape=RoundedRectangleBorder(radius=6))
    )
    # tombol SUBMIT dan tombol cari KOTA akan ditampilkan dalam row yang sama / span row
    weather = Card(width=410, height=400) # card tampilan hasil
    page.add(Row([city, button], alignment=MainAxisAlignment.SPACE_BETWEEN, width=400), weather)
app(main)