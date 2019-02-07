#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 065

Maximize It!

Source : https://www.hackerrank.com/challenges/maximize-it/problem
"""
from itertools import product, repeat
k, m = map(int, input().split())
l = [list(map(pow, map(int, input().split()), repeat(2)))[1:] for _ in range(k)]
print(max(sum(x) % m for x in product(*l)))
