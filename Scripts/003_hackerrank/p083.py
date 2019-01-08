#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 083

Detect Floating Point Number

Source : https://www.hackerrank.com/challenges/introduction-to-regex/problem
"""
import re
r = r"^[+|-]?\d*\.\d+$"
[print(bool(re.match(r, input()))) for _ in range(int(input()))]
