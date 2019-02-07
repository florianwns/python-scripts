#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 055

Set .symmetric_difference() Operation

Source : https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem
"""
a, b = [set(map(int,input().split())) for i in range(4)][1::2]
print(len(a^b))
