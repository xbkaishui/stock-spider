# -*- coding: utf-8 -*-
import csv
import os
import re

import requests
from hyper.contrib import HTTP20Adapter
from spiders.common.objects import Symbol
from spiders.util import is_cached
from hyper import HTTPConnection

headers = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"en-GB,en;q=0.9,en-US;q=0.8,ml;q=0.7",
    "Connection":"keep-alive",
    "Host":"www.nasdaq.com",
    "Referer":"http://www.nasdaq.com",
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36"
}

def get_exchange_url(exchange):
    return ("http://www.nasdaq.com/screening/companies-by-industry.aspx?"
            "exchange={}&render=download".format(exchange.name))


def fetch_file(url):
    print(url)
    session = requests.session()
    session.mount(url, HTTP20Adapter())
    req = session.request("GET", "https://www.nasdaq.com/api/v1/screener?page=1&pageSize=200",
                           headers=headers, verify=False)
    return req.text


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
        symbol_data.sector = row[6]
        symbol_data.industry = row[7]
        symbol_list.append(symbol_data)
    return symbol_list


def get_exchange_symbols(exchange):
    """
     read symbols from exchange

    """
    url = get_exchange_url(exchange)
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/", exchange.name)
    print(file_path)
    if is_cached(file_path):
        with open(file_path, "r") as cached_file:
            symbol_data = cached_file.read()
    else:
        symbol_data = fetch_file(url)
        save_file(file_path, symbol_data)

    return read_symbol_list(symbol_data)
