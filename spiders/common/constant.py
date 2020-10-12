# -*- coding: utf-8 -*-

from enum import Enum, unique


@unique
class Exchange(Enum):
    NYSE = 1
    AMEX = 2
    NASDAQ = 3
