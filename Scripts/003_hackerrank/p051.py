#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 051

Set .discard(), .remove() & .pop()

Source : https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem
"""
n = int(input())
s = set(map(int, input().split()))
for _ in range(int(input())):
    args = input().split()
    eval("s.{}({})".format(*args+['']))
print(sum(s))
