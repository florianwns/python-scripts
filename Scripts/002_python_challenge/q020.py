#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Question 020

Source: http://www.pythonchallenge.com/pc/hex/idiot2.html

go away!
but inspecting it carefully is allowed.
"""

import re
from urllib import request
import base64

url = "http://www.pythonchallenge.com/pc/hex/unreal.jpg"
credentials = base64.b64encode(b'butter:fly').decode()

req = request.Request(url)
req.add_header('Authorization', f'Basic {credentials}')

pattern = re.compile('bytes (\d+)-(\d+)/(\d+)')
pos = (0, 30203, 30237, 30284, 30295, 30313, 2123456744, 2123456743, 1152983631)
for i in pos:
    req.headers['Range'] = f'bytes={i}-'
    with request.urlopen(req) as response:
        message = response.read()
        try:
            message = message.decode()
        except:
            pass
        print(response.headers, message)

with open("assets/level_21.zip", "wb") as f:
    f.write(message)

# password : redavni
