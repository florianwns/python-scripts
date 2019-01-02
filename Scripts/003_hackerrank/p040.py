#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 040

Zeros and Ones

Source : https://www.hackerrank.com/challenges/np-zeros-and-ones/problem
"""
import numpy as np

n = np.array(input().split(), int)
print(np.zeros(n, dtype=int))
print(np.ones(n, dtype=int))
