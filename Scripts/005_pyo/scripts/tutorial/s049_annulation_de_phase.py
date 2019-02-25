#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Annulation de phase
"""
from pyo import *

s = Server()
s.boot().start()

# un première Sinuoïde de 440hz
a = Sine(freq=440).out()

# Deuxième Sinusoïde en annulation de phase
b = Sine(freq=440, phase=0.5).out()

# Résultat des deux Sinusoïdes pour l'affichage
r = a+b

sc = Scope([a, b, r])
sp = Spectrum([a, b, r])

s.gui(locals())
