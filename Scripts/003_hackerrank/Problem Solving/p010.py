#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 010

Time Conversion

Source : https://www.hackerrank.com/challenges/time-conversion/problem
"""
t = input()
h, m, s = int(t[:2])%12, t[3:5], t[6:8]
if t[8:] == "PM":
    h += 12
print(f"{h:02d}:{m}:{s}")
