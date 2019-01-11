#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Day 8: Dictionaries and Maps

Source : https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem
"""
n = int(input())
book = dict([input().split() for _ in range(n)])
for _ in range(n):
    name = input()
    print("%s=%s" % (name, book[name]) if name in book else "Not found")
