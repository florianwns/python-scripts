#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Day 19: Interfaces

Source : https://www.hackerrank.com/challenges/30-interfaces/problem?h_r=next-challenge&h_v=zen
"""
class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        return sum([i for i in range(1, n+1) if n % i == 0])

n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented:", type(my_calculator).__bases__[0].__name__)
print(s)
