#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 018

Between Two Sets

Source : https://www.hackerrank.com/challenges/between-two-sets/problem
"""
from math import gcd
from functools import reduce

_ = input()
a = map(int, input().split())
b = map(int, input().split())
# find the Least Common Multiple (LCM) of all the integers of array A.
lcm = lambda x, y: x * y // gcd(x,y)
l = reduce(lcm, a)
# find the Greatest Common Divisor (GCD) of all the integers of array B.
g = reduce(gcd, b)
# Count the number of multiples of LCM that evenly divides the GCD.
print(len([i for i in range(1, g//l + 1) if g % (l * i) == 0]))
