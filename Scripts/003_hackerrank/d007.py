#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Day 7: Arrays

Source : https://www.hackerrank.com/challenges/30-arrays/problem
"""
n = int(input())
arr = list(map(int, input().split()))
print(*arr[::-1])
