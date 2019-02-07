#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Day 10: Binary Numbers

Source : https://www.hackerrank.com/challenges/30-binary-numbers/problem
"""
print(max(map(len, bin(int(input()))[2:].split("0"))))
