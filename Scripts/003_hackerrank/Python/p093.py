#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 093

Validating Email Addresses With a Filter

Source : https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem
"""
import re
def fun(s):
    return re.match(r"^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$", s)

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
