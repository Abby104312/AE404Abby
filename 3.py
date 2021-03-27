import requests
from bs4 import BeautifulSoup

url = 'https://www.books.com.tw/web/sys_saletopb/books/'
data = requests.get(url)

soup = BeautifulSoup(data.text,'html.parser')

divs = soup.find_all('img', class_='cover')

for each_div in divs[:3]:
    img = each_div['src']
    t = each_div['alt']
    imgRespond = requests.get(img)
    with open(t+'.jpg', 'wb') as f:
        f.write(imgRespond.content)
        
    