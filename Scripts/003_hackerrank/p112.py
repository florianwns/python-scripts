#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 111

Polar Coordinates

Source : https://www.hackerrank.com/challenges/polar-coordinates/problem
"""
from cmath import polar
print(*polar(complex(input())), sep="\n")
