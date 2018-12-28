#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 016

HTML Parser - Part 1

Source : https://www.hackerrank.com/challenges/html-parser-part-1/problem
"""
from html.parser import HTMLParser

class CustomHTMLParser(HTMLParser):
    def handle_comment(self, data):
        type = "Multi-line" if "\n" in data else "Single-line"
        print(">>> {} Comment".format(type))
        print(data)

    def handle_data(self, data):
        if data.strip():
            print(">>> Data")
            print(data)

html = ""
for _ in range(int(input())):
    html += input().rstrip() + "\n"

parser = CustomHTMLParser()
parser.feed(html)
parser.close()
