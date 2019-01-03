#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Day 4: Class vs. Instance

Source : https://www.hackerrank.com/challenges/30-class-vs-instance/problem
"""
class Person:
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        if initialAge < 0:
            print("Age is not valid, setting age to 0.")
        self.age = max(0, initialAge)

    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        state = "young" if self.age < 13 else "a teenager" if self.age < 18 else "old"
        print("You are {}.".format(state))


    def yearPasses(self):
        # Increment the age of the person in here
        self.age += 1

t = int(input())
for i in range(0, t):
    age = int(input())
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")
