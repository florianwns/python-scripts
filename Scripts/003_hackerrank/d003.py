#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Day 3: Intro to Conditional Statements

Source : https://www.hackerrank.com/challenges/30-conditional-statements/problem
"""
try:
    n = int(input())
    even = n % 2 == 0
    in_range = n in range(2,6) or n > 20
    assert even and in_range
except:
    print("Weird")
else:
    print("Not Weird")
