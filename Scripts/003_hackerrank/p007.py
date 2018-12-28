#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 007

List Comprehensions

Source : https://www.hackerrank.com/challenges/list-comprehensions/problem
"""

x = int(input())
y = int(input())
z = int(input())
n = int(input())
ar = []
for i in range(0,x+1):
    for j in range(0,y+1):
        for k in range(0,z+1):
            if i + j + k != n:
                ar.append([i,j,k])
print(ar)


"""
x, y, z, n = (int(input()) for _ in range(4))
print ([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a + b + c != n ])
"""
