#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Question 008

Source : http://www.pythonchallenge.com/pc/def/integrity.html

Where is the missing link ?
"""
import bz2

login = bz2.decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')
password = bz2.decompress(b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08')

print(login.decode(), ':', password.decode())

# enter login et password
# http://www.pythonchallenge.com/pc/return/good.html
