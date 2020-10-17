from unittest import TestCase, main

from spiders.common.constant import Exchange
from spiders.symbols import *


class TestSymbols(TestCase):
    def test_get_exchange_url(self):
        url = get_exchange_url(Exchange.AMEX)
        self.assertEqual(url,
                         'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=AMEX&render=download')

    def test_get_exchange_symbols(self):
        symbols = get_exchange_symbols(Exchange.NASDAQ)
        self.assertIsNotNone(symbols)

if __name__ == '__main__':
    main()
