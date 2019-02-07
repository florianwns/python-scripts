#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 008

Find the Runner-Up Score!

Source : https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
"""

n = int(input())
ar = set(map(int, input().split()))
ar.remove(max(ar))
print(max(ar))
