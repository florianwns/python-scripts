#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 105

Zipped!

Source : https://www.hackerrank.com/challenges/zipped/problem
"""
n, x = map(int, input().split())
arr = []
for _ in range(x):
    arr.append(list(map(float, input().split())))

for scores in zip(*arr):
    print(sum(scores)/len(scores))
