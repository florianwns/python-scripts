#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 039

Concatenate

Source : https://www.hackerrank.com/challenges/np-concatenate/problem
"""
import numpy as np

n, m, p = map(int, input().split())
a = np.array([input().split() for _ in range(n)], int)
b = np.array([input().split() for _ in range(m)], int)
print(np.concatenate((a, b)))
