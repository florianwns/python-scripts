#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 034

Polynomials

Source : https://www.hackerrank.com/challenges/np-polynomials/problem
"""
import numpy as np

n = np.array(input().split(), float)
m = float(input())
print(np.polyval(n, m))
