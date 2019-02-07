#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 015

Hex Color Code

Source : https://www.hackerrank.com/challenges/hex-color-code/problem
"""
import re

regex_hex_color = r"(?!^)(#[a-fA-F0-9]{1,2}[a-fA-F0-9]{1,2}[a-fA-F0-9]{1,2})"
for _ in range(int(input())):
    for hex_color in re.findall(regex_hex_color, input()):
        print(hex_color)
