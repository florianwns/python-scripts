#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 015

Apple and Orange

Source : https://www.hackerrank.com/challenges/apple-and-orange/problem
"""
s, t = map(int, input().split())
a, b = map(int, input().split())
_, _ = map(int, input().split())
apples = [a + d for d in map(int, input().split())]
oranges = [b + d for d in map(int, input().split())]
print(sum([1 for d in apples if d >= s and d <= t]))
print(sum([1 for d in oranges if d >= s and d <= t]))
