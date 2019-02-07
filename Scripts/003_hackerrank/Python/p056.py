#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 056

Set Mutations

Source : https://www.hackerrank.com/challenges/py-set-mutations/problem
"""
n = int(input())
a = set(map(int, input().split()))
for _ in range(int(input())):
    op = input().split()[0]
    b = set(map(int, input().split()))
    eval("a.{}(b)".format(op))
print(sum(a))
