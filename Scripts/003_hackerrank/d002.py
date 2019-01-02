#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Day 2: Operators

Source : https://www.hackerrank.com/challenges/30-operators/problem
"""
# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip = meal_cost * tip_percent / 100
    tax = meal_cost * tax_percent / 100
    price = round(meal_cost + tip + tax)
    print(price)

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
