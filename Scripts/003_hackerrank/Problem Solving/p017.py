#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 017

Grading Students

Source : https://www.hackerrank.com/challenges/grading/problem
"""
for _ in range(int(input())):
    n = int(input())
    d = 5 - n % 5
    print(n if n < 38 or d > 2 else n + d)
