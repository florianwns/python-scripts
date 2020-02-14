#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Day 14: Scope

Source : https://www.hackerrank.com/challenges/30-scope/problem
"""
class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        a = self.__elements[1:]
        b = self.__elements[:-1]
        self.maximumDifference = max([abs(i - j) for j in b for i in a])

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()
print(d.maximumDifference)
