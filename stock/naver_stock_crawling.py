import requests
from bs4 import BeautifulSoup


def sise():
    html = requests.get('https://finance.naver.com/item/sise.nhn?code=005930')
    # print(html.text)

    soup = BeautifulSoup(html.text, 'html.parser')

    stock_now = soup.select('#_nowVal')

    for stock in stock_now:
        print(stock.text)


def stock_list():
    html = requests.get('https://finance.naver.com/sise/sise_market_sum.nhn')
    # print(html.text)
    soup = BeautifulSoup(html.text, 'html.parser')

    stock_tag = soup.select('table > tbody > tr > td:nth-child(2) > a')

    stock_now = soup.select('table > tbody > tr > td:nth-child(3)')

    # print(stock_now)

    num = 0
    for tags in stock_tag:
        num += 1
        if num == 11:
            break
        company_name = tags.text
        company_code = tags['href'].split('=')[1]
        print(company_name, company_code)

    num = 0
    for tags in stock_now:
        num += 1
        if num == 11:
            break
        company_stock = tags.text
        print(company_stock)




stock_list()