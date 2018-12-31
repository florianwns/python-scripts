#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 049

No Idea!

Source : https://www.hackerrank.com/challenges/no-idea/problem
"""
_, ar = [list(map(int, input().split())) for _ in range(2)]
a, b = [set(map(int, input().split())) for _ in range(2)]
print(sum([(i in a) - (i in b) for i in ar]))
