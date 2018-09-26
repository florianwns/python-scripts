#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Question 015

Source: http://www.pythonchallenge.com/pc/return/uzi.html

whom?
he ain't the youngest, he is the second
todo: buy flowers for tomorrow
"""

from calendar import datetime
from datetime import timedelta

dates = []
for year in range(0,1900):
    if year%10 == 6:
        date = datetime.datetime(year, 1, 26)
        if "Monday" == date.strftime("%A"):
            dates.append(date)

tomorrow = dates[-2] + timedelta(days=1)
print(tomorrow.strftime("%A %d %B %Y"), "is Mozart's birth day")
