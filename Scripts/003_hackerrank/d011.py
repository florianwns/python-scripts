#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Day 11: 2D Arrays

Source : https://www.hackerrank.com/challenges/30-2d-arrays/problem
"""

a = [list(map(int, input().rstrip().split())) for _ in range(6)]
sums = []
for i in range(4):
    for j in range(4):
        sums.append(sum(a[i][j:j+3]) + a[i+1][j+1] + sum(a[i+2][j:j+3]))
print(max(sums))
