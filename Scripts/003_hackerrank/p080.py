#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 080

Mod Divmod

Source : https://www.hackerrank.com/challenges/python-mod-divmod/problem
"""
a, b = (int(input()) for _ in range(2))
print(a//b, a%b, divmod(a,b), sep="\n")
