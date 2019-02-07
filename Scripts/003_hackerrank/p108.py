#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 108

collections.Counter()

Source : https://www.hackerrank.com/challenges/collections-counter/problem
"""
from collections import Counter

#_ = input()
shoes = Counter(map(int, "2 3 4 5 6 8 7 6 5 18".split()))
total = 0
for _ in range(6):
    size, price = map(int, "6 55".split())
    if shoes[size]:
        shoes[size] -= 1
        total += price
print(total)
