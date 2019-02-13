#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 020

Birthday Chocolate

Source : https://www.hackerrank.com/challenges/the-birthday-bar/problem
"""
_ = input()
squares = list(map(int, input().split()))
d, m = map(int, input().split())
sums = [sum(squares[i:i+m]) for i in range(len(squares)-m+1)]
print(sums.count(d))
