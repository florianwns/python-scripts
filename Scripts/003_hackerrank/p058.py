#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 058

Check Subset

Source : https://www.hackerrank.com/challenges/py-check-subset/problem
"""
for _ in range(int(input())):
    a, b = [set(map(int, input().split())) for _ in range(4)][1::2]
    print(a.issubset(b))
