#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 016

Kangaroo

Source : https://www.hackerrank.com/challenges/kangaroo/problem
"""
x1, v1, x2, v2 = map(int, input().split())
try:
    assert v2 < v1
    assert (x1-x2) % (v2-v1) == 0
except:
    print("NO")
else:
    print("YES")
    
