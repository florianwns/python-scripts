#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 090

Tuples

Source : https://www.hackerrank.com/challenges/python-tuples/problem
"""
n, t = int(input()), tuple(map(int, input().split()))
print(hash(t))
