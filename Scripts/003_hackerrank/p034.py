#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 034

Polynomials

Source : https://www.hackerrank.com/challenges/np-polynomials/problem
"""
import numpy as np

p = np.poly1d(np.array(input().split(), float))
x = int(input())
print(p(x))
