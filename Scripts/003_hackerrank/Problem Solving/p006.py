#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 006

Plus Minus

Source : https://www.hackerrank.com/challenges/plus-minus/problem
"""
n, l = int(input()), list(map(int, input().split()))
print("%.6f" % (len([x for x in l if x > 0])/n))
print("%.6f" % (len([x for x in l if x < 0])/n))
print("%.6f" % (len([x for x in l if x == 0])/n))
