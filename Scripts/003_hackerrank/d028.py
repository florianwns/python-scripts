#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Day 28: RegEx, Patterns, and Intro to Databases

Source : https://www.hackerrank.com/challenges/30-regex-patterns/problem?h_r=next-challenge&h_v=zen
"""
import re

contacts = []
r = re.compile(r"^([a-z]+) ([a-z.]+@gmail.com)$")
for _ in range(int(input())):
    try:
        m = r.search(input())
        contacts.append(m.group(1))
    except:
        pass

print(*sorted(contacts), sep="\n")
