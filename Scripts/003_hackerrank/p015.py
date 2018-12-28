#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 014

Hex Color Code

Source : https://www.hackerrank.com/challenges/hex-color-code/problem
"""
import re

regex_hex_color = r"(#[a-fA-F0-9]{1,2}[a-fA-F0-9]{1,2}[a-fA-F0-9]{1,2})"
for _ in range(int(input())):
    line = input()
    line = line[1:-1]
    for hex_color in re.findall(regex_hex_color, line):
        print(hex_color)
