#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 041

Eye and Identity

Source : https://www.hackerrank.com/challenges/np-eye-and-identity/problem
"""
import numpy as np
np.set_printoptions(sign=' ')
n, m = map(int, input().split())
print(np.eye(n, m))
