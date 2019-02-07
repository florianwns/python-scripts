#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 045

Min and Max

Source : https://www.hackerrank.com/challenges/np-min-and-max/problem
"""
import numpy as np

n, m = map(int, input().split())
ar = np.array([input().split() for _ in range(n)], int)
print(np.max(np.min(ar, axis = 1)))
