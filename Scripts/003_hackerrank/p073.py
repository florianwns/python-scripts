#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 073

Validating Roman Numerals

Source : https://www.hackerrank.com/challenges/validate-a-roman-number/problem
"""
import re
regex_pattern = r"^(M{0,3})(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
print(str(bool(re.match(regex_pattern, input()))))
