#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 087

Collections.namedtuple()

Source : https://www.hackerrank.com/challenges/py-collections-namedtuple/problem
"""
from collections import OrderedDict
smkt = OrderedDict()
for _ in range(int(input())):
    item, price = input().rsplit(maxsplit = 1)
    smkt.setdefault(item, 0)
    smkt[item] += int(price)
[print(k, v) for k, v in smkt.items()]
