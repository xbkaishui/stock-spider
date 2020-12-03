from unittest import TestCase, main

from spiders.engine import CrawlerEngine

class TestCrawlerEngine(TestCase):

    def test_sync_all_nasdaq(self):
        engine = CrawlerEngine()
        engine.sync_all_nasdaq("/tmp/stocks", '2019-08-01', '2020-10-10')

if __name__ == '__main__':
    main()
