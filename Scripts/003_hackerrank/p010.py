#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 010

Finding the percentage

Source : https://www.hackerrank.com/challenges/finding-the-percentage/problem
"""

import sys

def debug (msg):
    print(msg, file=sys.stderr)
    return

n = int(input())
student_marks = {}

for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
marks = student_marks[query_name]
avg = sum(marks)/len(marks)
print("{:.2f}".format(avg))
