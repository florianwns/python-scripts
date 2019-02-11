#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 013

Non-Divisible Subset

Source : https://www.hackerrank.com/challenges/non-divisible-subset/problem
"""
from collections import Counter

n, k = map(int, input().split())
cpts = Counter([int(i) % k for i in input().split()])

# pour tout K, la somme des deux valeurs A et B est divisible par K
# seulement si le reste de A/K + B/K = K
total = int(k%2 == 0) + min(cpts[0], 1)
total += sum([max(cpts[i], cpts[k-i]) for i in range(1, k//2+1) if i != k-i])
print(total)
