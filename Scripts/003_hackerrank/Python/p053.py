#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 053

Set .intersection() Operation

Source : https://www.hackerrank.com/challenges/py-set-intersection-operation/problem
"""
a, b = [set(map(int,input().split())) for i in range(4)][1::2]
print(len(a&b))
