#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 098

Exceptions

Source : https://www.hackerrank.com/challenges/exceptions/problem
"""
for _ in range(int(input())):
    try:
        n, d = input().split()
        print(int(n)//int(d))
    except (ValueError, ZeroDivisionError) as e:
        print("Error Code:", e)
