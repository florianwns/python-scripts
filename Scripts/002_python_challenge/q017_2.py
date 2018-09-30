#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Question 017 (Part 2)

Source: http://www.pythonchallenge.com/pc/return/romance.html

is it the 26th already? call his father and inform him that "the flowers are on their way". he'll understand.

The father of Wolfgang Amadeus Mozart is Leopold Mozart
"""

import xmlrpc.client

with xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php") as proxy:
    try:
        print(proxy.phone("Leopold")) # 555-VIOLIN
    except xmlrpc.client.Fault as err:
        print("A fault occurred")
        print("Fault code: %d" % err.faultCode)
        print("Fault string: %s" % err.faultString)

# http://www.pythonchallenge.com/pc/return/violin.html
