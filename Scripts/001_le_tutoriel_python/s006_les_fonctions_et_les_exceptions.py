#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Les fonctions et les exceptions

Quelques exemples de fonctions
"""

def ask_ok(prompt, retries=3, reminder='Essayes encore!'):
    while True:
        ok = input(prompt).upper()
        if ok in ('Y', 'YES', 'O', 'OUI'):
            return True
        if ok in ('N', 'NO', 'NON'):
            return False
        retries -= 1
        if retries < 1:
            raise ValueError('Invalid Answer')
        print(reminder)

try:
    if ask_ok('Aimes tu les patates ? => '):
        print('Tu as bien raison ;)')
    else:
        print('C\'est dommage ;(')
except ValueError:
    print('Et alors t\'as pas compris la question ?')
