from unittest import TestCase, main

from spiders.nasdaq import NasdaqSpider


class TestNasdaqSpider(TestCase):
    def test_get_stock_data(self):
        spider = NasdaqSpider()
        symbol = 'AMZN'
        data = spider.get_stock_data(symbol, '2019-08-01', '2020-10-10')
        self.assertIsNotNone(data)


if __name__ == '__main__':
    main()
