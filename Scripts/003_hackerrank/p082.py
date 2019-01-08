#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 082

itertools.combinations_with_replacement()

Source : https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem
"""
from itertools import combinations_with_replacement
s, k = "HACK 2".split()
[print(''.join(c)) for c in combinations_with_replacement(sorted(s), int(k))]
