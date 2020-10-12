# -*- coding: utf-8 -*-

from dataclasses import dataclass


@dataclass
class Symbol:
    symbol: str = None
    company: str = None
    sector: str = None
    industry: str = None


if __name__ == '__main__':
    symbol = Symbol()
    symbol.company = "11"
    print(symbol)
