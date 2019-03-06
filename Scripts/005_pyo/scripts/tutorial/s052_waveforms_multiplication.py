#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Superposition de formes d'ondes
"""
from pyo import *
import numpy as np

s = Server().boot()

f = 440

# Table d'onde Carré avec possibilité de déphasage grâce à l'OSC
t = SquareTable(order=15).normalize()
t.view()
a = Osc(table=t, freq=f, mul=1).out()
a.ctrl()

# Triangle
b = LFO(freq=f, type=3)

# addition
r = a*b
r.out()

# affichage
sp = Spectrum(r)
sc = Scope([a,b,r])

# Démarre le serveur
s.start()

s.gui(locals())
