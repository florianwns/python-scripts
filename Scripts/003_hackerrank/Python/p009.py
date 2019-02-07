#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 009

Nested Lists

Source : https://www.hackerrank.com/challenges/nested-list/problem
"""
students = []
notes = set()
for _ in range(int(input())):
    name = input()
    note = float(input())
    notes.add(note)
    students.append([name, note])


students = sorted(students, key=lambda x: (x[1], x[0]))
before_last = sorted(notes)[1]

for student in students:
    if student[1] == before_last:
        print(student[0])
