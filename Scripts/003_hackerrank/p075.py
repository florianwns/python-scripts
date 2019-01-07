#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 075

Power - Mod Power

Source : https://www.hackerrank.com/challenges/python-power-mod-power/problem
"""
a, b, m = (int(input()) for _ in range(3))
print(pow(a, b))
print(pow(a, b, m))
