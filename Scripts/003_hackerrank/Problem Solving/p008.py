#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 008

Mini-Max Sum

Source : https://www.hackerrank.com/challenges/mini-max-sum/problem
"""
l = list(map(int, input().split()))
s = [sum(l[:i]+l[i+1:]) for i in range(len(l))]
print(min(s), max(s))
