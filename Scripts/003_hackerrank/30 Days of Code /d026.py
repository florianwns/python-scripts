#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Day 26: Nested Logic

Source : https://www.hackerrank.com/challenges/30-nested-logic/problem
"""
from datetime import date

d1 = date(*list(map(int,input().split()))[::-1])
d2 = date(*list(map(int,input().split()))[::-1])

if d1 < d2:
    print(0)
elif d1.year > d2.year:
    print(10000)
elif d1.month > d2.month:
    print(500 * (d1.month - d2.month))
else:
    print(15 * (d1-d2).days)
