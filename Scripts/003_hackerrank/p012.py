#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 012

Validating Postal Codes

Source : https://www.hackerrank.com/challenges/validating-postalcode/problem
"""

import re

regex_integer_in_range = r"^([1-9]\d{5})$"
regex_alternating_repetitive_digit_pair = r"(?=(\d)\d\1)"

postal_code = input()

print (bool(re.match(regex_integer_in_range, postal_code))
and len(re.findall(regex_alternating_repetitive_digit_pair, postal_code)) < 2)
