#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 084

Re.split()

Source : https://www.hackerrank.com/challenges/re-split/problem
"""
regex_pattern = r"(?<=\d)[,\.]"

import re
print("\n".join(re.split(regex_pattern, input())))
