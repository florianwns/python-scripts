#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 009

Birthday Cake Candles

Source : https://www.hackerrank.com/challenges/birthday-cake-candles/problem
"""
_, height = input(), list(map(int, input().split()))
print(height.count(max(height)))
