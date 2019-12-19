import requests
from bs4 import BeautifulSoup

html = requests.get('https://finance.naver.com/item/sise.nhn?code=005930')
# print(html.text)

soup = BeautifulSoup(html.text, 'html.parser')


stock = soup.select('table.type2')

stock_now = soup.select('#_nowVal')

for stock in stock_now:
    print(stock.text)