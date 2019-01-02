#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 044

Sum and Prod

Source : https://www.hackerrank.com/challenges/np-sum-and-prod/problem
"""
import numpy as np

n, m = map(int, input().split())
ar = np.array([input().split() for _ in range(n)], int)
print(np.prod(np.sum(ar, axis = 0)))
