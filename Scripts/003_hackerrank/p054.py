#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 054

Set .difference() Operation

Source : https://www.hackerrank.com/challenges/py-set-difference-operation/problem
"""
a, b = [set(map(int,input().split())) for i in range(4)][1::2]
print(len(a-b))
