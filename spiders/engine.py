# -*- coding: utf-8 -*-

from spiders.symbols import get_exchange_symbols
from spiders.common.constant import Exchange
import os
from spiders.nasdaq import NasdaqSpider

class CrawlerEngine(object):

    """
     sync all stock to local path
    """
    def sync_all_nasdaq(self, file_path, start, end):
        spider = NasdaqSpider()
        symbols = get_exchange_symbols(Exchange.NASDAQ)
        print("symbols size " + str(len(symbols)))
        self.create_dir_if_needed(file_path)
        for symbol in symbols:
            code = symbol.symbol
            stock_path = os.path.join(file_path, code+".csv")
            print("try to sync symbol " + code )
            spider.store_kline_data(stock_path, code, start, end)

    def create_dir_if_needed(self, file_path):
        if not os.path.exists(file_path):
            os.mkdir(file_path)



