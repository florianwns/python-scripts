#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 037

Transpose and Flatten

Source : https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem
"""
import numpy as np

n, m = map(int, input().split())
ar = np.array([input().split() for _ in range(n)], int)
print(np.transpose(ar))
print(ar.flatten())
