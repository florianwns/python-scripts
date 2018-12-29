#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 027

Designer Door Mat

Source : https://www.hackerrank.com/challenges/designer-door-mat/problem
"""
word = "WELCOME"
motif1 = ".|."
motif2 = "-"

row, col = map(int, input().split())

# top
for i in range(row//2):
    print((motif1*i*2+motif1).center(col, motif2))

# middle
print(word.center(col, motif2))

# bottom
for i in reversed(range(row//2)):
    print((motif1*i*2+motif1).center(col, motif2))
