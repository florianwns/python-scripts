#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 006

Print Function

Source : https://www.hackerrank.com/challenges/python-print/problem
"""

a = int(input())
i = 1
while i <= a:
    print(i, end="")
    i += 1


"""
print(*range(1, int(input())+1), sep='')
""
