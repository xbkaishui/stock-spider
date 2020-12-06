# -*- coding: utf-8 -*-

from spiders.symbols import get_exchange_symbols
from spiders.common.constant import Exchange
import os
from spiders.nasdaq import NasdaqSpider
from spiders.util import is_cached

class CrawlerEngine(object):

    """
     sync all stock to local path
    """
    def sync_all_nasdaq(self, file_path, start, end, cache = True):
        spider = NasdaqSpider()
        symbols = get_exchange_symbols(Exchange.NASDAQ)
        print("symbols size " + str(len(symbols)))
        self.create_dir_if_needed(file_path)
        for symbol in symbols:
            try:
                code = symbol.symbol
                stock_path = os.path.join(file_path, code+".csv")
                if cache and is_cached(stock_path):
                    print("file is cached ignore " + stock_path)
                    continue
                print("try to sync symbol " + code )
                spider.store_kline_data(stock_path, code, start, end)
            except :
                print("fetch symbol error " + symbol + " ignore")

    def create_dir_if_needed(self, file_path):
        if not os.path.exists(file_path):
            os.mkdir(file_path)



