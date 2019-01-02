#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 057

The Captain's Room

Source : https://www.hackerrank.com/challenges/py-the-captains-room/problem
"""
from itertools import groupby
k = int(input())
l = sorted(map(int, input().split()))
captain_room = [key for key, value in groupby(l) if len(list(value)) != k][0]
print(captain_room)

# other solution
k = int(input())
l = sorted(map(int, input().split()))
s = set(l)
captain_room = (sum(s) * k - sum(l)) // (k-1)
print(captain_room)
