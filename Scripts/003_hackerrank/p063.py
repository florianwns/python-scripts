#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 063

Compress the String!

Source : https://www.hackerrank.com/challenges/compress-the-string/problem
"""
from itertools import groupby
print(*[(len(list(g)), int(k)) for k, g in groupby(input())])
