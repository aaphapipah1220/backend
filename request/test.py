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


# ======================== interface
screen = tkinter.Tk()
screen.geometry("500x500")

def check():
    # img.configure(image=data['current']['weather_icons'])
    show.configure(text=f"""
                   Kota : {data['request']['query']} 
                   Suhu : {data['current']['temperature']}
                   Keterangan : {data['current']['weather_descriptions']}""")

button = tkinter.Button(screen, text="weather check", command=check)
show = tkinter.Label(screen)
img = tkinter.Label(screen)

button.pack()
show.pack()

screen.mainloop()