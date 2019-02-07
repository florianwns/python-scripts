#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 089

Lists

Source : https://www.hackerrank.com/challenges/python-lists/problem
"""
l = []
for _ in range(int(input())):
    args = input().split()
    print(l) if "print" in args else eval(f"l.{args[0]}({','.join(args[1:])})")
