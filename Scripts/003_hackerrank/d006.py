#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Day 6: Let's Review

Source : https://www.hackerrank.com/challenges/30-review-loop/problem
"""
for _ in range(int(input())):
    s = input()
    print(*[s[::2], s[1::2]])
