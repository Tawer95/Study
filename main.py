import requests
from bs4 import BeautifulSoup as BS
import fake_useragent as fu
import csv



user_agent = fu.UserAgent().random

headers = {
    'user-agent': user_agent,
}

url = 'https://www.coingecko.com/'
response = requests.get(url, headers=headers)
html = BS(response.content, 'html.parser')


def name_coin(html):
    name_coins = []
    names = html.select('.sort.table.mb-0.text-sm.text-lg-normal.table-scrollable')[0].select('tr')[1:]
    for name in names:
        coin = name.select('.font-bold.tw-items-center.tw-justify-between')[0].text.strip() # strip обрезает неровности
        name_coins.append(coin)
    return name_coins


def ticker_coin(html):
    name_tickers = []
    tickers = html.select('.sort.table.mb-0.text-sm.text-lg-normal.table-scrollable')[0].select('tr')[1:]
    for ticker in tickers:
        coin = ticker.select('.d-lg-inline.font-normal.text-3xs.tw-ml-0.tw-text-gray-500')[0].text.strip() # strip обрезает неровности
        name_tickers.append(coin)
    return name_tickers


def price_coin(html):
    prices_coins = []
    prices = html.select('.tw-flex.tw-justify-between.tw-items-center.tw-gap-2')
    for price in prices:
        count = price.text.strip()
        prices_coins.append(count)
    return prices_coins


def change_1h(html):
    changes_1h = []
    changes = html.select('.td-change1h.change1h.stat-percent.text-right.col-market')
    for change in changes:
        count = change.text.strip()
        changes_1h.append(count)
    return changes_1h


def change_24h(html):
    changes_24h = []
    changes = html.select('.td-change24h.change24h.stat-percent.text-right.col-market')
    for change in changes:
        count = change.text.strip()
        changes_24h.append(count)
    return changes_24h


def change_7d(html):
    changes_7d = []
    changes = html.select('.td-change7d.change7d.stat-percent.text-right.col-market')
    for change in changes:
        count = change.text.strip()
        changes_7d.append(count)
    return changes_7d


def volume_24h(html):
    volumes_24h = []
    volumes = html.select('.td-liquidity_score.lit.text-right.col-market')
    for volume in volumes:
        count = volume.text.strip()
        volumes_24h.append(count)
    return volumes_24h


def Mcap(html):
    Mcaps_all = []
    Mcaps = html.select('.td-market_cap.cap.col-market.cap-price.text-right')
    for mcap in Mcaps:
        count = mcap.text.strip()
        Mcaps_all.append(count)
    return Mcaps_all

name_coins = name_coin(html)
name_tickers = ticker_coin(html)
prices_coins = price_coin(html)
changes_1h = change_1h(html)
changes_24h = change_24h(html)
changes_7d = change_7d(html)
volumes_24h = volume_24h(html)
Mcaps_all = Mcap(html)

full_list = [[] for i in range(len(name_coins))] # все списки одной размерности, поэтому любой можно выбирать.

for row in range(len(name_coins)):
    full_list[row].append(name_coins[row])
    full_list[row].append(name_tickers[row])
    full_list[row].append(prices_coins[row])
    full_list[row].append(changes_1h[row])
    full_list[row].append(changes_24h[row])
    full_list[row].append(changes_7d[row])
    full_list[row].append(volumes_24h[row])
    full_list[row].append(Mcaps_all[row])


print(full_list)


with open('coin_gecko_parsing/cg_parsing.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(full_list)



    






# document.querySelector('.font-bold.tw-items-center.tw-justify-between'); - Name
# document.querySelector('.sort.table.mb-0.text-sm.text-lg-normal.table-scrollable').querySelectorAll('tr')[2].querySelector('.d-lg-inline.font-normal.text-3xs.tw-ml-0.tw-text-gray-500') - Ticker
# document.querySelector('.tw-flex.tw-justify-between.tw-items-center.tw-gap-2').querySelector('.no-wrap'); - price
# document.querySelector('.tw-flex.tw-justify-between.tw-items-center.tw-gap-2').querySelector('.text-danger'); - price
