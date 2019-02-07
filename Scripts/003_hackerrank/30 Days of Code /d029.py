#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Day 29: Bitwise AND

Source : https://www.hackerrank.com/challenges/30-bitwise-and/problem?h_r=next-challenge&h_v=zen
"""
from itertools import combinations

def get_max(n, k):
    m = 0
    for t in combinations(range(1, n+1), 2):
        r = t[0]&t[1]
        if r < k and r > m:
            m = r
        if m == k - 1:
            break
    return m
"""
res = []
for _ in range(int(input())):
    n, k = map(int, input().split())
    res.append(get_max(n, k))
print(*res, sep="\n")
"""
res = []
for _ in range(500):
    res.append(get_max(800, 50))
print(*res, sep="\n")
