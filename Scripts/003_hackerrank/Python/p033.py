#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 033

Inner and Outer

Source : https://www.hackerrank.com/challenges/np-inner-and-outer/problem
"""
import numpy as np

a, b = [np.array(input().split(), int) for _ in range(2)]
print(np.inner(a, b), np.outer(a, b), sep="\n")
