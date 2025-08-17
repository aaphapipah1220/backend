import requests
import json
import tkinter

api_key = "9459b7154238a873aaddf1cef6d06fdc"
url = f"https://api.weatherstack.com/current?access_key={api_key}"
querystring = {
    "access_key": api_key,
    "query": "Jakarta"
}

response = requests.get(url, querystring)

if response.status_code == 200:
    data = response.json()
    print(json.dumps(data, indent=4))
else:
    print(f"Gagal memuat data {response.status_code}")


# ====================================== interface =========================================
screen = tkinter.Tk()
screen.geometry("500x500")
screen.title("Information Time")

# ====================================== function ==========================================

def check_weather():
    # img.configure(image=data['current']['weather_icons'])
    show_weather.configure(text=f"""
                   Kota : {data['request']['query']} 
                   Suhu : {data['current']['temperature']}
                   Keterangan : {data['current']['weather_descriptions']}""")
    
def check_time():
    show_time.configure(text=f"""
                        Kota : {data['request']['query']} 
                        Zona Waktu : {data['location']['timezone_id']}
                        Jam : {data['location']['localtime']}

                        Informasi:
                        - sunrise : {data['current']['astro']['sunrise']}
                        - sunset : {data['current']['astro']['sunset']}
                        - moonrise : {data['current']['astro']['moonrise']}
                        - moonset : {data['current']['astro']['moonset']}""")

# ======================================= widgets ==========================================

# img = tkinter.Label(screen)

button_weather = tkinter.Button(screen, text="Weather", command=check_weather, background="blue")
show_weather = tkinter.Label(screen)

button_time = tkinter.Button(screen, text="Time", command=check_time, background="orange")
show_time = tkinter.Label(screen)

button_weather.pack()
show_weather.pack()
button_time.pack()
show_time.pack()

screen.mainloop()