#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 035

Linear Algebra

Source : https://www.hackerrank.com/challenges/np-linear-algebra/problem
"""
import numpy as np
a = [np.array(input().split(), float) for _ in range(int(input()))]
print(round(np.linalg.det(a), 2))
