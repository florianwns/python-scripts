#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 081

itertools.combinations()

Source : https://www.hackerrank.com/challenges/itertools-combinations/problem
"""
from itertools import combinations
s, k = input().split()
for i in range(1, int(k)+1):
    [print(''.join(c)) for c in combinations(sorted(s), i)]
