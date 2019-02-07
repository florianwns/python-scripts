#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 113

Find Angle MBC

Source : https://www.hackerrank.com/challenges/find-angle/problem
"""
from math import *
ab, bc = 100, 1
print(int(degrees(atan(ab/bc))+0.5))
