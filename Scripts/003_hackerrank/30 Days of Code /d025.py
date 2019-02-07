#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Day 25: Running Time and Complexity

Source : https://www.hackerrank.com/challenges/30-running-time-and-complexity/problem
"""
def is_prime(n):
    if n <= 3:
        return n > 1
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True

nb = int(input())
[print("Prime" if is_prime(int(input())) else "Not prime") for _ in range(nb)]
