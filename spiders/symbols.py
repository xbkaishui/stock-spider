# -*- coding: utf-8 -*-
import csv
import os
import re

import requests
from hyper.contrib import HTTP20Adapter

from spiders.common.objects import Symbol
from spiders.util import is_cached

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-GB,en;q=0.9,en-US;q=0.8,ml;q=0.7",
    "Connection": "keep-alive",
    "Host": "www.nasdaq.com",
    "Referer": "http://www.nasdaq.com",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36"
}


def get_exchange_url(exchange):
    return ("http://www.nasdaq.com/screening/companies-by-industry.aspx?"
            "exchange={}&render=download".format(exchange.name))


def fetch_file(exchange):
    url = get_exchange_url(exchange)
    session = requests.session()
    session.mount(url, HTTP20Adapter())
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/", exchange.name)
    out = open(file_path, 'a', newline='\n')
    csv_writer = csv.writer(out, delimiter=',')
    for i in range(50):
        print("start crawler page " + str(i+1))
        url = "https://www.nasdaq.com/api/v1/screener?page="+str(i+1)+"&pageSize=200"
        req = session.request("GET", url,
                              headers=headers, verify=False)
        json_obj = req.json()
        rows = json_obj['data']
        if rows is None:
            continue

        for row in rows:
            ticker = row['ticker']
            company = row['company']
            marketCapGroup = row['marketCapGroup']
            sector = row['sectorName']
            gicsSector = row['gicsSector']
            csv_writer.writerow([ticker, company, marketCapGroup, sector, gicsSector])


def save_file(file_path, symbol_data):
    with open(file_path, "w") as saved_file:
        saved_file.write(symbol_data)


def read_symbol_list(symbol_data):
    symbol_list = list()
    symbol_data = re.split("\r?\n", symbol_data)
    # symbol,company,sector,industry,headquaters
    symbol_data = list(csv.reader(symbol_data, delimiter=','))
    # We need to cut off the the last row because it is a null string
    for row in symbol_data[1:-1]:
        symbol_data = Symbol()
        symbol_data.symbol = row[0]
        symbol_data.company = row[1]
        symbol_data.sector = row[2]
        symbol_data.industry = row[3]
        symbol_list.append(symbol_data)
    return symbol_list


def get_exchange_symbols(exchange):
    """
     read symbols from exchange

    """
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/", exchange.name)
    print(file_path)
    if not is_cached(file_path):
        fetch_file(exchange)
    symbol_data = None
    with open(file_path, "r") as cached_file:
        symbol_data = cached_file.read()
    return read_symbol_list(symbol_data)
