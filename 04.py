import requests
import re
from bs4 import BeautifulSoup

url = 'https://www.books.com.tw/web/sys_saletopb/books/'
data = requests.get(url)
soup = BeautifulSoup(data.text, 'html.parser')

a_tag = soup.find_all('a')
for tag in a_tag:
    url = tag['href']
    if re.fullmatch('https://www.books.com.tw/web/sys_saletopb/books/(\d{2})/[?]loc=P_0002_(\d{3})', url):
        print(url)
