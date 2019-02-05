#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 102

itertools.product()

Source : https://www.hackerrank.com/challenges/itertools-product/problem
"""
from itertools import product
a, b = [list(map(int, input().split())) for i in range(2)]
print(*list(product(a, b)))
