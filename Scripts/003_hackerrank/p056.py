#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 056

Set Mutations

Source : https://www.hackerrank.com/challenges/py-set-mutations/problem
"""
n = int(input())
a = set(map(int, input().split()))
for _ in range(int(input())):
    args = input().split()
    b = set(map(int, input().split()))
    eval("a.{}({})".format(args[0], b))
print(sum(a))
