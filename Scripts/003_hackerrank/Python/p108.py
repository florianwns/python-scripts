#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 108

collections.Counter()

Source : https://www.hackerrank.com/challenges/collections-counter/problem
"""
from collections import Counter
_ = input()
shoes = Counter(map(int, input().split()))
total = 0
for _ in range(int(input())):
    size, price = map(int, input().split())
    if shoes[size]:
        shoes[size] -= 1
        total += price
print(total)
