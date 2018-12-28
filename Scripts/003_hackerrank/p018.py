#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 018

Detect HTML Tags, Attributes and Attribute Values

Source : https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values/problem
"""
from html.parser import HTMLParser

class CustomHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print("-> {} > {}".format(attr[0], attr[1]))

    def handle_startendtag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print("-> {} > {}".format(attr[0], attr[1]))

html = ""
for _ in range(int(input())):
    html += input().rstrip() + "\n"


parser = CustomHTMLParser()
parser.feed(html)
parser.close()
