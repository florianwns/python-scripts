#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fabriquer des formes d'ondes avec numpy
"""
from pyo import *
import numpy as np

s = Server().boot()

# récupère la taille du buffer
bs = s.getBufferSize()

# Crée une table de la longueur du buffer et la lit en boucle
t = DataTable(size=bs)
osc = TableRead(t, freq=t.getRate(), loop=True, mul=1).out()

# Partage la mémoire du tableau avec le numpy array
arr = np.asarray(t.getBuffer())

# Définition des différente formes d'ondes
def sine():
    "Sine wave"
    arr[:] = np.sin(np.linspace(-np.pi, np.pi, bs))

def sawup():
    "Sawtooth up"
    arr[:] = np.linspace(-1, 1, bs)

def sawdown():
    "Sawtooth down"
    arr[:] = np.linspace(1, -1, bs)

def square():
    "Square"
    arr[:] = [1 if i >= 0 else -1 for i in np.linspace(-1, 1, bs) ]

def triangle():
    "Triangle"
    arr[:] =  2 * np.abs(np.linspace(-1, 1, bs)) - 1

# affichage
sp = Spectrum(osc)
sc = Scope(osc)

# appel de la fonction qui crée un triangle
triangle()

# Démarre le serveur
s.start()

s.gui(locals())
