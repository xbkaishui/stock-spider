# -*- coding: utf-8 -*-
from spiders.spider import Spider
import requests
import json

class NasdaqSpider(Spider):

    def __init__(self):
        self.base_url = 'https://api.nasdaq.com/api/quote/{0}/chart?assetclass=stocks&fromdate={1}&todate={2}'

    """
     get specify stock data by start and end date
     @:return kline
    """
    def get_stock_data(self, symbol, start, end):
        headers = {
            "authority":'api.nasdaq.com',
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "deflate",
            "Accept-Language": "en-GB,en;q=0.9,en-US;q=0.8,ml;q=0.7",
            "Connection": "keep-alive",
            "Origin":"https://www.nasdaq.com",
            "sec-fetch-mode":"cors",
            "sec-fetch-site":"same-site",
            "Referer": "https://www.nasdaq.com/market-activity/stocks/amzn",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36"
        }
        url = self.base_url.format(symbol, start, end)
        resp = requests.get(url, headers = headers, verify=False)
        stock_datas = resp.json()['data']['chart']
        if stock_datas and len(stock_datas) > 0:
            print(json.dumps(stock_datas))
        return stock_datas