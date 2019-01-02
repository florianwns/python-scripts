#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 058

Check Subset

Source : https://www.hackerrank.com/challenges/py-check-subset/problem
"""
a = set(map(int, input().split()))
l = [a > set(map(int, input().split())) for _ in range(int(input()))]
print(all(l))
