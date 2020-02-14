#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Day 9: Recursion 3

Source : https://www.hackerrank.com/challenges/30-recursion/problem
"""
from functools import reduce

def factorial(n):
    return reduce(lambda x, y: x*y, range(1,n+1), 1)

n = int(input())
print(factorial(n))
