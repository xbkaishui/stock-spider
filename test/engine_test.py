from unittest import TestCase, main

from spiders.engine import CrawlerEngine

class TestCrawlerEngine(TestCase):

    def test_sync_all_nasdaq(self):
        engine = CrawlerEngine()
        engine.sync_all_nasdaq("/tmp/stocks", '2010-01-01', '2020-12-04')

if __name__ == '__main__':
    main()
