#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 106

Piling Up!

Source : https://www.hackerrank.com/challenges/piling-up/problem
"""
for _ in range(int(input())):
    n, i= int(input()) - 1, 0
    l = list(map(int, input().split()))
    while i < n and l[i] >= l[i+1]:
        i += 1
    while i < n and l[i] <= l[i+1]:
        i += 1
    print("Yes" if i == n else "No")
