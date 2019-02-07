#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 061

Any or All

Source : https://www.hackerrank.com/challenges/any-or-all/problem
"""
n, l = int(input()), input().split()
a, b = [int(x) > 0 for x in l], [x == x[::-1] for x in l]
print(all(a) and any(b))
