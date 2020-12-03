# stock-spider
Spider US stocks. for quant research purpose, star if you like

## usage
### pip install stock-spider

#### batch save all stocks

``` python
from spiders.engine import CrawlerEngine
engine = CrawlerEngine()
engine.sync_all_nasdaq("/tmp/stocks", '2019-08-01', '2020-10-10')

```

#### get single stock 
``` python
from spiders.nasdaq import NasdaqSpider  
spider = NasdaqSpider()
spider.store_kline_data("/tmp/amzn.csv", 'AMZN', '2019-08-01', '2020-10-10') 

```


## please submit a issue if you have any questions


## reference
https://www.scrapehero.com/scrape-nasdaq-stock-market-data/
http://skillachie.github.io/finsymbols/
https://github.com/ranaroussi/yfinance
https://www.zhihu.com/question/22145919
https://medium.com/ai%E8%82%A1%E4%BB%94/%E7%94%A8-python-%E6%89%93%E9%80%A0%E8%87%AA%E5%B7%B1%E7%9A%84%E8%82%A1%E5%B8%82%E8%B3%87%E6%96%99%E5%BA%AB-%E7%BE%8E%E8%82%A1%E7%AF%87-e3e896659fd6
https://zhuanlan.zhihu.com/p/143144116

### how to reach me
by twitter (xbkaishui1) or wechat (xbkaishui) 
