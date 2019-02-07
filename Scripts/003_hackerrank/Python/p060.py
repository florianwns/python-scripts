#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 060

Introduction to Sets

Source : https://www.hackerrank.com/challenges/py-introduction-to-sets/problem
"""
def average(array):
    s = set(array)
    return sum(s) / len(s)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
