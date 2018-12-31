#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 036

Validating phone numbers

Source : https://www.hackerrank.com/challenges/validating-the-phone-number/problem
"""
import re

for _ in range(int(input())):
    print("YES" if re.match(r"^[789]\d{9}$", input()) else "NO")
