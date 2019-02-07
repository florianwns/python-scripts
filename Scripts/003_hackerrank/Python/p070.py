#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 070

Re.findall() & Re.finditer()

Source : https://www.hackerrank.com/challenges/re-findall-re-finditer/problem
"""
import re
v = "aeiou"
c = "qwrtypsdfghjklzxcvbnm"
m = re.findall(r"(?<=[%s])([%s]{2,})[%s]" % (c, v, c), input(), re.I)
print('\n'.join(m or ['-1']))
