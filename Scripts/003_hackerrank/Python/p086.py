#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 086

Collections.namedtuple()

Source : https://www.hackerrank.com/challenges/py-collections-namedtuple/problem
"""
from collections import namedtuple
n, Student = int(input()), namedtuple('Student', input())
marks = [int(Student(*input().split()).MARKS) for _ in range(n)]
print(sum(marks) / len(marks))
