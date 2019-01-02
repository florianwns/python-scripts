#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 043

Floor, Ceil and Rint

Source : https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem
"""
import numpy as np

np.set_printoptions(sign=' ')
a = np.array(input().split(), float)
print(np.floor(a), np.ceil(a), np.rint(a), sep="\n")
