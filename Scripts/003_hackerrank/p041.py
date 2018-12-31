#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 040

Zeros and Ones

Source : https://www.hackerrank.com/challenges/np-zeros-and-ones/problem
"""
import numpy as np
np.set_printoptions(sign=' ')
n, m = map(int, input().split())
print(np.eye(n, m))
