import requests

url = 'https://m.media-amazon.com/images/I/71ic53hVKtL._SL1000_.jpg'

res = requests.get(url)
name = 'photos/photo1.jpg'
with open(name, 'wb') as file:
    file.write(res.content)
