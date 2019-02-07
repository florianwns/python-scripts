#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 103

itertools.permutations()

Source : https://www.hackerrank.com/challenges/itertools-permutations/problem
"""
from itertools import permutations
a, b = input().split()
print(*sorted(["".join(t) for t in permutations(a, int(b))]), sep="\n")
