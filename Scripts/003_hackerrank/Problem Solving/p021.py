#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 021

Divisible Sum Pairs

Source : https://www.hackerrank.com/challenges/divisible-sum-pairs/problem
"""
_, d = map(int, input().split())
numbers = list(map(int, input().split()))
nb = len(numbers)
count = 0
for i in range(nb-1):
    for j in range(i+1, nb):
        count += (numbers[i] + numbers[j]) % d == 0
print(count)
