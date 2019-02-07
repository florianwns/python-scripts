#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 007

Staircase

Source : https://www.hackerrank.com/challenges/staircase/problem
"""
n = int(input())
[print(("#"*i).rjust(n)) for i in range(1, n+1)]
