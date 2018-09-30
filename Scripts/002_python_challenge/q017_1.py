#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Question 017 (Part 1)

Source: http://www.pythonchallenge.com/pc/return/romance.html

eat?
a picture of cookie

with cookie inspector : we have this message
"you+should+have+followed+busynothing..."

http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=12345
"""

from urllib import (request, parse)
from http import cookiejar
import bz2
import re

cookie_jar = cookiejar.MozillaCookieJar()
opener = request.build_opener(request.HTTPCookieProcessor(cookie_jar))

site = "http://www.pythonchallenge.com/pc/def/"
opt = "linkedlist.php?busynothing="
nothing = "12345"
cookies = b""

# Part 1
while True:
    with opener.open(site + opt + nothing) as f:
        text = f.read().decode('utf-8')
        print(text)
        for ind, cookie in enumerate(cookie_jar):
            cookies += parse.unquote_to_bytes(cookie.value.replace("+", " "))
        if "the next busynothing is" in text:
            nothing = "".join(re.findall('busynothing is ([0-9]*)', text))
            print("Opening URL:", nothing)
        else:
            break

message = bz2.decompress(cookies).decode()
print(message)

# is it the 26th already? call his father and inform him that "the flowers are on their way". he'll understand.
