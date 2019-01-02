#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 052

Set .union() Operation

Source : https://www.hackerrank.com/challenges/py-set-union/problem
"""
a, b = [set(map(int,input().split())) for i in range(4)][1::2]
print(len(a|b))
