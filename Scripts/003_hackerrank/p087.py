#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 087

Collections.namedtuple()

Source : https://www.hackerrank.com/challenges/py-collections-namedtuple/problem
"""
from collections import OrderedDict
smkt = OrderedDict()
for _ in range(int(input())):
    name, number = input().rsplit(maxsplit = 1)
    smkt[name] = smkt[name] + int(number) if name in smkt else int(number)
[print(k, v) for k, v in smkt.items()]
