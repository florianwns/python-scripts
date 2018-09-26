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
for year in range(1006,1996, 10):
    date = datetime.datetime(year, 1, 26)
    if date.isoweekday() == 1:  # if "Monday" == date.strftime("%A"):
        dates.append(date)

# on prend la deuxième date la plus recente
tomorrow = dates[-2] + timedelta(days=1)
print(tomorrow.strftime("%A %d %B %Y"), "is Mozart's birth day")
