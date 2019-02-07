#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 115

Calendar Module

Source : https://www.hackerrank.com/challenges/calendar-module/problem
"""
from calendar import weekday, day_name
m, d, y = map(int, input().split())
print(day_name[weekday(y, m, d)].upper())
