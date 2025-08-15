import requests

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"data ditemukan {data}")
else:
    print(f"Gagal memuat data {response.status_code}")