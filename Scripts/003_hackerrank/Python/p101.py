#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 101

Time Delta

Source : https://www.hackerrank.com/challenges/python-time-delta/problem

https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
"""
from datetime import datetime
fmt = "%a %d %b %Y %H:%M:%S %z"
for _ in range(int(input())):
    t1 = datetime.strptime(input(), fmt)
    t2 = datetime.strptime(input(), fmt)
    print(int(abs(t1 - t2).total_seconds()))
