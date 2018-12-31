#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 047

Dot and Cross

Source : https://www.hackerrank.com/challenges/np-dot-and-cross/problem
"""
import numpy as np

n = int(input())
a, b = [np.array([input().split() for _ in range(n)], int) for _ in range(2)]
print(np.dot(a, b))
