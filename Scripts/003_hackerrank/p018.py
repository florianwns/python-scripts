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
        [print('-> {} > {}'.format(*attr)) for attr in attrs]

html = '\n'.join([input() for _ in range(int(input()))])
parser = CustomHTMLParser()
parser.feed(html)
parser.close()
