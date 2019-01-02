#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 059

Check Strict Superset

Source : https://www.hackerrank.com/challenges/py-check-strict-superset/problem
"""
a = set(map(int, input().split()))
l = [a > set(map(int, input().split())) for _ in range(int(input()))]
print(all(l))
