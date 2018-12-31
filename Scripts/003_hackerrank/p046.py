#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 046

Mean, Var, and Std

Source : https://www.hackerrank.com/challenges/np-mean-var-and-std/problem
"""
import numpy as np

np.set_printoptions(legacy='1.13')
n, m = map(int, input().split())
ar = np.array([input().split() for _ in range(n)], int)
print(np.mean(ar, axis = 1), np.var(ar, axis = 0), np.std(ar), sep="\n")
