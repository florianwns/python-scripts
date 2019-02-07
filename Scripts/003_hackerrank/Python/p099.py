#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 099

Incorrect Regex

Source : https://www.hackerrank.com/challenges/incorrect-regex/problem
"""
import re
for _ in range(int(input())):
    try:
        re.compile(input())
        print(True)
    except re.error:
        print(False)
