#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 071

Re.start() & Re.end()

Source : https://www.hackerrank.com/challenges/re-start-re-end/problem
"""
import re
s, p = input(), input()
m = [(m.start(1), m.end(1)-1) for m in re.finditer(r"(?=(%s))" % p, s)]
print(*m if m else [(-1, -1)], sep="\n")
