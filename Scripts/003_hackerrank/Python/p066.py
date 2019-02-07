#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 066

Standardize Mobile Number Using Decorators

Source : https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem
"""

#import re
def wrapper(f):
    def fun(l):
        f("+91 {} {}".format(n[-10:-5], n[-5:]) for n in l)
        #f(re.sub(r"^(0|\+?91)?(\d{5})(\d{5})$", r"+91 \2 \3", e) for e in l)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
