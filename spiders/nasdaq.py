# -*- coding: utf-8 -*-
from spiders.spider import Spider
import requests
import json
from spiders.common.objects import Kline

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
        klines = []
        if stock_datas and len(stock_datas) > 0:
            print(json.dumps(stock_datas))
            for stock_data in stock_datas :
                stock_info = stock_data['z']
                kline = Kline()
                kline.symbol = symbol
                kline.high =  float(stock_info['high'])
                kline.low = float(stock_info['low'])
                kline.open = float(stock_info['open'])
                kline.close = float(stock_info['close'])
                kline.volume = float(stock_info['volume'].replace(',',''))
                kline.value = float(stock_info['value'])
                kline.dateTime = stock_info['dateTime']
                klines.append(kline)
        return klines