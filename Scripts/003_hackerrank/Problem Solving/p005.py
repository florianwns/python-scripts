#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 005

Diagonal Difference

Source : https://www.hackerrank.com/challenges/diagonal-difference/problem
"""
n = int(input())
sum = 0
for i, j in zip(range(n), reversed(range(n))):
    l = list(map(int, input().split()))
    sum += l[i] - l[j]
print(abs(sum))
