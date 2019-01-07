#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 078

Classes: Dealing with Complex Numbers

Source : https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem
"""
import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        return Complex(self.real + no.real, self.imaginary + no.imaginary)

    def __sub__(self, no):
        return Complex(self.real - no.real, self.imaginary - no.imaginary)

    def __mul__(self, no):
        a, b, c, d = self.real, self.imaginary, no.real, no.imaginary
        r = a*c - d*b
        i = a*d + b*c
        return Complex(r, i)

    def __truediv__(self, no):
        c = Complex(no.real, -no.imaginary)
        n = self * c
        d = no * c
        return Complex(n.real / d.real, n.imaginary / d.real)

    def mod(self):
        return Complex(math.sqrt(self.real**2 + self.imaginary**2), 0)

    def __str__(self):
        return "{0:.2f}{1:+.2f}i".format(self.real,self.imaginary)

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
