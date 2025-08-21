import http.client, urllib.parse

api_key = f"2a244967e7d5a012e19f7311d172c226"
url_link = f"api.mediastack.com"

connection = http.client.HTTPConnection(url_link)

params = urllib.parse.urlencode({
    'access_key': api_key,
    'categories': 'technology,-science',
    'countries' : 'us,-de',
    'sort': 'published_desc',
    # 'limit': 10,
    })

connection.request('GET', '/v1/news?{}'.format(params))

respon = connection.getresponse()
data = respon.read()

print(data.decode('utf-8'))



