import requests
url = 'https://chat.google.com/room/AAAADcx6838'

data = requests.get(url)
print(data)