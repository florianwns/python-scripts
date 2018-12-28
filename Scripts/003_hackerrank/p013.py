#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 013

Matrix Script

Source : https://www.hackerrank.com/challenges/matrix-script/problem
"""

import re
from itertools import chain

n, m = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(input())

matrix = list(chain.from_iterable(zip(*matrix)))
line = "".join(matrix)

pattern = r"([a-zA-Z0-9])([!@#$%&\s]+)([a-zA-Z0-9])"
line = re.sub(pattern, r"\1 \3", line)
print(line)
