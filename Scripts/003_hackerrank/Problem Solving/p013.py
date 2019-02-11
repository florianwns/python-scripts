#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 013

Non-Divisible Subset

Source : https://www.hackerrank.com/challenges/non-divisible-subset/problem
"""
from itertools import combinations
n, k = map(int, input().split())
s = [int(i) % k for i in input().split()]

def GetLengthOfTheLongestNonDivisibleSubset(l, n, k):
    if k == 1:
        return 1

    for i in reversed(range(2, len(l)+1)):
        for c in combinations(l, i):
            # si toutes les sommes sont divisibles par k
            test = True
            for e in combinations(c, 2):
                if (e[0]+e[1]) % k == 0:
                    test = False
                    break
            if test:
                return len(c)
    for i in l:
        if i % k:
            return 1
    return 0

print(GetLengthOfTheLongestNonDivisibleSubset(s, n, k))
