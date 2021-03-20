import requests
from bs4 import BeautifulSoup

url = 'https://www.books.com.tw/web/sys_saletopb/books/'
data = requests.get(url)

soup = BeautifulSoup(data.text,'html.parser')

divs  = soup.find_all('div', class_='type02_bd-a')

for each_div in divs:
    
    h4 = each_div.find('h4')
    a = h4.find('a')
    bookname = a.text
    print(bookname)
    

    

