#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 024

String Validators

Source : https://www.hackerrank.com/challenges/string-validators/problem
"""
from functools import reduce
s = input()
print(reduce(lambda a, b: a or b,[c.isalnum() for c in s]))
print(reduce(lambda a, b: a or b,[c.isalpha() for c in s]))
print(reduce(lambda a, b: a or b,[c.isdigit() for c in s]))
print(reduce(lambda a, b: a or b,[c.islower() for c in s]))
print(reduce(lambda a, b: a or b,[c.isupper() for c in s]))
