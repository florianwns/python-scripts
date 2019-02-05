#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 092

Map and Lambda Function

Source : https://www.hackerrank.com/challenges/map-and-lambda-expression/problem
"""
cube = lambda x: x**3

def fibonacci(n):
    fib = [0, 1]
    [fib.append(fib[i-1]+fib[i-2]) for i in range(2, n)]
    return fib[0:n]

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
