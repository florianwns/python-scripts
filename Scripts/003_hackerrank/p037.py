#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 037

Shape and Reshape

Source : https://www.hackerrank.com/challenges/np-shape-reshape/problem
"""
import numpy as np

ar = np.array(input().split(), int)
print(np.reshape(ar, (3, 3)))
