# -*- coding: utf-8 -*-

from spiders.symbols import get_exchange_symbols
from spiders.common.constant import Exchange
import os
from spiders.nasdaq import NasdaqSpider
from spiders.util import is_cached
from multiprocessing import Pool

class CrawlerEngine(object):

    def __init__(self):
        self.spider = NasdaqSpider()

    """
     sync all stock to local path, support multi thread
    """
    def sync_all_nasdaq(self, file_path, start, end, cache = True):
        symbols = get_exchange_symbols(Exchange.NASDAQ)
        print("symbols size " + str(len(symbols)))
        self.create_dir_if_needed(file_path)
        cpu_count = os.cpu_count()
        pool = Pool(cpu_count)
        sync_params = []
        for symbol in symbols:
            param = {"symbol":symbol, "file_path":file_path, "start":start, "end":end, "cache":cache}
            sync_params.append(param)
        pool.map(self.sync_single_symbol, sync_params)

    def create_dir_if_needed(self, file_path):
        if not os.path.exists(file_path):
            os.mkdir(file_path)

    def sync_single_symbol(self, param):
        symbol = param['symbol']
        file_path = param['file_path']
        start  = param['start']
        end = param['end']
        cache = param['cache']
        try:
            code = symbol.symbol
            stock_path = os.path.join(file_path, code+".csv")
            if cache and is_cached(stock_path):
                print("file is cached ignore " + stock_path)
                return
            print("try to sync symbol " + code)
            self.spider.store_kline_data(stock_path, code, start, end)
        except :
            print("fetch symbol error " + symbol.symbol + " ignore")



