#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 011

Validating Credit Card Numbers

Source : https://www.hackerrank.com/challenges/validating-credit-card-number/problem

---- Valid ----
4253625879615786
4424424424442444
5122-2368-7954-3214

--- Invalid ---
42536258796157867       #17 digits in card number → Invalid
4424444424442444        #Consecutive digits are repeating 4 or more times → Invalid
5122-2368-7954 - 3214   #Separators other than '-' are used → Invalid
44244x4424442444        #Contains non digit characters → Invalid
0525362587961578        #Doesn't start with 4, 5 or 6 → Invalid

"""
import sys
import re

def debug (msg):
    print(msg, file=sys.stderr)
    return

n = int(input())
r1 = re.compile(r'^[456][0-9]{3}-?[0-9]{4}-?[0-9]{4}-?[0-9]{4}$')
r2 = re.compile(r'.*([0-9])\1{3,}')
for _ in range(n):
    line = input()
    check = "Invalid"
    if r1.match(line) and not r2.match(line.replace("-","")):
        check = "Valid"
    print(check)
