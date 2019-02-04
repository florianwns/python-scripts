#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 091

Arrays

Source : https://www.hackerrank.com/challenges/np-arrays/problem
"""
import numpy

def arrays(arr):
    return numpy.array(arr, float)[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
