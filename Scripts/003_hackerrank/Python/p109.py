#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 109

DefaultDict Tutorial

Source : https://www.hackerrank.com/challenges/defaultdict-tutorial/problem
"""
from collections import defaultdict
d =  defaultdict(list)
n, m = map(int, input().split())
[d[input()].append(i) for i in range(1, n+1)]
[print(" ".join(map(str, d[input()])) or -1) for i in range(m)]
