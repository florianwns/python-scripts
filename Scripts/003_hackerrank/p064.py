#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 064

Iterables and Iterators

Source : https://www.hackerrank.com/challenges/iterables-and-iterators/problem
"""
from itertools import combinations
n = int(input())
l = list(combinations(input().replace(' ', ''), int(input())))
b = filter(lambda c: 'a' in c, l)
print(len(list(b))/len(l))
