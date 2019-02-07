#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 113

Find Angle MBC

Source : https://www.hackerrank.com/challenges/find-angle/problem
"""
from math import *
ab, bc = [int(input()) for _ in range(2)]
print(str(int(degrees(atan2(ab,bc)) + 0.5))+'°')
