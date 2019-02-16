#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 023

Day of the Programmer

Source : https://www.hackerrank.com/challenges/day-of-the-programmer/problem
"""
def is_leap(year):
    if year <= 1917:
        return year%4==0
    else:
        return year%4==0 and (year%400==0 or year%100!=0)

d, m, y = "12", "09", int(input())
if y == 1918:
    d = "26"
elif not is_leap(y):
    d = "13"
print(f"{d}.{m}.{y}")
