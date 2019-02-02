#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Day 20: Sorting

Source : https://www.hackerrank.com/challenges/30-sorting/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
"""
_ = input()
a = list(map(int, input().split()))
numberOfSwaps = 0
for i in range(len(a)):
    for j in range(len(a)-1):
        k = j+1
        if a[j] > a[k]:
            a[j], a[k] = a[k], a[j]
            numberOfSwaps += 1

print(f"Array is sorted in {numberOfSwaps} swaps.")
print(f"First Element: {a[0]}")
print(f"Last Element: {a[-1]}")
