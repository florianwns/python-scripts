#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 003

Compare the Triplets

Source : https://www.hackerrank.com/challenges/compare-the-triplets/problem
"""
a, b = [list(map(int, input().split())) for _ in range(2)]
alice, bob = 0, 0
for i, j in zip(a, b):
    if i > j:
        alice+=1
    elif i < j:
        bob+=1
print(alice, bob)
