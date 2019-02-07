#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 110

from collections import deque

Source : https://www.hackerrank.com/challenges/py-collections-deque/problem
"""
from collections import deque
d = deque()
for _ in range(int(input())):
    eval("d.{}({})".format(*input().split()+[""]))
print(*d)
