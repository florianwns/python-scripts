#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 014

Repeated String

Source : https://www.hackerrank.com/challenges/repeated-string/problem
"""
s, k = input(), int(input())
l = len(s)
n = k // l
# debut de chaîne non tronquée + fin de la chaîne tronquée
print(s.count("a") * n  + s[:k - l * n].count("a"))
