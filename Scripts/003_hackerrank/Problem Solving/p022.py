#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 022

Migratory Birds

Source : https://www.hackerrank.com/challenges/migratory-birds/problem
"""
from collections import Counter
_ = input()
birds = list(map(int, input().split()))
print(sorted(Counter(birds).items(), key=lambda x: (-x[1], x[0]))[0][0])
