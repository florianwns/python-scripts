#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 048

Symmetric Difference

Source : https://www.hackerrank.com/challenges/symmetric-difference/problem
"""
a, b = [set(map(int, input().split())) for _ in range(4)][1::2]
[print(x) for x in sorted(a^b)]
