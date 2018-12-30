#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 030

Capitalize!

Source : https://www.hackerrank.com/challenges/capitalize/problem
"""
import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    out = ""
    for i in range(len(s)):
        out += (s[i].upper() if s[i].isalpha()
            and (i == 0 or s[i-1].isspace())
            else s[i].lower())
    return out

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
