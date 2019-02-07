#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 072

Regex Substitution

Source : https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem
"""
import re
d = {"&&" : "and","||" : "or"}
r = re.compile("(?<=\ )(" + "|".join(map(re.escape, d.keys())) + ")(?=\ )")
for _ in range(int(input())):
    print(r.sub(lambda w: d[w.string[w.start():w.end()]], input()))
