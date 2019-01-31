#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Day 12: Inheritance

Source : https://www.hackerrank.com/challenges/30-inheritance/problem
"""
class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def __str__(self):
        s = "Name: {}, {}".format(self.lastName, self.firstName)
        s += "\nID: {}".format(self.idNumber)
        return s

class Student(Person):
    GRADES = {'O':90, 'E':80, 'A':70, 'P':55, 'D':40, 'T':0}

    def __init__(self, firstName, lastName, idNumber, scores):
        self.scores = scores
        self.avg = sum(scores) / len(scores)
        self.grade = [g for g, n in self.GRADES.items() if self.avg >= n][0]
        super().__init__(firstName, lastName, idNumber)

    def __str__(self):
        s = super().__str__()
        s += "\nGrade: {}".format(self.grade)
        return s


line = input().split()
numScores = int(input())
scores = list(map(int, input().split()))
s = Student(line[0], line[1], line[2], scores)
print(s)
