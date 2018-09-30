#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Question 017 (Part 3)

Source: http://www.pythonchallenge.com/pc/return/romance.html

http://www.pythonchallenge.com/pc/return/violin.html
"""

import re
from urllib import (request, parse)

# Part 3
# http://www.pythonchallenge.com/pc/return/violin.html
# no! i mean yes! but ../stuff/violin.php.

url = "http://www.pythonchallenge.com/pc/stuff/violin.php"
msg = "the flowers are on their way"
req = request.Request(url, headers = { "Cookie": "info=" + parse.quote_plus(msg)})
print(request.urlopen(req).read().decode())

# oh well, don't you dare to forget the balloons.
# http://www.pythonchallenge.com/pc/return/balloons.html
