#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Day 29: Bitwise AND

Source : https://www.hackerrank.com/challenges/30-bitwise-and/problem?h_r=next-challenge&h_v=zen
"""
for _ in range(int(input())):
    n, k = map(int, input().split())
    s = list(range(1, n+1))
    print(max([i&j for i in s[:-1] for j in s[1:] if i!=j  and i&j < k]))
