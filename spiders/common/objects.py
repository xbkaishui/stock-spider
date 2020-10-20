# -*- coding: utf-8 -*-

from dataclasses import dataclass


@dataclass
class Symbol:
    symbol: str = None
    company: str = None
    sector: str = None
    industry: str = None


@dataclass
class Kline:
    symbol: str = None
    high: float = None
    low: float = None
    open: float = None
    close: float = None
    volume: float = None
    dateTime: str = None
    value: float = None

if __name__ == '__main__':
    symbol = Symbol()
    symbol.company = "11"
    print(symbol)
