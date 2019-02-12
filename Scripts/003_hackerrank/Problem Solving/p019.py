#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 019

Breaking the records

Source : https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
"""
_ = input()
scores = list(map(int, input().split()))
score_min = score_max = scores[0]
results = [0, 0]
for score in scores[1:]:
    if score > score_max:
        results[0] += 1
        score_max = score

    if score < score_min:
        results[1] += 1
        score_min = score
print(*results)
