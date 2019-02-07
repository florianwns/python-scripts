#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 010

Time Conversion

Source : https://www.hackerrank.com/challenges/time-conversion/problem
"""
t = input()
h = 12 + int(t[:2])%12 if t[8:] == "PM" else int(t[:2])%12
m = t[3:5]
s = t[6:8]
print(f"{h:02d}:{m}:{s}")
