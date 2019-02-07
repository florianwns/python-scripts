#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 088

Word Order

Source : https://www.hackerrank.com/challenges/word-order/problem
"""
from collections import Counter, OrderedDict
class OrderedCounter(Counter, OrderedDict):
    pass
words = OrderedCounter(input() for _ in range(int(input())))
print(len(words))
print(*words.values())
