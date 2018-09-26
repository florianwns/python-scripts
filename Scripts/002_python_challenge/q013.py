#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Question 013

Call him
phone that evil

Source: http://www.pythonchallenge.com/pc/return/disproportional.html
        http://www.pythonchallenge.com/pc/phonebook.php

'Bert' is the devil
"""

import xmlrpc.client

with xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php") as proxy:
    # help(proxy)
    try:
        print(proxy.phone("Bert")) # 555-ITALY
    except xmlrpc.client.Fault as err:
        print("A fault occurred")
        print("Fault code: %d" % err.faultCode)
        print("Fault string: %s" % err.faultString)

# the good answer is 'italy'
