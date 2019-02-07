#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 002

Python If-Else

Source : https://www.hackerrank.com/challenges/py-if-else/problem
"""

n = int(input())

if n>=1 and n<=100:
    if n%2:
        print("Weird")
    else:
        if n>=2 and n<=5:
            print("Not Weird")
        elif n>=6 and n<=20:
            print("Weird")
        elif n>20:
            print("Not Weird")
