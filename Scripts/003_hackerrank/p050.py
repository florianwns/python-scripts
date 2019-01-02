#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 050

Set .add()

Source : https://www.hackerrank.com/challenges/py-set-add/problem
"""
countries = set()
[countries.add(input()) for country in range(int(input()))]
print(len(countries))
